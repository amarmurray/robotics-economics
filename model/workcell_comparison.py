"""Matched automotive service, modeled work and conditional customer cash bounds.

This adapter replays the existing engine. It assigns no asset price, removable
staffing fraction, supplier margin or empirical probability.
"""
import copy
import hashlib
import json
from pathlib import Path

from .automotive_workcell import run_workcell

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = 'workcell-comparison/1.0'
SOURCE = 'model/results/automotive_workcell.json'
RESULT = 'model/results/workcell_comparison.json'


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':'), allow_nan=False).encode()).hexdigest()


def source_hashes():
    return {p: hashlib.sha256((ROOT / p).read_bytes()).hexdigest() for p in (
        'model/workcell_comparison.py', 'model/automotive_workcell.py', 'model/treasury.py', SOURCE)}


def obligation(x):
    return dict(tick_seconds=x['tick_seconds'], horizon_ticks=x['horizon_ticks'],
        jobs=[dict(job_id=j['job_id'], variant=j['variant'], part_ids=sorted(j['part_ids']),
                   supply_tick=j['supply_tick'], release_tick=j['release_tick'], due_tick=j['due_tick']) for j in x['jobs']],
        source_closed_intervals=sorted(x['source_closed_intervals']))


def account(r):
    s, x = r['summary'], r['inputs']
    receipts = dict(staff=s['paid_staff_cents'], station_resources=s['operating_and_startup_cash_cents'],
                    preparation=s['preparation_cash_cents'], replacement_equipment=s['replacement_cash_cents'])
    assert sum(receipts.values()) == s['operator_outlay_cents']
    return dict(operator_cash_cents=s['operator_outlay_cents'], external_payee_receipts_cents=receipts,
        nonstaff_operator_cash_cents=s['operator_outlay_cents'] - s['paid_staff_cents'],
        station_person_seconds=s['staff_person_ticks_used'] * x['tick_seconds'],
        preparation_person_seconds=s['preparation_executed_person_ticks'] * x['tick_seconds'],
        modeled_person_seconds=(s['staff_person_ticks_used'] + s['preparation_executed_person_ticks']) * x['tick_seconds'],
        paid_staff_cents=s['paid_staff_cents'],
        provider_resource_cost_cents=None, provider_profit_cents=None,
        missing_provider_account_reason='External payees are receipt accounts, not modeled supplier businesses. Receipts do not reveal their resources, liabilities or margins.')


def compare(inputs):
    if not isinstance(inputs, dict) or set(inputs) != {'baseline', 'alternative'}:
        raise ValueError('Exactly complete baseline and alternative workcell inputs required')
    executions = {k: run_workcell(inputs[k]) for k in ('baseline', 'alternative')}
    obligations = {k: obligation(r['inputs']) for k, r in executions.items()}
    reasons = []
    different = [k for k in obligations['baseline'] if obligations['baseline'][k] != obligations['alternative'][k]]
    if different:
        reasons.append('unmatched_service:' + ','.join(different))
    for name, r in executions.items():
        if r['summary']['on_time_kits'] != r['summary']['due_kits']:
            reasons.append(name + ':incomplete_timely_service')
        if r['summary']['due_unpaid_cents']:
            reasons.append(name + ':unpaid_commitments')
    cash = {k: account(v) for k, v in executions.items()}
    b, a = cash['baseline'], cash['alternative']
    bounds = None
    if not reasons:
        delta = a['operator_cash_cents'] - b['operator_cash_cents']
        ceiling = b['operator_cash_cents'] - a['nonstaff_operator_cash_cents']
        bounds = dict(operator_cash_change_cents=delta,
            incremental_net_omitted_cost_allowance_cents=-delta,
            alternative_staff_bill_ceiling_cents=ceiling,
            recorded_staff_bill_reduction_needed_cents=max(0, delta),
            staff_bill_alone_arithmetically_sufficient=ceiling >= 0,
            modeled_person_seconds_change=a['modeled_person_seconds'] - b['modeled_person_seconds'],
            station_person_seconds_change=a['station_person_seconds'] - b['station_person_seconds'],
            preparation_person_seconds_change=a['preparation_person_seconds'] - b['preparation_person_seconds'])
    result = dict(schema_version=SCHEMA, status='derived_synthetic_window_comparison_not_lifecycle_roi',
        inputs=copy.deepcopy(inputs), executions=executions,
        comparison=dict(eligible=not reasons, reasons=reasons, obligations=obligations),
        accounts=cash, bounds=bounds,
        asset_boundary={k:dict(opening_robot_owned=r['inputs']['config']['kind'] != 'human',
            opening_configuration=r['inputs']['config']['config_id'], installed_buffer_positions=r['inputs']['buffer_capacity'],
            closing_robot_assets=r['assets']) for k, r in executions.items()},
        source_sha256=source_hashes(),
        equations=['Operator cash equals external staff + station-resource + preparation + replacement-equipment receipts.',
            'Modeled person-seconds equal executed station plus separate executed preparation person-ticks, multiplied by seconds per tick.',
            'Staff-bill ceiling = baseline operator cash - alternative nonstaff operator cash.',
            'Incremental omitted net costs (alternative minus baseline) must be no greater than baseline cash minus alternative cash for parity.'],
        limits=['All numbers are inherited synthetic assumptions. These bounds establish no real site qualification or avoidable staffing.',
            'A lower hypothetical staff invoice is not an executable roster or cancelled shift. It must cover the actual remaining duties, capacity and commitments. Preparation labor is purchased separately.',
            'If staffing, fees, timing or omitted work change, replay full service and cash. A necessary accounting bound is not proof the saving is operationally attainable.',
            'Opening robots/buffers and terminal assets differ; acquisition, depreciation, financing, taxes, maintenance and residual value are incomplete. No lifecycle ROI or total production cost is computed.',
            'External payee receipts are not provider resource costs or profit. This boundary cannot inherit the utility model consolidation formula.',
            'The unit is a declared three-component kit, not a vehicle, plant shift or cart-transport service. Late kits do not satisfy the original deadline.'])
    result = json.loads(json.dumps(result, allow_nan=False))
    result['comparison_hash'] = digest(result)
    return result


def replay(saved):
    if not isinstance(saved, dict) or saved.get('schema_version') != SCHEMA:
        raise ValueError('Complete workcell comparison required')
    return compare(saved.get('inputs'))


def catalog():
    return {
        'fixed_vs_human': ('human_direct', 'fixed_buffered'),
        'humanoid_vs_human': ('human_direct', 'humanoid_buffered'),
        'prepared_vs_human': ('human_direct', 'prepared_presentation'),
        'prepared_vs_buffered_fixed': ('fixed_buffered', 'prepared_presentation'),
        'humanoid_vs_buffered_fixed': ('fixed_buffered', 'humanoid_buffered'),
        'refill_fixed_vs_human': ('human_refill_buffered', 'fixed_refill_buffered'),
        'mixed_humanoid_vs_fast_fixed': ('fixed_fast_retool', 'humanoid_mixed_variants'),
        'mixed_fixed_vs_matched_human': ('matched_human_mixed', 'fixed_fast_retool'),
        'direct_misses_deadline': ('human_direct', 'fixed_direct'),
        'preparation_shortfall': ('human_direct', 'presentation_capacity_short'),
        'quality_rework_is_late': ('human_direct', 'quality_rework'),
        'support_gap': ('human_direct', 'support_expires'),
        'qualified_replacement_still_late': ('human_direct', 'qualified_replacement'),
        'unqualified_replacement': ('human_direct', 'unqualified_replacement'),
    }


def artifact():
    saved = json.loads((ROOT / SOURCE).read_text())['cases']
    cases = {k: copy.deepcopy(v['inputs']) for k, v in saved.items()}
    # Same human method, now facing the exact mixed-family obligation. This is a
    # matched comparator reconstruction, not an empirically qualified new method.
    cases['matched_human_mixed'] = copy.deepcopy(cases['human_direct'])
    cases['matched_human_mixed']['jobs'] = copy.deepcopy(cases['fixed_fast_retool']['jobs'])
    comparisons = {k: compare(dict(baseline=cases[b], alternative=cases[a])) for k, (b, a) in catalog().items()}
    return dict(schema_version='workcell-comparison-artifact/1.0', source_sha256=source_hashes(),
        pairs={k:dict(baseline=b, alternative=a) for k, (b, a) in catalog().items()}, comparisons=comparisons,
        summary=[dict(pair=k, eligible=r['comparison']['eligible'], reasons=r['comparison']['reasons'], bounds=r['bounds']) for k, r in comparisons.items()],
        boundary='Fourteen derived comparisons use the existing workcell engine and one explicitly matched human comparator. No prior world changes and no probabilities or empirical labor savings are assigned.')
