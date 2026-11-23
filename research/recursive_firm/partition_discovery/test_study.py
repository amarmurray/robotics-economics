import unittest
import numpy as np
from study import simulate, world


class DiscoveryTests(unittest.TestCase):
    def setUp(self):
        self.w = world(24, 64, "independent")

    def test_holdout_shift_cannot_change_acquisition_or_qualification(self):
        a = simulate(self.w, "learned", "independent")
        b = simulate(self.w, "learned", "new_site")
        np.testing.assert_array_equal(a[:, [2, 3, 4, 6]], b[:, [2, 3, 4, 6]])
        self.assertTrue(np.any(a[:, 5] != b[:, 5]))

    def test_pair_price_settles_only_purchased_records(self):
        a = simulate(self.w, "mixture", "independent", price=0)
        b = simulate(self.w, "mixture", "independent", price=1)
        np.testing.assert_allclose(a[:, 0]-b[:, 0], a[:, 2])
        np.testing.assert_array_equal(a[:, 1:], b[:, 1:])

    def test_raw_spends_no_robot_budget(self):
        a = simulate(self.w, "raw", "independent")
        np.testing.assert_array_equal(a[:, [2, 3, 6]], 0)
        np.testing.assert_array_equal(a, simulate(self.w, "raw", "independent", reserve=True))

    def test_matched_audits_and_capacity(self):
        for design in ("shuffled", "learned", "mixture"):
            a = simulate(self.w, design, "reversal", period=8)
            np.testing.assert_array_equal(a[:, 3], 9)
            self.assertTrue(np.all(a[:, 2] + a[:, 4] <= 72))
