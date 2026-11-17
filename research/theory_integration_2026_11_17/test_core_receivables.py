import math
import unittest
from core_receivables import effort,survival_completion,sustainable_share,full_effort_bridge,pledgeable_full_effort,staged_probability

class CoreTest(unittest.TestCase):
    def test_no_invoice_maturity(self):
        self.assertEqual(effort(2,.5,1,100,3),.5)
    def test_cash_can_wait(self):
        self.assertEqual(effort(2,.25,1,4.5,1),1.25)
    def test_full_receipt_self_finance(self):
        self.assertEqual(effort(4,1,1,2,1),4)
    def test_slow_collection_rate(self):
        self.assertAlmostEqual(effort(4,0,1,.25,1),.75)
    def test_survival(self):
        self.assertAlmostEqual(survival_completion(2,.25,1,4.5,1,2),1-math.exp(-2.5))
    def test_resource_sharing(self):
        self.assertAlmostEqual(sustainable_share(1,2,0),2/3)
        self.assertEqual(sustainable_share(1,2,1),1)
    def test_lender_liquidity(self):
        self.assertEqual(full_effort_bridge(2,.25,1,4.5,1,1),.75)
        self.assertEqual(full_effort_bridge(4,.25,1,4.5,1,0),3.75)
    def test_lender_receipts(self):
        val=pledgeable_full_effort(2,2,10,.2)
        self.assertAlmostEqual(val,3.018315638888734)
        self.assertEqual(pledgeable_full_effort(2,2,10,.2,3),0)
    def test_staged_integral_benchmarks(self):
        self.assertAlmostEqual(staged_probability(2,.5,1,1,2,2,4.5,0),.6138049199398236,places=8)
        self.assertAlmostEqual(staged_probability(2,.5,1,1,2,2,4.5,1),.5465723439598089,places=8)
        self.assertAlmostEqual(staged_probability(2,.5,1,1,2,2,0,2),1-2/math.e,places=8)
    def test_validation(self):
        with self.assertRaises(ValueError):sustainable_share(1,2,1.1)
        with self.assertRaises(ValueError):pledgeable_full_effort(2,2,10,2)

if __name__=='__main__':unittest.main()
