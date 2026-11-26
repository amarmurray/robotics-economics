# Whole-game equilibrium regions in a common hardware price

## Result and scope

This extends the accepted four-block game at input commit 90adeff078811aab2ef02885d432a5cfc47c50e2. The common mobile-kit price now varies at every date and in every continuation, rather than at one selected subgame. Two complete behavioral equilibrium profiles have exact eligibility intervals. The exclusive profile includes nine intermediate mixed subgames.

The calendar is (1,1,5,5), with ten later operating shifts, two firms, three human and five compute units per shift, digital-market admission at date three, initial cash 10,000 per firm, and procedure cap two. All figures are synthetic model units. Hardware ordering and assembly, ordinary learning, internal successor development, costly outside substitutes, evidence retention, and lab scope remain in the accepted menus. The difference between regimes is whether research and hardware investment can occur concurrently, still subject to their common resource constraints.

| Complete seed profile | Exclusive investment | Concurrent investment |
| --- | ---: | ---: |
| Common kit-price interval, inclusive | [0,8] | [0,6] |
| Canonical continuation states | 3,898 | 13,025 |
| Reduced joint profiles evaluated at seed | 1,108,797 | 6,431,973 |
| Original retained-menu incentive inequalities | 114,578 | 479,768 |
| Intermediate mixed subgames | 9 | 0 |
| Generated wealth per firm at price 4 | 160 | 163.625 |
| Generated wealth per firm throughout interval | 164 − κ | 167.625 − κ |
| Accepted jobs | 44 | 42 |
| Customer surplus | 88 | 84 |

These are complete-profile equilibrium certificates, not just accounting sensitivities. Each listed strategy remains individually optimal against the rival's complete strategy throughout its interval. All relevant off-path continuations are included. This establishes an equilibrium branch's existence; it does not enumerate every equilibrium or show that a particular selection rule continues to choose that branch.

On the common interval [0,6], the certified concurrent branch has 7.25 more combined private wealth, two fewer accepted jobs, and four less customer surplus. Both profiles order one mobile kit per firm, so this private difference is constant in κ. This comparison does not measure total social welfare: input suppliers, factor owners, financing and entry are not yet fully closed.

Evidence: [solver](dynamic_kit_certificate.js) and [exact results](dynamic_kit_certificate_results.json). The antecedent mixed solution is documented in [MIXED_CONTINUATION.md](MIXED_CONTINUATION.md).

## 1. What changes globally

Let κ be the common monetary price of each actual mobile-kit order. Every order, including an off-path order at a later date, pays κ. Assembly does not pay the order price again, and inherited installed hardware is not retrospectively charged. All other primitives remain at the accepted S=10 values.

The seed is κ₀=4. The solver obtains a complete equilibrium there using the accepted higher-total pure-first continuation rule, with a nondegenerate two-by-two mixed fallback when no pure equilibrium exists. We then fix the resulting complete behavioral profile, including every mixed probability, and determine exactly where it continues to satisfy every incentive constraint.

Holding a candidate profile fixed while checking its eligibility is a certification device. Optimality is established by comparisons with every feasible unilateral action and its continuation, not assumed because the candidate was selected at the seed. If a candidate fails, the next step is to solve for a different profile and certify the next region.

The uniform analysis domain is 0≤κ≤500. The accepted funded quotient is valid throughout this domain. Its conservative four-date cash threshold is 1,968, below the initial 10,000; the input guard uses the still more conservative bound 2,004. The existing dated outlay bounds remain valid. This uniform funding condition matters: if a price change made an action unaffordable, the menus and cash quotient would need to be reconsidered.

## 2. Fixed behavioral profiles have affine values

**Proposition.** Consider a finite-horizon stochastic game with finite actions and states, fixed feasible menus and transition probabilities, and per-period rewards affine in a parameter vector θ. Fix a complete behavioral profile σ, including mixed probabilities at every state. Then every continuation value and every one-action deviation value is affine in θ. Its equilibrium eligibility region is the intersection of the parameter domain with finitely many affine inequalities.

**Proof.** Terminal payoffs are affine. Given affine continuation values, a fixed-probability expectation of those values plus an affine immediate payoff is affine. Backward induction proves the assertion for all state-date pairs. For each player, date, state, and feasible action a, impose
\[
V_i^\sigma(t,s;\theta)-Q_i^\sigma(t,s,a;\theta)\ge0.
\]
The finite-horizon one-deviation argument establishes sequential optimality: terminal deviations cannot improve value, and induction then rules out any multi-date deviation. For a mixed strategy, its value is the weighted average of supported actions. If every action value is at most that average, each positively weighted action must equal it. Thus support indifference is included in the inequalities rather than omitted. □

The theorem extends the earlier pure-profile result to fixed behavioral profiles. Mixed probabilities need not remain constant under a general parameter change; if they must adjust, the fixed-profile region can be lower dimensional or a singleton. The present kit-price direction happens to admit intervals while preserving all nine exclusive-game mixes. This is not evidence that common research costs or learning probabilities leave those mixes unchanged.

For a scalar price the region is an interval, possibly empty or a point. With affine primitives and a fixed profile, the multidimensional region is polyhedral. The union of eligible profiles, or the region chosen by a selector, can have a more complicated shape.

## 3. Exact construction

For each retained action the program propagates two integer-scaled quantities:
\[
V_i^\sigma(\kappa_0),\qquad
D_i^\sigma=\frac{\partial V_i^\sigma}{\partial\kappa}.
\]
A unilateral-deviation slack has the form
\[
a+b(\kappa-\kappa_0)\ge0.
\]
The result is the intersection of all such inequalities, including mixed-subgame actions, with [0,500].

The continuation arithmetic retains the antecedent quarter-probability scaling and the additional factors needed for the accepted mixed denominators. Integer safety is asserted for values, slopes and mixture calculations. Bound intersection and endpoint signs use BigInt rational arithmetic. This is a certificate for every real κ in the interval, rather than inference from a numerical grid.

The economically interpretable derivative is
\[
D_i^\sigma(t,s)=-
\mathbb E_\sigma[\text{remaining actual mobile-kit orders by firm }i\mid t,s].
\]
Each firm can order at most one mobile kit, so all unscaled action-value slopes lie in [−1,0]. The implementation asserts that bound. At the root both firms order once, giving slopes (−1,−1). An independently reconstructed forward account reports two total orders.

### Preserving the menu reductions

The original menu retains the least-cost action among actions with identical payoff-relevant output and successor attributes. The certificate asserts that actions merged under this original key have the same mobile-order coefficient. Their relative cost therefore cannot reverse when κ changes.

A later transition-class quotient can merge actions with the same continuation distribution and current quantity. Every action before that later reduction remains in the final deviation check. Thus a changing cheapest representative cannot conceal a profitable deviation.

The seed recursion considers every reduced joint action profile at every reached state. Each distinct successor kernel has a representative, so it reaches continuations following joint deviations as well as unilateral deviations and equilibrium actions. “Every state” here means this complete finite game's root-reachable canonical domain, including off-path states; it does not mean every hypothetical initial condition of a larger economy.

## 4. Endpoint replay and maximality for these profiles

The verification re-evaluates the frozen seed strategies using actual endpoint prices and primitive cash costs. It uses the same accepted technology but does not use derivative propagation to compute endpoint values. Every seed state is explicitly visited, including states that no unilateral root deviation would reach.

| Regime and endpoint | States replayed | Deviations checked | Wealth per firm | Largest deviation gain |
| --- | ---: | ---: | ---: | ---: |
| Exclusive, κ=0 | 3,898 | 114,578 | 164 | 0 |
| Exclusive, κ=8 | 3,898 | 114,578 | 156 | 0 |
| Concurrent, κ=0 | 13,025 | 479,768 | 167.625 | 0 |
| Concurrent, κ=6 | 13,025 | 479,768 | 161.625 | 0 |

At every state, directly recomputed value equals seed value plus its certified price slope times the price change. Forward dated histories also satisfy the cash, hardware, resource and probability-mass accounts. These are independent endpoint calculations within the shared primitive engine, not an independent implementation of the entire economic model.

The upper boundary is genuine for each complete profile. Among the exclusive profile's 44 binding upper constraints is an off-path research deviation with normalized slack
\[
8-\kappa.
\]
Among the concurrent profile's eight binding upper constraints is an off-path training deviation with slack
\[
6-\kappa.
\]
Either slack becomes negative immediately above its boundary. Both bounds are included because zero regret remains an equilibrium condition.

**These are not root adoption cutoffs.** They identify where one part of the complete contingent policy must change. An equilibrium beyond the boundary may retain the same root investment and change only a continuation. Solving adjacent regions is required before reporting an adoption threshold or a selected-equilibrium surface.

The lower endpoint is the nonnegative-price boundary, with additional action ties there. No conclusion is drawn about subsidized negative prices, where the stated domain and some reductions would require a new audit.

## 5. What this closes and leaves open

Closed in this restriction:

- A parameter is changed consistently at every date and every off-path procurement opportunity.
- Mixed continuations are included in a complete-game interval certificate.
- Every retained original-menu deviation is checked.
- Direct endpoint revaluation agrees in all states and with dated accounting.
- The first incentive constraint breaking each profile is identified.

Open:

- Full equilibrium correspondence, including mixed equilibria coexisting with pure equilibria, larger supports and degeneracy.
- Whether the seed continuation selector continues to choose the same equilibrium as κ changes.
- Adjacent equilibrium branches beyond 6 and 8 and their root behavior.
- Common research-cost changes, probability changes and multidimensional surfaces with endogenous mixing.
- Binding finance, within-block decisions, directed rights, latent common uncertainty, endogenous factor prices, supplier capacity and entry.
- Repeated-economy existence, long-run stability, growth or cycles.

The source guard pins all four antecedent JavaScript files. The reproduction command is:

    node papers/integrated_firm/dynamic_kit_certificate.js --reproduce

It recomputes both certificates and four endpoint replays. The individual command accepts an integer seed in [0,500]; this computational restriction on the seed does not discretize the certified parameter interval.

## 6. Next mathematical step

Continue beyond a profile boundary by solving a new equilibrium and retaining its complete continuation information. In parallel, introduce a common research-cost parameter in the primitive menu before reduction. Actions that happened to be equivalent at the seed must only be merged if their entire parameter-dependent rewards and kernels agree over the claimed region.

When a mixed support persists but its probabilities change, solve its indifference equations symbolically, propagate its rational continuation values upstream, and certify probability, determinant, feasibility and deviation conditions together. See [RECURSIVE_PROPAGATION.md](RECURSIVE_PROPAGATION.md) for the general geometry and the event-time and market-closure contracts.
