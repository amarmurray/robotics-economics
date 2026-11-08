"""Calendar resource commitments inside the funded competitive execution loop.

Outside reservations constrain this market; they are not an executed second
market, an expense, a forecast of use, or another fleet. All quantities below
are explicit synthetic assumptions. Existing monthly unit and cash ledgers win.
"""
from dataclasses import asdict
from fractions import Fraction
import hashlib
import json
from pathlib import Path

from model.calendar_bridge import Bridge, bridge_context, exact, rational, wire_rationals
from model.competitive_renewals import (Competition, _CompetitiveEnterprise, bounded,
    canonical_wire, competitive_case_inputs, competitive_summary, source_hashes as competition_hashes)
from model.enterprise_finance import FinancePlan, TermLoan
from model.monthly_commercial import restore_opening_inputs
from model.monthly_deployment import run_monthly, _rational
from model.monthly_enterprise import Business, CustomerMove, EnterprisePlan, Equity, Market

from model.annual_resource_ledger import AnnualResourceAdmission, AnnualResources, ResourceYear, read_resources

ROOT = Path(__file__).resolve().parents[1]


class _ResourceEnterprise(AnnualResourceAdmission, _CompetitiveEnterprise):
    def __init__(self, plan, contracts, treasury, enterprise, finance, bridge, competition, resources):
        super().__init__(plan, contracts, treasury, enterprise, finance, bridge, competition)
        self.initialize_resources(resources)


def source_hashes():
    return {**competition_hashes(), **{p: hashlib.sha256((ROOT / p).read_bytes()).hexdigest() for p in ('model/annual_commitments.py', 'model/annual_resource_ledger.py')}}


def run_annual_commitments(plan, treasury, contracts, enterprise, finance, bridge, competition, resources):
    policy = _ResourceEnterprise(plan, contracts, treasury, enterprise, finance, bridge, competition, resources)
    r = run_monthly(plan, treasury, commercial=policy)
    r.update(schema_version='annual-commitments-window/0.1', scope='synthetic_calendar_resource_commitments_and_funded_renewals')
    r['commercial'] = policy.result(r)
    r['commercial']['limits'] = ['Competition, finance and calendar sections define the bounded scope.']
    r['enterprise'] = policy.enterprise_result(r)
    r['enterprise']['limits'] = ['Conserved recurring demand with explicit renewal policy; see competition limits.']
    r['finance'] = policy.finance_result(r)
    r['calendar_bridge'] = policy.bridge_result(r)
    r['competition'] = policy.competition_result(r)
    r['annual_resources'] = policy.resource_result()
    assert r['finance']['consolidation']['unclassified_other_boundary_cash_cents'] == 0
    r['source_sha256'] = source_hashes()
    r = wire_rationals(canonical_wire(r))
    r['case_hash'] = hashlib.sha256(json.dumps(r, sort_keys=True, separators=(',', ':')).encode()).hexdigest()
    return json.loads(json.dumps(r))


def annual_case_inputs(overrides=None):
    if overrides is None: overrides = {}
    if not isinstance(overrides, dict) or set(overrides) - {'competitive', 'resources'}:
        raise ValueError('Unknown annual commitment inputs')
    if not isinstance(overrides.get('competitive', {}), dict): raise ValueError('Competitive inputs must be an object')
    args = competitive_case_inputs(overrides.get('competitive', {}))
    calendar = bridge_context(args[5], args[0].months)[-1]
    value = overrides.get('resources', {'years': [{'calendar_year': y} for y in sorted({x['calendar_year'] for x in calendar})]})
    return (*args, read_resources(value))


def run_annual_case(overrides=None):
    return run_annual_commitments(*annual_case_inputs(overrides))


def replay_annual_case(saved):
    if not isinstance(saved, dict) or saved.get('schema_version') != 'annual-commitments-window/0.1':
        raise ValueError('Complete annual commitment case required')
    try:
        e = dict(saved['enterprise']['inputs']); e['market'] = Market(**e['market'])
        for key, cls in [('businesses', Business), ('moves', CustomerMove), ('equity', Equity)]:
            e[key] = tuple(cls(**x) for x in e[key])
        f = dict(saved['finance']['inputs']); f['loans'] = tuple(TermLoan(**x) for x in f['loans'])
        return run_annual_commitments(*restore_opening_inputs(saved), EnterprisePlan(**e), FinancePlan(**f),
            Bridge(**saved['calendar_bridge']['inputs']), Competition(**saved['competition']['inputs']),
            read_resources(saved['annual_resources']['inputs']))
    except (KeyError, TypeError, AttributeError) as exc:
        raise ValueError('Incomplete or invalid annual commitment inputs') from exc


def available_2026(support_minutes=720000, integration_minutes=144000, prior_support_minutes=0):
    # Declared residual allocations against the unchanged 12,000/2,400-hour pools.
    return {'years': [asdict(ResourceYear(2026, prior_support_minutes, 720000-prior_support_minutes-support_minutes,
                                         0, 144000-integration_minutes)), asdict(ResourceYear(2027))]}


def annual_worlds():
    return {
        'unreserved_control': {},
        'support_exhausted_before_november': {'resources': available_2026(3900)},
        'exact_first_year_support': {'resources': available_2026(9100)},
        'one_minute_below_support': {'resources': available_2026(9099)},
        'integration_for_two_units': {'resources': available_2026(integration_minutes=8400)},
        'same_available_with_prior_use': {'resources': available_2026(3900, prior_support_minutes=300000)},
        'human_led_with_support_commitment': {'resources': available_2026(3900),
            'competitive': {'incumbent_robots': 0, 'competition': {'response_mode': 'calendar_human', 'response_after_month': 2}}},
        'monthly_ceiling_still_binds': {'competitive': {'support_hours_per_month': 20}},
    }


def annual_summary(name, r):
    result = competitive_summary(name, r)
    result['annual_blocked_bookings'] = sum(x['reason'] in ('annual_support_commitments', 'annual_integration_commitments') for x in r['annual_resources']['attempts'])
    result['first_year_supported_robot_months'] = r['calendar_bridge']['calendar_years'][0]['supported_robot_months']
    result['first_year_remaining_support_minutes'] = r['annual_resources']['calendar_years'][0]['resources']['support']['remaining_unbooked_minutes']
    return result


def annual_artifact():
    inputs = annual_worlds(); cases = {name: run_annual_case(x) for name, x in inputs.items()}
    return wire_rationals({'schema_version': 'annual-commitments-artifact/0.1', 'source_sha256': source_hashes(),
        'case_inputs': inputs, 'cases': cases, 'summary': [annual_summary(name, r) for name, r in cases.items()],
        'comparison_boundary': 'Synthetic July 2026–June 2027 competitive cleaning service. Outside reservations constrain actual support/commissioning without creating outside activity or cash. The human-led world deliberately changes robot procurement and response policy. Prior-use decomposition changes opening attribution only. Monthly and calendar-year ceilings both apply; future capacity never backfills missed service.'})


def annual_catalog():
    data = json.loads((ROOT / 'model/results/annual_commitments.json').read_text())
    if data['source_sha256'] != source_hashes(): raise ValueError('Annual commitment export has stale source hashes; regenerate')
    return {k: v for k, v in data.items() if k != 'cases'} | {'cases': {'unreserved_control': data['cases']['unreserved_control']}}
