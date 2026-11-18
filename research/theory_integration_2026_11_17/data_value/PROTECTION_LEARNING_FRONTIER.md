# When Capabilities Become Production — preserving customer service can consume learning capacity

**18 November 2026 | private theory continuation, conditional—not a tested robot system.**

## The unresolved question

[The preceding order-loss chapter](AUDITABLE_ORDER_LOSS_BOUNDS.md) shows that a verified bound on lost *complete* customer orders may certify a deployment's contribution even with one connected interference network. Its candidate pinned grounding policy looked attractive **only because** it assumed that isolation preserved the full grounding-induced A service gain. A controller/model, dispatcher, operator, or customer-demand cut may preserve existing B service *and change the source-to-joint-qualification map*, so the A gain must be recomputed. Here the endogenous decision is a joint choice of source/teleoperation/simulation mixture, target grounding, embodiment, and which baseline service promises to protect.

## Definitions and a causal separation lemma

Fix original customer opportunities, a horizon, persistent latent regime θ, baseline qualified full-policy F, and the *safely approved* candidate menu. For each baseline accepted whole-service bundle j in B, let b_j ≥ 0 be its incremental net contribution after all shared costs have been allocated consistently. Separate candidate A service gains from potentially displaced B bundles, additional physical/data costs and residual market effects as in the preceding chapter. All comparisons refer to the *same θ* and an identical pre-action customer opportunity census. No learning-data premium is added after its production effect is included.

**Lemma (conditional pathwise protection).** Suppose, for a proposed protected set P ⊆ B, the entire B_P state—including original order arrivals, prices, contractual acceptance, controller updates, execution, recovery, dispatch, downstream customer substitutions, human-capacity reservations, rights and valid fallbacks—has identical initial state and exogenous disturbances under F and candidate p. Assume all structural transition/output equations for B_P under p equal those under F and have no arguments depending directly or indirectly on any policy-sensitive state outside B_P; all physically reachable candidate histories respect those exclusions. Then by induction on the finite horizon, accepted B_P service and associated captured margins are identical under p and F, so ℓ_pj=0 for j∈P **in each coupled world**, not merely on average.

*Proof.* Equality at t=0 holds by premise. Conditional on equality through t, identical exogenous inputs and unchanged B_P transition functions with no outside arguments imply equality at t+1. The same output/contract/acceptance functional yields identical whole-service and margins; iterate over the horizon. This is elementary structural causal modularity, not a discovery about robotics. It is NOT demonstrated by running an old controller once, checking an access-control flag, or observing that nominal robots are separate.

**Failure case.** Independent controller weights and hardware do not establish the lemma when the customer switches orders to the newly capable A robot, B prices adjust, or a shared operator queue changes recovery. Example: B serves one exogenously available order under F but B customer demand under G is D_B=1−1{A's new offer becomes attractive}; B service disappears under G despite perfect controller isolation. To claim the lemma, one must cut *market and organizational* pathways, not just the learning gradient.

## Joint protection/acquisition frontier

Let P be a verifiably protected subset under an **approved** full policy p(P), including its own data-learning rule, rights, embodiment, trained checkpoint and operator/demand topology. Let a_L(P) lower-bound incremental *accepted A production* under that exact complete policy, c_U(P) bound all incremental real costs and e_U(P) bound residual adverse market effects. Suppose (separately and explicitly) an audited **horizon-wide** loss budget of k complete orders applies to unprotected B\setminus P. Write T_k(U) for the sum of the k largest nonnegative margins in U (fractional final order is an LP relaxation, not literal divisible service).

Then the previous loss accounting yields the conditional robust certificate

L(P)=a_L(P)−c_U(P)−e_U(P)−T_k(B\setminus P).

**Protection-selection identity.** For j∉P, the exact change in this *certificate*, with the same loss-budget k and all changed A/cost/residual effects actually included, is

L(P∪{j})−L(P)
 = [a_L(P∪{j})−a_L(P)]
 −[c_U(P∪{j})−c_U(P)]
 −[e_U(P∪{j})−e_U(P)]
 +[T_k(B\setminus P)−T_k(B\setminus(P\cup\{j\}))].

For integer k, if j is one of the current largest k remaining margins, the final bracket equals b_j−b_(k+1) of the remaining pool (taking b_(k+1)=0 when absent); otherwise it is zero, up to ties. Hence **protecting an important order need not improve the investment guarantee** when it uses controller capacity, validation/operator time or source learning opportunities.

**Complementarity in *certificates*, not automatically in output.** For fixed k and b≥0, the set function W(P)=T_k(B)−T_k(B\setminus P) is monotone **supermodular** in protection P: protecting a lower-margin order may yield no tightening until higher-margin orders are protected. Proof: U↦T_k(U) is the weighted rank function of a uniform matroid, hence submodular; complementing its set argument preserves submodularity and negating it gives supermodularity. Equivalently, the loss-bound reduction from protecting an order weakly grows as other orders become protected. This algebraic complementarity is a property of the *worst-case bound*, **not proof of positive physical interactions, realized new orders, or a novel theorem**. The actual L(P) can be non-supermodular because a(P), c(P), e(P) are endogenous and often discontinuous.

### Exact synthetic reversal

As in the preceding chapter, F's accepted A contribution is 5 and B=(6/5,3/5,1/5), so F=7. Shared G has increment 12/5, incremental cost 2/5, and a *hypothetical verified* k=1 whole-horizon loss budget: its bound is 4/5. Suppose a real protection cut for the high-margin B1 costs 1/5 **and** reduces jointly accepted A production by 7/10 because validation/controller resources are reserved. Its loss bound tightens from 6/5 to 3/5, but its economic certificate falls from 4/5 to 1/2: the 3/5 tightening is dominated by 7/10 forgone A and 1/5 additional cost. This is a constructed counterexample to “protect the most valuable existing order first.” If k is *not* structurally verified, neither number is a real decision bound.

For illustration, let the cost of each independently approved additional protection be κ=(1/5,1/10,1/20) and lost A contribution under those cuts be (7/10,1/10,1/25). Brute-force enumeration across all eight protection subsets finds certificates between 41/100 and 81/100, with the all-protected option narrowly best **in this synthetic cost schedule**; the high-margin B1-only cut lowers the bound. Multiple protections can complement in the *information bound* even when any one protection is privately unattractive. No hardware cost or A learning response here is measured.

## Isolated grounding and the demand-conditioned transfer gap

A completely pinned G^pin policy has zero B loss only if the full separation lemma, including demand and recovery, holds. It need not preserve shared G's A outcome. Denote u the usable A-side physical/validation/teleoperation resource budget, r≥0 the resource quantity ceded to protection, and Z_A the accepted A **captured contribution** over the customer window, with 0≤Z_A≤M. If (i) at fixed u the *full accepted-service outcome distributions* under G and pinned training (including demand and joint qualification, conditional on pre-action stratum d and persistent θ) have total variation at most δ for every (θ,d); (ii) decreasing u by r loses at most Kr in conditional expected A contribution, uniformly in (θ,d); and (iii) common baseline A accounting and cost bounds apply, then

a_L(G^pin) ≥ a_L(G)−Kr−Mδ,

and hence, given pathwise B retention and e_U=0,

L(G^pin) ≥ a_L(G)−Kr−Mδ−c_U(G^pin).

*Derivation.* The difference in expectations of a bounded [0,M] service payoff is at most M times total variation of the **whole relevant outcome law**. Then apply the resource-response bound at pinned training and the triangle inequality, stratum by stratum, before averaging. If a_L is a θ-uniform lower bound, the conclusion is θ-uniform only when these assumptions hold uniformly across θ. A pooled benchmark-skill TV number is **not** δ here, and a population mean bound is **not** a worst-regime certificate.

Taking the old synthetic numbers a_L(G)=12/5 and c_U(G^pin)=3/5, pinned grounding beats a competent specialist with *upper* gain 9/10 only if Kr+Mδ < 9/10. For illustrative r=1/4, K=2 and Mδ=1/5, this gives pinned lower 11/10; with Mδ=2/5 it yields a tie at 9/10. There are **no data** showing such transport bounds hold. A direct safely matched pinned-versus-shared accepted-service trial, when authorized, is better evidence than setting δ=0.

**Discontinuity obstruction.** If a candidate qualifies an entire indivisible service bundle only with u≥1 and gives A gain 12/5 upon qualification but zero otherwise, moving from u=1 to u=99/100 eliminates all A gain. No small universal K supports the earlier threshold. The old optional F remains available ex ante, but sunk spending on unusable forced training can reduce the chosen *net* return. Adding a source dataset for free cannot harm an optimizer with unchanged old options; compelling a controller overwrite or removing access to old data does not satisfy this premise.

## Operational, empirical and paper meaning

The proposal is **not** that every deployment should isolate controllers or that source acquisition is inferior. The choice is jointly (a) which field/recovery/teleoperation/simulation/synthetic/public/pretrained trajectories to acquire or retain; (b) what grounding/embodiment and *joint customer-service qualifications* result; (c) what source reuse is lost through protection/segmentation; and (d) which actual original customer orders and alternative providers are affected. Protecting orders can be economically complementary only in a worst-case bound while resource competition makes protection costly in the actual production function.

Prospective falsifiers: (1) a supposedly sealed baseline bundle's order, price or recovery changes under a safely approved alternative; (2) pinned grounding's **whole-service** A qualification/accepted output falls outside the proposed uniform δ/K envelope; (3) a signed horizon-wide k token rule fails under customer churn or recursive dispatch; (4) the competent specialist dominates measured pinned contribution. Log a failure rather than invent an isolation proof. No field calibration, physical safety approval, signed target architecture or genuine customer-order panel has been obtained.

Prior foundations: structural modularity and interference are not new; see Hudgens and Halloran (2008), https://pmc.ncbi.nlm.nih.gov/articles/PMC2600548/ for partial interference, and the preceding project's structural-coupling chapters. Top-k weighted rank supermodularity under complementation, expectation/TV bounds and LP duality are standard. Data-Driven Automation, https://arxiv.org/abs/2606.10127, already studies future data's effect on production (§5) and complementary aggregation (Appendix B). This chapter gives a falsifiable combined *production–transfer–protection* accounting argument, **not established publication novelty**.

**Exact next empirical/proof question:** Can an actually versioned architecture and customer contract establish a full-horizon structural B cut *including order demand*, and what safely reachable qualification/accepted-service evidence bounds the **lost A transfer from pinning** under the same customer and resource regime? If either is absent, state L(P) as conditional and retain unsupported-policy partial bounds; do not silently copy the shared controller's gains.