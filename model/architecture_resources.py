"""Four intelligence arrangements on one dated resource, part and cash ledger.

The shared admission wrapper does not import competitive actor semantics.
All resource requirements and qualification gates remain synthetic premises.
"""
from dataclasses import asdict, replace
from fractions import Fraction
import hashlib
import json

from model.annual_resource_ledger import AnnualResourceAdmission, read_resources
from model.calendar_bridge import ROOT, Bridge, bridge_context, rational
from model.component_inventory import ComponentContract, ComponentInventory, ComponentReceipt, Replacement, read_components, zero
from model.enterprise_finance import FinancePlan, TermLoan
from model.monthly_architectures import (ArchitectureExecution, _ArchitectureEnterprise,
    architecture_case_inputs, architecture_execution_hashes, architecture_result, canonical_wire)
from model.monthly_commercial import restore_opening_inputs
from model.monthly_deployment import TypedComponentSystem, _rational, run_monthly
from model.monthly_enterprise import Business, CustomerMove, EnterprisePlan, Equity, Market


class _ResourceArchitecture(AnnualResourceAdmission, _ArchitectureEnterprise):
    def __init__(self, plan, contracts, treasury, enterprise, finance, bridge, architecture, resources):
        super().__init__(plan, contracts, treasury, enterprise, finance, bridge, architecture)
        self.initialize_resources(resources)


def source_hashes():
    paths = ('model/annual_resource_ledger.py', 'model/component_inventory.py', 'model/architecture_resources.py')
    return {**architecture_execution_hashes(), **{p: hashlib.sha256((ROOT / p).read_bytes()).hexdigest() for p in paths}}


def run_architecture_resources(plan, treasury, contracts, enterprise, finance, bridge, architecture, resources, components):
    policy = _ResourceArchitecture(plan, contracts, treasury, enterprise, finance, bridge, architecture, resources)
    if components.onboard_configuration != policy.annual['onboard_configuration']:
        raise ValueError('Parts must match the architecture annual configuration')
    materials = ComponentInventory(components)
    r = architecture_result(run_monthly(plan, treasury, commercial=policy, materials=materials), policy)
    r.update(schema_version='architecture-resources-window/0.1', scope='synthetic_intelligence_roles_dated_resources_and_compatible_parts')
    r['annual_resources'] = policy.resource_result()
    # The shared ledger has the same units and admission order. Its original
    # competitive wrapper's descriptions are not this arrangement's scope.
    a = r['annual_resources']
    for row in a['metric_lineage'][:4]:
        row['implementation'] = row['implementation'].replace('_ResourceEnterprise.__init__', 'AnnualResourceAdmission.initialize_resources').replace('_ResourceEnterprise.', 'AnnualResourceAdmission.')
    a['metric_lineage'][-1] = {
        'metric': 'qualified operating date and paid service',
        'equation': 'minimum month with actual commissioning; minimum month with supported units equal opening plus requested additions (null if unreached or no robots); accepted robot plus human zones',
        'inputs': 'dated part releases, annual/monthly pools, initial engineering/demonstrations, role Treasury accounts and contingent bills',
        'implementation': 'AnnualResourceAdmission.admit; _ArchitectureEnterprise.admit; run_monthly',
        'basis': 'one active business; no competitive awards or optimal portfolio allocation'}
    a['limits'] = [x for x in a['limits'] if not x.startswith(('Annual component vectors', 'These cases'))] + [
        'Compatible typed parts replace generic modules in this execution; quantities, replacement labor and prices remain assumptions.',
        'No competition, acquisition, recovery, endogenous R&D trials or jointly executed six-cell portfolio is added by this wrapper.']
    r['component_inventory'] = materials.result(r['units'])
    r['architecture_resource_contract'] = {
        'evidence_status': 'synthetic_unqualified_contracts',
        'resource_relationship': 'Four distinct resources: monthly architecture engineering, monthly demonstrations, annual/monthly physical support (including software upgrades), and annual/monthly physical integration. No shared staff identity or substitution is assumed.',
        'atomic_boundary': 'An unperformed contingent qualification/support group consumes no engineering, demonstrations, annual minutes, replacement parts or candidate cash. Earlier manufacture, fixed staffing and other already executed work remain incurred.',
        'failed_research_boundary': 'This is not an executed R&D attempt. It does not erase failed-trial costs from the separate learning-execution model or join that model to this ledger.',
        'cash_boundary': 'Existing role accounts, invoices and transfers are authoritative. Annual reservations are unavailable capacity, not a second expense. Parts and replacement work are included in the existing physical bundles.',
        'baseline': 'One fixed 500-zone/month service objective and unchanged paid digital-human capacity. A zero-robot control uses the same customer/operator arrangement, staffing, digital site work and receipt rules; it is a strong feasible alternative, not an optimized dispatcher.',
        'metric_lineage': a['metric_lineage'] + [
            {'metric': 'initial architecture qualification work', 'equation': 'profile adaptation + validation engineering and demonstration hours, booked once per actually admitted unit',
             'inputs': 'architecture profile, monthly resource ceilings and successful contingent admission', 'implementation': '_ArchitectureEnterprise.prepare/admit',
             'basis': 'distinct synthetic pools; no inferred equivalence with physical support/integration'},
            {'metric': 'compatible manufacturing and replacement issues', 'equation': 'actual paid starts × whole BOM; one named whole replacement vector per successfully supported unit',
             'inputs': 'typed inventory, receipt/qualification dates, unit IDs and actual Treasury', 'implementation': 'ComponentInventory; run_monthly',
             'basis': 'consigned stock priced once through existing bundles; no real product BOM, failure frequency or supplier financing inferred'}],
        'limits': ['All numerical coefficients, role funding, rights and qualification assumptions remain synthetic.',
                   'Released task hours and robot output do not establish removed payroll, added total service, profitability or a preferred architecture.',
                   'One selected cleaning system; no other five-cell workload, endogenous learning or joint competition/acquisition/recovery is executed.']}
    r['architecture_execution']['contract']['resource_hours'] = r['architecture_resource_contract']['resource_relationship']
    r.pop('case_hash')
    r['source_sha256'] = source_hashes()
    r = canonical_wire(r)
    r['case_hash'] = hashlib.sha256(json.dumps(r, sort_keys=True, separators=(',', ':')).encode()).hexdigest()
    return json.loads(json.dumps(r))


def default_parts(plan, configuration):
    quantity = sum(s.quantity for s in plan.starts)
    units = [f'opening-installed-{o.operator_id}-{i+1}' for o in plan.operators for i in range(o.opening_installed)]
    units += [f'start-{s.order_id}-{i+1}' for s in plan.starts for i in range(s.quantity)]
    receipts = []
    if quantity * 24 + len(units):
        receipts.append(ComponentReceipt('actuators-for-starts-and-replacements', 'actuator_h', quantity * 24 + len(units), 0, 0, 0))
    if quantity:
        receipts.append(ComponentReceipt('compatible-manufacturing-boards', 'embedded_lpddr_boards', quantity * (2 if configuration == 'high_memory' else 1), 0, 0, 0))
    replacements = tuple(Replacement('replace-' + uid, uid, 4, {**zero(), 'actuator_h': 1}) for uid in units)
    return ComponentContract('SYN-H', configuration, zero(), tuple(receipts), replacements)


def resource_architecture_inputs(inputs=None):
    if inputs is None: inputs = {}
    if not isinstance(inputs, dict) or set(inputs) - {'architecture', 'bridge', 'resources', 'components', 'start_month'}:
        raise ValueError('Unknown architecture resource inputs')
    for key in ('architecture', 'bridge'):
        if key in inputs and not isinstance(inputs[key], dict): raise ValueError(key + ' must be an object')
    args = list(architecture_case_inputs(inputs.get('architecture'), inputs.get('bridge')))
    plan = args[0]
    if 'start_month' in inputs:
        month = inputs['start_month']
        if type(month) is not int or not 0 <= month < plan.months: raise ValueError('Whole manufacturing month inside the window required')
        plan = replace(plan, starts=tuple(replace(s, month=month) for s in plan.starts))
    typed = TypedComponentSystem(**{**asdict(plan.system), 'components_per_start': 0, 'service_components_per_robot_month': 0})
    plan = replace(plan, system=typed, opening_components=0, qualified_component_receipts=(0,) * plan.months)
    args[0] = plan
    calendar = bridge_context(args[5], plan.months)[-1]
    resources = read_resources(inputs.get('resources', {'years': [{'calendar_year': y} for y in sorted({x['calendar_year'] for x in calendar})]}))
    configuration = args[5].annual_overrides['onboard_configuration']
    components = read_components(inputs['components']) if 'components' in inputs else default_parts(plan, configuration)
    return (*args, resources, components)


def run_resource_architecture_case(inputs=None):
    return run_architecture_resources(*resource_architecture_inputs(inputs))


def replay_resource_architecture_case(saved):
    if not isinstance(saved, dict) or saved.get('schema_version') != 'architecture-resources-window/0.1':
        raise ValueError('Complete architecture resources case required')
    try:
        e = dict(saved['enterprise']['inputs']); e['market'] = Market(**e['market'])
        for key, cls in [('businesses', Business), ('moves', CustomerMove), ('equity', Equity)]:
            e[key] = tuple(cls(**x) for x in e[key])
        f = dict(saved['finance']['inputs']); f['loans'] = tuple(TermLoan(**x) for x in f['loans'])
        return run_architecture_resources(*restore_opening_inputs(saved), EnterprisePlan(**e), FinancePlan(**f),
            Bridge(**saved['calendar_bridge']['inputs']), ArchitectureExecution(**saved['architecture_execution']['inputs']),
            read_resources(saved['annual_resources']['inputs']), read_components(saved['component_inventory']['inputs']))
    except (KeyError, TypeError, AttributeError) as exc:
        raise ValueError('Incomplete or invalid architecture resources inputs') from exc


def resource_architecture_worlds():
    profiles = ('integrated_oem', 'licensed_independent', 'open_adapted', 'model_led_operator')
    # Same unavailable physical integration capacity for all four profiles.
    reserved = {'years': [{'calendar_year': 2026, 'integration_reserved_elsewhere_minutes': 135600}, {'calendar_year': 2027}]}
    out = {name + '_unreserved': {'architecture': {'architecture_id': name}} for name in profiles}
    out.update({name + '_committed': {'architecture': {'architecture_id': name}, 'resources': reserved} for name in profiles})
    out['open_less_adaptation_unreserved'] = {'architecture': {'architecture_id': 'open_adapted', 'architecture_overrides': {'profiles': {'open_adapted': {'adaptation_engineering_hours': 100}}}}}
    out['open_less_adaptation_committed'] = {'architecture': {'architecture_id': 'open_adapted', 'architecture_overrides': {'profiles': {'open_adapted': {'adaptation_engineering_hours': 100}}}}, 'resources': reserved}
    out['licensed_unfunded_model'] = {'architecture': {'role_opening_cash_cents': {'model_supplier': 0}}, 'resources': reserved}
    components = default_parts(resource_architecture_inputs()[0], 'standard')
    delayed = replace(components, receipts=tuple(replace(x, qualified_month=1) if x.pool == 'embedded_lpddr_boards' else x for x in components.receipts))
    out['licensed_parts_and_start_delayed'] = {'components': canonical_wire(asdict(delayed)), 'start_month': 1, 'resources': reserved}
    out['paid_digital_human_only'] = {'architecture': {'opening_robots': 0, 'new_robots': 0}, 'resources': reserved}
    return out


def resource_architecture_summary(name, r):
    a = r['architecture_execution']; months = r['enterprise']['months']
    commissioned = [m['month'] for m in r['months'] if m['flows']['commissioned']]
    expected = a['inputs']['opening_robots'] + a['inputs']['new_robots']
    full = [m['month'] for m in r['months'] if expected and m['support']['used'] == expected]
    return {'case': name, 'architecture_id': a['inputs']['architecture_id'],
        'first_new_commission_month': min(commissioned) if commissioned else None,
        'first_full_supported_fleet_month': min(full) if full else None,
        'supported_robot_months': sum(m['support']['used'] for m in r['months']),
        'accepted_zones': _rational(sum((rational(m['total_delivered_units']) for m in months), Fraction())),
        'robot_zones': _rational(sum((rational(x['robot_delivered_units']) for m in months for x in m['operators']), Fraction())),
        'staff_cash_paid_cents': sum(x['current_period_staff_cash_paid_cents'] for m in r['calendar_bridge']['months'] for x in m['human_work']),
        'qualified_units': len(a['months'][-1]['qualified_unit_ids']),
        'completed_replacements': sum(x['completed'] for x in r['component_inventory']['replacement_outcomes']),
        **a['consolidation']}


def resource_architecture_artifact():
    inputs = resource_architecture_worlds()
    cases = {name: run_resource_architecture_case(value) for name, value in inputs.items()}
    return canonical_wire({'schema_version': 'architecture-resources-artifact/0.1', 'source_sha256': source_hashes(),
        'case_inputs': inputs, 'cases': cases, 'summary': [resource_architecture_summary(name, r) for name, r in cases.items()],
        'comparison_boundary': 'Four declared intelligence arrangements face the same complete service objective, logical-role capital, annual outside reservations and qualified parts. Profile work requirements and legal consolidation differ explicitly. Paid human capacity remains available; no measured or optimized architecture ranking, added total demand or payroll reduction follows.'})


def resource_architecture_catalog():
    data = json.loads((ROOT / 'model/results/architecture_resources.json').read_text())
    if data['source_sha256'] != source_hashes(): raise ValueError('Architecture resource export is stale; regenerate')
    return {k: v for k, v in data.items() if k != 'cases'} | {'cases': {'licensed_independent_unreserved': data['cases']['licensed_independent_unreserved']}}
