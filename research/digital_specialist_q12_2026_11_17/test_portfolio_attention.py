import unittest, json
from dataclasses import replace
from fractions import Fraction as F
from itertools import product
from portfolio_attention import (Environment,Policy,FLEX,DEDICATED,COORDINATED,
                                 optimize,states,value,compare,full_capacity_difference,
                                 expected_surplus,results)

class PortfolioAttentionTests(unittest.TestCase):
    def test_closed_form_vs_exact_across_joint_dependence(self):
        for i in range(21):
            e=Environment(synchrony=F(i,20))
            self.assertEqual(value(e,FLEX)-value(e,COORDINATED),full_capacity_difference(e))

    def test_exact_synchrony_threshold(self):
        self.assertEqual(full_capacity_difference(Environment(synchrony=F(3,5))),F(0))
        self.assertEqual(compare(Environment(synchrony=F(3,5)))['winner'],'dedicated_digital')
        self.assertEqual(compare(Environment(synchrony=F(0)))['winner'],'qualified_flexible')
        self.assertEqual(compare(Environment(synchrony=F(1)))['winner'],'dedicated_digital')

    def test_attention_reverses_antiphase_choice(self):
        e=Environment(H=F(4,5))
        self.assertEqual(value(e,FLEX)-value(e,COORDINATED),-F(54,125))
        self.assertEqual(compare(e)['winner'],'dedicated_digital')

    def test_attention_release_reverses_back(self):
        self.assertEqual(value(Environment(),FLEX)-value(Environment(),COORDINATED),F(6,25))

    def test_tight_attention_not_misused_as_closed_form(self):
        with self.assertRaises(ValueError):full_capacity_difference(Environment(H=F(4,5)))

    def test_joint_distribution_preserves_marginal(self):
        for s in (F(0),F(1,7),F(1,2),F(1)):
            e=Environment(synchrony=s)
            st=states(e)
            self.assertEqual(sum(p for _,a,b,p in st),1)
            self.assertEqual(sum(p for _,a,b,p in st if a==e.d_high),F(1,2))
            self.assertEqual(sum(p for _,a,b,p in st if b==e.d_high),F(1,2))

    def test_exact_state_allocation(self):
        e=Environment()
        f=optimize(F(5),F(3),e.b,e.H,FLEX)
        self.assertEqual((f.q_a,f.q_b),(F(3,2),F(1,2)))
        self.assertEqual(optimize(F(5),F(3),e.b,e.H,COORDINATED).q_a,F(1))

    def test_optimization_respects_constraints(self):
        for h in (F(0),F(1,5),F(4,5),F(1),F(3)):
            for da,db in product((F(0),F(1),F(3),F(5),F(10)), repeat=2):
                for p in (FLEX,DEDICATED,COORDINATED):
                    z=optimize(da,db,F(2),h,p)
                    self.assertGreaterEqual(z.q_a,0)
                    self.assertGreaterEqual(z.q_b,0)
                    self.assertLessEqual(z.q_a,p.cap_a)
                    self.assertLessEqual(z.q_b,p.cap_b)
                    self.assertLessEqual(z.q_a+z.q_b,p.cap_total)
                    self.assertLessEqual(p.attention_a*z.q_a+p.attention_b*z.q_b,h)

    def test_finite_grid_independent_global_lower_bound(self):
        # Any independent feasible grid candidate must be no better than exact optimizer.
        for H in (F(1,2),F(4,5),F(1),F(2)):
            for da,db in ((F(3),F(5)),(F(5),F(5)),(F(1),F(4))):
                for p in (FLEX,DEDICATED,COORDINATED):
                    v=optimize(da,db,F(2),H,p).surplus
                    for i,j in product(range(21),repeat=2):
                        qa,qb=F(i,10),F(j,10)
                        if (qa<=p.cap_a and qb<=p.cap_b and qa+qb<=p.cap_total
                                and p.attention_a*qa+p.attention_b*qb<=H):
                            g=(da-p.overhead_a)*qa+(db-p.overhead_b)*qb-(qa*qa+qb*qb)
                            self.assertLessEqual(g,v)

    def test_attention_makes_gross_surplus_monotone(self):
        for p in (FLEX,DEDICATED,COORDINATED):
            for a,b in ((F(5),F(3)),(F(3),F(3)),(F(2),F(5))):
                vals=[optimize(a,b,F(2),F(i,10),p).surplus for i in range(21)]
                self.assertTrue(all(x<=y for x,y in zip(vals,vals[1:])))

    def test_lower_attention_requirement_does_not_reduce_output_value(self):
        p=DEDICATED
        q=replace(DEDICATED,attention_a=F(2,5),attention_b=F(2,5),cost=DEDICATED.cost)
        for h in map(lambda j:F(j,10),range(21)):
            for da,db in ((F(5),F(3)),(F(3),F(3)),(F(5),F(5))):
                self.assertGreaterEqual(optimize(da,db,F(2),h,q).surplus,
                                        optimize(da,db,F(2),h,p).surplus)

    def test_digital_rights_gate(self):
        e=Environment(synchrony=F(1))
        self.assertIsNone(value(e,replace(COORDINATED,rights=False)))
        d=compare(e,(FLEX,DEDICATED,replace(COORDINATED,rights=False)))
        self.assertNotEqual(d['winner'],'dedicated_digital')

    def test_flex_missing_B_qualification(self):
        e=Environment()
        p=replace(FLEX,eligible_b=False)
        self.assertEqual(optimize(F(5),F(3),F(2),e.H,p).q_b,F(0))
        self.assertLess(value(e,p),value(e,COORDINATED))

    def test_liquidity_gate(self):
        e=Environment(budget=F(2))
        self.assertIsNone(value(e,FLEX))
        self.assertIsNone(value(e,COORDINATED))
        self.assertEqual(compare(e)['winner'],'dedicated_uncoordinated')

    def test_no_work_without_demand(self):
        p=FLEX
        z=optimize(F(0),F(0),F(2),F(1),p)
        self.assertEqual((z.q_a,z.q_b,z.surplus),(0,0,0))

    def test_high_cash_does_not_change_unconstrained_best(self):
        for b in (F(3),F(100)):
            self.assertEqual(compare(Environment(budget=b))['winner'],'qualified_flexible')

    def test_same_total_physical_capacity(self):
        self.assertEqual(FLEX.cap_total,DEDICATED.cap_total)
        self.assertEqual(FLEX.cap_total,COORDINATED.cap_total)
        self.assertEqual(FLEX.cost,COORDINATED.cost)

    def test_provider_capture_zero_costs_still_count(self):
        e=Environment(capture=F(0))
        for p in (FLEX,DEDICATED,COORDINATED): self.assertEqual(value(e,p),-p.cost)

    def test_validation_of_invalid_parameters(self):
        with self.assertRaises(ValueError):Environment(synchrony=F(2))
        with self.assertRaises(ValueError):Environment(H=F(-1))
        with self.assertRaises(ValueError):optimize(F(1),F(2),F(0),F(1),FLEX)
        with self.assertRaises(ValueError):Policy('bad',F(-1),F(0),F(0),F(0),F(0),F(0))

    def test_json_determinism(self):
        self.assertEqual(json.dumps(results(),sort_keys=True),json.dumps(results(),sort_keys=True))

if __name__=='__main__':unittest.main()
