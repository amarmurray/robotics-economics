"""Qualified supply and annual support through paid crews and actual renewals.

One Treasury and physical execution. Annual support engineers, integration
capacity and each operating company's site crew are different resources.
No additional outside work or cost is invented for annual reservations.
"""
from dataclasses import asdict, replace
import hashlib
import json

from model.annual_resource_ledger import AnnualResourceAdmission, read_resources
from model.calendar_bridge import ROOT, Bridge, bridge_context, rational
from model.component_inventory import ComponentInventory, ComponentContract, ComponentReceipt, Replacement, read_components, zero
from model.competitive_renewals import Competition
from model.enterprise_finance import FinancePlan, TermLoan
from model.entry_transitions import Transition
from model.monthly_architectures import canonical_wire
from model.monthly_commercial import restore_opening_inputs
from model.monthly_deployment import TypedComponentSystem, run_monthly
from model.monthly_enterprise import Business, CustomerMove, EnterprisePlan, Equity, Market
from model.shared_workforce import Workforce
from model.staffed_renewals import (_StaffedRenewals, staffed_renewals_inputs,
    staffed_renewals_result, staffed_renewals_summary, source_hashes as crew_hashes)


class _QualifiedStaffing(AnnualResourceAdmission, _StaffedRenewals):
    def __init__(self, plan, contracts, treasury, enterprise, finance, bridge, competition, transition, crews, resources):
        super().__init__(plan, contracts, treasury, enterprise, finance, bridge, competition, transition, crews)
        self.initialize_resources(resources)


def source_hashes():
    paths=('model/qualified_staffing.py','model/annual_resource_ledger.py','model/component_inventory.py')
    return {**crew_hashes(),**{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in paths}}


def run_qualified_staffing(plan, treasury, contracts, enterprise, finance, bridge, competition, transition, crews, resources, components):
    policy=_QualifiedStaffing(plan,contracts,treasury,enterprise,finance,bridge,competition,transition,crews,resources)
    if components.onboard_configuration!=policy.annual['onboard_configuration'] or components.system_id!=plan.system.system_id:
        raise ValueError('Qualified parts must match the declared annual and physical system')
    materials=ComponentInventory(components)
    execution=run_monthly(plan,treasury,commercial=policy,materials=materials)
    return qualified_staffing_result(execution,policy,materials)


def qualified_staffing_result(execution,policy,materials):
    """Format the already completed shared execution without creating another run."""
    r=staffed_renewals_result(execution,policy)
    r.update(schema_version='qualified-staffing-window/0.1',scope='synthetic_qualified_parts_annual_support_paid_crews_entry_and_renewal')
    r.pop('case_hash')
    r['annual_resources']=policy.resource_result()
    a=r['annual_resources']
    for row in a['metric_lineage']:
        row['implementation']=row['implementation'].replace('_ResourceEnterprise.__init__','AnnualResourceAdmission.initialize_resources').replace('_ResourceEnterprise.','AnnualResourceAdmission.')
    a['metric_lineage'][-1].update(equation='funded supported units and separate paid site crews constrain offers, actual awards and delivery',
        implementation='_StaffedRenewals.finish_shipping/close; _CompetitiveEnterprise.finish_shipping',
        basis='one entry/renewal execution, with fixed separate offer mandates after common ownership')
    a['limits']=[x for x in a['limits'] if not x.startswith(('Annual component vectors','These cases do not join'))]+[
        'Typed qualified parts and share entry are joined here. Four intelligence architectures, asset recovery and endogenous learning remain separate contracts.',
        'Shared provider support/integration ceilings do not pool separate operating-company site crews or legal cash accounts.']
    r['component_inventory']=materials.result(r['units'])
    r['renewing_entry']['limits']=[x for x in r['renewing_entry']['limits'] if not x.startswith('Separate operating-company crews')]+[
        'Separate paid crews, annual support/integration and typed qualified parts are joined here; architecture choice, asset recovery and learning remain separate.']
    r['qualified_staffing']=dict(
        information_clock='Dated qualified parts and annual/monthly provider capacity gate physical admission. Only actual prior completed service qualifies staffing notice. A later failed support or replacement booking does not revoke binding notice. Site crews then reserve retained duties and funded overtime before actual awards.',
        resource_boundary='Provider support engineers, integration capacity and each legal operator site crew are separate. Outside annual reservations are unavailable capacity, not executed outside service, payroll or cash.',
        component_boundary='One synthetic catalog BOM per whole paid start, including rejected starts. A named actuator replacement is due in month4. Consigned parts and repair labor remain inside the existing paid manufacture/support bundles; their independent supplier cash or labor capacity is not modeled.',
        decision_gate='A removable paid block needs a forward qualified-service and fallback plan, not only purchased robots or one successful prior month. Check both cleaning and separately due inventory service.',
        limits=['No actual BOM, support entitlement, staffing agreement, maintenance rate, payroll removal or all-service ROI is measured.',
                'Eight monthly periods, deterministic installed-unit-first admission, fixed bids and no within-shift travel/deadlines; not an optimized portfolio or staffing policy.',
                'The other five cells are measurement/decision boundaries, not numerically calibrated or jointly executed in this fixture.',
                'Annual reservations carry no invented expense; outside inventory service and its payer are executed separately on the site crew. Do not sum these resource pools or service units.'])
    r['source_sha256']=source_hashes();r=canonical_wire(r)
    r['case_hash']=hashlib.sha256(json.dumps(r,sort_keys=True,separators=(',',':')).encode()).hexdigest()
    return json.loads(json.dumps(r))


def default_components(plan):
    count=sum(s.quantity for s in plan.starts)
    receipts=() if not count else (
        ComponentReceipt('manufacturing-actuators','actuator_h',count*24,0,0,0),
        ComponentReceipt('manufacturing-boards','embedded_lpddr_boards',count,0,0,0),
        ComponentReceipt('replacement-actuators','actuator_h',count,0,0,0))
    replacements=tuple(Replacement('replace-'+s.order_id+'-'+str(i+1),f'start-{s.order_id}-{i+1}',4,{**zero(),'actuator_h':1})
        for s in plan.starts for i in range(s.quantity))
    return ComponentContract('SYN-H','standard',zero(),receipts,replacements)


def qualified_staffing_inputs(inputs=None):
    if inputs is None:inputs={}
    if not isinstance(inputs,dict) or set(inputs)-{'staffed','resources','components'}:raise ValueError('Unknown qualified staffing inputs')
    if not isinstance(inputs.get('staffed',{}),dict):raise ValueError('Staffed inputs must be an object')
    x=dict(inputs.get('staffed',{}));crews=x.get('crews',{})
    if not isinstance(crews,dict) or not isinstance(crews.get('incumbent',{}),dict):raise ValueError('Crew controls must be objects')
    x['crews']={**crews,'incumbent':{'target_blocks':1,**crews.get('incumbent',{})}}
    args=list(staffed_renewals_inputs(x));p=args[0]
    p=replace(p,system=TypedComponentSystem(**{**asdict(p.system),
        'components_per_start':0,'service_components_per_robot_month':0}),opening_components=0,qualified_component_receipts=(0,)*p.months)
    args[0]=p
    years=sorted({row['calendar_year'] for row in bridge_context(args[5],p.months)[-1]})
    resources=read_resources(inputs.get('resources',{'years':[{'calendar_year':y} for y in years]}))
    components=read_components(inputs['components']) if 'components' in inputs else default_components(p)
    return (*args,resources,components)


def run_qualified_staffing_case(inputs=None):return run_qualified_staffing(*qualified_staffing_inputs(inputs))


def replay_qualified_staffing(saved):
    if not isinstance(saved,dict) or saved.get('schema_version')!='qualified-staffing-window/0.1':raise ValueError('Complete qualified staffing case required')
    try:
        e=dict(saved['enterprise']['inputs']);e['market']=Market(**e['market'])
        for key,cls in [('businesses',Business),('moves',CustomerMove),('equity',Equity)]:e[key]=tuple(cls(**x) for x in e[key])
        f=dict(saved['finance']['inputs']);f['loans']=tuple(TermLoan(**x) for x in f['loans'])
        return run_qualified_staffing(*restore_opening_inputs(saved),EnterprisePlan(**e),FinancePlan(**f),Bridge(**saved['calendar_bridge']['inputs']),
            Competition(**saved['competition']['inputs']),Transition(**saved['entry_transition']['inputs']),
            {op:Workforce(**w) for op,w in saved['staffed_renewals']['inputs'].items()},
            read_resources(saved['annual_resources']['inputs']),read_components(saved['component_inventory']['inputs']))
    except (KeyError,TypeError,AttributeError) as exc:raise ValueError('Incomplete qualified staffing inputs') from exc


def available_support(minutes):
    return {'years':[{'calendar_year':2026,'support_reserved_elsewhere_minutes':720000-minutes},{'calendar_year':2027}]}


def qualified_staffing_worlds():
    parts=default_components(qualified_staffing_inputs()[0])
    late=replace(parts,receipts=tuple(replace(x,qualified_month=6) if x.receipt_id=='replacement-actuators' else x for x in parts.receipts))
    unqualified=replace(parts,receipts=tuple(replace(x,qualified_month=None) if x.pool=='embedded_lpddr_boards' else x for x in parts.receipts))
    scarce={'resources':available_support(2599)}
    return {
        'qualified_control':{},
        'exact_support_through_december':{'resources':available_support(2600)},
        'one_minute_short_after_notice':scarce,
        'retain_staff_through_support_gap':{**scarce,'staffed':{'crews':{'incumbent':{'target_blocks':None}}}},
        'prepaid_fallback_through_support_gap':{**scarce,'staffed':{'crews':{'incumbent':{'overtime_minutes_per_month':5000}}}},
        'replacement_qualified_in_january':{'components':canonical_wire(asdict(late))},
        'unqualified_board_no_notice':{'components':canonical_wire(asdict(unqualified))},
        'human_only_same_service':{'staffed':{'entry':{'market':{'incumbent_robots':0,'entrant_robots':0}},'crews':{'incumbent':{'target_blocks':None}}}},
        'equal_robot_access_shared_support':{'resources':available_support(2600),'staffed':{'entry':{'market':{'incumbent_robots':1,'entrant_robots':1}}}},
    }


def qualified_staffing_summary(name,r):
    s=staffed_renewals_summary(name,r)
    s.update(supported_robot_months=sum(len(x['supported_unit_ids']) for x in r['annual_resources']['months']),
        annual_blocked_bookings=sum(x['reason'] in ('annual_support_commitments','annual_integration_commitments') for x in r['annual_resources']['attempts']),
        completed_replacements=sum(x['completed'] for x in r['component_inventory']['replacement_outcomes']),
        started_units=sum(m['flows']['started'] for m in r['months']),
        closing_qualified_parts=r['component_inventory']['closing_qualified_parts'],closing_quarantined_parts=r['component_inventory']['closing_quarantined_parts'])
    return s


def qualified_staffing_artifact():
    options=qualified_staffing_worlds();cases={k:run_qualified_staffing_case(v) for k,v in options.items()}
    return canonical_wire(dict(schema_version='qualified-staffing-artifact/0.1',case_inputs=options,cases=cases,
        summary=[qualified_staffing_summary(k,r) for k,r in cases.items()],source_sha256=source_hashes(),
        comparison_boundary='One synthetic physical, cash, part, annual-provider and site-crew history. Forward service constraints can outlive a successful month that triggered binding staffing notice. Retained staff, prepaid fallback and the human-only alternative keep the same two service obligations. No empirical payroll or lifecycle return is inferred.'))


def qualified_staffing_catalog():
    data=json.loads((ROOT/'model/results/qualified_staffing.json').read_text())
    if data['source_sha256']!=source_hashes():raise ValueError('Qualified staffing export is stale; regenerate')
    return {k:v for k,v in data.items() if k!='cases'}|{'cases':{'qualified_control':data['cases']['qualified_control']}}
