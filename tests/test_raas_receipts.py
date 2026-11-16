import unittest
from fractions import Fraction as Q
from model.raas_receipts import outcome


class RaaSReceiptsTests(unittest.TestCase):
    def test_exact_contract_comparison(self):
        old=outcome(2,4);new=outcome(4,4)
        self.assertEqual((old['q'],new['q']),(4,5))
        self.assertEqual((old['terminal_cash'],new['terminal_cash']),(12,Q(15,4)))
        self.assertEqual((old['source_joint_surplus'],new['source_joint_surplus']),(14,Q(65,4)))
        self.assertEqual(outcome(4,2,'output')['terminal_cash'],13)
        self.assertEqual(outcome(2,3,'output')['terminal_cash'],Q(27,2))
        self.assertEqual(outcome(4,3,'output')['terminal_cash'],Q(57,4))

    def test_participation_and_funding_interval(self):
        for n in range(8,49):
            s=Q(n,12)
            row=outcome(s,4)
            self.assertEqual(row['invested'],Q(4,3)<=s<=2)
            self.assertGreaterEqual(row['customer_profit'],row['customer_outside'])
            if s<Q(4,3):self.assertEqual(row['receipts'],0)

    def test_advance_not_additional_value_and_operating_cash_reserved(self):
        for s in (Q(2),Q(4)):
            for cash in (Q(0),Q(4)):
                for fraction in (Q(0),Q(1,2),Q(1)):
                    row=outcome(s,4,cash=cash,advance_fraction=fraction)
                    self.assertGreaterEqual(row['provider_profit']-row['loan'],0)
                    self.assertEqual(row['terminal_cash'],cash+row['provider_profit']+(6 if row['invested'] else 0))
                    if cash==4:self.assertTrue(row['invested'])

    def test_retention_and_repricing_counterexamples(self):
        old=outcome(2,4)['terminal_cash'];new=outcome(4,4)['terminal_cash']
        self.assertEqual(max(old,new),old)
        for s in (Q(2),Q(4)):
            unit=outcome(s,3,'output');hourly=outcome(s,3*s,'hourly')
            for key in ('q','receipts','customer_profit','provider_profit','terminal_cash'):
                self.assertEqual(unit[key],hourly[key])

    def test_explicit_domain_restrictions(self):
        with self.assertRaises(ValueError):outcome(0,4)
        with self.assertRaises(ValueError):outcome(1,1) # more than three robot hours
        with self.assertRaises(ValueError):outcome(2,4,contract='unmodelled')


if __name__=='__main__':unittest.main()
