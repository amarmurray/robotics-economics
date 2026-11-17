"""Scoped exact tests of the synthetic counterexample, not observed BEA data."""
import unittest
from fractions import Fraction as F
import sector_bridge as m

class TestSectorBridge(unittest.TestCase):
    def test_balances(self): self.assertIsNone(m.validate())
    def test_reversed_customer_adoption(self):
        a=m.opportunities(m.TASK_E1);b=m.opportunities(m.TASK_E2)
        self.assertTrue(a['manufacturing']['customer_buys'])
        self.assertFalse(a['health_services']['customer_buys'])
        self.assertFalse(b['manufacturing']['customer_buys'])
        self.assertTrue(b['health_services']['customer_buys'])
    def test_profits(self):
        a=m.opportunities(m.TASK_E1)
        self.assertEqual(a['manufacturing']['customer_gain'],F(15))
        self.assertEqual(a['manufacturing']['provider_profit'],F(3))
    def test_output_conservation(self):
        for i in range(3):
            self.assertEqual(sum(m.USE[i])+m.FINAL[i],m.OUTPUT[i])
            self.assertEqual(sum(m.USE[j][i] for j in range(3))+m.VALUE_ADDED[i],m.OUTPUT[i])
    def test_demand_propagation_E1(self):
        dy,dx=m.conditional_feedback(m.TASK_E1,'manufacturing')
        self.assertEqual(dy,F(3,2))
        self.assertEqual(dx,(F(13,23),F(321,184),F(25,184)))
    def test_demand_propagation_E2(self):
        dy,dx=m.conditional_feedback(m.TASK_E2,'health_services')
        self.assertEqual(dy,F(3,2))
        self.assertEqual(dx,(F(6,23),F(21,92),F(165,92)))
    def test_no_response_if_no_purchase(self):
        self.assertEqual(m.conditional_feedback(m.TASK_E1,'health_services')[1],(F(0),)*3)
    def test_invalid_pass_through(self):
        with self.assertRaises(ValueError):m.conditional_feedback(m.TASK_E1,'manufacturing',pass_through=F(3,2))
if __name__=='__main__':unittest.main()
