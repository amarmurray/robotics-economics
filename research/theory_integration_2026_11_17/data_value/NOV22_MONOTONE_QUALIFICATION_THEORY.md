# November 22 adversarial synthesis: demand-matched monotone qualification and menu closure

> **20 November adversarial correction to interpretation.** [Policy availability is not casewise nested qualification](FALLBACK_POLICY_VS_NESTED_QUALIFICATION.md). A physically **selectable** old policy guarantees only enlargement of a feasible decision set under an unchanged world; it does not imply that a *chosen/admitted upgraded controller* succeeds on every old-success history. The proposition below remains correct conditional on the **stronger** Q1>=Q0 for the **implemented** policy, with a verified nonregressing gate, non-destructive retry or genuinely redundant resources and stable original buyer B. A mere reversible model installation or positive arm-average qualification gain is insufficient. See [proofs](FALLBACK_POLICY_VS_NESTED_QUALIFICATION_PROOFS.md) and [prospective safety audit](FALLBACK_POLICY_VS_NESTED_QUALIFICATION_EMPIRICAL.md). This correction keeps the Nov22 gate OPEN.

**20 November 2026 UTC | Private working theorem/proof review | No field estimate; November 22 gate OPEN.**

## One question, not another independent model

When can an upgrade from heterogeneous source learning X, target grounding G or a certified embodiment E be valued as *additional safely deliverable, purchased original-customer service*, rather than as an improvement in technical task scores? The preceding joint menu/exposure analysis showed that baseline buyer/qualification correlations alone do not transport across policy or menu changes. Its sharp conditional two-bit bounds need upper restrictions on **individual cross-world** buyer and qualification changes; equality of randomized arm means cannot provide those restrictions.

This review isolates a constructive answer when one of those assumptions is *physically implementable*: retaining a certified incumbent service option can make the set of safe qualifications nested. Monotonicity then turns the **observable qualification marginal difference** into the number of qualifications newly created, without pretending that individual potential outcomes were observed. Combining that with original-market unmet-demand records gives honest bounds on how many of those new qualifications can actually be sold. This is a conditional specialization of the same optimized qualified-production framework, not an alternative to it.

## A demand-matched monotone qualification proposition

Fix an original eligible parent/customer/network registry, a single lawful precommitted second-service offer and window, unchanged physical/operator rights and capacity, and the original menu/quality/capture rules. The buyer's prospective second-service purchase indicator is B (including B=0 for declines), defined *before* conditioning on a robot's observed ability. Let Q0 indicate complete, safe, approved joint second-service qualification under the incumbent and Q1 under the contemplated upgrade. A **nested qualified fallback** means Q1 >= Q0 for every original parent/network realization: the old qualified recipe and its resource/dispatch rights are actually still available, and the upgrade can be ignored. This is a strong physical-contractual restriction, not a consequence of training, randomization or technical model accuracy.

Write

    d = P(Q1=1) - P(Q0=1),
    M = P(B=1, Q0=0),     N = P(B=0, Q0=0).

Then 0 <= d <= M+N, and the *incremental paid-and-qualified opportunity rate* obeys the sharp, attainable bounds

    max(0, d-N) <= P(B Q1) - P(B Q0) <= min(d,M).             (1)

Proof and finite-population attainment: [proof ledger](NOV22_MONOTONE_QUALIFICATION_PROOFS.md). The interval is generally not a point even though the treatment-arm marginal qualification effect d is identified under valid randomization. The missing quantity is **where the conversion from Q0=0 to Q1=1 falls relative to a genuine customer purchase**, not the average transfer effect itself.

For an isolated second-service opportunity with stable *net captured contribution* v per actually purchased, safe accepted unit, no other displaced resource uses and one acquisition cost k, incremental economic contribution lies in

    [v max(0,d-N)-k,  v min(d,M)-k].                         (2)

It is not legitimate to use (2) with incompatible robot configurations, scarce shared operator slots, menu-dependent buyer choice, uncertain contribution capture, or post-treatment-selected customers. Then use the full optimized complete-order V and its valid LP/resource-price upper and feasible-policy lower certificates. Acquisition effects on future customer orders already enter the continuation problem; do not append a second "data premium".

**Exact finite example, not a robotics estimate.** On eight original cases, M=2/8, N=2/8, and d=3/8; the other four baseline cases are already qualified. Exactly three formerly unqualified cases convert, but their allocation between prospective purchasers and nonpurchasers is unknown. Incremental paid qualification is between 1/8 and 2/8. At hypothetical contribution v=4 and incremental cost k=1/4, net incremental value lies in [1/4,3/4] normalized units. The exact-integer executable independently enumerates every feasible allocation; the algebraic proof does not rest on the code. A new benchmark result giving d alone would incorrectly report 3/8 as new market production.

## A stronger observable when demand strata are recorded before treatment

Let Z be a *preintervention* original market/customer/task stratum with stable membership and no cross-stratum interference. Within each stratum use observed baseline (B,Q0) and identified qualification gain d_z. Equation (1) bounds the total incremental paid rate by

    sum_z P(Z=z) max(0,d_z-N_z)
       <= Delta_paid <=
    sum_z P(Z=z) min(d_z,M_z).                              (3)

This interval is contained in the one computed from aggregate d,M,N: information about **which demand stratum learned** matters even when aggregate technical learning is unchanged.

Exact demonstration: two equally weighted strata, each with four original cases. A has M_A=2/4,N_A=0 and one conversion; B has M_B=0,N_B=2/4 and one conversion. Without stratum labels the population has M=N=2/8,d=2/8, giving a paid-improvement interval [0,2/8]. With the preassigned stratum gains the paid improvement is exactly **1/8**: one useful conversion in A and none in B. This is a structural explanation of why a demand-conditioned source mixture or target-grounding experiment may be economically informative without identifying a dollar price per trajectory.

An empirical design can compare deployment trajectories, recoveries, teleoperation, simulation, synthetic/public/pretrained and other legally usable data sources by their **stratum-specific safe qualification changes under matched source cost, compute, operator time and rights**, not by a common demonstration count. Target grounding may change B or lower operator requirements, while embodiment E may change the original service universe; those cases require the full action-specific model, not (1).

## Where the monotone shortcut fails

1. **Demand changes:** If prospective purchase becomes B1 after the policy/offer change, the identity

       B1 Q1 - B0 Q0 = B0(Q1-Q0) + (B1-B0)Q1

   separates nested technical improvement from customer-choice drift. If a separately justified same-original-network switch bound P(B1 != B0)<=u_B exists, (1) implies only the **conservative**, not generally sharp, difference interval [max(0,d-N)-u_B, min(d,M)+u_B]. Without that bound or direct policy-specific paid-service measurement, improved qualifications can produce *less* paid service. In the committed eight-case counterexample Q1>=Q0 on every case and one baseline demand-active failure becomes qualified, yet one buyer flips out; realized paid qualification stays at 2/8, not the stable-buyer 3/8. A small change in buyer *mean* is not a substitute for a switch bound.
2. **Mandatory model swap:** Q1>=Q0 is valid only if the original complete-service recipe is still certified, legal, supported, dispatchable and feasible with the relevant operator/resource budget. A forced controller/embodiment replacement can remove the old recipe; equal "new" technical percentages do not give an economically nested feasible set. Free *optional* availability of source data weakly enlarges the feasible choice menu and cannot reduce the optimized **gross** value under unchanged environment. Forced costly training and closed old options can lower **net** value.
3. **Menu-dependent first purchase:** For legal menus m6 (one service at 6) and m4 (two services at 4 each), the actual **precommitted** expected value is

       J(a) = max{6 q_(a,m6), 4[q_(a,m4)+s_(a,m4)]} - K(a),

   with first-sale probabilities q and the paid-qualified second-event rate s indexed by their own policy **and menu**. The old expression max{6q,4(q+s)}-K is a valid reduction *only if the first-sale probability is common across legal menus*. A synthetic original market with q6=4/8, q4=6/8, s4=1/8 has correct optimized value 7/2, while transporting the q6 first-sale rate to the low-price menu incorrectly yields 3. If menu selection is permitted only *after* an observed market report, its information value is E[max_m E[R_m|report]] rather than max_m E[R_m]; no double count.
4. **Whole-network and rights interference:** Nesting a single Q for one order does not certify simultaneous scheduling, procurement competition or model-pool effects for another. If qualification, buyer alternatives and operator recovery interact across customers, use approved *whole-network policy* outcomes with original zero-sales in the denominator, or a physically justified network exposure/transport envelope. A supplier's offer quote, willingness to pay, buyer cash budget, and customer payment are distinct records.

## November 22 A–B and scientific status

**Model A** remains optimized qualified production with complementary recipe bundles, heterogeneous customer demand, physical/operator prices and a competent alternative. The new result identifies a precise special case in which a measured marginal qualification gain yields **bounds on value-relevant demand matching**. It does not imply that all useful service is divisible or noninterfering.

**Model B** retains the timing of acquisition, informative reports, productive deployment data, target-grounding interventions, embodiment/manufacturing choice, retained fallback and finance/rights constraints. The result is a one-window projection of its safe operator/customer closure. When action changes future learning opportunities or customers, apply the entire two-date J without adding the continuation value again.

**Prior-art objections remain decisive.** Manski (1997), *Monotone Treatment Response*, Econometrica 65(6), 1311–1334 (https://ideas.repec.org/a/ecm/emetrp/v65y1997i6p1311-1334.html) already establishes monotone response as an identification restriction. Laroche, Trichelair and Tachet des Combes (ICML 2019, https://proceedings.mlr.press/v97/laroche19a) analyze baseline-safe policy improvement. Standard principal-stratum, joint potential-outcome and Fréchet/transport bounds provide the statistics. The project can claim neither the monotonicity argument nor the inequality alone as a novel theorem. DDA §5 and Appendix B already value future data, modified production and complementary aggregation (https://arxiv.org/abs/2606.10127). The candidate robotics-economics contribution must be a substantive, empirically discriminated *joint qualified whole-service production* mechanism against competent retained/specialist and digital-operator alternatives.

**Acceptance gate remains OPEN.** No signed physically nested fallback, original whole-parent purchase/decline registry, randomized same-network qualification gain, lawful policy-specific price/capture envelope, approved embodiment trial, full numerical BEA use/supply + BLS concordance, full CI, or independent originality review was obtained. The original December 25, 2026, 23:59 America/New_York deadline remains intact.