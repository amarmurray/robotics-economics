# Failure-origin data, recovery-generated evidence, and economically gated overlap
23 November 2026 · Continuation of *When Capabilities Become Production*, especially [endogenous two-cohort source acquisition](ENDOGENOUS_TWO_COHORT_SOURCE_AND_DEMAND.md), [data-mixture topology](ADAPTIVE_SOURCE_MIXTURE_QUALIFICATION_TOPOLOGY.md), and [economically sufficient histories](WHAT_MUST_THE_FIRM_REMEMBER.md).

**Status:** conditional finite-state theory, proof and exact synthetic counterexample. NOT measured robotics returns, independently verified novelty, approved intervention or acceptance of the November 22 scientific gate.

## The precise next question

After an attempted paid robot service fails, (i) it leaves a typed field-failure trajectory, (ii) its original buyer still has an unfulfilled order and finite purchasing authorization, (iii) an operator has a repair job, and (iv) clearing that job may generate an entirely different recovery trajectory. What evidence, beyond aggregate transfer accuracy and even source-by-source **paid** success, identifies the incremental value of using *both* failure-origin target grounding and recovery-origin learning in a subsequent customer cohort?

**Answer:** the economically relevant intersection of the two independently qualified recipes **within the same original-buyer, budget-valid, worker-available risk set**. The unconditional technical overlap and the two individual paid-service coincidences need not identify it. This result is an application of established set algebra, potential-outcome support and finite decision theory. Its value is the specific physical/market mapping, not a claim to invent those methods.

## Physical and economic environment (three cohorts)

At cohort 1 an eligible original buyer holds **one unfulfilled ticket**, with remaining dollar authorization at least four normalized units. The incumbent robot attempts that ticket. With probability 1/2 it completes an accepted service and captures contribution 1; the ticket closes, so it cannot be sold again even if unspent nominal budget remains. With probability 1/2 the attempt fails: no sale, the original ticket and authorization remain open, and one **real worker recovery job** is owed. The failed work also produces a typed field-failure trace L; this is not an accepted production success, teleoperation, simulation or a public demonstration. Only an explicitly lawful retained L is usable for training.

At cohort 2 the firm recovers the robot. W=1 indicates actual clearance before the final deadline, not an independent Bernoulli 'available capacity' invented after the job. A recovery trajectory K is generated **only on W=1** and only if rights and retention permit it; K can qualify a different target recipe. G is a precommitted, licensed, compute-only target-grounding update from L. K-policy is a precommitted, post-recovery adaptation from the recovery trajectory; if W=0 it produces no valid recovery data and cannot qualify by that path. Both methods can be acquired without extending the worker's repair duration **in this restricted submodel**; their training, checkpoint-selection, curation, legal use and deployment costs are charged. G and K use separate retained checkpoints, selectable by cohort 3: the service qualifies if either checkpoint independently passes a matched held-out **complete customer recipe**. This OR is an explicit feasible-checkpoint assumption, **not** an assertion that forced joint gradient training is monotone. If that assumption fails, keep the old checkpoints/actions; no monotonicity is inferred.

At cohort 3 D=1 means the **same original unfilled** ticket is renewed and still within budget and deadline; W=1 means the worker is actually free. A single paid service can be accepted only if D W=1. The untrained retained fallback completes it at contribution 2, while a genuinely qualified target upgrade offers contribution 4 for that **same one service**, rather than two sales. No service is delivered if D W=0. An independent, target-qualified, separately staffed new embodiment E can serve the original buyer without the incumbent W, with its own build and labor cost. A learning update cannot directly alter original D or W before the cohort-3 offer and clearance cutoffs **in the witness**; this pre-offer exclusion/non-displacement must be justified prospectively and is *not* implied by historical P evidence.

Let F be cohort-1 failure with probability p, h=Pr(DW=1 | F), Q_G and Q_K the deadline-qualified target recipes under lawful G and recovery-origin K, and c_S the full conditional-on-failure acquisition cost of source menu S. Let x_S=Pr(Q_S D W=1 | F), with Q_empty=0 and Q_GK=Q_G OR Q_K where selectable checkpoints are feasible. If the incumbent fallback and upgrade share a single mutually exclusive service, and m0 and m1 denote their contribution respectively, then the **whole-program** value is exactly

\[
J_S=(1-p)r_1+p\left[m_0h+(m_1-m_0)x_S-c_S\right].
\tag{1}
\]

The buyer's original ticket is spent at most once; no continuation-data premium is added to (1). The recovery job is generated only by the actual failure and a K trace only by actual clearance. Equation (1) follows by partitioning the original cluster into early accepted service, failed-and-late-service, and failed-without-late-service. In a longer horizon, replace the terminal bracket with the *optimized* policy-contingent production-value continuation, carrying the complete budget, worker queue, lawful lineage and acceptance state. It is not permissible to sum option values of incompatible orders.

For E, when independently qualified/staffed, and when original D is not itself changed by the E program, the corresponding stipulated entire-program net is
\[
J_E=(1-p)r_1+p\,m_E\Pr(D=1\mid F)-C_E.
\tag{2}
\]
Without those E-specific transport/staffing conditions, (2) is **not identified** from the incumbent's records.

## Economic overlap theorem

Define the **single-source paid coincidences** x_G=Pr(Q_G D W |F) and x_K=Pr(Q_K D W|F), and the **economic redundancy** z=Pr(Q_G Q_K D W|F). Also let o=Pr(Q_G Q_K|F) be the ordinary technical checkpoint overlap. Under selectable-checkpoint qualification,

\[
x_{GK}=x_G+x_K-z,\qquad
\lambda_{K\mid G}=x_K-z
=\Pr(Q_K=1,Q_G=0,D=1,W=1\mid F).
\tag{3}
\]
\[
J_{GK}-J_G
=p\left[(m_1-m_0)\lambda_{K\mid G}-c_K\right].
\tag{4}
\]

If only h, o, x_G and x_K are known from a *common causally valid law*, elementary event containment gives
\[
\boxed{\max\{0,o+h-1,x_G+x_K-h\}\le z\le\min\{o,x_G,x_K\}.}
\tag{5}
\]
The first lower term follows from nonnegativity; the second from the Fréchet bound for the technical intersection and the paid risk set; the third because the union of qualified paid sets cannot exceed h. The upper terms follow by set containment. These bounds are valid outer bounds in general; they are not asserted sharp for every arbitrary vector of reported marginals when additional common-law or structural constraints apply. In the constructive family below **both endpoints are achieved with every stated observable invariant**, so the resulting economic bounds are sharp for that family.

Equation (4) says K should be added to G ex ante only when the expected *qualified incremental late buyer service* passes the program's real conditional acquisition-cost threshold; generic benchmark accuracy, unconditional Q_K or unconditional technical overlap o cannot replace lambda. If the K opportunity has no charge and is truly optional with unchanged legal/physical policy menu, choosing the old G checkpoint preserves its value regardless of a negative result from a particular forced-training recipe. This is not a statement that collecting, curating or training on K is free.

## Exact common-law counterworlds with a real recovery gate

Condition on F=1. Eight equiprobable latent cohort histories have (D,W) rows:

| atom | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| D | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 0 |
| W | 1 | 1 | 1 | 0 | 0 | 0 | 1 | 0 |

Hence Pr(D)=3/4, Pr(W)=1/2 and h=Pr(DW)=3/8. There is exactly one inherited failure-repair job; K trajectory exists only if W=1. Every observed old-policy R outcome and the original buyer's retained budget are identical across two potential worlds. Under the hypothetical *matched technical validations* Q_G and Q_K are:

| world | qualified G atoms | qualified K atoms (all W=1) |
|---|---|---|
| A | {1,2,4,5,6,7} | {0,6} |
| B | {1,2,3,4,5,7} | {1,6} |

In both worlds Pr(Q_G)=6/8, Pr(Q_K)=2/8, Pr(Q_G Q_K)=1/8, **x_G=2/8** and **x_K=1/8**. Thus even the *unconditional paired technical checkpoint joint law* and the **separate original paid event** for each source are the same. Nevertheless z_A=0 and z_B=1/8. The two programs differ only in **which latent histories contain technical overlap relative to the original paid-and-cleared gate**. K's physical qualification restriction Q_K<=W holds atom by atom.

With p=1/2, early accepted contribution r1=1, m0=2, m1=4, c_G=1/4 and c_K=1/8 *per failed original cluster*, equation (1) gives the following normalized **entire-program** values:

| executable option | world A | world B |
|---|---:|---:|
| R: retain fallback; recover worker | 7/8 | 7/8 |
| G: licensed failure-origin target grounding | 1 | 1 |
| K: recovery-origin adaptation only | 15/16 | 15/16 |
| G+K: keep both selectable checkpoints | **17/16** | **15/16** |
| E: independent staffed embodiment | 33/32 | 33/32 |

E assumes Q_E=1 and Pr(D|F)=3/4, gross (1/2)+(1/2)(4)(3/4)=2, with one comparable program-level new-embodiment resource cost **31/32**; it does **not** use inherited W or sell the same ticket twice. A sufficiently different E demand response, staffing, task-qualification or cost changes its value; these figures are **not actual robot ROI**.

The sharp admissible gated-overlap range from (5) is z in [0,1/8], and a finite exhaustive enumeration of all 18 eight-atom qualifying Q_G/Q_K assignments under the displayed margins and Q_K<=W confirms only those two endpoint values. Therefore GK lies in [15/16,17/16], straddling E=33/32. Under a precommitment over independently comparable eligible customer/worker clusters and this exact two-endpoint ambiguity family, the worst regrets of allocating fraction alpha to GK and 1-alpha to E are (1-alpha)/32 in A and 3alpha/32 in B; minimax regret chooses **alpha=1/4**, with worst regret **3/128**. Maximin chooses E. The regulator, customer and resource conditions required for such cluster mixing remain assumptions; this is not a recommendation to buy robots.

The sign of source overlap is thus *economically gated*. Even if the two source checkpoints each earn the same qualified paid value and have the same technical joint distribution, a second source can create a previously uncovered payable recipe in one economy and only duplicate the first source within the payable gate in another. The specific thresholds and numbers are synthetic; the general accounting identity is algebra.

## Conditional identification, falsification, and the broader agenda

A prospective matched **technical intervention** could hold hardware, model version, training/compute budget, customer recipe, quality threshold and evaluation horizon constant for G-only, K-only and retained-checkpoint branches, distinguishing field failure, recovery, teleoperation, simulation, synthetic and public/pretrained evidence *without flattening them to counts*. But Q_G and Q_K from separate test populations are not jointly defined on the same counterfactual customer cluster by default; matched paired qualification and lawful cluster-level treatments or justified coupling restrictions are indispensable.

An **original-buyer/worker audit** must record the *unselected* original order/no-order, remaining dollar authorization, deadline, accepted quality/rejection, paid amount, inherited worker job, clearance and new job creation in the same licensed risk set. Crucially it must estimate **z conditional on failed-first-service status**, not only o, x_G and x_K separately or all receipts conditional on accepted service. When K is produced only after clearance, analysis must keep W=0 failures in the original denominator: K-only-selected clips do not identify its missing-by-construction economic value. For real action-dependent demand and recovery, measure policy-specific D/W effects rather than transporting R outcomes. A prospective cluster randomization with pre-registered source-menu rights, model checkpoints and interference boundaries is the cleanest identification route; signed permissions and customer access have not been obtained.

The end-market atlas should index this mechanism by **original service recipe and worker bottleneck** (warehouse tote-pick, replenishment, mobile-robot/arm kit, and digital/physical order orchestration), not a single benchmark score. BEA industry-level input-output exposure can provide market context only with verified quantitative cells, not a task transfer estimate. Capital choice remains across fleet, learning, coordination, manufacturing, embodiment, access and rights, but this continuation retains the original P/G/E/R qualified-production value rather than reverting to financing/default contracts.

**Prior-art boundary:** [Farboodi, Koh & Xia, *Data-Driven Automation* (2026), arXiv:2606.10127](https://arxiv.org/abs/2606.10127) already models heterogeneous endogenously produced data, spillovers and forward value; its Section 5 and Appendix B already cover future data value and complementary aggregation. [Ghorbani & Zou, *Data Shapley* (ICML 2019)](https://proceedings.mlr.press/v97/ghorbani19c.html) studies supervised performance-based data valuation. Classical set unions, Fréchet bounds, dynamic production and causal-support arguments underlie (1)-(5). The candidate synthesis here is the original-buyer-budget/worker-gated economic overlap and the accompanying cross-source identifiability demonstration, **not independently demonstrated scientific novelty**.

**Unresolved exact proof/identification obligation:** extend this *same* conditional failure/clearance/buyer-budget model when choosing G or K changes t3 buyer demand and job-clearance probabilities; determine a common, nonrectangular physically feasible causal law and **minimum lawfully supported intervention** that can identify or sharply bound z and the full adaptive P/G/E/R ranking. Without signed data rights or G/K assignment support, report economically uninformative causal contrasts rather than claiming empirical identification. Nov22 scientific gate remains OPEN; theory stays majority through Dec6 and the final **December 25, 2026, 23:59 America/New_York** target is unchanged.
