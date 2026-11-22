# Queue-duration coupling, target grounding, and the economics of source-generated capability

**22 November 2026 — continuation of When Capabilities Become Production, integrated Models A/B.** This is a conditional mathematical extension of [worker carryover](WORKER_CARRYOVER_NETWORK_AND_VALUE.md), not a new independent project or an established scientific novelty claim. The November 22 scientific acceptance gate stays **OPEN**. All numbers below are deliberately **synthetic normalized expected customer-paid production contributions**; none is a robotics benchmark converted into money.

## The question and the limitation of the last result

The previous four-date example fixed the t2-to-t3 response rule and obtained a sharp bound from the missing joint event of original eligible buyer orders and one worker's busy state. Here a recovery intervention produces a *single physical queue duration* that restricts **multiple** downstream windows. Source-generated data P, legally available target grounding G (also called D/SG when appropriate), and a separately resourced embodiment E must be compared against the same safe R production in the full economic program. Can a coupled duration-and-original-buyer *path* identify an investment ordering when periodwise qualification rates, demand, and worker utilization cannot?

The key answer is an exact finite optimal-transport certificate, conditional on a specified safe recipe, rights and deadline clock. When the physical queue comes from one recovery job, its busy indicators across dates are **nested**, not separately chosen. Period-by-period Fréchet bounds can be extremely loose and even suggest impossible simultaneous extremal assignments. The economically sufficient missing input in the restricted model is the joint allocation of recovery durations to original-buyer order paths, rather than a vector of periodwise averages. This does *not* identify the general adaptive network with new jobs, demand response, or learned embodiment expansion; that remains the next proof gap.

## Production environment, timing and allowable programs

Let t=1,2,3 be service windows following an initial lawful source-data inventory. R is a safe qualified production recipe paying a conditional expected net 2 in each window, hence total 6 with discount factor one. Its availability and the underlying contractual expected values are unchanged in this example. These figures are expected paid-service categories from hypothetical original buyers, not realization of future settlement known at dispatch. Real acceptance/refunds/payment are recorded **after** service.

At t=1, the firm chooses an investment program without observing future worker recovery duration D or future original eligible buyer order path U=(U2,U3). Distinguish:
- **P:** retain the source checkpoint and optionally run a field learning pilot at t=1, yielding conditional expected net 7/4 instead of R's 2. The pilot creates a legally transferable qualification for the new target at t=2,3, subject to actual signed use rights. It occupies a target-specific shared recovery worker for D service windows. Choosing R instead of the pilot always remains possible, with full R continuation.
- **G:** apply a target-specific grounding/verification operation to already-held *lawfully reusable* source data, at total incremental cost 7/10, without this pilot's worker occupancy. At t=2,3 the target is qualified. When an eligible original target buyer orders, serving the target on the existing robot earns conditional expected net 3 instead of R's 2. G's future target service lasts one window. It does not manufacture another robot.
- **E:** acquire a separately capable robot and **independent** recovery/teleoperation capacity, at total incremental lifetime cost 13/20. Its qualified target service earns conditional expected net 1 per eligible original target order **in addition to** the R production on the old robot. This separate target service lasts one window. Independence of both robot-time and worker resources is essential.
- **R:** do not buy, train or pilot; produce the old R in all three windows.

P's field pilot is distinct from deliberate target teleoperation/grounding G, and neither is simulation, synthetic data, pretrained/public data or failure/recovery trajectories. Source inventory may contain several such classes, but only the explicitly legal pilot and grounding rights are assumed in this illustrative submodel. The pilot's current receipt sacrifice is an **opportunity cost** already included in program value, not a second data premium.

D is the duration of the *t=1* P pilot's one worker recovery job. Under the no-new-job restriction, define F2(D)=1{D<=1} and F3(D)=1{D<=2}. Thus F2<=F3 pathwise: the worker cannot be free at t=2 and then busy again at t=3 without an intervening job. U2,U3 are the *predispatch* original-buyer safe eligible-order indicators under the P-potential environment. They can be correlated with D through common customer demand, incidents, learner adaptation or operations; there is no independence assumption. Subsequent t=2 target dispatch requires F2 U2=1; t=3 dispatch requires F3 U3=1. A t=2 or t=3 target transaction here does not create a new recovery job lasting beyond its own window, and it does not further alter demand or qualification. These are strong, falsifiable simplifying conditions.

The general integrated law remains J_a=sup over lawful adapted policies of E_a[sum_t beta^t r_t], with shared robot/operator capacities, full order and learner transitions, rights state, manufacturing resources and endogenous subsequent demand. The following finite transportation result is **one solvable restriction** of this general Bellman program, not an alternative production accounting framework.

## Proposition: a sharp queue-path data-value certificate

Suppose the t=1 pilot choice is made without observing (D,U), and all safely eligible t=2/3 target services yield a nonnegative incremental expected net 1 without affecting later states. Let m_d=Pr_P(D=d) and n_u=Pr_P(U=u) be known P-conditional marginals, with u in the original-buyer path set. Let C(d,u)=1{d<=1}u2+1{d<=2}u3. The physical joint-law set is the transportation polytope

    Gamma(m,n)={gamma>=0: sum_u gamma(d,u)=m_d, sum_d gamma(d,u)=n_u}.

Then for each admissible joint law gamma, the exact optimized P contribution is

    J_P(gamma)=6+[ -1/4+sum_(d,u) gamma(d,u) C(d,u) ]_+.   (1)

Here [x]_+=max(x,0). Define M=min_(gamma in Gamma)<gamma,C> and X=max_(gamma in Gamma)<gamma,C>. The **sharp** identified interval is

    [ 6+[-1/4+M]_+,  6+[-1/4+X]_+ ].                    (2)

Every intermediate value is attained by a feasible joint law. The upper transport problem has the exact finite dual

    X = min_(alpha,beta) (sum_d m_d alpha_d+sum_u n_u beta_u)
        subject to alpha_d+beta_u >= C(d,u) for all d,u. (3)

The lower is the corresponding transport minimization with reversed dual inequality. The dual variables certify upper or lower **program opportunities** over supported duration/order paths; they are not market wages or a universal dollar shadow price.

**Proof.** Under each future observed lawful predispatch U and worker F, a target service replaces R only when F_t U_t=1 and increases expected paid contribution by 1, with no downstream cost in this restricted environment. Hence future optimal extra contribution along a realized pilot path is C(D,U). Pilot t=1 sacrifices 2-7/4=1/4, while the no-pilot policy produces the complete R value 6. The pilot is chosen *before* D and U, so the optimizer compares one ex-ante expectation to zero, yielding (1); taking a pathwise positive part before expectation would be illegal clairvoyance. Gamma is a compact convex nonempty finite transportation polytope. The linear expectation attains endpoints M and X and all intermediate values by mixing its extremizers. The positive-part map is continuous and nondecreasing, which proves sharpness of (2) including its flat region. Equation (3) is standard finite LP/Kantorovich duality (not a newly discovered theorem). It does not permit one independent marginal coupling to be selected for every future date: all dates share the *same* gamma and the same D. QED.

An informational qualification matters: (2) is a sharp *set of full-information optimized program values across admissible worlds*, not a guaranteed payoff for a single unchanging investment strategy when the true coupling is unknown. A robust ex-ante controller must select its pilot/report policy against a common joint uncertainty set. An additional lawful pre-pilot signal W changes (1) to a sum over W-atoms of conditional positive parts, but then the conditional joint laws must arise from **one** supported original connected-cluster law; one cannot optimize independent fictional reports or observe post-service settlement in advance.

## Exact synthetic P / G / E counterworlds

Let all four original-buyer path types U=00,10,01,11 occur with probability 1/4 under each of the three programs, and let P's physical queue duration D have distribution (Pr(D=1),Pr(D=2),Pr(D=3))=(1/4,1/4,1/2). Thus both buyer-site/time order marginals are 1/2, their entire **two-window path distribution** is known, t=2 worker free probability is 1/4 and t=3 worker free probability is 1/2. Everyone also knows the *nesting* F2<=F3, not just the busy rates.

Each column U has exactly a quarter of mass. The transportation matrix is integral after scaling by four; every extreme law assigns one U path to D=1, a different U path to D=2, and the other two paths to D=3. All 12 such assignments are enumerated in [executable exact model](queue_duration_grounding_exact.js) and its [record](queue_duration_grounding_results.json). The two sharply extremal laws are:

| Physically feasible P world | D=1 assigned buyer path | D=2 assigned buyer path | E_P[C] | optimized J_P |
| --- | --- | --- | --- | --- |
| High source-learning return | 11 | 01 | 3/4 | 13/2 |
| Low source-learning return | 00 | 10 | 0 | 6 |

The D=3 assignments are the two remaining order paths. These worlds have identical full U-path distribution, identical D marginal, identical qualifications after a successful pilot, identical t=1 contractual receipt and the **same** queue service law; only the correlation of one physical recovery duration with future original buyers changes. A simple sharp dual certificate is C(d,u)<=2 1{d=1}+1 1{d=2}, yielding X<=2/4+1/4=3/4; the high coupling attains it. Since C>=0 and the low coupling attains zero, M=0. The real-valued mixture of these kernels gives exactly the full interval [6,13/2] in (2). Source data being freely available does not cause a loss: the producer declines the costly pilot in the low world.

G uses the retained source without the queue-consuming pilot. Its complete program value is 6+E(U2+U3)-7/10=63/10. E adds a separate robot **and worker**, has expected extra original-buyer paid value 1, and cost 13/20: J_E=127/20. Those costs and receipts are fully hypothetical, included once, and specified identically across the counterworlds. The high world ranks P > E > G > R; the low world ranks E > G > P=R. Consequently P−E ranges sharply from −7/20 to +3/20. This is a refusal to identify an investment winner from queue utilization and technical success; it is not a claim about a measured threshold for a robotics firm.

## Negative result: separate-period bounds can lose valid queue constraints

If the pilot has D=1 or D=3 each with probability 1/2, then F2=F3=F=1{D=1}. Suppose the original-buyer future path is either 10 or 01, each with probability 1/2: exactly one eligible customer offer occurs across the two windows. Without knowing any dependence between F and which period receives the order,

    C=F U2+F U3=F(U2+U3)=F, so E[C]=1/2 exactly.

An analyst applying separate single-window Fréchet bounds to Pr(FU2) and Pr(FU3), each with marginal rates 1/2, would produce [0,1] for their sum. That interval is nonsharp: its endpoints cannot both reflect the conserved buyer order path and the common duration. This counterexample **falsifies independent time-row interval multiplication**, not Fréchet mathematics itself. It shows that some demand-path/queue structures can make economic production identified without determining the detailed correlation; blanket claims of nonidentification would also be wrong.

## Where the result stops, and a route to the full recursive firm

For t=2 service that creates another persistent recovery job, D ceases to be the only queue clock. A new arrival A_t, operator service residual B_t and causal dispatch/recovery action generate B_(t+1)=[B_t-1]_+ + L_t(A_t,dispatch_t,incidents_t), with admission restricted when the worker is busy. Depending on whether arrivals are served FIFO, rejected or queued, this equation needs an explicit scheduling convention and distinct states for waiting jobs and work in service; adding service time to B is legitimate only as an aggregate-workload convention. The original customer can alter orders after successful production; qualifications and rights can change with source/grounding choices; new embodiments may change the action menu and effective cluster graph. Then C(d,u) alone is insufficient and the same probability mass cannot be reallocated separately by window or policy.

The correct next theorem should replace the one-job transport cost by **nonanticipative policy-specific complete paid Bellman continuation** under a joint physical-worker/learner/order/rights support polytope. For fixed admissible policy pi, complete payoff is linear in the joint *full-history path* law; for the optimized controller it is an upper envelope of such linear forms. Maximum across possible worlds can exchange the two suprema, but minimum-world optimized return and the value of one deployable robust policy are generally different. A static observed-R support or expected worker utilization cannot certify all optimizing SG/E policies. Compare true matched P/G/E interventions at connected-cluster exposure levels, rather than deriving dollars from task benchmark gains.

The queue assumptions themselves provide prospective falsifiers: with no new jobs after the pilot, Pr(F2=1,F3=0) must be zero and Pr(worker busy at t3)<=Pr(worker busy at t2). Reversals imply unrecorded jobs, different staffing or recovery scheduling, or misaligned clocks. Captured duration must be a *true resource occupation event*, not merely prediction that an operator was needed. A G program without signed source reuse rights is **not** a costly action with uncertain return; it is *inadmissible*. An E program that borrows the pilot's worker is **not** independently resourced.

The [unpopulated intervention and original-buyer evidence protocol](QUEUE_DURATION_GROUNDING_EVIDENCE.md) specifies the admissibility, demand paths, censoring and selection tests. [Exercises](QUEUE_DURATION_GROUNDING_EXERCISES.md) and separate [solutions](QUEUE_DURATION_GROUNDING_SOLUTIONS.md) accompany the exact model. The model was checked using integer-quarter enumeration of 12 transportation extreme assignments and a distinct Python Fraction implementation. Such finite checks are not proofs of transport duality or causal identification.

**Closest prior foundations:** Farboodi, Koh and Xia, [Data-Driven Automation](https://arxiv.org/abs/2606.10127) (June 2026), already treats production-generated future data and complementarity; Hoque et al., [Fleet-DAgger](https://arxiv.org/abs/2206.14349) (2022), already models scarce shared human supervision. Finite discrete transport, LP duality, Fréchet, adaptive dynamic optimization and queue workload conservation are classical foundations. The specific original-customer demand-path × worker-duration × lawful source/grounding/embodiment synthesis here is a proposed research **application**, not independently verified scientific novelty.

**Evidence and gate:** No authorized matched connected-cluster P/G/E study, original buyer no-offer cohort and cleared payment ledger, signed cross-site source rights, actual worker duration/order causal joint law, demonstrated separate E worker/capacity or quantitative official BEA/BLS interindustry I/O coefficients is available. November 22 Models A/B acceptance remains **OPEN**; November 29 should strengthen evidence, December 6 retains theory contribution choice, and final delivery remains December 25, 2026 at 23:59 America/New_York.
