"""Typed parts must preserve paid execution and expose missing qualification."""
import copy
from dataclasses import replace
import json
from pathlib import Path
import unittest

from model.annual_commitments import available_2026
from model.calendar_bridge import rational
from model.component_execution import component_case_inputs, replay_component_case, run_component_case, run_component_execution


class CompatibleComponentExecution(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.cases = json.loads(Path('model/results/component_execution.json').read_text())['cases']

    def assert_conserved(self, r):
        self.assertEqual(sum(a['cash_cents'] for a in r['opening_treasury']['actors']), sum(a['cash_cents'] for a in r['closing_treasury']['actors']))
        self.assertEqual(r['finance']['consolidation']['unclassified_other_boundary_cash_cents'], 0)
        self.assertEqual(len(r['units']), len({u['unit_id'] for u in r['units']}))
        for p, a, b, market, competition in zip(r['months'], r['component_inventory']['months'], r['calendar_bridge']['months'], r['enterprise']['months'], r['competition']['months']):
            self.assertEqual(p['compatible_parts'], a)
            for k in a['qualified_closing']:
                self.assertEqual(a['qualified_opening'][k] + a['qualified_release'][k], a['qualified_closing'][k] + a['manufacturing_issued'][k] + a['service_issued'][k])
                self.assertEqual(a['quarantine_opening'][k] + a['received'][k], a['quarantine_closing'][k] + a['qualified_release'][k])
                self.assertGreaterEqual(a['qualified_closing'][k], 0)
            self.assertEqual(p['support']['used'], len(b['cohorts']))
            self.assertEqual(sum(x['units'] for x in competition['lots']), 500)
            self.assertEqual(sum(rational(x['delivered_units']) for x in competition['lots']), rational(market['total_delivered_units']))
        for year in r['annual_resources']['calendar_years']:
            for v in year['resources'].values():
                self.assertEqual(v['prior_use_minutes'] + v['reserved_elsewhere_minutes'] + rational(v['booked_here_minutes']) + rational(v['remaining_unbooked_minutes']), rational(v['pool_minutes']))

    def test_all_complete_worlds_conserve_parts_units_customer_work_and_actor_cash(self):
        for r in self.cases.values(): self.assert_conserved(r)

    def test_qualified_control_preserves_prior_unit_cash_service_and_competition(self):
        old = json.loads(Path('model/results/annual_commitments.json').read_text())['cases']['unreserved_control']
        r = self.cases['qualified_control']
        for key in ('units', 'opening_treasury', 'closing_treasury', 'finance', 'competition', 'annual_resources'):
            self.assertEqual(old[key], r[key], key)
        for before, after in zip(old['months'], r['months']):
            for key in before:
                if key != 'components': self.assertEqual(before[key], after[key], key)
        self.assertEqual(old['calendar_bridge']['months'], r['calendar_bridge']['months'])
        self.assertEqual(old['calendar_bridge']['annual_parameters'], r['calendar_bridge']['annual_parameters'])
        self.assertEqual(r['component_inventory']['manufacturing_bom_per_start'], {'actuator_h': 24, 'actuator_q': 0, 'embedded_lpddr_boards': 1})

    def test_promised_quarantined_and_wrong_system_parts_create_no_robots_or_manufacturing_payment(self):
        for name in ('promised_only', 'boards_still_quarantined', 'wrong_actuator_pool'):
            r = self.cases[name]
            self.assertFalse(r['units']); self.assertIsNone(r['competition']['incumbent_response_first_month'])
            self.assertEqual(sum(i['paid_cents'] for i in r['closing_treasury']['invoices'] if i['category'] == 'start'), 0)
            self.assertTrue(all(not m['cohorts'] for m in r['calendar_bridge']['months']))
        self.assertEqual(self.cases['boards_still_quarantined']['component_inventory']['closing_quarantined_parts']['embedded_lpddr_boards'], 4)
        self.assertEqual(self.cases['wrong_actuator_pool']['component_inventory']['closing_qualified_parts']['actuator_q'], 100)

    def test_qualification_does_not_automatically_recreate_a_missed_manufacturing_order(self):
        early = self.cases['qualification_misses_start']; later = self.cases['explicit_later_start']
        self.assertFalse(early['units']); self.assertEqual(len(later['units']), 4)
        self.assertEqual(early['component_inventory']['closing_qualified_parts']['embedded_lpddr_boards'], 4)
        self.assertEqual(later['months'][1]['flows']['started'], 4)
        self.assertEqual(later['competition']['incumbent_response_first_month'], 3)
        self.assertEqual(later['calendar_bridge']['calendar_years'][0]['supported_robot_months'], 10)

    def test_phase_four_spares_miss_current_service_and_do_not_consume_annual_hours(self):
        r = self.cases['spares_arrive_after_service']
        self.assertEqual(r['months'][4]['support']['used'], 0)
        self.assertEqual(rational(r['calendar_bridge']['months'][4]['support_hours_used']), 0)
        self.assertEqual(r['component_inventory']['months'][4]['qualified_closing']['actuator_h'], 4)
        self.assertEqual(r['component_inventory']['months'][4]['service_issued']['actuator_h'], 0)
        self.assertEqual(r['months'][5]['support']['used'], 4)
        self.assertEqual(r['component_inventory']['months'][5]['service_issued']['actuator_h'], 4)
        self.assertEqual(r['competition']['months'][4]['offers_cents_per_unit']['incumbent'], 2900)
        self.assertEqual(sum(rational(x['total_delivered_units']) for x in r['enterprise']['months']), 6000)

    def test_rejected_starts_keep_full_bom_and_bundled_cash_sunk(self):
        r = self.cases['two_paid_starts_rejected']
        self.assertEqual(sum(u['status'] == 'rejected' for u in r['units']), 2)
        self.assertEqual(r['component_inventory']['months'][0]['manufacturing_issued'], {'actuator_h': 96, 'actuator_q': 0, 'embedded_lpddr_boards': 4})
        self.assertEqual(sum(i['paid_cents'] for i in r['closing_treasury']['invoices'] if i['category'] == 'start'), 14_400_000)
        self.assertEqual(r['component_inventory']['closing_qualified_parts']['actuator_h'], 2)
        self.assertEqual(sum(x['completed'] for x in r['component_inventory']['replacement_outcomes']), 2)

    def test_annual_support_refusal_preserves_qualified_replacement_stock_until_january(self):
        r = run_component_case({'annual': {'competitive': {'months': 8}, 'resources': available_2026(3900)}})
        self.assert_conserved(r)
        self.assertTrue(all(r['component_inventory']['months'][i]['service_issued']['actuator_h'] == 0 for i in (4, 5)))
        self.assertEqual(r['component_inventory']['months'][5]['qualified_closing']['actuator_h'], 4)
        self.assertEqual(r['component_inventory']['months'][6]['service_issued']['actuator_h'], 4)
        self.assertTrue(all(x['completed'] for x in r['component_inventory']['replacement_outcomes']))

    def test_one_cent_manufacturing_cash_shortfall_keeps_all_qualified_parts(self):
        r = run_component_case({'annual': {'competitive': {'months': 8, 'provider_cash_cents': 14_399_999}}})
        self.assert_conserved(r); self.assertFalse(r['units'])
        self.assertEqual(r['component_inventory']['closing_qualified_parts'], {'actuator_h': 100, 'actuator_q': 0, 'embedded_lpddr_boards': 4})

    def test_unfunded_software_qualification_does_not_consume_the_due_replacement(self):
        args = list(component_case_inputs({'annual': {'competitive': {'months': 8}}}))
        args[5] = replace(args[5], upgrade_cost_cents_per_robot=100_000_000,
            digital_paths={'schema_version': 'digital-annual-paths/0.1', 'base_year': 2026,
                           'epistemic_status': 'synthetic_assumption', 'coordination': [.1, .3, .3]})
        args[-1] = replace(args[-1], replacements=tuple(replace(r, due_month=6) for r in args[-1].replacements))
        r = run_component_execution(*args); self.assert_conserved(r)
        self.assertEqual(r['months'][6]['support']['used'], 0)
        self.assertEqual(r['component_inventory']['months'][6]['service_issued']['actuator_h'], 0)
        self.assertEqual(r['component_inventory']['closing_qualified_parts']['actuator_h'], 4)
        self.assertFalse(any(x['completed'] for x in r['component_inventory']['replacement_outcomes']))
        self.assertTrue(any(x['reason'] == 'funding:software_upgrade_qualification' for x in r['annual_resources']['attempts']))

    def test_complete_replay_uses_typed_inputs_and_rejects_incompatible_contracts(self):
        saved = copy.deepcopy(self.cases['spares_arrive_after_service']); expected = saved['case_hash']
        saved['closing_treasury'] = {}; saved['component_inventory']['months'] = []; saved['months'] = []; saved['case_hash'] = 'forged'
        self.assertEqual(replay_component_case(saved)['case_hash'], expected)
        for value in (None, [], {'annual': None}, {'components': None}, {'accepted_quantity': True}, {'onboard_configuration': 'unknown'}):
            if value is None: continue  # Omitted shortcut object is the explicit default.
            with self.assertRaises(ValueError): run_component_case(value)
        with self.assertRaises(ValueError): replay_component_case({'schema_version': 'compatible-components-window/0.1'})
        wrong = copy.deepcopy(self.cases['qualified_control']); wrong['component_inventory']['inputs']['system_id'] = 'SYN-Q'
        with self.assertRaises(ValueError): replay_component_case(wrong)


if __name__ == '__main__': unittest.main()
