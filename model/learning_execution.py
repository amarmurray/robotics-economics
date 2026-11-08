"""Funded data, qualification and supported service on the unchanged workcell.

Candidate performance is an explicit hypothesis, never fitted to source papers.
Two persistent opening units share a planning resource and one Treasury. Each
physical window reuses the exact workcell executor; subledgers are partitions,
not additional capital, fleets, customer service or training demonstrations.
"""
from __future__ import annotations
import copy, hashlib, json
from pathlib import Path
from .automotive_workcell import workcell_inputs, validate as validate_workcell, run_workcell
from .treasury import Account, Event, Invoice, Moment, Posting, Treasury

ROOT=Path(__file__).resolve().parents[1]
SCHEMA='learning-execution/0.1'
UNITS=('retained-unit','target-unit')
SOURCES=('model/learning_execution.py','model/automotive_workcell.py','model/treasury.py')


def learning_inputs():
    w=workcell_inputs()
    for i,j in enumerate(w['jobs']):j['variant']='A' if (i//3)%2==0 else 'B'
    return {'cycles':3,'workcell':w,'engineering_hours_per_cycle':24,
        'engineering_cents_per_hour':1000,'support_hours_per_unit':2,
        'priority':'support_first','learning_enabled':True,'candidate_improves':True,
        'transfer_allowed':True,'collection_allowed':True,'training_rights':True,
        'sensor_valid':True,'duplicate_observation_copies':0,
        'minimum_eligible_episodes':12,'collection_batch_size':6,
        'collection_cents_per_episode':100,'training_hours':4,'training_compute_cents':20000,
        'adaptation_hours_per_unit':2,'adaptation_resource_cents_per_unit':5000,
        'qualification_engineering_hours_per_unit':6,'validation_ticks_per_unit_cycle':156,
        'qualification_staff_cents':8000,'target_candidate_changeover_ticks':1,
        'retained_candidate_changeover_ticks':1,'target_min_on_time_kits':12,
        'retained_min_on_time_kits':4,'trial_quality_failure':False,
        'turnaround_capacity_person_ticks_per_unit_cycle':48,
        'turnaround_person_ticks_per_buffered_part':1,'turnaround_cents_per_person_tick':100,
        'module_cost_cents':10000,'module_lead_cycles':0,'module_compatible':True}


def validate(inputs):
    b=learning_inputs()
    if not isinstance(inputs,dict) or set(inputs)!=set(b):raise ValueError('Complete exact learning inputs required')
    x=copy.deepcopy(inputs)
    for k,v in b.items():
        if type(v) is bool:
            if type(x[k]) is not bool:raise ValueError(k+' requires Boolean')
        elif type(v) is int:
            if type(x[k]) is not int or not 0<=x[k]<=1_000_000_000:raise ValueError(k+' requires bounded integer')
    if not 1<=x['cycles']<=6:raise ValueError('Require 1..6 cycles')
    if x['priority'] not in ('support_first','candidate_first'):raise ValueError('Unknown allocation priority')
    for k in ('collection_batch_size','minimum_eligible_episodes','training_hours',
              'adaptation_hours_per_unit','qualification_engineering_hours_per_unit','support_hours_per_unit'):
        if not 1<=x[k]<=1000:raise ValueError(k+' requires 1..1000')
    if x['engineering_hours_per_cycle']>1000 or x['duplicate_observation_copies']>5 or x['module_lead_cycles']>6:
        raise ValueError('Resource, duplicate or lead bound exceeded')
    for k in ('target_candidate_changeover_ticks','retained_candidate_changeover_ticks','validation_ticks_per_unit_cycle'):
        if x[k]>1000:raise ValueError('Workcell tick bound exceeded')
    w=validate_workcell(x['workcell']);x['workcell']=w
    if w['replacement'] is not None or w['prepared_presentation'] or w['config']['kind']!='fixed':
        raise ValueError('This feedback contract uses two opening fixed units without replacement/preparation')
    if any(len(j['job_id'])>8 or any(len(p)>12 for p in j['part_ids']) for j in w['jobs']):
        raise ValueError('Short source IDs required for unique physical-window namespacing')
    if any(x[k]>len(w['jobs']) for k in ('target_min_on_time_kits','retained_min_on_time_kits')):
        raise ValueError('Qualification criterion exceeds available test jobs')
    # Integer costs remain exactly representable in the browser and Treasury.
    if x['engineering_cents_per_hour']*1000>1_000_000_000:raise ValueError('Engineering charge exceeds bound')
    return x


class _Execution:
    def __init__(self,x):
        self.x=x;self.transaction=0;self.cycle=0;self.used=0
        self.t=Treasury(tuple(Account(a,x['workcell']['opening_cash_cents'] if a=='operator' else 0)
            for a in ('operator','staff','resources','preparation','equipment','rd_resources')))
        self.opening=self.t.snapshot();self.charges=[];self.allocations=[];self.events=[]
        self.windows=[];self.episodes=[];self.training_ids=[];self.built=False
        self.turnarounds=[];self.turnaround_used={u:0 for u in UNITS}
        self.physical_state={u:{'last_window_id':None,'variant':x['workcell']['config']['initial_variant'],
            'buffered_component_ids':[],'quarantined_component_ids':[]} for u in UNITS}
        self.states={u:{'unit_id':u,'opening_config_id':u+'-v1','active_config_id':u+'-v1',
            'baseline_setup_funded':False,
            'adapted':False,'module_order_cycle':None,'module_ready_cycle':None,
            'qualification_status':'not_attempted','qualified_cycle':None,
            'production_active':False,'trial_window_id':None} for u in UNITS}
        self.months=[]

    def pay(self,category,amount,payee='rd_resources',conditional=True,stage=None,tick=None):
        self.transaction+=1;iid=f'L{self.transaction}-{category}'
        a,b=Moment(self.transaction,1),Moment(self.transaction,2)
        if amount:
            self.t=self.t.issue_invoice('issue-'+iid,iid,'operator',payee,amount,a,b,b,
                provenance='synthetic_learning_execution',cancellable=conditional,category=category)
            candidate=self.t.settle_invoice('pay-'+iid,iid,b,provenance='synthetic_learning_execution')
            paid=candidate.invoice(iid).outstanding_cents==0
            self.t=candidate if paid or not conditional else self.t.cancel_invoice('cancel-'+iid,iid,b,provenance='unfunded_work_not_started')
        else:paid=True
        self.charges.append({'cycle':self.cycle,'stage':stage,'tick':tick,'category':category,
            'payee':payee,'requested_cents':amount,'paid_cents':amount if paid else 0,
            'funded':paid,'conditional':conditional,'invoice_id':iid if amount else None})
        return paid

    def book(self,kind,hours,other_cents=0,unit=None):
        if self.used+hours>self.x['engineering_hours_per_cycle']:
            self.events.append({'cycle':self.cycle,'kind':kind,'unit_id':unit,'status':'engineering_deferred'})
            return False
        charge=hours*self.x['engineering_cents_per_hour']+other_cents
        if not self.pay(kind,charge,stage=unit):return False
        self.allocations.append({'cycle':self.cycle,'kind':kind,'unit_id':unit,
            'hours':hours,'engineering_cash_cents':hours*self.x['engineering_cents_per_hour'],
            'other_resource_cash_cents':other_cents,'paid_cents':charge})
        self.used+=hours
        return True

    def physical(self,unit,kind,config,supported=True):
        """Replay workcell funding in order into the shared immutable Treasury."""
        w=copy.deepcopy(self.x['workcell']);stage=f'C{self.cycle}-{unit}-{kind}'
        w['opening_cash_cents']=self.t.balance('operator');w['config']=copy.deepcopy(config)
        baseline=kind=='production' and not self.states[unit]['production_active']
        w['startup_cents']=w['startup_cents'] if baseline and not self.states[unit]['baseline_setup_funded'] else 0
        if kind=='qualification':
            w['staff_cents']=self.x['qualification_staff_cents']
            w['quality_fail_first_job_ids']=[w['jobs'][min(3,len(w['jobs'])-1)]['job_id']] if self.x['trial_quality_failure'] else []
        state=self.physical_state[unit]
        reset_ticks=(len(state['buffered_component_ids'])*self.x['turnaround_person_ticks_per_buffered_part']+
            (config['changeover_ticks'] if state['variant']!=config['initial_variant'] else 0)) if state['last_window_id'] else 0
        reset_ok=self.turnaround_used[unit]+reset_ticks<=self.x['turnaround_capacity_person_ticks_per_unit_cycle']
        if reset_ok:reset_ok=self.pay('window_turnaround',reset_ticks*self.x['turnaround_cents_per_person_tick'],
            'resources',stage=stage+'-turnaround')
        self.turnarounds.append({'cycle':self.cycle,'unit_id':unit,'next_window_id':stage,
            'prior_window_id':state['last_window_id'],'prior_variant':state['variant'],'next_initial_variant':config['initial_variant'],
            'buffered_component_ids':list(state['buffered_component_ids']),
            'person_ticks_required':reset_ticks,'performed':reset_ok})
        if reset_ok:
            self.turnaround_used[unit]+=reset_ticks
            state['quarantined_component_ids']+=state['buffered_component_ids'];state['buffered_component_ids']=[]
            state['variant']=config['initial_variant']
        if not supported or not reset_ok:w['config']['support_until_tick']=0
        # Distinct held-out and service components: trials never supply training IDs.
        mapping={j['job_id']:stage+'-'+j['job_id'] for j in w['jobs']}
        w['quality_fail_first_job_ids']=[mapping[i] for i in w['quality_fail_first_job_ids']]
        for j in w['jobs']:
            j['job_id']=mapping[j['job_id']];j['part_ids']=[stage+'-'+p for p in j['part_ids']]
        w['opening_cash_cents']=self.t.balance('operator')
        r=run_workcell(w)
        if baseline and next(f for f in r['funding'] if f['kind']=='startup_configuration')['funded']:
            self.states[unit]['baseline_setup_funded']=True
        ledger=r['closing_treasury'];invoices={i['invoice_id']:i for i in ledger['invoices']}
        before={a.actor_id:self.t.balance(a.actor_id) for a in self.t.accounts}
        # Append an already executed, audited physical cash partition once. Its
        # opening operator balance is exact; no new account/opening cash is added.
        # Namespace identities and shift transaction moments without changing
        # postings, obligations, cancellations, funding order or amounts.
        assert not any(ledger[k] for k in ('deposits','credits','reservations'))
        offset=self.transaction
        def moment(m):return Moment(offset+m['month'],m['phase'])
        appended_invoices=[];appended_events=[]
        for source in ledger['invoices']:
            i={k:v for k,v in source.items() if k not in ('outstanding_cents','status')}
            i['invoice_id']=stage+':'+i['invoice_id']
            for k in ('issued_at','eligible_at','due_at'):i[k]=moment(i[k])
            appended_invoices.append(Invoice(**i))
        for source in ledger['events']:
            e=dict(source);e['event_id']=stage+':'+e['event_id'];e['reference_id']=stage+':'+e['reference_id']
            e['at']=moment(e['at']);e['postings']=tuple(Posting(**p) for p in e['postings'])
            assert not e['reservation_uses'];appended_events.append(Event(**e))
        self.t=Treasury(self.t.accounts,self.t.invoices+tuple(appended_invoices),
            self.t.reservations,self.t.deposits,self.t.credits,self.t.events+tuple(appended_events))
        self.transaction=offset+max((e['at']['month'] for e in ledger['events']),default=0)
        for f in r['funding']:
            inv=invoices.get(f['invoice_id']);payee=inv['payee'] if inv else 'resources'
            self.charges.append({'cycle':self.cycle,'stage':stage,'tick':f['tick'],'category':f['kind'],
                'payee':payee,'requested_cents':f['requested_cents'],
                'paid_cents':f['requested_cents'] if f['funded'] else 0,'funded':f['funded'],
                'conditional':f['conditional'],'invoice_id':stage+':'+f['invoice_id'] if inv else None})
        for a in r['closing_treasury']['actors']:
            expected=a['cash_cents']-(w['opening_cash_cents'] if a['actor_id']=='operator' else 0)
            assert self.t.balance(a['actor_id'])-before[a['actor_id']]==expected,'Cash partition mismatch'
        if reset_ok:
            state['last_window_id']=stage
            for e in r['events']:
                if e['event']=='zero_duration_recipe_switch' or e['event']=='finish' and e['kind']=='changeover':state['variant']=e['variant']
            state['buffered_component_ids']=[p['part_id'] for p in r['components'] if p['state']=='buffer']
        projection={k:v for k,v in r.items() if k not in ('opening_treasury','closing_treasury')}
        row={'window_id':stage,'cycle':self.cycle,'unit_id':unit,'kind':kind,
            'physical_unit_alias':{'opening-resource':unit},
            'cash_partition':'Physical funding is in the shared Treasury with window-prefixed identities; replay complete physical inputs for the executor subledger and case hash.',
            'physical':projection}
        self.windows.append(row)
        return row

    def cfg(self,unit,candidate=False):
        c=copy.deepcopy(self.x['workcell']['config'])
        c['config_id']=unit+('-candidate-v2' if candidate else '-v1')
        if candidate and self.x['candidate_improves']:
            c['changeover_ticks']=self.x['retained_candidate_changeover_ticks' if unit=='retained-unit' else 'target_candidate_changeover_ticks']
        return c

    def candidate(self):
        x=self.x
        if not x['learning_enabled']:return
        eligible=[e['episode_id'] for e in self.episodes if e['eligible'] and e['cycle']<self.cycle]
        if not self.built:
            if len(eligible)<x['minimum_eligible_episodes']:
                self.events.append({'cycle':self.cycle,'kind':'training','status':'insufficient_eligible_episodes','eligible_count':len(eligible)})
                return
            if not self.book('candidate_training',x['training_hours'],x['training_compute_cents']):return
            self.built=True;self.training_ids=eligible
            self.events.append({'cycle':self.cycle,'kind':'candidate_built','training_episode_ids':eligible,
                'performance_basis':'explicit input hypothesis, not learned or inferred from data count'})
        for unit in ('target-unit','retained-unit'):
            s=self.states[unit]
            if unit=='retained-unit' and (not x['transfer_allowed'] or self.states['target-unit']['qualification_status']!='passed'):continue
            if s['qualification_status']!='not_attempted':continue
            if s['module_order_cycle'] is None:
                if not self.pay('compatible_module_order',x['module_cost_cents'],'equipment',stage=unit):continue
                s['module_order_cycle']=self.cycle;s['module_ready_cycle']=self.cycle+x['module_lead_cycles']
                self.events.append({'cycle':self.cycle,'kind':'module_ordered','unit_id':unit,'ready_cycle':s['module_ready_cycle']})
            if self.cycle<s['module_ready_cycle']:
                self.events.append({'cycle':self.cycle,'kind':'qualification','unit_id':unit,'status':'awaiting_delivery'})
                continue
            if not x['module_compatible']:
                self.events.append({'cycle':self.cycle,'kind':'qualification','unit_id':unit,'status':'delivered_module_incompatible'})
                continue
            if not s['adapted']:
                if not self.book('unit_adaptation',x['adaptation_hours_per_unit'],x['adaptation_resource_cents_per_unit'],unit):continue
                s['adapted']=True
            if x['validation_ticks_per_unit_cycle']<x['workcell']['horizon_ticks']:
                self.events.append({'cycle':self.cycle,'kind':'qualification','unit_id':unit,'status':'physical_validation_slot_unavailable'})
                continue
            if not self.book('held_out_qualification',x['qualification_engineering_hours_per_unit'],unit=unit):continue
            r=self.physical(unit,'qualification',self.cfg(unit,True));s['trial_window_id']=r['window_id']
            summary=r['physical']['summary'];minimum=x['target_min_on_time_kits' if unit=='target-unit' else 'retained_min_on_time_kits']
            passed=summary['on_time_kits']>=minimum and summary['undelivered_kits']==0 and summary['due_unpaid_cents']==0
            s['qualification_status']='passed' if passed else 'failed'
            if passed:
                s['qualified_cycle']=self.cycle;s['active_config_id']=unit+'-candidate-v2';s['production_active']=True
            self.events.append({'cycle':self.cycle,'kind':'qualification_result','unit_id':unit,'status':s['qualification_status'],
                'observed_on_time_kits':summary['on_time_kits'],'minimum_on_time_kits':minimum,
                'window_id':r['window_id'],'retained_prior_config_on_failure':not passed})

    def collect(self,windows):
        x=self.x
        if not x['collection_allowed']:return
        records=[]
        for w in windows:
            counts={};r=w['physical']
            for e in r['events']:
                if e['event']!='finish' or e['kind'] not in ('handoff','direct'):continue
                jid=e['job_id'];counts[jid]=counts.get(jid,0)+1
                eid=jid+'-attempt-'+str(counts[jid])
                record={'episode_id':eid,'cycle':self.cycle,'unit_id':w['unit_id'],
                    'source_window_id':w['window_id'],'configuration_id':e['config_id'],
                    'job_id':jid,'attempt':counts[jid],'sensor_valid':x['sensor_valid'],
                    'training_rights':x['training_rights'],'eligible':x['sensor_valid'] and x['training_rights'],
                    'accepted_attempt':not any(z['event']=='quality_rejected' and z['job_id']==jid and z['tick']==e['end_tick'] for z in r['events'])}
                records.extend([record]*(1+x['duplicate_observation_copies']))
        unique={r['episode_id']:r for r in records}
        existing={e['episode_id'] for e in self.episodes};pending=[e for k,e in unique.items() if k not in existing]
        collected=0
        for start in range(0,len(pending),x['collection_batch_size']):
            batch=pending[start:start+x['collection_batch_size']]
            if not self.book('episode_collection',1,len(batch)*x['collection_cents_per_episode']):break
            self.episodes.extend(batch);collected+=len(batch)
        self.events.append({'cycle':self.cycle,'kind':'episode_observation','observed_records':len(records),
            'unique_attempts':len(unique),'duplicates_ignored':len(records)-len(unique),'collected':collected,
            'not_collected':len(pending)-collected,'held_out_episodes_included':0})

    def run(self):
        for cycle in range(self.x['cycles']):
            self.cycle=cycle;self.used=0;self.turnaround_used={u:0 for u in UNITS};supported={u:False for u in UNITS}
            def support():
                for unit in UNITS:supported[unit]=self.book('installed_support',self.x['support_hours_per_unit'],unit=unit)
            if self.x['priority']=='support_first':support();self.candidate()
            else:self.candidate();support()
            windows=[]
            for unit in UNITS:
                windows.append(self.physical(unit,'production',self.cfg(unit,self.states[unit]['production_active']),supported[unit]))
            self.collect(windows)
            self.months.append({'cycle':cycle,'engineering_hours_used':self.used,
                'engineering_hours_available':self.x['engineering_hours_per_cycle'],'supported':supported,
                'turnaround_person_ticks':dict(self.turnaround_used),
                'qualified_configurations':{u:self.states[u]['active_config_id'] for u in UNITS},
                'production_window_ids':[w['window_id'] for w in windows],
                'on_time_kits':sum(w['physical']['summary']['on_time_kits'] for w in windows),
                'collected_unique_episodes':len(self.episodes),'eligible_unique_episodes':sum(e['eligible'] for e in self.episodes),
                'closing_operator_cash_cents':self.t.balance('operator')})
        self.t.audit()
        production=[w for w in self.windows if w['kind']=='production'];trials=[w for w in self.windows if w['kind']=='qualification']
        total=lambda rows,key:sum(w['physical']['summary'][key] for w in rows)
        summary={'due_service_kits':total(production,'due_kits'),'on_time_service_kits':total(production,'on_time_kits'),
            'late_service_kits':total(production,'late_kits'),'undelivered_service_kits':total(production,'undelivered_kits'),
            'qualification_attempts':len(trials),'qualification_on_time_kits':total(trials,'on_time_kits'),
            'candidate_built':self.built,'qualified_units':sum(s['production_active'] for s in self.states.values()),
            'robot_units_owned':len(UNITS),'modules_ordered':sum(s['module_order_cycle'] is not None for s in self.states.values()),
            'modules_delivered':sum(s['module_ready_cycle'] is not None and s['module_ready_cycle']<self.x['cycles'] for s in self.states.values()),
            'unique_collected_episodes':len(self.episodes),'unique_eligible_episodes':sum(e['eligible'] for e in self.episodes),
            'training_episode_uses':len(self.training_ids),'collection_cash_cents':sum(c['paid_cents'] for c in self.charges if c['category']=='episode_collection'),
            'training_cash_cents':sum(c['paid_cents'] for c in self.charges if c['category']=='candidate_training'),
            'production_staff_cash_cents':total(production,'paid_staff_cents'),
            'qualification_staff_cash_cents':total(trials,'paid_staff_cents'),
            'engineering_hours_used':sum(r['hours'] for r in self.allocations),
            'turnaround_person_ticks':sum(t['person_ticks_required'] for t in self.turnarounds if t['performed']),
            'turnaround_cash_cents':sum(c['paid_cents'] for c in self.charges if c['category']=='window_turnaround'),
            'unsupported_unit_cycles':sum(not v for m in self.months for v in m['supported'].values()),
            'operator_outlay_cents':self.x['workcell']['opening_cash_cents']-self.t.balance('operator'),
            'due_unpaid_cents':sum(i.outstanding_cents for i in self.t.invoices),'removed_payroll_cents':None}
        assert summary['due_service_kits']==summary['on_time_service_kits']+summary['late_service_kits']+summary['undelivered_service_kits']
        assert len({e['episode_id'] for e in self.episodes})==len(self.episodes)
        assert all(m['engineering_hours_used']<=m['engineering_hours_available'] for m in self.months)
        assert all('-production-' in i for i in self.training_ids)
        result={'schema_version':SCHEMA,'status':'synthetic_qualified_feedback_not_model_training_or_empirical_learning_rate',
            'inputs':self.x,'summary':summary,'cycles':self.months,'assets':list(self.states.values()),
            'engineering_allocations':self.allocations,'episodes':self.episodes,'training_episode_ids':self.training_ids,
            'events':self.events,'charges':self.charges,'physical_windows':self.windows,
            'turnarounds':self.turnarounds,'closing_physical_state':self.physical_state,
            'opening_treasury':self.opening,'closing_treasury':self.t.snapshot(),
            'source_sha256':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in SOURCES},
            'evidence_role':{'references':['LEC-005','LEC-006','LEC-007','LEC-008'],'numerical_calibration':False},
            'boundary':'Two persistent opening units. Each cycle allocates finite planning engineering, reserves per-unit held-out physical windows, then executes two separate production windows and paid episode collection. A cycle is a planning/production batch, not a calendar month. Treasury month is transaction order. Physical subledgers are partitions of one cash account, not additional capital or fleet. Validation is extra physical work in a declared preproduction slot and never customer service/training data. No continuous-time plant schedule, external model run, empirical learning curve, market price, financing return or payroll reduction is inferred.'}
        result['case_hash']=hashlib.sha256(json.dumps(result,sort_keys=True,separators=(',',':'),allow_nan=False).encode()).hexdigest()
        return result


def run_learning(inputs):return _Execution(validate(inputs)).run()


def run_learning_case(overrides=None):
    o={} if overrides is None else overrides;x=learning_inputs()
    if not isinstance(o,dict) or set(o)-set(x):raise ValueError('Unknown learning shortcut')
    x.update(copy.deepcopy(o));return run_learning(x)


def replay_learning(saved):
    if not isinstance(saved,dict) or saved.get('schema_version')!=SCHEMA or not isinstance(saved.get('inputs'),dict):
        raise ValueError('Complete saved learning inputs required')
    return run_learning(saved['inputs'])


def learning_artifact():
    conventional=learning_inputs()['workcell'];conventional['config']['changeover_ticks']=1
    cases={'qualified_feedback':{},'no_research':{'learning_enabled':False},
        'no_learning':{'candidate_improves':False},'no_transfer':{'transfer_allowed':False},
        'no_training_rights':{'training_rights':False},'invalid_observations':{'sensor_valid':False},
        'duplicate_observations':{'duplicate_observation_copies':2},
        'retained_regression':{'retained_candidate_changeover_ticks':20},
        'failed_target_quality':{'trial_quality_failure':True},
        'support_priority':{'engineering_hours_per_cycle':20},
        'candidate_priority':{'engineering_hours_per_cycle':20,'priority':'candidate_first'},
        'validation_slot_short':{'validation_ticks_per_unit_cycle':155},
        'delayed_module':{'module_lead_cycles':1},'module_after_horizon':{'module_lead_cycles':4},
        'incompatible_module':{'module_compatible':False},
        'conventional_fast_retool':{'workcell':conventional,'learning_enabled':False}}
    values={k:run_learning_case(v) for k,v in cases.items()}
    return {'schema_version':SCHEMA,'challenge_ids':['DE-CF09','DE-CF14'],'partial_mechanisms':['DE-CF10'],
        'case_inputs':cases,'cases':values,'summary':[{'case':k,**r['summary']} for k,r in values.items()],
        'comparison_boundary':'Matched unique service kits across two persistent units; candidate quality is a disclosed hypothesis. Endogenous eligible-data, paid qualification, delivered compatible modules and adaptive finite support admission gate actual service. Conventional fast retool is an already-qualified alternative, not a free implementation claim. No product ROI or calibrated training effect.'}


def learning_catalog():
    """Serve a current exported reference plus small presets; replay edits on demand."""
    path=ROOT/'model/results/learning_execution.json'
    if not path.exists():raise ValueError('Generate the learning execution export first')
    d=json.loads(path.read_text());r=d['cases']['qualified_feedback']
    if r['source_sha256']!={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in SOURCES}:
        raise ValueError('Learning execution export has stale source hashes; regenerate')
    return {k:v for k,v in d.items() if k!='cases'}|{'cases':{'qualified_feedback':r}}
