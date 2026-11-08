"""Composition must conserve one physical execution and every actor's cash."""
import copy
from dataclasses import asdict, replace
from fractions import Fraction
import json
from pathlib import Path
import random
import unittest

from model.architecture_resources import (resource_architecture_inputs, replay_resource_architecture_case,
    run_architecture_resources, run_resource_architecture_case)
from model.calendar_bridge import rational


class ArchitectureResources(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.cases = json.loads(Path('model/results/architecture_resources.json').read_text())['cases']

    def assert_conserved(self, r):
        self.assertEqual(sum(a['cash_cents'] for a in r['opening_treasury']['actors']), sum(a['cash_cents'] for a in r['closing_treasury']['actors']))
        self.assertEqual(r['finance']['consolidation']['unclassified_other_boundary_cash_cents'], 0)
        self.assertEqual(len(r['units']), len({u['unit_id'] for u in r['units']}))
        for m, b, a, c, market in zip(r['months'], r['calendar_bridge']['months'], r['annual_resources']['months'], r['component_inventory']['months'], r['enterprise']['months']):
            self.assertEqual(m['support']['used'], len(b['cohorts']))
            self.assertEqual(a['supported_unit_ids'], sorted(x['unit_id'] for x in b['cohorts']))
            self.assertEqual(m['compatible_parts'], c)
            self.assertEqual(sum(rational(x['total_delivered_units']) for x in market['operators']), rational(market['total_delivered_units']))
            for k in c['qualified_closing']:
                self.assertEqual(c['qualified_opening'][k] + c['qualified_release'][k], c['qualified_closing'][k] + c['manufacturing_issued'][k] + c['service_issued'][k])
                self.assertEqual(c['quarantine_opening'][k] + c['received'][k], c['quarantine_closing'][k] + c['qualified_release'][k])
        for y in r['annual_resources']['calendar_years']:
            for v in y['resources'].values():
                self.assertEqual(v['prior_use_minutes'] + v['reserved_elsewhere_minutes'] + rational(v['booked_here_minutes']) + rational(v['remaining_unbooked_minutes']), rational(v['pool_minutes']))
        for x in r['annual_resources']['attempts']:
            if x['status'] == 'blocked': self.assertTrue(all(rational(v) == 0 for v in x['committed_minutes'].values()))

    def test_all_worlds_conserve_cash_parts_work_and_resources(self):
        for r in self.cases.values(): self.assert_conserved(r)

    def test_unreserved_profiles_preserve_existing_execution_and_paid_obligations(self):
        old = json.loads(Path('model/results/monthly_architectures.json').read_text())['cases']
        for name in ('integrated_oem', 'licensed_independent', 'open_adapted', 'model_led_operator'):
            before, after = old[name], self.cases[name + '_unreserved']
            for k in ('units', 'opening_treasury', 'closing_treasury', 'finance', 'enterprise', 'commercial'):
                self.assertEqual(before[k], after[k], (name, k))
            self.assertEqual(before['calendar_bridge'], after['calendar_bridge'])
            for a, b in zip(before['months'], after['months']):
                for k in a:
                    if k != 'components': self.assertEqual(a[k], b[k], (name, k))
            for k in ('events', 'cash_lines', 'months', 'entities', 'consolidation'):
                self.assertEqual(before['architecture_execution'][k], after['architecture_execution'][k], (name, k))

    def test_common_integration_commitment_changes_qualified_date_not_customer_service(self):
        integrated = self.cases['integrated_oem_committed']; licensed = self.cases['licensed_independent_committed']
        self.assertEqual(integrated['months'][2]['support']['used'], 4)
        self.assertEqual(licensed['months'][2]['support']['used'], 3)
        self.assertEqual(licensed['months'][6]['support']['used'], 4)
        self.assertEqual(rational(integrated['annual_resources']['calendar_years'][0]['resources']['integration']['booked_here_minutes']), 8400)
        self.assertEqual(rational(licensed['annual_resources']['calendar_years'][0]['resources']['integration']['booked_here_minutes']), 5250)
        for r in self.cases.values():
            self.assertEqual(sum(rational(m['total_delivered_units']) for m in r['enterprise']['months']), 4000)
            self.assertEqual(sum(x['current_period_staff_cash_paid_cents'] for m in r['calendar_bridge']['months'] for x in m['human_work']), 3200000)

    def test_exact_integration_boundary_and_one_minute_shortfall(self):
        def case(minutes): return run_resource_architecture_case({'resources': {'years': [{'calendar_year': 2026, 'integration_reserved_elsewhere_minutes': 144000-minutes}, {'calendar_year': 2027}]}})
        exact, below = case(10500), case(10499)
        self.assertEqual(exact['months'][2]['support']['used'], 4)
        self.assertEqual(below['months'][2]['support']['used'], 3)
        self.assertEqual(below['months'][6]['support']['used'], 4)
        self.assert_conserved(exact); self.assert_conserved(below)

    def test_less_adaptation_work_moves_bottleneck_to_physical_integration(self):
        base = self.cases['open_adapted_committed']; fast = self.cases['open_less_adaptation_committed']; free = self.cases['open_less_adaptation_unreserved']
        self.assertFalse(any(m['flows']['started'] for m in base['months']))
        self.assertEqual(fast['months'][0]['flows']['started'], 2)
        self.assertEqual(fast['months'][3]['support']['used'], 3)
        self.assertEqual(free['months'][3]['support']['used'], 4)
        self.assertEqual(fast['months'][6]['support']['used'], 4)
        more = run_resource_architecture_case({'architecture': {'architecture_id': 'open_adapted', 'architecture_overrides': {'profiles': {'open_adapted': {'adaptation_engineering_hours': 50}}}}, 'resources': fast['annual_resources']['inputs']})
        for before, after in zip(fast['months'], more['months']):
            for key in ('flows', 'support', 'outputs', 'compatible_parts'):
                self.assertEqual(before[key], after[key])
        self.assertLess(more['architecture_execution']['consolidation']['itemized_architecture_resource_cash_cents'], fast['architecture_execution']['consolidation']['itemized_architecture_resource_cash_cents'])

    def test_failed_role_funding_consumes_no_contingent_resources_or_parts(self):
        r = self.cases['licensed_unfunded_model']; self.assert_conserved(r)
        self.assertFalse(any(m['support']['used'] for m in r['months']))
        self.assertFalse(any(rational(m['engineering_hours_used']) or rational(m['demonstration_hours_used']) for m in r['architecture_execution']['months']))
        self.assertTrue(all(not x['completed'] for x in r['component_inventory']['replacement_outcomes']))
        self.assertEqual(r['component_inventory']['closing_qualified_parts']['actuator_h'], 52)
        self.assertTrue(all(x['paid_cents'] == 0 for x in r['architecture_execution']['cash_lines'] if x['resource_expense']))
        self.assertGreater(sum(x['paid_cents'] for x in r['closing_treasury']['invoices'] if x['category'] == 'human_staff'), 0)

    def test_support_reservation_preserves_due_spares_and_previously_paid_manufacture(self):
        r = run_resource_architecture_case({'resources': {'years': [{'calendar_year': 2026, 'support_reserved_elsewhere_minutes': 720000-5200}, {'calendar_year': 2027}]}})
        self.assert_conserved(r)
        self.assertTrue(any(m['flows']['started'] for m in r['months']))
        self.assertEqual(r['months'][4]['support']['used'], 0)
        self.assertEqual(r['component_inventory']['months'][4]['service_issued']['actuator_h'], 0)
        self.assertEqual(r['component_inventory']['months'][5]['qualified_closing']['actuator_h'], 4)
        self.assertEqual(r['component_inventory']['months'][6]['service_issued']['actuator_h'], 4)
        self.assertEqual(sum(x['paid_cents'] for x in r['closing_treasury']['invoices'] if x['category'] == 'start'), 7200000)

    def test_unqualified_board_does_not_automatically_reschedule_start(self):
        delayed = self.cases['licensed_parts_and_start_delayed']
        self.assertEqual(delayed['months'][1]['flows']['started'], 2)
        self.assertEqual(delayed['months'][3]['flows']['commissioned'], 1)
        missed = run_resource_architecture_case({'components': delayed['component_inventory']['inputs']})
        self.assertFalse(any(m['flows']['started'] for m in missed['months']))
        self.assertEqual(missed['component_inventory']['closing_qualified_parts']['embedded_lpddr_boards'], 2)

    def test_human_alternative_keeps_service_and_staff_cash_without_robot_bills(self):
        r = self.cases['paid_digital_human_only']; self.assert_conserved(r)
        self.assertFalse(r['units']); self.assertFalse(r['annual_resources']['attempts'])
        self.assertFalse(r['architecture_execution']['events'])
        self.assertEqual(sum(rational(x['human_delivered_units']) for m in r['enterprise']['months'] for x in m['operators']), 4000)

    def test_funded_manufacture_survives_later_role_qualification_failures(self):
        r = self.cases['model_led_operator_committed']
        self.assertEqual(sum(m['flows']['started'] for m in r['months']), 2)
        self.assertEqual(sum(m['flows']['commissioned'] for m in r['months']), 0)
        self.assertEqual(sum(i['paid_cents'] for i in r['closing_treasury']['invoices'] if i['category'] == 'start'), 7200000)
        self.assertEqual(r['component_inventory']['months'][0]['manufacturing_issued']['actuator_h'], 48)
        self.assertEqual(r['component_inventory']['closing_qualified_parts']['actuator_h'], 2)

    def test_missing_rights_premise_never_commits_parts_or_annual_hours(self):
        r = run_resource_architecture_case({'architecture': {'architecture_overrides': {'profiles': {'licensed_independent': {'assume_rights_available': False}}}}})
        self.assert_conserved(r)
        self.assertFalse(any(m['flows']['started'] or m['support']['used'] for m in r['months']))
        self.assertEqual(r['component_inventory']['closing_qualified_parts']['actuator_h'], 52)

    def test_exact_full_replay_ignores_forged_outputs(self):
        for name in ('licensed_independent_committed', 'open_adapted_unreserved', 'paid_digital_human_only'):
            saved = copy.deepcopy(self.cases[name]); expected = saved['case_hash']
            saved['closing_treasury'] = {}; saved['months'] = []; saved['case_hash'] = 'forged'
            saved['annual_resources']['attempts'] = []; saved['component_inventory']['events'] = []
            self.assertEqual(replay_resource_architecture_case(saved)['case_hash'], expected)

    def test_strict_inputs_and_incompatible_replay_are_rejected(self):
        for value in ([], {'architecture': None}, {'bridge': None}, {'resources': None}, {'components': None}, {'start_month': True}, {'start_month': 8}, {'unknown': 1}):
            with self.assertRaises((ValueError, TypeError)): run_resource_architecture_case(value)
        saved = copy.deepcopy(self.cases['licensed_independent_unreserved'])
        saved['component_inventory']['inputs']['system_id'] = 'SYN-Q'
        with self.assertRaises(ValueError): replay_resource_architecture_case(saved)
        saved['component_inventory']['inputs']['system_id'] = 'SYN-H'
        saved['plan']['system']['components_per_start'] = 1
        with self.assertRaises(ValueError): replay_resource_architecture_case(saved)

    def test_seeded_adverse_allocations_preserve_one_cash_and_resource_ledger(self):
        rng = random.Random(3301)
        for _ in range(6):
            r = run_resource_architecture_case({'architecture': {'engineering_hours_per_month': rng.randrange(0, 601)},
                'resources': {'years': [{'calendar_year': 2026, 'support_reserved_elsewhere_minutes': 720000-rng.randrange(0, 18001), 'integration_reserved_elsewhere_minutes': 144000-rng.randrange(0, 14001)}, {'calendar_year': 2027}]}})
            self.assert_conserved(r)


if __name__ == '__main__': unittest.main()
