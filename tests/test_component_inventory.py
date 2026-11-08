"""Typed part compatibility, actual release, atomic issue and dated maintenance."""
from dataclasses import replace
import unittest

from model.component_inventory import (ComponentContract, ComponentInventory, ComponentReceipt,
    Replacement, read_components, zero)
from model.monthly_deployment import Plan, Operator, Start, System, TypedComponentSystem, run_monthly
from model.treasury import Account, Treasury


def parts(h=0, q=0, board=0):
    return {'actuator_h': h, 'actuator_q': q, 'embedded_lpddr_boards': board}


def fixture(*, opening=0, start=0, accepted=1, months=3, cash=10_000_000, inventory=None, receipts=(), replacements=(), configuration='standard'):
    plan = Plan('typed-components', months, (Operator('site', 1, (1000,) * months, opening),), ('site',),
        (0,) * months, (4,) * months, (4,) * months, (4,) * months,
        system=TypedComponentSystem(system_id='SYN-H'),
        starts=() if start is None else (Start('one', start, 1, accepted),))
    treasury = Treasury((Account('provider', cash), Account('manufacturer', 0), Account('deployment_vendor', 0)))
    contract = ComponentContract('SYN-H', configuration, inventory or zero(), receipts, replacements)
    return plan, treasury, contract


def execute(**kw):
    p, t, c = fixture(**kw)
    ledger = ComponentInventory(c); r = run_monthly(p, t, materials=ledger)
    r['typed_inventory'] = ledger.result(r['units'])
    return r


class CompatibleComponentInventory(unittest.TestCase):
    def assert_conserved(self, r):
        self.assertEqual(sum(a['cash_cents'] for a in r['opening_treasury']['actors']),
                         sum(a['cash_cents'] for a in r['closing_treasury']['actors']))
        for month in r['months']:
            c = month['compatible_parts']
            self.assertEqual(month['components']['status'], 'inactive_generic_balance_in_typed_contract')
            for k in zero():
                self.assertEqual(c['qualified_opening'][k] + c['qualified_release'][k],
                    c['service_issued'][k] + c['manufacturing_issued'][k] + c['qualified_closing'][k])
                self.assertEqual(c['quarantine_opening'][k] + c['received'][k], c['qualified_release'][k] + c['quarantine_closing'][k])
                self.assertGreaterEqual(c['qualified_closing'][k], 0)
                self.assertLessEqual(c['protected_for_unsupported_existing'][k], c['qualified_closing'][k])

    def test_explicit_typed_contract_preserves_old_generic_guards_and_rejects_duplicate_inventory(self):
        with self.assertRaises(ValueError): System(components_per_start=0)
        with self.assertRaises(ValueError): TypedComponentSystem(components_per_start=2)
        with self.assertRaises(ValueError): TypedComponentSystem(service_components_per_robot_month=True)
        p, t, c = fixture()
        with self.assertRaises(ValueError): replace(p, opening_components=1)
        with self.assertRaises(ValueError): replace(p, qualified_component_receipts=(1, 0, 0))
        with self.assertRaises(ValueError): run_monthly(p, t)
        with self.assertRaises(ValueError): run_monthly(replace(p, system=System()), t, materials=ComponentInventory(c))

    def test_wrong_actuator_pool_cannot_manufacture_the_humanoid_configuration(self):
        r = execute(inventory=parts(q=24, board=1)); self.assert_conserved(r)
        self.assertFalse(r['units'])
        self.assertEqual(r['typed_inventory']['closing_qualified_parts'], parts(q=24, board=1))
        self.assertTrue(any(e['reason'] == 'compatible_manufacturing_parts' for e in r['events']))
        self.assertTrue(all(i['paid_cents'] == 0 for i in r['closing_treasury']['invoices'] if i['category'] == 'start'))

    def test_qualified_phase_four_receipt_can_fund_that_months_phase_five_start(self):
        receipts = (ComponentReceipt('h', 'actuator_h', 24, 0, 0, 0), ComponentReceipt('b', 'embedded_lpddr_boards', 1, 0, 0, 0))
        r = execute(receipts=receipts); self.assert_conserved(r)
        self.assertEqual(r['months'][0]['flows']['started'], 1)
        self.assertEqual(r['months'][2]['flows']['commissioned'], 1)
        self.assertEqual(r['months'][0]['compatible_parts']['manufacturing_issued'], parts(h=24, board=1))
        self.assertEqual(r['typed_inventory']['closing_qualified_parts'], zero())

    def test_received_but_unqualified_parts_remain_quarantined(self):
        receipts = (ComponentReceipt('h', 'actuator_h', 24, 0, 0, None), ComponentReceipt('b', 'embedded_lpddr_boards', 1, 0, 0, None))
        r = execute(receipts=receipts); self.assert_conserved(r)
        self.assertFalse(r['units']); self.assertEqual(r['typed_inventory']['closing_quarantined_parts'], parts(h=24, board=1))
        self.assertEqual(r['typed_inventory']['closing_qualified_parts'], zero())

    def test_announcement_without_receipt_adds_no_inventory(self):
        r = execute(receipts=(ComponentReceipt('promised-h', 'actuator_h', 24), ComponentReceipt('promised-b', 'embedded_lpddr_boards', 1)))
        self.assert_conserved(r); self.assertFalse(r['units'])
        self.assertEqual(r['typed_inventory']['closing_qualified_parts'], zero())
        self.assertEqual(r['typed_inventory']['closing_quarantined_parts'], zero())
        self.assertTrue(all(e['available_inventory_added'] == 0 for e in r['typed_inventory']['events']))

    def test_later_qualification_requires_an_explicit_later_start(self):
        receipts = (ComponentReceipt('h', 'actuator_h', 24, 0, 0, 1), ComponentReceipt('b', 'embedded_lpddr_boards', 1, 0, 0, 1))
        early = execute(receipts=receipts); later = execute(receipts=receipts, start=1, months=4)
        self.assertFalse(early['units']); self.assertEqual(later['months'][1]['flows']['started'], 1)
        self.assertEqual(later['months'][3]['flows']['commissioned'], 1)
        self.assert_conserved(early); self.assert_conserved(later)

    def test_unfunded_manufacturing_issues_no_parts(self):
        r = execute(inventory=parts(h=24, board=1), cash=3_599_999); self.assert_conserved(r)
        self.assertFalse(r['units']); self.assertEqual(r['typed_inventory']['closing_qualified_parts'], parts(h=24, board=1))
        self.assertFalse(any(e['action'] == 'funded_manufacturing_issue' for e in r['typed_inventory']['events']))

    def test_rejected_manufacture_keeps_sunk_parts_and_cash(self):
        r = execute(inventory=parts(h=24, board=1), accepted=0); self.assert_conserved(r)
        self.assertEqual(r['units'][0]['status'], 'rejected')
        self.assertEqual(r['typed_inventory']['closing_qualified_parts'], zero())
        self.assertEqual(sum(i['paid_cents'] for i in r['closing_treasury']['invoices'] if i['category'] == 'start'), 3_600_000)

    def test_late_parts_cannot_retroactively_repair_phase_three_service(self):
        req = Replacement('repair', 'opening-installed-site-1', 0, parts(h=1))
        r = execute(opening=1, start=None, replacements=(req,), receipts=(ComponentReceipt('spare', 'actuator_h', 1, 0, 0, 0),))
        self.assert_conserved(r)
        self.assertEqual([m['support']['used'] for m in r['months']], [0, 1, 1])
        self.assertEqual(r['months'][0]['compatible_parts']['protected_for_unsupported_existing'], parts(h=1))
        self.assertEqual(r['months'][1]['compatible_parts']['service_issued'], parts(h=1))
        self.assertEqual(r['months'][2]['compatible_parts']['service_issued'], zero())
        self.assertTrue(r['typed_inventory']['replacement_outcomes'][0]['completed'])

    def test_unfunded_support_retains_parts_and_uncompleted_requirement(self):
        req = Replacement('repair', 'opening-installed-site-1', 0, parts(h=1))
        r = execute(opening=1, start=None, inventory=parts(h=1), replacements=(req,), cash=9999)
        self.assert_conserved(r); self.assertTrue(all(m['support']['used'] == 0 for m in r['months']))
        self.assertEqual(r['typed_inventory']['closing_qualified_parts'], parts(h=1))
        self.assertFalse(r['typed_inventory']['replacement_outcomes'][0]['completed'])

    def test_installed_replacement_has_priority_over_new_manufacturing(self):
        req = Replacement('repair', 'opening-installed-site-1', 0, parts(h=1))
        r = execute(opening=1, inventory=parts(h=24, board=1), replacements=(req,)); self.assert_conserved(r)
        self.assertEqual(r['months'][0]['support']['used'], 1)
        self.assertEqual(r['months'][0]['flows']['started'], 0)
        self.assertEqual(r['typed_inventory']['closing_qualified_parts'], parts(h=23, board=1))

    def test_high_memory_bom_needs_two_compatible_boards_without_changing_a_price(self):
        short = execute(inventory=parts(h=24, board=1), configuration='high_memory')
        full = execute(inventory=parts(h=24, board=2), configuration='high_memory')
        self.assertFalse(short['units']); self.assertEqual(full['months'][0]['flows']['started'], 1)
        self.assertEqual(full['typed_inventory']['manufacturing_bom_per_start'], parts(h=24, board=2))
        self.assertEqual(short['plan']['system']['bundled_start_cents'], full['plan']['system']['bundled_start_cents'])
        self.assert_conserved(short); self.assert_conserved(full)

    def test_replacement_is_not_consumed_early_or_repeated_as_an_annual_average(self):
        req = Replacement('repair', 'opening-installed-site-1', 1, parts(h=1))
        r = execute(opening=1, start=None, inventory=parts(h=1), replacements=(req,)); self.assert_conserved(r)
        self.assertEqual([m['compatible_parts']['service_issued']['actuator_h'] for m in r['months']], [0, 1, 0])

    def test_receipt_and_replacement_validation_keeps_unknowns_distinct(self):
        for value in (True, -1, .5, None, '24'):
            with self.assertRaises(ValueError): ComponentReceipt('x', 'actuator_h', value)
        for received, qualified in ((None, 0), (1, 0), (True, None)):
            with self.assertRaises(ValueError): ComponentReceipt('x', 'actuator_h', 1, 0, received, qualified)
        for value in (None, [], {}, {'system_id': 'SYN-H', 'onboard_configuration': 'standard', 'opening_qualified_parts': {'actuator_h': 24}}):
            with self.assertRaises(ValueError): read_components(value)
        for req in (Replacement('wrong-id', 'no-unit', 0, parts(h=1)),
                    Replacement('wrong-type', 'opening-installed-site-1', 0, parts(q=1)),
                    Replacement('too-many', 'opening-installed-site-1', 0, parts(board=2))):
            with self.assertRaises(ValueError): execute(opening=1, replacements=(req,))
        req = Replacement('one', 'opening-installed-site-1', 0, parts(h=1))
        with self.assertRaises(ValueError): ComponentContract('SYN-H', 'standard', zero(), (), (req, replace(req, requirement_id='two')))


if __name__ == '__main__': unittest.main()
