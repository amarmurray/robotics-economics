import unittest
from unittest.mock import patch

import numpy as np

import model
from model import BLOCK, EYE, MANUAL, OPTIONS, SUPPORT, WAGES, ZERO, Economy, draw
from reference_audit import archive_share, diagnostic_value, margins
from study import decisions, transmission


class NetworkProducts(unittest.TestCase):
    def setUp(self):
        self.world = draw(37111)
        self.base = Economy(self.world)

    def test_balance_and_separate_accounting(self):
        o = self.base.operating(1,ZERO)
        np.testing.assert_allclose(o.gross, o.final+self.base.network[1]@o.gross)
        np.testing.assert_allclose(o.human+o.machine_output, o.gross)
        np.testing.assert_allclose(o.labor, o.human@MANUAL + o.attempts@SUPPORT)
        external = o.final@self.world.price - o.labor@WAGES - o.attempts@model.RUN_COST
        self.assertAlmostEqual(external,o.profit)
        with patch.object(model,"INTERNAL_PRICE",np.zeros(4)):
            free = Economy(self.world).operating(1,ZERO)
        self.assertAlmostEqual(external,free.profit)
        self.assertFalse(np.allclose(o.ledger,free.ledger))

    def test_physical_frontier_concavity_bound(self):
        o = self.base.operating(0,ZERO,objective="physical_frontier")
        for i,k in enumerate(OPTIONS[1:]):
            more = self.base.operating(0,k,objective="physical_frontier")
            slope = (more.final-o.final)@self.world.price/BLOCK[i]
            self.assertGreaterEqual(slope,-1e-8)
            self.assertLessEqual(slope,o.machine_shadow[i]+1e-8)

    def test_scope_nesting_and_paid_accounts(self):
        flex,_ = decisions(self.base)
        local,_ = decisions(self.base,scope="local")
        freeze,_ = decisions(self.base,source="none")
        for p,l,f in zip(flex,local,freeze):
            self.assertAlmostEqual(p.value,p.account.sum())
            self.assertGreaterEqual(p.value+1e-9,l.value)
            self.assertGreaterEqual(l.value+1e-9,f.value)

    def test_delays_and_duplicate_evidence(self):
        late = Economy(self.world,"late_release")
        for k in OPTIONS:
            self.assertEqual(late.policy(k).value,late.policy(k,source_option="none").value)
        op = self.base.operating(0,ZERO)
        independent = self.base.chance(op)
        copies = Economy(self.world,"duplicate_logs").chance(op)
        np.testing.assert_allclose(1-independent,(1-copies)**4)
        restricted = Economy(self.world,"selective_retention").chance(op)
        np.testing.assert_allclose(restricted[[0,2]],independent[[0,2]])
        self.assertTrue(np.all(restricted[[1,3]]<=independent[[1,3]]))

    def test_cross_dock_preserves_embodied_supplier_content(self):
        for regime in ("baseline","standardization"):
            direct = Economy(self.world,regime)
            dock = Economy(self.world,regime,"cross_dock")
            np.testing.assert_allclose(direct.require[1][:2,3],dock.require[1][:2,3])
            self.assertAlmostEqual(dock.require[1][2,3]-direct.require[1][2,3],.45)

    def test_two_terms_exhaust_propagation_even_across_routes(self):
        changed = Economy(self.world,"standardization","cross_dock")
        result = transmission(self.base,changed,"standardization")
        np.testing.assert_allclose(result["induced"]+result["engineering"],result["gross"],atol=1e-9)
        self.assertAlmostEqual(result["net"],sum(result["incidence"]))
        changed = Economy(self.world,"labor_remix")
        limits = []
        solve = model.linprog
        def capture(*args, **kwargs):
            limits.append(kwargs["b_ub"][:3].copy())
            return solve(*args, **kwargs)
        with patch("model.linprog",side_effect=capture):
            Economy(self.world).operating(1,ZERO)
            changed.operating(1,ZERO)
        self.assertAlmostEqual(limits[0]@WAGES,limits[1]@WAGES)
        self.assertLess(limits[1][1],limits[0][1])

    def test_target_reference_and_price_bounds(self):
        delta = margins(self.world)
        self.assertGreaterEqual(delta[0],-1e-8)
        self.assertLessEqual(delta[1],1e-8)
        self.assertAlmostEqual(diagnostic_value(delta,.5,.5),0.)
        self.assertLessEqual(diagnostic_value(delta,.5,.9),diagnostic_value(delta,.5,1.)+1e-9)
        self.assertAlmostEqual(archive_share(1.),.45)
        self.assertLess(archive_share(.1),.45)
        self.assertGreater(archive_share(4.),.45)


if __name__=="__main__":
    unittest.main()
