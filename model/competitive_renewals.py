"""Bounded customer renewals on the existing funded physical/calendar loop.

Offers and buyer rules are synthetic policies, not a competitive equilibrium,
estimated customer behavior, executed prices or a new physical engine.
"""
from dataclasses import asdict, dataclass, replace
from fractions import Fraction
from pathlib import Path
import hashlib
import json

from model.calendar_bridge import (Bridge, _BridgedEnterprise, bridge_case_inputs,
                                  bridge_source_hashes, rational, wire_rationals)
from model.enterprise_finance import FinancePlan, TermLoan
from model.monthly_commercial import restore_opening_inputs
from model.monthly_deployment import Start, run_monthly, _rational
from model.monthly_enterprise import Business, CustomerMove, EnterprisePlan, Equity, Market, round_cents
from model.treasury import Moment

ROOT = Path(__file__).resolve().parents[1]


def bounded(value, maximum=1_000_000_000, minimum=0):
    if type(value) is not int or not minimum <= value <= maximum:
        raise ValueError('Bounded exact integer required')


@dataclass(frozen=True)
class Competition:
    lot_count: int = 10
    units_per_lot: int = 50
    first_renewal_month: int = 0
    term_months: int = 1
    incumbent_pre_response_cents: int = 2900
    incumbent_response_cents: int = 2500
    entrant_offer_cents: int = 2700
    response_mode: str = 'supported_robot'
    response_after_month: int = 0
    response_supported_units: int = 1
    buyer_switch_cost_cents_per_lot: int = 5000
    breach_exit: bool = True
    minimum_delivery_basis_points: int = 9000

    def __post_init__(self):
        for key, maximum in [('lot_count', 20), ('units_per_lot', 650), ('term_months', 24), ('response_supported_units', 10)]:
            bounded(getattr(self, key), maximum, 1)
        for key in ('first_renewal_month', 'response_after_month'):
            bounded(getattr(self, key), 120)
        for key in ('incumbent_pre_response_cents', 'incumbent_response_cents',
                    'entrant_offer_cents', 'buyer_switch_cost_cents_per_lot'):
            bounded(getattr(self, key))
        bounded(self.minimum_delivery_basis_points, 10000)
        if type(self.breach_exit) is not bool:
            raise ValueError('Explicit breach-exit Boolean required')
        if self.response_mode not in ('supported_robot', 'calendar_human', 'none'):
            raise ValueError('Unknown incumbent response policy')


class _CompetitiveEnterprise(_BridgedEnterprise):
    def __init__(self, plan, contracts, treasury, enterprise, finance, bridge, competition):
        super().__init__(plan, contracts, treasury, enterprise, finance, bridge)
        if not isinstance(competition, Competition):
            raise ValueError('Explicit competition policy required')
        if set(self.business) != {'incumbent', 'entrant'} or enterprise.market.incumbent_operator != 'incumbent':
            raise ValueError('Named incumbent and entrant required')
        if enterprise.moves or enterprise.market.unmet_units or enterprise.market.new_units:
            raise ValueError('Renewals require one conserved baseline and no scheduled moves/new demand')
        if enterprise.market.baseline_units != competition.lot_count * competition.units_per_lot:
            raise ValueError('Lot identities must exactly partition baseline demand')
        if any(min(o.demand_units_by_month) < enterprise.market.baseline_units for o in plan.operators):
            raise ValueError('Each physical planning ceiling must admit the whole contestable pool')
        for business in enterprise.businesses:
            initial = competition.incumbent_pre_response_cents if business.operator_id == 'incumbent' else competition.entrant_offer_cents
            if any(rate != initial for rate in business.price_cents_per_unit_by_month):
                raise ValueError('Base price arrays must project initial competition quotes; actual bills use locked lot prices')
        if treasury.invoices:
            raise ValueError('Opening invoices require a separate inherited-obligation contract')
        self.competition = competition
        self.lots = [{'lot_id': f'lot-{i:03d}', 'units': competition.units_per_lot,
                      'owner': 'incumbent', 'price_cents': competition.incumbent_pre_response_cents,
                      'expires_month': competition.first_renewal_month}
                     for i in range(competition.lot_count)]
        self.renewal_events = []
        self.renewal_months = []
        self.contract_lines = []
        self.last_lot_service = {}
        self.opening_balances = {b.operator_id: treasury.balance(b.actor_id) for b in enterprise.businesses}
        self.switch_invoice_ids = set()
        self.award_invoice_ids = set()
        self.response_month = None
        self.current_offers = {}
        self.current_capacities = {}
        self.award_quotes = {}

    def renewal_due(self, lot, month):
        c = self.competition
        previous = self.last_lot_service.get(lot['lot_id'])
        breach = bool(c.breach_exit and lot['owner'] is not None and previous is not None and
                      rational(previous) * 10000 < lot['units'] * c.minimum_delivery_basis_points)
        return month >= lot['expires_month'] or breach or lot['owner'] is None, breach

    def prepare(self, t, month, units):
        t = super().prepare(t, month, units)
        # These are contingent offers, created before their phase-5 eligibility.
        # Qualification and an award are still required before any payment.
        for lot in self.lots:
            if not self.renewal_due(lot, month)[0]:
                continue
            for target, business in self.business.items():
                if target == lot['owner']:
                    continue
                costs = [('onboarding', business.actor_id, lot['units'] * business.acquisition_cents_per_recurring_unit)]
                if lot['owner'] is not None:
                    costs.append(('buyer_switch', self.enterprise.market.buyer_actor,
                                  self.competition.buyer_switch_cost_cents_per_lot))
                ids = []
                for category, payer, amount in costs:
                    if not amount:
                        continue
                    iid = self._id('renewal', month, lot['lot_id'], target, category)
                    t = self.issue_enterprise(t, iid, payer, self.enterprise.enterprise_vendor_actor, amount,
                                              Moment(month, 1), Moment(month, 5), 'competitive_' + category, True)
                    ids.append((category, iid))
                self.award_quotes[(month, lot['lot_id'], target)] = ids
        return t

    def offer_prices(self, month):
        c = self.competition
        supported = sum(x['operator_id'] == 'incumbent' for x in self.supported.values())
        response = month >= c.response_after_month and (
            c.response_mode == 'calendar_human' or
            c.response_mode == 'supported_robot' and supported >= c.response_supported_units)
        if response and self.response_month is None:
            self.response_month = month
        return {'incumbent': c.incumbent_response_cents if response else c.incumbent_pre_response_cents,
                'entrant': c.entrant_offer_cents}

    def capacity(self, t, operator, month):
        b = self.business[operator]
        if not self.ready(t, b, month, 5):
            return Fraction()
        return Fraction(b.human_capacity_by_month[month]) + sum(
            (rational(x['capacity_units']) for x in self.supported.values() if x['operator_id'] == operator), Fraction())

    def award_costs(self, t, month, lot, target):
        """Commit contingent resource payments together, or return the old ledger."""
        old = lot['owner']
        if old == target:
            return t, '', []
        candidate = t
        ids = self.award_quotes[(month, lot['lot_id'], target)]
        for category, iid in ids:
            candidate = candidate.settle_invoice(iid + ':pay', iid, Moment(month, 5), provenance=self.provenance)
            if candidate.invoice(iid).outstanding_cents:
                return t, 'unfunded_' + category, []
        for category, iid in ids:
            (self.switch_invoice_ids if category == 'buyer_switch' else self.award_invoice_ids).add(iid)
            if category == 'onboarding':
                self.enterprise_cost_ids.add(iid)
        return candidate, '', [iid for _, iid in ids]

    def finish_shipping(self, t, month):
        t = super().finish_shipping(t, month)
        c = self.competition
        self.current_offers = self.offer_prices(month)
        self.current_capacities = {o: self.capacity(t, o, month) for o in self.business}
        reserved = {o: 0 for o in self.business}
        pending = []
        for lot in self.lots:
            due, breach = self.renewal_due(lot, month)
            if due:
                pending.append((lot, breach))
            else:
                reserved[lot['owner']] += lot['units']
        for lot, breach in pending:
            old = lot['owner']
            prior_price, prior_expiry = lot['price_cents'], lot['expires_month']
            available_before = {o: max(Fraction(), cap - reserved[o]) for o, cap in self.current_capacities.items()}
            proposals = []
            for operator, capacity in self.current_capacities.items():
                available = max(Fraction(), capacity - reserved[operator])
                if available < lot['units']:
                    continue
                switching = c.buyer_switch_cost_cents_per_lot if old is not None and operator != old else 0
                cost = self.current_offers[operator] * lot['units'] * c.term_months + switching
                proposals.append((cost, operator != old, operator))
            proposals.sort()
            attempts = []
            winner = None
            for cost, _, operator in proposals:
                candidate, reason, invoice_ids = self.award_costs(t, month, lot, operator)
                attempts.append({'operator_id': operator, 'quoted_cents_per_unit': self.current_offers[operator],
                                 'term_price_and_switch_cost_cents': cost, 'status': reason or 'funded',
                                 'invoice_ids': invoice_ids})
                if not reason:
                    t, winner = candidate, operator
                    break
            lot.update(owner=winner, price_cents=self.current_offers[winner] if winner else None,
                       expires_month=month + c.term_months if winner else month + 1)
            if winner:
                reserved[winner] += lot['units']
            self.renewal_events.append({'month': month, 'phase': 5, 'lot_id': lot['lot_id'],
                                       'from_operator': old, 'to_operator': winner, 'prior_service_breach': breach,
                                       'previous_price_cents': prior_price, 'previous_expires_month': prior_expiry,
                                       'available_capacity_before_award': {o: _rational(v) for o, v in available_before.items()},
                                       'units': lot['units'], 'attempts': attempts, 'expires_month': lot['expires_month']})
        for (quoted_month, _, _), ids in self.award_quotes.items():
            if quoted_month == month:
                for _, iid in ids:
                    if t.invoice(iid).outstanding_cents:
                        t = t.cancel_invoice(iid + ':cancel', iid, Moment(month, 5), provenance=self.provenance)
        owners = {None: 0, **{o: 0 for o in self.business}}
        for lot in self.lots:
            owners[lot['owner']] += lot['units']
        assert sum(owners.values()) == self.enterprise.market.baseline_units
        self.assignment['baseline'] = owners
        self.current_treasury = t
        return t

    def billed(self, t, month, b, category, payer, payee, rate, due):
        if category != 'end_market_sale':
            return super().billed(t, month, b, category, payer, payee, rate, due)
        owned = [lot for lot in self.lots if lot['owner'] == b.operator_id]
        demand = sum(lot['units'] for lot in owned)
        delivered = rational(self.period_service[b.operator_id]['total_delivered_units'])
        amount = Fraction()
        for lot in owned:
            units = delivered * lot['units'] / demand if demand else Fraction()
            charge = units * lot['price_cents']
            amount += charge
            self.contract_lines.append({'month': month, 'lot_id': lot['lot_id'], 'operator_id': b.operator_id,
                                        'accepted_units': _rational(units), 'locked_cents_per_unit': lot['price_cents'],
                                        'unrounded_cents': _rational(charge)})
        rounded = round_cents(amount)
        iid = self._id('enterprise', b.operator_id, month, category)
        if rounded:
            t = self.issue_enterprise(t, iid, payer, payee, rounded, Moment(month, 6), due, category)
            self.sales_ids.add(iid)
        self.invoice_lines.append({'month': month, 'operator_id': b.operator_id, 'category': category,
                                   'invoice_id': iid if rounded else None, 'accepted_units': _rational(delivered),
                                   'rate_cents_per_unit': None, 'rate_missing_reason': 'Sum of separately locked lot prices; see contract lines',
                                   'unrounded_cents': _rational(amount), 'face_cents': rounded,
                                   'rounding_difference_cents': _rational(Fraction(rounded) - amount), 'due_at': asdict(due)})
        return t

    def close(self, t, month, units, supported):
        super().close(t, month, units, supported)
        lots = []
        cash = []
        for lot in self.lots:
            if lot['owner'] is None:
                delivered = Fraction()
            else:
                row = self.period_service[lot['owner']]
                assigned = sum(row['assigned_units'].values())
                delivered = rational(row['total_delivered_units']) * lot['units'] / assigned if assigned else Fraction()
            self.last_lot_service[lot['lot_id']] = _rational(delivered)
            lots.append({**lot, 'delivered_units': _rational(delivered), 'unserved_units': _rational(lot['units'] - delivered)})
        assert sum((rational(lot['delivered_units']) for lot in lots), Fraction()) == rational(self.market_months[-1]['total_delivered_units'])
        for b in self.enterprise.businesses:
            equity = sum(i.paid_cents for i in t.invoices if i.invoice_id in self.equity_ids and i.payee == b.actor_id)
            principal = sum(x.drawn_cents - x.repaid_cents for x in t.credits if x.borrower == b.actor_id)
            net = t.balance(b.actor_id) - self.opening_balances[b.operator_id] - equity - principal
            outstanding = sum(i.outstanding_cents for i in t.invoices if i.payer == b.actor_id and not i.cancellable)
            cash.append({'operator_id': b.operator_id, 'cash_cents': t.balance(b.actor_id),
                         'funded_equity_cents': equity, 'net_loan_principal_cash_cents': principal,
                         'cumulative_operating_cash_cents': net, 'recorded_unpaid_obligations_cents': outstanding,
                         'cash_after_recorded_bills_cents': net - outstanding})
        self.renewal_months.append({'month': month, 'offers_cents_per_unit': dict(self.current_offers),
                                   'funded_capacity_before_awards': {k: _rational(v) for k, v in self.current_capacities.items()},
                                   'lots': lots, 'operator_cash': cash})

    def competition_result(self, r):
        outcomes = []
        for operator in self.business:
            cash = [next(x for x in m['operator_cash'] if x['operator_id'] == operator) for m in self.renewal_months]
            values = [x['cash_after_recorded_bills_cents'] for x in cash]
            first_crossing = next((i for i in range(len(values)) if any(v < 0 for v in values[:i]) and values[i] >= 0), None)
            recovery = next((i for i in range(len(values)) if any(v < 0 for v in values[:i]) and all(v >= 0 for v in values[i:])), None)
            lots = [lot for m in self.renewal_months for lot in m['lots'] if lot['owner'] == operator]
            outcomes.append({'operator_id': operator, 'assigned_zone_months': sum(lot['units'] for lot in lots),
                             'delivered_zones': _rational(sum((rational(lot['delivered_units']) for lot in lots), Fraction())),
                             'first_cash_break_even_month': first_crossing,
                             'cash_break_even_held_through_horizon_month': recovery, 'terminal_cash_after_recorded_bills_cents': values[-1],
                             'minimum_cash_after_recorded_bills_cents': min(values)})
        invoices = r['closing_treasury']['invoices']
        return {'schema_version': 'competitive-renewals/0.1', 'evidence_status': 'synthetic_policies_not_observed_contracts', 'inputs': asdict(self.competition),
                'incumbent_response_first_month': self.response_month, 'months': self.renewal_months,
                'events': self.renewal_events, 'contract_lines': self.contract_lines, 'outcomes': outcomes,
                'buyer_switch_resource_cash_cents': sum(i['paid_cents'] for i in invoices if i['invoice_id'] in self.switch_invoice_ids),
                'operator_onboarding_resource_cash_cents': sum(i['paid_cents'] for i in invoices if i['invoice_id'] in self.award_invoice_ids),
                'metric_lineage': [
                    {'metric': 'awarded recurring service', 'equation': 'sum lot units by owner; all owners plus unassigned equal the fixed baseline',
                     'inputs': 'lot IDs, expiry, prior delivery, current funded capacity and quoted firm-term prices',
                     'implementation': '_CompetitiveEnterprise.finish_shipping', 'basis': 'synthetic conventional renewal rule'},
                    {'metric': 'switch threshold', 'equation': 'term × lot units × quoted accepted-unit price + buyer switching resources; equal cost retains the old provider',
                     'inputs': 'Competition, current owner, contingent paid onboarding/switch quotes',
                     'implementation': '_CompetitiveEnterprise.award_costs/finish_shipping', 'basis': 'explicit policy, not estimated preference'},
                    {'metric': 'contract revenue', 'equation': 'sum delivered lot units × locked price; round the provider/month invoice once',
                     'inputs': 'contract_lines and enterprise.invoice_lines; actual cash waits for settlement',
                     'implementation': '_CompetitiveEnterprise.billed', 'basis': 'synthetic accepted-unit contract'},
                    {'metric': 'cash after recorded bills', 'equation': 'bank change − paid equity − (loan draws − principal repayments) − recorded unpaid operating obligations',
                     'inputs': 'one Treasury, closing invoices/credits, operator opening balances',
                     'implementation': '_CompetitiveEnterprise.close/competition_result',
                     'basis': 'first crossing and maintenance through the simulated horizon; not distributed returns or lifetime ROI'}],
                'limits': [
                    'One existing recurring cleaning market; no new demand from winning or renewing a contract.',
                    'Synthetic declared offers and greedy stable-lot order; no equilibrium, optimal bid or measured customer preference.',
                    'Awards use currently funded modeled capacity and prior service only; no future outcome is consulted.',
                    'Locked contracts can become under-served; a declared breach clause permits the next renewal, without guaranteeing a new supplier.',
                    'Rational service is allocated proportionally; no individual clinical/job timing or statistical availability claim.',
                    'One provider/month invoice rounds summed locked-price service once; per-lot collections are not inferred.',
                    'Base Business price arrays are checked projections of initial offers; actual invoices use the separately recorded locked lot prices.',
                    'Buyer switching bills lie outside the operator/provider consolidation; recipient onboarding is already in enterprise costs.',
                    'Cash recovery subtracts recorded unpaid bills and financing principal/equity inflows. It is not distributable cash, lifetime ROI or funding of all unissued future commitments.',
                    'Contract periods after the observation window, residual assets and company valuation remain unobserved.']}


def source_hashes():
    return {**bridge_source_hashes(), 'model/competitive_renewals.py': hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}


def canonical_wire(value):
    if isinstance(value, dict): return {k: canonical_wire(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)): return [canonical_wire(v) for v in value]
    if type(value) is float and value.is_integer(): return int(value)
    return value


def run_competitive_renewals(plan, treasury, contracts, enterprise, finance, bridge, competition):
    policy = _CompetitiveEnterprise(plan, contracts, treasury, enterprise, finance, bridge, competition)
    r = run_monthly(plan, treasury, commercial=policy)
    r.update(schema_version='competition-window/0.1', scope='synthetic_conserved_market_with_funded_renewals')
    r['commercial'] = policy.result(r)
    r['commercial']['limits'] = ['Competition, finance and calendar sections define the bounded scope.']
    r['enterprise'] = policy.enterprise_result(r)
    r['enterprise']['limits'] = ['Conserved recurring demand with explicit renewal policy; see competition limits.']
    r['finance'] = policy.finance_result(r)
    r['calendar_bridge'] = policy.bridge_result(r)
    r['competition'] = policy.competition_result(r)
    assert r['finance']['consolidation']['unclassified_other_boundary_cash_cents'] == 0
    r['source_sha256'] = source_hashes()
    r = wire_rationals(canonical_wire(r))
    r['case_hash'] = hashlib.sha256(json.dumps(r, sort_keys=True, separators=(',', ':')).encode()).hexdigest()
    return json.loads(json.dumps(r))


DEFAULTS = {'months': 12, 'entrant_cash_cents': 10_000_000, 'incumbent_cash_cents': 50_000_000,
            'provider_cash_cents': 20_000_000, 'lessor_cash_cents': 50_000_000,
            'incumbent_procurement_month': 0, 'entrant_qualified_month': 0,
            'incumbent_robots': 2, 'entrant_robots': 2, 'start_month': 0,
            'support_hours_per_month': 100, 'integration_hours_per_month': 200,
            'onboarding_cents_per_zone': 1000, 'entrant_receipt_lag': 1,
            'loan_cents': 0, 'extra_equity_cents': 0, 'competition': {}}


def competitive_case_inputs(overrides=None):
    if overrides is None: overrides = {}
    if not isinstance(overrides, dict) or set(overrides) - set(DEFAULTS):
        raise ValueError('Unknown competitive-window inputs')
    x = {**DEFAULTS, **overrides}
    for key, value in x.items():
        if key != 'competition': bounded(value, 1_000_000_000)
    bounded(x['months'], 24, 8)
    if not isinstance(x['competition'], dict): raise ValueError('Competition controls must be an object')
    c = Competition(**x['competition'])
    if c.lot_count * c.units_per_lot > 650: raise ValueError('Demand exceeds the shared physical ceiling')
    if max(x['incumbent_robots'], x['entrant_robots']) > 5: raise ValueError('At most five requested units per operator')
    if not 0 <= x['start_month'] < x['months'] or not 1 <= x['entrant_receipt_lag'] <= 12:
        raise ValueError('Invalid start or collection timing')
    p, t, contracts, e, f, b = bridge_case_inputs(
        {'loan_cents': x['loan_cents'], 'entrant_cash_cents': x['entrant_cash_cents'], 'response_month': None,
         'incumbent_procurement_month': x['incumbent_procurement_month'], 'later_start_candidate': False},
        {'support_hours_per_month': x['support_hours_per_month'], 'integration_hours_per_month': x['integration_hours_per_month'],
         'annual_overrides': {'capability_progress': 0}})
    requested = {'incumbent': x['incumbent_robots'], 'entrant': x['entrant_robots']}
    total = sum(requested.values())
    months = x['months']
    def extend(series):
        return tuple(series) + (series[-1],) * (months - len(series))
    p = replace(p, plan_id='competitive-cleaning-window', months=months, allocation_cycle=('incumbent', 'entrant'),
                operators=tuple(replace(o, opening_installed=0, requested_additions=requested[o.operator_id],
                                        demand_units_by_month=extend(o.demand_units_by_month)) for o in p.operators),
                starts=(Start('shared-supply', x['start_month'], total, total),) if total else (),
                **{key: extend(getattr(p, key)) for key in ('qualified_component_receipts', 'commissioning_slots', 'support_slots', 'shipping_slots')})
    money = {k: x[k + '_cash_cents'] for k in ('entrant', 'incumbent', 'provider', 'lessor')}
    t = replace(t, accounts=tuple(replace(a, opening_cash_cents=money.get(a.actor_id, a.opening_cash_cents)) for a in t.accounts))
    businesses = tuple(replace(v, acquisition_cents_per_recurring_unit=x['onboarding_cents_per_zone'],
                               qualified_month=x['entrant_qualified_month'] if v.operator_id == 'entrant' else v.qualified_month,
                               receipt_lag_by_month=(x['entrant_receipt_lag'],) * months if v.operator_id == 'entrant' else extend(v.receipt_lag_by_month),
                               price_cents_per_unit_by_month=((c.incumbent_pre_response_cents if v.operator_id == 'incumbent' else c.entrant_offer_cents),) * months,
                               **{key: extend(getattr(v, key)) for key in ('overhead_cents_by_month', 'human_capacity_by_month', 'human_staff_cents_by_month')})
                       for v in e.businesses)
    equity = (Equity('competitive-equity', 0, 'investor', 'entrant', x['extra_equity_cents']),) if x['extra_equity_cents'] else ()
    e = replace(e, market=replace(e.market, baseline_units=c.lot_count * c.units_per_lot, unmet_units=0, new_units=0),
                businesses=businesses, moves=(), equity=equity)
    return p, t, contracts, e, f, b, c


def run_competitive_case(overrides=None):
    return run_competitive_renewals(*competitive_case_inputs(overrides))


def replay_competitive_case(saved):
    if not isinstance(saved, dict) or saved.get('schema_version') != 'competition-window/0.1':
        raise ValueError('Complete competitive-window case required')
    try:
        e = dict(saved['enterprise']['inputs']); e['market'] = Market(**e['market'])
        for key, cls in [('businesses', Business), ('moves', CustomerMove), ('equity', Equity)]:
            e[key] = tuple(cls(**x) for x in e[key])
        f = dict(saved['finance']['inputs']); f['loans'] = tuple(TermLoan(**x) for x in f['loans'])
        return run_competitive_renewals(*restore_opening_inputs(saved), EnterprisePlan(**e), FinancePlan(**f),
                                       Bridge(**saved['calendar_bridge']['inputs']), Competition(**saved['competition']['inputs']))
    except (KeyError, AttributeError) as exc:
        raise ValueError('Incomplete competitive-window inputs') from exc


def competitive_worlds():
    return {
        'prompt_response': {},
        'no_response': {'competition': {'response_mode': 'none'}},
        'response_month_seven': {'competition': {'response_after_month': 7}},
        'response_month_ten': {'competition': {'response_after_month': 10}},
        'human_led_response': {'incumbent_robots': 0, 'competition': {'response_mode': 'calendar_human', 'response_after_month': 2}},
        'short_observation_window': {'months': 8, 'competition': {'response_mode': 'none'}},
        'delayed_procurement': {'incumbent_procurement_month': 7},
        'late_entrant_qualification': {'entrant_qualified_month': 4},
        'thin_entrant_cash': {'entrant_cash_cents': 1_500_000},
        'delayed_collections': {'entrant_receipt_lag': 3, 'competition': {'response_mode': 'none'}},
        'support_scarcity': {'support_hours_per_month': 20},
        'six_month_contracts': {'competition': {'term_months': 6}},
        'switch_cost_tie': {'competition': {'buyer_switch_cost_cents_per_lot': 10_000}},
        'one_cent_below_switch_tie': {'competition': {'buyer_switch_cost_cents_per_lot': 9_999}},
        'onboarding_unfunded': {'onboarding_cents_per_zone': 1_000_000},
        'breach_allows_exit': {'entrant_cash_cents': 900_000, 'competition': {'term_months': 6}},
        'breach_locks_service': {'entrant_cash_cents': 900_000, 'competition': {'term_months': 6, 'breach_exit': False}},
    }


def competitive_summary(name, r):
    c = r['competition']; entrant = next(x for x in c['outcomes'] if x['operator_id'] == 'entrant')
    return {'case': name, 'months': len(r['months']), 'response_month': c['incumbent_response_first_month'],
            'accepted_zones': _rational(sum((rational(m['total_delivered_units']) for m in r['enterprise']['months']), Fraction())),
            'entrant_delivered_zones': entrant['delivered_zones'],
            'entrant_first_cash_break_even_month': entrant['first_cash_break_even_month'],
            'entrant_cash_break_even_held_through_horizon_month': entrant['cash_break_even_held_through_horizon_month'],
            'entrant_terminal_cash_after_recorded_bills_cents': entrant['terminal_cash_after_recorded_bills_cents'],
            'buyer_switch_resource_cash_cents': c['buyer_switch_resource_cash_cents']}


def competitive_artifact():
    inputs = competitive_worlds()
    cases = {name: run_competitive_case(x) for name, x in inputs.items()}
    return wire_rationals({'schema_version': 'competitive-window-artifact/0.1', 'source_sha256': source_hashes(),
            'defaults': DEFAULTS, 'case_inputs': inputs, 'cases': cases,
            'summary': [competitive_summary(name, r) for name, r in cases.items()],
            'comparison_boundary': 'Synthetic funded recurring cleaning service, not measured contract economics. Prompt/no/seven/ten bid-response worlds hold physical procurement and staffing inputs fixed. Human-led response and delayed procurement deliberately change those inputs. Horizons, locks, cash and residual obligations remain explicit.'})


def competitive_catalog():
    path = ROOT / 'model/results/competitive_renewals.json'
    if not path.exists(): raise ValueError('Generate the competitive renewals export first')
    data = json.loads(path.read_text())
    if data['source_sha256'] != source_hashes(): raise ValueError('Competitive renewals export has stale source hashes; regenerate')
    return {k: v for k, v in data.items() if k != 'cases'} | {'cases': {'prompt_response': data['cases']['prompt_response']}}
