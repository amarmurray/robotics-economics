import copy
import json
import unittest
from pathlib import Path

from model.workcell_comparison import artifact, compare, replay


class WorkcellComparisonTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.r = artifact()
        cls.c = cls.r['comparisons']

    def test_original_workcell_executions_replayed_exactly(self):
        old=json.loads(Path('model/results/automotive_workcell.json').read_text())['cases']
        for name,pair in self.r['pairs'].items():
            for role,case in pair.items():
                if case!='matched_human_mixed':self.assertEqual(self.c[name]['executions'][role],old[case])

    def test_mixed_human_comparator_has_same_obligation(self):
        r=self.c['mixed_fixed_vs_matched_human']
        self.assertTrue(r['comparison']['eligible'])
        self.assertEqual(r['comparison']['obligations']['baseline'],r['comparison']['obligations']['alternative'])
        self.assertEqual(r['executions']['baseline']['summary']['on_time_kits'],12)
        x=copy.deepcopy(r['inputs']);x['baseline']=copy.deepcopy(self.c['fixed_vs_human']['inputs']['baseline'])
        self.assertFalse(compare(x)['comparison']['eligible'])

    def test_paid_preparation_reverses_the_apparent_labor_reduction(self):
        r=self.c['prepared_vs_human'];b=r['bounds']
        self.assertEqual(b['station_person_seconds_change'],-300)
        self.assertEqual(b['preparation_person_seconds_change'],360)
        self.assertEqual(b['modeled_person_seconds_change'],60)
        self.assertEqual(r['accounts']['alternative']['modeled_person_seconds'],420)
        self.assertEqual(r['accounts']['baseline']['modeled_person_seconds'],360)
        self.assertEqual(r['accounts']['alternative']['paid_staff_cents'],50000)

    def test_customer_cash_receipts_reconcile_without_invented_supplier_profit(self):
        for r in self.c.values():
            for a in r['accounts'].values():
                self.assertEqual(a['operator_cash_cents'],sum(a['external_payee_receipts_cents'].values()))
                self.assertIsNone(a['provider_resource_cost_cents']);self.assertIsNone(a['provider_profit_cents'])

    def test_exact_staff_invoice_bounds_are_conditional_not_removed_hours(self):
        for pair,delta,ceiling in [('fixed_vs_human',23600,26400),('humanoid_vs_human',37200,12800),('prepared_vs_human',33600,16400)]:
            r=self.c[pair];self.assertEqual(r['bounds']['operator_cash_change_cents'],delta)
            self.assertEqual(r['bounds']['alternative_staff_bill_ceiling_cents'],ceiling)
            self.assertEqual(r['bounds']['incremental_net_omitted_cost_allowance_cents'],-delta)

    def test_one_cent_hypothetical_invoice_change_replays_service_and_parity(self):
        r=self.c['fixed_vs_human'];x=copy.deepcopy(r['inputs'])
        for invoice,delta in [(26399,-1),(26400,0),(26401,1)]:
            x['alternative']['staff_cents']=invoice;y=compare(x)
            self.assertTrue(y['comparison']['eligible'])
            self.assertEqual(y['bounds']['operator_cash_change_cents'],delta)
            self.assertEqual(y['executions']['alternative']['summary']['staff_person_ticks_used'],12)

    def test_reducing_paid_capacity_can_invalidate_the_invoice_bound(self):
        x=copy.deepcopy(self.c['fixed_vs_human']['inputs']);x['alternative'].update(staff_cents=26400,staff_capacity_person_ticks=11)
        r=compare(x);self.assertFalse(r['comparison']['eligible']);self.assertIsNone(r['bounds'])

    def test_complete_service_precedes_economic_comparison(self):
        for name in ['direct_misses_deadline','preparation_shortfall','quality_rework_is_late','support_gap','qualified_replacement_still_late','unqualified_replacement']:
            r=self.c[name];self.assertIsNone(r['bounds']);self.assertIn('alternative:incomplete_timely_service',r['comparison']['reasons'])
        self.assertEqual(self.c['quality_rework_is_late']['executions']['alternative']['summary']['delivered_components'],36)

    def test_opening_and_terminal_assets_remain_visible(self):
        r=self.c['qualified_replacement_still_late']
        self.assertEqual(len(r['asset_boundary']['alternative']['closing_robot_assets']),2)
        self.assertEqual(len(r['asset_boundary']['baseline']['closing_robot_assets']),0)
        self.assertIsNone(r['bounds'])

    def test_tick_due_release_raw_supply_and_closure_must_match(self):
        for field in ['tick_seconds','horizon_ticks']:
            x=copy.deepcopy(self.c['fixed_vs_human']['inputs']);x['alternative'][field]+=1
            self.assertFalse(compare(x)['comparison']['eligible'])
        for field in ['supply_tick','release_tick','due_tick']:
            x=copy.deepcopy(self.c['fixed_vs_human']['inputs']);x['alternative']['jobs'][0][field]+=1
            self.assertFalse(compare(x)['comparison']['eligible'])
        x=copy.deepcopy(self.c['fixed_vs_human']['inputs']);x['alternative']['source_closed_intervals']=[[24,34]]
        self.assertFalse(compare(x)['comparison']['eligible'])

    def test_equivalent_component_set_order_is_not_a_new_obligation(self):
        x=copy.deepcopy(self.c['fixed_vs_human']['inputs']);x['alternative']['jobs'][0]['part_ids'].reverse()
        self.assertEqual(compare(x)['bounds'],self.c['fixed_vs_human']['bounds'])

    def test_extra_other_cost_can_make_staff_only_parity_impossible(self):
        x=copy.deepcopy(self.c['fixed_vs_human']['inputs']);x['alternative']['startup_cents']=100000
        r=compare(x);self.assertTrue(r['comparison']['eligible'])
        self.assertLess(r['bounds']['alternative_staff_bill_ceiling_cents'],0)
        self.assertFalse(r['bounds']['staff_bill_alone_arithmetically_sufficient'])

    def test_saved_results_never_override_complete_replay_inputs(self):
        original=self.c['fixed_vs_human'];saved=copy.deepcopy(original)
        saved.update(bounds={'operator_cash_change_cents':-10**9},accounts={},executions={},comparison={'eligible':True},comparison_hash='forged')
        self.assertEqual(replay(saved),original)

    def test_malformed_or_unfunded_pair_rejected(self):
        for x in [None,{},[],{'baseline':{},'alternative':{},'extra':1}]:
            with self.assertRaises(ValueError):compare(x)
        x=copy.deepcopy(self.c['fixed_vs_human']['inputs']);x['alternative']['staff_cents']=True
        with self.assertRaises(ValueError):compare(x)
        x=copy.deepcopy(self.c['fixed_vs_human']['inputs']);x['alternative']['opening_cash_cents']=0
        r=compare(x);self.assertIsNone(r['bounds']);self.assertIn('alternative:unpaid_commitments',r['comparison']['reasons'])


if __name__=='__main__':unittest.main()
