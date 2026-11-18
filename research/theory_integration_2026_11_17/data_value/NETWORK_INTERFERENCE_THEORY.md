# When Capabilities Become Production — network interference, transferable learning and shared operator safety

**18 November 2026 · private continuing research; conditional mathematics, not robot-field evidence.** Companion to [SAFE_POOL_FACTORIAL_THEORY.md](SAFE_POOL_FACTORIAL_THEORY.md), [NETWORK_INTERFERENCE_PROOF_LEDGER.md](NETWORK_INTERFERENCE_PROOF_LEDGER.md), [NETWORK_INTERFERENCE_EMPIRICAL.md](NETWORK_INTERFERENCE_EMPIRICAL.md), and the [exact model](network_interference.js). This is the same source → qualification → accepted customer production → subsequent learning argument, now challenging its *independent-controller-pool* assumption. No new data premium, industry calibration or independent novelty claim.

## The next unresolved issue, not a newly numbered research program

The preceding full-pool randomization argument identifies an approved controller-pool's mean economic value if pools are independent. But controller weights, human recovery teams and customer order flows can join pools that organizational records treat as separate. A nominally isolated intervention may change another site's future data, service qualification, order mix, or ability to recover safely. **When can a measured single-pool route advantage license selective network deployment, and what must be observed if it cannot?**

Use the established state: qualified hardware/controller/retained-policy state Q, customer opportunities and capture omega, optimized accepted-service value V(Q;omega), and complete policy payoff J(pi)=actual current accepted-service contribution minus acquisition/validation/physical/organizational cost plus terminal V on a *nonoverlapping* terminal production horizon. Data affect the reachable Q, reports, production and new order opportunities; they are not separately monetized a second time. Embodiment redesign and qualified specialist remain genuine alternative histories. Each training source (routine field, failures, recovery, teleoperation, simulation, synthetic, public) has different rights, content and generated-state support; none is presumed equivalent.

### Three distinct interference networks

On pools i=1,...,n, let A_i name the complete learning/deployment policy in pool i. **Controller network C** joins pools that share trainable checkpoints, replay buffers or deployed version updates. **Operator network O** joins pools that can simultaneously draw from a common human rescue, validation or supervisory budget. **Market/production network M** joins pools serving substitutable or jointly required customers, material capacity or upstream/downstream accepted recipes. They need not have the same edges, and no scalar "interference coefficient" is presumed sufficient. An end market can have zero controller linkage but strong order competition; two robot sites can share weights without competing for orders.

Define the feasible *network* policy menu F_N by complete timelines, physical/organizational capacity, approved abort paths, rights, and available old versions. The potential complete history Y_N(a) is the total net captured accepted production of network action vector a, including future changes in customer orders (zeros retained), recovered failures and the continuation term once. For attribution only, separately record frozen-order held-out qualification Q^hold(a) and endogenous orders O^market(a). Optimizing only robot success rates cannot recover Y_N.

An exposure summary e_i(a)= (e_i^C,e_i^O,e_i^M) is sufficient only if changing the other pools' full actions while keeping (A_i,e_i) identical leaves pool i's entire potential history unchanged. Weighted neighbor counts, a graph-distance truncation and a learned graph are hypotheses requiring tests. Controller merges and operator queues can propagate beyond immediate neighbors; approximation error cannot be treated as zero by default.

## Result: safe whole-network policy identification versus isolated-pool averages

**Proposition N1 (finite design identification; standard interference estimand).** Suppose eligible networks, not nominal pools, are independent experimental units under fixed complete capture/qualification definitions. Before assignment define demand stratum d, the safely permitted complete vectors F_N(d), and a pre-action registry including every possible no-order customer. For every approved vector a under comparison, known assignment probabilities p_k(a|d)>0 are used to randomize the *entire* network k. There is consistency and no relevant interference across distinct network units. Then the network policy's stratum-specific finite-population mean is design-identified by

\[
\widehat \mu_d(a)=\frac{1}{K_d}\sum_{k:D_k=d}\frac{{\bf1}\{A_k=a\}Y_k}{p_k(a\mid d)}.
\tag{N1}
\]

Conditioning on observed post-deployment customers or intervened sites is not part of the estimand. The randomized mean includes own service, external site service and demand adaptation. Its result is not an individual paired potential outcome, latent regime identification, transferable site effect, or an authorization for an unapproved vector. Proof: conditional on complete potential outcomes, expectation of each indicator divided by its known probability is one; sum and divide. If two "networks" share a future controller checkpoint or recovery queue, the independence premise is wrong; merge them or give an explicitly partial/approximate interference model.

**Proposition N1b (sequential extension under restricted support).** Let a whole network's history H_t contain the pre-action registry, observed orders including zero, safety resources, controller lineage and earlier reports. An independently preapproved sequential behavior design assigns full-network action A_t with probability p_t(A_t|H_t)>0 whenever a target stochastic policy pi_t(A_t|H_t)>0. With sequential conditional randomization, complete measured histories, consistency, a common feasible history tree and no unmeasured between-network influence, the identity

\[
{\mathbb E}_p[Y(H_T)\prod_{t=0}^{T} \frac{\pi_t(A_t\mid H_t)}{p_t(A_t\mid H_t)}]
={\mathbb E}_{\pi}[Y(H_T)]
\tag{N2}
\]

follows by iterated expectation (or path probability cancellation). This is *off-policy identification* of an approved full-history target rule, not validation of safety from logged averages. A target policy choosing a recovery/embodiment route never supported under the behavior policy is unidentified by N2. If the target changes future possible states outside the observed support, positivity fails. A hidden persistent regime is not required to be labeled for the randomized **mean**, but robust regime-conditional individual policy contrasts do not follow from this identity.

## Result: an exact bounded-spillover correction to the earlier 70/30 selective certificate

The earlier safe-pool experiment had observed approved A-segment mixing gain g=0.5 over retained old-controller production 7, pre-action weights w_A=0.7 and w_B=0.3, and unchanged B fallback. It yielded 7.35 before genuine incremental segmentation costs. That conclusion requires A deployment to leave B opportunity, qualification and capacity unchanged.

Define s as the net *per-B-eligible-unit contribution loss* when approved A mixing is rolled out in the actual coupled network, relative to B's fallback history. s includes controller interference, downstream order diversion and dispatch externalities; s<0 is a productive spillover. Preserve the measured own-A g only under an explicitly matched customer/physical population and controller recipe. Let c be all additional network rollout costs in the same total per-pool normalized units (no double counting).

**Proposition N3 (conditional selective value interval).** Under a stable pre-action composition and complete-network accounting,

\[
J_{A{\rm -mix}, B{\rm -old}}-J_{\rm old}
= w_A g-w_B s-c.
\tag{N3}
\]

If a justified externality identification set is s in [s_L,s_U], the sharp difference interval under *only those constraints* is [w_A g-w_B s_U-c, w_A g-w_B s_L-c]. A strict worst-case selective advantage exists iff w_A g>w_B s_U+c. For g=0.5, w_A=.7, w_B=.3, c=0 and s in [-.4,1.5], the allowed target contribution is [6.9,7.47]; the 7.35 claim is **not** robust. Selective mixing dominates the old seven-unit route exactly when s<7/6 at c=0; for nonzero c the bound is s<(0.35-c)/0.3. Endpoints are attained by networks with B's net customer response constant at the stipulated extrema, while all isolated A observations remain identical. This is a sensitivity identity with explicit sharpness class, not a robotics-estimated externality.

The same sign ambiguity can arise from very different physical mechanisms. B can lose 0.6 because controller sharing damages whole-service qualification at fixed orders; or B can gain 0.2 in held-out qualification while losing 0.8 in realized orders owing to substitution, again totaling -0.6. Identical Y_B and aggregate network contribution cannot identify controller negative transfer as the cause. A matched **shared-versus-isolated checkpoint** experiment plus frozen-demand held-out complete recipe acceptance and independent original-order registry is necessary to separate these accounts. If isolation itself costs k, its causal net advantage is avoided controller-related harm less k, not avoidance of demand diversion; isolation can reduce positive learned-controller spillovers.

This transports only when w_A and w_B are pre-action target weights for *the true connected market/controller network*. Once rollout changes the pre-action eligibility process, recruits customers across markets, or changes support at other sites, the weighted formula is insufficient: use a complete network transition for demand and data acquisition. Ordinary site-level regression conditioned on *orders received after deployment* can create post-treatment selection bias and reverse the observed sign.

## Result: pathwise shared capacity and jointly possible tails

Let R_i(t,h,a) be resources required by pool i at calendar time t under **supported global history** h, including human failure recovery, audits, requalification and remote operation. A strict physical operator constraint requires

\[
\sup_{h\in{\rm supp}(a)} \sup_t\sum_i R_i(t,h,a) \le B_t
\quad\text{with the capacity at each t evaluated against its own B_t.}
\tag{N4}
\]

Equivalently, for every supported history and every time t, sum_i R_i(t,h,a) <= B_t. An optional certified abort can change the actual reachable support and must be encoded in the tested action and service-acceptance rule. Separate per-pool certificates R_i<=B_t are **not compositional**: the same finite operator may be required simultaneously.

**Proposition N4 (matching marginals, opposite feasibility).** Two independently individually approved R routes each require exactly one operator in a rare recovery with marginal probability 0.1. The shared instantaneous budget is B=1. World I permits simultaneous recovery with positive probability (e.g. independent recovery flags: P(both)=0.01); attempting R at both sites is inadmissible because a supported path uses two. World II has disjoint recovery events, P(both)=0, so the same two routes satisfy this particular peak constraint, assuming all other route, cumulative, latency and rights constraints are approved. The two worlds have identical per-pool recovery frequency and mean loads of 0.1. Thus no marginal failure rate, expected operator use or separately granted safety label proves network feasibility. The counterexample is about *support and scheduling*, not empirical evidence that any route is safe.

A conservative sufficient certificate is sum_i sup_h R_i(t,h,a)<=B_t at every t, but it may reject a truly safe negatively correlated joint recovery law. For exact necessity use the support of the verified joint process, accounting for possible overlapping time windows. In incomplete observation, a single unsupported high-risk joint path cannot be declared impossible from its absence in a limited trial; a bounded-risk policy would require a separately specified acceptable tail criterion rather than treating expectation as a hard certificate.

## Implications, identification limits and empirical discriminators

The independent controller-pool representation of Models A/B is recovered when C, O and M have no edges (or are experimentally neutral under the policy), action support factorizes safely, and operating contribution is additive under actual qualified service. With edges, the first paper needs an optimized network recipe/qualification value, not a fixed per-dataset return, and Model B's cash/expansion calendar must use actual joint service and human capacity. This does not imply integration always wins: independent controllers at sufficiently low cost can restore additivity. A competent specialist can dominate every data-acquisition route when it safely serves the demanded complete bundle.

**Empirical priority:** map the union of controller/rights, operator/dispatch and commercial demand ties *before* choosing randomization units; record both direct and spillover accepted-service outcomes and zero orders for the whole reachable market; compare isolated and shared checkpoint lineages under equivalent resources; record pathwise joint operator peaks rather than only average teleop time. [The measurement protocol](NETWORK_INTERFERENCE_EMPIRICAL.md) specifies a minimum linked dataset and negative controls. Multi-stage source qualification must still distinguish production-generated field failures from deliberate target grounding, teleoperation, simulation, synthetic and public/pretrained interventions.

**Closest prior art and limits (metadata/abstracts checked November 18):** Hudgens and Halloran, *JASA* 103 (2008), 832–842 (https://pubmed.ncbi.nlm.nih.gov/19081744/); Aronow and Samii, *Annals of Applied Statistics* 11 (2017), 1912–1947, DOI 10.1214/16-AOAS1005 (https://isps.yale.edu/resource/estimating-average-causal-effects-under-general-interference-with-application-to-a-social); and Leung, *Econometrica* 90 (2022), 267–293, DOI 10.3982/ECTA17841 (https://onlinelibrary.wiley.com/doi/abs/10.3982/ECTA17841). Interference-aware randomization, exposure mappings and approximate-neighborhood theory already exist. The proposed contribution is the **economically and physically specific composition** with whole accepted customer services, shared learned controller and operator budgets; neither general causal inference nor this economic composition has been independently established as new. No customer acceptance panel, linked sector numeric backbone, independent review, historical CI or physical safety signoff exists.

**Exact next gap:** establish whether an *approximate*, rather than zero, interference radius plus measured/justified residual effects suffices to certify a demand- and recovery-feasible policy difference, while preserving one persistent transfer regime and actual coupled opportunity transitions. The November 22 scientific synthesis is pending; December 25 at 23:59 Eastern is unchanged.
