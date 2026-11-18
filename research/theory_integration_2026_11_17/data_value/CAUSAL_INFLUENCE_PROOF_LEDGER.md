# Proof and rejection ledger — conditional causal graph influence and admission

**18 Nov 2026.** Read with [theoretical continuation](CAUSAL_INFLUENCE_AND_ADMISSION_THEORY.md), synthetic [model](causal_influence_admission.js) and [results](causal_influence_admission_results.json).

### C1-to-C2: conditional mismatch induction

Fix a persistent θ and a complete nonanticipatory π from the declared class Π. Couple the initial network states exactly and use shared policy randomness. By assumption C1 there exists one *joint* coupling of next complete states whose i-th mismatch conditional probability is bounded by the nonnegative right side. With \(e_{t,i}=P(X_{t,i}\ne\tilde X_{t,i})\), apply total expectation. The resulting vector inequality \(e_{t+1}\le C_t e_t+b_t\) is entrywise. Because C_t has nonnegative entries, repeated substitution from e0=0 yields \(e_t\le \sum_{s<t}C_{t-1}\cdots C_{s+1}b_s\). Neither statistical independence across customer qualification outcomes nor resetting the latent θ is needed.

For each time-specific captured service contribution r_t and the *single* terminal V, the assumed coordinate bounded-difference inequality gives \(|E r_t(X_t)-E \tilde r_t(\tilde X_t)|\le\delta_t+\sum_i w_{t,i}e_{t,i}\). Summing these finite bounds proves C2. If stage reward is earned on the *next* state, attach its w to t+1, not t. If the optimized V includes joint orders, w is a worst-case **change in total captured production** when one component changes and others stay fixed. For a discrete qualified service bundle this can be large even when single robot success percentages hardly move; additive per-skill prices would be unjustified. Equal-state reward mismatch δ also includes genuine accounting/timing approximation, not a second price for data.

### Policy-uniformity and same-world comparison

Use the componentwise supremum C_t and b_t over all relevant π, persistent θ and admissible histories; then C2 is uniform across Π. If a new embodiment makes a state not covered by this support, the stated Π was wrong and the result does not apply. For each fixed θ, apply the lower error bound to π and the upper error bound to π0, subtract, and minimize over the *same θ*. This proves C3. A positive result proves an economic comparison **conditional on separate pathwise physical admissibility**, not a permission to run π.

### A subtle sufficient condition; marginal site TV is not automatically a joint coupling

If next-node outputs are conditionally independent given a fully expanded complete state including all common latent noises, one may couple each factor with a single-coordinate conditional-TV bound and obtain a product joint coupling satisfying C1. If outputs are coupled through an unrepresented global shock, separately fitted marginal TVs can be zero while the joint downstream event differs. For example, binary \(U,V\) can have identical fair marginals under both kernels, yet in one kernel U=V and in another U=1−V. Their separate marginal TV is zero, but the joint event {U=V} flips probability from one to zero. A downstream customer bundle or recovery queue depending on both requires the joint law. Thus a list of marginal robot/controller effects does not establish C1. Representation must include relevant common shocks or an explicitly validated joint coupling.

### C4 and its restricted meaning

Expand the matrix products in C2: a coordinate error is bounded by a sum of products of conditional influence coefficients over time-respecting paths from an omitted-source shock to that coordinate. If every relevant path has length at least r+1, there are at most d^ℓ paths of length ℓ and every product ≤α^ℓ, then the finite T path contribution is ≤β∑_{ℓ=r+1}^{T}(dα)^ℓ under the one-shot shock assumption. When dα<1, the infinite geometric tail is β(dα)^{r+1}/(1−dα). This is **not** a theorem that every production network has decaying interference. Repeated shocks require summing their individually time-indexed tails; arbitrary global broadcast edges create paths of length one at any geographic separation.

### Exact conditional arithmetic and independence audit

The three-block time sequence has b0_X=.05, C1_BX=.4 (other specified entries zero): e1_X=.05 and e2_B=.02; w_B=.3×10=3, so omitted economic B value bound .06. Unstaged lower difference \(.7(.5)-.3(.6)-.02-.03-.06=.06\); total 7.06, **below** assumed specialist upper 7.08. A serial admission alternative has b0_X=.015, C1_BX=.25, e2_B=.00375 and cost .01125 in aggregate captured production. Its separate lower difference \(.7(.44)-.3(.45)-.02-.045-.01125=.09675\); lower 7.09675, specialist margin .01675. These losses could be jointly attained in the unrestricted additive worst-case construction; physical law constraints may tighten but are not asserted. The specialist comparison requires an actual valid **upper** 7.08 for the true same-regime specialist on the same customer horizon, not an illustrative mean.

For a one-shot β=.05 shock, at most d=2 outgoing relevant paths per step and edge coefficient α=.2, r=1, T=4, the finite remote tail is \(.05(.4^2+.4^3+.4^4)=39/3125=.01248\); the infinite upper is \(1/75=.0133333...\). These are path-disagreement magnitudes, not dollar values or evidence for any chosen d or α in physical robotics.

### Safe admission induction is distinct from statistical guarantees

Assume B=1; every initiated potentially recovery-needing activity holds exactly one exclusive token, no other activity can generate unreserved recovery need, tokens cannot be duplicated, and the verified non-operator-dependent safe-stop action is reached **before** a dangerous state if no token is available. Initially active≤1. For any transition, a new activity starts only if a token is free, and release cannot increase count; therefore active≤1 for every reachable history by induction. The finite toy semaphore exhaustively checks request/release traces, **not** those robotics premises. If a stopped robot can still need a human, if two retained versions act outside the scheduler, or if emergency duties overlap by design, the invariant is false and independent safety review must reject that route.

### Counterexample to a policy-uniform bound from incumbent logs

Incumbent π0 retains local controllers with no remote checkpoint share; in observed π0 histories C_BX=0. Proposed adaptive π makes a globally shared controller after reaching a new target state and induces C_BX=1 on that branch. Both worlds agree perfectly under π0. Any universal bound inferred solely from π0 as C_BX=0 makes a false guarantee about π. Even an arbitrarily long incumbent-only log cannot identify the missing intervention response without architectural restrictions. This is standard unsupported-policy identification, not new scientific novelty.

### Proof classification and unresolved work

C1–C4 are conditional standard mathematical constructions and bounds. The explicit numerical examples are synthetic; exact JavaScript assertions and independent Fraction arithmetic test the numbers, not the hypotheses or causal interpretation. Unknown: genuine engineering sup C/b and w under expanded accepted-service/zero-order states, safe nonhuman abort with hard operator cap, specialist upper bound, nonadditive network ownership impacts, full 2025–35 BLS/BEA numeric production crosswalk, and independent first-paper contribution review. A true joint-kernel diagnostic might yield a tighter result than this worst-case path envelope.
