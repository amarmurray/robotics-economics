import json
import math
import unittest
from dataclasses import replace
from fractions import Fraction as F
from workflow import Market, frechet_bounds, independent_success, evaluate, closed_form_capacity_root, results

class WorkflowTests(unittest.TestCase):
    def test_sharp_bounds(self):
        self.assertEqual(frechet_bounds((F(19,20),)*3),(F(17,20),F(19,20)))

    def test_bounds_for_asymmetric_marginals(self):
        self.assertEqual(frechet_bounds((F(1,2),F(3,4))), (F(1,4),F(1,2)))

    def test_single_event(self):
        self.assertEqual(frechet_bounds((F(9,10),)), (F(9,10),F(9,10)))

    def test_independence_case(self):
        self.assertEqual(independent_success((F(19,20),)*3), F(6859,8000))

    def test_independent_within_sharp_bounds(self):
        s=(F(19,20),)*3
        lo,hi=frechet_bounds(s)
        self.assertLessEqual(lo,independent_success(s))
        self.assertLessEqual(independent_success(s),hi)

    def test_source_acceptance_qualifies(self):
        o=evaluate(F(19,20))
        self.assertTrue(o.enter)
        self.assertEqual(o.attempts,F(4))
        self.assertEqual(o.gross_customer_provider_profit,F(479,25))
        self.assertEqual(o.provider_after_qualification_if_enter,F(29,25))

    def test_independence_target_fails(self):
        o=evaluate(F(6859,8000))
        self.assertFalse(o.enter)
        self.assertEqual(o.attempts,F(4))
        self.assertLess(o.gross_customer_provider_profit,F(18))

    def test_disjoint_fails_coincident_passes(self):
        self.assertFalse(evaluate(F(17,20)).enter)
        self.assertTrue(evaluate(F(19,20)).enter)

    def test_threshold_analytic(self):
        self.assertAlmostEqual(closed_form_capacity_root(), (6-math.sqrt(6))/4,places=12)
        for p in (F(17,20), F(9,10), F(19,20)):
            o=evaluate(p)
            self.assertEqual(o.enter,float(p)>closed_form_capacity_root())

    def test_demand_change(self):
        s=F(6859,8000)
        self.assertFalse(evaluate(s).enter)
        self.assertTrue(evaluate(s,replace(Market(),intercept=F(12))).enter)

    def test_declining_rework_cost(self):
        p=F(19,20)
        a=evaluate(p)
        b=evaluate(p,replace(Market(),manual_completion_cost=F(0)))
        self.assertGreaterEqual(b.gross_customer_provider_profit,a.gross_customer_provider_profit)

    def test_monotone_acceptance_with_fixed_market(self):
        g=[F(i,100) for i in range(101)]
        x=[evaluate(v).gross_customer_provider_profit for v in g]
        self.assertTrue(all(a<=b for a,b in zip(x,x[1:])))

    def test_no_positive_output_when_zero_success(self):
        o=evaluate(F(0))
        self.assertEqual((o.attempts,o.expected_accepted,o.gross_customer_provider_profit),(F(0),F(0),F(0)))

    def test_outside_option_prevents_adoption(self):
        o=evaluate(F(19,20),replace(Market(),outside_profit=F(100)))
        self.assertEqual(o.incremental_surplus,F(0))
        self.assertFalse(o.enter)

    def test_free_no_entry_option(self):
        o=evaluate(F(6859,8000))
        self.assertLess(o.provider_after_qualification_if_enter,F(0))
        self.assertFalse(o.enter)

    def test_capture_affects_entry(self):
        o=evaluate(F(19,20),replace(Market(),capture=F(1,2)))
        self.assertFalse(o.enter)

    def test_invalid_inputs(self):
        with self.assertRaises(ValueError):frechet_bounds(())
        with self.assertRaises(ValueError):frechet_bounds((F(101,100),))
        with self.assertRaises(ValueError):evaluate(F(-1,5))
        with self.assertRaises(ValueError):Market(curvature=F(0))

    def test_deterministic_reproduction(self):
        self.assertEqual(json.dumps(results(),sort_keys=True),json.dumps(results(),sort_keys=True))

if __name__=='__main__':unittest.main()
