import copy
import itertools
import json
import unittest
from pathlib import Path

from model.inspection_uncertainty import artifact, decision, replay, reveal, run_uncertainty, validate, AXES, POLICIES


class InspectionUncertaintyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.r = artifact()
        cls.rows = cls.r['states']

    def row(self, **changes):
        s = dict(staffing='per_visit', field_duty=False, fixed_fit='complete', mobile_fit='complete', review_capacity=24, deadline_minute=180)
        s.update(changes)
        return next(r for r in self.rows if r['state'] == s)

    def test_full_factorial_has_exactly_once_each_possibility_without_weights(self):
        self.assertEqual(len(self.rows), 96)
        self.assertEqual(len({tuple(r['state'].values()) for r in self.rows}), 96)
        self.assertIsNone(self.r['probability_model'])
        self.assertEqual(self.r['policy_evaluations'], 288)

    def test_inherited_complete_cases_reproduce_exactly(self):
        old = json.loads(Path('model/results/utility_inspection.json').read_text())['cases']
        for policy, case in [('human','human_per_visit'), ('fixed','fixed_complete_avoidable'), ('mobile','mobile_complete_avoidable')]:
            self.assertEqual(self.row()['policies'][policy]['summary'], old[case]['summary'])

    def test_service_and_money_conservation_across_every_replay(self):
        for row in self.rows:
            self.assertTrue(row['policies']['human']['feasible'])
            for v in row['policies'].values():
                s, c = v['summary'], v['cash']
                self.assertEqual(s['accepted_point_windows']+s['unaccepted_point_windows'], 48)
                self.assertEqual(c['customer_outlay_cents']-c['provider_cash_change_cents'], c['consolidated_resource_cash_cents'])
                self.assertEqual(c['monitor_fees_cents']-c['provider_cash_change_cents'], c['provider_resource_cash_cents'])
                self.assertEqual(v['obligation'], row['policies']['human']['obligation'])

    def test_failed_review_retains_full_visit_bill_with_complete_fallback(self):
        v = self.row(mobile_fit='one_quality_failure')['policies']['mobile']
        self.assertTrue(v['feasible'])
        self.assertEqual(v['summary']['remote_accepted_point_windows'], 44)
        self.assertEqual(v['summary']['review_person_minutes'], 96)
        self.assertEqual(v['summary']['paid_field_crew_cents'], 120000)

    def test_late_fallback_cannot_win_by_appearing_cheap(self):
        row = self.row(mobile_fit='one_quality_failure', deadline_minute=100)
        self.assertFalse(row['policies']['mobile']['feasible'])
        d = decision([row], 'customer_outlay_cents')
        self.assertIsNone(d['policies']['mobile']['worst_regret_cents'])
        self.assertNotIn('mobile', d['minimax_policies'])

    def test_paid_staffing_is_not_released_time(self):
        row = self.row(staffing='committed')
        self.assertEqual(row['policies']['human']['summary']['paid_field_crew_cents'], row['policies']['mobile']['summary']['paid_field_crew_cents'])
        self.assertGreater(row['policies']['mobile']['cash']['customer_outlay_cents'], row['policies']['human']['cash']['customer_outlay_cents'])

    def test_residual_cost_limits_preserve_both_payer_boundaries(self):
        pairs = self.row()['residual_cost_limits']
        m = next(v for v in pairs if v['baseline']=='fixed' and v['alternative']=='mobile')
        self.assertEqual(m['customer_incremental_net_residual_allowance_cents'], -22000)
        self.assertEqual(m['consolidated_incremental_net_residual_allowance_cents'], -13400)
        for row in self.rows:
            for v in row['residual_cost_limits']:
                if not v['eligible']:
                    self.assertIsNone(v['customer_incremental_net_residual_allowance_cents'])
                    self.assertIsNone(v['consolidated_incremental_net_residual_allowance_cents'])
                else:
                    reverse=next(x for x in row['residual_cost_limits'] if x['baseline']==v['alternative'] and x['alternative']==v['baseline'])
                    self.assertEqual(v['customer_incremental_net_residual_allowance_cents'], -reverse['customer_incremental_net_residual_allowance_cents'])

    def test_known_state_oracle_and_minimax_are_distinct(self):
        d = self.r['decisions']['customer_outlay_cents']
        self.assertEqual(d['before_evidence']['minimax_policies'], ['human'])
        self.assertEqual(d['before_evidence']['worst_regret_cents'], 94000)
        self.assertEqual(decision([self.row()], 'customer_outlay_cents')['minimax_policies'], ['fixed'])

    def test_joint_packet_has_information_complementarity(self):
        vals = self.r['decisions']['customer_outlay_cents']['evidence_partitions']
        self.assertTrue(all(v['worst_regret_reduction_cents']==0 for v in vals if len(v['revealed_axes'])<=2))
        best = {n:min(v['worst_remaining_regret_cents'] for v in vals if len(v['revealed_axes'])==n) for n in range(1,7)}
        self.assertEqual(best, {1:94000,2:94000,3:72000,4:48000,5:0,6:0})
        for v in vals:
            self.assertEqual(sum(b['state_count'] for b in v['branches']),96)

    def test_more_information_cannot_increase_worst_regret(self):
        for obj in self.r['decisions'].values():
            rows = obj['evidence_partitions']
            for a in rows:
                for b in rows:
                    if set(a['revealed_axes']) <= set(b['revealed_axes']):
                        self.assertGreaterEqual(a['worst_remaining_regret_cents'],b['worst_remaining_regret_cents'])

    def test_removing_deadline_risk_alone_does_not_resolve_cash_tradeoff(self):
        rs = [r for r in self.rows if r['state']['deadline_minute']==180]
        d = decision(rs, 'customer_outlay_cents')
        self.assertEqual(d['minimax_policies'], ['human'])
        self.assertEqual(d['policies']['fixed']['infeasible_state_count'], 0)
        self.assertEqual(d['policies']['fixed']['worst_regret_cents'], 106000)
        rs = [r for r in rs if r['state']['fixed_fit']=='complete' and r['state']['review_capacity']==24]
        d = decision(rs, 'customer_outlay_cents')
        self.assertEqual(d['minimax_policies'], ['fixed'])
        self.assertEqual(d['worst_regret_cents'], 34000)

    def test_one_cent_provider_funding_threshold_is_not_terminal_cash(self):
        for policy, threshold in [('fixed',3400),('mobile',7800)]:
            a,b = [v for v in self.r['funding_boundaries'] if v['policy']==policy]
            self.assertEqual(a['additional_initial_resource_cents'],threshold)
            self.assertTrue(a['feasible']);self.assertFalse(b['feasible'])
            self.assertEqual(b['summary']['complete_service_windows'],4)
            self.assertIn('unfunded_monitoring_booking',b['reasons'])

    def test_replay_ignores_forged_results(self):
        saved=copy.deepcopy(self.r)
        saved.update(states=[], decisions={'profit':10**12}, result_hash='forged', source_sha256={})
        self.assertEqual(replay(saved), self.r)

    def test_typed_bounded_inputs_and_infeasible_baseline_rejected(self):
        for value in [[],[True],[23,23],[0],[23.0]]:
            x=copy.deepcopy(self.r['inputs']);x['axes']['review_capacity']=value
            with self.assertRaises(ValueError):validate(x)
        x=copy.deepcopy(self.r['inputs']);x['base_inputs']['utility_cash_cents']=0
        with self.assertRaises(ValueError):run_uncertainty(x)

    def test_explicit_subset_changes_state_domain_without_inventing_frequencies(self):
        x=copy.deepcopy(self.r['inputs'])
        for k in AXES:x['axes'][k]=[x['axes'][k][0]]
        d=run_uncertainty(x)
        self.assertEqual(d['state_count'],1)
        self.assertIsNone(d['probability_model'])


if __name__ == '__main__':
    unittest.main()
