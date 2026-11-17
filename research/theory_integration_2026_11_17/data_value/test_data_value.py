"""Scoped checks of the written data-value propositions; not their proofs."""
import json
from math import exp, log1p
from random import Random
import unittest
from data_value import (DataProduction, expected_value, expected_difference,
                        probability, optimal_mix, mix_value, grounding_value, results)


class DataValueTests(unittest.TestCase):
    def test_probability_mass(self):
        for p in ((),(0.0,1.0),(0.1,0.7,0.3),(0.999,0.001)):
            self.assertAlmostEqual(sum(probability(s,p) for s in range(2**len(p))),1.0)

    def test_expected_value_direct_two_capabilities(self):
        p=(0.3,0.8); v=(0.0,2.0,3.0,8.0)
        self.assertAlmostEqual(expected_value(p,v),2*.3*.2+3*.7*.8+8*.3*.8)

    def test_conditional_marginal(self):
        p=(0.3,0.8); v=(0.0,2.0,3.0,8.0)
        self.assertAlmostEqual(expected_difference(p,v,(0,)),.2*2+.8*5)
        self.assertAlmostEqual(expected_difference(p,v,(0,1)),3.0)

    def test_production_complement(self):
        m=DataProduction(((1.,0.),(0.,1.)),(0.,0.),(0.,0.,0.,7.))
        d=m.derivatives((.4,.8))
        self.assertAlmostEqual(d['hessian'][0][1],7*exp(-1.2))
        self.assertGreater(d['hessian'][0][1],0)

    def test_same_capability_exhaustion(self):
        m=DataProduction(((2.,3.),),(0.2,),(0.,4.))
        d=m.derivatives((.4,.8))
        self.assertAlmostEqual(d['hessian'][0][1],-24*exp(-3.4))
        self.assertEqual(d['production_interactions'][0][1],0)

    def test_decomposition_sums_to_hessian(self):
        m=DataProduction(((1.,.2),(.3,1.)),(.1,.2),(0.,2.,0.,8.))
        d=m.derivatives((.4,.8))
        for i in range(2):
            for j in range(2):
                self.assertAlmostEqual(d['hessian'][i][j],d['production_interactions'][i][j]+d['same_capability_exhaustion'][i][j])

    def test_gradient_finite_difference(self):
        rng=Random(19); h=1e-5
        for _ in range(30):
            m=DataProduction(tuple(tuple(rng.random() for _ in range(3)) for _ in range(3)),
                             tuple(rng.random() for _ in range(3)),tuple(10*rng.random() for _ in range(8)))
            x=tuple(.2+rng.random() for _ in range(3)); d=m.derivatives(x)
            for j in range(3):
                plus=list(x); minus=list(x); plus[j]+=h; minus[j]-=h
                empirical=(m.value(tuple(plus))-m.value(tuple(minus)))/(2*h)
                self.assertAlmostEqual(d['gradient'][j],empirical,places=7)

    def test_hessian_independent_difference_of_gradient(self):
        rng=Random(20); h=1e-5
        for _ in range(20):
            m=DataProduction(tuple(tuple(rng.random() for _ in range(2)) for _ in range(3)),
                             (.1,.3,.2),tuple(rng.random()*10 for _ in range(8)))
            x=(.2+rng.random(),.2+rng.random()); d=m.derivatives(x)
            for j in range(2):
                xp=list(x); xm=list(x); xp[j]+=h; xm[j]-=h
                gp=m.derivatives(tuple(xp))['gradient']; gm=m.derivatives(tuple(xm))['gradient']
                for i in range(2):
                    self.assertAlmostEqual(d['hessian'][i][j],(gp[i]-gm[i])/(2*h),places=7)
                    self.assertAlmostEqual(d['hessian'][i][j],d['hessian'][j][i])

    def test_monotone_production_nonnegative_data_value(self):
        rng=Random(27)
        for _ in range(20):
            # Nonnegative independent services plus an all-required service.
            w=[rng.random()*5 for _ in range(4)]
            v=tuple(sum(w[i] for i in range(3) if s&(1<<i))+(w[3] if s==7 else 0) for s in range(8))
            m=DataProduction(((1.,.3),(.4,1.),(.2,.7)),(.1,.2,.3),v)
            self.assertTrue(all(x>=-1e-12 for x in m.derivatives((.4,.8))['gradient']))

    def test_submodular_coverage_has_diminishing_returns(self):
        cover=({0,1},{1,2},{0,2})
        v=tuple(float(len(set().union(*(cover[i] for i in range(3) if s&(1<<i))))) for s in range(8))
        m=DataProduction(((1.,.1),(.3,1.),(.5,.8)),(.1,.2,.3),v)
        for data in ((0.,0.),(.3,.4),(3.,2.)):
            self.assertTrue(all(x<=1e-12 for row in m.derivatives(data)['hessian'] for x in row))
        g0=m.derivatives((.2,.2))['gradient']; g1=m.derivatives((.5,.8))['gradient']
        self.assertTrue(all(a>=b for a,b in zip(g0,g1)))

    def test_no_first_order_value_can_coexist_with_bundle_value(self):
        m=DataProduction(((1.,0.),(0.,1.)),(0.,0.),(0.,0.,0.,5.))
        self.assertEqual(m.derivatives((0.,0.))['gradient'],[0.,0.])
        self.assertGreater(m.value((.3,.3)),0)
        self.assertEqual(m.value((.3,0.)),0)

    def test_exponential_global_optimum_against_grid(self):
        rng=Random(32)
        for _ in range(25):
            r=.2+4*rng.random(); e=.9*rng.random(); u=10*rng.random(); v=.1+10*rng.random()
            ans=optimal_mix(r,e,u,v)
            grid=max(mix_value(i*r/2000,r,e,u,v)['value'] for i in range(2001))
            self.assertGreaterEqual(ans['value']+1e-12,grid)
            self.assertLess(ans['value']-grid,2e-5)

    def test_rational_global_optimum_against_grid(self):
        rng=Random(33)
        for _ in range(25):
            r=.2+4*rng.random(); e=.9*rng.random(); u=10*rng.random(); v=.1+10*rng.random()
            ans=optimal_mix(r,e,u,v,'rational')
            grid=max(mix_value(i*r/2000,r,e,u,v,'rational')['value'] for i in range(2001))
            self.assertGreaterEqual(ans['value']+1e-12,grid)
            self.assertLess(ans['value']-grid,2e-5)

    def test_symmetric_service_requires_balanced_mix(self):
        for kind in ('exponential','rational'):
            self.assertAlmostEqual(optimal_mix(2.,.25,0.,6.,kind)['x'],1.0)

    def test_customer_weights_change_optimal_mix(self):
        for kind in ('exponential','rational'):
            x0=optimal_mix(2.,.25,0.,6.,kind)['x']
            x1=optimal_mix(2.,.25,3.,6.,kind)['x']
            x2=optimal_mix(2.,.25,12.,3.,kind)['x']
            self.assertLess(x0,x1); self.assertLess(x1,x2)

    def test_more_transfer_can_reduce_acquisition_diversity(self):
        rs=[optimal_mix(2.,e,3.,6.) for e in (0.,.25,.5,.75,.9)]
        self.assertTrue(all(a['x']<=b['x'] for a,b in zip(rs,rs[1:])))
        self.assertTrue(all(a['value']<=b['value'] for a,b in zip(rs,rs[1:])))
        self.assertEqual(rs[-1]['x'],2.)

    def test_benchmark_and_economic_objective_disagree(self):
        economic=optimal_mix(2.,.25,12.,3.)
        balanced=mix_value(1.,2.,.25,12.,3.)
        self.assertGreater(economic['value'],balanced['value'])
        self.assertLess(economic['mean_qualification_score'],balanced['mean_qualification_score'])

    def test_mixture_threshold_and_interior_stationarity(self):
        r=2.; e=.25; u=3.; v=6.
        threshold=log1p(u/v)/(1-e)
        self.assertEqual(optimal_mix(threshold/2,e,u,v)['x'],threshold/2)
        ans=optimal_mix(r,e,u,v)
        z1=ans['x']+e*ans['y']; z2=e*ans['x']+ans['y']
        self.assertAlmostEqual((u+v)*exp(-z1),v*exp(-z2))

    def test_complete_transfer_is_indifference_not_concentration(self):
        for kind in ('exponential','rational'):
            vals=[mix_value(x,2.,1.,3.,6.,kind)['value'] for x in (0.,.5,1.,2.)]
            self.assertAlmostEqual(max(vals),min(vals))
            self.assertEqual(optimal_mix(2.,1.,3.,6.,kind)['x'],1.)

    def test_zero_budget_and_rewards(self):
        for kind in ('exponential','rational'):
            self.assertEqual(optimal_mix(0.,.5,1.,1.,kind)['value'],0.)
            self.assertEqual(optimal_mix(2.,.5,0.,0.,kind)['value'],0.)
            self.assertEqual(optimal_mix(2.,.5,2.,0.,kind)['x'],2.)

    def test_technical_grounding_interaction_changes_sign(self):
        self.assertGreater(grounding_value(.5,.5)['mixed_derivative'],0)
        self.assertLess(grounding_value(2.,1.)['mixed_derivative'],0)
        self.assertEqual(grounding_value(1.,0.)['value'],0)

    def test_marginal_qualification_scores_do_not_identify_value(self):
        # Same two 0.5 marginals, distinct joint state distributions.
        distributions=((.25,.25,.25,.25),(.5,0.,0.,.5),(0.,.5,.5,0.))
        vals=[]
        for dist in distributions:
            self.assertEqual(dist[1]+dist[3],.5); self.assertEqual(dist[2]+dist[3],.5)
            vals.append(dist[3])
        self.assertEqual(vals,[.25,.5,0.])

    def test_invalid_arguments(self):
        with self.assertRaises(ValueError): DataProduction(((-1.,),),(0.,),(0.,1.))
        with self.assertRaises(ValueError): expected_value((1.2,),(0.,1.))
        with self.assertRaises(ValueError): optimal_mix(-1.,.2,1.,1.)
        with self.assertRaises(ValueError): mix_value(3.,2.,.2,1.,1.)
        with self.assertRaises(ValueError): grounding_value(-1.,2.)

    def test_reproducible_results(self):
        self.assertEqual(json.dumps(results(),sort_keys=True),json.dumps(results(),sort_keys=True))


if __name__ == '__main__':
    unittest.main()
