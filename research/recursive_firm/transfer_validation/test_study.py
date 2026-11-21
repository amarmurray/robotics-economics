import unittest
import numpy as np
from study import World, simulate, T, fee_break_even

class Checks(unittest.TestCase):
    def test_audit_and_training_budgets(self):
        w=World(range(8),"reversal")
        a=simulate(w,14,policy="versioned",lag=7)
        b=simulate(w,14,policy="rotation_pinned",lag=7)
        np.testing.assert_array_equal(a["audits"],b["audits"])
        self.assertTrue(np.all(a["audits"]==14))
        self.assertTrue(np.all(a["native_incidents"]<=a["updates"]))
        self.assertTrue(np.all(a["updates"]<=T))

    def test_closed_window_replicates_fixed(self):
        w=World(range(8),"drift")
        a=simulate(w,14)
        b=simulate(w,14,policy="versioned",window=(0,0))
        for k in a:
            np.testing.assert_array_equal(a[k],b[k])

    def test_fee_settlement_and_local_heads(self):
        w=World(range(16),"late")
        fixed=simulate(w,0)
        np.testing.assert_array_equal(fixed["native_incidents"],fixed["updates"])
        paid=simulate(w,14,policy="versioned")
        fee=fee_break_even(paid,fixed)
        replay=simulate(w,14,policy="versioned",fee=fee)
        self.assertAlmostEqual(replay["cash"].mean(),fixed["cash"].mean(),delta=.001)
