"""Distribution-free decision sensitivity over the existing inspection engine.

Every state is an explicit synthetic possibility, never a sampled observation.
Infeasible complete service has no monetary penalty or equivalent-cost ranking.
"""
import copy
import hashlib
import itertools
import json
from pathlib import Path

from .inspection_price_bounds import cash_account, digest, obligation
from .utility_inspection import run_inspection

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = 'inspection-uncertainty/1.0'
INPUT = 'model/inspection_uncertainty_inputs.json'
RESULT = 'model/results/inspection_uncertainty.json'
POLICIES = ('human', 'fixed', 'mobile')
OBJECTIVES = ('customer_outlay_cents', 'consolidated_resource_cash_cents')
AXES = {
    'staffing': ('committed', 'per_visit'),
    'field_duty': (False, True),
    'fixed_fit': ('complete', 'one_unqualified'),
    'mobile_fit': ('complete', 'one_quality_failure', 'late_capture'),
    'review_capacity': (23, 24),
    'deadline_minute': (100, 180),
}


def source_hashes():
    return {p: hashlib.sha256((ROOT / p).read_bytes()).hexdigest() for p in (
        'model/inspection_uncertainty.py', 'model/inspection_price_bounds.py',
        'model/utility_inspection.py', 'model/treasury.py', INPUT)}


def validate(inputs):
    if not isinstance(inputs, dict) or set(inputs) != {'base_inputs', 'axes'}:
        raise ValueError('Exactly base_inputs and axes required')
    if not isinstance(inputs['axes'], dict) or set(inputs['axes']) != set(AXES):
        raise ValueError('Complete named uncertainty axes required')
    run_inspection(inputs['base_inputs'])  # Existing strict input validator.
    for key, values in inputs['axes'].items():
        if not isinstance(values, list) or not values or len(values) > len(AXES[key]):
            raise ValueError('Nonempty bounded axis required: ' + key)
        allowed = {(type(v), v) for v in AXES[key]}
        if any(type(v) not in (str, int, bool) or (type(v), v) not in allowed for v in values) or len(set(values)) != len(values):
            raise ValueError('Unknown, duplicate or mistyped axis value: ' + key)
    # These named perturbations use a four-window/twelve-point inherited fixture.
    b = inputs['base_inputs']
    if b['cycles'] != 4 or len(b['required_points']) != 12 or b['decision_minute'] != 60:
        raise ValueError('This experiment requires four windows, twelve points and cutoff 60')
    return copy.deepcopy(inputs)


def policy_inputs(base, state, policy):
    x = copy.deepcopy(base)
    x.update(staffing=state['staffing'], deadline_minute=state['deadline_minute'],
             review_capacity_person_minutes=state['review_capacity'],
             field_duty_cycles=list(range(x['cycles'])) if state['field_duty'] else [])
    for c in x['channels']:
        c.update(enabled=c['channel_id'] == policy, coverage_ids=x['required_points'][:],
                 qualified_ids=x['required_points'][:], bad_quality_ids=[], capture_minute=10)
        if c['channel_id'] == 'fixed' and state['fixed_fit'] == 'one_unqualified':
            c['qualified_ids'] = x['required_points'][:-1]
        if c['channel_id'] == 'mobile':
            if state['mobile_fit'] == 'one_quality_failure':
                c['bad_quality_ids'] = x['required_points'][-1:]
            elif state['mobile_fit'] == 'late_capture':
                c['capture_minute'] = 61  # After the declared review cutoff; not a failure rate.
    return x


def execute(x):
    r = run_inspection(x)
    reasons = []
    if r['summary']['complete_service_windows'] != x['cycles']:
        reasons.append('incomplete_due_service')
    if r['summary']['due_unpaid_cents']:
        reasons.append('unpaid_commitments')
    if any(not c['fee_funded'] or not c['resource_funded'] for w in r['cycles'] for c in w['channels']):
        reasons.append('unfunded_monitoring_booking')
    return dict(inputs=x, execution_hash=r['case_hash'], feasible=not reasons, reasons=reasons,
                summary=r['summary'], cash=cash_account(r),
                # Complete original execution is recovered from inputs, not trusted from a saved result.
                obligation=obligation(x))


def decision(rows, objective):
    if objective not in OBJECTIVES:
        raise ValueError('Unknown cash objective')
    if not rows:
        raise ValueError('At least one state required')
    oracle = {r['state_id']: min(v['cash'][objective] for v in r['policies'].values() if v['feasible']) for r in rows}
    out = {}
    for p in POLICIES:
        failures = [r['state_id'] for r in rows if not r['policies'][p]['feasible']]
        regret = None if failures else max(r['policies'][p]['cash'][objective] - oracle[r['state_id']] for r in rows)
        out[p] = dict(infeasible_state_count=len(failures), worst_regret_cents=regret)
    viable = {p: v['worst_regret_cents'] for p, v in out.items() if v['worst_regret_cents'] is not None}
    if not viable:
        return dict(policies=out, minimax_policies=[], worst_regret_cents=None)
    best = min(viable.values())
    return dict(policies=out, minimax_policies=[p for p in POLICIES if viable.get(p) == best], worst_regret_cents=best)


def reveal(rows, keys, objective):
    groups = {}
    for r in rows:
        k = tuple(r['state'][key] for key in keys)
        groups.setdefault(k, []).append(r)
    branches = [dict(observed=dict(zip(keys, key)), state_count=len(rs), **decision(rs, objective))
                for key, rs in groups.items()]
    worst = None if any(b['worst_regret_cents'] is None for b in branches) else max(b['worst_regret_cents'] for b in branches)
    return dict(revealed_axes=list(keys), worst_remaining_regret_cents=worst, branches=branches)


def run_uncertainty(inputs):
    x = validate(inputs)
    rows = []
    for i, vals in enumerate(itertools.product(*(x['axes'][k] for k in AXES))):
        state = dict(zip(AXES, vals))
        policies = {p: execute(policy_inputs(x['base_inputs'], state, p)) for p in POLICIES}
        if len({digest(v['obligation']) for v in policies.values()}) != 1:
            raise ValueError('Policies must have the same full service obligation in each state')
        if not policies['human']['feasible']:
            raise ValueError('Human fallback comparator is infeasible; this experiment cannot rank the state')
        limits = []
        for baseline, alternative in itertools.permutations(POLICIES, 2):
            b, a = policies[baseline], policies[alternative]
            eligible = b['feasible'] and a['feasible']
            limits.append(dict(baseline=baseline, alternative=alternative, eligible=eligible,
                customer_incremental_net_residual_allowance_cents=b['cash']['customer_outlay_cents']-a['cash']['customer_outlay_cents'] if eligible else None,
                consolidated_incremental_net_residual_allowance_cents=b['cash']['consolidated_resource_cash_cents']-a['cash']['consolidated_resource_cash_cents'] if eligible else None))
        rows.append(dict(state_id=f'S{i:03d}', state=state, policies=policies, residual_cost_limits=limits))
    decisions = {}
    for objective in OBJECTIVES:
        prior = decision(rows, objective)
        evidence = []
        for size in range(1, len(AXES) + 1):
            for keys in itertools.combinations(AXES, size):
                r = reveal(rows, keys, objective)
                r['worst_regret_reduction_cents'] = prior['worst_regret_cents'] - r['worst_remaining_regret_cents']
                evidence.append(r)
        decisions[objective] = dict(before_evidence=prior, evidence_partitions=evidence,
            full_revelation=reveal(rows, tuple(AXES), objective))
    # Exact provider funding headroom, re-executed at the boundary and one cent above.
    good = dict(staffing='per_visit', field_duty=False, fixed_fit='complete', mobile_fit='complete', review_capacity=24, deadline_minute=180)
    funding = []
    for p in ('fixed', 'mobile'):
        y = policy_inputs(x['base_inputs'], good, p)
        r = run_inspection(y)
        if not execute(y)['feasible']:
            funding.append(dict(policy=p, boundary_applicable=False, reason='Starting service is not funded and complete'))
            continue
        headroom = min(w['closing_cash_cents']['monitor_provider'] for w in r['cycles'])
        for extra in (headroom, headroom + 1):
            z = copy.deepcopy(y)
            next(c for c in z['channels'] if c['enabled'])['initial_resource_cents'] += extra
            funding.append(dict(policy=p, boundary_applicable=True, additional_initial_resource_cents=extra, **execute(z)))
    result = dict(schema_version=SCHEMA, status='synthetic_conditional_decision_analysis_not_empirical_estimate',
        inputs=x, source_sha256=source_hashes(), states=rows, decisions=decisions,
        funding_boundaries=funding, state_count=len(rows), policy_evaluations=3 * len(rows),
        probability_model=None,
        boundary='Finite possibility set, not frequencies, probability or expected value. Regret is relative to the best feasible recorded-window cash option in each state. Missing lifecycle, maintenance benefit and legal rights remain unbounded empirical requirements. No economic action is recommended without their evidence.')
    result['result_hash'] = digest(result)
    return result


def replay(saved):
    if not isinstance(saved, dict) or saved.get('schema_version') != SCHEMA:
        raise ValueError('Complete inspection uncertainty artifact required')
    return run_uncertainty(saved.get('inputs'))


def artifact():
    d = json.loads((ROOT / INPUT).read_text())
    return run_uncertainty(d['experiment'])
