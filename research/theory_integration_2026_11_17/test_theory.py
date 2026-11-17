"""Adversarial verification, not proofs or empirical calibration.

Includes every 3x3 binary eligibility graph, exact finite lotteries,
independent LP certificates, convexity checks and learning allocation comparators.
"""
import json
import math
import random
import unittest
from fractions import Fraction as F
from itertools import combinations, product
import numpy as np
from scipy.optimize import minimize_scalar
from theory import (Network, chain, expected_gain, leading_order, joint_two,
    learning_allocation, success_probability, homogeneous_probability,
    homogeneous_derivatives, break_even, optimal_total, sequential_success,
    lp_value, common_certificate, network_arrays, results, rational_probability, rational_break_even, adaptive_chain, adaptive_gross)


class NetworkTheoryTests(unittest.TestCase):
    def test_chain_all_proper_bundles_have_zero_gain(self):
        for k in range(1,9):
            n,b,c=chain(k); v=n.table(b,c)
            self.assertTrue(all(x==v[0] for x in v[:-1]))
            self.assertEqual(v[-1]-v[0],1)

    def test_chain_survives_strict_value_perturbations(self):
        n,b,c=chain(4)
        for old_values in ((9,6,3),(F(31,10),F(21,10),F(11,10)),(100,101,102)):
            new=Network(n.capacity,n.demand,tuple(map(F,old_values))+(F(1),))
            v=new.table(b,c)
            self.assertTrue(all(x==sum(old_values) for x in v[:-1]))
            self.assertEqual(v[-1],sum(old_values)+1)

    def test_independent_learning_chain_is_exact_product(self):
        for k in range(1,7):
            n,b,c=chain(k); v=n.table(b,c)
            ps=[F(i+1,i+4) for i in range(k)]
            self.assertEqual(expected_gain(v,ps),math.prod(ps))

    def test_all_512_three_by_three_graphs_monotonicity(self):
        n=Network((1,1,1),(1,1,1),(F(3),F(2),F(1)))
        es=n.edges(); vals=n.table((),es)
        self.assertEqual(len(vals),512)
        comparisons=0
        for mask in range(512):
            for i in range(9):
                if not mask>>i & 1:
                    self.assertGreaterEqual(vals[mask | (1<<i)],vals[mask]); comparisons+=1
        self.assertEqual(comparisons,2304)
        self.assertEqual(vals[-1],6)

    def test_all_19683_disjoint_old_new_partitions_have_valid_critical_order(self):
        n=Network((1,1,1),(1,1,1),(F(3),F(2),F(1)))
        vals=n.table((),n.edges()); count=0
        for statuses in product((0,1,2),repeat=9):
            old=sum(1<<i for i,x in enumerate(statuses) if x==1)
            new=[i for i,x in enumerate(statuses) if x==2]
            # Independent enumeration of subsets that improve old production.
            productive=[]
            for m in range(1<<len(new)):
                added=sum(1<<new[j] for j in range(len(new)) if m>>j&1)
                if vals[old|added] > vals[old]: productive.append((m.bit_count(),m))
            tab=tuple(vals[old|sum(1<<new[j] for j in range(len(new)) if m>>j&1)]
                      for m in range(1<<len(new)))
            order,coeff,masks=leading_order(tab)
            self.assertEqual(order,min((x[0] for x in productive),default=None))
            if masks: self.assertGreater(coeff,0)
            count+=1
        self.assertEqual(count,19683)

    def test_no_submodularity_guarantee(self):
        n,b,c=chain(2); v=n.table(b,c)
        self.assertLess(v[1]+v[2],v[0]+v[3])

    def test_no_supermodularity_guarantee(self):
        n=Network((1,),(1,1),(F(1),F(1)))
        v=n.table((),((0,0),(0,1)))
        self.assertGreater(v[1]+v[2],v[0]+v[3])

    def test_changing_only_demand_changes_return_order(self):
        n,b,c=chain(3)
        self.assertEqual(leading_order(n.table(b,c))[0],3)
        richer=Network(n.capacity,(2,1,1),n.value)
        self.assertEqual(leading_order(richer.table(b,c))[:2],(F(1),F(3)))

    def test_weighted_technical_exponents(self):
        n,b,c=chain(3); v=n.table(b,c)
        self.assertEqual(leading_order(v,[2,3,5],[F(1,2),1,2])[:2],(F(7,2),F(30)))
        self.assertEqual(leading_order(v,[1,0,1])[0],None)

    def test_general_leading_coefficient_not_just_series(self):
        # Value of at least one successful qualification: p1+p2-p1*p2.
        v=(F(0),F(1),F(1),F(1))
        self.assertEqual(leading_order(v,[2,3])[:2],(F(1),F(5)))
        for t in (F(1,100),F(1,1000)):
            self.assertEqual(expected_gain(v,[2*t,3*t]),5*t-6*t*t)

    def test_two_event_dependence_opposite_signs(self):
        n,b,c=chain(2); comp=n.table(b,c)
        sub=(F(0),F(1),F(1),F(1)); p=F(1,5)
        self.assertEqual([joint_two(comp,p,p,q)-comp[0] for q in (F(0),p*p,p)],
                         [F(0),F(1,25),F(1,5)])
        self.assertEqual([joint_two(sub,p,p,q) for q in (F(0),p*p,p)],
                         [F(2,5),F(9,25),F(1,5)])

    def test_invalid_joint_distribution_rejected(self):
        with self.assertRaises(ValueError): joint_two((0,1,1,1),F(1,5),F(1,5),F(1,2))

    def test_qualification_retention_required(self):
        with self.assertRaises(ValueError): leading_order((F(2),F(1)))

    def test_graph_validation(self):
        with self.assertRaises(ValueError): Network((1,),(-1,),(F(2),))
        with self.assertRaises(ValueError): Network((1,),(1,),(F(2),)).solve(((1,0),))
        with self.assertRaises(ValueError): chain(0)


class DualCertificateTests(unittest.TestCase):
    def test_individual_dual_certificates_not_common(self):
        n,b,c=chain(2); A,budget,cost=network_arrays(n,b)
        for added in ((c[0],),(c[1],)):
            N,_,nc=network_arrays(n,added)
            r=common_certificate(A,budget,cost,N,nc)
            self.assertTrue(r['exists']); self.assertEqual(r['new_value'],2)
        N,_,nc=network_arrays(n,c)
        r=common_certificate(A,budget,cost,N,nc)
        self.assertFalse(r['exists']); self.assertEqual(r['new_value'],3)

    def test_120_seeded_graph_certificates_against_exact_allocations(self):
        rng=random.Random(20261117)
        for _ in range(120):
            n=Network(tuple(rng.choice((1,2)) for _ in range(3)),(1,1,1),
                      tuple(F(rng.randint(1,6)) for _ in range(3)))
            old=set(); added=set()
            for e in n.edges():
                status=rng.randrange(3)
                if status==1: old.add(e)
                elif status==2: added.add(e)
            A,b,c=network_arrays(n,old); N,_,nc=network_arrays(n,added)
            r=common_certificate(A,b,c,N,nc)
            self.assertAlmostEqual(r['old_value'],float(n.solve(old)),places=8)
            self.assertAlmostEqual(r['new_value'],float(n.solve(old|added)),places=8)
            self.assertEqual(r['exists'],n.solve(old)==n.solve(old|added))
            if r['exists']:
                y=np.array(r['dual'])
                self.assertLessEqual(abs(b@y-r['old_value']),1e-7)
                self.assertTrue(np.all(np.column_stack((A,N)).T@y>=np.r_[c,nc]-1e-7))

    def test_shared_attention_can_render_new_recipe_worthless(self):
        # One unit scarce attention: old service earns 2; new service earns 1.
        r=common_certificate([[1]],[1],[2],[[1]],[1])
        self.assertTrue(r['exists'])
        # Coordination removes new recipe's scarce input, but gives it a market cap.
        r=common_certificate([[1],[0]],[1,1],[2],[[0],[1]],[1])
        self.assertFalse(r['exists']); self.assertEqual(r['new_value'],3)

    def test_fixed_technology_continuous_capacity_concavity(self):
        rng=np.random.default_rng(71)
        A=rng.uniform(.2,2,(4,7)); c=rng.uniform(1,4,7)
        for _ in range(60):
            b1=rng.uniform(.1,5,4); b2=rng.uniform(.1,5,4); w=rng.uniform()
            lhs=lp_value(A,w*b1+(1-w)*b2,c)
            rhs=w*lp_value(A,b1,c)+(1-w)*lp_value(A,b2,c)
            self.assertGreaterEqual(lhs+1e-8,rhs)

    def test_integer_bundle_limit_of_linear_relaxation(self):
        # Pairwise recipes on three unit resources; LP returns 1.5, integer optimum 1.
        A=[[1,0,1],[1,1,0],[0,1,1]]
        self.assertAlmostEqual(lp_value(A,[1,1,1],[1,1,1]),1.5)
        feasible=[sum(x) for x in product((0,1),repeat=3)
                  if all(sum(a*y for a,y in zip(row,x))<=1 for row in A)]
        self.assertEqual(max(feasible),1)


class LearningTests(unittest.TestCase):
    def test_homogeneous_optimal_allocation(self):
        for k in range(1,7):
            for R in (.01,.3,2,5):
                u=learning_allocation(R,[1]*k)
                self.assertTrue(all(abs(x-R/k)<1e-10 for x in u))
                self.assertAlmostEqual(success_probability(u,[1]*k),homogeneous_probability(R,k),places=12)

    def test_heterogeneous_kkt_and_budget(self):
        a=(.5,1.,2.); z=(2.,0.,0.); R=3
        u=learning_allocation(R,a,z)
        self.assertAlmostEqual(sum(u),R,places=10)
        ds=[aa/math.expm1(aa*(zz+uu)) for aa,zz,uu in zip(a,z,u)]
        active=[d for d,x in zip(ds,u) if x>1e-8]
        self.assertLess(max(active)-min(active),1e-10)
        self.assertLess(u[0],learning_allocation(R,a)[0])

    def test_allocation_against_independent_scalar_optimizer(self):
        for a1,a2,R,z1 in product((.3,1,3),(.5,2),(1,4),(0,2)):
            u=learning_allocation(R,[a1,a2],[z1,0])
            result=minimize_scalar(lambda x:-success_probability((x,R-x),(a1,a2),(z1,0)),
                                   bounds=(0,R),method='bounded',options={'xatol':1e-12})
            exact=success_probability(u,[a1,a2],[z1,0])
            oracle=max(-result.fun,success_probability((0,R),(a1,a2),(z1,0)),
                       success_probability((R,0),(a1,a2),(z1,0)))
            self.assertAlmostEqual(exact,oracle,places=8)

    def test_s_shape_and_inflection(self):
        for k in range(2,8):
            R=k*math.log(k)
            self.assertGreater(homogeneous_derivatives(R/2,k)[1],0)
            self.assertAlmostEqual(homogeneous_derivatives(R,k)[1],0,places=12)
            self.assertLess(homogeneous_derivatives(2*R,k)[1],0)
        self.assertLess(homogeneous_derivatives(1,1)[1],0)

    def test_derivatives_against_finite_differences(self):
        h=1e-4
        for k,R,a in product((1,2,3,5),(.1,1.,5.),(.5,2.)):
            f0=homogeneous_probability(R,k,a); fp=homogeneous_probability(R+h,k,a); fm=homogeneous_probability(R-h,k,a)
            d,dd=homogeneous_derivatives(R,k,a)
            self.assertAlmostEqual(d,(fp-fm)/(2*h),places=6)
            self.assertAlmostEqual(dd,(fp-2*f0+fm)/(h*h),places=5)

    def test_global_break_even_not_local_derivative(self):
        for k in range(2,7):
            v=break_even(k)
            self.assertAlmostEqual(math.expm1(v['x']),k*v['x'],places=10)
            self.assertAlmostEqual(v['reward']*homogeneous_probability(v['effort'],k),v['effort'],places=10)
            self.assertEqual(optimal_total(50,v['reward']*.99,k)['effort'],0)
            self.assertGreater(optimal_total(50,v['reward']*1.01,k)['effort'],0)
            self.assertEqual(homogeneous_derivatives(0,k)[0],0)

    def test_global_total_against_dense_independent_grid(self):
        for k,W,B in product((1,2,3,5),(.5,4.,10.,30.),(.5,3.,8.,15.)):
            r=optimal_total(B,W,k)
            grid=np.linspace(0,B,3001)
            best=max(W*homogeneous_probability(float(x),k)-x for x in grid)
            self.assertGreaterEqual(r['gain']+1e-8,best)
            self.assertLessEqual(r['gain']-best,.002)
            self.assertTrue(0<=r['effort']<=B)

    def test_liquidity_restricts_effort_not_gross_value(self):
        vals=[optimal_total(B,10,3) for B in range(11)]
        self.assertTrue(all(x['gain']<=y['gain']+1e-12 for x,y in zip(vals,vals[1:])))
        self.assertEqual(vals[4]['effort'],0)
        self.assertEqual(vals[5]['effort'],5)
        self.assertGreater(vals[-1]['gain'],0)

    def test_sequential_retention_dominates_precommitted_split(self):
        for k,B in product(range(1,8),(.001,.1,.5,2,5,10)):
            self.assertGreaterEqual(sequential_success(B,k)+1e-14,homogeneous_probability(B,k))

    def test_sequential_preserves_low_budget_order(self):
        B=.001
        for k in range(1,7):
            self.assertAlmostEqual(sequential_success(B,k)/B**k,1/math.factorial(k),delta=.001)
            self.assertAlmostEqual(homogeneous_probability(B,k)/B**k,1/k**k,delta=.001)

    def test_correlated_qualifications_destroy_independent_exponent(self):
        n,b,c=chain(2); v=n.table(b,c)
        p=F(1,100)
        independent=expected_gain(v,(p,p)); shared=joint_two(v,p,p,p)-v[0]
        self.assertEqual(independent,p*p); self.assertEqual(shared,p)

    def test_alternative_concave_response_has_same_local_order(self):
        B=.001
        for k in range(1,7):
            self.assertAlmostEqual(rational_probability(B,k)/B**k,1/k**k,delta=.001)

    def test_alternative_response_break_even_global(self):
        for k in range(2,6):
            r=rational_break_even(k)
            self.assertAlmostEqual(r['reward'],k**(k+1)/(k-1)**(k-1))
            self.assertAlmostEqual(r['reward']*rational_probability(r['effort'],k)-r['effort'],0)
            for R in np.linspace(.001,3*r['effort'],2001):
                self.assertLessEqual(r['reward']*rational_probability(R,k)-R,1e-9)

    def test_alternative_response_changes_numeric_threshold(self):
        self.assertAlmostEqual(rational_break_even(3)['reward'],20.25)
        self.assertLess(break_even(3)['reward'],10)

    def test_adaptive_value_against_independent_bellman_ode(self):
        from scipy.integrate import solve_ivp
        for k,W,a in ((1,3,1),(2,5,1),(3,10,1),(4,9,.7),(3,2,1)):
            def rhs(t,y):
                prev=np.r_[W,y[:-1]]
                return np.maximum(0,a*(prev-y)-1)
            grid=(.5,1,2,4,8)
            z=solve_ivp(rhs,(0,8),np.zeros(k),t_eval=grid,rtol=1e-10,atol=1e-11,max_step=.005)
            for col,B in enumerate(grid):
                self.assertAlmostEqual(adaptive_chain(B,W,k,a)['gain'],z.y[-1,col],delta=2e-7)

    def test_adaptive_cash_reconciliation_and_bounds(self):
        for k,W,a,B in product((1,2,3,4),(2,10,20),(.7,1.5),(.1,1,4,10)):
            r=adaptive_chain(B,W,k,a)
            self.assertAlmostEqual(r['gain'],W*r['success_probability']-r['expected_expenditure'],places=9)
            self.assertTrue(-1e-9<=r['success_probability']<=1+1e-9)
            self.assertTrue(-1e-9<=r['expected_expenditure']<=B+1e-9)

    def test_adaptive_large_budget_limit_and_no_project(self):
        for k in range(1,7):
            self.assertEqual(adaptive_chain(30,k,k)['gain'],0)
            self.assertAlmostEqual(adaptive_chain(80,10,k)['gain'],10-k,places=9)

    def test_adaptive_information_overturns_batch_noninvestment(self):
        self.assertEqual(optimal_total(1,10,3)['gain'],0)
        self.assertGreater(adaptive_chain(1,10,3)['gain'],0)
        self.assertAlmostEqual(adaptive_chain(1,10,3)['start_budget'],.7271641033794616,places=9)
        self.assertAlmostEqual(adaptive_chain(1,10,3)['gain'],.09443223594027295,places=9)

    def test_adaptive_gross_matches_erlang_on_chain(self):
        for k in range(1,5):
            n,b,c=chain(k); vals=n.table(b,c)
            for B in (.1,1,3):
                gain=adaptive_gross(vals,[1]*k,B)-float(vals[0])
                self.assertAlmostEqual(gain,sequential_success(B,k),delta=1e-8)

    def test_adaptive_gross_critical_order_with_heterogeneous_rates(self):
        n,b,c=chain(3); vals=n.table(b,c); B=.02
        gain=adaptive_gross(vals,[.5,1,2],B)-float(vals[0])
        self.assertAlmostEqual(gain/B**3,1/6,delta=.004)
        self.assertLessEqual(gain, float(vals[-1]-vals[0])*sequential_success(B,3,2)+1e-10)

    def test_adaptive_alternative_qualifications_use_competent_policy(self):
        vals=(F(0),F(1),F(1),F(1))
        self.assertAlmostEqual(adaptive_gross(vals,[1,2],1),1-math.exp(-2),delta=1e-8)

    def test_zero_budget_and_bad_learning_inputs(self):
        self.assertEqual(learning_allocation(0,[1,2]),(0,0))
        for args in ((-1,[1]),(1,[0]),(1,[])):
            with self.assertRaises(ValueError): learning_allocation(*args)
        with self.assertRaises(ValueError): break_even(0)

    def test_deterministic_result_regeneration(self):
        self.assertEqual(json.dumps(results(),sort_keys=True),json.dumps(results(),sort_keys=True))


if __name__=='__main__': unittest.main()
