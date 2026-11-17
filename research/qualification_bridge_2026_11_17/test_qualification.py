import json
import math
import unittest
from dataclasses import replace
from fractions import Fraction as F
from qualification import (Component, PROFILES, qualify, fixed_failure_budgets,
                           zero_failure_trials, experiment)
from bridge import comparison, rounded_cost


class QualificationTests(unittest.TestCase):
    def test_closed_form_score_profile(self):
        a=qualify(PROFILES['score_rich'],.02,2)
        self.assertAlmostEqual(a.adaptation_cost,8*math.log(20/3),places=11)
        self.assertEqual(a.effort[0],0)
        self.assertAlmostEqual(a.residual[1],.018)

    def test_closed_form_bottleneck_profile(self):
        a=qualify(PROFILES['bottleneck_rich'],.02,2)
        self.assertAlmostEqual(a.adaptation_cost,math.log(36)+8*math.log(45/16),places=11)
        self.assertAlmostEqual(a.multiplier,450)

    def test_ranking_reversal(self):
        s=PROFILES['score_rich']; b=PROFILES['bottleneck_rich']
        self.assertLess(sum(x.initial for x in s),sum(x.initial for x in b))
        self.assertGreater(qualify(s,.02).total_cost,qualify(b,.02).total_cost)

    def test_zero_effort_still_pays_verification(self):
        a=qualify((Component('a',.001),Component('b',.002)),.01,3)
        self.assertEqual((a.adaptation_cost,a.total_cost),(0,3))

    def test_irreducible_floor_infeasible(self):
        a=qualify((Component('a',.1,.015),Component('b',.1,.01)),.02)
        self.assertFalse(a.feasible)
        self.assertIsNone(a.total_cost)

    def test_exact_floor_attained_at_zero_effort(self):
        a=qualify((Component('a',.01,.01),),.01,2)
        self.assertTrue(a.feasible)
        self.assertEqual(a.total_cost,2)
        self.assertFalse(qualify((Component('a',.02,.01),),.01).feasible)

    def test_zero_initial_component(self):
        a=qualify((Component('a',0),Component('b',.2)),.05)
        self.assertEqual(a.effort[0],0)
        self.assertAlmostEqual(a.total_cost,math.log(4))

    def test_kkt_and_primal_reconstruction(self):
        for eps in (.001,.01,.05,.15):
            for profile in PROFILES.values():
                ans=qualify(profile,eps)
                self.assertLessEqual(sum(ans.residual),eps+1e-12)
                for c,x,r in zip(profile,ans.effort,ans.residual):
                    self.assertAlmostEqual(r,c.floor+(c.initial-c.floor)*math.exp(-c.rate*x))
                    if x>1e-9:
                        self.assertAlmostEqual(c.cost/(c.rate*(r-c.floor)),ans.multiplier)
                    elif ans.multiplier:
                        self.assertLessEqual(ans.multiplier,c.cost/(c.rate*(c.initial-c.floor))+1e-9)

    def test_two_component_grid_lower_bound(self):
        p=PROFILES['bottleneck_rich']; ans=qualify(p,.02)
        # An independent grid over the risk allocation must not beat KKT.
        for i in range(1,1000):
            first=.02*i/1000;second=.02-first
            cost=fixed_failure_budgets(p,(first,second))
            self.assertLessEqual(ans.total_cost,cost+1e-10)

    def test_optimized_budget_beats_equal_split(self):
        for p in PROFILES.values():
            self.assertLessEqual(qualify(p,.02).total_cost,fixed_failure_budgets(p,(.01,.01)))

    def test_free_componentwise_improvement_cannot_hurt(self):
        p=PROFILES['bottleneck_rich']; old=qualify(p,.02).total_cost
        for factor in (.1,.5,.9):
            improved=tuple(replace(c,initial=c.initial*factor) for c in p)
            self.assertLessEqual(qualify(improved,.02).total_cost,old)

    def test_tighter_criterion_costs_more(self):
        costs=[qualify(PROFILES['score_rich'],e).total_cost for e in (.1,.05,.02,.01)]
        self.assertEqual(costs,sorted(costs))

    def test_envelope_derivative_for_risk(self):
        p=PROFILES['bottleneck_rich'];h=1e-7;eps=.02
        numerical=(qualify(p,eps+h).total_cost-qualify(p,eps-h).total_cost)/(2*h)
        self.assertAlmostEqual(numerical,-qualify(p,eps).multiplier,places=4)

    def test_zero_failure_sample_size_minimal(self):
        for p,n in ((.9,29),(.95,59),(.99,299),(.999,2995)):
            self.assertEqual(zero_failure_trials(p),n)
            self.assertGreaterEqual(.05**(1/n),p)
            self.assertLess(.05**(1/(n-1)),p)

    def test_cost_quantization_is_conservative(self):
        self.assertEqual(rounded_cost(13.8561090787),F(693,50))
        self.assertEqual(rounded_cost(13.86),F(693,50))
        self.assertGreaterEqual(float(rounded_cost(17.176959879)),17.176959879)

    def test_bridge_and_counterexamples(self):
        base=comparison()
        self.assertEqual(base['winner'],'bottleneck_rich')
        self.assertEqual(base['paths']['score_rich']['added_value'],F(1441,50))
        self.assertEqual(base['paths']['bottleneck_rich']['added_value'],F(1597,50))
        self.assertEqual(comparison(weak_demand=True)['winner'],'score_rich')
        self.assertEqual(comparison(equal_profiles=True)['winner'],'score_rich')
        self.assertEqual(comparison(initial_cash=4)['winner'],'score_rich')
        self.assertEqual(comparison(verification=20)['winner'],'score_rich')

    def test_invalid_input_and_serialization(self):
        for kwargs in (dict(initial=-1),dict(initial=.5,floor=.6),dict(initial=.5,rate=0),dict(initial=float('nan'))):
            with self.assertRaises(ValueError):Component('invalid',**kwargs)
        for eps in (0,1,float('nan')):
            with self.assertRaises(ValueError):qualify(PROFILES['score_rich'],eps)
        json.dumps(experiment(),allow_nan=False)


if __name__=='__main__':
    unittest.main()
