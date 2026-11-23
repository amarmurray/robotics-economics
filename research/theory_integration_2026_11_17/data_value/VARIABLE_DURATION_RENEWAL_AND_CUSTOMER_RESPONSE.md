# Variable remediation durations, service deadlines, and learning-generated customer demand

23 November 2026 · Continuation of *When Capabilities Become Production*, directly extending [the two-job renewal and shared queue result](JOINT_QUEUE_BUYER_FEEDBACK.md).

**Status.** Conditional production economics, constructive proofs and exact synthetic common-law worlds. The November 22 scientific gate remains **OPEN**. No measured robotics customer payments, validated cross-source duration law, signed rights, confirmed independent embodiment staffing or originality finding is asserted.

## The same economic question, with actual time

A robot firm's failure-origin trajectories (G) and completed-recovery traces (K) may each improve a complete customer production recipe. Real validation work on each source can also create physical remediation, occupying the *same* worker that would otherwise execute accepted customer orders. The earlier chapter modeled binary one-slot jobs and an all-or-nothing later buyer renewal. Here G and K induce jobs of heterogeneous duration; some service is accepted *late but still paid*, while a new original buyer renewal requires earlier completion. The policy may postpone K until observing G's completed job duration. The question is whether the isolated histories, full paid accepted-service definition, and legal observation timing are sufficient to choose G, K, G+K, further production P or a separately staffed new embodiment E.

Let a finite controlled state record outstanding uniquely identified original customer orders and budgets, the typed release/deadline/remaining processing times of each genuine remediation job, available robot and worker time, complete qualified recipes by embodiment, legally admissible provenance-tagged source stocks, and observed history. The firm may allocate worker and robot capacity to recovery, validation, training, and accepted paid dispatch. More field failures, successful recoveries, teleoperation, simulator rollouts, synthetic and pretrained data are distinct inputs with different source-rights and learning kernels. The source-to-joint-qualification transition and next original-buyer order process are **action-dependent**.

For finite horizon and a legally/physically admissible nonanticipative policy \(\pi\), write

\[
J_a(\pi)=\mathbb E_a^\pi\!\left[\sum_{t=0}^{T}\beta^t
 \bigl(\text{receipts from accepted uniquely budgeted customer services at }t -
 \text{actual validation, operator, compute and training costs at }t\bigr)\right].
\tag{1}
\]

The learning contribution is *inside* future accepted receipts and the Bellman continuation: do not add a duplicate data asset premium. The old trained checkpoint and old dispatch remain selectable when a new source is truly freely optional, but activating K below consumes real capacity and may reduce value. Different programs can have different feasible action menus and treatment kernels; the common-policy controlled-kernel identity from the preceding chapter applies only on their shared admissible policies.

**Timed queue and payment lemma.** In an admissible cluster with one worker, no other arrivals, available validation inputs from time 0, mandatory completion of both real validation repairs before dispatching A, and no idle time, let G validation duration be \(g\), K duration under joint activation be \(\kappa\), and accepted A service itself require \(s\) minutes. The earliest feasible A completion is \(C_A=g+\kappa+s\). If A remains a unique authorized original ticket and is payable for complete qualified service by deadline \(d_A\), with a separately authorized new B ticket arriving with conditional probability \(\gamma(C_A)\) after accepted A and accepted B capacity genuinely available later, then

\[
J_{GK}=\mathbb E\left[
\mathbf1\{Q_{GK}=1,\ C_A\le d_A\}
\bigl(m(C_A)+\beta n\gamma(C_A)\bigr)\right]-c_{GK}.
\tag{2}
\]

Here \(m(C_A)\) is actual A contribution conditional on acceptance, not a benchmark percentage; \(n\) is the contribution from *one* accepted and newly authorized B. **Proof:** under the stated precedence, serial conservation gives the earliest completion time. If accepted A is absent there is no induced B; conditional on accepted A, B has one independent authorization and contributes its own single expectation. Add actual intervention costs once. Equation (2) is an elementary dynamic production identity. It does not assert that no-idle serial precedence is optimal when validation is optional, jobs have different release dates, or several accepted orders compete. Those situations require the common controlled-kernel optimization over schedules.

Equation (2) already distinguishes a technical gain from its economic usefulness: higher Q can coexist with a worse accepted-payable probability if learned recipes generate longer recovery queues, while an earlier result may change follow-up demand.

## Exact shared-worker, three-tier deadline witness

Condition on a real failed first attempt, a still-unpaid original A ticket, and a completed inherited recovery that produced the K trace. Assume both G and K usage rights, separately validated complete A recipes, unchanged customer eligibility, and all relevant costs already netted or stipulated equal. In the four equally likely hypothetical latent types, isolated G repair minutes \(g=(1,1,2,2)\), isolated K repair minutes \(k\in\{1,2\}\) with exactly two long K types, and a fully qualified A service needs one additional worker minute. G alone and K alone finish A by minute 3, each generating normalized contribution 2 from accepted A plus 1 from a genuinely separate B order, for \(J_G=J_K=3\). The old R and productive P comparators are each 2 in this deliberately fixed witness. The independently staffed and qualified new embodiment E yields 13/4, **assumed**, not established.

If both sources are committed, a complete GK recipe commands contribution 4 from A if completed by minute 4. A *new* B order worth 1 is authorized only if A completes by minute 3; if A finishes at minute 4 it is paid but produces no B, and if A finishes later both receipts are zero. No A receipt or buyer is replicated. Let \(L_G=\mathbf1\{g=2\}\), \(L_K=\mathbf1\{k=2\}\) and \(z=\Pr(L_G=L_K=1)\). Each long marginal is 1/2; common-law Fréchet bounds imply \(0\le z\le1/2\). The complete G-only and K-only histories (including job duration, original A accepted payments and B renewal), and paired *technical* qualification, are invariant across the six placements of long K.

**Proposition 1: payoff slope across deadlines.** Under the additional **neutral cross-program duration** restriction \(g^{GK}=g\), \(k^{GK}=k\), the joint program yields

\[
\begin{aligned}
\Pr(C_A=3)&=\Pr(g=k=1)=z,\\
\Pr(C_A=4)&=1-2z,\qquad \Pr(C_A=5)=z,\\
J^{N}_{GK}&=5z+4(1-2z)=4-3z.
\tag{3}
\end{aligned}
\]

The sharp interval is \([5/2,4]\). Thus the neutral committed GK beats E=13/4 at \(z<1/4\), ties at \(z=1/4\), loses above it. The six worlds give z=0,1/4,1/2; probabilistic mixtures of complete coherent worlds fill the interval. **Proof:** an A receipt is lost only at \(C_A=5\); B is newly ordered only at \(C_A=3\). With half-long marginals, both-short mass equals both-long mass z and mixed mass equals \(1-2z\). Substitution proves (3) and sharpness. QED.

**Important negative result.** Without B, \(J^N_{GK}=4(1-z)\), with derivative -4 with respect to z. The *real induced B option* adds \(\Pr(C_A=3)=z\), yielding derivative -3. Thus a second deadline tier can **attenuate**, rather than mechanically amplify, a change in the congestion-overlap penalty. Moving correlation toward both-long also moves mass toward both-short, producing early renewal. The prior one-threshold queue–renewal amplification result remains correct under its own assumptions; it is *not* a universal sign theorem for customer-demand feedback. The economically relevant object is the full vector of duration/deadline/renewal coincidences, not a universal scalar shadow price.

**Proposition 2: source interaction makes isolated data nonidentifying even with equal technical Q.** The cross-program K job duration \(\kappa(g,k)\) can respond causally to G's activation. Restrict it, for this demonstration, to the physically explicit envelope

\[
\max(1,k-1)\ \le\ \kappa(g,k)\ \le\
k+\mathbf1\{g=2\},\qquad g^{GK}=g.
\tag{4}
\]

Both isolated programs are *identical* across three possible whole-program laws:

- Neutral: \(\kappa=k\), value \(4-3z\).
- Cross-source shortening: \(\kappa=\max(1,k-1)\), value \(9/2\) for every z.
- Cross-source elongation: \(\kappa=k+\mathbf1\{g=2\}\), value \(2+z\).

The three laws preserve every isolated G/K history and paired technical complete-recipe qualification, but assign different **physical** joint-job durations and customer renewal. Across the explicitly restricted common-law family (4) and the six possible joint g/k arrangements, the sharp committed GK interval is \([2,9/2]\). Since the payable receipt in (2) is weakly decreasing in completion time, the pointwise longest and shortest \(\kappa\) choices attain the respective lower and upper value envelopes; varying the coherent shared latent law supplies the endpoints. **Proof:** For shortening, the pairs (g,k)=(1,1),(1,2),(2,1),(2,2) pay respectively (5,5,4,4), giving 9/2. For elongation, they pay (5,4,0,0), giving \(5z+4(1/2-z)=2+z\). For neutral, Proposition 1 applies. Under (4), these pointwise min/max policies bound each other law's receipts; the long/short overlap z ranges from 0 to 1/2, so the global minimum is 2 and maximum 9/2. Each endpoint is generated by one physically coherent common law, not by independently selecting incompatible program marginals. QED.

Without the structural duration envelope, joint-action rights, qualification, offer timing and worker conservation, the narrower numerical interval is **not** an empirical bound. Historical G-only and K-only records cannot establish (4). Conversely, a signed, genuinely paired whole-program audit could reveal shortening or elongation even though a separately tested model score remains identical.

## A constructive decision when the full joint law remains unknown

**Proposition 3: an observation-timed safe learning policy.** Suppose G's validation duration \(g\) is recorded *before the irreversible K validation choice*, G-only remains safely selectable, and choosing K only after \(g=1\) never changes G's already finished job or makes K take more than 2 minutes, while K consumes no irrevocable resources if skipped. Let \(\pi_s\) run K **iff g=1**, otherwise continue G alone. Then, under the stated whole-program family,

\[
J(\pi_s)\ge \tfrac12(4)+\tfrac12(3)=\tfrac72
   > J_E=\tfrac{13}4.
\tag{5}
\]

In the neutral and elongation laws \(J(\pi_s)=7/2+z\); in the shortening law \(J(\pi_s)=4\). **Proof:** With g=1 and K chosen, the worst allowed joint K job takes 2 minutes, so accepted A finishes by minute 4 and earns at least 4; the possible renewed B can only add. With g=2 and K skipped, G alone finishes by minute 3 and earns 3. Both g groups have probability 1/2. The stated identities follow by enumeration. QED.

This is a *real policy-level partial ordering* within the synthetic assumptions: the firm can prefer information-conditioned grounding/recovery to the assumed E even though the best committed GK value is not identified. It is not an oracle choosing z or an unconditional claim that training on both sources helps. A legitimate delay before observing g, a G-induced change to K duration beyond 2 when g=1, changed A/B demand, worker interference between clusters, rights denial, different costs, or missed acquisition deadline can invalidate (5). If extra K curation or worker costs are not already netted, the robust preference survives only if their incremental expected whole-program costs stay strictly below the lower margin 1/4, assuming no other benefit/cost change. No claim of an actual deployment recommendation follows.

For **neutral durations only**, after g=2 the marginal expected benefit of K is \(4(1-2z)-3\), so a law-aware policy processes K in that history iff \(z<1/8\). This threshold is a formal consequence of the *restricted* four-type model; it cannot be used without identifying the conditional G→K outcome law. In a prior-outcome-blind implementation, \(\pi_s\) does not require z.

## Which evidence is economically sufficient?

Let \(H\) be the lawful, timestamped information available immediately before K. Define \(Y_K(h)\) as total uniquely payable A/B contribution when K is chosen after G under history h, and \(Y_0(h)\) when G alone continues. For any fixed nonanticipative K decision \(\delta(H)\), under consistent cluster interference boundaries, well-defined treatment versions, rights eligibility, and sequential exchangeability/positivity within H,

\[
J(\delta)=\mathbb E\big[\delta(H)\,\mathbb E(Y\mid H,K=1)
+(1-\delta(H))\,\mathbb E(Y\mid H,K=0)\big]-c(\delta).
\tag{6}
\]

This is the established sequential g-formula applied to qualified paid customer production. The **smallest economic audit for the *fixed* G→K policy choice** need only identify \(\mathbb E[Y_K(h)-Y_0(h)]\) and the action-specific costs in each *decision-relevant* G-history cell, not reconstruct every hidden joint technical state. A full law or joint durations are needed if other worker assignments, alternative customer deadlines or future qualification policies are being optimized. If the goal is merely certifying \(\pi_s>E\) under physically proved lower-duration caps and receipts, the inequality (5) can obviate a full paired copula audit; those physical caps and customer receipts themselves require verification.

Only a lawful whole-program or sequentially randomized cluster experiment can validate potential duration changes due to joint source use. The old G-only and K-only arms lack support for \(\kappa^{GK}\) and for K decisions after g. A paired *technical* checkpoint evaluation is not evidence of a shared worker's realized completion time. An audit conditioned on accepted invoices excludes the delayed and unpaid clusters and biases exactly the event (6) needs. An unregistered later B should not be imputed because historical accepted A customers tended to return.

## Prior foundations, robustness and integration

Dynamic treatment regimes with sequentially randomized, history-conditional actions and positivity are established: see [Murphy (2003), Optimal Dynamic Treatment Regimes](https://academic.oup.com/jrsssb/article/65/2/331/7092852). Scheduling with due dates and earliness/tardiness penalties is an established operations-research area; e.g. [Lakshminarayan et al. (1978)](https://doi.org/10.1287/opre.26.6.1079). [Farboodi, Koh and Xia, *Data-Driven Automation*, NBER WP 35320 (2026)](https://www.nber.org/papers/w35320) already model endogenous future data value, and complementary aggregation appears in its Appendix B. The Fréchet coupling, common-law partial identification, decision timing and renewal thresholds here are *conditional standard mathematical applications*, not a validated new economic principle or novel formula.

The broader implication is a connection between **information timing and the topology of qualified production**. Source integration is economically complementary only insofar as it permits timely fully qualified *paid* service; a worker-shortage, source interaction or customer deadline may turn technical complementarity into an economic liability. Equally, selective processing of the same provenance-preserving sources can outperform full immediate integration without predicting the hidden source copula. That is a candidate organizing mechanism for the recursive firm—learning and production jointly reshape the next feasible action set—rather than a reason to replace the full hardware/manufacturing/multilayer value-chain roadmap with a single repair-queue example.

The first-paper argument remains source capability → target recipe qualification → resource-constrained accepted customer production → genuine new demand and source generation → informed next allocation. Companion [unpopulated field evidence protocol](VARIABLE_DURATION_RENEWAL_EVIDENCE.md), [exact CPU model](variable_duration_renewal_exact.js), [replication](VARIABLE_DURATION_RENEWAL_REPLICATION.md), and separate [exercises](VARIABLE_DURATION_RENEWAL_EXERCISES.md)/[solutions](VARIABLE_DURATION_RENEWAL_SOLUTIONS.md) preserve an auditable path. The official [BEA Input-Output program](https://www.bea.gov/itable/input-output) and [BEA InputOutput API](https://apps.bea.gov/api/) remain primary quantitative routes; no verified actual numerical interindustry cell was extracted here. Theory remains the majority workstream through December 6 and final delivery is December 25, 2026, 23:59 Eastern.

**Exact next proof gap:** can a lawful observation-timed lower bound of the form (5) survive program-dependent *G duration itself*, customer-order response, multiple accepted A tickets, and endogenous K-generated data for future embodiments? This requires a common law for complete buyer/worker/learning histories, or an explicitly partial support-preserving bound—not more isolated parameter runs.
