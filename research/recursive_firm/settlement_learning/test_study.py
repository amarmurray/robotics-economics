import unittest
import numpy as np
from study import channel, simulate, tape, HORIZON, TRANS


class SettlementTests(unittest.TestCase):
    def test_aggregate_alias_and_separation(self):
        _, channel_prob, _ = channel(.93)
        np.testing.assert_allclose(channel_prob.sum(axis=2), 1.)
        np.testing.assert_allclose(channel_prob[0,1],channel_prob[0,2])
        np.testing.assert_allclose(channel_prob[3,1],channel_prob[3,2])
        self.assertGreater(np.abs(channel_prob[1,1]-channel_prob[1,2]).sum(),1.)
        np.testing.assert_allclose(TRANS.sum(axis=1),1.)

    def test_common_cost_accounting(self):
        u=tape(23,48)
        for policy in ("target","incumbent","experiment","selective","tagged"):
            a=simulate(u,"reversal",policy,span=3,cadence=8,lag=3)
            np.testing.assert_allclose(a[:,0],5*a[:,1]-2*a[:,3]-.6*a[:,4])
            self.assertTrue(np.all(a[:,4]<=HORIZON))
            self.assertTrue(np.all((0<=a[:,2]) & (a[:,2]<=1+1e-12)))
    
    def test_uninformative_audit_changes_only_fee(self):
        u=tape(21,32)
        a=simulate(u,"single","incumbent",span=3,cadence=8,lag=3)
        b=simulate(u,"single","experiment",span=3)
        np.testing.assert_allclose(a[:,0]+2*a[:,3],b[:,0])
        np.testing.assert_array_equal(a[:,1],b[:,1])

    def test_target_fee_settles_on_actual_reviews(self):
        u=tape(25,32)
        a=simulate(u,"stable","target",lag=1,fee=0.)
        b=simulate(u,"stable","target",lag=1,fee=2.)
        np.testing.assert_allclose(a[:,0]-b[:,0],2*a[:,3])
