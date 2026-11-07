"""Exact conventional planning over a bounded, observed synthetic request queue.

No model, ROS, network or robot calls. The clock advances during proposal latency.
Planning only sees observed work; a shared funded executor admits every policy.
"""
from __future__ import annotations
from dataclasses import asdict,dataclass
from functools import lru_cache
import hashlib,json
from pathlib import Path
from model.treasury import Account,Moment,Treasury

ROOT=Path(__file__).resolve().parents[1]
RESOURCES=('courier','robot')
MAX_STATES=300_000


def integer(value,minimum=0,maximum=1_000_000):
    if type(value) is not int or not minimum<=value<=maximum:raise ValueError('Bounded exact integer required')


@dataclass(frozen=True)
class Mode:
    mode_id:str
    duration:int
    claims:tuple[tuple[str,int,int],...]
    resource_cents:int
    def __post_init__(self):
        if not isinstance(self.mode_id,str) or not self.mode_id:raise ValueError('Mode identity required')
        integer(self.duration,1,12);integer(self.resource_cents)
        claims=tuple(tuple(x) for x in self.claims);object.__setattr__(self,'claims',claims)
        if not claims:raise ValueError('Execution needs a resource claim')
        occupied={r:0 for r in RESOURCES}
        for resource,offset,length in claims:
            if resource not in RESOURCES:raise ValueError('Unknown resource')
            integer(offset,0,12);integer(length,1,12)
            if offset+length>self.duration:raise ValueError('Resource claim outside mode duration')
            mask=((1<<length)-1)<<offset
            if occupied[resource]&mask:raise ValueError('Overlapping within-mode resource claims')
            occupied[resource]|=mask


@dataclass(frozen=True)
class Request:
    request_id:str
    release:int
    deadline:int
    mandatory:bool
    modes:tuple[Mode,...]
    def __post_init__(self):
        if not isinstance(self.request_id,str) or not self.request_id:raise ValueError('Request identity required')
        integer(self.release,0,11);integer(self.deadline,1,12)
        if self.deadline<=self.release or type(self.mandatory) is not bool:raise ValueError('Invalid service window/priority')
        object.__setattr__(self,'modes',tuple(self.modes))
        if not self.modes or len(self.modes)>2 or any(not isinstance(m,Mode) for m in self.modes):raise ValueError('One or two explicit modes required')
        if len({m.mode_id for m in self.modes})!=len(self.modes):raise ValueError('Duplicate mode identity')


@dataclass(frozen=True)
class Outage:
    tick:int
    until:int
    recovery_cents:int=500
    def __post_init__(self):
        integer(self.tick,0,11);integer(self.until,1,12);integer(self.recovery_cents)
        if self.until<=self.tick:raise ValueError('Outage return must follow observation')


@dataclass(frozen=True)
class Workload:
    requests:tuple[Request,...]
    horizon:int=12
    tick_minutes:int=5
    robot_available:bool=True
    urgent_courier_reserve:tuple[int,int]=(2,4)
    opening_cash_cents:int=30_000
    paid_staff_shift_cents:int=12_000
    robot_support_cents:int=2_000
    integration_allocation_cents:int=500
    outage:Outage|None=None
    def __post_init__(self):
        object.__setattr__(self,'requests',tuple(self.requests))
        object.__setattr__(self,'urgent_courier_reserve',tuple(self.urgent_courier_reserve))
        integer(self.horizon,1,12);integer(self.tick_minutes,1,60)
        for name in ('opening_cash_cents','paid_staff_shift_cents','robot_support_cents','integration_allocation_cents'):integer(getattr(self,name))
        if type(self.robot_available) is not bool:raise ValueError('Explicit robot availability premise required')
        if not 1<=len(self.requests)<=6 or any(not isinstance(r,Request) for r in self.requests):raise ValueError('One to six explicit requests required')
        if len({r.request_id for r in self.requests})!=len(self.requests):raise ValueError('Duplicate business request identity')
        if any(r.deadline>self.horizon for r in self.requests):raise ValueError('Deadline outside declared horizon')
        a,b=self.urgent_courier_reserve;integer(a,0,self.horizon);integer(b,0,self.horizon)
        if b<a:raise ValueError('Invalid standby interval')
        if self.outage is not None and (not isinstance(self.outage,Outage) or self.outage.until>self.horizon):raise ValueError('Invalid observed outage')


@dataclass(frozen=True)
class Controller:
    label:str='exact_conventional'
    latency_ticks:int=0
    planning_cents_per_slot:int=10
    verification_cents_per_slot:int=5
    urgent_fast_path:bool=False
    fixed_proposals:dict|None=None
    def __post_init__(self):
        if not isinstance(self.label,str) or not self.label:raise ValueError('Controller label required')
        integer(self.latency_ticks,0,3);integer(self.planning_cents_per_slot);integer(self.verification_cents_per_slot)
        if type(self.urgent_fast_path) is not bool:raise ValueError('Explicit fast-path Boolean required')
        if self.fixed_proposals is not None and not isinstance(self.fixed_proposals,dict):raise ValueError('Fixed proposals must be an object')


def claim_masks(mode,start):
    return tuple(sum((((1<<length)-1)<<(start+offset)) for resource,offset,length in mode['claims'] if resource==r) for r in RESOURCES)


def allowed(request,mode,start,snapshot,occupied,cash):
    if type(start) is not int or start<max(snapshot['tick'],request['release']):return False
    if start+mode['duration']>min(request['deadline'],snapshot['horizon']) or mode['resource_cents']>cash:return False
    masks=claim_masks(mode,start)
    if any(a&b for a,b in zip(masks,occupied)):return False
    if not request['mandatory'] and masks[0]&snapshot['urgent_reserve_mask']:return False
    return True


def exact_plan(snapshot,earliest=None):
    """Exhaust all feasible schedules of the observed queue; no future input."""
    requests=tuple(sorted(snapshot['pending'],key=lambda r:r['request_id']))
    earliest=snapshot['tick'] if earliest is None else earliest
    integer(earliest,0,15)
    visited=0
    @lru_cache(None)
    def solve(index,occupied,cash):
        nonlocal visited
        visited+=1
        if visited>MAX_STATES:raise ValueError('Exact planning state budget exceeded; no optimality claim returned')
        if index==len(requests):return (0,0,0,0),()
        request=requests[index];best=solve(index+1,occupied,cash)
        for mode in request['modes']:
            for start in range(max(earliest,request['release']),min(request['deadline'],snapshot['horizon'])-mode['duration']+1):
                if not allowed(request,mode,start,snapshot,occupied,cash):continue
                masks=claim_masks(mode,start)
                later,actions=solve(index+1,tuple(a|b for a,b in zip(occupied,masks)),cash-mode['resource_cents'])
                gain=(int(request['mandatory']),1,-mode['resource_cents'],-(start+mode['duration']))
                score=tuple(a+b for a,b in zip(later,gain))
                action=(start,request['request_id'],mode['mode_id'])
                candidate=(score,tuple(sorted((action,*actions))))
                if candidate[0]>best[0] or (candidate[0]==best[0] and candidate[1]<best[1]):best=candidate
        return best
    score,actions=solve(0,tuple(snapshot['occupied_masks']),snapshot['available_cash_cents'])
    return {'objective':list(score),'actions':[{'start':t,'request_id':r,'mode_id':m} for t,r,m in actions],
            'states_visited':visited,'optimality_scope':'exact_for_this_observed_queue_and_declared_resources',
            'observed_request_ids':[r['request_id'] for r in requests]}


def verify_actions(actions,snapshot):
    """Common all-or-nothing executor guard; proposals confer no authority."""
    if not isinstance(actions,list):return 'proposal_not_a_list',[]
    by_id={r['request_id']:r for r in snapshot['pending']};seen=set();occupied=tuple(snapshot['occupied_masks']);cash=snapshot['available_cash_cents'];resolved=[]
    for action in actions:
        if not isinstance(action,dict) or set(action)!={'start','request_id','mode_id'}:return 'invalid_action_schema',[]
        rid=action['request_id']
        if not isinstance(rid,str) or not isinstance(action['mode_id'],str):return 'invalid_action_identity',[]
        if rid in seen:return 'duplicate_request_in_proposal',[]
        seen.add(rid)
        if rid not in by_id:return 'request_not_observed_pending',[]
        if action['start']!=snapshot['tick']:return 'not_current_execution_tick',[]
        request=by_id[rid];mode=next((m for m in request['modes'] if m['mode_id']==action['mode_id']),None)
        if mode is None:return 'mode_not_eligible',[]
        if not allowed(request,mode,action['start'],snapshot,occupied,cash):return 'deadline_resource_reserve_or_cash_constraint',[]
        masks=claim_masks(mode,action['start']);occupied=tuple(a|b for a,b in zip(occupied,masks));cash-=mode['resource_cents']
        resolved.append((request,mode,masks))
    return '',resolved


def run_coordination(workload,controller=Controller()):
    if not isinstance(workload,Workload) or not isinstance(controller,Controller):raise ValueError('Explicit workload and controller required')
    w=workload;h=w.horizon
    treasury=Treasury((Account('service_operator',w.opening_cash_cents),Account('resource_supplier',0)))
    costs=[];events=[];observations=[];proposals=[];admissions=[]
    states={r.request_id:{'status':'unreleased','attempts':0} for r in w.requests}
    jobs={r.request_id:asdict(r) for r in w.requests}
    occupied=[0,0];running={};pending_packets=[];accepted={};failed=[];next_attempt=0
    reserve=((1<<(w.urgent_courier_reserve[1]-w.urgent_courier_reserve[0]))-1)<<w.urgent_courier_reserve[0]
    robot_block=0 if w.robot_available else (1<<h)-1
    def pay(tick,phase,category,amount,tag):
        nonlocal treasury
        iid=f'coordination:{tick}:{category}:{tag}'
        ledger_period=len(costs)
        if amount:
            treasury=treasury.issue_invoice(iid+':issue',iid,'service_operator','resource_supplier',amount,
                Moment(ledger_period,1),Moment(ledger_period,2),Moment(ledger_period,2),provenance='synthetic_coordination_window',cancellable=True,category=category)
            treasury=treasury.settle_invoice(iid+':pay',iid,Moment(ledger_period,2),provenance='synthetic_coordination_window')
            paid=treasury.invoice(iid).paid_cents
            if paid!=amount:treasury=treasury.cancel_invoice(iid+':cancel',iid,Moment(ledger_period,2),provenance='synthetic_coordination_window')
        else:paid=0
        costs.append({'tick':tick,'phase':phase,'ledger_period':ledger_period,'invoice_id':iid if amount else None,'category':category,'amount_cents':amount,'paid_cents':paid,'tag':tag})
        return paid==amount
    setup=[('paid_staff_shift',w.paid_staff_shift_cents),('robot_support',w.robot_support_cents if w.robot_available else 0),
           ('integration_allocation',w.integration_allocation_cents),('planning_capacity',h*controller.planning_cents_per_slot),
           ('verification_capacity',h*controller.verification_cents_per_slot)]
    ready=True
    for category,amount in setup:ready=pay(0,1,category,amount,'window') and ready
    def snapshot(tick,exclude_inflight=False):
        masks=[occupied[0],occupied[1]|robot_block]
        inflight=set();tentative_cash=treasury.available('service_operator') if ready else 0
        if exclude_inflight:
            # Local proposal reservations confer no execution authority. Malformed,
            # stale or now-infeasible packets reserve nothing and are rejected on arrival.
            for packet in sorted(pending_packets,key=lambda p:(p['arrival'],p['id'])):
                future={'tick':packet['arrival'],'horizon':h,'urgent_reserve_mask':reserve,
                    'occupied_masks':masks,'available_cash_cents':tentative_cash,
                    'pending':[jobs[rid] for rid,state in states.items() if state['status']=='pending' and rid not in inflight]}
                reason,resolved=verify_actions(packet['actions'],future)
                if reason:continue
                for request,mode,claims in resolved:
                    inflight.add(request['request_id']);masks=[a|b for a,b in zip(masks,claims)]
                    tentative_cash-=mode['resource_cents']
        return {'tick':tick,'horizon':h,'urgent_reserve_mask':reserve,'occupied_masks':masks,
            'available_cash_cents':tentative_cash,
            'pending':[jobs[rid] for rid,state in states.items() if state['status']=='pending' and (not exclude_inflight or rid not in inflight)],
            'funded_execution_ready':ready,'inflight_request_ids':sorted(inflight) if exclude_inflight else []}
    def execute(tick,packet):
        nonlocal occupied,next_attempt
        current=snapshot(tick);reason,resolved=verify_actions(packet['actions'],current)
        if not ready:reason='unfunded_required_window_capacity';resolved=[]
        if reason:
            admissions.append({'tick':tick,'proposal_id':packet['id'],'status':'rejected','reason':reason,'actions':packet['actions']});return
        amount=sum(mode['resource_cents'] for _,mode,_ in resolved)
        if not pay(tick,5,'attempt_resources',amount,packet['id']):raise AssertionError('Verified cash changed before atomic commit')
        for request,mode,masks in resolved:
            rid=request['request_id'];next_attempt+=1;aid=f'attempt-{next_attempt}'
            occupied=[a|b for a,b in zip(occupied,masks)]
            states[rid].update(status='running',attempts=states[rid]['attempts']+1)
            running[rid]={'attempt_id':aid,'request_id':rid,'mode_id':mode['mode_id'],'start':tick,
                          'finish':tick+mode['duration'],'claims':list(masks),'resource_cents':mode['resource_cents']}
            events.append({'tick':tick,'kind':'started',**running[rid]})
        admissions.append({'tick':tick,'proposal_id':packet['id'],'status':'admitted','reason':'','actions':packet['actions'],'committed_attempt_cents':amount})
    for tick in range(h+1):
        if w.outage and w.outage.tick==tick and w.robot_available:
            restored=pay(tick,2,'outage_recovery',w.outage.recovery_cents,'robot')
            until=w.outage.until if restored else h
            robot_block|=((1<<(until-tick))-1)<<tick
            events.append({'tick':tick,'kind':'observed_robot_outage','unavailable_until':until,'recovery_paid':restored,'authoritative_stop_assumed':True})
            future_mask=((1<<h)-1)^((1<<tick)-1)
            for rid,active in list(running.items()):
                if active['claims'][1]&(1<<tick):
                    states[rid]['status']='failed';failed.append({**active,'failed_at':tick,'reason':'observed_outage','partial_work_preserved':True,'accepted_service':0})
                    occupied=[a&~(claim&future_mask) for a,claim in zip(occupied,active['claims'])]
                    del running[rid]
        for rid,active in list(running.items()):
            if active['finish']==tick:
                assert rid not in accepted and tick<=jobs[rid]['deadline']
                states[rid]['status']='accepted';accepted[rid]={'request_id':rid,'attempt_id':active['attempt_id'],'completion_tick':tick,'mandatory':jobs[rid]['mandatory']}
                events.append({'tick':tick,'kind':'authoritative_accepted_completion',**accepted[rid]});del running[rid]
        for rid,job in jobs.items():
            if states[rid]['status']=='unreleased' and job['release']<=tick:states[rid]['status']='pending'
        arriving=[p for p in pending_packets if p['arrival']==tick];pending_packets=[p for p in pending_packets if p['arrival']!=tick]
        for packet in arriving:execute(tick,packet)
        if tick==h:break
        if controller.urgent_fast_path:
            obs=snapshot(tick,True);obs['pending']=[r for r in obs['pending'] if r['mandatory']]
            if obs['pending'] and ready:
                plan=exact_plan(obs);actions=[a for a in plan['actions'] if a['start']==tick]
                packet={'id':f'fast-{tick}','as_of':tick,'arrival':tick,'actions':actions,'kind':'conventional_urgent_fast_path'}
                proposals.append({**packet,'plan':plan});execute(tick,packet)
        obs=snapshot(tick,True);observations.append(obs)
        arrival=tick+controller.latency_ticks
        if controller.fixed_proposals is None:
            plan=exact_plan(obs,arrival) if ready else {'objective':[0,0,0,0],'actions':[],'states_visited':0,'optimality_scope':'window_not_funded','observed_request_ids':[]}
            actions=[a for a in plan['actions'] if a['start']==arrival]
        else:
            plan=None;actions=controller.fixed_proposals.get(str(tick),[])
        packet={'id':f'proposal-{tick}','as_of':tick,'arrival':arrival,'actions':actions,'kind':'synthetic_proposal' if controller.label!='exact_conventional' else 'conventional_plan'}
        proposals.append({**packet,'plan':plan})
        if arrival==tick:execute(tick,packet)
        elif arrival<=h:pending_packets.append(packet)
    for state in states.values():
        if state['status']=='pending':state['status']='missed_deadline'
    result={'schema_version':'conventional-coordination/0.1','evidence_status':'synthetic_bounded_request_and_resource_contract',
        'workload':asdict(w),'controller':asdict(controller),'source_sha256':source_hashes(),
        'service_unit':'one uniquely accepted synthetic item request, complete by its declared deadline',
        'clock':'Service uses integer ticks of tick_minutes. Treasury Moment.month is a monotonically ordered transaction index; cost_lines link each payment to its service tick. No financial-month or interest conversion is made.',
        'observations':observations,'proposals':proposals,'admissions':admissions,'events':events,
        'request_states':states,'accepted_requests':list(accepted.values()),'failed_attempts':failed,'running_at_horizon':list(running.values()),
        'opening_cash_cents':w.opening_cash_cents,'closing_treasury':treasury.snapshot(),'cost_lines':costs,
        'summary':{'requested':len(jobs),'accepted':len(accepted),'mandatory_requested':sum(r['mandatory'] for r in jobs.values()),
            'mandatory_accepted':sum(r['mandatory'] for r in accepted.values()),'mandatory_service_gate_met':all(rid in accepted for rid,j in jobs.items() if j['mandatory']),
            'attempts_started':next_attempt,'failed_attempts':len(failed),'paid_resource_cents':sum(c['paid_cents'] for c in costs),
            'paid_staff_cents':sum(c['paid_cents'] for c in costs if c['category']=='paid_staff_shift'),
            'all_attempt_cash_per_accepted_request':{'numerator':sum(c['paid_cents'] for c in costs),'denominator':len(accepted)} if accepted else None,
            'controller_calls':len(proposals),'declared_decision_slots':h,'unfunded_required_capacity':not ready},
        'limits':['No observed hospital duration, price, quality or payroll coefficient; no clinical prioritization recommendation',
            'Exact scheduling only for currently observed requests and stated interval resources; no clairvoyant future events or real travel dynamics',
            'Mode durations include stated loading/handoff claims; paid service staffing is retained and no labor expense is charged twice',
            'Planning/verification bills book window capacity, including the optional conventional urgent fast path; they are assumptions, not measured CPU/model costs',
            'No LLM, model API, RMF installation, robot experiment or physical service evaluation is executed',
            'Outage has a cooperative authoritative-stop and recovery-duration assumption; failed work is not reversed or retried automatically',
            'Proposal revalidation and unique local intent do not establish distributed durability or actual installation authority',
            'Tentative local in-flight proposals reserve declared resources and cash for planning only; execution rechecks actual state and cash',
            'Required window capacities are booked sequentially; prior paid bookings remain if a later required booking is unfunded',
            'Existing assets and full lifecycle economics remain outside this service-window cash boundary; no annual/monthly conversion is inferred']}
    assert len(accepted)==len(set(accepted)) and sum(a['cash_cents'] for a in result['closing_treasury']['actors'])==w.opening_cash_cents
    result['case_hash']=hashlib.sha256(json.dumps(result,sort_keys=True,separators=(',',':')).encode()).hexdigest()
    return json.loads(json.dumps(result))


def source_hashes():
    return {p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in ('model/conventional_coordination.py','model/treasury.py')}


def restore_workload(raw):
    if not isinstance(raw,dict) or not isinstance(raw.get('requests'),list):raise ValueError('Complete workload object with requests required')
    value=dict(raw);value['requests']=tuple(Request(**{**r,'modes':tuple(Mode(**m) for m in r['modes'])}) for r in value['requests'])
    if value.get('outage') is not None:value['outage']=Outage(**value['outage'])
    return Workload(**value)


def replay_coordination(saved):
    if not isinstance(saved,dict) or saved.get('schema_version')!='conventional-coordination/0.1':raise ValueError('Saved conventional coordination case required')
    return run_coordination_inputs({'workload':saved.get('workload'),'controller':saved.get('controller')})


def run_coordination_inputs(inputs):
    if not isinstance(inputs,dict) or set(inputs)!={'workload','controller'} or not isinstance(inputs['controller'],dict):
        raise ValueError('Complete workload and controller inputs required')
    try:return run_coordination(restore_workload(inputs['workload']),Controller(**inputs['controller']))
    except (KeyError,AttributeError) as exc:raise ValueError('Incomplete workload or controller inputs') from exc


def reference_workload():
    human=Mode('human',3,(('courier',0,3),),100)
    robot=Mode('robot',4,(('courier',0,1),('robot',0,4),('courier',3,1)),150)
    urgent=Mode('human_urgent',2,(('courier',0,2),),100)
    return Workload((Request('routine-A',0,6,False,(human,robot)),Request('routine-B',0,9,False,(human,robot)),
                     Request('routine-C',0,12,False,(human,robot)),Request('routine-D',4,12,False,(human,robot)),
                     Request('urgent-E',2,4,True,(urgent,)),Request('routine-F',6,12,False,(human,robot))))


def coordination_artifact():
    from dataclasses import replace
    base=reference_workload();exact=Controller()
    duplicate={'start':1,'request_id':'routine-A','mode_id':'robot'}
    worlds={
        'mixed_exact':(base,exact),
        'human_only_exact':(replace(base,robot_available=False),exact),
        'no_urgent_reserve':(replace(base,urgent_courier_reserve=(0,0)),exact),
        'observed_robot_outage':(replace(base,outage=Outage(3,6)),exact),
        'matched_proposal_alias':(base,replace(exact,label='synthetic_proposal_alias')),
        'delayed_proposal':(base,replace(exact,label='synthetic_delayed_proposal',latency_ticks=1)),
        'delayed_with_urgent_fast_path':(base,replace(exact,label='synthetic_delayed_proposal',latency_ticks=1,urgent_fast_path=True)),
        'extra_proposal_overhead':(base,replace(exact,label='synthetic_extra_overhead',planning_cents_per_slot=110)),
        'limited_execution_cash':(replace(base,opening_cash_cents=15000),exact),
        'unfunded_window':(replace(base,opening_cash_cents=12000),exact),
        'duplicate_and_malformed_guard':(base,replace(exact,label='fixed_adversarial_proposals',fixed_proposals={
            '0':[{'start':0,'request_id':[],'mode_id':'human'}],
            '1':[duplicate,duplicate],
            '2':[{'start':2,'request_id':'urgent-E','mode_id':'human_urgent'}],
            '4':[{'start':4,'request_id':'unobserved-X','mode_id':'human'}]})),
        'delayed_stale_outage_guard':(replace(base,outage=Outage(1,4)),replace(exact,label='fixed_stale_proposal',latency_ticks=1,
            fixed_proposals={'0':[duplicate]})),
    }
    cases={name:run_coordination(w,c) for name,(w,c) in worlds.items()}
    return {'schema_version':'conventional-coordination-artifact/0.1','evidence_status':'synthetic_bounded_service_window',
        'cases':cases,'summary':[{'case':name,**result['summary']} for name,result in cases.items()],
        'comparison_boundary':'Same declared workload and funded executor. Exactness applies only to each observed queue. Proposal aliases use the same solver with explicit latency/cost; no LLM performance is measured. Mandatory service is a separate gate, paid staff remains, and window cash excludes asset lifecycle economics.'}
