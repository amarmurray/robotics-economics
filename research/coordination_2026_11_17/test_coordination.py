from dataclasses import replace
from fractions import Fraction as F
import json
import unittest
from coordination import stationary,effective_capacity,Market,Operations,enumerate_choices,optimal,cross_effects,binding_interaction_threshold,encode,exact_results


class QueueTests(unittest.TestCase):
    def test_zero_robots(self):self.assertEqual(stationary(0,F(1),F(1)),(F(1),))
    def test_no_incidents(self):self.assertEqual(effective_capacity(4,F(0)),F(4))
    def test_one_machine(self):self.assertEqual(effective_capacity(1,F(1),F(2)),F(2,3))
    def test_stationarity_sum(self):
        for n in range(1,10):
            for lam in (F(0),F(1,10),F(1,2),F(3)):
                for c in (1,2,4):
                    p=stationary(n,lam,F(1),c)
                    self.assertEqual(sum(p),1)
                    self.assertTrue(all(x>=0 for x in p))
                    for k in range(1,n+1):
                        self.assertEqual(p[k]*min(k,c)*1,p[k-1]*(n-k+1)*lam)
    def test_flow_balance_ceiling(self):
        for n in (1,2,4,8,12):
            for lam in (F(1,10),F(1,2),F(2)):
                for c in (1,2,3):
                    p=stationary(n,lam,F(1),c)
                    active=effective_capacity(n,lam,F(1),c)
                    self.assertEqual(lam*active,sum(F(min(k,c))*p[k] for k in range(1,n+1)))
                    self.assertLessEqual(active,F(c)/lam)
    def test_hardware_nonnegative_gain_capacity(self):
        for n in range(1,12):
            for l in (F(1,10),F(1,2),F(1),F(2)):
                self.assertGreaterEqual(effective_capacity(n+1,l),effective_capacity(n,l))
    def test_more_supervision_or_reduced_incidents(self):
        for n in range(1,12):
            for lam in (F(1,10),F(1,2),F(3)):
                self.assertGreaterEqual(effective_capacity(n,lam,supervisors=2),effective_capacity(n,lam))
                self.assertGreaterEqual(effective_capacity(n,lam/2),effective_capacity(n,lam))
    def test_ceiling_convergence(self):
        self.assertGreater(effective_capacity(48,F(1,2)),F(199,100))
        self.assertLessEqual(effective_capacity(48,F(1,2)),F(2))
    def test_invalid_queue_parameters(self):
        for args in [(-1,F(1),F(1)),(1,F(-1),F(1)),(1,F(1),F(0)),(1,F(1),F(1),0)]:
            with self.assertRaises(ValueError):stationary(*args)
        with self.assertRaises(ValueError):effective_capacity(1,F(1),rate=F(-1))


class EconomicTests(unittest.TestCase):
    def setUp(self):
        self.ops=Operations()
        self.market=Market(F(18),F(2),F(2),F(5))
    def test_low_failure_hardware(self):
        w=optimal(replace(self.ops,incident_rate=F(1,10)),self.market)
        self.assertEqual((w.hardware,w.digital,w.additional_supervisor),(1,0,0))
    def test_high_failure_digital(self):
        w=optimal(replace(self.ops,budget=F(3)),self.market)
        self.assertEqual((w.hardware,w.digital,w.additional_supervisor),(0,1,0))
    def test_high_incident_joint_with_budget(self):
        w=optimal(self.ops,self.market)
        self.assertEqual((w.hardware,w.digital,w.additional_supervisor),(1,1,0))
    def test_demand_saturation(self):
        w=optimal(self.ops,Market(F(5),F(2),F(2)))
        self.assertEqual((w.hardware,w.digital,w.additional_supervisor),(0,0,0))
    def test_zero_budget(self):
        w=optimal(replace(self.ops,budget=F(0)),self.market)
        self.assertEqual(w.outlay,F(0))
    def test_budget_respected_and_value_non_decreasing(self):
        for l in (F(1,10),F(1,2)):
            values=[]
            for B in range(12):
                o=replace(self.ops,incident_rate=l,budget=F(B))
                w=optimal(o,self.market)
                self.assertLessEqual(w.outlay,B)
                values.append(w.gain)
            self.assertTrue(all(a<=b for a,b in zip(values,values[1:])))
    def test_option_not_harmful(self):
        for l in (F(1,10),F(1,4),F(1,2)):
            self.assertGreaterEqual(optimal(replace(self.ops,incident_rate=l,budget=F(6)),self.market).gain,
                                    optimal(replace(self.ops,incident_rate=l,budget=F(0)),self.market).gain)
    def test_provider_and_customer_share_incremental_surplus(self):
        m=self.market;K=effective_capacity(4,F(1,2));q,provider,customer=m.outcome(K)
        G=(m.a-m.resource_cost)*q-m.b*q*q/2
        self.assertEqual(provider+customer,G)
    def test_outside_option_and_no_adoption(self):
        m=replace(self.market,outside_profit=F(1000))
        self.assertEqual(m.outcome(F(3)),(F(0),F(0),F(1000)))
    def test_customer_saturation_decreases_private_investment_return(self):
        for o in enumerate_choices(self.ops,Market(F(5),F(2),F(2))):
            self.assertLessEqual(o.gain,F(0))
    def test_physical_complement_but_value_substitution(self):
        o=Operations(robots=3,incident_rate=F(1,2),budget=F(6))
        low=cross_effects(o,Market(F(31,4),F(2),F(2)))
        high=cross_effects(o,Market(F(10),F(2),F(2)))
        self.assertGreater(low['physical'],0)
        self.assertEqual(low['physical'],high['physical'])
        self.assertLess(low['private'],0)
        self.assertGreater(high['private'],0)
    def test_interaction_threshold_within_binding_region(self):
        ops=Operations(robots=3,incident_rate=F(1,2),budget=F(6))
        m=Market(F(31,4),F(2),F(2))
        complement, threshold, binding_min = binding_interaction_threshold(ops,m)
        self.assertGreater(complement,F(0))
        self.assertGreater(threshold,binding_min)
        self.assertLess(m.a-m.resource_cost,threshold)
        self.assertGreater(F(8),threshold)
        self.assertEqual(complement,F(961508,2917887))
    def test_incident_flow_zero_requests(self):
        p=stationary(5,F(0),F(1))
        self.assertEqual(p[0],1)
        self.assertEqual(sum(p[1:]),0)

    def test_supervisor_is_separate_choice(self):
        cs=enumerate_choices(self.ops,self.market)
        self.assertTrue(any(x.additional_supervisor==1 and x.hardware==x.digital==0 for x in cs))
    def test_invalid_ops_market(self):
        with self.assertRaises(ValueError):Operations(digital_rate_factor=F(0))
        with self.assertRaises(ValueError):Operations(budget=F(-1))
        with self.assertRaises(ValueError):Market(F(4),F(0),F(1))
        with self.assertRaises(ValueError):Market(F(4),F(2),F(1),capture=F(2))
    def test_serialization_deterministic(self):
        a=json.dumps(encode(exact_results()),sort_keys=True)
        b=json.dumps(encode(exact_results()),sort_keys=True)
        self.assertEqual(a,b)

if __name__=='__main__':unittest.main()
