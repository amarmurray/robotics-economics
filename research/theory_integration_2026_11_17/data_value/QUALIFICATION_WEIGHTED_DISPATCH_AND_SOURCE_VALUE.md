# Qualification-weighted dispatch: target prediction is not the production decision

**20 November 2026 Eastern; continuation of *When Capabilities Become Production*.** This extends the same X (additional source data), G (target grounding), E (changed embodiment), and R (retained qualified controller) comparison. It resolves a specific simplifying premise in [QUALIFICATION_GATE_AND_DATA_VALUE.md](QUALIFICATION_GATE_AND_DATA_VALUE.md): its majority-vote policy is Bayes-optimal for predicting the customer regime, but need **not** optimize *qualified, accepted and paid customer production* when separately signed recipe outcomes differ. The preceding chapter carefully describes that formula as a **fixed selected policy**, and its common-reliability result remains valid under its declared assumptions. We do not retroactively describe it as the unconstrained production optimum.

## One joint economic environment

The original buyer's latent service regime θ is 0 or 1 with equal prior probability. Source program X provides three task-relevant signals S_i=θ⊕E_i. Conditional on θ, the exchangeable error vector has a law indexed by t, with one-way error 1/4 and every pair's joint error 1/16. The probability of a *particular* vector with k errors is

| k | 0 | 1 | 2 | 3 |
|---|---:|---:|---:|---:|
| g_k(t) | 7/16−t | 1/8+t | 1/16−t | t |

where 0≤t≤1/16. The law is identical conditional on either customer regime and preserves all one- and two-way error distributions. This is a specified inference experiment, **not a robot training law**, and varying t is not adding free data to a fixed experiment.

Assume two separately physically admissible whole-network specialist service recipes A (regime 0) and B (regime 1), each with a matched signed dispatch and operator/buyer boundary. A correctly selected A qualifies, is accepted and earns the stipulated incremental 10 units over fallback R with conditional probability r_A=1/4; a correctly selected B does so with r_B=3/4. A wrong-regime recipe generates no incremental accepted paid service; the fully signed, feasible fallback R still earns 2. The paid service contribution on a successful match remains 12, as in the preceding chapter. These r values are **hypothetical full-service success rates**, including joint technical qualification, physical permission, original-customer acceptance and payment—not task prediction accuracies or observed hardware reliability. X and G each have the previous 1/4 complete-program cost; the net from baseline R after cost is 7/4. A separately signed E retains the previously stipulated net value 10.

G produces one matched target report with symmetric regime accuracy 7/8; the same A/B whole-service response table is assumed for G for this comparison. Source- and grounding-induced changes to controller, response rates, buyer demand, physical menu, fallback or operator usage would require a new joint experimental policy table. **No customer or robot evidence currently licenses those equal-response transports.** Only admissible actions are compared, and old R remains available if the signed failure path genuinely permits it.

## Proposition: optimal dispatch uses *conditional paid-service yield*, not majority accuracy

Let s be a signal vector containing k ones. Since θ is equally likely,
P(θ=0,S=s)=g_k/2 and P(θ=1,S=s)=g_(3−k)/2.
Choosing A contributes paid incremental service with joint mass r_A g_k/2, whereas B contributes r_B g_(3−k)/2. Thus the production-optimal signed conditional dispatch selects A exactly when

    r_A g_k(t) >= r_B g_(3-k)(t),

with ties immaterial. When the signed complete service yields or operator costs differ more generally, replace the two products with the **conditional optimized captured original-customer contribution** for each physically allowed recipe and resource state. Maximizing posterior label correctness is optimal only under an appropriate symmetry/equal-increment condition. This is standard Bayes risk/expected-utility decision theory, applied to the existing production menu.

The resulting X qualification-and-paid-service probability is

    q_X(t) = (1/2) sum_(k=0)^3 C(3,k) max{(1/4)g_k(t), (3/4)g_(3-k)(t)}.

For 0≤t≤1/16, k=0 always chooses A, k=2 and k=3 choose B. The contested reports are k=1 (two zero-votes, one one-vote): choosing the *minority* B is economically optimal when

    (3/4)(1/16−t) > (1/4)(1/8+t), i.e. t < 1/64.

Inserting the maximum yields the exact continuous piecewise expression

    q_X(t) = 55/128 − t/2,       0 ≤ t ≤ 1/64;
             13/32 + t,         1/64 ≤ t ≤ 1/16.

The proof is the four-case finite Bayes action maximization. The minimum is q_X(1/64)=27/64 and maximum is q_X(1/16)=15/32; both are attainable, so the conditional pairwise-only bounds are **sharp**. By contrast, the three-signal *accuracy-optimal* majority rule has accuracy p_X(t)=13/16+2t, strictly increasing with t; its paid-service success is only (r_A+r_B)p_X/2 =13/32+t. At t=0, accuracy-majority creates 13/32 qualified services, while optimized dispatch creates 55/128; conditional on the three split reports where zeros win 2–1, B is better because its relative *production* qualification advantage exceeds the posterior odds. At t=1/64, the two tie; above it majority is also economically optimal.

**Consequential negative comparative-static:** from t=0 to 1/64, technical majority accuracy rises (13/16 to 27/32), yet the *optimized* qualified-service probability falls (55/128 to 27/64). It is not negative transfer from adding optional free data. The two t-indexed experiments are not ordered by an assumed Blackwell refinement; their third-order error dependence changes. The mistake would be to equate higher binary-prediction accuracy with higher productive optional capacity when customer-specific qualification yields differ.

## Same buyer: partial identification, grounding, embodiment, and no double count

For the fixed costs and R, J_X(t)=7/4+10 q_X(t). Therefore its sharp identified set from all pairwise signal moments but unknown t is [191/32,103/16]. G's signed report is followed according to the report: since B/A conditional yield ratio 3 is below the posterior likelihood ratio 7, G's optimal signed net is J_G=7/4+10(7/16)=49/8. Consequently J_X−J_G ranges sharply over **[−5/32,5/16]**, crossing zero at t=1/32. The source X majority-only ranking would understate q_X in the low-t part of the identified set. Source predictive accuracy and even exact pairwise qualification information cannot substitute for the real success-response table.

Crucially **E retains its already stipulated net 10**: both J_X≤103/16 and J_G=49/8 are below E. Hence the full portfolio's optimum is E for all t, and even perfect t information has *zero gross portfolio value*. We retain that genuine negative conclusion rather than changing E's price to produce an artificial new investment reversal. Within an *already committed X-only signed program* whose report-dispatch rule can be modified, suppose t is equally likely to be 0 or 1/16. An audit of t **before dispatch-rule precommitment** has conditional gross value

    10[(q_X(0)+q_X(1/16))/2 − q_X(1/32)]
    = 10[(115/256) − (7/16)] = 15/128.

Under no audit the optimal policy is chosen using the mixture law (equivalent to t=1/32), **not** by averaging t-contingent optimal rules. This 15/128 is not an incremental return to add atop an E investment: with freely available E=10 the global investment-choice audit value remains zero. Any nonzero audit cost further reduces net audit value.

The conditional formula already accounts for physically qualified original service, retained R and program cost once. Endogenous future data/continuation is not a second premium. Free optional extra information that merely enlarges the observation sigma-field while preserving a feasible old policy **cannot lower** optimized production, because the decision maker can ignore it. A forced new training recipe, changed joint signal law or added collection cost does not satisfy that premise.

## General original-network production formulation

For actual programs a∈{X,G,E,R}, signed actions d, evidence/report y, original order/market θ, joint qualification Q, and physical/human/scarce-resource state h, the right decision is

    d*(y,h) ∈ argmax_{d ∈ P_signed(y,h)}
      E[V_original_paid(d,Q,θ,h) | y, a, assignment and history],

where V_original_paid includes accepted/refunded receipts, capture, variable costs, resource feasibility, alternative manual service, qualified fallback and any correctly discounted endogenous learning continuation *once*. Report-likelihood calibration must condition on the **whole learner/controller, customer and operator cluster**, not assume independence of Q from y. Where production V is an LP, existing dual resource-price certificates provide a within-active-basis interpretation of scarce operator/robot time; changed active sets require reoptimization, not a fixed shadow-price extrapolation. A flexible E changes P_signed as well as the qualification map.

Thus the necessary empirical link is **joint source/report/true demand × separately signed recipe-by-report completed accepted paid outcomes**, not a stand-alone signal benchmark score. The previous calibration-gate common-r result is a valid nested special case. No field X/G/E ranking is identified without signed buyer/operator evidence.

## Prior work and limitations

This is finite Bayesian action optimization and sharp partial identification, not an original decision-theory theorem. Asymmetric posterior loss thresholds are textbook, e.g. Casella and Berger *Statistical Inference* (2002) §§8.2–8.3 and the independently published proof at https://statproofbook.github.io/P/bc-thr (2026-10-17). Blackwell informativeness/value of information is prior theory. Farboodi–Koh–Xia, *Data-Driven Automation* (https://arxiv.org/abs/2606.10127) §5 and Appendix B **already** price generated future data and discuss source complements. This note identifies a missing calibration/dispatch dependency in the continuing original-customer model, not independently verified scientific novelty.

Exact integer [source](weighted_qualified_dispatch.js) enumerates **all 256 binary dispatch policies** for each of 17 t-grid points (4,352 policy comparisons), checks unchanging one/two-way error moments and verifies the analytic formulas. Its [stored record](weighted_qualified_dispatch_results.json) is a scoped consistency test, **not** proof or a field experiment. Independent Python Fraction spot checks were performed for t∈{0,1/64,1/32,1/16}. [Prospective evidence design](QUALIFICATION_WEIGHTED_DISPATCH_PROSPECTIVE.md), [separate exercises](QUALIFICATION_WEIGHTED_DISPATCH_EXERCISES.md) and [solutions](QUALIFICATION_WEIGHTED_DISPATCH_SOLUTIONS.md) preserve interpretability. No customer receipts, source learner training, physical certification, episode manifest, causal policy effect, official BEA numerical interindustry matrix, whole repository CI or external scientific review was established. November 22 Models A/B scientific gate remains **OPEN**. Theory majority through December 6; December 25, 2026 23:59 America/New_York final target unchanged.
