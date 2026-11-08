"""Prototype: explicit support/cash admission for finite expansion candidates.

The physical, commercial, enterprise and Treasury engines remain unchanged.
Announcements are planning inputs, never observations of future service.
"""
from dataclasses import asdict, dataclass, replace
from fractions import Fraction
from pathlib import Path
import hashlib
import json

from model.calendar_bridge import (Bridge, _BridgedEnterprise, bridge_case_inputs,
                                  bridge_source_hashes, exact, rational, wire_rationals)
from model.enterprise_finance import FinancePlan, TermLoan
from model.monthly_commercial import restore_opening_inputs
from model.monthly_deployment import Start, run_monthly, _rational
from model.monthly_enterprise import Business, CustomerMove, EnterprisePlan, Equity, Market, round_cents
from model.trajectories import parameters_at


def integer(v, minimum=0, maximum=1_000_000_000):
    if type(v) is not int or not minimum <= v <= maximum:raise ValueError('Bounded exact integer required')


@dataclass(frozen=True)
class ExpansionPolicy:
    mode: str = 'announced_capacity_reserve'
    reserve_months: int = 2
    actual_support_hours_by_month: tuple[int, ...] = (25,25,25,25,60,60,60,60)
    announced_support_hours_by_month: tuple[int, ...] = (25,25,25,25,60,60,60,60)

    def __post_init__(self):
        if self.mode not in ('funded_only','current_capacity_reserve','announced_capacity_reserve'):
            raise ValueError('Unknown expansion admission policy')
        integer(self.reserve_months,0,12)
        for field in ('actual_support_hours_by_month','announced_support_hours_by_month'):
            xs=getattr(self,field)
            if not isinstance(xs,(tuple,list)) or not 1<=len(xs)<=24:raise ValueError('Explicit finite resource calendar required')
            for v in xs:integer(v,0,1000)
            object.__setattr__(self,field,tuple(xs))


class _ExpansionEnterprise(_BridgedEnterprise):
    def __init__(self,plan,contracts,treasury,enterprise,finance,bridge,policy):
        super().__init__(plan,contracts,treasury,enterprise,finance,bridge)
        if not isinstance(policy,ExpansionPolicy):raise ValueError('Explicit expansion policy required')
        for field in ('actual_support_hours_by_month','announced_support_hours_by_month'):
            if len(getattr(policy,field))!=plan.months:raise ValueError('Resource calendar must match the physical horizon')
            if max(getattr(policy,field))>bridge.support_hours_per_month:raise ValueError('Resource calendar exceeds the declared annual allocation ceiling')
        if any(c.arrangement!='provider_service' for c in contracts):raise ValueError('This reserve contract requires provider-funded robot service')
        if treasury.invoices or enterprise.moves or enterprise.market.unmet_units or enterprise.market.new_units:
            raise ValueError('Use one fixed baseline without inherited invoices or scheduled transfers')
        if any(b.active_from_month is not None for b in enterprise.businesses if b.operator_id!='incumbent'):
            raise ValueError('One active service business required')
        if any(o.requested_additions or o.opening_installed for o in plan.operators if o.operator_id!='incumbent') or plan.opening_finished:
            raise ValueError('All installed stock and growth requests must belong to the incumbent')
        if any(s.quantity!=1 for s in plan.starts):raise ValueError('One individually identified unit per expansion candidate required')
        self.policy=policy;self.inventory=[];self.expansion_events=[];self.expansion_months=[]
        self.requested_growth=sum(o.requested_additions for o in plan.operators)
        self.candidates={f'monthly:{plan.plan_id}:m{s.month}:start:{s.order_id}':s for s in plan.starts}

    def prepare(self,t,month,units):
        # The existing loop maintains this live list; it is the only inventory.
        self.inventory=units
        return super().prepare(t,month,units)

    def admit(self,t,iid,month,phase,physical_reason,unit=None,operator_id=None):
        invoice=t.invoice(iid);action=invoice.category
        if action in ('support','commission'):
            _,target,upgrade=self.robot_invoices[(month,unit.unit_id)]
            need=exact(self.robot_operation(target)['support_hours'])/12+(self.bridge.upgrade_hours_per_robot if upgrade else 0)
            used=self.support_hours_used+self.qualification_hours_used
            if used+need>self.policy.actual_support_hours_by_month[month]:
                physical_reason=physical_reason or 'actual_monthly_support_allocation'
        if action!='start':return super().admit(t,iid,month,phase,physical_reason,unit,operator_id)
        candidate=self.candidates[iid];order_id=candidate.order_id
        committed=[u for u in self.inventory if u.origin!='opening_stock' and u.status!='rejected']
        retained=[u for u in self.inventory if u.status!='rejected']
        current_index=self.calendar[month]['annual_period_index']
        # Preserve known cohort differences. For a new candidate use the current
        # configuration as a planning assumption, not a future qualified release.
        def requirements(index):
            settings=parameters_at(self.annual,self.paths,index)
            software=round_cents(exact(settings['digital_cost_usd'])*100/12) if self.bridge.digital_enabled else 0
            return exact(self.robot_operation(index)['support_hours'])/12, self.plan.system.support_cents_per_robot_month+software
        candidate_hours, candidate_recurring_cents=requirements(current_index)
        known=[]
        for retained_unit in retained:
            index=self.target_vintage(retained_unit,month)
            hours,cost=requirements(index)
            known.append({'unit_id':retained_unit.unit_id,'planning_annual_period_index':index,
                          'recurring_support_hours':_rational(hours),'recurring_support_cents':cost})
        expected_month=month+self.plan.system.assembly_lead_months+self.plan.system.commissioning_lead_months
        proposed_fleet=len(retained)+candidate.quantity
        hours_needed=sum((rational(u['recurring_support_hours']) for u in known),Fraction())+candidate.quantity*candidate_hours
        planning_hours=(self.policy.actual_support_hours_by_month[month] if self.policy.mode=='current_capacity_reserve'
                        else self.policy.announced_support_hours_by_month[min(expected_month,self.plan.months-1)])
        reserve=(sum(u['recurring_support_cents'] for u in known)+candidate.quantity*candidate_recurring_cents)*self.policy.reserve_months
        cash_after=t.available(invoice.payer)-invoice.outstanding_cents
        reason=physical_reason
        if len(committed)+candidate.quantity>self.requested_growth:reason=reason or 'finite_growth_request_already_committed'
        if expected_month>=self.plan.months:reason=reason or 'candidate_delivery_outside_observation_window'
        if self.policy.mode!='funded_only':
            if hours_needed>planning_hours:reason=reason or 'planned_fleet_support_capacity'
            if cash_after<reserve:reason=reason or 'installed_and_growth_cash_reserve'
        candidate_t,reason=super().admit(t,iid,month,phase,reason,unit,operator_id)
        self.expansion_events.append({'month':month,'phase':phase,'order_id':order_id,'invoice_id':iid,
            'policy':self.policy.mode,'status':'blocked' if reason else 'admitted','reason':reason,
            'known_unit_ids':[u.unit_id for u in retained], 'committed_growth_units':len(committed),
            'fixed_requested_growth_units':self.requested_growth,'candidate_units':candidate.quantity,
            'expected_commission_month_without_delays':expected_month,'proposed_fleet_units':proposed_fleet,
            'known_cohort_requirements':known,'candidate_current_support_hours_per_unit':_rational(candidate_hours),
            'planned_fleet_support_hours':_rational(hours_needed),
            'planning_support_hours':planning_hours,'actual_current_support_hours':self.policy.actual_support_hours_by_month[month],
            'candidate_current_recurring_support_cents_per_unit':candidate_recurring_cents,'required_payer_reserve_cents':reserve,
            'payer_available_before_start_cents':t.available(invoice.payer),'candidate_start_cents':invoice.face_cents,
            'cash_after_start_before_other_future_obligations_cents':cash_after,
            'future_actual_support_consulted':False})
        return candidate_t,reason

    def close(self,t,month,units,supported):
        super().close(t,month,units,supported)
        assert self.support_hours_used+self.qualification_hours_used<=self.policy.actual_support_hours_by_month[month]
        assert sum(u.origin!='opening_stock' and u.status!='rejected' for u in units)<=self.requested_growth
        self.expansion_months.append({'month':month,'actual_support_hours':self.policy.actual_support_hours_by_month[month],
            'announced_support_hours':self.policy.announced_support_hours_by_month[month],
            'support_and_qualification_hours_used':_rational(self.support_hours_used+self.qualification_hours_used),
            'integration_hours_used':_rational(self.integration_hours_used),
            'opening_cohort_supported_ids':[u.unit_id for u in units if u.origin=='opening_stock' and u.unit_id in supported],
            'new_cohort_supported_ids':[u.unit_id for u in units if u.origin!='opening_stock' and u.unit_id in supported],
            'actual_unit_ids':[u.unit_id for u in units],
            'provider_cash_cents':t.balance(self.plan.provider_actor),
            'accepted_service_units':self.market_months[-1]['total_delivered_units']})

    def expansion_result(self,r):
        invoices=r['closing_treasury']['invoices']
        return {'schema_version':'support-expansion-policy/0.1','evidence_status':'synthetic_declared_admission_policy',
            'inputs':asdict(self.policy),'events':self.expansion_events,'months':self.expansion_months,
            'summary':{'accepted_zones':_rational(sum((rational(m['total_delivered_units']) for m in r['enterprise']['months']),Fraction())),
                'due_zones':self.enterprise.market.baseline_units*self.plan.months,
                'funded_starts':sum(m['flows']['started'] for m in r['months']),
                'rejected_manufactured_units':sum(m['flows']['rejected'] for m in r['months']),
                'commissioned_new_units':sum(m['flows']['commissioned'] for m in r['months']),
                'unsupported_installed_unit_months':sum(m['support']['unsupported_installed'] for m in r['months']),
                'opening_cohort_supported_unit_months':sum(len(m['opening_cohort_supported_ids']) for m in self.expansion_months),
                'provider_closing_cash_cents':r['months'][-1]['closing_cash_cents'][self.plan.provider_actor],
                'external_operating_cash_cents':r['enterprise']['consolidation']['external_physical_outlay_cents']+r['enterprise']['consolidation']['external_enterprise_outlay_cents'],
                'provider_uncollected_service_fees_cents':sum(i['outstanding_cents'] for i in invoices if i['category']=='service_fee'),
                'provider_unpaid_recorded_bills_cents':sum(i['outstanding_cents'] for i in invoices if i['payer']==self.plan.provider_actor and not i['cancellable'])},
            'metric_lineage':[
                {'metric':'finite growth commitment','equation':'live non-opening, non-rejected units + candidate quantity <= fixed requested additions',
                 'inputs':'existing physical inventory and identified candidate starts','implementation':'_ExpansionEnterprise.admit',
                 'basis':'synthetic declared growth objective; rejected units retain sunk cost and unique identity'},
                {'metric':'planned fleet support','equation':'sum known retained-cohort recurring hours + candidate units × current-configuration hours',
                 'inputs':'known_cohort_requirements and candidate_current_support_hours_per_unit',
                 'implementation':'_ExpansionEnterprise.admit; _BridgedEnterprise.robot_operation',
                 'basis':'current or announced allocation is a planning premise, not realized future service'},
                {'metric':'payer support reserve','equation':'declared months × (sum known recurring support/software cents + candidate recurring cents)',
                 'inputs':'current cohort prices, actual payer available cash after manufacture, reserve months',
                 'implementation':'_ExpansionEnterprise.admit',
                 'basis':'bounded reserve excludes commissioning, debt, all other future bills and residual assets'},
                {'metric':'accepted service and actual resources','equation':'unchanged monthly dispatch under paid support, commissioning, staff and declared current-hour limits',
                 'inputs':'expansion months, calendar cohorts, enterprise demand and one Treasury',
                 'implementation':'run_monthly; _ExpansionEnterprise.close',
                 'basis':'no backfilled service, synthetic exact rational zones; no observed system availability or ROI'}],
            'limits':['Fixed finite growth requests and candidate dates; no optimized investment, pricing, shutdown or autonomous demand generation.',
                'Support for installed units remains first in the unchanged phase order. Start admission can protect future cash but cannot backfill missed service.',
                'Announcements inform planning but do not guarantee realized resources. No future realized outcome enters a start decision.',
                'Reserve uses current per-unit recurring support/software bills and declared months, not every future commitment or terminal asset value.',
                'Opening installed assets predate this cash window; results are not lifetime ROI or a valuation.']}


def source_hashes():
    return {**bridge_source_hashes(),'model/support_expansion.py':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}


def canonical(value):
    if isinstance(value,dict):return {k:canonical(v) for k,v in value.items()}
    if isinstance(value,(list,tuple)):return [canonical(v) for v in value]
    if type(value) is float and value.is_integer():return int(value)
    return value


def run_support_expansion(plan,treasury,contracts,enterprise,finance,bridge,policy):
    x=_ExpansionEnterprise(plan,contracts,treasury,enterprise,finance,bridge,policy)
    r=run_monthly(plan,treasury,commercial=x);r.update(schema_version='support-expansion/0.1',scope='synthetic_funded_installed_service_and_finite_expansion')
    r['commercial']=x.result(r);r['commercial']['limits']=['See support_expansion, finance and calendar_bridge scopes.']
    r['enterprise']=x.enterprise_result(r);r['enterprise']['limits']=['Fixed demand and one active operator; see support_expansion limits.']
    r['finance']=x.finance_result(r);r['calendar_bridge']=x.bridge_result(r);r['support_expansion']=x.expansion_result(r)
    assert r['finance']['consolidation']['unclassified_other_boundary_cash_cents']==0
    r['source_sha256']=source_hashes();r=wire_rationals(canonical(r))
    r['case_hash']=hashlib.sha256(json.dumps(r,sort_keys=True,separators=(',',':')).encode()).hexdigest()
    return json.loads(json.dumps(r))


DEFAULTS={'provider_cash_cents':20_000_000,'operator_cash_cents':50_000_000,'service_fee_cents':150_000,
          'service_receipt_lag':1,'requested_growth':1,'assembly_lead_months':1,'provider_loan_cents':0,
          'opening_components':100,'first_candidate_accepted':True,'policy':{}}


def expansion_case_inputs(overrides=None):
    if overrides is None:overrides={}
    if not isinstance(overrides,dict) or set(overrides)-set(DEFAULTS):raise ValueError('Unknown expansion controls')
    x={**DEFAULTS,**overrides}
    for k,v in x.items():
        if k not in ('policy','first_candidate_accepted'):integer(v)
    if type(x['first_candidate_accepted']) is not bool:raise ValueError('Explicit first-candidate acceptance hypothesis required')
    integer(x['requested_growth'],0,4);integer(x['assembly_lead_months'],1,6);integer(x['service_receipt_lag'],1,12)
    if not isinstance(x['policy'],dict):raise ValueError('Policy inputs must be an object')
    policy=ExpansionPolicy(**x['policy'])
    ceiling=max(*policy.actual_support_hours_by_month,*policy.announced_support_hours_by_month,1)
    p,t,cs,e,f,b=bridge_case_inputs({'loan_cents':0,'later_start_candidate':False,'response_month':None},
        {'support_hours_per_month':ceiling,'annual_overrides':{'capability_progress':0}})
    n=p.months
    p=replace(p,plan_id='installed-service-expansion',allocation_cycle=('incumbent','entrant'),opening_components=x['opening_components'],
        system=replace(p.system,assembly_lead_months=x['assembly_lead_months']),
        operators=tuple(replace(o,opening_installed=2 if o.operator_id=='incumbent' else 0,
                               requested_additions=x['requested_growth'] if o.operator_id=='incumbent' else 0,
                               demand_units_by_month=(1000,)*n) for o in p.operators),
        starts=tuple(Start('candidate-'+str(m),m,1,0 if m==0 and not x['first_candidate_accepted'] else 1) for m in range(n)))
    money={'provider':x['provider_cash_cents'],'incumbent':x['operator_cash_cents']}
    t=replace(t,accounts=tuple(replace(a,opening_cash_cents=money.get(a.actor_id,a.opening_cash_cents)) for a in t.accounts))
    cs=tuple(replace(c,arrangement='provider_service',lessor_actor=None,service_cents_per_supported_month=x['service_fee_cents'],
                     service_collection_lag_months=x['service_receipt_lag']) for c in cs)
    small=next(v for v in e.businesses if v.operator_id=='entrant')
    businesses=tuple(replace(v,active_from_month=0 if v.operator_id=='incumbent' else None,
                             human_staff_cents_by_month=small.human_staff_cents_by_month,
                             human_capacity_by_month=small.human_capacity_by_month) for v in e.businesses)
    e=replace(e,market=replace(e.market,baseline_units=1000,unmet_units=0,new_units=0),businesses=businesses,moves=(),equity=())
    loans=(TermLoan('growth-support-loan','capital_lender','provider',x['provider_loan_cents'],0,7,0,10000,'full_or_nothing'),) if x['provider_loan_cents'] else ()
    f=replace(f,loans=loans)
    return p,t,cs,e,f,b,policy


def run_expansion_case(overrides=None):return run_support_expansion(*expansion_case_inputs(overrides))


def replay_expansion(saved):
    if not isinstance(saved,dict) or saved.get('schema_version')!='support-expansion/0.1':raise ValueError('Complete support-expansion case required')
    try:
        e=dict(saved['enterprise']['inputs']);e['market']=Market(**e['market'])
        for key,cls in [('businesses',Business),('moves',CustomerMove),('equity',Equity)]:e[key]=tuple(cls(**x) for x in e[key])
        f=dict(saved['finance']['inputs']);f['loans']=tuple(TermLoan(**x) for x in f['loans'])
        return run_support_expansion(*restore_opening_inputs(saved),EnterprisePlan(**e),FinancePlan(**f),
                                     Bridge(**saved['calendar_bridge']['inputs']),ExpansionPolicy(**saved['support_expansion']['inputs']))
    except (KeyError,AttributeError) as exc:raise ValueError('Incomplete support-expansion inputs') from exc


def expansion_worlds():
    ample={'actual_support_hours_by_month':[60]*8,'announced_support_hours_by_month':[60]*8}
    thin={'provider_cash_cents':4_000_000,'service_receipt_lag':3}
    return {
        'announced_capacity_reserve':{},
        'funded_only':{'policy':{'mode':'funded_only'}},
        'current_capacity_reserve':{'policy':{'mode':'current_capacity_reserve'}},
        'announced_increase_fails':{'policy':{'actual_support_hours_by_month':[25]*8}},
        'ample_support':{'policy':ample},
        'thin_provider_funded_only':{**thin,'policy':{**ample,'mode':'funded_only'}},
        'thin_provider_reserve':{**thin,'policy':ample},
        'separate_provider_loan':{**thin,'provider_loan_cents':500_000,'policy':ample},
        'operator_cannot_pay':{'operator_cash_cents':0,'policy':ample},
        'rejected_start_replacement':{'first_candidate_accepted':False,'policy':{'mode':'funded_only'}},
        'qualified_component_scarcity':{'opening_components':7,'policy':{'mode':'funded_only'}},
        'longer_manufacturing_lead':{'assembly_lead_months':3},
        'zero_requested_growth':{'requested_growth':0},
        'exact_initial_reserve':{**thin,'provider_cash_cents':4_273_032,'policy':ample},
        'one_cent_below_reserve':{**thin,'provider_cash_cents':4_273_031,'policy':ample},
        'support_allocation_shrinks':{'policy':{**ample,'actual_support_hours_by_month':[60]*4+[20]*4}},
    }


def expansion_artifact():
    options=expansion_worlds();cases={name:run_expansion_case(x) for name,x in options.items()}
    return {'schema_version':'support-expansion-artifact/0.1','source_sha256':source_hashes(),
            'defaults':DEFAULTS,'case_inputs':options,'cases':cases,
            'summary':[{'case':name,**r['support_expansion']['summary']} for name,r in cases.items()],
            'comparison_boundary':'Synthetic finite growth against installed service on one unchanged execution loop. Announcements, actual resource allocations, actor cash and fees remain separate. Current-capacity caution can delay useful capacity; failed announcements can strand units. No optimized policy, lifecycle ROI or empirical supply reliability.'}


def expansion_catalog():
    path=Path(__file__).resolve().parents[1]/'model/results/support_expansion.json'
    if not path.exists():raise ValueError('Generate the support-expansion export first')
    data=json.loads(path.read_text())
    if data['source_sha256']!=source_hashes():raise ValueError('Support-expansion export has stale source hashes; regenerate')
    return {k:v for k,v in data.items() if k!='cases'}|{'cases':{'announced_capacity_reserve':data['cases']['announced_capacity_reserve']}}
