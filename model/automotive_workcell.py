"""Bounded physical workcell: unique parts, one manipulator, buffer and due kits.

All numerical assumptions are synthetic. No empirical cycle/ROI calibration.
"""
from __future__ import annotations
import copy,hashlib,json
from pathlib import Path
from .treasury import Account,Moment,Treasury
ROOT=Path(__file__).resolve().parents[1]
SCHEMA='automotive-workcell/0.1'
SOURCES=('model/automotive_workcell.py','model/treasury.py')


def _int(v,k,lo=0,hi=1_000_000_000):
 if type(v) is not int or not lo<=v<=hi:raise ValueError(f'{k} requires integer {lo}..{hi}')


def _bool(v,k):
 if type(v) is not bool:raise ValueError(k+' requires Boolean')


def _config(kind='fixed',suffix='v1'):
 return {'config_id':kind+'-'+suffix,'kind':kind,'pick_ticks':1 if kind=='human' else 2 if kind=='fixed' else 3,'handoff_ticks':3,
         'changeover_ticks':12 if kind=='fixed' else 1 if kind=='humanoid' else 0,
         'rework_ticks':4,'qualified_variants':['A','B'],'initial_variant':'A','support_until_tick':1000,
         'operation_cents_per_tick':100,'inspection_person_ticks':1}


def workcell_inputs():
 jobs=[{'job_id':f'J{i+1:02}','variant':'A','part_ids':[f'J{i+1:02}-P{j+1}' for j in range(3)],
        'supply_tick':0,'release_tick':12+(i+1)*12-6,'due_tick':12+(i+1)*12} for i in range(12)]
 return {'tick_seconds':5,'horizon_ticks':156,'jobs':jobs,'buffer_capacity':6,'source_closed_intervals':[],
         'config':_config(),'startup_cents':20000,'staff_cents':50000,'staff_capacity_person_ticks':156,
         'opening_cash_cents':1000000,'quality_fail_first_job_ids':[],
         'prepared_presentation':False,'preparation_ticks_per_part':2,'preparation_capacity_person_ticks':72,
         'preparation_setup_cents':10000,'preparation_cents_per_part':100,'replacement':None}


def validate(x):
 b=workcell_inputs()
 if not isinstance(x,dict) or set(x)!=set(b):raise ValueError('Complete exact workcell input keys required')
 for k,lo,hi in [('tick_seconds',1,3600),('horizon_ticks',1,1000),('buffer_capacity',0,72),('staff_capacity_person_ticks',0,10000),('preparation_ticks_per_part',1,1000),('preparation_capacity_person_ticks',0,100000)]:_int(x[k],k,lo,hi)
 for k in ('startup_cents','staff_cents','opening_cash_cents','preparation_setup_cents','preparation_cents_per_part'):_int(x[k],k)
 _bool(x['prepared_presentation'],'prepared_presentation')
 if not isinstance(x['jobs'],list) or not 1<=len(x['jobs'])<=24:raise ValueError('Require 1..24 ordered jobs')
 jobids=[];partids=[];prior_due=-1
 for j in x['jobs']:
  if not isinstance(j,dict) or set(j)!=set(b['jobs'][0]):raise ValueError('Exact job fields required')
  if not isinstance(j['job_id'],str) or not j['job_id'] or len(j['job_id'])>40:raise ValueError('Invalid job ID')
  if j['variant'] not in ('A','B'):raise ValueError('Unknown variant')
  if not isinstance(j['part_ids'],list) or len(j['part_ids'])!=3 or any(not isinstance(p,str) or not p or len(p)>60 for p in j['part_ids']):raise ValueError('Exactly three named component identities required')
  for k in ('supply_tick','release_tick','due_tick'):_int(j[k],k,0,x['horizon_ticks'])
  if not j['release_tick']<j['due_tick'] or j['due_tick']<=prior_due:raise ValueError('Increasing due times and nonempty loading windows required')
  prior_due=j['due_tick'];jobids.append(j['job_id']);partids+=j['part_ids']
 if len(jobids)!=len(set(jobids)) or len(partids)!=len(set(partids)):raise ValueError('Job and component identities must be globally unique')
 q=x['quality_fail_first_job_ids']
 if not isinstance(q,list) or any(not isinstance(i,str) for i in q) or len(q)!=len(set(q)) or not set(q)<=set(jobids):raise ValueError('Unknown or duplicate failed-quality job')
 if not isinstance(x['source_closed_intervals'],list):raise ValueError('Source closures must be a list')
 for a in x['source_closed_intervals']:
  if not isinstance(a,list) or len(a)!=2:raise ValueError('Closure needs start/end')
  for t in a:_int(t,'closure tick',0,x['horizon_ticks'])
  if a[0]>=a[1]:raise ValueError('Closure must have positive duration')
 def cfg(c):
  if not isinstance(c,dict) or set(c)!=set(b['config']):raise ValueError('Exact configuration fields required')
  if not isinstance(c['config_id'],str) or not c['config_id'] or len(c['config_id'])>60:raise ValueError('Invalid configuration ID')
  if c['kind'] not in ('fixed','humanoid','human'):raise ValueError('Unknown configuration kind')
  for k in ('pick_ticks','handoff_ticks','rework_ticks'):_int(c[k],k,1,1000)
  for k in ('changeover_ticks','inspection_person_ticks','support_until_tick'):_int(c[k],k,0,10000)
  _int(c['operation_cents_per_tick'],'operation_cents_per_tick')
  if c['initial_variant'] not in ('A','B'):raise ValueError('Unknown configured initial variant')
  q=c['qualified_variants']
  if not isinstance(q,list) or any(v not in ('A','B') for v in q) or len(q)!=len(set(q)):raise ValueError('Unique qualified variants required')
 cfg(x['config'])
 if x['replacement'] is not None:
  r=x['replacement']
  if not isinstance(r,dict) or set(r)!={'order_tick','cost_cents','commission_ticks','stock_available','rights_assumed','config'}:raise ValueError('Exact replacement fields required')
  _int(r['order_tick'],'order_tick',0,x['horizon_ticks']);_int(r['cost_cents'],'cost_cents');_int(r['commission_ticks'],'commission_ticks',0,1000)
  _bool(r['stock_available'],'stock_available');_bool(r['rights_assumed'],'rights_assumed');cfg(r['config'])
  if r['config']['config_id']==x['config']['config_id'] or r['config']['kind']=='human' or x['config']['kind']=='human':raise ValueError('Replacement requires distinct robot configurations')
 return copy.deepcopy(x)


def run_workcell(inputs):
 x=validate(inputs);h=x['horizon_ticks'];jobs=x['jobs'];lookup={j['job_id']:j for j in jobs}
 t=Treasury((Account('operator',x['opening_cash_cents']),Account('staff',0),Account('resources',0),Account('preparation',0),Account('equipment',0)))
 opening=t.snapshot();transaction=0;funding=[];events=[];idle=[];active=None;pending_rework=None;staff_used=0
 parts={p:{'part_id':p,'job_id':j['job_id'],'variant':j['variant'],'state':'raw','supply_tick':j['supply_tick']} for j in jobs for p in j['part_ids']}
 outcomes={j['job_id']:{'job_id':j['job_id'],'variant':j['variant'],'due_tick':j['due_tick'],'completed_tick':None,'on_time':False,'attempts':0} for j in jobs}
 config=x['config'];variant=config['initial_variant'];unit='opening-resource';max_buffer=0
 assets=[] if config['kind']=='human' else [{'unit_id':unit,'config_id':config['config_id'],'owner':'operator','acquired_tick':'opening_owned_stock','ready_tick':0,'support_until_tick':config['support_until_tick']}]
 replacement_status='not_requested';replacement_ready=None;replaced=False

 def pay(amount,payee,kind,tick,conditional=True):
  nonlocal t,transaction
  transaction+=1;iid=f'{transaction}-{kind}'
  if not amount:ok=True
  else:
   a,b=Moment(transaction,1),Moment(transaction,2)
   t=t.issue_invoice('issue-'+iid,iid,'operator',payee,amount,a,b,b,provenance='synthetic_workcell',cancellable=conditional,category=kind)
   candidate=t.settle_invoice('pay-'+iid,iid,b,provenance='synthetic_workcell');ok=candidate.invoice(iid).outstanding_cents==0
   t=candidate if ok or not conditional else t.cancel_invoice('cancel-'+iid,iid,b,provenance='unfunded_work_not_started')
  funding.append({'tick':tick,'kind':kind,'requested_cents':amount,'funded':ok,'conditional':conditional,'invoice_id':iid if amount else None})
  return ok

 staff_paid=pay(x['staff_cents'],'staff','staff_commitment',0,False)
 startup_paid=pay(x['startup_cents'],'resources','startup_configuration',0)
 preparation_planned=0;preparation_paid=False
 if x['prepared_presentation']:
  preparation_planned=min(len(parts),x['preparation_capacity_person_ticks']//x['preparation_ticks_per_part'])
  preparation_paid=pay(x['preparation_setup_cents']+preparation_planned*x['preparation_cents_per_part'],'preparation','prepared_presentation',0)
  prep_clock=0
  for index,p in enumerate(parts.values()):
   if preparation_paid and index<preparation_planned:
    p['presentation_start_tick']=max(prep_clock,p['supply_tick']);prep_clock=p['presentation_start_tick']+x['preparation_ticks_per_part'];p['presentation_ready_tick']=prep_clock
   else:p['presentation_start_tick']=None;p['presentation_ready_tick']=None
 else:
  for p in parts.values():p['presentation_start_tick']=None;p['presentation_ready_tick']=p['supply_tick']

 def ready(p,tick):
  a=parts[p];return a['state']=='raw' and a['presentation_ready_tick'] is not None and tick>=max(a['supply_tick'],a['presentation_ready_tick'])
 def source_open(tick,duration):return not any(tick<end and start<tick+duration for start,end in x['source_closed_intervals'])
 def start(kind,job,part_ids,duration,tick,person):
  nonlocal active,staff_used,max_buffer
  if tick+duration>h:return 'insufficient_shift_time'
  if tick+duration>config['support_until_tick']:return 'support_window_exhausted'
  if not staff_paid:return 'staff_commitment_unfunded'
  if staff_used+person>x['staff_capacity_person_ticks']:return 'staff_capacity_exhausted'
  if not pay(duration*config['operation_cents_per_tick'],'resources',kind,tick):return 'operation_cash_insufficient'
  staff_used+=person;active={'kind':kind,'job_id':job['job_id'],'variant':job['variant'],'part_ids':part_ids,'start_tick':tick,'end_tick':tick+duration,'unit_id':unit,'config_id':config['config_id'],'person_ticks':person}
  for p in part_ids:parts[p]['state']='in_'+kind
  events.append({'event':'start',**active})
  max_buffer=max(max_buffer,sum(p['state'] in ('buffer','in_pick') for p in parts.values()))
  return None

 for tick in range(h+1):
  if active and active['end_tick']==tick:
   a=active;active=None;kind=a['kind'];jid=a['job_id']
   if kind=='pick':
    for p in a['part_ids']:parts[p]['state']='buffer'
   elif kind in ('handoff','direct'):
    outcomes[jid]['attempts']+=1
    if jid in x['quality_fail_first_job_ids'] and outcomes[jid]['attempts']==1:
     for p in a['part_ids']:parts[p]['state']='buffer' if kind=='handoff' else 'raw'
     pending_rework=jid;events.append({'event':'quality_rejected','tick':tick,'job_id':jid,'part_ids':a['part_ids']})
    else:
     for p in a['part_ids']:parts[p]['state']='delivered'
     outcomes[jid].update(completed_tick=tick,on_time=tick<=lookup[jid]['due_tick'])
   elif kind=='changeover':variant=a['variant']
   elif kind=='rework':pending_rework=None
   events.append({'event':'finish',**a})
  r=x['replacement']
  if r and tick==r['order_tick']:
   if not r['stock_available']:replacement_status='stock_unavailable'
   elif not r['rights_assumed']:replacement_status='rights_not_assumed'
   elif pay(r['cost_cents'],'equipment','replacement_purchase',tick):
    replacement_ready=tick+r['commission_ticks'];replacement_status='commissioning'
    assets.append({'unit_id':'replacement-resource','config_id':r['config']['config_id'],'owner':'operator','acquired_tick':tick,'ready_tick':replacement_ready,'support_until_tick':r['config']['support_until_tick']})
   else:replacement_status='purchase_unfunded'
  if tick==h:break
  if active:continue
  if replacement_ready is not None and tick>=replacement_ready and not replaced:
   config=r['config'];variant=config['initial_variant'];unit='replacement-resource';replaced=True;replacement_status='activated'
   events.append({'event':'configuration_activated','tick':tick,'unit_id':unit,'config_id':config['config_id'],'qualified_variants':config['qualified_variants']})
  current=next((j for j in jobs if outcomes[j['job_id']]['completed_tick'] is None),None)
  if current is None:break
  reason=None
  if not startup_paid and not replaced:reason='startup_configuration_unfunded'
  elif tick>=config['support_until_tick']:reason='support_expired'
  elif current['variant'] not in config['qualified_variants']:reason='variant_not_qualified'
  else:
   if variant!=current['variant']:
    if config['changeover_ticks']:
     reason=start('changeover',current,[],config['changeover_ticks'],tick,config['changeover_ticks'])
    else:variant=current['variant'];events.append({'event':'zero_duration_recipe_switch','tick':tick,'variant':variant})
   if not active and not reason and pending_rework:
    reason=start('rework',lookup[pending_rework],[],config['rework_ticks'],tick,config['rework_ticks'])
   if not active and not reason:
    ids=current['part_ids']
    if x['buffer_capacity']==0:
     if tick<current['release_tick']:reason='waiting_loading_release'
     elif not all(ready(p,tick) for p in ids):reason='input_or_presentation_not_ready'
     else:
      duration=3*config['pick_ticks']+config['handoff_ticks']
      if not source_open(tick,duration):reason='source_refill_conflict'
      else:reason=start('direct',current,ids,duration,tick,duration if config['kind']=='human' else config['inspection_person_ticks'])
    else:
     complete=all(parts[p]['state']=='buffer' for p in ids)
     if complete and tick>=current['release_tick']:
      duration=config['handoff_ticks'];reason=start('handoff',current,ids,duration,tick,duration if config['kind']=='human' else config['inspection_person_ticks'])
     elif sum(p['state']=='buffer' for p in parts.values())>=x['buffer_capacity']:reason='buffer_full'
     else:
      # Reserve the current kit before looking ahead, so future parts cannot deadlock it.
      candidates=[current]
      if complete:
       candidates=[]
       for j in jobs[jobs.index(current):]:
        if j['variant']!=variant:break
        candidates.append(j)
      item=next(((j,p) for j in candidates for p in j['part_ids'] if ready(p,tick)),None)
      if item is None:reason='input_or_presentation_not_ready'
      elif complete and tick+config['pick_ticks']>current['release_tick']:reason='reserve_manipulator_for_handoff'
      elif not source_open(tick,config['pick_ticks']):reason='source_refill_conflict'
      else:
       j,p=item;reason=start('pick',j,[p],config['pick_ticks'],tick,config['pick_ticks'] if config['kind']=='human' else 0)
  if reason:idle.append({'tick':tick,'reason':reason,'job_id':current['job_id'],'config_id':config['config_id']})
  max_buffer=max(max_buffer,sum(p['state'] in ('buffer','in_pick') for p in parts.values()))

 t.audit();closing=t.snapshot();rows=list(outcomes.values());delivered=sum(p['state']=='delivered' for p in parts.values())
 for a in assets:
  a['closing_status']=('unsupported_retained' if h>=a['support_until_tick'] else
   'configuration_unfunded' if a['unit_id']=='opening-resource' and not startup_paid else
   'commissioning' if a['ready_tick']>h else 'active_configured' if a['unit_id']==unit else
   'ready_not_activated' if a['unit_id']=='replacement-resource' and not replaced else 'superseded_retained')
 prepared_done=sum(p['presentation_ready_tick'] is not None and p['presentation_ready_tick']<=h for p in parts.values()) if x['prepared_presentation'] else 0
 summary={'due_kits':len(jobs),'on_time_kits':sum(r['on_time'] for r in rows),'late_kits':sum(r['completed_tick'] is not None and not r['on_time'] for r in rows),
  'undelivered_kits':sum(r['completed_tick'] is None for r in rows),'on_time_components':3*sum(r['on_time'] for r in rows),'delivered_components':delivered,
  'remaining_components':len(parts)-delivered,'handoff_attempts':sum(r['attempts'] for r in rows),'max_buffer_parts':max_buffer,
  'manipulator_busy_ticks':sum(e['end_tick']-e['start_tick'] for e in events if e['event']=='start'),'staff_person_ticks_used':staff_used,
  'paid_staff_cents':t.balance('staff'),'preparation_planned_parts':preparation_planned,'prepared_parts_by_horizon':prepared_done,
  'preparation_booked_person_ticks':preparation_planned*x['preparation_ticks_per_part'] if preparation_paid else 0,
  'preparation_executed_person_ticks':sum(max(0,min(h,p['presentation_ready_tick'])-p['presentation_start_tick']) for p in parts.values() if p['presentation_start_tick'] is not None),
  'operator_outlay_cents':x['opening_cash_cents']-t.balance('operator'),'operating_and_startup_cash_cents':t.balance('resources'),
  'preparation_cash_cents':t.balance('preparation'),'replacement_cash_cents':t.balance('equipment'),'due_unpaid_cents':sum(i.outstanding_cents for i in t.invoices),
  'robot_units_owned':len(assets),'replacement_status':replacement_status}
 assert delivered%3==0 and delivered==3*(summary['on_time_kits']+summary['late_kits'])
 assert summary['on_time_kits']+summary['late_kits']+summary['undelivered_kits']==len(jobs)
 assert max_buffer<=x['buffer_capacity']
 result={'schema_version':SCHEMA,'status':'synthetic_physical_workcell_not_empirical_takt_or_roi','inputs':x,'jobs':rows,'components':list(parts.values()),'assets':assets,
  'events':events,'idle':idle,'funding':funding,'summary':summary,'opening_treasury':opening,'closing_treasury':closing,
  'source_sha256':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in SOURCES},
  'evidence_role':{'references':['CAP-E001','CAP-E002','CAP-E024','CAP-E025','CAP-E026','CAP-E027'],'numerical_calibration':False},
  'boundary':'One manipulator does picks, kit handoffs, changeover and recovery without overlap. Three unique components form one accepted by-deadline kit. Late deliveries stay late. External prepared presentation and replacement have explicit capacity, timing and cash. Fixed staffing remains paid. Treasury month is a transaction sequence, not calendar months; lifecycle economics, welding and transport are excluded.'}
 result['case_hash']=hashlib.sha256(json.dumps(result,sort_keys=True,separators=(',',':'),allow_nan=False).encode()).hexdigest()
 return result


def run_workcell_case(overrides=None):
 o={} if overrides is None else overrides
 allowed={'mode','mixed_variants','buffer_capacity','changeover_ticks','pick_ticks','source_refill','quality_failure','prepared_presentation','preparation_capacity_person_ticks','opening_cash_cents','support_until_tick','replacement','replacement_qualified','replacement_cash_cents','replacement_stock','replacement_rights'}
 if not isinstance(o,dict) or set(o)-allowed:raise ValueError('Unknown workcell shortcut')
 x=workcell_inputs();mode=o.get('mode','fixed')
 if mode not in ('fixed','humanoid','human'):raise ValueError('Unknown workcell mode')
 x['config']=_config(mode);x['startup_cents']=0 if mode=='human' else 30000 if mode=='humanoid' else 20000
 if mode=='human':x['buffer_capacity']=0
 for k in ('mixed_variants','source_refill','quality_failure','prepared_presentation','replacement','replacement_qualified','replacement_stock','replacement_rights'):
  if k in o:_bool(o[k],k)
 if o.get('mixed_variants'):
  for i,j in enumerate(x['jobs']):j['variant']='A' if (i//3)%2==0 else 'B'
 for k in ('buffer_capacity','preparation_capacity_person_ticks','opening_cash_cents'):
  if k in o:x[k]=o[k]
 for k in ('changeover_ticks','pick_ticks','support_until_tick'):
  if k in o:x['config'][k]=o[k]
 if o.get('source_refill'):x['source_closed_intervals']=[[24,34]]
 if o.get('quality_failure'):x['quality_fail_first_job_ids']=['J04']
 if o.get('prepared_presentation'):x['prepared_presentation']=True;x['config']['pick_ticks']=o.get('pick_ticks',1)
 if o.get('replacement'):
  c=_config(mode,'v2');c['qualified_variants']=['A','B'] if o.get('replacement_qualified',True) else []
  x['replacement']={'order_tick':72,'cost_cents':o.get('replacement_cash_cents',40000),'commission_ticks':12,'stock_available':o.get('replacement_stock',True),'rights_assumed':o.get('replacement_rights',True),'config':c}
 return run_workcell(x)


def replay_workcell(saved):
 if not isinstance(saved,dict) or saved.get('schema_version')!=SCHEMA or not isinstance(saved.get('inputs'),dict):raise ValueError('Complete saved workcell inputs required')
 return run_workcell(saved['inputs'])


def workcell_artifact():
 shortcuts={
  'fixed_buffered':{},'fixed_direct':{'buffer_capacity':0},'human_direct':{'mode':'human'},'humanoid_buffered':{'mode':'humanoid'},
  'fixed_refill_buffered':{'source_refill':True},'human_refill_buffered':{'mode':'human','buffer_capacity':6,'source_refill':True},'insufficient_kit_buffer':{'buffer_capacity':2},
  'fixed_mixed_variants':{'mixed_variants':True},'humanoid_mixed_variants':{'mode':'humanoid','mixed_variants':True},
  'fixed_fast_retool':{'mixed_variants':True,'changeover_ticks':1},
  'prepared_presentation':{'prepared_presentation':True,'buffer_capacity':0},
  'presentation_capacity_short':{'prepared_presentation':True,'buffer_capacity':0,'preparation_capacity_person_ticks':70},
  'quality_rework':{'quality_failure':True},'support_expires':{'support_until_tick':72},
  'qualified_replacement':{'support_until_tick':72,'replacement':True},
  'unqualified_replacement':{'support_until_tick':72,'replacement':True,'replacement_qualified':False},
  'unfunded_replacement':{'support_until_tick':72,'replacement':True,'replacement_cash_cents':1000000},
  'replacement_stock_unavailable':{'support_until_tick':72,'replacement':True,'replacement_stock':False}
 }
 cases={k:run_workcell_case(v) for k,v in shortcuts.items()}
 return {'schema_version':SCHEMA,'challenge_id':'DE-CF04','case_inputs':shortcuts,'cases':cases,'summary':[{'case':k,**r['summary']} for k,r in cases.items()],
  'comparison_boundary':'Common synthetic three-part kits and deadlines, one manipulator and unique stock. Source single-part times and three-part target timings are not calibration. Qualified fixed vision/buffering and paid input preparation are alternatives; hypothetical changeovers and supported generations must earn the same service. No product or lifecycle-cost ranking.'}
