"""Exact scoped verification for Q9; no empirical calibration/independent review."""
import unittest
from dataclasses import replace
from fractions import Fraction as F
from value_of_evidence import (Market,Design,binomial_probability,policy,optimize,
                               information_without_budget_gate,results)
import json


class Q9Tests(unittest.TestCase):
    def setUp(self):
        self.d=Design()

    def test_q8_state_payoffs_exact(self):
        self.assertEqual(self.d.market.value(F(19,20)),F(29,25))
        self.assertEqual(self.d.market.value(F(17,20)),-F(19,25))

    def test_incumbent_real_cost_once(self):
        self.assertEqual(self.d.incumbent_value,F(3,10))

    def test_prior_no_test_select_incumbent(self):
        r=policy(0,self.d)
        self.assertEqual(r['net'],F(3,10))
        self.assertEqual(r['branches'][0][2],'incumbent')

    def test_zero_or_one_signal_no_value(self):
        self.assertEqual(information_without_budget_gate(0,self.d),0)
        self.assertEqual(information_without_budget_gate(1,self.d),0)

    def test_two_successes_change_action(self):
        r=policy(2,self.d)
        self.assertEqual([s for s,_,a,_ in r['branches'] if a=='new_service'],[2])
        self.assertEqual(information_without_budget_gate(2,self.d),F(103,20000))

    def test_eight_all_success_only(self):
        r=policy(8,self.d)
        self.assertEqual([s for s,_,a,_ in r['branches'] if a=='new_service'],[8])

    def test_eight_exact_values(self):
        r=policy(8,self.d)
        self.assertEqual(r['gross'],F(112857806639,256000000000))
        self.assertEqual(r['net'],F(92377806639,256000000000))
        self.assertEqual(r['gross']-F(3,10),F(36057806639,256000000000))
        self.assertEqual(r['test_cost'],F(2,25))

    def test_eight_signal_distribution(self):
        r=policy(8,self.d)
        self.assertEqual(r['branches'][-1][1],F(11979660241,25600000000))
        self.assertEqual(sum((x[1] for x in r['branches']),F(0)),1)

    def test_derive_posterior_threshold(self):
        vh,vl=self.d.market.value(self.d.high_g),self.d.market.value(self.d.low_g)
        self.assertEqual((self.d.incumbent_value-vl)/(vh-vl),F(53,96))

    def test_bayesian_likelihood_threshold(self):
        ratio=(F(19,17)**8)
        self.assertGreater(ratio,F(53,43))
        self.assertLess(F(19,17)**7/F(3),F(53,43))

    def test_exact_optimal_sample_size(self):
        r=optimize(40,self.d)
        self.assertEqual(r['n'],8)
        self.assertEqual(r['net'],F(92377806639,256000000000))

    def test_cash_only_2_no_testing(self):
        r=optimize(40,replace(self.d,budget=F(2)))
        self.assertEqual((r['n'],r['net']),(0,F(3,10)))
        self.assertFalse(policy(1,replace(self.d,budget=F(2)))['new_service_available'])

    def test_cash_2_05_five_test_optimum(self):
        r=optimize(40,replace(self.d,budget=F(41,20)))
        self.assertEqual((r['n'],r['net']),(5,F(27804959,80000000)))

    def test_more_budget_cannot_hurt_value(self):
        b=[F(2)+F(j,100) for j in range(26)]
        v=[optimize(40,replace(self.d,budget=x))['net'] for x in b]
        self.assertTrue(all(a<=b for a,b in zip(v,v[1:])))

    def test_perfect_information_upper_bound(self):
        vh,vl=self.d.market.value(self.d.high_g),self.d.market.value(self.d.low_g)
        perfect=(max(self.d.incumbent_value,vh)*self.d.prior_high +
                 max(self.d.incumbent_value,vl)*(1-self.d.prior_high))
        self.assertEqual(perfect-F(3,10),F(43,100))
        for n in range(41):
            self.assertLessEqual(information_without_budget_gate(n,self.d),F(43,100))

    def test_free_information_monotonicity(self):
        vals=[information_without_budget_gate(n,self.d) for n in range(41)]
        self.assertTrue(all(a<=b for a,b in zip(vals,vals[1:])))

    def test_high_demand_makes_test_unnecessary(self):
        d=replace(self.d,market=replace(self.d.market,intercept=F(12)))
        self.assertGreater(d.market.value(d.low_g),d.incumbent_value)
        self.assertEqual(optimize(40,d)['n'],0)

    def test_low_capture_excludes_target(self):
        d=replace(self.d,market=replace(self.d.market,capture=F(1,2)))
        self.assertLess(d.market.value(d.high_g),d.incumbent_value)
        self.assertEqual(optimize(40,d)['n'],0)

    def test_costly_experiment_setup_can_kill_value(self):
        d=replace(self.d,fixed_trial_cost=F(1,2))
        self.assertEqual(optimize(40,d)['n'],0)

    def test_explicit_unfunded_test_action(self):
        d=replace(self.d,budget=F(0))
        self.assertEqual(policy(0,d)['net'],0)
        self.assertIsNone(policy(1,d))

    def test_no_free_information_by_infinite_tests(self):
        self.assertLessEqual(optimize(40,self.d)['n'],40)
        self.assertGreaterEqual(optimize(40,self.d)['net'],policy(0,self.d)['net'])

    def test_broad_parameter_scan_participation(self):
        for capture in (F(0),F(1,2),F(1)):
            for intercept in (F(8),F(10),F(12)):
                d=replace(self.d,market=replace(self.d.market,capture=capture,intercept=intercept))
                r=optimize(12,d)
                self.assertGreaterEqual(r['net'],policy(0,d)['net'])
                for n in range(13):
                    p=policy(n,d)
                    if p is not None:
                        self.assertEqual(sum((x[1] for x in p['branches']),F(0)),F(1))

    def test_binomial_normalizes(self):
        for g in (F(1,2),F(17,20),F(19,20)):
            for n in range(16):
                self.assertEqual(sum((binomial_probability(n,s,g) for s in range(n+1)),F(0)),1)

    def test_negative_inputs_rejected(self):
        for fn in (lambda: Market(curvature=F(0)),lambda: Design(high_g=F(1,2)),
                   lambda: Design(prior_high=F(-1)),lambda: policy(-1),
                   lambda: binomial_probability(2,3,F(1,2)), lambda: optimize(-1)):
            with self.assertRaises(ValueError): fn()

    def test_results_reproducible(self):
        self.assertEqual(json.dumps(results(),sort_keys=True),json.dumps(results(),sort_keys=True))

if __name__=='__main__':
    unittest.main()
