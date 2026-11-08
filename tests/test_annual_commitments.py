"""Resource commitments must change funded execution without another ledger."""
import copy
from dataclasses import replace
from fractions import Fraction
import json
from pathlib import Path
import random
import unittest

from model.annual_commitments import (AnnualResources, ResourceYear, annual_case_inputs,
    available_2026, read_resources, replay_annual_case, run_annual_case, run_annual_commitments)
from model.calendar_bridge import rational


class AnnualCommitments(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.cases = json.loads(Path('model/results/annual_commitments.json').read_text())['cases']

    def test_unreserved_case_preserves_complete_accepted_competitive_execution(self):
        old = json.loads(Path('model/results/competitive_renewals.json').read_text())['cases']['prompt_response']
        new = self.cases['unreserved_control']
        for key in old:
            if key not in ('schema_version', 'scope', 'source_sha256', 'case_hash'):
                self.assertEqual(old[key], new[key], key)

    def assert_conserved(self, r):
        self.assertEqual(sum(x['cash_cents'] for x in r['opening_treasury']['actors']),
                         sum(x['cash_cents'] for x in r['closing_treasury']['actors']))
        self.assertEqual(r['finance']['consolidation']['unclassified_other_boundary_cash_cents'], 0)
        self.assertEqual(len(r['units']), len({u['unit_id'] for u in r['units']}))
        for year in r['annual_resources']['calendar_years']:
            for kind, values in year['resources'].items():
                self.assertEqual(values['prior_use_minutes'] + values['reserved_elsewhere_minutes'] +
                    rational(values['booked_here_minutes']) + rational(values['remaining_unbooked_minutes']),
                    rational(values['pool_minutes']))
                self.assertGreaterEqual(rational(values['remaining_unbooked_minutes']), 0)
                self.assertEqual(rational(values['booked_here_minutes']), sum((rational(x['committed_minutes'][kind])
                    for x in r['annual_resources']['attempts'] if x['calendar_year'] == year['calendar_year']), Fraction()))
        for row, bridge, market, competition in zip(r['annual_resources']['months'], r['calendar_bridge']['months'],
                                                   r['enterprise']['months'], r['competition']['months']):
            attempts = [x for x in r['annual_resources']['attempts'] if x['month'] == row['month']]
            self.assertEqual(sum((rational(x['committed_minutes']['support']) for x in attempts), Fraction()),
                60 * (rational(bridge['support_hours_used']) + rational(bridge['qualification_hours_used'])))
            self.assertEqual(sum((rational(x['committed_minutes']['integration']) for x in attempts), Fraction()),
                60 * rational(bridge['integration_hours_used']))
            self.assertEqual(row['supported_unit_ids'], sorted(x['unit_id'] for x in bridge['cohorts']))
            self.assertEqual(sum(x['units'] for x in competition['lots']), r['enterprise']['inputs']['market']['baseline_units'])
            self.assertEqual(sum((rational(x['delivered_units']) for x in competition['lots']), Fraction()), rational(market['total_delivered_units']))
            for x in attempts:
                for kind in ('support', 'integration'):
                    self.assertEqual(rational(x['committed_minutes'][kind]),
                        rational(x['needed_minutes'][kind]) if x['status'] == 'booked' else 0)

    def test_all_worlds_conserve_calendar_resources_stock_demand_and_actor_cash(self):
        for r in self.cases.values(): self.assert_conserved(r)

    def test_future_year_capacity_cannot_restore_november_or_december_robot_service(self):
        r = self.cases['support_exhausted_before_november']
        months = r['annual_resources']['months']
        self.assertEqual([(x['calendar_year'], x['calendar_month']) for x in months],
            [(2026, m) for m in range(7, 13)] + [(2027, m) for m in range(1, 7)])
        self.assertTrue(all(not months[i]['supported_unit_ids'] for i in (4, 5)))
        self.assertEqual(len(months[6]['supported_unit_ids']), 4)
        self.assertEqual(r['calendar_bridge']['calendar_years'][0]['supported_robot_months'], 6)
        self.assertEqual(r['calendar_bridge']['calendar_years'][1]['supported_robot_months'], 24)
        self.assertTrue(all(y['annualized_service'] is None for y in r['calendar_bridge']['calendar_years']))
        self.assertTrue(all(rational(months[i]['remaining_minutes']['support']) == 0 for i in (4, 5)))

    def test_one_minute_boundary_does_not_fractionally_admit_a_robot_month(self):
        exact = self.cases['exact_first_year_support']; short = self.cases['one_minute_below_support']
        self.assertEqual(exact['calendar_bridge']['calendar_years'][0]['supported_robot_months'], 14)
        self.assertEqual(short['calendar_bridge']['calendar_years'][0]['supported_robot_months'], 13)
        last = short['annual_resources']['calendar_years'][0]['resources']['support']
        self.assertEqual(rational(last['remaining_unbooked_minutes']), 649)
        blocked = [x for x in short['annual_resources']['attempts'] if x['reason'] == 'annual_support_commitments']
        self.assertEqual(len(blocked), 1); self.assertEqual(blocked[0]['month'], 5)
        self.assertEqual(rational(blocked[0]['needed_minutes']['support']), 650)
        self.assertEqual(rational(blocked[0]['committed_minutes']['support']), 0)

    def test_integration_reservation_retains_real_units_and_delays_only_new_commissioning(self):
        r = self.cases['integration_for_two_units']
        self.assertEqual([len(x['cohorts']) for x in r['calendar_bridge']['months']], [0, 0, 2, 2, 2, 2, 4, 4, 4, 4, 4, 4])
        self.assertEqual(rational(r['annual_resources']['calendar_years'][0]['resources']['integration']['booked_here_minutes']), 8400)
        old = self.cases['unreserved_control']
        self.assertEqual({x['unit_id'] for x in r['units']}, {x['unit_id'] for x in old['units']})
        self.assertTrue(any(x['reason'] == 'annual_integration_commitments' for x in r['annual_resources']['attempts']))

    def test_resource_shortage_changes_competitive_awards_without_inventing_new_market_output(self):
        base = self.cases['unreserved_control']; shock = self.cases['support_exhausted_before_november']
        self.assertEqual([x['offers_cents_per_unit']['incumbent'] for x in shock['competition']['months'][3:7]], [2500, 2900, 2900, 2500])
        for r, entrant_zones in [(base, 200), (shock, 400)]:
            self.assertEqual(sum(rational(x['total_delivered_units']) for x in r['enterprise']['months']), 6000)
            entrant = next(x for x in r['competition']['outcomes'] if x['operator_id'] == 'entrant')
            self.assertEqual(rational(entrant['delivered_zones']), entrant_zones)
            self.assertLess(entrant['terminal_cash_after_recorded_bills_cents'], 0)
            self.assertTrue(all(x['removed_payroll_cents'] is None for m in r['calendar_bridge']['months'] for x in m['human_work']))

    def test_human_led_bid_does_not_require_robot_support(self):
        r = self.cases['human_led_with_support_commitment']
        self.assertEqual(r['competition']['months'][5]['offers_cents_per_unit']['incumbent'], 2500)
        self.assertFalse(r['annual_resources']['months'][5]['supported_unit_ids'])
        self.assertFalse(any(x['operator_id'] == 'incumbent' for x in r['units']))
        self.assertEqual(sum(rational(x['total_delivered_units']) for x in r['enterprise']['months']), 6000)

    def test_prior_use_and_reserved_capacity_are_not_double_booked_as_cost_or_activity(self):
        a = self.cases['support_exhausted_before_november']; b = self.cases['same_available_with_prior_use']
        for key in ('plan', 'units', 'months', 'closing_treasury', 'commercial', 'enterprise', 'finance', 'competition', 'calendar_bridge'):
            self.assertEqual(a[key], b[key], key)
        self.assertEqual(a['annual_resources']['attempts'], b['annual_resources']['attempts'])
        self.assertNotEqual(a['annual_resources']['inputs'], b['annual_resources']['inputs'])

    def test_monthly_allocation_remains_binding_with_large_annual_pool(self):
        r = self.cases['monthly_ceiling_still_binds']
        self.assertTrue(all(len(x['cohorts']) <= 1 for x in r['calendar_bridge']['months']))
        self.assertTrue(any(x['reason'] == 'shared_support_and_qualification_hours' for x in r['annual_resources']['attempts']))
        self.assertFalse(any(str(x['reason']).startswith('annual_') for x in r['annual_resources']['attempts']))

    def test_unfunded_support_has_zero_annual_booking_and_preserves_other_obligations(self):
        args = list(annual_case_inputs({'competitive': {'months': 8, 'entrant_cash_cents': 0, 'incumbent_robots': 0, 'entrant_robots': 0}}))
        args[0] = replace(args[0], operators=tuple(replace(o, opening_installed=1 if o.operator_id == 'entrant' else 0) for o in args[0].operators))
        r = run_annual_commitments(*args)
        self.assert_conserved(r)
        failed = [x for x in r['annual_resources']['attempts'] if x['status'] == 'blocked' and x['operator_id'] == 'entrant']
        self.assertTrue(failed)
        self.assertTrue(all(rational(x['committed_minutes']['support']) == 0 for x in failed))
        self.assertTrue(any(i['payer'] == 'entrant' and not i['cancellable'] for i in r['closing_treasury']['invoices']))

    def test_one_cent_software_shortfall_rolls_back_physical_cash_and_annual_minutes(self):
        def execute(extra):
            args = list(annual_case_inputs({'competitive': {'incumbent_robots': 0, 'entrant_robots': 0}}))
            p, t, _, e = args[:4]
            args[0] = replace(p, months=1, operators=tuple(replace(o, opening_installed=int(o.operator_id == 'incumbent'),
                requested_additions=0, demand_units_by_month=(500,)) for o in p.operators), starts=(),
                qualified_component_receipts=(0,), commissioning_slots=(1,), support_slots=(1,), shipping_slots=(1,))
            needed = 150000 + 5000 + p.system.support_cents_per_robot_month + 12500
            args[1] = replace(t, accounts=tuple(replace(a, opening_cash_cents=needed+extra) if a.actor_id == 'incumbent' else a for a in t.accounts))
            args[3] = replace(e, businesses=tuple(replace(b, human_staff_cents_by_month=(0,), human_capacity_by_month=(0,),
                overhead_cents_by_month=(0,), price_cents_per_unit_by_month=(b.price_cents_per_unit_by_month[0],),
                receipt_lag_by_month=(1,), active_from_month=0 if b.operator_id == 'incumbent' else None,
                formation_cents=0, material_cents_per_delivered_unit=0) for b in e.businesses))
            args[-1] = AnnualResources((ResourceYear(2026),))
            return run_annual_commitments(*args)
        short = execute(-1); funded = execute(0)
        self.assert_conserved(short); self.assert_conserved(funded)
        self.assertEqual(short['annual_resources']['attempts'][0]['reason'], 'funding:robot_digital_subscription')
        self.assertEqual(rational(short['annual_resources']['attempts'][0]['committed_minutes']['support']), 0)
        self.assertEqual(rational(funded['annual_resources']['attempts'][0]['committed_minutes']['support']), 650)
        cancelled = [i for i in short['closing_treasury']['invoices'] if i['category'] in ('support', 'robot_digital_subscription')]
        self.assertTrue(cancelled); self.assertTrue(all(i['paid_cents'] == i['outstanding_cents'] == 0 for i in cancelled))

    def test_upgrade_qualification_consumes_the_same_annual_support_pool(self):
        args = list(annual_case_inputs({'competitive': {'months': 8}}))
        args[5] = replace(args[5], digital_paths={'schema_version': 'digital-annual-paths/0.1', 'base_year': 2026, 'epistemic_status': 'synthetic_assumption', 'coordination': [.1, .3, .3]})
        r = run_annual_commitments(*args); self.assert_conserved(r)
        upgraded = [x for x in r['calendar_bridge']['months'][6]['cohorts'] if x['upgrade_performed']]
        self.assertTrue(upgraded)
        self.assertTrue(all(rational(x['upgrade_qualification_hours']) == 2 for x in upgraded))

    def test_complete_replay_ignores_forged_results_and_keeps_resource_inputs(self):
        saved = copy.deepcopy(self.cases['integration_for_two_units'])
        expected = saved['case_hash']; saved['annual_resources']['months'] = []; saved['competition']['outcomes'] = []
        saved['closing_treasury'] = {}; saved['case_hash'] = 'forged'
        replayed = replay_annual_case(saved)
        self.assertEqual(replayed['case_hash'], expected)
        with self.assertRaises(ValueError): replay_annual_case({'schema_version': 'annual-commitments-window/0.1'})

    def test_strict_year_and_resource_input_validation(self):
        for value in (True, -1, .5, float('inf'), None, '650'):
            with self.assertRaises(ValueError): ResourceYear(2026, support_prior_use_minutes=value)
        for rows in ((), (ResourceYear(2026), ResourceYear(2026)), (ResourceYear(2027), ResourceYear(2026))):
            with self.assertRaises(ValueError): AnnualResources(rows)
        for value in (None, [], {}, {'years': [{}]}, {'years': [None]}, {'years': [], 'extra': 1}):
            with self.assertRaises(ValueError): read_resources(value)
        for rows in ([ResourceYear(2026)], [ResourceYear(2026), ResourceYear(2027), ResourceYear(2028)],
                     [ResourceYear(2026), ResourceYear(2027, support_prior_use_minutes=1)],
                     [ResourceYear(2026, support_reserved_elsewhere_minutes=720001), ResourceYear(2027)]):
            args = list(annual_case_inputs()); args[-1] = AnnualResources(tuple(rows))
            with self.assertRaises(ValueError): run_annual_commitments(*args)
        with self.assertRaises(ValueError): run_annual_case({'competitive': None})
        with self.assertRaises(ValueError): run_annual_case({'resources': None})

    def test_seeded_resource_commitments_reconcile_actual_bookings(self):
        rng = random.Random(20261108)
        for _ in range(3):
            r = run_annual_case({'competitive': {'months': 8}, 'resources': available_2026(rng.randrange(1000, 10000), rng.randrange(1, 5) * 4200)})
            self.assert_conserved(r)


if __name__ == '__main__': unittest.main()
