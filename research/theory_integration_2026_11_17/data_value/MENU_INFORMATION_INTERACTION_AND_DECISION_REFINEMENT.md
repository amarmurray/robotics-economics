# Economic menu–information interaction and lawful decision refinement

**21–22 November 2026; continuation of *When Capabilities Become Production* and the November 22 Models A/B argument. Scientific acceptance remains OPEN.**

## The question within the existing theory

The previous [economic continuation quotient](ECONOMIC_CONTINUATION_QUOTIENT_AND_DEMAND_SIGNAL.md) showed that an otherwise accurate summary of licensed and paid events may throw away an offered buyer order, an available learned recipe, or an operator constraint and thereby reverse the SG (source data + grounding) versus E (new embodiment) comparison. The immediate constructive question is **when an additional source-trained qualified production option makes target information more economically useful, and when it makes that information less useful**. This is not a claim about the sign of neural-network transfer. It concerns optimized *finally accepted and paid* qualified customer production, conditional on a fixed lawful action menu and customer distribution. It supplies an implementable backward decision-refinement test and a counterexample to assuming that source training and grounding always complement one another.

The larger finite-horizon program remains

\[
J_a=\sup_{\pi\in\Pi_a}\mathbb E_a\!\left[\sum_{t=0}^{H-1}r_a(h_t,u_t,\xi_{t+1})\right],\quad a\in\{R,S,G,SG,E\}.
\]

The state includes learner/checkpoint, robot embodiment, original customer demand, accepted/settled service and refunds, shared robot/operator availability, qualifications, failure/recovery, future learned services and source-specific rights/expiry. Field successes *and failures*, licensed teleoperation, simulation/synthetic inputs, and public/pretrained inputs enter through different lawful interventions and conditional learning/qualification maps. One optimization already values permitted production-generated future data through future actions and receipts; **never add a second data premium**. The old controller remains a feasible option when that is physically and legally true.

## Proposition 1 — the sign of productive capability × demand information is not fixed

Consider one dispatch stage with a fixed original-buyer state \(z\in Z\) and prior \(p_z>0\), one scarce operator/robot slot, and an action \(u\) that commits capacity to one qualified customer recipe. Let \(w_u(z)\) denote **the entire conditional continuation net paid-production value** of taking \(u\): allowed successful service, refunds and operator costs, plus optimized subsequent learning and paid work, counted exactly once. In this proposition, the underlying \(p\) and \(w_u(z)\) are held invariant across source and information interventions, and the source intervention changes only a **nested lawful menu** \(A_0\subseteq A_1\). This is a deliberately restrictive, empirically testable specialization; real source/grounding interventions can also change future kernels, demand, rights or the monetary opportunity.

Let \(Y\) be a costless, lawful buyer/target signal, observed before commitment. Define

\[
V(A,Y)=\sum_y P(y)\max_{u\in A}\sum_z P(z\mid y)w_u(z),\qquad
V(A,\varnothing)=\max_{u\in A}\sum_z p_z w_u(z).
\]

Any independent fixed acquisition costs are subtracted **once** from program net value, not from every counterfactual service. Write \(D(y)\) for the gain from menu expansion \(A_0\to A_1\) *conditional on signal \(y\)* and \(D(\varnothing)\) for the gain without the signal. Then the exact economic interaction is

\[
\mathcal I_{S,Y}
=V(A_1,Y)-V(A_1,\varnothing)-V(A_0,Y)+V(A_0,\varnothing)
=\sum_y P(y)D(y)-D(\varnothing).
\tag{1}
\]

**Proof.** Expand the four optimized values and group the two source-menu increments. The same law of total probability gives the right-hand equality. Each source increment is nonnegative by menu inclusion, and each information increment is nonnegative by the option to ignore the signal. **Their difference need not have either sign**. Under pure fixed-cost additivity, costs cancel from the mixed difference; costs do affect which total investment is optimal. The result requires no assumption that the learning maps are exponential, rational or additive.

For a *fully revealing* buyer signal \(Y=z\), \(\mathcal I_{S,Y}>0\) exactly when the **expected ex-post gain from newly available qualified recipes exceeds their ex-ante gain before observing demand**. The reverse strict inequality gives substitution. This is a necessary-and-sufficient statement under the fixed-\(p\), fixed-\(w\), common-menu specialization, not a field certificate or a general sign theorem for recursive robot firms.

For a fixed menu, a costless signal that Blackwell-dominates another cannot decrease optimized value; that standard information ordering does **not** order the *incremental value of information between two menus*. A more universal source-trained controller or new embodiment may substitute for demand information by succeeding across order types without dispatch adaptation.

## Two explicit counterexamples with retained old production

Let there be two equally likely original-buyer order types A and B. A normalized payoff is a hypothetical **finally paid net contribution conditional on that order and recipe**, not a benchmark percentage. The old action may legally reserve the robot slot for A, earning zero if no A order arrives. All portfolios allow idling. The source-enabled menu retains every old action.

| Synthetic program | Qualified reservation options | No buyer signal | Buyer signal |
|---|---|---:|---:|
| Positive example: old R | idle; A yields (1,0) | 1/2 | 1/2 |
| Positive example: source S | old R; learned B yields (0,1) | 1/2 | 1 |
| Negative example: old R | idle; A yields (1,0); B yields (0,1) | 1/2 | 1 |
| Negative example: source S | old R; learned generalist yields (3/4,3/4) | 3/4 | 1 |

Each ordered pair is net contribution in states (A,B). In the positive world, \(\mathcal I_{S,Y}=+1/2\): new customer-specific qualification makes a demand report valuable even though all old recipes stay available. In the negative world, \(\mathcal I_{S,Y}=-1/4\): a reliable generalist recipe is itself useful under *unknown* demand and partly replaces the value of a report. Technical data accessibility is optional and never lowers gross optimized value in either world.

These are different lawful qualification environments, not a single fitted parameter change. The absence of a positive interaction in the second case is **not** negative technical transfer. It is an economic substitution between production flexibility and information. If a pure target-report intervention costs 0.05, source acquisition/training costs 0.10 and an embodiment that supplies an uninformed universal 3/4-paid option costs 0.10, the positive-world net comparison is SG=0.85, E=0.65, R=0.50 (the latter two do not buy the report). The numbers are purely illustrative. A real grounding intervention also changes robot alignment, policy success, qualification and possibly source reuse; then equation (1) alone is insufficient.

## Proposition 2 — exact decision-loss test for a hidden buyer distinction

At one stage, suppose the physical/legal menu \(A\) is genuinely common across full histories \(h_z\) aggregated into a reported state \(s\), with positive conditional weights \(p(z\mid s)\). Let \(Q(z,u)\) be the true **full-information conditional optimized continuation** after committing to \(u\), with subsequent decision dates once again able to observe their normal lawful histories. A controller allowed to condition on \(z\) obtains \(\sum_zp_z\max_{u\in A}Q(z,u)\). A controller forced to choose one current action from \(s\) obtains \(\max_{u\in A}\sum_zp_zQ(z,u)\). Therefore its exact one-stage information loss is

\[
L(s)=\sum_zp_z\max_{u\in A}Q(z,u)-\max_{u\in A}\sum_zp_zQ(z,u)\ge0.
\tag{2}
\]

For finite \(A,Z\) and strictly positive \(p_z\), **\(L(s)=0\) if and only if the sets of continuation-optimal actions across the histories have a nonempty common intersection**.

**Proof.** For any fixed action, the statewise maximum is at least its payoff; summing and then maximizing establishes nonnegativity. If there is a common maximizer, it attains both terms. Conversely, choose a maximizer of the pooled expectation. If equality holds, the nonnegative gaps between each statewise optimum and this action sum to zero with strictly positive weights; hence every gap is zero and this action belongs to every statewise argmax set.

This is a *decision-specific* test, weaker than controlled Markov lumpability. The old R in the positive example has a common optimum (reserve A, even when B appears, where it ties idling); the learned S menu has disjoint statewise optimal actions (reserve A versus reserve B). Therefore a coarsening that is **decision sufficient for R becomes decision insufficient after source-generated qualification**. A policy-value or state quotient accepted on an old controller cannot automatically be transported to SG or a new embodiment. In the positive example \(L_R=0\) and \(L_S=1/2\).

Important qualification: the formula permits full information at *later* dates after this one common decision. If a deployed dashboard hides information at every future decision, equation (2) by itself is **not** a total-horizon error identity. Neither is actionwise logged performance enough to learn all \(Q\). If full histories in a proposed cell have **different lawful menus**, a common action must lie in their menu intersection; an empty intersection makes the proposed uniform policy infeasible. Unsupported or unsafe controls cannot be labeled as merely uncertain.

## Backward lawful state refinement: what to audit

For each *program* separately, begin at the terminal date with a single continuation class. Working backward over legally reachable full learner/operator/buyer/checkpoint/rights/settlement histories, split a cell whenever:

1. physical/contractual **action menus** differ, including old fallback, new learned recipes, shared-operator reservation and the embodiment's physical action choices;
2. an action has a different conditional expected **complete net paid return** (not task benchmark or service acceptance alone); or
3. an action has a different probability distribution over the **next already-refined continuation classes**.

Under exactly validated equality, this reproduces the sufficient economic quotient theorem by backward Bellman induction (standard finite controlled bisimulation). For a **specific** optimized decision, the common-argmax test (2) can justify a coarser *policy* partition even when a full transition quotient cannot be certified. Such a coarser partition is not suitable for evaluating counterfactual training, alternate programs, new customer demand or embodiment menus without another audit.

Prioritize splits that can change the paid SG/E decision: buyer's *offered* order and its observation time; qualifying full recipes versus isolated skills; robot/operator slot and failure rescue; learner and embodiment lineage; legal provenance and expiry; rights-linked paid episode joint events; finally cleared customer payment; and future new service reachability. This is a proposed *audit of lawful exposure*, not a fabricated empirical quotient. For pooled learners, the full history must include shared updates and overlapping original-customer assignments; independent site averages cannot supply missing action-conditional kernels.

## What would distinguish the explanation empirically?

Under physically approved matched programs on the same original buyers, compare (i) source-enlarged *qualified menu* and same buyer order/report, (ii) **ex-post** optimized accepted-paid service conditional on that order, (iii) **ex-ante** commitment without that information under valid observability restrictions, and (iv) an embodiment alternative under the same operator and customer accounting. Linked order non-arrivals, safe/qualified action menus, source rights, checkpoints, training/teleop/curation costs, failure/recovery, shared learners and ultimately cleared receipts must all be recorded. Equation (1) predicts the sign from the difference between the ex-post and ex-ante source opportunity increments only **if** the proposed action-conditional payoffs and demand law remain invariant; violations must be separately estimated or bounded. No unapproved controller should be run to generate missing positivity.

For recursive Model B, replace the one-stage payoff \(w\) by a validated full-horizon \(Q\) over endogenous production-generated data, future customer choices, licensed reuse and new embodiments. If actual transition and demand effects are unidentified, retain the existing supported-policy lower floors / lawful Bellman-resource upper envelopes and report **unknown** rather than transporting the synthetic sign. Model A's fixed qualified recipes may be audited earlier.

**Closest prior foundations:** Blackwell's comparison of experiments / Bayes value of information; Givan, Dean & Greig (2003), *Equivalence notions and model minimization in Markov decision processes*, DOI [10.1016/S0004-3702(02)00376-4](https://doi.org/10.1016/S0004-3702(02)00376-4); Castro, Panangaden & Precup (2009), [MDP/POMDP equivalence](https://ijcai.org/proceedings/2009/276); DDA, Farboodi–Koh–Xia (2026), [arXiv:2606.10127](https://arxiv.org/abs/2606.10127), whose §5 already changes production in response to future data and whose Appendix B considers complementary data aggregation. The novelty candidate, still unverified, is a **robotic qualified-service/source-rights/market-demand economic composition**, not the max-expectation inequality, finite-state aggregation or endogenous data principle.

**Reproduction:** [exact integer-tick Node model](menu_information_refinement.js), [record](menu_information_refinement_results.json), [independent rational checker](menu_information_refinement_independent.py), [prospective evidence](MENU_INFORMATION_REFINEMENT_EVIDENCE.md), [exercises](MENU_INFORMATION_EXERCISES.md), [separate solutions](MENU_INFORMATION_SOLUTIONS.md). The small enumeration checks signs of 50 nested-menu pairs (not all possible robot production models). No actual original-customer data, lawful SG/E field trial, verified joint qualification kernels, official numerical BEA/BLS input-output coefficients, independent novelty assessment or full repository CI was obtained. **November 22 acceptance remains OPEN; theory priority through December 6; final deadline December 25, 2026 23:59 Eastern.**
