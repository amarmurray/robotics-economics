# When Capabilities Become Production — passive support, target grounding and embodied escape

**18 November 2026. Conditional theory, not field inference or safety certification.** Continuation of [shadow learning and target support](SHADOW_LEARNING_AND_TARGET_SUPPORT.md), not a new research question or an independent paper.

## The unresolved economic choice

The previous chapter established that a rights-cleared, causally isolated read-only copy of B's routine production data can preserve B's accepted orders until A admission. It also showed that those logs cannot by themselves identify A's unsupported target action. The next decision is therefore not simply how much data to accumulate. It is whether to (i) keep receiving production-generated shadow observations, (ii) conduct a *safely approved* target-grounding/validation intervention, or (iii) redesign the embodiment so that an economically valuable, certifiable customer recipe becomes feasible by another route.

This chapter derives a precise limit on what passive observation can decide and distinguishes **learning that changes a policy's physical qualification** from **evidence that reveals which already qualified policy to select**. These can coexist, but they are not the same benefit. In particular, zero identification value does not imply zero technical transfer or zero productive value.

## Common qualified-production environment

Keep the full model of the living manuscript. A configuration Q contains the retained F policy, separately approved competitors S and candidate A, accessible rights-cleared data and physically certified production/recovery recipes. The customer state omega includes the original order registry, demand, prices, captured contribution, dispatch, operators, bottlenecks and end-date. For any approved complete policy a, its horizon contribution is V_a(theta) = sum over accepted orders and dates of captured net contribution, optimized subject to the common physical and organizational constraints, minus costs counted once. The unobserved theta is one persistent transfer/demand/recovery regime. No benchmark percentage is assigned a monetary value.

An acquisition e consists of three separate objects:
- A physical learning/qualification transition T_e from the initial Q into a possibly different Q_e. A production-generated shadow corpus may change what A can learn without telling management *which* regime is present.
- An experiment report Y_e with conditional law P_e(Y | theta, Q_e), available before a downstream admission decision. Passive logs, target-grounded trials and changed-body tests have different report mechanisms and support.
- A resource, delay and rights cost C_e plus an admissibility condition. A target action is considered only when the actual versioned policy/embodiment/operator recovery mechanism has been approved. Reading source data alone is not approval.

For a **pure diagnostic** comparison, hold T_e, the physically approved action menu, original customer horizon and resource state fixed. The only change is report informativeness. Let Aset = {A,S}; both are *assumed already physically approved* in the toy decision problem. Define the fixed-state minimax decision regret

    R*(Y) = min_{decision rule pi(Y)} max_{theta in Theta}
            [max_{a in Aset} V_a(theta) - E_theta V_{pi(Y)}(theta)].

A randomized admission rule is permitted before the same customer-window deadline, and its randomization was already available without another dataset. Regret measures foregone contribution *relative to the best policy in that same world*; it is **not** maximin profits, an actual customer-profit estimate, or a free add-on to V. Pure diagnostic operating cost and foregone orders must be separately included to compare implemented acquisitions; the post-experiment reference and timing must match.

For a real developmental intervention (grounding, retraining or a new body), T_e, admissible menus, qualification and demand may change. Its actual value is obtained by optimizing the original complete-history production objective J(e,pi), subtracting C_e once. The pure information exercise below cannot be copied into J as a second data premium.

## Proposition — persistent unsupported-outcome ambiguity survives arbitrary passive volume

Suppose there are two admissible worlds theta- and theta+ with the *same full law* of F's versioned source histories, original B accepted orders, available passive read-only observations and any already observed control-plane events. Under the fixed-state approved menu, let the incremental advantage of A over competent S be -L in theta- and +H in theta+, where L,H>0. Assume no additional externally justified structural bridge, no A action support, and that collecting additional copies of F data neither changes T_e nor opens a new report channel.

Then no number of such passive F observations improves the minimax regret relative to choosing between A and S with no report. It is exactly

    R_passive = L H / (L + H).

The optimal unconditioned probability of choosing A is p = H/(L+H). A perfect admissible diagnostic that reveals the two worlds before the same decision deadline reduces *decision* regret to zero (before its real costs). This is the familiar two-hypothesis information-limit construction, not a novelty claim.

**Proof.** The distribution of every passive report is identical in the two worlds, so integrating any report-dependent randomized rule gives the same overall probability p of choosing A in both worlds. Regret in theta- is p L and regret in theta+ is (1-p) H. Equalizing the two monotone expressions gives p=H/(L+H) and value L H/(L+H). Repeating a statistically identical report law without a new intervention cannot distinguish the worlds. Conversely, an admissible perfect report permits S only in theta- and A only in theta+. This proves the stated fixed-menu claim, not the existence or safety of such a diagnostic.

**Important scope.** A source record may predict demand, customer mix, dispatch load or other payoff-relevant states and thus have decision value even if it contains no new target action. The proposition requires the *entire report law* to be identical across the two payoff-different worlds. Records can also improve A via T_e (below). Neither possibility is ruled out by a missing target-action label.

## The existing shadow example now yields an exact decision-cost frontier

Re-use, rather than re-parameterize, the previous chapter's illustrative supported/unsupported target strata. A's net normalized captured contribution is

    V_A(x) = 1/20 + (2/5)x,   x in [0,2],

and a competent specialist has V_S=2/5. The retained F adds zero incremental value; S dominates F in this particular conditional exercise. A beats S precisely when the unknown unsupported-stratum mean x exceeds 7/8. Its gain versus S ranges from -7/20 at x=0 to +9/20 at x=2. All these policies are hypothetically and separately physically approved; the numbers are not a robot observation.

If F's passive source law is identical at the two endpoints and supplies no verified restriction on x, the exact minimax regret is 63/320 and the optimal report-independent probability of A admission is 9/16. Because the incremental difference is affine in x and regret is convex in x for any fixed policy, the worst cases over the full interval [0,2] are the endpoints; the binary calculation is also the interval calculation. More routine historical records of the same law do not shrink it.

Now posit **only as a synthetic conditional diagnostic**, before the same deadline, a safely attainable binary target report Z whose error probability is 1/5 in *each* endpoint world. Z=+ indicates the high-A-value endpoint. Let a=P(choose A | Z=+) and b=P(choose A | Z=-). Its regrets are

    r- = (7/20)[a/5 + 4b/5],
    r+ = (9/20)[4(1-a)/5 + (1-b)/5].

The minimax rule is a=1 and b=2/37, giving **63/740**. A simple deterministic rule (a=1,b=0) would have worst regret 9/100, so *some* residual mixing of A after a negative signal improves the asymmetric minimax decision. For exact optimality, use adversarial weight 9/37 on theta- and 28/37 on theta+. The corresponding weighted expected regret has zero slope in b and negative slope in a, hence is minimized at a=1 and equals 63/740. The displayed rule equalizes the world regrets and attains the lower bound.

The synthetic *reduction in minimax decision regret* is

    63/320 - 63/740 = 1323/11840.

It is an upper budget for **total diagnostic cost plus same-horizon service/opportunity loss** only under this fixed-policy regret criterion and a validated report mechanism with these uniform error bounds. It is not an observed willingness to pay for teleoperation or target trials. An experiment that modifies A, uses a scarce operator, displaces B orders, changes customer demand or misses the qualification window must be recomputed from J and cannot inherit this threshold.

## Why passive shadow data may nevertheless be economically valuable

**Constructive counterexample to equating no information with no transfer.** Suppose the source report laws remain identical between the two worlds, but a verified free, optional, rights-cleared shadow-training recipe raises A's *qualified whole-service contribution* by a common delta in both worlds, without disturbing S, F, demand, resources or safety. This is a hypothesis about T_e, not something inferred from the indistinguishable logs. A's new differences from S become delta-L and delta+H. If delta >= L, A weakly dominates S in both worlds despite the passive signal revealing absolutely nothing about theta. At delta=L=7/20 in this example, decision ambiguity disappears by a **physical policy improvement**, not Bayesian learning. With positive training costs or forced retraining the benefit can vanish; when the old policy and dataset remain genuinely optional, menu expansion cannot lower optimized value.

In practice, the delta need not be additive, uniform, positive or even known. A policy can improve a low-level training metric while failing an essential joint customer recipe or violating a recovery limit. The testable object is the controlled source-data -> versioned qualification -> whole accepted-order transition, including time to admission. Passive information and technical learning must not be conflated.

## Grounding and new embodiments act on different support objects

Let E(a,h) denote the set of action/context/recovery and **joint whole-service** events on which the economic qualification of approved policy a with body h depends. A source corpus gives an observation law on its naturally selected support S_F; its sample volume does not expand S_F to a target-body action absent intervention or a separately validated transfer invariance. A safely permitted grounding design may supply new observations S_G with corresponding target action and recovery supervision. A redesigned embodiment h' changes the feasible recipe and therefore E(a,h'), perhaps *bypassing* one unsupported action, but may introduce its own entirely untested interactions.

**Support-cut implication.** If a required event e in E(a,h) remains outside all measured support and its effect can vary across two observationally equivalent worlds while changing the complete accepted-order payoff, then no point certificate for that policy can be derived from those measurements alone. Testing individual component skills is not sufficient when unobserved joint recoveries, bundles, customer demand or dispatch can vary. The statement is conditional on this nonparametric world class: validated physical/action invariances can legitimately shrink it. A changed body or new source mix can instead remove the uncertain dependency, but only after its *new* recipe, acceptance and safety have been measured and certified.

This identifies distinct investments rather than assigning arbitrary fixed transfer coefficients: (1) more source data can improve representation or Q on already covered support; (2) grounding can alter target support and/or Q; (3) a different body can change which qualifications and actions the customer service requires. Their economics depends on the production envelope V, deadlines, common scarce resources, rights and old-policy alternatives. There is no universal dominance ranking, nor an assumed privileged field, human, teleoperation, simulation or synthetic source.

## Alternative assumptions and serious objections

- **Cross-embodiment representation bridges.** A validated invariant mapping can identify or bound target outcomes absent literal target-action overlap. The support obstruction deliberately excludes an unvalidated bridge; it does not deny generalization. Such a bridge requires stress-testing on held-out target bodies and whole service, not trusting perceptual similarity.
- **Dynamic learning.** A target diagnostic can *create* competency and change future customer demand; a shadow corpus can improve Q without resolving theta. Therefore a pure signal-only R* is a component comparison, not the whole project decision. Model the full endogenous history J where these changes occur.
- **Risk criterion.** Minimax regret is not the same as maximin contribution, a posterior-optimal policy under a specified prior, or a hard safety constraint. No probability prior on x is inferred from an interval. A firm's actual preference may rationally choose S throughout even where minimax regret mixes.
- **Network interference.** A trial in one robot or customer order can alter other customers' accepted service, operator capacity and demand. The diagnostic comparison presumes a complete, physically approved, stable whole-network policy and common window; partial robot-level randomization would not justify it.
- **Hard physical constraints.** Learning about a rare unsafe recovery mode cannot license exposure to it. A report accuracy or economic lower bound never substitutes for versioned safety approval and peak-tail recovery feasibility.
- **Observation noise and positive support.** A nominal 1/5 report error measured only on the production controller or pooled customers may be irrelevant to unsupported target strata. The synthetic calculation is falsified by site-specific miscalibration, demand expiry or incomplete policy coverage.

## Prior-art boundary, checked primary sources

This is a synthesis of standard two-hypothesis decision theory, deficiency of off-policy support, optional technology sets and dynamic qualified production. We make **no independent mathematical novelty claim** for the binary minimax calculation or a support-cut counterexample. Farboodi, Koh and Xia, *Data-Driven Automation* (2026, arXiv:2606.10127), already study future data value and complementary aggregation. Sachdeva, Su and Joachims, *Off-policy Bandits with Deficient Support* (2020, arXiv:2006.09438), analyze the overlap failure and alternatives. Yang, Finn and Sadigh, *Data Analogies Enable Efficient Cross-Embodiment Transfer*, arXiv:2603.06450v2, revised 20 March 2026, show that paired morphology analogies can matter more than unstructured volume in controlled learning experiments. Wang, Verghese and Schneider, *Latent Policy Steering*, arXiv:2609.22521, submitted 18 September 2026, report a target-finetuning/world-model approach. These technical papers propose plausible bridge mechanisms; neither their benchmark improvements nor our hypothetical diagnostic error determine customer captured contribution or operator approval.

Primary links: https://arxiv.org/abs/2606.10127 ; https://arxiv.org/abs/2006.09438 ; https://arxiv.org/abs/2603.06450v2 ; https://arxiv.org/abs/2609.22521 . This limited audit does not establish distinctiveness against all economics or robot-learning work.

## Matched economic evidence needed

Before/after intervention, freeze the original customer opportunity census and trace all accepted and displaced orders, prices, fulfillment, recovery peaks, rights, costs, controller and embodiment versions and deadline. Compare retention-only F, F with isolated shadow copy, separately approved A trained with/without that copy, A plus target grounding, redesigned embodiment if approved, and an independently competent specialist S. Register target strata and joint recipe outcomes before looking at post-policy service. Estimate report calibration and qualification transition separately; do not treat a target skill benchmark as V_A. For signal-only identification, demonstrate the report is available **before** the route choice and does not alter B orders or the A/S qualification set. For interventions that change Q or demand, evaluate full J instead of using R*.

There are **no** target controller/control-graph measurements, B-inert architecture audit, qualified target-action trials, field demand panel or physical safety approvals in this repo. The defensible present conclusion is a conditional choice boundary and a testable distinction between developmental and informational data value. Continue the Nov22 integrated manuscript/Models A–B synthesis and the official numerical sector backbone; none of its scientific gates is hereby passed.

**Exact next action:** seek versioned evidence of (i) inert B shadow transport and any verified source-to-Q shift, (ii) safe, customer-stratified A joint-service/report support with consistent original B orders, and (iii) whether an independently qualified new embodiment removes or merely relocates missing support. If these are absent, derive transportable **bounds** on report accuracy/whole-service value from actual approved evidence, not a fabricated target trial or guessed sensor-performance coefficient.