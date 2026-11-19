# Dynamic-source exposure: proof ledger and rejected statements
**19 November 2026.** Continue the [integrated theoretical chapter](DYNAMIC_EXPOSURE_PRODUCTION.md). Conditional finite Markov coupling and standard network interference mathematics; not calibrated field science.

## P1. Recursive coupling with joint qualification permitted

Let two policy vectors z,z' differ at assignment j. Their initial state distributions agree on a pre-policy cohort; if they do not, include initial TV discrepancy in U_0. Conditional transition laws across correctly grouped state blocks factor as product kernels. At any time t, couple the two block-k updates maximally for their conditionally given input histories. The two whole next-state marginals are the required conditional products. By TV triangle inequality (first replace policy j at unchanged input, then change prior state coordinates one at a time), the conditional disagreement probability is at most \(b_{kj,t}+\sum_l A_{kl,t}1\{S_{lt}\ne S'_{lt}\}\), capped at one. Hence \(q_{k,t+1}\le\min(1,b_{kj,t}+\sum_l A_{kl,t}q_{l,t})\). Nonnegative A and induction prove q<=U as in (D2). This uses no independence of terminal qualifications, because all blocks can depend on the same earlier shared state.

Under a uniform pathwise payoff bounded-difference \(d+\sum L 1\{\text{state blocks differ}\}\), take expectation to prove (D3). Costs attributable only to changed assignment j may affect W_i directly and must enter d. If the operating payoff jumps discontinuously at a tight shared capacity threshold, a *correct* L may approach its maximum customer-order span: no continuity is assumed by the theorem.

## P2. Transporting the dynamic certificate to the market estimand

For fixed i, own action a, use the coordinatewise bound (D3) to telescope other assignments to all a. With independent site-assignment probability p, each other j mismatches the all-1 vector with probability 1-p, and all-0 with p. Sum i, j and divide by N. This is prior (I9) with dynamic epsilon, independent of whether rewards or terminal qualifications are correlated. If a randomized assignment is not supported for the global target (e.g. unsafe all-X model broadcast), the algebra defines a potential-value sensitivity comparison but cannot license that deployment.

## P3. Fully joint kernel, weaker but dependency-robust

If the next-state *joint* kernels admit uniform \(\mathrm{TV}(K^z_t(\cdot|s),K^{z'}_t(\cdot|s'))\le\beta_{jt}+\alpha_t1\{s\ne s'\}\), maximal coupling of whole states gives \(h_{t+1}\le\min(1,\beta_{jt}+\alpha_t h_t)\) with common initial state. Apply whole-state bounded payoff spans B_it along a coupled history to obtain the coarse bound in (D5). A credible joint-kernel bound cannot be inferred from zero **marginal** TV effects; a shared operator/learner can alter the correlation law while preserving every separate marginal.

## P4. Exact synthetic failure cases

The exact rational [CPU source](dynamic_influence_production.js) and [results](dynamic_influence_production_results.json) calculate b=(1/10,1/5,0), Q/O/D influence matrix with O→D=1/2, and L=(2,1,4). At horizons 1–4 the entire L-weighted exposure is 521/500; deleting that edge yields 273/500, understated by 62/125. If a putative direct per-site X effect were 2/5 and p=1/2 in symmetric two-site policy units with only X cross exposure, the correct market T enclosure [-121/1000,921/1000] includes both signs while the invalid deletion yields [127/1000,673/1000]. The *bound example* is deliberately distinct from the exact payout counterworld below: it does not assert that the chosen influence numbers calibrate the counterworld.

For \(w_i(z_i,z_j)=3+(3/4)z_i-z_i z_j\), complete incumbent/one-X/all-X net values are 6,27/4,11/2. Under half saturation, the randomized own-X direct effect is 1/4; whole-market all-X minus all-G is -1/4 per site. The missing edge can be an operator-mediated date-1/demand-date-2 response; no real mechanism is established by the reduced form. When two joint qualification components are perfectly concordant versus perfectly discordant, their identical Bernoulli(1/2) marginals coexist with complete recipe success rates 1/2 versus 0. This disproves use of coordinate marginal policies as a complete kernel certificate in the absence of factorization or grouping.

## P5. Alternative assumptions and negative results

A product *conditional transition* is not the same as independent unconditional learning. However, there is **no** positive or tight certificate without (i) actual closure; (ii) genuinely bounded joint-kernel effects; or (iii) a justified structural dependency graph with joint common-cause blocks. A simple local positivity assumption does not identify all-X adoption. A negative full-X paid conversion does not lower the optimized value of free optional source information, because the old controller/physical policy is still feasible in the latter comparison. A new embodiment changes service and the law of source learning unless a capacity-only exclusion is independently justified.

**Empirical falsifier:** one approved held-out original-order stratum with operator-mediated buyer demand changes exceeding a prespecified A/O→D limit invalidates the claimed certificate. Unknown support and missing refusals force an uninformative bound; silent deletion of an unmeasured edge is not a permitted shortcut.
