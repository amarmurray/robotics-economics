import unittest
import numpy as np
from adapter_repair import environment, run, T


class AdapterTests(unittest.TestCase):
    def test_geometry_same_counts_same_orders(self):
        a=environment(range(12),"coherent")
        b=environment(range(12),"fragmented")
        np.testing.assert_array_equal(a.orders,b.orders)
        np.testing.assert_array_equal(a.source,b.source)
        def discrepancy(w):
            return (w.target!=w.source[:,:,None,:]).sum(axis=3)
        np.testing.assert_array_equal(discrepancy(a),discrepancy(b))
        self.assertTrue(np.all(discrepancy(a)[:,-1,1:]==6))

    def test_fee_is_charged_only_on_acquired_labels(self):
        w=environment(range(20),"coherent")
        a=run(w,(1,2),paired=True,pair_fee=0)
        b=run(w,(1,2),paired=True,pair_fee=2)
        np.testing.assert_allclose(a["cash"]-b["cash"],2*a["repair_updates"])
        np.testing.assert_array_equal(a["orders"],b["orders"])
        self.assertTrue(np.all(a["donor_updates"]+a["local_updates"]+a["repair_updates"]<=T))

    def test_rotation_and_priority_receive_matched_audits(self):
        w=environment(range(20),"revert")
        a=run(w,(1,1),audit="priority",delay=7,cadence=6)
        b=run(w,(1,1),audit="rotation",delay=7,cadence=6)
        np.testing.assert_array_equal(a["audits"],b["audits"])
        self.assertTrue(np.all(a["audits"]==9))

    def test_raw_fleet_cannot_benefit_from_unused_spare_slot(self):
        w=environment(range(8),"stable")
        a=run(w,(1,1))
        b=run(w,(1,1),donor_slot=True)
        np.testing.assert_allclose(a["cash"],b["cash"])
        self.assertTrue(np.all(a["repair_updates"]==0))

if __name__=="__main__":
    unittest.main()
