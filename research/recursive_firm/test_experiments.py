from fractions import Fraction as F
import unittest

from evidence_budget import batch_value, posterior, solve, stop_value
from pilot_market import Offer, buyer_gain, exact_returns, settle


class MarketTests(unittest.TestCase):
    def test_fee_rents_and_resource_accounting(self):
        trial = Offer(F(13, 4), 8)
        self.assertEqual(buyer_gain(trial, F(1, 4)), F(1, 4))
        self.assertEqual(exact_returns(trial, 1, F(1, 4)),
                         {"pilot": True, "seller": 16.75, "buyers": 6.25, "joint": 23.0})
        for accepts in (False, True):
            for works in (False, True):
                for mature in (0, 1, 3):
                    for offer in (trial, Offer(5, 5), Offer(8, 8)):
                        s, b = settle(offer, mature, accepts, works)
                        total = 21 * mature - int(offer.uses_registry)
                        if accepts:
                            total += 3 * 10 * works - 3 * (1 + 2 * works)
                        self.assertEqual(s + b, total)

    def test_continuous_uniform_optima_and_threshold(self):
        p = F(1, 4)
        self.assertEqual(buyer_gain(Offer(5, 5), p), 0)
        self.assertLess(buyer_gain(Offer(F(501, 100), F(501, 100)), p), 0)
        for n in (0, 1):
            grid = [Offer(F(t, 4), F(t, 4)) for t in range(12, 33)]
            best = max(grid, key=lambda o: exact_returns(o, n, p)["seller"])
            self.assertEqual(best.first, 8 if n else 5)
        self.assertEqual(exact_returns(Offer(5, 5), 1, p)["joint"], 24)
        self.assertEqual(exact_returns(Offer(8, 8), 1, p)["joint"], 21)

    def test_ordinary_logs_equivalent_opposing_investments(self):
        uniform = Offer(8, 8)
        self.assertEqual(exact_returns(uniform, 1, F(1, 4)),
                         exact_returns(uniform, 1, F(1, 20)))
        self.assertGreater(24 * F(1, 4) - 3, 0)
        self.assertLess(24 * F(1, 20) - 3, 0)


class ResearchDesignTests(unittest.TestCase):
    def test_minimum_number_of_informative_probes(self):
        base = stop_value(0, 0)
        self.assertEqual(base, 6)
        self.assertEqual([batch_value(n) for n in (1, 2)], [base, base])
        self.assertEqual(batch_value(3) - base, F(5553, 4000))
        self.assertGreater(posterior(0, 2), F(1, 8))
        self.assertLess(posterior(0, 3), F(1, 8))

    def test_adaptive_policy_and_fixed_batch_comparator(self):
        best_batch = max(batch_value(n) - F(n, 5) for n in range(4))
        self.assertEqual(solve(0, 0, 1).action, "deploy")
        self.assertEqual(solve(0, 0, 2).action, "deploy")
        self.assertEqual(solve(0, 0, 3).action, "probe")
        self.assertEqual(solve(0, 3, 0).action, "decline")
        self.assertEqual(solve(1, 0, 2).action, "deploy")
        self.assertEqual(best_batch, F(27153, 4000))
        self.assertEqual(solve(0, 0, 3).value, F(27487, 4000))
        self.assertEqual(solve(0, 0, 3).value - best_batch, F(167, 2000))


if __name__ == "__main__":
    unittest.main()
