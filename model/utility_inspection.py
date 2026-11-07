"""Synthetic accepted-point inspection windows with funded residual human visits.

No source number calibrates these assumptions. Reuses the immutable Treasury;
its month index is a transaction sequence here, not a calendar month.
"""
from __future__ import annotations
import copy
import hashlib
import json
from pathlib import Path
from .treasury import Account, Moment, Treasury

ROOT=Path(__file__).resolve().parents[1]
SCHEMA='utility-inspection/0.1'
POINTS=[f'P{i:02}' for i in range(1,13)]
SOURCES=('model/utility_inspection.py','model/treasury.py')
ACTORS=('utility','monitor_provider','field_crew','review_staff','technical_resources','travel_resources')


def _hash(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(',',':'),allow_nan=False).encode()).hexdigest()


def _int(v,name,lo=0,hi=100_000_000):
    if type(v) is not int or not lo<=v<=hi:raise ValueError(f'{name} requires integer {lo}..{hi}')
    return v


def _bool(v,name):
    if type(v) is not bool:raise ValueError(name+' requires Boolean')


def _set(v,name,allowed):
    if not isinstance(v,list) or any(type(x) is not type(next(iter(allowed))) for x in v) or len(v)!=len(set(v)) or not set(v)<=set(allowed):
        raise ValueError(name+' requires unique allowed identities')


def inspection_inputs():
    def channel(name,coverage):
        mobile=name=='mobile'
        return {'channel_id':name,'enabled':mobile,'coverage_ids':coverage,'qualified_ids':POINTS[:],
                'bad_quality_ids':[],'capture_minute':10,'repeats':1,
                'initial_fee_cents':20000 if mobile else 10000,'cycle_fee_cents':6000 if mobile else 3000,
                'initial_resource_cents':15000 if mobile else 8000,
                'cycle_resource_cents':2000 if mobile else 1000,'attempt_resource_cents':100 if mobile else 50,
                'support_person_minutes':10 if mobile else 5}
    return {'cycles':4,'required_points':POINTS[:],'decision_minute':60,'deadline_minute':180,
            'replacement_authorized':True,'mandatory_visit_cycles':[],'field_duty_cycles':[],
            'field_duty_person_minutes':20,'crew_size':2,'travel_elapsed_minutes':40,'setup_elapsed_minutes':10,
            'point_elapsed_minutes':2,'field_capacity_person_minutes':180,'staffing':'committed',
            'fixed_staff_cents':25000,'visit_crew_cents':30000,'travel_cents':2000,
            'review_capacity_person_minutes':30,'review_minutes_per_observation':2,'review_commitment_cents':3000,
            'utility_cash_cents':1000000,'provider_cash_cents':0,
            'channels':[channel('fixed',POINTS[:8]),channel('mobile',POINTS[:11])]}


def validate(x):
    base=inspection_inputs()
    if not isinstance(x,dict) or set(x)!=set(base):raise ValueError('Complete exact inspection input keys required')
    _int(x['cycles'],'cycles',1,12)
    p=x['required_points']
    if not isinstance(p,list) or not 1<=len(p)<=40 or any(not isinstance(i,str) or not i or len(i)>40 for i in p) or len(p)!=len(set(p)):
        raise ValueError('Required point identities must be unique nonempty strings (1..40)')
    _bool(x['replacement_authorized'],'replacement_authorized')
    for k in ('mandatory_visit_cycles','field_duty_cycles'):_set(x[k],k,list(range(x['cycles'])))
    for k in ('decision_minute','deadline_minute','field_duty_person_minutes','travel_elapsed_minutes','setup_elapsed_minutes','point_elapsed_minutes','field_capacity_person_minutes','review_capacity_person_minutes','review_minutes_per_observation'):
        _int(x[k],k,1 if k in ('deadline_minute','review_minutes_per_observation') else 0,10000)
    if x['decision_minute']>x['deadline_minute']:raise ValueError('Decision cutoff must precede deadline')
    _int(x['crew_size'],'crew_size',1,10)
    for k in ('fixed_staff_cents','visit_crew_cents','travel_cents','review_commitment_cents','utility_cash_cents','provider_cash_cents'):_int(x[k],k)
    if x['staffing'] not in ('committed','per_visit'):raise ValueError('Unknown staffing contract')
    if not isinstance(x['channels'],list) or len(x['channels'])!=2 or [c.get('channel_id') for c in x['channels'] if isinstance(c,dict)]!=['fixed','mobile']:
        raise ValueError('Fixed and mobile channel records required in declared order')
    for c,b in zip(x['channels'],base['channels']):
        if set(c)!=set(b):raise ValueError('Unexpected channel fields')
        _bool(c['enabled'],'channel enabled')
        for k in ('coverage_ids','qualified_ids','bad_quality_ids'):_set(c[k],k,p)
        _int(c['capture_minute'],'capture_minute',0,10000);_int(c['repeats'],'repeats',1,5)
        for k in ('initial_fee_cents','cycle_fee_cents','initial_resource_cents','cycle_resource_cents','attempt_resource_cents','support_person_minutes'):_int(c[k],k)
    return copy.deepcopy(x)


def run_inspection(inputs):
    x=validate(inputs);required=set(x['required_points']);enabled=[c for c in x['channels'] if c['enabled']]
    t=Treasury(tuple(Account(a,x['utility_cash_cents'] if a=='utility' else x['provider_cash_cents'] if a=='monitor_provider' else 0) for a in ACTORS))
    opening=t.snapshot();transaction=0;funding=[];rows=[];initialized=set()

    def pay(items,cycle,kind,conditional=False):
        """Atomic paid resource batches. Committed bills survive failed funding."""
        nonlocal t,transaction
        items=[(a,b,c) for a,b,c in items if c];transaction+=1
        start,finish=Moment(transaction,1),Moment(transaction,2)
        candidate=t;ids=[]
        for n,(payer,payee,amount) in enumerate(items):
            iid=f'c{cycle}-{kind}-{transaction}-{n}';ids.append(iid)
            candidate=candidate.issue_invoice('issue-'+iid,iid,payer,payee,amount,start,finish,finish,
                provenance='synthetic_inspection_window',cancellable=conditional,category=kind)
        issued=candidate
        for iid in ids:candidate=candidate.settle_invoice('pay-'+iid,iid,finish,provenance='synthetic_inspection_window')
        ok=all(candidate.invoice(iid).outstanding_cents==0 for iid in ids)
        if ok:t=candidate
        elif conditional:
            t=issued
            for iid in ids:t=t.cancel_invoice('cancel-'+iid,iid,finish,provenance='unfunded_conditional_service_not_started')
        else:t=candidate  # Single-party committed bill; its unpaid obligation persists.
        funding.append({'cycle':cycle,'kind':kind,'requested_cents':sum(v for _,_,v in items),'funded':ok,'conditional':conditional,'invoice_ids':ids})
        return ok

    for cycle in range(x['cycles']):
        before_cash={a:t.balance(a) for a in ACTORS}
        staff_ok=pay([('utility','field_crew',x['fixed_staff_cents'])],cycle,'committed_staff') if x['staffing']=='committed' else True
        review_ok=pay([('utility','review_staff',x['review_commitment_cents'])],cycle,'review_commitment') if enabled else False
        observations=[];support=0;channel_rows=[]
        for c in enabled:
            name=c['channel_id'];n=len(c['coverage_ids'])*c['repeats']
            fee=c['cycle_fee_cents']+(c['initial_fee_cents'] if cycle==0 else 0)
            fee_ok=pay([('utility','monitor_provider',fee)],cycle,name+'_fee')
            resource=c['cycle_resource_cents']+n*c['attempt_resource_cents']+(c['initial_resource_cents'] if name not in initialized else 0)
            resource_ok=pay([('monitor_provider','technical_resources',resource)],cycle,name+'_resources',True) if fee_ok else False
            channel_rows.append({'channel_id':name,'fee_funded':fee_ok,'resource_funded':resource_ok,'planned_captures':n,'resource_request_cents':resource})
            if not resource_ok:continue
            initialized.add(name);support+=c['support_person_minutes']
            for point in c['coverage_ids']:
                for repeat in range(c['repeats']):
                    observations.append({'observation_id':f'{cycle}-{name}-{point}-{repeat}','cycle':cycle,'point_id':point,
                        'channel_id':name,'captured_minute':c['capture_minute'],'qualified':point in c['qualified_ids'],
                        'quality_pass':point not in c['bad_quality_ids']})
        # First accepted reading removes duplicate review, while failed assessment still uses time.
        accepted={};review_used=0;review_clock=0
        for o in sorted(observations,key=lambda a:(a['captured_minute'],a['observation_id'])):
            key=o['point_id'];status='';finish=None
            if key in accepted:status='duplicate_of_accepted_point'
            elif not o['qualified']:status='unqualified_configuration'
            elif not review_ok:status='review_not_funded'
            elif review_used+x['review_minutes_per_observation']>x['review_capacity_person_minutes']:status='review_capacity_exhausted'
            elif max(review_clock,o['captured_minute'])+x['review_minutes_per_observation']>x['decision_minute']:status='missed_review_cutoff'
            else:
                review_used+=x['review_minutes_per_observation'];review_clock=max(review_clock,o['captured_minute'])+x['review_minutes_per_observation'];finish=review_clock
                status='accepted' if o['quality_pass'] else 'quality_rejected'
                if status=='accepted':accepted[key]={'point_id':key,'channel':o['channel_id'],'observation_id':o['observation_id'],'accepted_minute':finish}
            o['status']=status;o['review_finished_minute']=finish
        remote_ids=sorted(accepted);residual=sorted(required-set(accepted));duty=cycle in x['field_duty_cycles']
        policy_visit=cycle in x['mandatory_visit_cycles'] or not x['replacement_authorized']
        needs_visit=bool(residual) or duty or policy_visit
        person=(x['travel_elapsed_minutes']+x['setup_elapsed_minutes']+len(residual)*x['point_elapsed_minutes'])*x['crew_size']+(x['field_duty_person_minutes'] if duty else 0)
        # No remote channel: the competent human route begins at window opening.
        start=x['decision_minute'] if enabled else 0
        elapsed_base=x['travel_elapsed_minutes']+x['setup_elapsed_minutes']+len(residual)*x['point_elapsed_minutes']
        finish_numerator=(start+elapsed_base)*x['crew_size']+(x['field_duty_person_minutes'] if duty else 0)
        reason='no_visit_needed';visited=False
        if needs_visit:
            reason='unfunded_committed_staff' if not staff_ok else 'field_capacity_exhausted' if person>x['field_capacity_person_minutes'] else 'fallback_misses_deadline' if finish_numerator>x['deadline_minute']*x['crew_size'] else ''
            if not reason:
                bills=[('utility','travel_resources',x['travel_cents'])]
                if x['staffing']=='per_visit':bills.append(('utility','field_crew',x['visit_crew_cents']))
                visited=pay(bills,cycle,'visit_resources',True)
                reason='visit_completed' if visited else 'visit_cash_insufficient'
            if visited:
                for key in residual:accepted[key]={'point_id':key,'channel':'human','accepted_minute_numerator':finish_numerator,'accepted_minute_denominator':x['crew_size']}
        remaining=sorted(required-set(accepted));service_complete=not remaining and (not duty or visited) and (not policy_visit or visited)
        rows.append({'cycle':cycle,'required_point_ids':x['required_points'],'channels':channel_rows,'observations':observations,
            'remote_accepted_point_ids':remote_ids,'residual_before_visit':residual,'visit_needed':needs_visit,'visit_completed':visited,'visit_reason':reason,
            'field_duty_required':duty,'field_duty_completed':duty and visited,'policy_visit_required':policy_visit,
            'field_person_minutes':person if visited else 0,'field_person_minutes_requested':person if needs_visit else 0,
            'purchased_field_capacity_person_minutes':x['field_capacity_person_minutes'] if x['staffing']=='committed' and staff_ok else person if visited else 0,
            'review_person_minutes':review_used,'support_person_minutes':support,'accepted_points':[accepted[k] for k in sorted(accepted)],
            'unaccepted_point_ids':remaining,'service_complete':service_complete,'operator_outlay_cents':before_cash['utility']-t.balance('utility'),
            'closing_cash_cents':{a:t.balance(a) for a in ACTORS},'due_unpaid_cents':sum(i.outstanding_cents for i in t.invoices)})
    t.audit();closing=t.snapshot();external=sum(t.balance(a) for a in ACTORS[2:])
    summary={'cycles':x['cycles'],'required_point_windows':len(required)*x['cycles'],
        'raw_captures':sum(len(r['observations']) for r in rows),'remote_accepted_point_windows':sum(len(r['remote_accepted_point_ids']) for r in rows),
        'accepted_point_windows':sum(len(r['accepted_points']) for r in rows),'unaccepted_point_windows':sum(len(r['unaccepted_point_ids']) for r in rows),
        'complete_service_windows':sum(r['service_complete'] for r in rows),'visits_required':sum(r['visit_needed'] for r in rows),'visits_completed':sum(r['visit_completed'] for r in rows),
        'field_person_minutes':sum(r['field_person_minutes'] for r in rows),'review_person_minutes':sum(r['review_person_minutes'] for r in rows),
        'support_person_minutes':sum(r['support_person_minutes'] for r in rows),'paid_field_crew_cents':t.balance('field_crew'),
        'operator_outlay_cents':x['utility_cash_cents']-t.balance('utility'),'provider_net_cash_change_cents':t.balance('monitor_provider')-x['provider_cash_cents'],
        'internal_monitor_fees_cents':sum(i.paid_cents for i in t.invoices if i.payer=='utility' and i.payee=='monitor_provider'),
        'external_resource_cash_cents':external,'due_unpaid_cents':sum(i.outstanding_cents for i in t.invoices)}
    summary['executed_person_minutes']=sum(summary[k] for k in ('field_person_minutes','review_person_minutes','support_person_minutes'))
    assert summary['accepted_point_windows']+summary['unaccepted_point_windows']==summary['required_point_windows']
    assert summary['operator_outlay_cents']-summary['provider_net_cash_change_cents']==external
    result={'schema_version':SCHEMA,'status':'synthetic_service_boundary_not_empirical_economics','inputs':x,
        'service_unit':'one complete due-window measurement set with accepted quality/review, plus separately recorded required field duty or presence',
        'timing':'Each cycle is a separate synthetic inspection window; Treasury month stores transaction index, not calendar months. No carryover of missed service.',
        'source_sha256':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in SOURCES},
        'evidence_role':{'references':['QOF-E01','QOF-E03','QOF-E09','QOF-E10','QOF-E11'],'numerical_calibration':False,'logic':'Evidence motivates qualification, coverage, review and residual duties; every numerical input is synthetic.'},
        'opening_treasury':opening,'closing_treasury':closing,'funding':funding,'cycles':rows,'summary':summary,
        'boundary':'Operator and monitor provider are inside. Fees cancel on consolidation; staff, review, travel and technical-resource payments cross outward once. Window resource bills exclude full asset lifecycle, financing, taxes, damage and avoided outage value. Human time used and paid capacity are separate.'}
    result['case_hash']=_hash(result)
    return result


def run_inspection_case(overrides=None):
    x=inspection_inputs();o={} if overrides is None else overrides
    allowed={'mode','staffing','mobile_points','fixed_points','review_capacity_person_minutes','field_duty','replacement_authorized','utility_cash_cents','provider_cash_cents','visit_crew_cents','mobile_bad_last_point','mobile_unqualified_last_point','mobile_repeats','deadline_minute','mobile_resource_cents'}
    if not isinstance(o,dict) or set(o)-allowed:raise ValueError('Unknown inspection shortcut input')
    mode=o.get('mode','mobile')
    if mode not in ('human','fixed','mobile','mixed'):raise ValueError('Unknown inspection mode')
    for c in x['channels']:c['enabled']=mode==c['channel_id'] or mode=='mixed'
    for k in ('staffing','review_capacity_person_minutes','replacement_authorized','utility_cash_cents','provider_cash_cents','visit_crew_cents','deadline_minute'):
        if k in o:x[k]=o[k]
    fixed,mobile=x['channels']
    for key,c in (('fixed_points',fixed),('mobile_points',mobile)):
        if key in o:_int(o[key],key,0,len(POINTS));c['coverage_ids']=POINTS[:o[key]]
    for k in ('field_duty','mobile_bad_last_point','mobile_unqualified_last_point'):
        if k in o:_bool(o[k],k)
    if o.get('field_duty'):x['field_duty_cycles']=list(range(x['cycles']))
    if o.get('mobile_bad_last_point'):mobile['bad_quality_ids']=[POINTS[-1]]
    if o.get('mobile_unqualified_last_point'):mobile['qualified_ids']=POINTS[:-1]
    if 'mobile_repeats' in o:mobile['repeats']=o['mobile_repeats']
    if 'mobile_resource_cents' in o:mobile['cycle_resource_cents']=o['mobile_resource_cents']
    return run_inspection(x)


def replay_inspection(saved):
    if not isinstance(saved,dict) or saved.get('schema_version')!=SCHEMA or not isinstance(saved.get('inputs'),dict):raise ValueError('Complete saved inspection inputs required')
    return run_inspection(saved['inputs'])


def inspection_artifact():
    shortcuts={
        'human_committed':{'mode':'human'},'human_per_visit':{'mode':'human','staffing':'per_visit'},
        'human_field_duty':{'mode':'human','field_duty':True,'staffing':'per_visit'},
        'mobile_residual':{},'mobile_complete_committed':{'mobile_points':12},
        'mobile_complete_avoidable':{'mobile_points':12,'staffing':'per_visit'},
        'fixed_partial':{'mode':'fixed'},'fixed_complete_avoidable':{'mode':'fixed','fixed_points':12,'staffing':'per_visit'},
        'mixed_overlap_residual':{'mode':'mixed'},
        'one_bad_reading':{'mobile_points':12,'mobile_bad_last_point':True,'staffing':'per_visit'},
        'review_bottleneck':{'mobile_points':12,'review_capacity_person_minutes':23,'staffing':'per_visit'},
        'field_duty_remains':{'mobile_points':12,'field_duty':True,'staffing':'per_visit'},
        'replacement_not_authorized':{'mobile_points':12,'replacement_authorized':False,'staffing':'per_visit'},
        'provider_resource_shortfall':{'mobile_points':12,'mobile_resource_cents':100000},
        'fallback_late':{'mobile_points':12,'mobile_bad_last_point':True,'deadline_minute':90},
        'duplicate_captures':{'mobile_points':12,'mobile_repeats':2},
        'unqualified_last_point':{'mobile_points':12,'mobile_unqualified_last_point':True,'staffing':'per_visit'}
    }
    cases={k:run_inspection_case(v) for k,v in shortcuts.items()}
    mixed=inspection_inputs();mixed['staffing']='per_visit'
    for c in mixed['channels']:c['enabled']=True
    mixed['channels'][1]['coverage_ids']=POINTS[6:]
    cases['mixed_complementary']=run_inspection(mixed)
    return {'schema_version':SCHEMA,'challenge_id':'DE-CF03','case_inputs':shortcuts,'cases':cases,
        'summary':[{'case':k,**v['summary']} for k,v in cases.items()],
        'comparison_boundary':'Common twelve-point measurement obligation and four due windows; technology coverage, quality, staffing contract or timing changes are explicit. Match complete service before comparing cash. Paid commitments and field duties can remain after full remote coverage; no real product ranking or lifecycle ROI.'}
