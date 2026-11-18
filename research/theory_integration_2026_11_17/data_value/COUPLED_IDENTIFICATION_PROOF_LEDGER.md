# Proof ledger — coupled identified complete histories and robust data-value

**18 November 2026. Companion:** [COUPLED_IDENTIFICATION_AND_AUDIT.md](COUPLED_IDENTIFICATION_AND_AUDIT.md). This is a conditional derivation under an explicitly specified finite response-type relaxation, not a new universal policy-learning theorem.

## Proposition 1: fixed-policy sharp identified interval and dual

Assume \(q\ge0\), \(1^\top q=1\), \(Aq=b\) nonempty; each type specifies all potential full histories for each feasible complete policy, including customer orders and future learning. Fixed precommitted history-policy \(\pi\) has a definite \(v_{\pi k}\), so \(J_\pi(q)=v_\pi^\top q\). The minimum same-law pairwise difference is the finite LP with coefficients \(d=v_\pi-v_\sigma\). Standard finite-dimensional LP strong duality gives \(\max_{\lambda_0,\lambda}[\lambda_0+\lambda^\top b]\) subject to \(\lambda_0+A_{\cdot k}^\top\lambda\le d_k\). Upper endpoints reverse the objective. A maximin optimizer over \(\pi\) is a **separate** outer maximization; the minimum difference of separate policy lower bounds is not the paired lower bound.

**Limits:** if one imposes nonlinear conditional independence, products of kernels, capacity spillovers or a structural cross-site invariant, the polytope may admit nonexistent structural worlds. It remains an *outer* set; linear sharpness does not establish sharpness for the narrower nonlinear physical model. A randomized experiment that identifies two route mean outcomes identifies their **mean difference** without observing joint unit-level counterfactuals under proper consistency and overlap. One must not call the cross-policy dependence itself empirically essential absent a specific partial-information restriction.

## Proposition 2: support robust policy constraint

Let \(S=\{k:\exists q\in{\cal Q},q_k>0\}\). For hard pathwise budget B, if a policy attempts a resource-consuming action after some reachable history on type \(k\in S\) requiring more than its **remaining** B without authorized preattempt fallback, there exists an admissible positive-probability violation; therefore it cannot be uniformly feasible. Conversely if every *attempted* supported history fits the budget and an approved fallback exists for all deferred actions, the policy meets the specified finite-model hard cap. This is model support feasibility only, never physical-world safety certification. With an additional risk budget \(\epsilon\), a different chance-constrained set could be optimized, but no such relaxation is made here.

A population with probability 0.9999 of peak recovery 1 and 0.0001 of peak 3 has mean 1.0002 below cap 2, yet fails hard pathwise feasibility if the action is attempted on the peak-3 path. Finite zero counts cannot logically prove that peak-3 support is absent.

## Proposition 3: joint dependence changes economic ranking

With \(P(H)=P(D)=1/2\), the feasible \(2\times2\) masses are \((t,.5-t,.5-t,t)\) by marginal equalities and nonnegativity: \(t\in[0,.5]\), both endpoints attainable. The synthetic response-type values give \(R=5+8t\), \(G=8-2t\), \(E=6\), \(S=5\). Thus \(R-G=-3+10t\) and the sharp range is [-3,2]. A dual lower witness has \(\lambda_0=-2,\lambda_H=0,\lambda_D=-2\); evaluate \(-2-2D\le v_R-v_G\) typewise: (-4,-2,-4,-2) versus (6,-2,-4,-2). Taking expectations gives -3, attained at t=0. The upper 2 is attained at t=.5. If a valid moment narrows t to [l,u], the exact pairwise bounds are [10l-3,10u-3]; no probabilistic independence is implicit.

## Proposition 4: maximin and minimax regret routes differ

A fractional x allocation to R has value \(8-3x+(10x-2)t\). At x=.2 this is 7.4 for every t. At t=.3 every route is worth at most 7.4, certifying global maximin optimality among convex mixtures of R/G/E/S. For x<=.2, the minimum is at t=.5 and equals \(7+2x\), increasing; for x>=.2 it is at t=0 and equals \(8-3x\), decreasing. Thus unique R/G maximin x=.2.

For type-parameter regret, G is best for t<=.3, R for t>=.3, and E/S are never best. The worst regret of x is \(\max[3x,\,2(1-x)]\), minimized at x=.4 to 1.2. Its worst production 6.8 is lower than the maximin 7.4; conversely the maximin hedge's largest regret is 1.6. The choice of criterion is not identified by the robotics data.

## Proposition 5: perfect population audit can have zero maximin incremental value

Suppose before allocating across a population, an oracle reveals *only t*, not the per-pool H regime, while leaving production/safety/rights unchanged. Its worst attainable value is \(\min_{t\in[0,.5]}\max\{5+8t,8-2t,6,5\}=7.4\) at t=.3. The unrestricted fractional maximin pre-audit guarantee was already 7.4; the incremental maximin value is exactly zero. With only pure indivisible action, best initial robust G guarantee is 7 and oracle worst guarantee is 7.4, giving gross benefit 0.4. This uses ordinary minimax convexification. It does **not** imply any diagnostic reporting *individual* H, changing Q, relaxing safe capacity, or serving a Bayesian objective has zero value.

## Proposition 6: calibrated diagnostic inverts joint event, subject to strong bridge

If \(D\) is a pre-action binary customer class with P(D)=.5, and an approved diagnostic Z has sensitivity s and false-positive probability f **independent of D within each H class**, then
\(m=P(Z=1,D=1)=s\,t+f(.5-t)=.5f+(s-f)t\).
For s>f, t=(m-.5f)/(s-f). With .9/.1 and m in [.34,.4], t is [.3625,.4375], so the R-G paired lower is .625. A proof of the inversion requires independent calibration across D **and** the proper H interpretation; observing Z alone cannot validate it. If signal quality depends on D or H proxies depend on policy, this is not identified. A validated diagnostic must also pass Proposition 2 before any real experiment.

## Checks and status

Exact reproducible JS source: [coupled_identification_audit.js](coupled_identification_audit.js); serialized synthetic [results](coupled_identification_audit_results.json). 1126 scoped deterministic assertions were executed on the exact source text in connected V8, including full t/x grid, equality/marginal constraints, four-type LP dual witness, both robust criteria, measurement inversion and a rare unsafe tail. Independent rational checks in Python Fraction confirmed end points, 7.4 equalization, R−G .6 at t=.36 and the zero-information minimax equality. Grid checks are **not** mathematical proofs; proofs are the algebra above. Historical repository CI, node clean replay, independent peer review, robot field observation, customer-priced accepted service and official quantitative backbone were **not** conducted.