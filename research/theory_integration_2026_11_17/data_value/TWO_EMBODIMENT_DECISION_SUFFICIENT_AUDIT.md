# Joint customer-service occupancy as the sufficient economic audit: two embodiments

23 November 2026 | Continuation of When Capabilities Become Production, not a new standalone estimand. The November 22 Models A/B science gate remains OPEN. All numerical quantities below are exact **synthetic normalized contribution**, not observed robotics economics or established scientific novelty.

## Question continued from sequential paid demand and recovery

The preceding SEQUENTIAL_PAID_DEMAND_RECOVERY_AND_AUDITS.md identified why a t2 report may improve t3 production after a repair clears and why the joint t3 original-buyer-demand/recovery event, not its margins, determines a fixed G service's value. The outstanding problem is **which evidence is sufficient to choose among productive source-data learning P, licensed target grounding G, a retained old policy R and an independently supported new embodiment E** when multiple customers have original orders, qualification arrives late, one worker is shared, and reports can be selected.

**New constructive result.** For a *specified* finite, rights-feasible, nonanticipative policy menu, it is unnecessary to recover every latent robot state to rank policies: the required information is the collection of **policy-payoff contrasts on reachable complete histories**, including original buyer offers, joint service eligibility, and shared-resource congestion. A linear-algebra certificate tests whether an audit identifies these contrasts; a common-law polytope and minimax-regret calculation handle the rest without imputing unsupported target-grounding outcomes. A two-embodiment construction gives an exact economically minimal *additional* joint statistic under an explicit invariant-law specialization. Without such intervention-support or invariance, the statistic under R cannot be transported to G.

This is a finite-history application of established linear identification, action-value and robust decision mathematics. Its role in the integrated theory is to expose exactly what original buyer/worker/qualification evidence buys an investment decision, not to name a new universal transfer law.

## 1. Longitudinal physical environment and feasible interventions

At t1 a completed accepted unit consumes one unit of its original buyer's remaining budget. At t2 a lawful report may arrive before a program and a physically eligible training/validation dispatch; qualification and new repair jobs arrive only at their specified times. For a single shared eligible worker and two inherited jobs, with one completed at t1 and at most one at t2,

L_2=(J_{A1}+J_{X1}-1)_+,
L_3=(L_2-\mu_2)_+ + J_{2,a,u},
0<=\mu_2<=min(1,L_2).

A job created after the t2 clearing opportunity is not cleared retroactively. Both original A and C orders at t3 are defined **before deployment dispatch**, including unserved, rejected and no-order outcomes. Each buyer has one unit of purchasing budget across accepted t1/t2/t3 service. Technical qualification Q of an accepted-service recipe is distinct from the paid event. R preserves already qualified policies; P learns from field/success/recovery data under allowed rights; G uses licensed target grounding and can retain the old fallback; E installs an independently eligible machine and support resource. All program costs, lead times, source rights, model versions, coordination and accepted quality enter once in the full history.

For a complete primitive/potential-outcome world \omega and a deterministic lawful contingent policy \pi (including its program and later decisions), let g_\pi(\omega) be captured, discounted, **actually accepted paid** contribution net of its incremental costs. The complete expectation V_\pi(\mu)=\sum_\omega \mu_\omega g_\pi(\omega) is linear in a *single* nonnegative causal population law \mu. The optimized firm benchmark is max_\pi V_\pi(\mu), but a real controller must choose its contingent policy before seeing the hidden world. In particular, terminal original orders can be used to choose t3 dispatch only if lawfully revealed by t3; an unknown population association cannot be treated as a pre-t0 signal.

## 2. Finite-policy economic identification theorem (standard linear algebra)

Fix finite admissible policies \Pi and a common finite support \Omega that already enforces customer budgets, shared-worker accounting, versioned qualification, rights and reporting order. Suppose legally observable moments impose B\mu=b, \mu>=0, with the normalization row in B. Define the feasible common-law set \mathcal M. For each pair of policies let d_{\pi,\kappa}=g_\pi-g_\kappa.

**Proposition.** If B contains a strictly positive feasible law on the declared support, the contrast V_\pi-V_\kappa is point identified for all \mu in \mathcal M **if and only if** d_{\pi,\kappa} is in the row span of B. If no strict interior exists, restrict to the relative support/affine hull of feasible laws before applying the criterion. Even if a contrast is not point identified, an investment ranking is robust whenever min_{\mu in \mathcal M} d^T\mu > 0 (or max d^T\mu <0). All extrema are finite linear programs in one joint law. The same law must be used for every policy.

**Proof.** If d=B^T\lambda, then d^T\mu=\lambda^T b for every admissible \mu. Conversely, if d is not in row(B), the fundamental theorem of linear algebra supplies \nu in ker(B) with d^T\nu not zero. Strict positivity of \mu_0 permits small both-sided perturbations \mu_0+\varepsilon\nu and \mu_0-\varepsilon\nu which remain probability laws, satisfy B\mu=b, and change the contrast. For robust sign, optimizing the linear functional over the same feasible compact polytope proves the ranking certificate. QED.

For an ex ante randomized policy x in the simplex over \Pi, robust **regret**, rather than an oracle allocation across worlds, is

R(x)=max_{\mu in \mathcal M} [max_{\pi in \Pi} g_\pi^T\mu-\sum_\kappa x_\kappa g_\kappa^T\mu]
    =max_{\pi in \Pi} max_{\mu in \mathcal M} (g_\pi-\sum_\kappa x_\kappa g_\kappa)^T\mu.

The equality follows because \Pi is finite. It gives a finite family of joint-law linear-program separation checks. **Do not** independently choose a worst transition kernel at every date if one latent causal regime couples those dates and policies: that rectangularization can describe a world in \mathcal M that cannot exist. For information arriving within a program, enumerate history-measurable contingent policies, not hindsight-dependent terminal choices.

**Audit design implication.** For a fixed menu, an audit need only distinguish payoff-relevant histories enough to recover relevant contrast rows; it need not observe every technical latent variable. This is *decision sufficiency*, not full causal identification and not a license to assume an unobserved arm has the same response law. The smallest feasible audit additionally depends on legal recording rights, actual program support, and when the evidence becomes available.

## 3. Exact two-embodiment construction: why pairwise tables lose the investment choice

Use the same after-t2 physical accounting but specialize to **one terminal t3 shift**. Fixed arm A and mobile embodiment C each have one original buyer offering at most one unit. Let A,C in {0,1} indicate their original eligible t3 offers, W in {0,1} indicate the common recovery worker and dispatch capacity are free after t2. Both embodiments exist in the installed fleet, but only one buyer can be served by the shared qualified slot. One accepted unit contributes 2. The separately financed E option provides independently staffed and qualified mobile-C service alongside the existing shared A cell; its *entire incremental capital/coverage cost* is 3/4. There is no double sale to C. The example makes W policy-invariant and introduces no new t2 service incident **only to isolate the missing original-buyer/worker association**; the preceding longitudinal chapter allows them to be program-dependent.

At t2, P uses previously admissible productive-source data to qualify the shared mobile-C recipe with an independently validated Bernoulli Q whose probability is 1/2; Q is observed before t3 dispatch. P uses an already scheduled production exposure and has zero *incremental* cost in this witness (not an assumption about real field data). G spends 1/8 on independently lawful offline target grounding and qualifies shared C with certainty, while keeping the old arm and skip policy. R retains qualified A but not C. E supplies a new mobile machine and a genuinely independent operator; qualification is verified independently. All four programs are selected at t0 before the joint buyer/recovery regime is known; at t3 the firm accepts the better feasible qualified order.

Their exact payoff functions on a common A,C,W,Q world are

g_R=2WA,
g_P=2W[A \vee (QC)],
g_G=2W(A\vee C)-1/8,
g_E=2C+2WA-3/4.

The max/union operator here is the *physically conserved one-slot service*, not a technical score. Programs may retain their old safe dispatch if a source or grounding update does not qualify. E may serve C when the shared worker is unavailable, and may serve A and C together when W=1. G's 1/8 and E's 3/4 are costs deducted once, not data premiums.

Suppose the verified univariate and **every pairwise** (A,C), (A,W), (C,W) law are fair and independent, and Q is an independent fair indicator. Let the unobserved joint occupancy be

t=Pr(A=1,C=1,W=1),    0<=t<=1/4.

Inclusion-exclusion and independence of Q give the exact values

V_R=1/2,
V_P=3/4-t,
V_G=7/8-2t,
V_E=3/4.

For example, P adds 2 Pr(Q=1) Pr(W=1,C=1,A=0)=Pr(WC)-Pr(WAC)=1/4-t to its base 1/2. G obtains 2[Pr(WA)+Pr(WC)-t]-1/8=7/8-2t. E receives a mobile-C unit independently and a shared A unit when available: 2Pr(C)+2Pr(WA)-3/4=3/4.

All possible t in [0,1/4] are attainable with the stipulated marginal and pairwise tables: take a convex mixture of the four equally weighted even-parity A,C,W states {000,011,101,110} and the four equally weighted odd-parity states {001,010,100,111}. Q is fair and independent in both. Both worlds preserve every one- and two-dimensional buyer/worker table; each is one coherent physically feasible history law with a terminal worker slot, not separately imagined program-specific draws.

At t=0, R=1/2, P=3/4, G=7/8, E=3/4, so **G wins**. At t=1/4, R=1/2, P=1/2, G=3/8, E=3/4, so **E wins**. Individual buyer rates, worker availability, pairwise associations and P technical qualification are identical. **The missing three-way original buyer/worker coincidence reverses the actual P/G/E investment ranking.**

The contrast G-E=1/8-2t is **not** in the row space generated by normalization and one- and two-body moments: the parity worlds furnish the explicit nullspace witness. Adding the **one scalar** matched original-offer/worker triple moment E[ACW]=t identifies the full ranking in this *restricted invariant-law menu*. The signal is economic occupancy, not a universal fleet transfer coefficient or a claim that ordinary R invoice data reveal it.

## 4. Robust choice, information timing, and the option to retain old policies

Throughout t in [0,1/4], E>=P and E>R. It suffices to compare G and E. If the t0 allocator commits probability x to G and 1-x to E without an informative early signal, worst regret comes from one of the two parity endpoints:

R(x)=max{(1-x)/8, 3x/8}.

The global minimax-regret solution equalizes the two endpoints:

x*=1/4,  R(x*)=3/32.

The maximin (worst paid production) policy is E alone: worst net value E=3/4, whereas G can fall to 3/8 and P to 1/2. Neither decision is the unattainable oracle choosing G in the low-overlap world and E in the high-overlap world. Free optional data availability never requires replacing an already-qualified R recipe; negative observed transfer under a forced training recipe cannot reverse feasible-menu inclusion.

Consider an **explicitly hypothetical lawful** report about which of the two endpoint population regimes holds, received *before t0 program commitment*. Under an equal prior and perfect regime report, the expected best value is (7/8+3/4)/2=13/16, compared with uninformed E=3/4. Gross information value is 1/16. With symmetric correct-classification probability a, choosing G after a "low-overlap" report has posterior incremental contribution

a(1/8)+(1-a)(-3/8)=(4a-3)/8.

A rational allocator therefore does **not** act on that report until accuracy exceeds 3/4. The ex ante gross value of this report is max(0,(4a-3)/16), under the stated binary prior and action menu. A report delivered only after irreversible t0 investment cannot re-select the program and has zero *program-choice* information value here. It could still affect a distinct lawful later decision if that menu were expanded, as the previous sequential chapter demonstrated. These are theoretical Bayes calculations, not field-validated signal accuracies.

## 5. Reporting selection and the causal-support boundary

Under R, accepted invoices are generated only when WA=1. Their aggregate paid incidence is 1/4 in both parity worlds. Observed R invoices consequently cannot recover t. A lawful independently randomized original-order/repair audit sampled with known strictly positive probability eta, conditionally independent of A,C,W given recorded pre-audit history and assigned action, recovers the corresponding observed-arm moment using E[M ACW/eta]=E[ACW]. An audit must record *original A and C orders even when unserved*, actual worker occupancy and clearance, complete episode/quality and rights context, and refusal/no-order denominators. The audit must be conducted on supported assigned cohorts and its timing reported; terminal audit results do not retrospectively authorize a t0 choice.

**Critical boundary.** The two-embodiment formulas use the same (A,C,W) terminal law across R/P/G/E. This is a transparent *exclusion/invariance assumption*, not something the old R log establishes. To see the failure, fix R's full (A,C,W) population history to even parity in two causal worlds. Let G leave that joint distribution unchanged in one world but induce odd parity in the other through t2 public service/repair demand feedback. The complete R original-offer/worker registry and all R payments match, and G's individual and pairwise A/C/W rates can match; nevertheless V_G is 7/8 versus 3/8. Both are physically possible program potential-outcome laws if t2 repair arrivals and buyer choices may respond to G. No R audit alone identifies the G effect without supported G service-response observations or an externally justified exclusion.

Thus there are TWO distinct audit questions: (i) what joint moment would be sufficient **conditional on a justified common response law**, and (ii) what G-specific lawful assignment, transport assumption, or sensitivity bound justifies treating that moment as relevant under G at all? The second cannot be solved by adding more R-only reporting fields, larger technical benchmarks or nonlinear extrapolation.

A prospective physically approved test should randomize entire connected buyer/robot/worker clusters to permitted P/G/E/R programs, or explicitly defend partial-law restrictions if no G assignment is permitted. Record preoffer demand, t1 budget depletion and quality, t2 original orders, recovery job onset/clearance and severity, t2 Q updates/version/release, t3 original buyer offers including non-service, buyer acceptance/payments, counterfactual old-policy feasibility and genuine E independent staffing. Use matched held-out source/target tasks to identify technical transfer separately. Protect consent and data-lineage rights. Distinguish field successes, recoveries, teleop, simulator, synthetic, and public/pretrained input, and charge all true data processing costs. The detailed unpopulated protocol is in TWO_EMBODIMENT_JOINT_AUDIT_EVIDENCE.md.

## 6. Relationship to established work, tests and remaining proof gap

Dynamic-programming continuation and positive-part dispatch come from standard stochastic control; linear-row-space identification and LP duality are standard; the paired-history question belongs to causal identification/transport, not independent qualification-rate multiplication. Robins's longitudinal g-formula and exchangeability/positivity, Manski's treatment-regret work, and the older DDA future-data and complementary aggregation mechanisms are closest foundations, not claims of our novelty.

- Robins (1986), longitudinal causal treatment and g-formula; see https://doi.org/10.1016/0270-0255(86)90088-6 and Hernan/Robins, What If (2025).
- Manski (2004), Statistical Treatment Rules for Heterogeneous Populations, Econometrica 72(4), 1221-1246, https://doi.org/10.1111/j.1468-0262.2004.00530.x.
- Farboodi, Koh and Xia, Data-Driven Automation (2026), https://www.nber.org/papers/w35320; its §5 already values future data and Appendix B already treats complementary aggregation.
- BEA, official input-output concepts and numerical publication route, https://www.bea.gov/itable/input-output. The official landing page was checked 23 November; **no actual numerical interindustry coefficient was acquired** in this tranche and no vendor announcement is used as its proxy.

The exact source two_embodiment_joint_audit_exact.js enumerates 17 eighth-state parity mixtures, all three pairwise moments, four program values and the minimax mixture; TWO_EMBODIMENT_JOINT_AUDIT_RESULTS.json records the V8 execution. These exact calculations check the **illustrative** algebra, not the general theorem, real economic returns or scientific novelty.

**Next connected proof gap:** replace this counterexample's program-invariant terminal A/C/W with a legally supportable **joint G-specific t2 accepted-quality, qualification and repair/late-original-order kernel**, while maintaining two embodiments, budget conservation and selected reporting. Identify the smallest prospective supported *full-program* original-buyer/worker audit that separates economically relevant responses under nonrectangular common regimes; compute robust P/G/E policy bounds without treating R-to-G invariance as observed. Actual matched paid cohorts, signed rights, independent E staffing/qualification and an official numerical BEA/BLS interindustry spine are still missing. Nov22 science OPEN; majority theory through Dec6; December25 2026 23:59 Eastern target unchanged.
