import unittest
from fractions import Fraction as Q
from model.selection_identification import selection


class SelectionIdentificationTests(unittest.TestCase):
    def test_observational_equivalence_and_reversed_economic_order(self):
        high=selection(Q(2,5),Q(12,5),Q(7,5));low=selection(Q(2,5),Q(6,5),Q(7,5))
        inc=selection(Q(4,5),0,Q(7,5))
        self.assertLess(high['economic_threshold'],inc['economic_threshold'])
        self.assertGreater(low['economic_threshold'],inc['economic_threshold'])
        for key in ('observed_threshold','development_probability','mean_successful_revenue','required_loan','success_state_repayment'):
            self.assertEqual(high[key],low[key])
        self.assertEqual((high['observed_threshold'],high['development_probability'],high['mean_successful_revenue']),(6,Q(2,5),8))

    def test_cash_variation_separates(self):
        high=selection(Q(2,5),Q(12,5),Q(23,10));low=selection(Q(2,5),Q(6,5),Q(23,10))
        self.assertEqual((high['observed_threshold'],high['development_probability'],high['mean_successful_revenue']),(3,Q(7,10),Q(13,2)))
        self.assertEqual((low['observed_threshold'],low['development_probability'],low['mean_successful_revenue']),(5,Q(1,2),Q(15,2)))

    def test_feasible_budget_and_value_equal_threshold_rule(self):
        for learning in (Q(0),Q(4,5),Q(6,5),Q(12,5),Q(3)):
            for cash in (Q(0),Q(7,5),Q(23,10),Q(16,5)):
                row=selection(Q(2,5),learning,cash)
                for n in range(101):
                    revenue=Q(n,10)
                    eligible=(Q(2,5)*revenue+learning>=Q(16,5) and cash+Q(3,10)*revenue>=Q(16,5))
                    self.assertEqual(eligible,revenue>=row['observed_threshold'])
                    if eligible:
                        self.assertLessEqual(row['success_state_repayment'],Q(3,4)*revenue)
                        self.assertEqual(Q(2,5)*row['success_state_repayment'],row['required_loan'])

    def test_identified_interval_and_common_prescreen_prior(self):
        prior=Q(2,5);bad_signal=Q(5,6)
        self.assertEqual(prior/(prior+(1-prior)*(1-bad_signal)),Q(4,5))
        for k in range(8,32):
            self.assertEqual(selection(prior,Q(k,10),Q(7,5))['observed_threshold'],6)
        self.assertGreater(selection(prior,Q(7,10),Q(7,5))['observed_threshold'],6)


if __name__=='__main__':unittest.main()
