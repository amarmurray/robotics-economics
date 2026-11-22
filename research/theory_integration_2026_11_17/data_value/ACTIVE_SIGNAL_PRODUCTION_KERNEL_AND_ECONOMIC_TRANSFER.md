# Active signal acquisition changes the production network: a conditional recursive data-value bridge

**22 November 2026 — continuation of *When Capabilities Become Production*, Models A/B. Scientific acceptance OPEN.** This chapter answers the next question from [lawful signal timing](LAWFUL_SIGNAL_TIMING_AND_RECURSIVE_DATA_OPTION.md): what becomes of exogenous report-value comparisons when collecting information is itself a production, learning and recovery intervention? All prices, probabilities and outcomes below are **synthetic normalized accepted-and-cleared original-buyer contributions**, not measured robot results or conversion of benchmarks into money.

## 1. Place in the same integrated economy

The object is a lawful *complete policy*: an original buyer's eligible offer or no-offer, service-specific qualified controller/robot configuration, customer acceptance and cleared net receipts, physical/worker/cash capacity, and data rights over the full horizon. The firm chooses among a retained approved controller R, productive source-field acquisition P, deliberate target grounding/teleoperation D, source-plus-grounding combinations SG, and an independently resourced new embodiment E. There can be distinct field trajectories (including failures and recoveries), teleop episodes, simulation, synthetic and public/pretrained data, with different source-to-qualification laws and legal uses. They cannot be collapsed into one homogeneous data count. The original production network may itself produce the next qualification, change the original buyer's future order probability, and congest a shared human recovery queue.

At time t the most general finite formulation is

    V_t(h) = max_{a in A_law(h)} sum_{x,y} K_t^a(x,y | h)
                    { r_t(h,a,x,y) + beta V_{t+1}(h,a,x,y) } .

Here h includes observed customer/learner/operator/rights histories, a is an approved production or learning action, y is a legally usable and timely report, and x records *joint* buyer demand, all relevant qualification outcomes, learner broadcast, recovery/operator availability, embodiment and cash states. A policy may condition on y and other actually observed items but not hidden x. The chosen action changes K as well as current r. The previous early/late information theorem holds only for an exogenous, **program-invariant** reporting law and *unchanged* conditional productive responses. It does not rank this action-dependent problem.

Continuation V already includes the increase in later qualified paid output. No extra “data option premium” may be added. The old R controller remains optional where safe, licensed and physically feasible; neither a particular training mixture nor a new embodiment is assumed mandatory. Costs and rights constraints are attached to each intervention once.

## 2. A tractable original-buyer decision embedded in the Bellman equation

To expose the active mechanism, consider one connected original-buyer cluster and two dates. At date 0, choose a productive field pilot P, a deliberate safe teleoperation/grounding program D, or an independent embodiment E. P earns a net cleared current contribution r_P; D has net current contribution r_D (possibly negative because its work uses a slot, supervised teleoperation and curation); E must cover its manufacturer, operator and deployment costs and earn an independent serviced contribution.

An initial latent cluster condition Z can affect later buyer demand and recovery. Intervention a produces a joint distribution of (Q,B,F,Y). Before date-1 dispatch, **Q** is an actually completed safe qualification gate for an additional customer recipe, and **Y** is a lawful report available before choosing how to allocate the scarce service slot. **B** indicates whether that *original customer* places an eligible order during the date-1 window, and **F** whether the shared additional-service recovery/operator path is available at execution. B and F are learned only after the allocation window; all potential original orders **and no-offer records** matter. A certified T recipe is never dispatched when Q=0. This is an explicitly defined information structure, not a claim that field controllers generally cannot recover jobs.

One incumbent R service can deliver net 2 without using the T-specific scarce recovery path. If Q=1 the firm may instead reserve the slot for approved target service T, which delivers net 4 only if B=1 and F=1, otherwise 0 because the original slot was reserved and the deadline/old R option has passed. Hence R is **always** a lawful alternative at the allocation decision, but cannot be retrospectively invoked after a reserved deadline. These values are complete net paid-service contributions, not skill points.

Define the joint *unconditional* strata

    q_a(y) = Pr_a(Q=1,Y=y),
    s_a(y) = Pr_a(Q=1,B=1,F=1,Y=y).

For q_a(y)>0, T is chosen at Q=1,Y=y iff Pr_a(B=1,F=1 | Q=1,Y=y)>1/2 (ties permit R). If q=0 the stratum contributes zero additional value.

### Proposition A — exact action-conditioned paid-data conversion identity

The optimized date-1 paid contribution is

    G_a = 2 + sum_y [4 s_a(y) - 2 q_a(y)]_+,

and the date-0 whole-program value in this two-date model, at beta=1, is

    J_a = r_a + G_a,

with E evaluated using its own independent-capacity legally feasible program. No marginal test accuracy, data volume, learner success rate, buyer order rate or operator utilization alone generally identifies G_a.

*Proof.* At Q=0 the pre-certified T choice is unavailable, so R pays 2. At Q=1,Y=y, selecting R contributes 2q_a(y) in unconditional expectation and selecting T contributes 4s_a(y). Taking their maximum adds [4s_a(y)-2q_a(y)]_+ to the always available baseline 2. Summing over report atoms gives G_a. The Bellman reward r_a is charged once; V_1 is exactly G_a. QED. This is elementary finite-policy optimization and not a claim of independent scientific novelty.

The result shows a precise conversion bottleneck: useful source data is **qualification AND actual original-buyer demand AND recovery resource availability**, weighted by the counterfactual slot reservation. A larger technical transfer probability Q need not change the value if the conditional buyer-and-worker probability remains below 1/2. As task-service menus and site interactions expand, the sufficient two-stratum moments need not remain sufficient; return to the full action-dependent K and the preceding policy-occupancy theory.

### Proposition B — sharp partial identification from separate, report-specific margins

Let m_y=Pr(Y=y), b_y=Pr(B=1,Y=y), f_y=Pr(F=1,Y=y), and q_y as defined, under **one fixed action**. Without restrictions on dependence within each report stratum,

    lower_s(y) = max{0,q_y+b_y+f_y-2m_y},
    upper_s(y) = min{q_y,b_y,f_y}.

Consequently, retaining the same r_a and lawful menu, G_a lies in the sharp interval

    2+sum_y[4 lower_s(y)-2q_y]_+
    <= G_a <=
    2+sum_y[4 upper_s(y)-2q_y]_+.

*Proof.* The three-event union bound on complements gives the lower Fréchet bound; intersection containment gives the upper. Both extrema are attainable by coupling three binary indicators inside a report stratum with the stated margins. When strata can be coupled independently, attain these extrema simultaneously; the positive-part map is nondecreasing in s. The bounds are sharp **only** for this unrestricted stratum-coupling class. A validated common learner/operator factor, physical support, or cross-site constraints can narrow them; assigning separate worst-case K to each site or investment arm would be invalid when a common cluster exposure law is imposed. QED.

This is a useful *identification protocol* rather than a second estimate of paid data value. If no original buyer no-offer/paid-settlement row exists, the production-value rank remains unidentified despite high robot task scores.

## 3. Observation-only and active-learning channels are not interchangeable

For an informative theoretical comparison, suppose the conditional law factors as

    Pr_a(z,q,b,f,y) = p(z) K_a(q,b,f | z) L_a(y | z),

with a common preassignment Z, but action-specific physical/market/recovery kernel K and permitted report kernel L. This factorization itself is a testable strong assumption; for a failure-generated report, Y and posttraining state may not be conditionally independent and the *joint* K_a(x,y) must be used.

Write G(K,L) for Proposition A evaluated under that factorization. For two lawful actions P,D, if hypothetical bridge combinations have coherent semantics,

    J_D-J_P = (r_D-r_P)
            + [G(K_D,L_D)-G(K_D,L_P)]
            + [G(K_D,L_P)-G(K_P,L_P)].

The first bracket is a **within-fixed-D-state** information effect. It is nonnegative if L_D Blackwell dominates L_P and D's legal policies can ignore information. The second bracket is a **physical/market/recovery state effect** measured under a common report channel. The breakdown changes if we bridge through (K_P,L_D) instead; it is a decomposition of one causal contrast, *not two additive data premiums*. The interaction

    I = G(K_D,L_D)-G(K_D,L_P)-G(K_P,L_D)+G(K_P,L_P)

can be positive, zero or negative, even when L_D is more informative and Q_D first-order dominates Q_P. A report and data-source intervention can be economically complementary or substitutable through demand, safety qualification and operator congestion. Hypothetical off-action bridges require feasible versions and support; they are not identified by logs of P and D alone.

### Proof of the information-only condition

If K is fixed across two legally feasible reports and L_P is a garbling of L_D, simulate L_P using L_D then follow the P-information policy. Its paid return is feasible with the D report, so G(K,L_D)>=G(K,L_P). If collecting the more accurate Y changes K, consumes an operator, changes buyer orders, qualification or legal rights, this constructed simulation is **not** the D intervention's outcome. The exogenous Blackwell argument therefore has no cross-action ranking implication. This is standard comparison-of-experiments reasoning, not a new data-scaling law.

## 4. Two exact coupled-network counterworlds (no fabricated empirical calibration)

Take Z fair in {0,1}. P (productive paid field pilot) generates current r_P=+1/2. In either world P produces Q fair independently of Z, a report Y that is an independent fair coin, an original B order iff Z=1 and a free T operator F iff Z=1. Q is *observed and audited* before date-1 allocation. Conditioned on Q=1 and uninformative Y, B&F has probability 1/2, so reserving T merely ties R. Thus G_P=2 and J_P=5/2. The hypothetical perfect Y=Z under P would make G(K_P,L_D)=5/2. This is the source-conditioned counterfactual, not an actual P signal.

D consumes -1/4 current net contribution, **always qualifies** T (Q=1), and produces a perfect report Y=Z. Both counterworlds have identical D marginal Q=1, B order probability 1/2, F free probability 1/2, and perfect Y accuracy about Z; P's whole law is identical in both. Only the *joint association between buyer demand and shared operator availability under D* differs:

| Action-conditioned law | B | F free | Y | Q |
|---|---|---|---|---|
| P in both worlds | Z | Z | fair independent coin | independent fair gate |
| D in world I | Z | Z | Z | 1 |
| D in world II | Z | 1-Z | Z | 1 |

**World I — aligned demand and recovery.** With D, Y=1 identifies the qualified target order and a free recovery path; Y=0 calls for R. G_D=3, so J_D=11/4. With P, J_P=5/2. E is stipulated to deliver a completely net 12/5 through physically *independent* embodiment, capacity and operator resources. Winner: **D, 11/4 > P, 5/2 > E, 12/5**.

**World II — recovery crowds out exactly the original buyer.** D's report is still perfect and Q still always passes, but when the buyer orders, the target operator is occupied. A T reservation can never produce accepted paid output. Thus G_D=2 and J_D=7/4. Winner: **P, 5/2 > E, 12/5 > D, 7/4**.

This is not a parameter-only perturbation: it changes the joint causal dependence structure while leaving every stipulated individual margin and reported regime accuracy fixed across the two D worlds. Reporting only Q, B, F rates and signal accuracy cannot discriminate these investment rankings. The exogenous-report calculation applied with P's K to D's perfect L would yield 9/4, which incorrectly ranks D below P even in world I.

The full bridged economic interaction is I=+1/2 in world I and I=-1/2 in world II. In world I, D's better learning and market alignment give no extra paid return under an uninformative report, but become valuable with timely Y. In world II, more technical qualification and a perfect report are stranded by the incompatible customer/operator conjunction. All numbers remain normalized synthetic quantities; E's 12/5 assumes **verified** separate capacity in the thought experiment, not an observed engineering fact.

## 5. Extension, tests against the claim, and implications for the full program

In a longer network horizon the report itself may direct the next source mixture, checkpoint broadcast, target-grounding budget, manufacturing order or customer segment. Then the response to P versus D is the *entire lawful adaptive policy* under their distinct K_t, not a one-shot G. Physical transfer can unlock a new task/service embodiment and inter-site data feedback, but that future paid production is inside the Bellman value. Cross-site shared broadcasts and coordinated operator assignment generally prevent factorization into independently qualified sites. Resource-price duals and process-flexibility/O-ring complementarities from the prior Models A/B remain available as static subproblems of each history. Neither an LP dual nor the toy moment formula certifies the full dynamic policy.

Specific falsifiers: (i) if all original-B orders are known before reserving capacity, the report margin can lose value; (ii) if an immediate safe R fallback survives a failed T reservation, the opportunity-cost term changes; (iii) if T cannot legally qualify before the decision, the proposed action is forbidden, not low-valued; (iv) if E still requires the same occupied human recovery queue, the independent-capacity E row fails; (v) if action a induces new customer orders, postselected paid episodes do not reveal its causal buyer denominator; (vi) if report law/rights or hardware change with a, bridges can be undefined. All such changes require recomputing the whole paid-production objective, not patching a generic task success percentage.

**Bounded closest prior art, checked 22 November 2026:** Farboodi, Koh and Xia, *Data-Driven Automation* (arXiv:2606.10127, posted June 8; updated June 10, 2026) already models endogenous production-generated heterogeneous data and spillovers; its §5 and Appendix B already treat future data and complementarity, so neither is claimed new here. Blackwell's experiment comparison (1951/1953) already establishes free, unaltered-state signal monotonicity. Dual control and POMDP frameworks already treat actions that influence future state and knowledge; see Mesbah (2018), https://doi.org/10.1016/j.arcontrol.2017.11.001, and Krale, Simão, Jansen (ICAPS 2023), https://doi.org/10.1609/icaps.v33i1.27197. **Candidate synthesis**, not validated novelty, is the explicit combination of legally qualified original-buyer paid receipts, source-specific data action, incomplete joint buyer/offers, shared labor recovery and embodiment opportunity inside one identified full-policy comparison.

**November 22 Models A/B gate remains OPEN.** Actual linked buyer offer/no-offer and cleared payments, approved P/D/SG/E physical comparisons, license and retention permission, conditional Q/Y/B/F state support, verified E independence, and official numerical interindustry BLS/BEA coefficients are not available. See [prospective evidence](ACTIVE_SIGNAL_PRODUCTION_EVIDENCE.md), [exact executable](active_signal_production_exact.js), [recorded result](active_signal_production_results.json), [separate rational audit](active_signal_fraction_audit.py), [student exercises](ACTIVE_SIGNAL_PRODUCTION_EXERCISES.md) and [instructor solutions](ACTIVE_SIGNAL_PRODUCTION_SOLUTIONS.md). Next: replace the partial-stage synthetic conditional law by a **validated physically feasible multi-date learner/buyer/operator joint transition and action support**; if access remains absent, develop sharp bounds for multi-site policy choices rather than falsely identifying an economic rank. Preserve theory majority through Dec 6 and final December 25, 2026 23:59 Eastern target.
