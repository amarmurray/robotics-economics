"""Scoped tests: exact special cases and independent finite-step Bellman checks."""
import math
import unittest
from joint_acquisition import (Program, solve, discrete_bellman, full_event_only,
                               example, hamiltonian, validate)

class JointQualificationTests(unittest.TestCase):
    def setUp(self):
        self.v, self.p = example()

    def test_baseline_and_retained_terminal_values(self):
        result = solve(self.v, self.p, 0)
        self.assertEqual(result['values'], self.v)
        self.assertEqual(result['initial_net'], 0)

    def test_marginal_slopes(self):
        deriv = hamiltonian(self.v, self.p)(0, self.v)
        self.assertAlmostEqual(deriv[0], 13)  # A: 2*7 - 1
        self.assertAlmostEqual(deriv[1], 5)   # B: 2*(10-7) - 1
        self.assertAlmostEqual(deriv[2], 19)  # A after B: 2*10 - 1
        self.assertAlmostEqual(deriv[3], 0)
        self.assertAlmostEqual(solve(self.v,self.p,1e-6)['initial_net']/1e-6,13,delta=.001)

    def test_joint_event_only_closed_form(self):
        p=(Program('both',3,1.2),)
        for b in (.05, .3, 1, 3, 9):
            self.assertAlmostEqual(solve((0,0,0,10),p,b)['initial_net'],
                                   full_event_only(10,1.2,b),delta=1e-8)

    def test_independent_terminal_chain_free_learning_exact(self):
        p=(Program('A',1,1),Program('B',2,1))
        for b in (.2, 1, 2, 4):
            expected=10*(1-math.exp(-b)*(1+b))
            self.assertAlmostEqual(solve((0,0,0,10),p,b,cost=0)['initial_net'],
                                   expected,delta=3e-8)

    def test_optimal_policy_switch_with_budget(self):
        self.assertEqual(solve(self.v,self.p,.05)['actions'][0], 'unloading_A')
        self.assertEqual(solve(self.v,self.p,4)['actions'][0], 'joint_redesign_AB')
        self.assertGreater(solve(self.v,self.p,4)['initial_net'],solve(self.v,self.p,1)['initial_net'])

    def test_large_budget_limit(self):
        gain=solve(self.v,self.p,16)['initial_net']
        self.assertAlmostEqual(gain,10-1/1.2,delta=1e-6)
        self.assertGreater(gain,10-2/2)

    def test_value_of_partial_state(self):
        empty=(0,0,0,10)
        withpartial=solve(self.v,self.p,.025)['initial_net']
        without=solve(empty,self.p,.025)['initial_net']
        self.assertGreater(withpartial,without)
        self.assertEqual(solve(empty,self.p,.025)['actions'][0], 'joint_redesign_AB')

    def test_discrete_bellman_independent_agreement(self):
        for b in (.2,1,3):
            v=solve(self.v,self.p,b)['initial_net']
            independent=discrete_bellman(self.v,self.p,b,steps=10000)
            self.assertAlmostEqual(v,independent,delta=0.004)

    def test_state_value_monotone(self):
        for s in range(4):
            vals=[solve(self.v,self.p,b)['values'][s] for b in (0,.1,.3,1,3,8)]
            self.assertTrue(all(x<=y+1e-7 for x,y in zip(vals,vals[1:])))

    def test_optional_event_does_not_reduce_value(self):
        p2=self.p[:2]
        for b in (.1, 1, 2, 5):
            self.assertGreaterEqual(solve(self.v,self.p,b)['initial_net']+1e-8,
                                    solve(self.v,p2,b)['initial_net'])

    def test_all_free_values_cannot_generate_gain(self):
        for b in (.1, 1, 10):
            self.assertAlmostEqual(solve((0,0,0,0),self.p,b)['initial_net'],0,places=10)

    def test_invalid_monotonicity_and_program(self):
        with self.assertRaises(ValueError):
            validate((0,5,0,4),self.p)
        with self.assertRaises(ValueError):
            validate(self.v,(Program('bad',0,1),))
        with self.assertRaises(ValueError):
            solve(self.v,self.p,-1)

    def test_small_budget_direct_joint_changes_order(self):
        empty=(0,0,0,10)
        joint=solve(empty,(Program('all',3,1.2),),1e-5)['initial_net']
        serial=solve(empty,(Program('A',1,2),Program('B',2,2)),1e-5)['initial_net']
        self.assertAlmostEqual(joint/1e-5,11,delta=.01)
        self.assertLess(serial/(1e-5),.005)

if __name__ == '__main__': unittest.main()
