import unittest
from fractions import Fraction as F

from model.recursive_firm_feedback import (COMMON, CONTRAST, next_gain, optimal_gain,
                                           prediction_variance, regime_report, site_updates,
                                           tracking_loss)


class TestRecursiveFirmFeedback(unittest.TestCase):
    def test_exact_stationary_losses_and_break_even_cost(self):
        modes = (COMMON, CONTRAST)
        pooled = tracking_loss(modes, (F(1, 2), F(1, 2)))
        paired = tracking_loss(modes, (F(1, 5), F(4, 5)))
        self.assertEqual((pooled, paired, pooled - paired), (35, F(55, 2), F(15, 2)))
        self.assertEqual(tracking_loss(modes, (F(4, 5), F(1, 5))), F(1065, 16))

    def test_first_order_condition_and_site_marginals(self):
        for (q, r), expected in ((COMMON, F(1, 5)), (CONTRAST, F(4, 5)), ((35, 70), F(1, 2))):
            self.assertEqual(r * expected ** 2 + q * expected, q)
            self.assertAlmostEqual(optimal_gain(q, r), float(expected))
            for step in (-F(1, 100), F(1, 100)):
                self.assertLess(prediction_variance(q, r, expected), prediction_variance(q, r, expected + step))
        self.assertEqual(site_updates(F(1, 5), F(4, 5)), (F(1, 2), -F(3, 10)))
        # An independent-site world has the same site marginals but uniform gains.
        same_marginals = ((F(35, 2), 35),) * 2
        self.assertEqual(tracking_loss(same_marginals, (F(1, 2),) * 2), 35)
        self.assertEqual(site_updates(F(1, 2), F(1, 2)), (F(1, 2), 0))

    def test_update_timing_and_missing_observations(self):
        self.assertEqual(next_gain(F(15), 60, 3), (F(1, 5), F(15)))
        self.assertEqual(next_gain(F(15), 15, 3), (F(1, 2), F(21, 2)))
        gain, prior = next_gain(F(15), None, 3)
        self.assertEqual((gain, prior), (0, 18))
        self.assertGreater(next_gain(prior, 60, 3)[0], F(1, 5))
        self.assertEqual(next_gain(F(15), 0, 3), (1, 3))

    def test_variance_recursion_agrees_with_stationary_calculation(self):
        for q, r in (COMMON, CONTRAST):
            gain = optimal_gain(q, r)
            variance = 800.0
            for _ in range(200):
                variance = q + (1 - gain) ** 2 * variance + gain ** 2 * r
            self.assertAlmostEqual(variance, prediction_variance(q, r, gain))

    def test_report_accuracy_and_cost_of_overreaction(self):
        chance = regime_report(0.5)
        self.assertEqual(chance["report_value_before_cost"], 0)
        report = regime_report(0.75)
        correct, wrong = F(55, 2), F(1065, 16)
        self.assertEqual(F(3, 4) * correct + F(1, 4) * wrong, F(2385, 64))
        self.assertEqual(report["full_strength_loss"], float(F(2385, 64)))
        cutoff = (wrong - 35) / (wrong - correct)
        self.assertEqual(cutoff, F(101, 125))
        self.assertAlmostEqual(regime_report(float(cutoff))["full_strength_loss"], 35)
        self.assertLess(report["calibrated_loss"], 35)
        self.assertGreater(report["full_strength_loss"], 35)
        gains = report["calibrated_gains"]
        mixed = 0.75 * tracking_loss((COMMON, CONTRAST), gains)
        mixed += 0.25 * tracking_loss((CONTRAST, COMMON), gains)
        self.assertAlmostEqual(mixed, report["calibrated_loss"])
        self.assertAlmostEqual(report["report_value_before_cost"], 1.6006370745)
        self.assertAlmostEqual(regime_report(1)["report_value_before_cost"], 7.5)
