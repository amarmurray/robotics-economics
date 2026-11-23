# Coupled validation queues, production-generated renewal, and the economic value of heterogeneous learning

23 November 2026 · Continuation of *When Capabilities Become Production* and [the common-law third-cohort chapter](COMMON_LAW_ACTION_DEPENDENT_THIRD_COHORT.md).

**Status:** conditional theory, explicit proofs, and exact synthetic counterworlds. No measured robot performance, signed customer/source rights, confirmed independent embodiment capacity, approved intervention, empirical causal effect, independently verified scientific novelty, or November 22 scientific acceptance. This is the **same** source-data → qualification → resource-constrained accepted service → customer-demand feedback argument. The extension below relaxes isolated-program buyer/worker transport at the **multi-job shared queue**, rather than returning to financial contract elaboration.

## Economic question

The earlier action-dependent result made failure-origin target grounding G and recovery-origin learning K jointly affect a qualified original customer's order and worker availability; it retained a restrictive mapping from separate interventions into the joint intervention. Here two *different* program-generated validation/remediation jobs can occupy the same worker shift. When both occur, a payable qualified first service may miss its acceptance window; the **next genuine customer order** then fails to materialize. How much joint learning is economically useful, and what can the firm know from separately observed G and K histories?

The answer depends on the **joint queue-event law**, not merely separate validation-job rates or a complete pair of technical qualification scores. A sequentially observable validation signal may permit an adaptive acquisition policy, but that does not identify the missing counterfactual law.

## General dynamic production and learning environment

At date t a firm's state is
\[
 X_t=(\mathcal D_t,\mathcal B_t,\mathcal Q_t,\mathcal W_t,\mathcal L_t,\mathcal R_t,\mathcal H_t).
\]
Here \(\mathcal D_t\) is the *set of actual customer orders* with unique ids, \(\mathcal B_t\) their remaining payable authorizations, \(\mathcal Q_t\) the typed job/recovery queue with deadlines and worker minutes, \(\mathcal W_t\) available robotic/worker capacity, \(\mathcal L_t\) a provenance- and rights-aware stock of field trajectories, validation failures, successful recoveries, teleoperation, simulation, synthetic and public/pretrained inputs, \(\mathcal R_t\) qualified **complete customer production recipes** for each embodiment, and \(\mathcal H_t\) the lawfully observed decision history. These inputs are *not* interchangeable sources or human-data counts. A permitted data intervention modifies the source-to-qualification kernel and may create/clear physical jobs, change the next order process, or alter source rights. The alternatives include additional productive source evidence P, target grounding G, recovery learning K, an independently supported embodiment E, and the retained old policy R.

A lawful nonanticipative policy selects source processing, verification, dispatch, recovery and capacity allocation conditional only on \(\mathcal H_t\). Feasible dispatch must respect unique ticket/payment conservation, accepted quality, resource capacity, repair precedence, action eligibility, rights and deadline constraints. The optimized production-value recursion is
\[
 V^a_t(x)=\max_{u\in\mathcal A_a(x)}
 \left\{r_t(x,u)-c_t(x,u)
 +\beta\int V^a_{t+1}(x')\,P_a(dx'\mid x,u)\right\}. \tag{1}
\]
Only *real accepted* services generate eligible receipts. The transition kernel \(P_a\) jointly governs new buyers, queue load, validation, typed learning and future qualifications. Future data value is **already** represented by the continuation term; attaching a separate premium to the same learning outcome would count it twice.

**Controlled-kernel performance identity.** Fix a policy \(\pi\) that is feasible, measurable and identically interpretable in two regimes a and b, on a common finite-horizon state/action space, with the same initial distribution. Let \(V^{b,\pi}_{t+1}\) denote its continuation under b. Define immediate net operating receipts \(r_a^\pi,r_b^\pi\). Direct Bellman subtraction and telescoping gives
\[
 J_a(\pi)-J_b(\pi)=\sum_{t=0}^{T-1}\beta^t
 \mathbb E_{X_t\sim a,\pi}\left[
 r_a^\pi(X_t)-r_b^\pi(X_t)
 +\beta(P_a^\pi-P_b^\pi)V^{b,\pi}_{t+1}(X_t)
 \right]. \tag{2}
\]
*Proof.* Write \(V_t^{a,\pi}-V_t^{b,\pi}
=\delta r_t+\beta(P_a-P_b)V^{b,\pi}_{t+1}
+\beta P_a(V^{a,\pi}_{t+1}-V^{b,\pi}_{t+1})\); repeatedly substitute the last term and take the common initial expectation. The terminal difference is zero. QED.

Equation (2) prices changes in **customer renewal and worker backlog through a continuation-value difference**, rather than through a model-accuracy-to-dollar conversion. It is not an optimal-policy identity across disjoint action sets. With optional checkpoint retention and shared feasible old actions, \(\max_\pi J_a(\pi)\ge J_a(\pi_b^*)\), but that does not mean forced retraining, job creation or new permission requirements are free. A claim that optimally available no-cost data hurts the firm contradicts inclusion of its old feasible policies; a negative result for a fixed forced training recipe does not.

## An exact two-remediation-job, two-customer-ticket economy

Condition on the original customer's **actual failed first attempt**. The original ticket A is still unpaid and valid at t3. The inherited failure recovery was completed at t2 and produced a distinct recovery trace; G may lawfully train on the *failure-origin* trace, while K may train on the *recovery-origin* trace. We assume both source permissions are granted **only for the synthetic witness**. Validation of G creates an additional real repair job if binary \(V=1\), and validation of K creates a distinct job if \(Z=1\). No job is created if the corresponding intervention is not performed. Both jobs, if created, require one of **two** shared worker slots at t3 and must be resolved before the customer service is allowed. At t3 one accepted A service itself consumes one slot. Therefore under committed GK,
\[
 q^{GK}_3=V+Z,\qquad
 W^{GK}_3=2-V-Z,\qquad
 Y^{GK}_{A,3}=\mathbf1\{V+Z\le1\}, \tag{3}
\]
where the equality presumes GK has already qualified a complete A recipe, A remains ordered and budget-valid, and no other jobs enter this finite witness. Under G or K alone at most one validation repair exists; the A service is always feasible and accepted.

At t4 the same customer's **new and separately authorized follow-up ticket B** exists *only* if A was accepted at t3. That is,
\[
 D^a_{B,4}=Y^a_{A,3},\qquad Y^a_{B,4}=D^a_{B,4}, \tag{4}
\]
under the witness's stipulated t4 qualified capacity. A is never charged twice; B is not counted if it was never ordered. This is an explicit, falsifiable strong demand-response assumption, not a general empirical relation. G and K alone each generate total normalized contribution 3 per eligible failed ticket (2 from A, 1 from new B); both together, when a worker slot remains, generate total 5 (4 from A, 1 from B), reflecting an assumed *validated complete-recipe productivity advantage* rather than an increase in benchmark percentage. The old policy R contributes 2. The independent staffing and qualified A/B customer service required for E are assumed, not demonstrated; its fixed net program contribution is 17/4. The displayed values are normalized after stipulated equal/sunk intervention costs, not robot revenues or free real-world deployments. Real unequal costs subtract from the appropriate whole programs and can alter the ranking.

Let \(a=\Pr(V=1)\), \(b=\Pr(Z=1)\), and \(z=\Pr(V=1,Z=1)\), all conditional on the eligible failed customer cluster and lawful program support. Then
\[
 \max(0,a+b-1)\le z\le\min(a,b),\quad
 J_{GK}=5(1-z),\quad J_G=J_K=3,\quad J_R=2,\quad J_E=17/4. \tag{5}
\]
**Queue–renewal amplification proposition.** Under (3)–(4), if the accepted A contribution is m and the conditional incremental payoff of a real follow-up B is \(\beta\gamma n\), where \(\gamma=\Pr(B\text{ ordered}\mid A\text{ accepted})\) and no B arises otherwise, then
\[
 J_{GK}=(m+\beta\gamma n)(1-z),\qquad
 \frac{\partial J_{GK}}{\partial z}=-(m+\beta\gamma n). \tag{6}
\]
*Proof.* Both A and B require the same earlier slot-feasibility event \(V+Z\le1\). A produces m if it occurs; with probability \(\gamma\) conditional on that event it then generates an independently budgeted B receipt n. Taking expectations gives (6). QED. The derivative is an economic queue-congestion price **including induced genuine buyer continuation**, not a second data asset premium. If B demand also exists without A, or t4 worker capacity is constrained, (6) must be replaced with (1), not extrapolated.

## Common-law equivalence and a sharp synthetic reversal

Take four equiprobable latent cluster types 0,1,2,3 and hold \(V=1\) on 0,1 and 0 otherwise. Let \(Z=1\) on **any two** of the four types. All six choices give identical *complete* G-only and K-only observed laws: each has exactly one validation-job indicator equal to one with probability one-half, one accepted original A, and one separately paid follow-up B per cluster. Both technical complete-recipe qualifications are one in every type, including the full paired technical test. Even the individual source contributions are unchanged. But joint G/K validation-job **coincidence** is unobserved without a lawful joint intervention.

For the six coherent common laws, the overlap counts among four types are 2,1,1,1,1,0. Hence
\[
 z\in[0,1/2],\quad
 J_{GK}\in[5/2,5],\qquad J_E=17/4. \tag{7}
\]
The endpoints are **sharp within the specified common-law family**, and any intermediate z follows by mixing whole coherent type laws, rather than independently combining incompatible policy marginals. When z=0, GK produces 5 and beats E at 4.25. When z=1/2, GK produces 2.5 and E wins. There is no changed technical qualification rate or source-label aggregation to explain the reversal: it is the **new physical co-remediation queue**, followed by actual customer renewal, that reverses it.

For a commitment assigning fraction x of *independent non-interfering comparable clusters* to GK and \(1-x\) to E, if only the above ambiguity class is admitted, regrets at z=0 and z=1/2 are respectively \(3(1-x)/4\) and \(7x/4\). The conditional minimax-regret commitment is \(x=3/10\), worst regret \(21/40\). Maximin contribution instead selects E. This is not a practical investment allocation: it assumes cluster independence, feasibility of E, a known normalized contribution table, and precisely this bounded family. Neither a test percentage nor a vendor announcement establishes those premises.

**Nonanticipative adaptation is a different object.** Suppose V becomes lawfully observable *before* the firm irrevocably chooses whether to process K, with enough time to validate K and dispatch. Retaining the G-only checkpoint and omitting K when V=1 is physically feasible. The fixed information-feasible **safe** policy \(\pi_s\) processes K iff V=0 and contributes \(5(1-a)+3a=4\) when \(a=1/2\), **for every z**. If the conditional joint law z were actually known from a supported audit, the optimal post-V policy instead gives
\[
 J_{\mathrm{adapt}}(z)=\tfrac12(5)+\tfrac12\max\{3,5(1-2z)\}
 =\max\{4,5-5z\}. \tag{8}
\]
*Proof.* On V=0 at most the K validation job can occur, so choose K, worth 5. On V=1, skipping K earns 3; processing K earns 5 if Z=0 and zero if Z=1. Since \(\Pr(Z=1\mid V=1)=2z\), choose the larger conditional expectation. QED. The rule choosing the second term based on z **cannot be implemented from separated G/K arm logs alone**. It requires identification or an explicit subjective decision rule. In this witness E=4.25 dominates the uniformly safe policy's contribution 4, but it does not dominate GK when z is small. With no lawful opportunity to observe V before K commitment, (8) is not available.

The optional intervention's *potentially free dataset* and its *capacity-consuming realization* must not be conflated. If K's traces can simply be stored and ignored with no resource or legal consequence, the old G policy remains feasible and value cannot decline. Actual K validation creates a job under Z=1; forcing it can destroy accepted service and downstream demand.

## What is and is not identified

The two separate complete arm histories identify a=b=1/2 in this witness but do not identify \(z=\Pr(VZ)\). No amount of additional isolated G-only or K-only observations distinguishes the six common worlds. Even paired **technical recipe** success does not measure paired **validation remediation** in the same worker cluster. Formally, let \(\pi\) be a common distribution of physical potential histories, \(A\pi=b\) the lawfully identified arm moments, and \(\mathcal P\) the nonempty common-law feasible polytope; the sharp program-specific payoff set is \(\{v_a^\top\pi:\pi\in\mathcal P\}\). The interval (7) uses the special structural assumptions (3)–(4). Without cross-regime invariance of job generation, source qualifications, worker duration or buyer response, (7) is **not** a sharp bound for realistic GK interventions: adding arbitrary unobserved cross-action effects generally widens the common-law set.

A lawful prospective cluster-level paired validation audit may identify z **only if** the same-unit G and K validation flags are invariant to their joint activation and recording the flags is physically and legally permitted. Otherwise the economically relevant target is the full GK regime's **joint original order, generated jobs, actual worker slots, accepted A service, and induced B order** under authorized whole-regime assignment. A sequential audit of K choice *after* a predeclared V signal needs positivity within each V history and documented acquisition rights. Randomizing workers independently while they share repair queues violates the cluster interference boundary. Conditioning analysis only on observed invoices or on queues that already cleared induces selection and hides precisely the economic losses the model prices.

This is a constructive identification agenda, not permission to run such an audit. Signed source rights, lawful treatment support, real buyer payment/quality and nonorder logs, verified queue timing, and independently staffed E evidence are unavailable.

## Alternative assumptions, negative tests, and broader economic consequences

1. **No follow-up causality:** if new B buyers renew independently of accepted A, the queue penalty loses the \(\beta\gamma n\) continuation term. The previous bound on contemporaneous paid service alone cannot be treated as the full dynamic result.
2. **Extra worker, lower queue density, or staggered K acquisition:** with three t3 slots, both repair jobs can clear and an A service can still occur. The overlap effect in (5) vanishes under the witness's exact service-time assumptions. This is a physical-resource-price comparative static, not a universal learning law.
3. **Unqualified K or incompatible checkpoints:** if either source fails complete-recipe validation, change the payoff table and admissible policies. Pairing benchmark scores does not yield the stated 5 contribution. An AND-qualified arm-and-mobile production recipe can flip the sign of source overlap; the service topology, not the data origin alone, determines that sign.
4. **Customer interference or variable budgets:** if A/B customers share an authorization, (4) is invalid; count B only when it has its own approved budget. If program assignments affect one another through shared worker pools or demonstration demand, cluster at the true interference unit and re-solve the common-law game.
5. **Contingent job duration and adaptive dispatch:** with stochastic job lengths, multiple embodiments, priorities, and paid service deadlines, let \(Q_{t+1}=[Q_t+J_t-S_t]_+\) componentwise subject to worker slots, and use (1) to choose recovery, production and training jointly. A forecast of technical progress alone does not supply the law of this queue.
6. **Rights, compute and acquisition cost:** enforce feasible data provenance and actual per-policy compute/curation/worker commitments; paid continuation stays in (1) rather than being charged as a separate data premium. The entire economic return to K can change sign despite a positive technical effect.
7. **Option to acquire a new embodiment:** independently staffed E is not a scalar backup unless its procurement, validation, integration, customer acceptance, deployment time and right to operate are demonstrated. The example's E number is deliberately assumed, never evidence.

The most consequential comparative static is that **data transfer changes both future production capability and the feasibility/demand distribution of production itself**. A firm with high technical source reuse may destroy economic value by co-locating learning interventions in a shared recovery bottleneck; conversely a spare worker slot or earlier actionable validation signal can transform the same two datasets into productive complements. This fits the larger recursive-firm agenda: each deployment changes source mixture, queue, end-market orders and future allocation, so investment selection requires the common controlled production law, not a one-direction accuracy learning curve.

## Closest foundations and contribution status

- Farboodi, Koh and Xia, [*Data-Driven Automation*, NBER Working Paper 35320 (June 2026)](https://www.nber.org/papers/w35320), already treat task-specific heterogeneous data, endogenous accumulation, spillovers and future production/automation. Nothing here claims invention of those mechanisms or its Appendix B complementarity.
- Han, [*Optimal Dynamic Treatment Regimes and Partial Welfare Ordering*](https://doi.org/10.1080/01621459.2023.2238941) (JASA, 2023), gives established partial-ordering/linear-program approaches for counterfactual dynamic policy value. This chapter's common-law identified set and regret exercise are applications, not a new causal-identification theorem.
- Finite-horizon Markov decision processes, renewal/abandonment queues and Fréchet bounds are standard foundations. The claimed research *candidate synthesis* is the economically integrated source provenance → qualified customer recipe → shared learning/recovery jobs → accepted paid service → next genuine customer demand mapping, with explicit restrictions and falsification. Independently established novelty remains **unverified**.

**Precise next proof gap.** Permit both programs to modify the *number and duration* of remediation jobs, and permit B demand to depend on elapsed delay even when A is eventually completed. Establish a common-law dynamic Bellman/LP bound over complete ticket/queue histories without transporting single-program flags into GK; characterize which lawful sequential joint measurements close the decision-relevant identification gap. Then place quantified end-market IO coefficients only when actual authoritative numeric primary cells are available. This is a continuation of the same argument, not another artificially numbered checkpoint.

**Reproduction:** [exact code](joint_queue_buyer_feedback_exact.js), [results](joint_queue_buyer_feedback_results.json), [replication](JOINT_QUEUE_BUYER_REPLICATION.md), [prospective evidence protocol](JOINT_QUEUE_BUYER_EVIDENCE.md), [student exercises](JOINT_QUEUE_BUYER_EXERCISES.md), [separate solutions](JOINT_QUEUE_BUYER_SOLUTIONS.md). All reported numerical values are exact rational statements about six synthetic common-law worlds; no full-repository CI or empirical robotics intervention is claimed.
