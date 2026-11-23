# Sequential action support and economic data value after paid service

23 November 2026 · Continuation of *When Capabilities Become Production* and [FOUR_DATE_ECONOMIC_INFLUENCE_CLOSURE.md](FOUR_DATE_ECONOMIC_INFLUENCE_CLOSURE.md). **November 22 scientific gate remains OPEN.** All worked amounts are synthetic normalized contributions, not observed robotics revenue, calibrated transfer or an independent novelty finding.

## The question that survives the fixed-policy four-date result

The preceding chapter found a late original C order and recovery clearance jointly worth money after an earlier t3 worker-blocked history. But it assumed a *fixed* t3 dispatch and recovery policy. In a recursive robotics firm the t3 action is itself selected using original offers, earlier accepted production, learning qualification, rights and the shared queue. It may change t4 customer demand, repairs and even what gets recorded. Can we identify and price an *adaptive* source-learning P / licensed target-grounding G / independent-embodiment E / retained R production policy without pretending old-policy R responses describe unsupported G interventions?

**Result:** Under lawful support of the *entire program*, sequential support of each targeted feasible action in each reachable history, consistency, sequential exchangeability (ideally prospective randomization) and complete or independently sampled **joint original offers and worker outcomes**, a finite-horizon dynamic g-formula identifies policy-specific qualified paid contribution. The calculation integrates the program's own mediated history distribution; it never fixes G's post-service buyers at the R distribution. But neither a full history under the formerly selected t3 policy nor even separately known marginals for an untried recovery action identifies its value when later orders and worker availability are dependent. A common-law counterworld proves a program-ranking reversal despite a *monotone* buyer response to accepted early service.

These are finite forms of established longitudinal causal inference, decision theory and Fréchet inequalities. The useful contribution to this research is the choice of economically weighted estimands, physical resource conservation, original-buyer reporting and a support-aware P/G/E/R intervention comparison—not a novel g-formula.

## 1. Economic environment, physical chronology and distinct data channels

At t0 choose an investment program z from {R,P,G,E}, retaining all feasible old recipes and their optional deployment policies. z changes rights, embodied capacity, source acquisition and which target recipes can qualify; G does not automatically confer training or cross-site reuse rights. At t1–t2, qualified paid production and heterogeneous evidence can update the model and create worker repair jobs. At t3, the firm sees an admissible history
\[
h_3=(x,z,\mathcal Q_3,\mathcal B_3,\mathcal O_3,\mathcal J_3,\mathcal D_3,\mathcal R_3),
\]
including baseline/site conditions x, qualified *joint* recipes \(\mathcal Q_3\), original buyer offers/no-offers \(\mathcal O_3\), remaining lifetime buyer budgets \(\mathcal B_3\), outstanding shared-worker jobs \(\mathcal J_3\), retained evidence \(\mathcal D_3\), and signed use/dispatch rights \(\mathcal R_3\). The notation \(\mathcal B_3\) is buyer budget, not a count of successful technical trials. Data sources remain separate: production successes, failures/recoveries, teleoperation, simulation, synthetic and public/pretrained inputs each has its own qualification and permission map.

With one exclusive worker, a feasible t3 action is at most one of: serve a qualified original A order, serve a qualified original C order, work on the currently occupied repair, carry out eligible preventive maintenance, or idle. Serving an absent/unqualified order, assigning a blocked worker to a second job, or exceeding a customer's remaining payable units is prohibited. A paid t3 acceptance y3 may generate a **new** t3-after-service repair claim j3 and a quality signal to the buyer. A recovery action can improve (or worsen) subsequent worker availability without generating accepted t3 production. At t4, **new** original customer offers d4 and actual worker clearance l4 arise after this entire t3 history, not before. t4 dispatch acts on the offers, budget, new repair state and current qualified recipes.

Thus the causal sequence includes:
\[
z\to h_3\to a_3\to (y_3,j_3)\to h_4=(d_4,l_4,\ldots)\to a_4\to y_4.
\]
The joint conditional law of d4 and l4 is part of the economic technology. They may share unobserved shocks. Demand may respond to actual earlier accepted service and quality; it need not be exogenous or independent of the support queue.

Use captured contribution at actual settlement dates, net of wages, compute, validation, hardware, rights and incremental recovery once. If accepted output already records missed production, do not add a second lost-output penalty. A data update changes future feasible production and the transition kernels, not an independent additive "data premium." A benchmark percentage is not a dollar valuation.

## 2. Proposition: identified value of a sequential supported production policy

Let \(\pi=(\pi_3,\pi_4)\) be a nonanticipative stochastic decision rule choosing eligible actions from \(\mathcal A_3(h_3)\) and \(\mathcal A_4(h_4)\). In program z let:
- \(k_z(h_3\mid x)\) be the **z-specific** t1–t3 preaction history law, including accepted earlier service, qualification and buyer responses;
- \(q_z(y_3,j_3\mid h_3,a_3)\) be the joint t3 paid acceptance and newly owed repair law;
- \(k_z(h_4\mid h_3,a_3,y_3,j_3)\) be the joint original t4 buyer offer, queue/clearance and qualification law;
- \(q_z(y_4\mid h_4,a_4)\) be the settled t4 accepted-service law.

Conditional costs can be included in each period reward \(r_2,r_3,r_4\). For a finite state/action network and fixed discount \(\beta\), the value is

\[
\begin{aligned}
V_z(\pi)=\mathbb E_x\sum_{h_3,a_3,y_3,j_3,h_4,a_4,y_4}
&k_z(h_3\mid x)\pi_3(a_3\mid h_3)q_z(y_3,j_3\mid h_3,a_3)\\
&\cdot k_z(h_4\mid h_3,a_3,y_3,j_3)
\pi_4(a_4\mid h_4)q_z(y_4\mid h_4,a_4)\\
&\cdot\left[r_2(h_3)+r_3(h_3,a_3,y_3,j_3)
+\beta r_4(h_4,a_4,y_4)\right]-K_z.
\end{aligned}
\]

K_z is an incremental program cost not already charged in the period rewards. Define \(J_{4,z}(h_4)=\max_{a_4\in\mathcal A_4(h_4)}\mathbb E[r_4\mid h_4,a_4,z]\) and
\[
Q_{3,z}(h_3,a_3)=\mathbb E[r_3+\beta J_{4,z}(H_4)\mid h_3,a_3,z].
\]
Then the optimized t3 action is \(\arg\max_{a_3\in\mathcal A_3(h_3)}Q_{3,z}(h_3,a_3)\), provided the relevant conditional kernels are identified or bounded and the timing of information is respected. The dependence of \(k_z(h_4\mid\cdot)\) on *actual accepted y3* incorporates buyer response, rather than treating y3 as a pre-treatment adjustment variable.

**Identification conditions.** (i) Consistency of the licensed action and its versioned technical production recipe, including report timing; (ii) program-level assignment/selection exchangeability with positive lawful z support for the relevant original cluster population; (iii) sequential exchangeability of t3/t4 action choices given *all action-relevant predecision* histories, or prospective approved randomization; (iv) positive action support only for histories reachable under the target rule; (v) measurement of original offers inclusive of zero orders and rejected attempts, verified worker occupation, qualification, actual paid service and real resource costs, with known noninformative observation sampling or a justified observation model; (vi) no omitted interference beyond the registered buyer/worker/training cluster. If reporting itself changes buyer behavior, it is an *action* with its own response kernel, not harmless observation.

**Proof.** Under consistency and sequential exchangeability, each supported conditional action-specific outcome law equals the corresponding interventional conditional law. By iterated conditional expectation, substituting the target \(\pi_3,\pi_4\) action kernels for the observed decision kernels and leaving the *z-specific*, postaction transition kernels intact gives the displayed formula. For a fixed feasible menu, backward induction gives the Bellman recursion. No step factors \(k_z(d_4,l_4\mid\cdot)\) into marginal demand and clearance, no step conditions the entire program contrast on a post-z risk set, and no R-to-G transition equality is used. Violating support or exchangeability invalidates the corresponding substitution, irrespective of sample size.

A prospective probability-weighted alternative, for a fixed and independently qualified t4 terminal service rule with verified outcomes, is
\[
V_z(\pi)=\mathbb E\left[
\frac{\mathbf1\{Z=z\}}{p_z(X)}
\frac{\pi_3(A_3\mid H_3)}{e_z(A_3\mid H_3)}
\left\{r_2+r_3+\beta\frac{M_4}{\eta(H_3,A_3,Y_3,J_3,L_4)}r_4^{\pi}(D_4,L_4,\ldots)\right\}
\right]-K_z.
\]
Here e_z is the lawful t3 assignment probability and M4 is an original-offer audit selected with known positive inclusion rate \(\eta\), **independently of the unreported offer conditional on its allowed observed inputs**. The expression assumes r2 and r3 are completely observed and r4^{\pi} is a valid supported/qualified potential t4 settlement rule, not an imagined untested recipe. If alternative t4 dispatch is not technically/causally supported, another t4 action factor and outcome qualification are required; if an audit is selected based on an unseen D4 or changes behavior, the identity fails. Simply conditioning on observed paid invoices cannot replace original-offer auditing.

## 3. Economic influence and sharp support-aware restrictions

Only a history-specific action that can change *optimized downstream accepted contribution* requires new response information for a particular finite policy comparison. For a terminal state with one qualified remaining C unit and one worker, terminal gross contribution is \(vD_4L_4\). Given action- and history-specific marginals \(d=\Pr(D_4=1\mid h_3,a_3,z)\) and \(\ell=\Pr(L_4=1\mid h_3,a_3,z)\), but no lawful joint reports, the exact Fréchet interval is
\[
v\max(0,d+\ell-1)\le \mathbb E[vD_4L_4\mid h_3,a_3,z]\le v\min(d,\ell).
\]
Both endpoints can arise under coherent common shocks; treating the marginals as independent silently chooses an interior coupling. If a worker is *physically unable* to clear before t4, or the buyer has no payable budget, this terminal component is a structural zero and an original-offer audit need not be funded **for that fixed terminal menu**. Earlier blocked states can still matter if repairs clear in a later period, as proved in the preceding chapter. For an enlarged menu or adaptive rule, repeat the backward influence calculation. No universal minimal-covariate theorem is claimed.

A support-aware certificate works with a common set \(\mathcal L\) of lawful causal scenario laws and compares
\[
\underline{\Delta}_{\pi,\pi'}=\inf_{p\in\mathcal L}\{V_\pi(p)-V_{\pi'}(p)\}.
\]
If \(\underline\Delta>0\), the ranking is robust even when neither value is point identified. Requiring an adversary to select **independent incompatible laws** for competing policies gives misleading bounds. Free optional access to another source cannot lower optimized value when the old action and corpus remain feasible; a costly, forced training or service-changing grounding program can lose.

## 4. Worked counterworld: accepted service raises demand but untried recovery can still reverse the ranking

Take a t0 G investment that has qualified both an installed arm A and a mobile C by t3. At t2 the G program delivers **one accepted paid C unit** worth 1; its one-time cost is 1/2, so the common pre-t3 net contribution is 1/2. The C buyer has exactly one additional payable unit remaining; A has exactly one. At t3 a worker is free and an original A order is present; there is no t3 C original order. The firm chooses one of two exclusive uses of the worker:

S: serve the A order (one accepted unit pays 1/2), possibly initiating a new repair after service, or
M: use the shift for a preventive recovery/maintenance intervention (no t3 accepted paid unit), possibly changing t4 worker availability.

At t4 a **new** original C order D4 earns 4 only if D4=1, the worker is free L4=1, the C recipe remains qualified, and its second and last budget unit is available. Set \(\beta=1\) for this finite example, and let U,V be independent fair latent bits unknown to the t3 dispatcher. The fully recorded historical G policy is S. Both causal worlds agree under S:
\[
D_4(S)=U\lor V,\qquad L_4(S)=1-U.
\]
The untried M action has
\[
D_4(M)=U,\quad
L_4(M)=\begin{cases}U&\text{world aligned},\\ 1-U&\text{world misaligned}.\end{cases}
\]
These are functions of exogenous shocks and t3 action, not clairvoyant choices conditioned on future t4 orders. In **both worlds and on every atom**, \(D_4(S)\ge D_4(M)\): accepting earlier A service *weakly raises C's subsequent original buyer demand*. The directions of the worker-clearing responses nevertheless differ after M. Each world has the same *complete* observed S history; even the **hypothetically known** M-specific separate D4 and L4 marginals equal 1/2 in both.

Because \(\Pr(D_4(S)=L_4(S)=1)=1/4\),
\[
V_G(S)=\tfrac12+\tfrac12+4(\tfrac14)=2.
\]
For M the joint event has probability 1/2 in the aligned world, and 0 in the misaligned world:
\[
V_G(M\mid +)=\tfrac12+4(\tfrac12)=\tfrac52,\qquad
V_G(M\mid -)=\tfrac12.
\]
Within the *hypothetically certified* M marginal class \(d=\ell=1/2\), the sharp bounds are \(V_G(M)\in[1/2,5/2]\); **the marginal certification itself cannot be inferred from S-only histories**. Without that additional information, bounds would be wider.

Preserve the same lawful outside R/P/E programs across worlds, with stipulated values \(V_R=19/10,\ V_P=21/10,\ V_E=11/5\) and a genuinely independent E robot/worker slot. The observed G policy S is worth 2, below E=11/5. Yet in the aligned world the G/M program is worth 5/2 and wins; in the misaligned world E wins. Neither an apparently favorable monotone early-service effect on *demand* nor complete S original-offer coverage identifies the missing action-specific later buyer × worker coincidence. This is a stronger failure of information *support* than a missing t4 marginal under a fixed action.

For a t0 nonanticipative commitment across independent clusters under the specified two-world or fixed-M-marginal ambiguity set, choose M-under-G on fraction x and E on 1−x. Because E strictly dominates G/S, P and R in both worlds, these exhaust the undominated commitments in this witness. Regrets are
\[
\mathcal R_+(x)=\tfrac3{10}(1-x),\qquad
\mathcal R_-(x)=\tfrac{17}{10}x.
\]
Equalizing gives \(x_G=3/20,\ x_E=17/20,\ \sup_\theta\mathcal R_\theta=51/200\). Maximin instead chooses E, whose guaranteed value is 11/5. The firm **cannot select the world after seeing U,V or the t4 outcomes**; learning from a legitimately assigned M cohort can improve future cohorts. The numbers are normalized hypothetical units. [Exact enumerator](sequential_adaptive_policy_exact.js) and [results](sequential_adaptive_policy_results.json).

## 5. Evidence that would actually change the decision

A realizable future study would first need signed G source retention/target training/validation/deployment rights and approval for its intervention. It would separately assign R/P/G/E at a network level closed under common training and support. Within G histories in which S and M are both physically qualified, safe and legal, t3 action variation must be prospectively assigned with recorded probability **before** any t4 original buyer or clearance outcome. A randomized, nonbehavior-changing audit must register t4 original C order **and** actual worker-free status jointly, including no order, rejected order and an unresolved repair; retain the entire original t3 A/C order and buyer budget registry; link receipts, case type, quality and new job times. If M cannot be lawfully assigned, report the uncertainty rather than manufacturing M outcomes by extrapolating R or S.

If technical experiments independently verify an action-specific terminal accepted-service recipe and customer cap, the cheapest value-relevant new statistic for this fixed two-action example is the within-G, within-action joint \(\Pr(D_4=L_4=1)\), not all downstream information indiscriminately. For a real adaptive fleet, further t3 histories, alternative t4 allocations and learner updates enlarge the influence closure. Design measurements from that fixed, rights-admissible action menu and confirm whether matched qualified accepted units—not benchmark scores—improve.

**Empirical status.** No lawful G/S–M action comparison, original-buyer joint panel, verified E independent worker pool, signed cross-site data rights or official numerical interindustry coefficients is present. No public vendor announcement substitutes for these observations. This note changes the endogenous *action-and-customer response* information structure, not merely a numerical parameter. It remains a conditional standard-method construction, not calibrated fleet economics or independently verified novelty.

## 6. Prior art, limitations and the next proof obligation

Robins' longitudinal g-formula and sequential exchangeability are antecedents, as summarized by [Naimi, Cole and Kennedy, *An Introduction to G Methods*, published 2016](https://doi.org/10.1093/ije/dyw323) and [Hernán and Robins, *Causal Inference: What If*, time-varying treatments](https://www.hsph.harvard.edu/miguel-hernan/causal-inference-book/). [Guo, Perković and Rotnitzky, *Variable elimination, graph reduction and the efficient g-formula*, published 18 November 2022](https://doi.org/10.1093/biomet/asac062), address eliminating uninformative variables under their specified DAG assumptions; our economic-influence closure is not asserted to be a new general theorem. Standard Fréchet bounds and minimax-regret rules do the remaining work. [Farboodi, Koh and Xia, *Data-Driven Automation*](https://www.nber.org/papers/w35320) already values future production-generated data and data complementarity. This work adds a physically defined P/G/E/R policy target with endogenous original-buyer, resource and legal support distinctions; it does not claim priority over those general ideas.

The next proof gap is **economically sufficient, legally observable longitudinal state compression** when multiple t3 dispatch and recovery histories *also generate new training data* that changes t4 qualification across both embodiments. Identify conditions for aggregating histories without collapsing different original-buyer/worker response kernels, then compare source learning, target grounding and an independent new embodiment under matched cash and support. This is a continuation of the same integrated argument, not a new free-standing question. November 29/December 6 scientific gates and December 25, 2026, 23:59 Eastern remain unchanged.
