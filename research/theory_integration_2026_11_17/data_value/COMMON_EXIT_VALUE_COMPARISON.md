# Comparing learned controllers when unsupported outcomes are shared

**Private theory continuation, 18 November 2026.** This develops the same data-transfer → joint qualification → accepted whole-network production argument after [policy-induced support](POLICY_INDUCED_SUPPORT_FRONTIER.md). It is a **conditional partial-identification reduction**, not a new off-policy theorem, field estimate or robotics safety certification.

## Intellectual question

The existing first-exit proposition bounds each source-trained or untrained controller separately. But the deployer must choose **between** controllers, source acquisition, target grounding and embodiment. If two controllers expose the *same* unknown post-exit customer outcome, independently taking the worst case for one and best case for the other implicitly selects **different worlds**. When can common uncertainty legitimately cancel in the economic contrast—and when does training change the unsupported continuation so cancellation is invalid?

## Environment and admissibility

For each candidate policy i (source-copy, no-copy, grounding, retained F, qualified specialist S or a new body), use the SAME pre-action complete customer order/opportunity census, horizon, captured-value contract, material resource constraints, permitted data rights and policy-closed controller/dispatch/operator/customer-demand boundary. Physical approval and qualification of every compared complete policy are **separate prerequisites**.

Policy i induces a *versioned* stopped joint history under its own approved checkpoint. Its first exit from genuinely identified **joint whole-network** history-action support has a mutually exclusive label j in a finite set E. A label must specify enough of the complete original-B-order state, customer demand/dispatch, action/recovery, operator pool, contracts and remaining time to make the residual economic object comparable. Let p_ij be that policy's identified probability of exit into j, measured under **i**, not transported from F. Let K_i include measured no-exit contribution, all known exit-prefix cash/production, policy-specific acquisition and training/curation costs and policy-specific *identified* qualified service after arrival. Count each order and cost once; do not add a separate data premium.

The **common-residual restriction**, more demanding than a shared state name, is that within every feasible complete world theta, the remaining *unidentified conditional mean* contribution is u_j(theta) for all compared policies arriving at j, even after accounting for each policy's identified differences already included in K_i. Thus

    J_i(theta) = K_i + sum_j p_ij u_j(theta).

This may hold if both arms use the **same independently certified pinned fallback** after reaching an identical complete state, or if a specific common customer-demand residual is demonstrably separable from known policy-specific qualified service. It usually **does not follow** for a source-trained recovery policy, newly connected controller, customer-choice response or changed embodiment. It is an assumption to audit, not a benefit inferred from similar marginal benchmarks. Fixed theta is shared across both policy alternatives; it is not redrawn adversarially after each visit.

If identified K or p also depend on theta, retain them as K_i(theta),p_ij(theta) and optimize the entire paired expression over one joint feasible theta set; the simple formula below does not apply unmodified. Let l_j <= u_j(theta) <= h_j. This is an *identified or explicitly sensitivity-assumed* box; independent endpoint attainment across j is an additional assumption for sharpness.

## Conditional proposition: signed-overlap whole-service comparison

For two feasible, separately qualified policies a and b, define d_j=p_aj-p_bj and D=K_a-K_b. The contrast is

    J_a(theta)-J_b(theta) = D + sum_j d_j u_j(theta).

Under the rectangular unrestricted common-residual class U=product_j[l_j,h_j], the **sharp** contrast interval is

    LOWER = D + sum_j (d_j>=0 ? d_j*l_j : d_j*h_j),
    UPPER = D + sum_j (d_j>=0 ? d_j*h_j : d_j*l_j).

Its width is sum_j |d_j|(h_j-l_j), **not** sum_j(p_aj+p_bj)(h_j-l_j). Against naive subtraction of two separately optimized policy bounds, *both endpoints* improve inward by the exact nonnegative amount

    sum_j min(p_aj,p_bj)(h_j-l_j).

**Proof.** Linearity and the common theta imply the signed d_j, rather than two independently selected u's. Under rectangular U, select each endpoint according to sign(d_j), giving attainable extrema if every corner is feasible. For d_j>=0 the naive lower contribution is p_aj*l_j-p_bj*h_j while the paired lower is (p_aj-p_bj)l_j: difference p_bj(h_j-l_j). For d_j<0 it is p_aj(h_j-l_j). Repeat with reversed endpoints for the upper bound. No assumption of independent **qualification outcomes** is used; p and K can derive from a fully joint, correlated Q/dispatch/recovery process. Rectangularity concerns residual *feasible worlds*, not independence of robots.

If p_aj=p_bj for every unsupported residual j, the **contrast is identified** as D even though neither policy's absolute contribution need be identified. This is a common-nuisance cancellation, not a claim that either robot is safe or commercially attractive relative to S. If residuals share a persistent demand/transfer regime, use the actual coupled set U(theta) and optimize the same single-world linear contrast; box formulas are outer bounds, not necessarily sharp.

### Allow qualified-service deviations rather than assuming them away

Where policies have different unknown post-exit service, write u_ij(theta)=u_j(theta)+e_ij(theta), with independently **auditable** |e_ij|<=epsilon_ij after known policy-specific terms are removed. Then the contrast above has an additional residual no larger in absolute value than sum_j(p_aj epsilon_aj+p_bj epsilon_bj). This is a valid conservative **economic** sensitivity expansion, but only if epsilon bounds every relevant B-order, demand, operator and recovery effect across the full horizon. A source-trained controller with genuinely new recovery states may have no useful epsilon bound. The earlier first-exit individual bound remains the honest fallback. No TV mean-value shortcut certifies peak recovery safety.

## Reused synthetic source-copy versus no-copy example

Use the **same** accepted-service witness from [policy-induced support](POLICY_INDUCED_SUPPORT_FRONTIER.md), but now allow the copy-trained controller's unsupported arrival probability to change (the defect identified in that chapter). No-copy c service 2, exit chance 1/4, cost 1/10; copy-trained c service 3, exit chance 1/2, cost 3/20. Their identified terms are K_no=7/5 and K_copy=27/20, with common full-network unknown u in [0,4]. These are invented exact normalized contribution units, not a mapped technical benchmark.

    J_copy(u)=27/20+(1/2)u;  J_no(u)=7/5+(1/4)u.
    J_copy-J_no=-1/20+(1/4)u.

The **same-world** interval is [-1/20,19/20], compared with [-21/20,39/20] if independently taking copy's worst and no-copy's best in different worlds. The common overlap 1/4 times uncertainty width 4 explains the exact 1-unit improvement at each endpoint. Neither controller is uniformly better: source-copy wins only for u>1/5. This remains distinct from comparing either with competent S=2, which the individual lower bounds fail to dominate.

If an **independently safe and valid** target diagnostic were to establish that this *same invariant residual* lies in [3,4] without changing p, K, demand, rights or actions, the contrast would be [7/10,19/20]; absolute conditional lower values are 57/20 and 43/20. This is an **illustrative inference** after legitimate evidence, not a proposal to probe unapproved target states and not a new physical production gain. A target-grounding **training intervention** that modifies recovery, Q or occupancy instead requires new policy-specific K, p and residual comparison.

Two falsifiers delimit the constructive result:

- With equal p=1/4 for both controllers, a known K difference of 1/5 identifies a 1/5 contrast regardless of unobserved u, **only if** the conditional residual truly is common.
- Merely giving two policies the same unsupported label cannot justify cancellation. If p=1/4 for both and known K matches, but post-exit source-copy service is 0 and no-copy service 4, their contrast is -1; reversing the unknown responses yields +1 while all pre-exit observations remain identical. A changed recovery controller, shared human dispatch or embodiment can create precisely this structural failure.

## Production economics and acquisition implications

**More source production data** may improve the identified K term by changing joint qualified accepted service, *or* shift p into newly unsupported target recoveries. **Target grounding** may shrink the admissible u set by supplying safe evidence, alter K through Q improvement, change p through a new policy, or combine all three; count each causal effect once. **New embodiment** generally changes the essential service states, operator commitments and the j labels, so policy-invariant residuals require independent evidence and often cannot be assumed. Deliberate teleoperation, failure/recovery, simulation, synthetic, public/pretrained and ordinary production logs have distinct likelihoods, rights and structural transitions. The model does not impose a universal additive transfer law or a human-data ontology.

Decision relevance is signed occupancy **difference**, not the sheer data count or even individual policies' unsupported occupancy. A safely grounded shared residual can sharply refine a policy **comparison** when |d_j| is large; if d_j=0 it cannot change the paired ranking under the assumptions, although it may be valuable for absolute risk, another comparator, safety or future model learning. Optional free data access weakly expands the admissible decision menu; mandatory use/training can lower realized J, and a negative-transfer training result cannot refute menu monotonicity.

Retained F/S and all rights/resource constraints remain in the feasible set. The correct economic objective is the established complete-history J through optimized V(Q;omega), not a regret premium or shadow price added on top. Conditional comparative dominance is not physical approval; qualification thresholds and B displacement can invalidate K/p and the shared residual.

## Prior art and empirical falsification

The mathematics is standard partial identification, signed differences and policy-dependent visitation, not proven scientific novelty. Relevant sources verified via primary abstract/full HTML on 18 Nov: Ross, Gordon and Bagnell (2011), PMLR 15:627–635, https://proceedings.mlr.press/v15/ross11a.html (policy-induced observations); Khan, Saveski and Ugander (2023), https://arxiv.org/abs/2305.11812 (off-policy bounds without overlap using smoothness); and DDA (2026), https://arxiv.org/abs/2606.10127 (already endogenous economic data value). Our **common residual** is a different, strong invariance premise, not an implication of those sources. No claim of direct quotation or comprehensive bibliographic audit.

Prospective empirical comparison: [COMMON_EXIT_EMPIRICAL.md](COMMON_EXIT_EMPIRICAL.md). Auditable derivations and boundary cases: [COMMON_EXIT_PROOF_LEDGER.md](COMMON_EXIT_PROOF_LEDGER.md). Reproducible exact arithmetic: [common_exit_comparison.js](common_exit_comparison.js) and [common_exit_results.json](common_exit_results.json). Student questions and separate instructor solutions accompany this chapter. Scientific gate on Nov 22 remains **OPEN**: actual target p/K, fully qualified whole-service conditional residual equivalence, signed original B orders, operator safety, numeric official production backbone and independent novelty remain missing.
