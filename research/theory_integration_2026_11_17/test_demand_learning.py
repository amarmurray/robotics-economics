import unittest
from dataclasses import replace
from math import sqrt
from demand_learning import (Economy,scalars,max_effort,output,net_a,shared_value,
                             optimal_shared,specialist,financially_sustainable_effort,
                             discrete_shared_value,penalty_optimized,examples)


class TheoryTests(unittest.TestCase):
    def setUp(self): self.e=Economy()
    def test_base_analytic(self):
        x=optimal_shared(self.e)
        self.assertAlmostEqual(x['u'],.5)
        self.assertAlmostEqual(x['value'],2.5)
        self.assertAlmostEqual(x['no_learning'],2.)
        self.assertEqual((x['g0'],x['L'],x['h']),(2.,0.,2.))
    def test_specialist_competitor(self):
        self.assertAlmostEqual(specialist(self.e)['value'],2.4)
        self.assertGreater(optimal_shared(self.e)['value'],specialist(self.e)['value'])
    def test_contract_floor_and_ranking(self):
        e=replace(self.e,q_floor=.9)
        x=optimal_shared(e)
        self.assertAlmostEqual(x['cap'],.1)
        self.assertAlmostEqual(x['u'],.1)
        self.assertAlmostEqual(x['value'],2.2333333333333334)
        self.assertLess(x['value'],specialist(e)['value'])
    def test_high_incumbent_demand(self):
        e=replace(self.e,m=6,W=6)
        x=optimal_shared(e)
        self.assertAlmostEqual(x['u'],(sqrt(2)-1)/2)
        self.assertAlmostEqual(x['value'],4.5-(sqrt(2)-1))
        self.assertLess(x['value'],specialist(e)['value'])
    def test_demand_switch_exact_boundary(self):
        m=31/5-4*sqrt(5)/5
        e=replace(self.e,m=m,W=m)
        self.assertAlmostEqual(optimal_shared(e)['value'],specialist(e)['value'],places=11)
        self.assertGreater(optimal_shared(replace(e,m=4,W=4))['value'],specialist(replace(e,m=4,W=4))['value'])
        self.assertLess(optimal_shared(replace(e,m=6,W=6))['value'],specialist(replace(e,m=6,W=6))['value'])
    def test_sustainable_quadratic_cash_share(self):
        u=financially_sustainable_effort(self.e)
        self.assertAlmostEqual(u,(sqrt(17)-1)/4)
        self.assertAlmostEqual(net_a(self.e,u),self.e.c*u)
    def test_cash_share_contract_gated(self):
        self.assertAlmostEqual(financially_sustainable_effort(replace(self.e,q_floor=.9)),.1)
    def test_independent_production(self):
        e=replace(self.e,eta=1)
        self.assertEqual(max_effort(e),1.)
        self.assertAlmostEqual(financially_sustainable_effort(e),1.)
        self.assertAlmostEqual(net_a(e,0),net_a(e,1))
    def test_zero_curvature_case(self):
        e=replace(self.e,eta=1,c=1)
        self.assertAlmostEqual(optimal_shared(e)['u'],1.)
    def test_no_value_of_learning(self):
        e=replace(self.e,W=1)
        self.assertEqual(optimal_shared(e)['u'],0.)
        self.assertEqual(optimal_shared(e)['value'],2.)
    def test_grid_global_optimum(self):
        for m,W,floor in [(4,4,0.),(4,4,.9),(6,6,0.),(7,7,0.),(4,1,0.)]:
            e=replace(self.e,m=m,W=W,q_floor=floor)
            x=optimal_shared(e)
            for i in range(1001):
                u=max_effort(e)*i/1000
                self.assertLessEqual(shared_value(e,u),x['value']+1e-9)
    def test_numerical_bellman_discretization(self):
        x=optimal_shared(self.e)['value']
        self.assertAlmostEqual(discrete_shared_value(self.e,.5,.0001),x,delta=.001)
        approx=max(discrete_shared_value(self.e,i/1000,.0001) for i in range(1001))
        self.assertAlmostEqual(approx,x,delta=.001)
    def test_concavity(self):
        for a,b in [(.1,.5),(.3,.7),(.7,1.)]:
            self.assertGreaterEqual(net_a(self.e,(a+b)/2)+1e-10,
                                    (net_a(self.e,a)+net_a(self.e,b))/2)
    def test_customer_qualified_output(self):
        self.assertAlmostEqual(output(replace(self.e,q_floor=.9),.1),.9)
        with self.assertRaises(ValueError): output(replace(self.e,q_floor=.9),.2)
    def test_penalty_accelerates_conditional_learning_but_can_flip_choice(self):
        mild=penalty_optimized(self.e,.9,.1)
        strong=penalty_optimized(self.e,.9,.25)
        self.assertTrue(mild['breaches_sla'])
        self.assertTrue(strong['breaches_sla'])
        self.assertGreater(mild['u'],.5)
        self.assertGreater(strong['u'],mild['u'])
        self.assertGreater(mild['value'],specialist(self.e)['value'])
        self.assertLess(strong['value'],specialist(self.e)['value'])
    def test_penalty_zero_recovers_unconstrained(self):
        x=penalty_optimized(self.e,.9,0)
        self.assertAlmostEqual(x['u'],.5)
        self.assertAlmostEqual(x['value'],2.5)
    def test_penalty_large_policy_never_breaches(self):
        x=penalty_optimized(self.e,.9,100)
        self.assertFalse(x['breaches_sla'])
        self.assertAlmostEqual(x['u'],.1)
    def test_invalid_inputs(self):
        for d in ({'m':2},{'q_floor':1.1},{'eta':-1},{'rho':0}):
            with self.assertRaises(ValueError): replace(self.e,**d)
    def test_result_serialization(self):
        y=examples()
        self.assertEqual(y['base']['winner'],'shared')
        self.assertEqual(y['contract_floor']['winner'],'specialist')
        self.assertEqual(y['higher_incumbent_demand']['winner'],'specialist')


if __name__=='__main__': unittest.main()
