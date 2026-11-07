"""Explicit synthetic cleaning units and annual digital paths in monthly execution.

The physical stock and Treasury remain authoritative. This does not add the
separate annual fleet or intelligence-architecture cash ledgers to that stock.
"""
from __future__ import annotations

from dataclasses import asdict, dataclass, replace
from fractions import Fraction
import hashlib
import json
from pathlib import Path

from model.engine import BOUNDS, capability_at, catalog, operation, parameters
from model.trajectories import parameters_at, resolve_paths
from model.enterprise_finance import (
    FinancePlan, TermLoan, _FinancedEnterprise, finance_source_hashes, financed_case_inputs,
)
from model.monthly_commercial import restore_opening_inputs
from model.monthly_deployment import Moment, _integer, _name, _rational, run_monthly, Start
from model.monthly_enterprise import (
    Business, CustomerMove, EnterprisePlan, Equity, Market, reference_inputs, round_cents,
)
from model.treasury import Account

CELL = 'CELL-M11-floor-cleaning-US-2025'
WORK = 'WORK-CLEANING-ZONE-BRIDGE-SYN-01'
ROOT = Path(__file__).resolve().parents[1]


def exact(value):
    """Preserve the published annual function's finite decimal representation."""
    return Fraction(str(value))


def rational(value):
    """Read internal integer or lossless wire-string rational components."""
    return Fraction(int(value['numerator']),int(value['denominator']))


def wire_rationals(value):
    """Preserve rational integers across JavaScript's binary64 JSON parser."""
    if isinstance(value,dict):
        if set(value)=={'numerator','denominator'}:
            return {key:str(component) for key,component in value.items()}
        return {key:wire_rationals(item) for key,item in value.items()}
    if isinstance(value,(list,tuple)):return [wire_rationals(item) for item in value]
    if type(value) is int and abs(value)>2**53-1:
        raise ValueError('Non-rational integer exceeds lossless browser JSON range')
    return value


@dataclass(frozen=True)
class Bridge:
    cell_id: str = CELL
    start_year: int = 2026
    start_month: int = 7
    annual_overrides: dict | None = None
    digital_paths: dict | None = None
    digital_enabled: bool = True
    software_policy: str = 'paid_calendar_upgrade'
    support_hours_per_month: int = 60
    integration_hours_per_month: int = 200
    upgrade_cost_cents_per_robot: int = 50_000
    upgrade_hours_per_robot: int = 2
    digital_vendor_actor: str = 'digital_vendor'

    def __post_init__(self):
        if self.cell_id != CELL: raise ValueError('Only the explicit cleaning-zone contract is implemented')
        _integer(self.start_year,2026);_integer(self.start_month,1)
        if self.start_month>12: raise ValueError('Calendar month must be 1..12')
        if type(self.digital_enabled) is not bool: raise ValueError('Explicit digital-enabled Boolean required')
        if self.software_policy not in ('paid_calendar_upgrade','frozen_cohort'):
            raise ValueError('Unknown cohort software policy')
        for x in (self.support_hours_per_month,self.integration_hours_per_month,self.upgrade_cost_cents_per_robot,self.upgrade_hours_per_robot):_integer(x)
        _name(self.digital_vendor_actor)
        if self.annual_overrides is not None and not isinstance(self.annual_overrides,dict):
            raise ValueError('Annual overrides must be an object')


def bridge_context(bridge,months):
    if not isinstance(bridge,Bridge):raise ValueError('Explicit bridge contract required')
    c=catalog();p=parameters({'years':3,**(bridge.annual_overrides or {})})
    if p['learning_transfer'] != 0:raise ValueError('Endogenous learning is not implemented in this bridge')
    if p['integration_hours']<=0:raise ValueError('This monthly booking contract requires positive process-integration hours')
    if bridge.support_hours_per_month*12>p['support_budget_hours'] or bridge.integration_hours_per_month*12>p['integration_budget_hours']:
        raise ValueError('Declared monthly allocation exceeds the annual reference resource pool')
    resolved=resolve_paths(p,c['base_year'],BOUNDS,bridge.digital_paths)
    cell=next(x for x in c['cells'] if x['cell_id']==bridge.cell_id)
    system=next(x for x in c['systems'] if x['system_id']==cell['system_id'])
    calendar=[]
    for month in range(months):
        offset=bridge.start_month-1+month;year=bridge.start_year+offset//12
        index=year-c['base_year']
        current=parameters_at(p,resolved,index)
        calendar.append({'month':month,'calendar_year':year,'calendar_month':offset%12+1,
                         'annual_period_index':index,'effective_parameters':current})
    return c,p,resolved,cell,system,calendar


class _BridgedEnterprise(_FinancedEnterprise):
    def __init__(self,plan,contracts,treasury,enterprise,finance,bridge):
        super().__init__(plan,contracts,treasury,enterprise,finance)
        self.bridge=bridge
        self.catalog,self.annual,self.paths,self.cell,self.system,self.calendar=bridge_context(bridge,plan.months)
        if plan.system.work_id!=WORK or enterprise.market.work_id!=WORK:
            raise ValueError('No inferred conversion from historical floor bundles; explicit cleaning work ID required')
        physical=operation(self.cell,self.system,self.annual,capability_at(self.annual,0),False)
        mapped={
            'bundled_start_cents':round_cents(exact(self.system['manufacture_cost_usd'])*100),
            'commissioning_cents':round_cents(exact(self.annual['integration_hours'])*6000),
            'support_cents_per_robot_month':round_cents(exact(physical['robot_operating_cost_usd'])*100/12)}
        if plan.system.system_id!=self.system['system_id'] or any(getattr(plan.system,k)!=v for k,v in mapped.items()):
            raise ValueError('Monthly physical cost/configuration differs from the declared annual mapping')
        for business in enterprise.businesses:
            for row in self.calendar:
                month=row['month'];d=exact(row['effective_parameters']['digital_efficiency']) if bridge.digital_enabled else Fraction()
                capacity=int(Fraction(business.human_staff_cents_by_month[month],100)/exact(self.cell['wage_usd_hour'])/exact(self.cell['human_hours_per_unit'])/(1-d))
                if business.human_capacity_by_month[month]!=capacity:
                    raise ValueError('Human capacity must follow the explicit paid-shift and digital-hour mapping')
        outsiders={enterprise.market.buyer_actor,enterprise.enterprise_vendor_actor,
                   plan.manufacturing_vendor_actor,plan.deployment_vendor_actor}
        if bridge.digital_vendor_actor in set(self.parties)|outsiders:
            raise ValueError('Digital resource supplier must be a distinct outside account')
        treasury.account(bridge.digital_vendor_actor)
        self.vintage={};self.robot_invoices={};self.digital_ids=set();self.supported={}
        self.bridge_events=[];self.bridge_months=[];self.charge_lines=[]
        self.support_hours_used=Fraction();self.qualification_hours_used=Fraction()
        self.integration_hours_used=Fraction()
        # Raw monthly capacity is a declared ceiling, not extra productive output.
        for row in self.calendar:
            op=self.robot_operation(row['annual_period_index'])
            if exact(op['accepted_units'])/12>plan.system.full_output_units_per_robot_month:
                raise ValueError('Annual rate exceeds the declared monthly mechanical ceiling')

    def robot_operation(self,index):
        current=parameters_at(self.annual,self.paths,index)
        return operation(self.cell,self.system,current,capability_at(self.annual,index),self.bridge.digital_enabled)

    def target_vintage(self,unit,month):
        current=self.calendar[month]['annual_period_index']
        old=self.vintage.get(unit.unit_id,current)
        return current if self.bridge.software_policy=='paid_calendar_upgrade' else old

    def robot_signature(self,index):
        current=parameters_at(self.annual,self.paths,index)
        return (capability_at(self.annual,index),current['coordination'] if self.bridge.digital_enabled else 0)

    def charge(self,t,month,phase,payer,category,amount,unit_id=None,cancellable=True):
        iid=self._id('calendar',month,category,unit_id or payer)
        value=round_cents(amount)
        self.charge_lines.append({'month':month,'category':category,'unit_id':unit_id,
            'payer':payer,'payee':self.bridge.digital_vendor_actor,'exact_cents':_rational(amount),
            'rounded_cents':value,'rounding_difference_cents':_rational(Fraction(value)-amount),
            'invoice_id':iid if value else None})
        if value:
            t=self.issue_enterprise(t,iid,payer,self.bridge.digital_vendor_actor,value,
                                   Moment(month,1),Moment(month,phase),category,cancellable)
            self.enterprise_cost_ids.add(iid);self.digital_ids.add(iid)
        return t,iid if value else None

    def prepare(self,t,month,units):
        t=super().prepare(t,month,units)
        self.supported={};self.support_hours_used=Fraction();self.qualification_hours_used=Fraction()
        self.integration_hours_used=Fraction()
        year_index=self.calendar[month]['annual_period_index']
        current=parameters_at(self.annual,self.paths,year_index)
        site=operation(self.cell,self.system,current,capability_at(self.annual,year_index),self.bridge.digital_enabled)
        for b in self.enterprise.businesses:
            if self.active(b,month):
                t,_=self.charge(t,month,3,b.actor_id,'site_digital_subscription',
                               exact(site['digital_site_cost_usd'])*100/12,cancellable=False)
        for u in units:
            if u.status=='installed' and u.unit_id not in self.vintage:self.vintage[u.unit_id]=year_index
            if u.status!='installed' and not (u.status=='transit' and u.ready_month<=month):continue
            phase=3 if u.status=='installed' else 4
            target=self.target_vintage(u,month)
            level=parameters_at(self.annual,self.paths,target)['digital_cost_usd'] if self.bridge.digital_enabled else 0
            payer=self.payer('support' if phase==3 else 'commission',u)
            t,digital=self.charge(t,month,phase,payer,'robot_digital_subscription',exact(level)*100/12,u.unit_id)
            upgrade=u.unit_id in self.vintage and self.robot_signature(self.vintage[u.unit_id])!=self.robot_signature(target)
            t,qualification=self.charge(t,month,phase,payer,'software_upgrade_qualification',
                Fraction(self.bridge.upgrade_cost_cents_per_robot if upgrade else 0),u.unit_id)
            self.robot_invoices[(month,u.unit_id)]=([x for x in (digital,qualification) if x],target,upgrade)
        return t

    def admit(self,t,iid,month,phase,physical_reason,unit=None,operator_id=None):
        action=t.invoice(iid).category
        if action not in ('support','commission'):
            return super().admit(t,iid,month,phase,physical_reason,unit,operator_id)
        extras,target,upgrade=self.robot_invoices[(month,unit.unit_id)]
        op=self.robot_operation(target);hours=exact(op['support_hours'])/12
        qualification=Fraction(self.bridge.upgrade_hours_per_robot if upgrade else 0)
        integration=exact(self.annual['integration_hours']) if action=='commission' else Fraction()
        reason=physical_reason
        if capability_at(self.annual,target)<self.cell['capability_threshold']:
            reason=reason or 'assumed_capability_below_cell_threshold'
        if self.support_hours_used+self.qualification_hours_used+hours+qualification>self.bridge.support_hours_per_month:
            reason=reason or 'shared_support_and_qualification_hours'
        if self.integration_hours_used+integration>self.bridge.integration_hours_per_month:
            reason=reason or 'allocated_process_integration_hours'
        # Parent success has no support/commission side effects. Evaluate all
        # contingent payments on an immutable candidate, then commit together.
        candidate,parent_reason=super().admit(t,iid,month,phase,reason,unit,operator_id)
        if parent_reason:
            t=candidate;reason=parent_reason
        else:
            for extra in extras:
                candidate=candidate.settle_invoice(extra+':pay',extra,Moment(month,phase),provenance=self.provenance)
                if candidate.invoice(extra).outstanding_cents:
                    reason='funding:'+candidate.invoice(extra).category;break
            if not reason:
                self.vintage[unit.unit_id]=target
                self.support_hours_used+=hours;self.qualification_hours_used+=qualification
                self.integration_hours_used+=integration
                ramp=Fraction(self.plan.system.first_month_ramp_numerator,self.plan.system.first_month_ramp_denominator) if action=='commission' else Fraction(1)
                self.supported[unit.unit_id]={'unit_id':unit.unit_id,'operator_id':unit.operator_id,
                    'annual_period_index':target,'software_year':self.catalog['base_year']+target,
                    'ramp_fraction':_rational(ramp),'support_hours':_rational(hours),
                    'upgrade_qualification_hours':_rational(qualification),'upgrade_performed':upgrade,
                    'initial_integration_hours':_rational(integration),
                    'capacity_units':_rational(exact(op['accepted_units'])/12*ramp)}
                return candidate,''
            group=[iid]
            first=self.first_rent.get((month,unit.unit_id)) if action=='commission' else None
            if first:group.insert(0,first)
            for invoice in group:
                t=t.cancel_invoice(invoice+':calendar-cancel',invoice,Moment(month,phase),provenance=self.provenance)
            self._record(Moment(month,phase),'blocked_group',invoice_ids=group+extras,reason=reason,
                         committed_cash_cents=0,unit_id=unit.unit_id)
        for extra in extras:
            t=t.cancel_invoice(extra+':cancel',extra,Moment(month,phase),provenance=self.provenance)
        self.bridge_events.append({'month':month,'unit_id':unit.unit_id,'action':'support_or_upgrade_blocked',
                                   'reason':reason,'retained_software_year':self.catalog['base_year']+self.vintage[unit.unit_id] if unit.unit_id in self.vintage else None})
        return t,reason

    def dispatch_output(self,month,operator,robot_capacity):
        cohorts=[x for x in self.supported.values() if x['operator_id']==operator.operator_id]
        raw=sum((rational(x['ramp_fraction'])*self.plan.system.full_output_units_per_robot_month for x in cohorts),Fraction())
        assert raw==robot_capacity,'Supported unit/ramp identity failed'
        effective=sum((rational(x['capacity_units']) for x in cohorts),Fraction())
        assert effective<=robot_capacity
        demand,robot,detail=super().dispatch_output(month,operator,effective)
        detail['effective_calendar_capacity_units']=_rational(effective)
        detail['supported_unit_ids']=[x['unit_id'] for x in cohorts]
        return demand,robot,detail

    def close(self,t,month,units,supported):
        super().close(t,month,units,supported)
        assert set(self.supported)==set(supported),'Support identity lost across bridge'
        market=self.market_months[-1];base_hours=exact(self.cell['human_hours_per_unit'])
        current=self.calendar[month]['effective_parameters']
        efficiency=exact(current['digital_efficiency']) if self.bridge.digital_enabled else Fraction()
        hours=[]
        for row in market['operators']:
            b=self.business[row['operator_id']]
            human=rational(row['human_delivered_units']);total=rational(row['total_delivered_units'])
            retained=human*base_hours*(1-efficiency)
            staff=next((i for i in t.invoices if i.invoice_id==self._id('enterprise',b.operator_id,month,'human_staff')),None)
            hours.append({'operator_id':b.operator_id,'baseline_equivalent_service_hours':_rational(total*base_hours),
                'retained_human_task_hours':_rational(retained),'released_human_task_hours':_rational(total*base_hours-retained),
                'staff_commitment_cents':staff.face_cents if staff else 0,
                'current_period_staff_cash_paid_cents':staff.paid_cents if staff else 0,
                'removed_payroll_cents':None,'payroll_missing_reason':'Paid commitments are fixed; released task time is not payroll removed'})
        market['baseline_equivalent_labor_hours']=_rational(sum((rational(x['baseline_equivalent_service_hours']) for x in hours),Fraction()))
        market['labor_conversion_unknown_reason']=None
        market['labor_conversion_basis']='Explicit synthetic cleaning-zone contract; not an observed hours-per-bundle estimate'
        self.bridge_months.append({**self.calendar[month],'cohorts':list(self.supported.values()),
            'support_hours_used':_rational(self.support_hours_used),'qualification_hours_used':_rational(self.qualification_hours_used),
            'hours_capacity':self.bridge.support_hours_per_month,'integration_hours_used':_rational(self.integration_hours_used),
            'integration_hours_capacity':self.bridge.integration_hours_per_month,'human_work':hours})

    def bridge_result(self,r):
        years=[]
        for year in sorted({x['calendar_year'] for x in self.calendar}):
            indices=[x['month'] for x in self.calendar if x['calendar_year']==year]
            service=sum((rational(self.market_months[m]['total_delivered_units']) for m in indices),Fraction())
            exposure=sum((len(self.bridge_months[m]['cohorts']) for m in indices),0)
            years.append({'calendar_year':year,'months_observed':indices,'whole_month_count':len(indices),
                'accepted_cleaning_zones':_rational(service),'supported_robot_months':exposure,
                'supported_robot_year_equivalents':_rational(Fraction(exposure,12)),
                'annualized_service':None,'annualization_reason':'Observed partial-year sums are not extrapolated'})
        invoices=[i for i in r['closing_treasury']['invoices'] if i['invoice_id'] in self.digital_ids]
        nondigital=operation(self.cell,self.system,self.annual,capability_at(self.annual,0),False)
        return {'schema_version':'monthly-calendar-bridge/0.1','evidence_status':'synthetic_explicit_unit_and_contract_mapping',
            'inputs':asdict(self.bridge),'annual_parameters':self.annual,'resolved_digital_paths':self.paths,
            'unit_contract':{'work_id':WORK,'annual_cell_id':self.cell['cell_id'],'monthly_unit':'accepted cleaning zone',
                'annual_unit':self.cell['output_unit'],'monthly_units_per_annual_unit':{'numerator':1,'denominator':1},
                'original_floor_bundle_conversion':None,'mapping_status':'New synthetic matched unit, not conversion of historical WORK-FLOOR-BUNDLE-SYN-02',
                'baseline_human_hours_per_zone':self.cell['human_hours_per_unit'],'wage_usd_hour':self.cell['wage_usd_hour']},
            'cost_and_resource_contract':{
                'manufacturing':'Annual catalog cost per start maps to each actual paid monthly start; rejected starts remain sunk, with no second expected-yield divisor',
                'manufacturing_per_start_cents':self.plan.system.bundled_start_cents,
                'integration':'Annual process-integration hours at 60 USD/hour map to each new monthly commissioned unit; opening stock is already integrated',
                'integration_per_new_unit_cents':self.plan.system.commissioning_cents,
                'physical_support':'Annual operation(digital=False) expense / 12 is rounded once per monthly booking; availability and output ramp do not discount the bill again',
                'exact_physical_support_cents_per_month':_rational(exact(nondigital['robot_operating_cost_usd'])*100/12),
                'physical_support_cents_per_month':self.plan.system.support_cents_per_robot_month,
                'additional_digital':'Annual digital_cost_usd / 12 per actually supported robot, plus annual site digital cost / 12 per active business; separate supplier, once in enterprise outlay',
                'shipping':'Explicit monthly shipping expense has no separate annual-reference counterpart; it remains counted',
                'staffing':'Fixed paid-shift commitments plus actual human work; digital capacity floors to whole zones without assuming payroll removal',
                'support_pool_annual_hours':self.annual['support_budget_hours'],
                'support_hours_allocated_here_per_year':12*self.bridge.support_hours_per_month,
                'integration_pool_annual_hours':self.annual['integration_budget_hours'],
                'integration_hours_allocated_here_per_year':12*self.bridge.integration_hours_per_month,
                'other_annual_markets_executed':False},
            'metric_lineage':[
                {'metric':'monthly accepted robot capacity','equation':'sum annual operation.accepted_units / 12 * actual cohort ramp, only for paid supported unit IDs',
                 'inputs':'annual cell, dated path, capability, unit software vintage, support admission and ramp',
                 'implementation':'operation; _BridgedEnterprise.admit/dispatch_output','basis':'synthetic source function and new matched cleaning unit'},
                {'metric':'calendar-year service and exposure','equation':'sum actual observed months; supported unit-months / 12 for robot-year equivalents',
                 'inputs':'calendar_bridge.months and enterprise.months','implementation':'_BridgedEnterprise.bridge_result',
                 'basis':'partial-year aggregation; no extrapolation or extra annual fleet'},
                {'metric':'retained human task hours','equation':'delivered human zones * baseline hours per zone * (1 - current digital efficiency)',
                 'inputs':'actual human delivery, selected cell and calendar-year digital path','implementation':'_BridgedEnterprise.close',
                 'basis':'task-time assumption; paid-shift commitment and settled payroll remain separate'},
                {'metric':'human service capacity','equation':'floor(scheduled staff cents / (100 * wage per hour * baseline hours per zone * (1 - digital efficiency)))',
                 'inputs':'explicit monthly paid-shift schedule, selected-cell wage/hours and dated efficiency; standard worlds begin with 500 incumbent and 100 entrant baseline zones',
                 'implementation':'bridge_case_inputs; _Enterprise.dispatch_output','basis':'fixed paid staffing; conservative whole-zone capacity'},
                {'metric':'digital and upgrade cash','equation':'sum settled uniquely identified supplier invoices; fees are included once in enterprise outlay',
                 'inputs':'annual robot/site rates divided by 12, actual support, declared upgrade price',
                 'implementation':'_BridgedEnterprise.charge/admit; Treasury','basis':'synthetic resource bills, exact cents and disclosed rounding'},
                {'metric':'qualified operating cohort','equation':'commit vintage and resource usage only after physical, rent, software and upgrade bookings all settle',
                 'inputs':'explicit qualification price/hours, shared support allocation and existing cohort vintage',
                 'implementation':'_BridgedEnterprise.admit','basis':'assumed qualification contract, not real model rights or field validation'},
                {'metric':'resource allocation','equation':'monthly support + upgrade hours <= allocated support; commissioning integration hours <= allocated integration; each allocation * 12 <= annual pool',
                 'inputs':'annual budgets and declared monthly shares','implementation':'bridge_context; _BridgedEnterprise.admit',
                 'basis':'one monthly market allocation; other annual markets are not simultaneously executed'}],
            'months':self.bridge_months,'calendar_years':years,'events':self.bridge_events,'charge_lines':self.charge_lines,
            'cash':{'digital_and_upgrade_paid_cents':sum(i['paid_cents'] for i in invoices),
                'digital_and_upgrade_unpaid_cents':sum(i['outstanding_cents'] for i in invoices),
                'included_in_enterprise_outlay':True,'add_to_consolidated_outlay_again':False},
            'limits':['The monthly unit IDs are the only fleet; annual fleet stocks and site estimates are not added',
                'Whole-month billing and exposure use one twelfth of annual rates; each invoice rounds once to cents',
                'Physical support, manufacturing and integration are mapped separately; shipping remains an explicit additional monthly expense',
                'Actual paid starts/rejects govern manufacturing; the annual expected-yield divisor is not applied again',
                'Qualified component bundles remain monthly synthetic units; annual actuator and board inventories are not imported',
                'Annual capability is an exogenous synthetic path; no endogenous learning/data premium is added',
                'Paid calendar upgrades require funds and shared support/qualification hours; frozen cohorts retain their vintage',
                'Four architecture ledgers, model/data rights qualification, acquisition transitions and full empirical economics remain pending']}


def bridge_source_hashes():
    paths=['model/calendar_bridge.py','model/engine.py','model/trajectories.py','model/assumptions.json']
    return {**finance_source_hashes(),**{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in paths}}


def run_bridged_enterprise(plan,treasury,contracts,enterprise,finance,bridge):
    policy=_BridgedEnterprise(plan,contracts,treasury,enterprise,finance,bridge)
    r=run_monthly(plan,treasury,commercial=policy)
    r.update(schema_version='monthly-deployment/0.5',scope='synthetic_monthly_calendar_and_digital_bridge',
             ownership='one_title_owner_per_unit_separate_from_custody_and_workflow')
    r['commercial']=policy.result(r)
    r['commercial']['limits']=['Scope is defined by calendar_bridge.limits, finance.limits and enterprise inputs']
    r['enterprise']=policy.enterprise_result(r)
    r['enterprise']['limits']=[x for x in r['enterprise']['limits'] if not x.startswith(('No automatic loan','No annual cleaning-zone'))]
    r['finance']=policy.finance_result(r)
    r['calendar_bridge']=policy.bridge_result(r)
    r['source_sha256']=bridge_source_hashes()
    r=wire_rationals(r)
    r['rational_wire_format']='decimal_string_numerator_and_denominator_for_lossless_JSON'
    r['case_hash']=hashlib.sha256(json.dumps(r,sort_keys=True,separators=(',',':')).encode()).hexdigest()
    return json.loads(json.dumps(r))


def replay_bridge(saved):
    if not isinstance(saved,dict) or saved.get('schema_version')!='monthly-deployment/0.5':raise ValueError('Saved calendar-bridge case required')
    e=dict(saved['enterprise']['inputs']);e['market']=Market(**e['market'])
    for key,cls in [('businesses',Business),('moves',CustomerMove),('equity',Equity)]:e[key]=tuple(cls(**x) for x in e[key])
    f=dict(saved['finance']['inputs']);f['loans']=tuple(TermLoan(**x) for x in f['loans'])
    return run_bridged_enterprise(*restore_opening_inputs(saved),EnterprisePlan(**e),FinancePlan(**f),Bridge(**saved['calendar_bridge']['inputs']))


def bridge_case_inputs(finance_inputs=None,bridge_inputs=None,human_only=False):
    if type(human_only) is not bool:raise ValueError('Explicit human-only Boolean required')
    if bridge_inputs is not None and not isinstance(bridge_inputs,dict):raise ValueError('Bridge inputs must be an object')
    x=financed_case_inputs(finance_inputs);b=Bridge(**(bridge_inputs or {}))
    p,t,cs,e=reference_inputs(entrant_cash=x['entrant_cash_cents'],incumbent_procurement=x['incumbent_procurement_month'],
                             response_month=x['response_month'],delayed_receipts=x['delayed_receipts'])
    c,a,paths,cell,system,calendar=bridge_context(b,p.months)
    nondigital=operation(cell,system,a,capability_at(a,0),False)
    per_month_baseline=cell['annual_units_per_site']//12
    assert per_month_baseline*12==cell['annual_units_per_site']
    ceiling=1000
    spec=replace(p.system,system_id=system['system_id'],work_id=WORK,full_output_units_per_robot_month=ceiling,
        bundled_start_cents=round_cents(exact(system['manufacture_cost_usd'])*100),
        commissioning_cents=round_cents(exact(a['integration_hours'])*6000),
        support_cents_per_robot_month=round_cents(exact(nondigital['robot_operating_cost_usd'])*100/12))
    operators=tuple(replace(o,demand_units_by_month=(650,)*p.months,
                           opening_installed=0 if human_only else o.opening_installed,
                           requested_additions=0 if human_only else o.requested_additions) for o in p.operators)
    starts=() if human_only else p.starts+((Start('later-candidate',3,1,1),) if x['later_start_candidate'] else ())
    p=replace(p,plan_id='calendar-cleaning-bridge',operators=operators,system=spec,starts=starts)
    cs=tuple(replace(contract,purchase_cents_per_robot=round_cents(exact(system['price_usd'])*exact(a['price_multiplier'])*100)) for contract in cs)
    businesses=[]
    for business in e.businesses:
        paid_capacity=per_month_baseline if business.operator_id=='incumbent' else 100
        capacities=[]
        for row in calendar:
            efficiency=exact(row['effective_parameters']['digital_efficiency']) if b.digital_enabled else Fraction()
            capacities.append(int(Fraction(paid_capacity)/(1-efficiency)))
        staff=round_cents(paid_capacity*exact(cell['human_hours_per_unit'])*exact(cell['wage_usd_hour'])*100)
        businesses.append(replace(business,human_capacity_by_month=tuple(capacities),human_staff_cents_by_month=(staff,)*p.months,
            price_cents_per_unit_by_month=(2000,)*p.months,material_cents_per_delivered_unit=100))
    e=replace(e,market=Market(WORK,'incumbent','end_buyers',500,100,50),businesses=tuple(businesses))
    if x['rescue_equity_cents']:e=replace(e,equity=e.equity+(Equity('scheduled-rescue',x['rescue_equity_month'],'investor','entrant',x['rescue_equity_cents']),))
    t=replace(t,accounts=t.accounts+(Account('capital_lender',x['lender_cash_cents']),Account(b.digital_vendor_actor,0)))
    loans=(TermLoan('entrant-term','capital_lender','entrant',x['loan_cents'],x['draw_month'],x['maturity_month'],x['monthly_rate_basis_points'],10000,x['principal_repayment_policy']),) if x['loan_cents'] else ()
    return p,t,cs,e,FinancePlan(loans,x['payment_priority'],x['default_policy'],x['reinvestment_reserve_cents']),b


def run_bridge_case(finance_inputs=None,bridge_inputs=None,human_only=False):
    return run_bridged_enterprise(*bridge_case_inputs(finance_inputs,bridge_inputs,human_only))


def bridge_witness_options():
    funded={'entrant_cash_cents':10_000_000,'loan_cents':0}
    flat={'annual_overrides':{'capability_progress':0}}
    paths={'schema_version':'digital-annual-paths/0.1','base_year':2026,'epistemic_status':'synthetic_assumption',
           'digital_efficiency':[.15,.35,.4],'coordination':[.15,.4,.5],'digital_cost_usd':[1500,1200,1000]}
    improving={'digital_paths':paths}
    return {
        'C00_human_baseline':{'finance_inputs':funded,'bridge_inputs':{**flat,'digital_enabled':False},'human_only':True},
        'C01_digital_human':{'finance_inputs':funded,'bridge_inputs':flat,'human_only':True},
        'C10_robot_base':{'finance_inputs':funded,'bridge_inputs':{**flat,'digital_enabled':False}},
        'C11_robot_digital':{'finance_inputs':funded,'bridge_inputs':flat},
        'calendar_improving':{'finance_inputs':funded,'bridge_inputs':improving},
        'frozen_cohorts':{'finance_inputs':funded,'bridge_inputs':{**improving,'software_policy':'frozen_cohort'}},
        'upgrade_hours_available':{'finance_inputs':funded,'bridge_inputs':{**improving,'support_hours_per_month':65}},
        'calendar_financing_pressure':{'bridge_inputs':improving},
    }


def bridge_artifact():
    inputs={name:{'finance_inputs':financed_case_inputs(x.get('finance_inputs')),
                  'bridge_inputs':asdict(Bridge(**x.get('bridge_inputs',{}))),
                  'human_only':x.get('human_only',False)} for name,x in bridge_witness_options().items()}
    cases={name:run_bridge_case(**x) for name,x in inputs.items()}
    summary=[]
    for name,r in cases.items():
        bridge=r['calendar_bridge'];enterprise=r['enterprise'];cash=enterprise['consolidation']
        service=sum((rational(m['total_delivered_units']) for m in enterprise['months']),Fraction())
        hours=sum((rational(x['retained_human_task_hours']) for m in bridge['months'] for x in m['human_work']),Fraction())
        committed=sum(x['staff_commitment_cents'] for m in bridge['months'] for x in m['human_work'])
        paid=sum(x['current_period_staff_cash_paid_cents'] for m in bridge['months'] for x in m['human_work'])
        summary.append({'case':name,'accepted_cleaning_zones':_rational(service),'retained_human_task_hours':_rational(hours),
            'staff_commitment_cents':committed,'current_period_staff_cash_paid_cents':paid,
            'external_physical_and_enterprise_cash_cents':cash['external_physical_outlay_cents']+cash['external_enterprise_outlay_cents'],
            'digital_and_upgrade_paid_cents':bridge['cash']['digital_and_upgrade_paid_cents'],
            'supported_robot_months':sum(len(m['cohorts']) for m in bridge['months']),
            'upgrade_count':sum(x['upgrade_performed'] for m in bridge['months'] for x in m['cohorts']),
            'entrant_closing_cash_cents':r['months'][-1]['closing_cash_cents']['entrant'],
            'first_debt_default_month':r['finance']['first_debt_default_month'].get('entrant')})
    by={r['case']:r for r in summary};joint={}
    for metric in ('accepted_cleaning_zones','retained_human_task_hours'):
        values={name:rational(by[name][metric]) for name in ('C00_human_baseline','C01_digital_human','C10_robot_base','C11_robot_digital')}
        joint[metric]={'values':{k:_rational(v) for k,v in values.items()},
                       'robot_increment_after_digital':_rational(values['C11_robot_digital']-values['C01_digital_human']),
                       'interaction':_rational(values['C11_robot_digital']-values['C10_robot_base']-values['C01_digital_human']+values['C00_human_baseline'])}
    out={'schema_version':'calendar-bridge-experiments/0.1','evidence_status':'synthetic_explicit_service_and_calendar_contract',
         'source_sha256':bridge_source_hashes(),'case_inputs':inputs,'summary':summary,'joint':joint,'cases':cases,
         'comparison_boundary':'Fixed human staffing and customer-move policy across four ample-capital branches; released task time is not payroll removed. This is not the stronger optimized conventional coordination comparator.'}
    out=wire_rationals(out)
    out['artifact_hash']=hashlib.sha256(json.dumps(out,sort_keys=True,separators=(',',':')).encode()).hexdigest()
    return out
