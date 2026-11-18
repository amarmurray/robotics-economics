# Policy-dependent continuation and the value of partial invariance

**18 November 2026 | Private continuation of *When Capabilities Become Production*.** This directly repairs the exact-equality premise in [the paired first-exit chapter](COMMON_EXIT_VALUE_COMPARISON.md). It is a standard constrained linear optimization result placed inside our complete-customer-service model, **not** an independently novel theorem, an actual robotics measurement, a safety certificate, or a pricing model for datasets.

## The exact intellectual question

Source-copy versus no-copy may change the jointly qualified services, first unsupported target encounter and the network's post-encounter behavior. The previous paired result is informative when the two versions share a common unknown *whole-service* continuation, but controller learning can alter recovery, original B-order displacement, dispatcher and operator behavior after that encounter. Must we abandon comparisons whenever strict invariance fails, or can partially shared responses give a valid intermediate certificate **without pretending source logs identify unseen target outcomes**?

## One economic environment, two policy-specific residuals

Keep the same finite customer opportunity horizon, pre-treatment original-order registry, captured-value measure, complete policy-closed dispatch/operator/controller/customer network, source rights, and qualified policies as the [original manuscript](../THEORY_MANUSCRIPT.md). A policy i may be retained F, no-copy A, rights-cleared offline source-copy A, target-grounded G, changed embodiment H, or competent specialist S. Only **separately approved, jointly qualified complete policies** are admissible for a real comparison. Training, validation, service displacement, acquisition and compute costs are included in the one dynamic production objective J; no future-data premium is added.

For a matched, complete unsupported-history label j, let p_ij be that checkpoint's *own* probability of reaching it first, and K_i its identified no-exit and pre-exit contribution net of counted costs. Labels must include customer and original B-order state, controller lineage, physical/temporal resources, operator, dispatcher, remaining window, and the contract; a shared pose or benchmark ID is insufficient. Let u_ij(theta) be the remaining **whole-network captured contribution** under policy i, in a persistent feasible world theta, after all known policy-specific terms are removed. No assumption of equal unobserved post-exit performance is made.

    J_i(theta) = K_i + sum_j p_ij u_ij(theta).

This reduction requires that K_i and p_ij are identified and fixed over the considered feasible worlds. If latent transfer or demand also changes p or K, optimize their joint feasible set rather than applying the closed form below. Probabilities across exit labels sum to at most one; the missing mass is no exit and already counted in K.

For each j, suppose a **credible independently audited** joint restriction is available:

    l_j <= u_aj, u_bj <= h_j,
    |u_aj - u_bj| <= eta_j <= h_j-l_j.

The first interval is an accepted-service/captured-contribution bound, not a robot performance percentage. The second constrains *cross-policy whole-network economic divergence* after conditioning on the same complete state. Neither can be inferred from similarly named robot states, a logged failure rate or observed source data alone.

## Conditional proposition: sharp bounded-disagreement frontier

For policies a and b, put D=K_a-K_b, d_j=p_aj-p_bj and o_j=min(p_aj,p_bj). If the above joint feasible pair-set is nonempty and rectangular **across labels**, the sharp comparison bounds are

    lower = D + sum_j [d_j>=0 ? d_j*l_j : d_j*h_j] - sum_j o_j*eta_j,
    upper = D + sum_j [d_j>=0 ? d_j*h_j : d_j*l_j] + sum_j o_j*eta_j.

The first terms are the previous **fully common residual** bounds. The extra ambiguity is proportional to the *overlapping policy exposure* o_j, not p_aj+p_bj. At eta=0 this equals the common-residual formula; at eta=h-l the bounds equal separate, independently optimized residual intervals. Intermediate eta provides an exact (not merely conservative) interpolation under the stated joint rectangular class. An observed or audited eta bound smaller than h-l can thus matter even when strict controller invariance is false.

**Proof sketch.** Fix j. If d>=0, minimizing p_a u_a-p_b u_b on the diagonal strip inside [l,h]^2 chooses (u_a,u_b)=(l,l+eta), giving d*l-p_b*eta. Maximization chooses (h,h-eta), giving d*h+p_b*eta. For d<0, the minimizing corner is (h-eta,h), giving d*h-p_a*eta; the maximizing corner is (l+eta,l), giving d*l+p_a*eta. Because each objective is linear and the feasible strip is a convex polygon, these corners attain the extrema. Add D and independent j extrema only if rectangular cross-label feasibility holds. Correlated persistent demand/transfer worlds instead require joint optimization; summing extrema then gives at most valid outer bounds. See [proof ledger](PAIRED_RESIDUAL_PROOF_LEDGER.md). This is linear programming geometry and a sensitivity identity, not a new off-policy estimator.

**Economic interpretation.** A mismatch-cap improvement from eta to eta' tightens each end of this *decision certificate* by sum_j o_j(eta_j-eta'_j). It does **not** manufacture additional customer production. A target diagnostic can be valuable only if the resulting information changes an actual future decision enough to pay for its cost; target training/grounding must remeasure p,K and residual bounds because it changes the technology. Similarly, a copied source trajectory is an **optionally usable input**; forcing its use may damage a controller, while freely ignoring it preserves the old-policy menu.

## Reuse the earlier source-copy/no-copy witness; do not retune to win

The previous chapter had K_copy=27/20, K_no=7/5, p_copy=1/2, p_no=1/4, with a shared unknown target-service residual in [0,4]. This is an **invented normalized whole-service witness**; it is not customer or robot data. D=-1/20, d=1/4 and overlap=1/4. With policy divergence cap eta:

    J_copy - J_no in [-1/20 - eta/4, 19/20 + eta/4].

At eta=0: [-1/20,19/20]; eta=1/2: [-7/40,43/40]; eta=4: [-21/20,39/20], recovering independent extrema exactly. Even perfect equality cannot establish unconditional source-copy dominance because its lower endpoint is negative.

If an independently approved diagnostic *only* establishes both conditional residuals in [3,4], then eta<=1 mechanically and the contrast is in [9/20,6/5]. **Conditional** source-copy economic dominance over no-copy follows in that restricted world class, without claiming the diagnostic was actually obtained or makes either controller safely admissible. Under eta=0 the [3,4] contrast is [7/10,19/20]. Neither bound gives a general ranking against F, S, new body H or a joint-market specialist under different qualification menus. If diagnostic collection changes the trajectory, accounting or feasibility, the same K,p cannot be reused.

## Constructive impossibility and a possible architectural route

Two worlds can agree on all pre-exit qualified-service, copied data, K, p and observed target-state labels. In world 1, the source-copy controller's unobserved post-exit whole-service residual is 0 while no-copy's is 4; their difference is -21/20. In world 2 these residuals are reversed; their difference is 39/20. Both satisfy the individual interval [0,4]. Thus **no eta<4 follows from the common observed histories**. This is identification logic, not a claim that physically deployed robots exhibited either world.

A possible *sufficient* mechanism for eta=0 is an independently approved **same-state, same-time, same-resource common continuation**: at first exit both complete policies transition without an omitted delay, cache, compute, shared-operator or demand effect to one identical fully qualified fallback/dispatch configuration, with equal conditional remaining-order laws given a genuinely complete network state. This is substantially stronger than "fall back to F when uncertain." If fallback action differs in physical reachability, embodiment, remaining customer window, queue history, B-order eligibility, service cancellation or controller/data-plane load, its value can be policy dependent; the eta gap has not been certified. A pre-certified fallback changes the **feasible policy** and potentially its K,p, not just a proof assumption.

## Development and identification consequences

1. **Technical transfer** should be tested as a source-use/no-use intervention under matched checkpoints, separate validation and resource budgets, with target joint qualification, learned-policy occupancy, and full B/A accepted-order histories. An increase in held-out motion accuracy does not supply K, p or eta.
2. **Source data, grounding and embodiment** can alter different components: extra source data may change qualified Q and target occupancy; grounding can identify unsupported target states, change the controller, or both; a new embodiment changes reachable action support and resource constraints. Their comparison occurs within the same dynamic J and V(Q;omega), with F/S retained as approved options.
3. **Policy-dependent network effects** must include original customer orders, substitutions/unattempted orders, operator peak recovery and dispatch spillovers. If these are not logged and approved, even a small positive measured A-customer gain is not a credible bound on the *whole network*.
4. **Prior art**: Laroche, Trichelair and Tachet des Combes (2019), ICML/PMLR 97, https://proceedings.mlr.press/v97/laroche19a.html, study baseline bootstrapping with data-uncertain state-actions; the baseline-bootstrapping and safety-improvement idea is not ours. Ross, Gordon and Bagnell (2011), https://proceedings.mlr.press/v15/ross11a.html, give prior policy-induced-data foundations. Khan, Saveski and Ugander (2023), https://arxiv.org/abs/2305.11812, study partial identification without overlap under their structural conditions. Farboodi, Koh and Xia (2026), https://arxiv.org/abs/2606.10127, already endogenize data and production value. Here the narrow conditional accounting object is *full accepted customer-production divergence* under policy-dependent target support, not an independently established new general theorem.

The [prospective test protocol](PAIRED_RESIDUAL_EMPIRICAL.md), [exact executable arithmetic](paired_residual_sensitivity.js), [saved results](paired_residual_sensitivity_results.json), and [exercises/solutions](PAIRED_RESIDUAL_EXERCISES.md) are research artifacts, not evidence of a real loss cap. No physically authorized whole-network experiment, signed customer-order panel, validated eta bound, numerically linked BLS–BEA production matrix or peer-reviewed novelty claim exists. The November 22 synthesis gate and all later gates remain open.
