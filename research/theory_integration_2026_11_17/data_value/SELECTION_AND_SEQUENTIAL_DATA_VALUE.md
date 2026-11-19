# Source-first failure selection and the economic value of grounding versus embodiment

**Private continuation, 18 November 2026 Eastern / 19 November UTC.** This extends *When Capabilities Become Production* and the immediately preceding sequential policy-value result. It is a conditional decision-theoretic synthesis, not estimated robotics economics or a scientific novelty claim.

## The unresolved distinction

An independently approved randomized comparison of grounding against a qualified fallback *after a specified source-training failure* can identify that policy's mean whole-network economic effect. It does **not** say how valuable grounding will be after changing the source mixture, data quality, training recipe, embodiment or customer opportunity process. Those changes can alter **who remains unqualified**, what their failure reports reveal, and what later acquisition is best. The distinction is material even if additional source data never change the physical efficacy of the later interventions.

The active question is therefore not another arbitrary transfer-coefficient simulation: **when does a source investment change the optimal subsequent choice between target grounding, an alternative body and retaining a competent incumbent merely by selecting the unresolved customer/qualification histories?**

## 1. The complete economic decision and four estimands

Let x denote a prospectively defined first-stage source/learning policy (including rights, compute, controller and embodiment lineage). It induces a first-stage full-network history H_x, qualification-failure indicator D_x, and E_x indicating *pre-second-stage* approval and feasibility of the candidate complete continuation policies. All jointly affected robots, dispatch, shared learning, human operators and customer-order markets belong in the unit. At every realized history the economically admissible policies include the qualified incumbent or specialist F; candidate later policies include source-conditioned grounding G, a changed embodiment B and continued productive routine R only where independently approved.

Write Y_x(a) for remaining-horizon **captured net accepted customer production** under complete continuation a, including original-order retention or displacement, demand, recovery, real resource and validation costs and the allowed old-policy fallback. No benchmark success is converted directly into a dollar. Define

    d_x(a,h) = E[Y_x(a)-Y_x(F) | H_x=h, D_x=E_x=1].

The first-stage contribution J_x(F) already includes current accepted production and source-learning expenses once. If conditional effects can be learned for every relevant pre-choice history, the optimal second-stage acquisition menu has

    J_x^* = J_x(F) +
            E_x[ 1{D_x=1,E_x=1} max(0, d_x(G,H_x), d_x(B,H_x), ...) ].

Here the maximum is taken **after the actual pre-choice history**, not after an unobserved future qualification. If actions are feasible only for subsets of histories, maximize over those preapproved actions. This is the standard dynamic-decision identity by conditional expectation. A different information state (e.g. no target-state diagnostic) changes the available decision rule; it cannot be treated as a free oracle. The term in expectation is the real continuation effect, not a second price premium for future data.

Four quantities must not be conflated:

1. **Static economic arm means:** mean Y(x,g) for separately approved, complete static source-by-grounding policies. A valid whole-network factorial study can identify them but does not identify cross-policy individual skill overlap.
2. **Cross-policy qualification dependence:** t=P(Q_a=1,Q_b=1) for potential complete controllers on the same underlying opportunity. Marginals alone cannot determine t; paired safe tests or explicit restrictions are needed.
3. **History-conditioned sequential technical response:** r_x(h)=P(Q_{x then G}=1 | H_x=h,D_x=1), where the later training algorithm and support are specified. Neither t nor a static G success rate is necessarily r_x.
4. **Sequential economic continuation effect:** d_x(G,h) or the integrated policy contrast above, which may be identified directly by a preapproved stage-two whole-network randomization without recovering t or r_x, but only for the source regime and supported eligible histories actually studied.

The prior [sequential chapter](SEQUENTIAL_POLICY_VALUE.md) proves the fourth identification conditional on no between-unit interference and complete outcome measurement. It does not establish transport from x to x'.

## 2. Exact failure-selection identity

For a transparent structural special case, index a fixed potential customer/qualification type by z, on one unchanged target population P. Let q_0(z),q_1(z) be deterministic first-stage success indicators. Assume **nested success** q_1(z)>=q_0(z): more source resolves some earlier failures but never removes an old qualification. Assume unchanged, type-specific complete-continuation incremental effect g_a(z)=Y(a,z)-Y(F,z) for each approved second-stage action a. This last restriction is strong: it excludes transfer-mediated changes to a, demand shifts, changed target occupancy, altered recovery, eligibility and shared-pool spillovers. We relax it conceptually below, rather than silently assuming it.

Define F_0={z:q_0(z)=0}, F_1={z:q_1(z)=0}, and R=F_0\F_1 (the newly resolved types). Let their masses be pi_0,pi_1,m=pi_0-pi_1>0. Put delta_j(a)=E[g_a(z)|F_j] and delta_R(a)=E[g_a(z)|R]. For positive masses,

    pi_0 delta_0(a) = pi_1 delta_1(a) + m delta_R(a),

and consequently

    delta_1(a)-delta_0(a) =
        (m/pi_0)[delta_1(a)-delta_R(a)].                      (S)

This is an exact decomposition of a changed **eligible failure composition**, not a causal estimate from unmatched post-source survivors. If the newly resolved histories were especially favorable for grounding, the observed grounding effect on the remaining failures decreases even if the grounding technology is identical.

For two downstream actions a and b apply (S) to g_a-g_b. The ranking can flip when the newly resolved group favors a while the remaining failure group favors b: specifically, with A=E[g_a-g_b|R]>0 and B=E[g_a-g_b|F_1]<0, a wins among original failures but b wins among new failures if and only if m*A>pi_1*(-B). The **action-substitution threshold is generated by the changed risk-set weights**, not an imposed source transfer coefficient. If either group has zero mass, define the corresponding conclusion without dividing by its mass.

Neither nested cross-world success nor g invariance is identified merely by two independent randomized source arms. One may use this as a *structural sensitivity scenario* if signed controller tests support the restrictions, never as a general causal claim. The sequential economic randomized effect is within its own x-regime and does not require comparing the same principal stratum across x.

## 3. Complete-service counterexample (all numbers synthetic)

Consider two equally common initial customer-opportunity types, easy and hard. The old qualified controller provides a retained B service with the same net contribution under every policy, so that contribution cancels in the comparison. An additional **accepted complete A order** contributes 2 normalized units if qualified and delivered; this is one complete-service increment in V(Q;omega), *not* a motion success or wage rate. Source regime x0 initially qualifies neither type. A better source x1 qualifies easy but not hard, with paid source acquisition/training expense 3/10. A grounding attempt G qualifies easy only and costs 2/5 per attempted still-failing case. A changed, separately qualified body B qualifies hard only and costs 7/10 per attempt. Every unsuccessful second-stage intervention retains the old B controller, but its intervention cost remains real. Before x1, the type is not distinguished by the failure observation; after x1, a failure reveals the hard type. No action has an asserted physical approval outside this hypothetical model.

| Initial source regime | Initial incremental A production | Expected G after failure | Expected B after failure | Best follow-on | Total increment before paid source expense |
| --- | ---: | ---: | ---: | --- | ---: |
| x0 (both fail) | 0 | 3/5 | 3/10 | G | 3/5 |
| x1 (only hard fails) | 1 | -1/5 | 13/20 | B | 33/20 |

With the 3/10 source expense, x1 followed by B produces **27/20**, exceeding x0 followed by G (**3/5**), even though G and B have completely unchanged type-specific training/qualification effects. Source investment here partly creates productive qualification and partly changes the information/selection set for later acquisition. It is wrong to ascribe the whole advantage to a learned positive technical transfer coefficient.

The conditional G effect per *eligible failure* is 3/5 after x0 but -2/5 after x1; the difference is purely selection. The conditional B effect is 3/10 then 13/10. On newly resolved easy types G-B=23/10, while on residual hard types G-B=-17/10; the original mixture favors G by 3/10, but residual failures favor B. Identity (S) verifies these figures exactly.

A **different information comparator is consequential**. If x0 could obtain a costless, independently valid and physically approved *pre-choice perfect type diagnostic*, it could choose G for easy and B for hard; its gross expected follow-on becomes 29/20, **larger than x1's net 27/20**. A diagnostic costing less than 1/10 still reverses the preferred investment. This diagnoses the model's information mechanism instead of assuming that more source data always win. The original x0 policy remains optional when x1 data are free; its feasible value cannot be reduced merely by optional availability. Paid/forced training and nonretention can reduce realized value.

The [scoped exact executable](stage_screening_selection.js) and [saved outputs](stage_screening_selection_results.json) audit the fractions, failure decomposition, action reversal and a finite 1,681-cost-case sign-condition grid. The checks are not an empirical test or an independent proof.

## 4. What the result does and does not imply

**General result:** the economic marginal value of later grounding or embodiment is conditional on the **distribution of unresolved qualified customer-service opportunities**, not merely on the total technical proficiency of the earlier source-trained controller. When source acquisition endogenously selects the remaining failures, a pooled effect per training attempt is not portable even if the downstream training technology were unchanged.

**Not established:** physical monotonicity of source performance; invariant downstream transfer or customer demand; existence of a cheap diagnostic; availability of independent complete market networks; point identification of any cross-policy principal stratum; an industry robot adoption law; or scientific novelty. If source learning changes g_a(z), operator coverage, safety, order arrivals, willingness to pay, policy occupancy or cross-embodiment representation, (S) no longer isolates the effect. Recompute each complete-policy Y_x(a) or bound the missing support instead. Fully optional free source data and an unrestricted old-policy menu retain the standard weak value monotonicity; the *incremental option value of one specific downstream action* need not increase.

**Connection to source type:** production-generated field trajectories, failures/recovery, productive teleoperation, deliberate target probes, simulation, synthetic episodes and public/pretrained corpora have different collection/selection gates. Their effect on first-stage Q, report H and second-stage r must be measured separately. A broad source mixture can remove easily transferable cases and leave a more expensive grounding population; conversely, targeted grounding can unlock dormant pretrained representations. Changes in the denominator of unqualified customer jobs and their demand value are as important as performance averaged over a benchmark.

**Models A and B:** each qualified A order above corresponds to an incremental optimized operating contribution V(Q union A;omega)-V(Q;omega). In Model A the contribution must be recomputed under the actual customer demand, alternative and capture contract; 2 is not an observed fixed wage. In the deterministic known-policy limit, Model B's funded expansion calculation remains intact; endogenous first-stage failure and contingent second-stage spending cannot be reproduced by substituting average training cost into that historical example.

## 5. Evidence that would discriminate the mechanism

The [empirical protocol](SELECTION_EMPIRICAL.md) preserves a full policy-closed original-order registry, pre-choice H and eligibility, safely approved within-source random continuation comparisons, and an explicitly separate test of cross-source transport and diagnostic substitution. Matching individual robots within one shared dispatcher does not provide independent network trial units. No approved deployment/customer data exist here. Public DROID and Open X-Embodiment are potential technical comparison resources, not invoices or economically qualified service.

The closest established methodological foundations are **Murphy (2003), Optimal Dynamic Treatment Regimes**, DOI https://doi.org/10.1111/1467-9868.00389, and **Frangakis and Rubin (2002), Principal Stratification in Causal Inference**, DOI https://doi.org/10.1111/j.0006-341X.2002.00021.x. The latter is especially relevant to the inadmissibility of a naive causal comparison conditioning on differently selected post-source failures. Farboodi, Koh and Xia (2026), *Data-Driven Automation*, https://arxiv.org/abs/2606.10127, already values production-generated future data in §5 and discusses complementarity in Appendix B. Our result is an organized robotics production interpretation of standard conditional expectation and selection mathematics, **not a proof of independently new science**.

**Next exact question:** Can prospectively versioned first-stage source alternatives and pre-choice failure/target-support histories be linked to *joint fully accepted customer-service recipes*, with stage-two policies genuinely approved and policy-closed? If not, which source-regime comparisons remain only identified sets rather than transportable rankings? Complete the November 22 synthesis review before broadening the policy menu further; empirical backbone and full Christmas scope remain active.
