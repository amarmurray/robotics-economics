"""Compatible manufacturing and replacement parts in the existing funded loop."""
from dataclasses import asdict, replace
import hashlib
import json
from pathlib import Path

from model.annual_commitments import (_ResourceEnterprise, annual_case_inputs, annual_summary,
    read_resources, source_hashes as annual_hashes)
from model.calendar_bridge import Bridge, wire_rationals
from model.competitive_renewals import Competition, canonical_wire
from model.component_inventory import (ComponentContract, ComponentInventory, ComponentReceipt,
    Replacement, read_components, zero)
from model.enterprise_finance import FinancePlan, TermLoan
from model.monthly_commercial import restore_opening_inputs
from model.monthly_deployment import TypedComponentSystem, run_monthly
from model.monthly_enterprise import Business, CustomerMove, EnterprisePlan, Equity, Market

ROOT = Path(__file__).resolve().parents[1]


def source_hashes():
    paths = ('model/component_inventory.py', 'model/component_execution.py')
    return {**annual_hashes(), **{p: hashlib.sha256((ROOT / p).read_bytes()).hexdigest() for p in paths}}


def run_component_execution(plan, treasury, contracts, enterprise, finance, bridge, competition, resources, components):
    policy = _ResourceEnterprise(plan, contracts, treasury, enterprise, finance, bridge, competition, resources)
    if components.onboard_configuration != policy.annual['onboard_configuration']:
        raise ValueError('Part configuration must match the annual parameter contract')
    materials = ComponentInventory(components)
    r = run_monthly(plan, treasury, commercial=policy, materials=materials)
    r.update(schema_version='compatible-components-window/0.1', scope='synthetic_typed_parts_dated_qualification_and_funded_competition')
    r['commercial'] = policy.result(r)
    r['commercial']['limits'] = ['Component, annual-resource, competition, finance and calendar sections define the bounded scope.']
    r['enterprise'] = policy.enterprise_result(r)
    r['enterprise']['limits'] = ['Conserved recurring demand with explicit renewal and component contracts.']
    r['finance'] = policy.finance_result(r)
    r['calendar_bridge'] = policy.bridge_result(r)
    r['competition'] = policy.competition_result(r)
    r['annual_resources'] = policy.resource_result()
    r['component_inventory'] = materials.result(r['units'])
    r['component_inventory']['metric_lineage'] = [
        {'metric': 'whole-start compatible BOM', 'equation': 'whole funded starts × catalog actuator units and declared onboard boards per system',
         'inputs': 'annual catalog system/configuration and actual Start quantities', 'implementation': 'ComponentInventory.__init__/issue_start',
         'basis': 'synthetic configuration; not a product bill of materials or measured board performance'},
        {'metric': 'usable component inventory', 'equation': 'opening qualified + actual qualification releases − paid manufacturing issues − paid replacement issues',
         'inputs': 'typed pools, dated receipts/qualification and successful physical admissions', 'implementation': 'ComponentInventory.close_month',
         'basis': 'integer stocks; incompatible and quarantined parts cannot substitute'},
        {'metric': 'quarantined component inventory', 'equation': 'opening quarantine + actual received parts − qualified releases',
         'inputs': 'receipt_id, received_month, qualified_month and pool', 'implementation': 'ComponentInventory.receive_and_qualify',
         'basis': 'a null receipt/qualification remains unrealized; an announcement adds no inventory'},
        {'metric': 'replacement completion', 'equation': 'one named requirement completes only when its whole compatible vector and all support bookings are funded',
         'inputs': 'unit ID, due month, part vector, physical support priority, annual hours and Treasury',
         'implementation': 'run_monthly; ComponentInventory.issue_service',
         'basis': 'declared calendar replacement; labor assumed within the paid support bundle, not inferred from an annual failure rate'},
        {'metric': 'cost and stock after manufacturing rejection', 'equation': 'all started units consume the BOM and bundled start payment, including subsequently rejected units',
         'inputs': 'actual paid starts, accept_when_ready, sunk part issues and Treasury invoices',
         'implementation': 'run_monthly; ComponentInventory.issue_start',
         'basis': 'consigned parts are priced once at issue; no automatic salvage/refund'},
    ]
    assert r['finance']['consolidation']['unclassified_other_boundary_cash_cents'] == 0
    r['source_sha256'] = source_hashes()
    r = wire_rationals(canonical_wire(r))
    r['case_hash'] = hashlib.sha256(json.dumps(r, sort_keys=True, separators=(',', ':')).encode()).hexdigest()
    return json.loads(json.dumps(r))


def default_components(plan, configuration='standard'):
    quantity = sum(s.quantity for s in plan.starts)
    board = 2 if configuration == 'high_memory' else 1
    receipts = () if not quantity else (
        ComponentReceipt('manufacture-and-replacement-actuators', 'actuator_h', quantity * 25, 0, 0, 0),
        ComponentReceipt('manufacturing-boards', 'embedded_lpddr_boards', quantity * board, 0, 0, 0))
    replacements = tuple(Replacement('replace-' + s.order_id + '-' + str(i+1), f'start-{s.order_id}-{i+1}', 4,
                                    {**zero(), 'actuator_h': 1}) for s in plan.starts for i in range(s.quantity))
    return ComponentContract('SYN-H', configuration, zero(), receipts, replacements)


def component_case_inputs(overrides=None):
    if overrides is None: overrides = {}
    if not isinstance(overrides, dict) or set(overrides) - {'annual', 'components', 'onboard_configuration', 'accepted_quantity'}:
        raise ValueError('Unknown component execution inputs')
    if not isinstance(overrides.get('annual', {}), dict): raise ValueError('Annual execution controls must be an object')
    args = list(annual_case_inputs(overrides.get('annual', {})))
    configuration = overrides.get('onboard_configuration', 'standard')
    if configuration not in ('standard', 'high_memory'): raise ValueError('Unknown component configuration')
    args[5] = replace(args[5], annual_overrides={**(args[5].annual_overrides or {}), 'onboard_configuration': configuration})
    p = args[0]
    if 'accepted_quantity' in overrides:
        value = overrides['accepted_quantity']
        if type(value) is not int or len(p.starts) != 1 or not 0 <= value <= p.starts[0].quantity:
            raise ValueError('Explicit whole acceptance count within the single start batch required')
        p = replace(p, starts=(replace(p.starts[0], accepted_quantity=value),))
    typed = TypedComponentSystem(**{**asdict(p.system), 'components_per_start': 0, 'service_components_per_robot_month': 0})
    p = replace(p, system=typed, opening_components=0, qualified_component_receipts=(0,) * p.months)
    args[0] = p
    components = read_components(overrides['components']) if 'components' in overrides else default_components(p, configuration)
    return (*args, components)


def run_component_case(overrides=None):
    return run_component_execution(*component_case_inputs(overrides))


def replay_component_case(saved):
    if not isinstance(saved, dict) or saved.get('schema_version') != 'compatible-components-window/0.1':
        raise ValueError('Complete component execution case required')
    try:
        e = dict(saved['enterprise']['inputs']); e['market'] = Market(**e['market'])
        for key, cls in [('businesses', Business), ('moves', CustomerMove), ('equity', Equity)]:
            e[key] = tuple(cls(**x) for x in e[key])
        f = dict(saved['finance']['inputs']); f['loans'] = tuple(TermLoan(**x) for x in f['loans'])
        return run_component_execution(*restore_opening_inputs(saved), EnterprisePlan(**e), FinancePlan(**f),
            Bridge(**saved['calendar_bridge']['inputs']), Competition(**saved['competition']['inputs']),
            read_resources(saved['annual_resources']['inputs']), read_components(saved['component_inventory']['inputs']))
    except (KeyError, TypeError, AttributeError) as exc:
        raise ValueError('Incomplete or invalid component execution inputs') from exc


def component_worlds():
    base = default_components(component_case_inputs()[0])
    def contract(transform): return canonical_wire(asdict(replace(base, receipts=tuple(transform(x) for x in base.receipts))))
    promised = contract(lambda x: replace(x, received_month=None, qualified_month=None))
    quarantined = contract(lambda x: replace(x, qualified_month=None) if x.pool == 'embedded_lpddr_boards' else x)
    wrong = contract(lambda x: replace(x, pool='actuator_q') if x.pool == 'actuator_h' else x)
    late = contract(lambda x: replace(x, qualified_month=1) if x.pool == 'embedded_lpddr_boards' else x)
    spare_receipts = (replace(base.receipts[0], quantity=96), base.receipts[1],
                      ComponentReceipt('late-spare-actuators', 'actuator_h', 4, 0, 4, 4))
    return {
        'qualified_control': {},
        'promised_only': {'components': promised},
        'boards_still_quarantined': {'components': quarantined},
        'wrong_actuator_pool': {'components': wrong},
        'qualification_misses_start': {'components': late},
        'explicit_later_start': {'components': late, 'annual': {'competitive': {'start_month': 1}}},
        'spares_arrive_after_service': {'components': canonical_wire(asdict(replace(base, receipts=spare_receipts)))},
        'two_paid_starts_rejected': {'accepted_quantity': 2},
    }


def component_summary(name, r):
    summary = annual_summary(name, r)
    c = r['component_inventory']
    summary.update(started_units=sum(m['flows']['started'] for m in r['months']),
                   rejected_units=sum(m['flows']['rejected'] for m in r['months']),
                   completed_replacements=sum(x['completed'] for x in c['replacement_outcomes']),
                   closing_qualified_parts=c['closing_qualified_parts'], closing_quarantined_parts=c['closing_quarantined_parts'])
    return summary


def component_artifact():
    inputs = component_worlds(); cases = {name: run_component_case(x) for name, x in inputs.items()}
    return wire_rationals({'schema_version': 'compatible-components-artifact/0.1', 'source_sha256': source_hashes(),
        'case_inputs': inputs, 'cases': cases, 'summary': [component_summary(name, r) for name, r in cases.items()],
        'comparison_boundary': 'Synthetic matched cleaning service with explicitly replaced generic component accounting. The annual catalog supplies the manufacturing BOM; dated qualified receipts and one replacement requirement per unit are separate assumptions. Parts and repair labor are included in existing paid bundles. No actual product BOM, failure rate, independent supplier funding or joint six-cell annual supply is inferred. Strong paid human capacity remains.'})


def component_catalog():
    data = json.loads((ROOT / 'model/results/component_execution.json').read_text())
    if data['source_sha256'] != source_hashes(): raise ValueError('Component export has stale source hashes; regenerate')
    return {k: v for k, v in data.items() if k != 'cases'} | {'cases': {'qualified_control': data['cases']['qualified_control']}}
