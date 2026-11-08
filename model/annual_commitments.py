"""Calendar resource commitments inside the funded competitive execution loop.

Outside reservations constrain this market; they are not an executed second
market, an expense, a forecast of use, or another fleet. All quantities below
are explicit synthetic assumptions. Existing monthly unit and cash ledgers win.
"""
from dataclasses import asdict, dataclass
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

ROOT = Path(__file__).resolve().parents[1]
RESOURCES = ('support', 'integration')


@dataclass(frozen=True)
class ResourceYear:
    calendar_year: int
    support_prior_use_minutes: int = 0
    support_reserved_elsewhere_minutes: int = 0
    integration_prior_use_minutes: int = 0
    integration_reserved_elsewhere_minutes: int = 0

    def __post_init__(self):
        bounded(self.calendar_year, 2100, 2026)
        for key, value in asdict(self).items():
            if key != 'calendar_year': bounded(value)


@dataclass(frozen=True)
class AnnualResources:
    years: tuple[ResourceYear, ...]

    def __post_init__(self):
        if not isinstance(self.years, tuple) or not self.years or any(not isinstance(x, ResourceYear) for x in self.years):
            raise ValueError('Explicit dated resource rows required')
        if len({x.calendar_year for x in self.years}) != len(self.years):
            raise ValueError('Duplicate calendar resource year')
        if list(self.years) != sorted(self.years, key=lambda x: x.calendar_year):
            raise ValueError('Resource years must be in calendar order')


def read_resources(value):
    if not isinstance(value, dict) or set(value) != {'years'} or not isinstance(value['years'], list):
        raise ValueError('Resource inputs require exactly one years array')
    try:
        return AnnualResources(tuple(ResourceYear(**row) for row in value['years']))
    except TypeError as exc:
        raise ValueError('Invalid resource year fields') from exc


class _ResourceEnterprise(_CompetitiveEnterprise):
    def __init__(self, plan, contracts, treasury, enterprise, finance, bridge, competition, resources):
        super().__init__(plan, contracts, treasury, enterprise, finance, bridge, competition)
        if not isinstance(resources, AnnualResources): raise ValueError('Explicit annual resources required')
        self.resources = resources
        self.resource_rows = {x.calendar_year: x for x in resources.years}
        if set(self.resource_rows) != {x['calendar_year'] for x in self.calendar}:
            raise ValueError('Resource rows must cover exactly the observed calendar years')
        self.resource_pools = {kind: exact(self.annual[kind + '_budget_hours']) * 60 for kind in RESOURCES}
        self.resource_limits = {}
        self.resource_used = {}
        for year, row in self.resource_rows.items():
            first = next(x for x in self.calendar if x['calendar_year'] == year)
            self.resource_limits[year] = {}
            self.resource_used[year] = {kind: Fraction() for kind in RESOURCES}
            for kind in RESOURCES:
                prior = getattr(row, kind + '_prior_use_minutes')
                reserved = getattr(row, kind + '_reserved_elsewhere_minutes')
                if first['calendar_month'] == 1 and prior:
                    raise ValueError('Prior-year-window use must be zero when the observed year starts in January')
                remaining = self.resource_pools[kind] - prior - reserved
                if remaining < 0: raise ValueError('Prior use and outside reservations exceed the annual pool')
                self.resource_limits[year][kind] = remaining
        self.resource_attempts = []
        self.resource_months = []

    def admit(self, t, iid, month, phase, physical_reason, unit=None, operator_id=None):
        action = t.invoice(iid).category
        if action not in ('support', 'commission'):
            return super().admit(t, iid, month, phase, physical_reason, unit, operator_id)
        year = self.calendar[month]['calendar_year']
        _, target, upgrade = self.robot_invoices[(month, unit.unit_id)]
        needs = {'support': (exact(self.robot_operation(target)['support_hours']) / 12 +
                             (self.bridge.upgrade_hours_per_robot if upgrade else 0)) * 60,
                 'integration': exact(self.annual['integration_hours']) * 60 if action == 'commission' else Fraction()}
        remaining = {k: self.resource_limits[year][k] - self.resource_used[year][k] for k in RESOURCES}
        reason = physical_reason
        for kind in RESOURCES:
            if needs[kind] > remaining[kind]: reason = reason or 'annual_' + kind + '_commitments'
        before = (self.support_hours_used + self.qualification_hours_used, self.integration_hours_used)
        t, reason = super().admit(t, iid, month, phase, reason, unit, operator_id)
        after = (self.support_hours_used + self.qualification_hours_used, self.integration_hours_used)
        for index, kind in enumerate(RESOURCES):
            delta = (after[index] - before[index]) * 60
            assert delta == (needs[kind] if not reason else 0), 'Annual and monthly booking identity lost'
            self.resource_used[year][kind] += delta
            assert 0 <= self.resource_used[year][kind] <= self.resource_limits[year][kind]
        self.resource_attempts.append({'month': month, 'calendar_year': year, 'phase': phase,
            'unit_id': unit.unit_id, 'operator_id': unit.operator_id, 'action': action,
            'needed_minutes': {k: _rational(v) for k, v in needs.items()},
            'remaining_before_minutes': {k: _rational(v) for k, v in remaining.items()},
            'committed_minutes': {k: _rational(v if not reason else Fraction()) for k, v in needs.items()},
            'status': 'booked' if not reason else 'blocked', 'reason': reason or None})
        return t, reason

    def close(self, t, month, units, supported):
        super().close(t, month, units, supported)
        year = self.calendar[month]['calendar_year']
        self.resource_months.append({'month': month, 'calendar_year': year,
            'calendar_month': self.calendar[month]['calendar_month'],
            'booked_year_to_date_minutes': {k: _rational(v) for k, v in self.resource_used[year].items()},
            'remaining_minutes': {k: _rational(self.resource_limits[year][k] - self.resource_used[year][k]) for k in RESOURCES},
            'supported_unit_ids': sorted(supported)})

    def resource_result(self):
        rows = []
        for year, row in self.resource_rows.items():
            observed = [x['month'] for x in self.calendar if x['calendar_year'] == year]
            resources = {}
            for kind in RESOURCES:
                booked = sum((rational(x['committed_minutes'][kind]) for x in self.resource_attempts if x['calendar_year'] == year), Fraction())
                assert booked == self.resource_used[year][kind]
                resources[kind] = {'pool_minutes': _rational(self.resource_pools[kind]),
                    'prior_use_minutes': getattr(row, kind + '_prior_use_minutes'),
                    'reserved_elsewhere_minutes': getattr(row, kind + '_reserved_elsewhere_minutes'),
                    'available_at_window_entry_minutes': _rational(self.resource_limits[year][kind]),
                    'booked_here_minutes': _rational(booked),
                    'remaining_unbooked_minutes': _rational(self.resource_limits[year][kind] - booked)}
            rows.append({'calendar_year': year, 'observed_month_indices': observed, 'resources': resources})
        return {'schema_version': 'annual-resource-commitments/0.1',
            'evidence_status': 'synthetic_declared_prior_use_and_outside_reservations', 'inputs': asdict(self.resources),
            'calendar_years': rows, 'months': self.resource_months, 'attempts': self.resource_attempts,
            'metric_lineage': [
                {'metric': 'available annual resource minutes', 'equation': '60 × annual reference hours − declared pre-window use − reserved elsewhere',
                 'inputs': 'calendar_bridge.annual_parameters and dated resource inputs', 'implementation': '_ResourceEnterprise.__init__',
                 'basis': 'one shared synthetic reference pool; outside reservation is not executed service or expense'},
                {'metric': 'successful support and qualification booking', 'equation': '60 × (annual operation support hours / 12 + actual upgrade qualification hours)',
                 'inputs': 'unit ID, target software vintage, support/qualification requirements, monthly and annual ceilings, actual Treasury',
                 'implementation': '_ResourceEnterprise.admit; _BridgedEnterprise.admit', 'basis': 'commit only after all contingent physical/software/rent bills settle'},
                {'metric': 'successful commissioning booking', 'equation': '60 × process integration hours per actually commissioned unit',
                 'inputs': 'qualified arriving unit, annual and monthly remaining integration capacity and funded contingent invoices',
                 'implementation': '_ResourceEnterprise.admit', 'basis': 'same physical unit and cash ledger; opening installed units are not recommissioned'},
                {'metric': 'calendar conservation', 'equation': 'prior use + outside reservations + booked here + remaining = annual pool, independently each year',
                 'inputs': 'dated attempt ledger and resource rows', 'implementation': '_ResourceEnterprise.resource_result',
                 'basis': 'no carry, borrowing from a future year or retrospective service; partial years are not extrapolated'},
                {'metric': 'competitive and cash consequences', 'equation': 'funded supported unit capacity feeds existing offers, lot awards, delivery and dated receipts',
                 'inputs': 'calendar_bridge, competition, enterprise and closing_treasury in this complete case',
                 'implementation': '_CompetitiveEnterprise.finish_shipping/close', 'basis': 'same synthetic conventional policy, not optimal portfolio allocation or equilibrium'}],
            'limits': [
                'One selected cleaning system; the other five annual cells are not simultaneously executed.',
                'Outside reservations are unavailable capacity, not inferred workloads, fulfilled commitments, resource cash or employment.',
                'Prior use is an explicit opening balance for the partial first year, not reconstructed historical activity; January openings require zero prior-window use.',
                'The annual budget and monthly allocation are both necessary ceilings. Unused monthly capacity does not waive either.',
                'Support includes software qualification. Commissioning consumes the separate integration pool and same-month support.',
                'Existing deterministic physical order gives installed support priority over new commissioning; this is not an optimized allocation.',
                'A failed contingent funding group consumes no annual booking. Fixed staffing, subscriptions, debt and other obligations still follow their existing contracts.',
                'Annual component vectors are not mapped to the monthly generic component module. Actual monthly receipts, reject losses and unit stocks remain authoritative; no conversion is invented.',
                'These cases do not join acquisition, recovery or the separate finite-expansion policy, nor value residual assets or guarantee future cash.',
                'All numerical assumptions remain synthetic; no target annual staffing plan, allocation contract or service economics are measured.']}


def source_hashes():
    return {**competition_hashes(), 'model/annual_commitments.py': hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}


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
