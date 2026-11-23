# What must a robotics firm remember? Economically sufficient histories for heterogeneous evidence and joint qualification

23 November 2026 · Continuation of *When Capabilities Become Production*, especially [SEQUENTIAL_ADAPTIVE_BUYER_WORKER_POLICY.md](SEQUENTIAL_ADAPTIVE_BUYER_WORKER_POLICY.md). **November 22 scientific acceptance remains OPEN.** This is a conditional economic-state-abstraction derivation and a synthetic counterexample, not field evidence, quantified robot ROI, or a novelty claim.

## The live question

The preceding four-date theorem prices a nonanticipative t3 service-versus-maintenance choice and t4 original buyer/worker response. It treats later qualification as fixed. Here both a paid production episode and recovery activity can generate heterogeneous retained records; t4 learning/validation can qualify an arm, a mobile unit, or an integrated two-embodiment recipe. Which parts of the lawful operating history must the firm retain to choose efficiently? In particular, can it compress everything into a count of examples, a benchmark accuracy, or separate embodiment qualification rates?

**Answer.** For a specified, supported finite customer-production decision, a compressed history is sufficient for the *optimal action* exactly when each positive-probability compression cell contains a common optimal feasible action. A stronger controlled-state condition preserves optimization through multiple dates. Neither data quantity, marginal skill qualification rates, nor historical invoice totals alone generally satisfy these conditions. When the omitted provenance changes which economically complementary recipe can qualify, discarding it can reverse the preferred P/G/E/R investment. This result uses existing statistical decision theory and MDP state-abstraction principles; the contribution here is the coupled paid-production/rights/worker/learning interpretation and a falsifiable observation design.

## 1. Economic environment: one argument, not an additive data premium

A program z belongs to the old-policy R, productive-source P, licensed target-grounding G, and independently embodied E investment menu. Historical customer demand, signed admissibility, simulation, public/pretrained data, field trajectories, production successes, recoveries and teleoperation remain separate provenance channels; *no modality is primitive for all tasks*. All source uses must have independent permission to retain, train, transfer, validate and deploy.

At the end of t3, a complete history H contains original customer offers and rejections, buyer budget left, accepted paid service and quality, physical worker/repair queue, versioned source-origin records, signed rights, model/embodiment version, validation eligibility and acquisition actions. Let T=f(H) be a compressed record available before the next decision. If a firm can choose a terminal t4 action a, including the old retained option, define

\[
q_z(h,a)=\mathbb E_z[\text{t4 accepted contribution, net of validation, labor and deployment costs}\mid H=h,\operatorname{do}(a)].
\]

The expectation is over the **z- and a-specific joint law** of qualification, original buyer orders, worker release, acceptance and prices. It is not a product of marginal benchmark qualification and independent demand, nor a transported R law. The action menu A_z(h) contains only actions technically qualified, lawfully authorized and physically feasible for that history; one scarce worker or validation slot cannot be assigned to two simultaneous exclusive jobs.

The current earned t3 service is already in the preceding dynamic reward. Future learning matters only by changing later achievable paid service; a second data premium would double count its value.

## 2. Proposition: exact economic cost of history compression

First take a fixed z with known *supported* finite history distribution, and assume a common nonempty terminal action set A within each fiber f^{-1}(t). Actions can be randomized but the terminal objective is risk-neutral and linear. Define

\[
V_z^{H}=\mathbb E[\max_{a\in A}q_z(H,a)],
\quad
V_z^{T}=\mathbb E[\max_{a\in A}\mathbb E[q_z(H,a)\mid T]].
\]

The second equality is optimal **restricted to rules measurable in T**, not an imaginary policy that still sees the hidden raw records. Then

\[
\boxed{
\Delta_z(T)=V_z^{H}-V_z^{T}
=\mathbb E\{\mathbb E[\max_a q_z(H,a)\mid T]-\max_a\mathbb E[q_z(H,a)\mid T]\}\ge0.
}
\]

Moreover, because A is finite, \(\Delta_z(T)=0\) **if and only if** in almost every positive-probability T-cell at least one action is a maximizer of \(q_z(h,\cdot)\) for almost every h in that cell. This is an economic *common-optimizer* criterion: Q vectors need not be identical, and a raw event log need not be preserved if all omitted differences are irrelevant for action choice.

**Proof.** Conditional expectation of a maximum is at least the maximum of conditional expectations, giving the inequality. If a common action maximizes at every h, that same action realizes both sides and the gap is zero. Conversely select any action attaining the maximum of conditional expected q in a cell. The nonnegative random variable \(\max_b q_z(H,b)-q_z(H,a)\) has expectation exactly the cell gap. If the gap is zero it must vanish almost surely, making a common maximizer. Nonnegative cell gaps cannot cancel across cells. Randomization cannot improve the maximum of a finite collection of expected rewards. QED.

With history-dependent eligibility, the same statement applies after replacing A by the *common feasible* intersection on each T-cell and explicitly charging the cost of unavailable actions. If compression loses feasibility, the displayed formula with the unaltered menu is invalid. If the report arrives only after irreversible validation, T cannot be used retroactively. These are real restrictions, not technical footnotes.

**Program rankings.** Write \(V_z^T=V_z^H-\Delta_z\). A program z outranks z' after compression iff
\[
V_z^H-V_{z'}^H>\Delta_z-\Delta_{z'}.
\]
Thus exact identification of the dollar-like program levels is stronger than needed to certify a ranking; an independently defended upper bound on the relevant relative compression loss can suffice. Such a certificate must use one common causal law, not unrelated worst-case distributions selected independently for P, G, E and R.

### Multi-date sufficient condition, and why it is stronger

For each supported program z and every pair h,h' with f_t(h)=f_t(h'), require: (i) identical lawful feasible menus and predecision information timing; (ii) identical conditional **net accepted reward** for each feasible action; (iii) identical joint conditional distribution of the next compressed state, qualified recipe outcomes, buyer offers, queue and report inclusion for each action. This is a controlled reward/transition quotient. Backward induction from the last period proves that a policy using f_t can attain the same optimal continuation value as a full-history policy at all earlier supported dates. If the next compressed state does not retain the qualification/queue variables needed for its own action menu, (iii) is not satisfied.

The controlled quotient is sufficient, **not necessary**, for this one economic objective. The one-stage common-optimizer criterion is strictly weaker. A stronger universal necessity statement would require a rich family of reward functions and menus. Economically relevant Q-value sufficiency may depend on buyer demand and access terms; it is not a universal robotics representation. Crucially, none of these mathematical equalities identifies unsupported action kernels. A perfectly compressed G/M record cannot be learned from R or G/S histories where G/M was never lawfully tried.

## 3. Counterexample: aggregate counts reverse an investment ranking

Hold the original t4 buyer offer fixed and valid, give the customer a single remaining purchasing budget, and provide one shared validation/service slot; the robot phases needed for a kit are **sequential**, never simultaneous demands on one exclusive worker. Common accepted t3 service and costs are equal across compared programs and omitted. A lawful G cohort produces one of four equally probable retained data histories after t3:

| h | t3 evidence | Number N | Old retained | Qualify arm A | Qualify mobile C | Validate joint kit A+C |
|---|---|---:|---:|---:|---:|---:|
| F | One field-production trace | 1 | 2 | 3 | 0 | -1 |
| T | One recovery/teleoperation correction | 1 | 2 | 0 | 3 | -1 |
| FF | Two distinct field traces | 2 | 2 | 3 | 0 | -1 |
| FT | One field and one recovery trace | 2 | 2 | 3 | 3 | 7 |

All entries are stipulated *net normalized accepted contribution*. Arm/mobile actions have been independently qualified in the corresponding source case, and only one may be validated/served before deadline. A kit requires **both** embodiment qualifications, gives gross 8 if accepted and costs 1 to attempt; a failed validation costs 1 and leaves no deadline capacity for the retained recipe. The old recipe contributes 2 and can always be chosen instead. No benchmarking percentage is converted mechanically to revenue. A source trace is not interchangeable with a recovery trace, even when both count as one row.

With full, lawfully available provenance the optimal choices are A, C, A, kit and

\[
V_G^{H}=(3+3+3+7)/4=\boxed{4}.
\]

With only the count N, the N=1 cohort must choose the same action in F and T. Its best action is the retained recipe worth 2. At N=2, either A or kit has conditional expected value 3. Hence

\[
V_G^{N}=\tfrac12(2)+\tfrac12(3)=\boxed{5/2}.
\]

The simple **qualification-presence signature**
\[
f^*(h)=(1\{\text{at least one admissible F}\},1\{\text{at least one admissible T}\})
\]
has three reachable classes and still obtains \(V_G^{f^*}=4\). It is sufficient for *this exact terminal menu*, since F and FF share an optimal A action. Its 1.5 value over counting rows is the maximum gross willingness to pay for timely usable provenance at this already specified cohort, before any additional recording/reporting expense. It is not a portable field-data price.

Now let the identical real-resource, lawful alternative programs' stipulated incremental values be \(V_E=3,\ V_P=11/4,\ V_R=2\). **With the true G information G outranks E, but under the imposed N-only organizational interface E outranks G.** The physical G data never changed. Only what the decision-maker could distinguish changed. The optimal strategy with free optional provenance always retains the N-only option, so free access to that information cannot hurt. Forced use of a faulty training recipe or extra reporting cost is a different comparison.

The executable exhaustive model checks all 15 partitions of the four histories. In this case a partition has zero loss exactly when every cell has a common optimal action; the only nontrivial safe merger combines F with FF. The script also checks that refining information never decreases its optimized economic value and that the conditional-gap identity holds for each partition. The enumeration checks the finite example, not the theorem.

### Acquisition can become misallocated one date earlier

The same failure can occur *before* data arrive. Consider an already lawful t3 signal that separates an A-relevant fault from a C-relevant one, each with probability 1/2. One exclusive worker can either serve A (S), earning an accepted current unit and sometimes yielding transferable field evidence, or perform preventive recovery (M), yielding distinct recovery evidence. The conditional t3-plus-t4 **already netted and jointly evaluated** payoffs are:

| Predecision signal | S: paid service plus future work | M: recovery plus future work |
|---|---:|---:|
| A-relevant | 5 | 0 |
| C-relevant | 1 | 6 |

The informed policy selects S then M and earns \((5+6)/2=11/2\). An agency required to commit to one action before learning the signal achieves only \(\max\{(5+1)/2,(0+6)/2\}=3\). An independent E alternative stipulated at 4.2 therefore reverses its ranking. No t4 outcome is foreseen: the two numbers per action are *conditional expectations* of later actual original orders, qualification and worker capacity, not post hoc oracle choices. This second construction highlights endogenous record acquisition; it does not establish the S/M kernels from S-only observational histories.

## 4. What qualifies as observable and sufficient in real deployment

An actually useful prospective signature has to start with **jointly** versioned original customer offers/no-offers, remaining payable budget, accepted service/quality, worker job IDs and occupation intervals, target embodiment and eligible recipes, action clock/deadline, and rights. Each retained event additionally needs provenance: field success, failure/recovery, remote teleoperation, simulation, synthetic or public/pretrained record; its source task/embodiment, distinct case family, release/version, license and target validation. A rights-ineligible item must not be counted as if its transferable qualification were licensed.

The testing unit is a buyer–worker–model-sharing cluster. Use lawful randomized or otherwise defensibly assigned combinations of (i) t3 service versus recovery/target grounding, (ii) retaining versus hiding source **provenance** from the t4 decision-maker while preserving safety and rights, and (iii) independently matched, qualified target validation. The information-only intervention must leave physical acquisitions and underlying training menu unchanged; otherwise it is a training-treatment contrast. Audit original *unserved* customer orders and concurrent repairs, not only receipts or resolved tickets. If reports change behavior, report acquisition is an economic intervention with its own response law.

Measure both technical transfer on held-out target tasks and incremental accepted buyer service at matched hardware, compute, data rights, support capacity and demand. Compare the strongest existing fixed rule and old-policy option to the provenance-aware rule, including validation burden and safe rollout. For a multi-embodiment order, record the joint recipe result, not only each stage's marginal success rate. Since actions can change subsequent evidence, complete the multi-date sequence before estimating a firm-value effect.

What the current sources do **not** establish: empirical frequencies of F/T histories, qualified buyer payments, the effect of a target grounding intervention on actual original orders or queues, signed G permissions, physically independent E labor, or numerical official interindustry production coefficients. These remain required evidence, not filled by this proof.

## 5. Bounded closest prior art and interpretation

Farboodi, Koh and Xia, *Data-Driven Automation* (NBER Working Paper 35320, June 2026), already endogenize task-specific data and cross-task spillovers, including forward value and complementary aggregation; they are a substantive starting point, not novelty to reclaim: https://www.nber.org/papers/w35320 .

Li, Walsh and Littman, *Towards a Unified Theory of State Abstraction for MDPs* (2006), analyze preservation of planning/learning under MDP state abstractions: https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/camera-ready-9.pdf . Blackwell's comparison of statistical experiments is a predecessor for the value of information to a decision-maker: https://celebratio.org/Blackwell_DH/article/255/ . Open X-Embodiment (2023) provides cross-robot training evidence, not customer-value coefficients: https://arxiv.org/abs/2310.08864 .

The exact expected-max gap and controlled-state quotient are established kinds of decision mathematics. This synthesis's value is an **operationally discriminating hypothesis** for a robotics business: keeping a modest number of qualified provenance/rights/queue distinctions may dominate buying another block of undifferentiated data, and a counting interface can direct both training and physical investment toward the wrong customer opportunity. The hypothesis fails where the same action optimizes every hidden history, where the additional report is too costly/late, where rights prohibit use, or where customer demand/worker capacity binds so tightly that new qualification creates no additional paid service.

**Next proof gap (unchanged intellectual question):** estimate or bound the program- and action-specific transition law of the proposed signature from t3 service/recovery into t4 *joint* qualification and original buyer/worker response, including buyer demand endogeneity, selection into observability, and optional E capacity. Prove a support-aware certificate for a compact signature without assuming an untried G/M intervention was already performed. Contrast transfer-compatible source mixtures against an independent embodiment and the retained safe policy on identical accepted-service recipes. Preserve the November 29 empirical backbone and December 6 theory-choice deadlines as scientific gates, not automatic successes; final target remains 25 December 2026 at 23:59 America/New_York.
