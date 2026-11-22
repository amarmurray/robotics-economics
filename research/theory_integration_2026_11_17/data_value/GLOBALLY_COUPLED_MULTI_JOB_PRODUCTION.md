# Globally coupled multi-job queues and the economic identification of transferable robot learning

**22 November 2026 — When Capabilities Become Production, integrated Models A/B.** Conditional theoretical synthesis; all monetary-style examples are *synthetic normalized net qualified customer-production units*, **not** observed robotics returns, benchmark percentages converted to revenue, or independently validated novelty. November 22 scientific gate remains **OPEN**. Extends [adaptive learning/recovery queues](ADAPTIVE_QUEUE_LEARNER_DEMAND_COUPLING.md) and [physical duration/buyer paths](QUEUE_DURATION_GROUNDING_AND_TRANSFER.md); earlier work is preserved.

## Question and common production environment

Can observed skill/qualification, buyer demand rates, and even **every pairwise** original-buyer-order/incident contingency table identify whether a full-stack firm should purchase another productive source-learning episode P, ground already licensed data into the target G, or build an independently operated embodiment E? Not necessarily. What matters may be a **third-order coincidence**: valuable original customer demand when *neither* of two distinct recovery jobs occupies the shared worker. This conditional result is a multi-job extension, not another source-data saturation parameter sweep.

The connected-cluster predispatch state is \(s_t=(Q_t,L_t,B_t,O_t,R_t,H_t)\): qualified customer service recipes, learner/model checkpoints, outstanding recovery jobs, original-buyer eligible orders and **no-orders**, lawful data-use/report rights, and actual robot/workforce resources. For admitted incidents \(\mathcal I_t\), physical worker work obeys
\[
 B_{t+1}=[B_t-c_t]_++\sum_{j\in\mathcal I_t}d_j.
\]
An action may create several incidents; the worker completes only actual feasible service \(c_t\). A target dispatch requires both a qualified/accepted original-customer recipe and feasible robot/operator slots. Cleared payments, refunds and post-service success are outcomes, **not predispatch forecasts observed clairvoyantly**.

A lawful original controller R is always optional. P can produce paid customer service and generate typed field/failure/teleoperation data and transfer to another recipe; G uses existing licensed data and target verification; E is a genuinely extra embodiment *and* independent worker/recovery resource. The model permits simulation, synthetic and public/pretrained data, all separately typed, but does not impose positive/additive transfer, known customer demand, independent qualifications, fixed hardware, or equal acquisition costs. A complete program's objective is
\[
 J_a(K)=\max_{\pi\in\Pi_a}\mathbb E_K\left[\sum_{t=0}^{T}\beta^t r_t^{\rm qualified,\ original\ buyer,\ net}-C_a\right].
\]
Future learning-created qualified and paid services enter this sum **once**, never a second continuation/data premium.

## Theorem: a common causal kernel yields exact polyhedral investment bounds

Let \(\omega\) be a finite *structural exogenous table* that specifies potential original orders, learner transitions, incidental recovery jobs, job durations, rights, safety, and paid-service outcomes for every lawful history-action. Only observed history may enter a dispatch rule: \(\omega\) may contain future outcomes that the operator does not yet know. Each table is *physically feasible* under the same conservation law. Let the **single** law across every arm and time be \(\mu\in\Gamma=\{\mu\ge0,\mathbf1^\top\mu=1,A\mu=b,D\mu\le d\}\), a nonempty compact polytope. This is a conditional structural assumption, not something identified merely by randomized arm assignments.

For each finite nonanticipative whole-program policy \(i\in\Pi_a\), let \(v_i^a(\omega)\) be its complete net paid-production payoff on that table (cost included). The known-environment optimization is
\[
 J_a(\mu)=\max_{i\in\Pi_a}(v_i^a)^\top\mu.
\]
**Proposition 1.** Sharp *oracle* difference bounds \(L\le J_P(\mu)-J_E(\mu)\le U\) over this *one* feasible \(\Gamma\) are obtainable by finitely many ordinary LPs:
\[
 L=\min_{j\in\Pi_E}\min_{\mu\in\Gamma,z}
 \{z:z\ge(v_i^P-v_j^E)^\top\mu\ \forall i\in\Pi_P\},
\]
\[
 U=\max_{i\in\Pi_P}\max_{\mu\in\Gamma,z}
 \{z:z\le(v_i^P-v_j^E)^\top\mu\ \forall j\in\Pi_E\}.
\]
**Proof.** For every common \(\mu\),
\[
 \max_i A_i(\mu)-\max_j B_j(\mu)
 =\min_j\max_i[A_i(\mu)-B_j(\mu)]
 =\max_i\min_j[A_i(\mu)-B_j(\mu)].
\]
Exchange only the two *minima* for L and the two *maxima* for U, and introduce an epigraph or hypograph variable for the remaining finite max/min. The constraints are linear. Compactness/finite policy sets ensure attained endpoints, so these are *sharp only for the specified globally feasible support*. Picking an unrelated adverse transition law for each site, date or program instead need not describe any possible worker/learner/buyer world. This is standard finite robust-decision/LP mathematics rather than a novel scalable robust-MDP solution. \(\square\)

**Implementability differs from an oracle envelope.** A deployable P controller chooses a fixed initial mixture \(x\in\Delta(\Pi_P)\) *without knowing* the unknown kernel, except for genuinely lawful and timely reports already encoded in its policies. Relative to an E oracle, its best guaranteed advantage is
\[
 C=\max_{x\in\Delta(\Pi_P)}
  \min_{\mu\in\Gamma,\ j\in\Pi_E}
 \left(\sum_i x_i v_i^P-v_j^E\right)^\top\mu.
\]
Enumerate vertices \(e\) of \(\Gamma\): maximize \(z\) subject to \(z\le(\sum_i x_i v_i^P-v_j^E)^\top e\) for every \(j,e\), with \(x\) a simplex. A *positive* C certifies one implementable P policy mixture beats even a regime-informed E alternative. An oracle upper bound U>0 does not. This is not generally a computationally efficient prescription for a large dynamic robotics fleet; enumerating all complete policies and structural scenarios may be intractable.

## Four-date structural counterexample with three generated jobs

Here is an exhaustive, fully synthetic counterexample. Existing qualified safe R pays net 2 in each t2,t3,t4 window, baseline total **6**. P source acquisition costs 1/8, whether or not its later controller chooses T. At t2 P permits R or a site-1 **qualified, accepted original-customer** productive target T with the *same net current receipt* as old R. T legally broadcasts capability that qualifies site-2 at t3 and site-3 at t4 with probability 1. R after the P source checkpoint still independently qualifies site-3 at t4 with probability 7/8; its original buyer orders with probability 1/2, giving an optional expected continuation 7/16 before pilot cost. Neither the T-specific incidents nor later buyer order is known before t2 dispatch.

At the **end** of t2 T, two separate recovery jobs enter one worker queue: J is caused by T, H comes from another site in the connected cluster. They are binary unit jobs and \(B_3=J+H\). The t3 worker clears at most one old job. With \(B_3=0\), an already qualified site-2 original buyer X=1 may be served for **incremental** net 1/2; that service creates a *third* job K=1 **after** t3 work. Alternatively the controller retains old R and avoids K. If \(B_3>0\), old R is required because the site-2 target operator is busy. Consequently
\[
 B_4=[J+H-1]_++K,\qquad
 K=\mathbf1\{\text{site-2 target actually served at t3}\}.
\]
An independent site-3 buyer may make an **original** qualified t4 order Y=1, worth increment 1 over old R *only if* \(B_4=0\). The date-3 dispatcher observes the queue and X, **not future Y**. These rules conserve all three possible recovery jobs; there is no independently sampled date-4 worker-free indicator. The complete deterministic P policies are R-after-P, T-then-wait at the free date-3 history, or T-then-serve at that history. Randomized policies are mixtures of these. Initial old R without P also remains available at increment zero.

The legal G comparator grounds already-held source data, independently qualifies target date-4 service with original-buyer order probability 5/8 and costs 1/4: \(J_G=6+3/8\). The E comparator **adds a distinct robot and operator/recovery pool** while retaining all old R, qualifies additional date-4 customer production with order probability 7/8, and costs 15/32: \(J_E=6+13/32\). The R/G/E opportunity processes are stipulated independent of the J,H,Y shock; they can be included as independent potential-outcome coordinates in **the same** structural law. These are assumed net buyer-payments and capacity—not observed contracts or an E hardware recommendation.

### A sharp law matching *all* pairwise evidence

Under t2 T, let J,H,Y each have Bernoulli(1/2) marginals and let **every one of the three pairwise two-by-two contingency tables** be uniform at 1/4 per cell. This fixes all first- and second-order binary moments but leaves one exact degree of freedom:
\[
 \Pr_\theta(J=j,H=h,Y=y)=
 \begin{cases}
 \theta/4,&j+h+y\text{ even},\\
 (1-\theta)/4,&j+h+y\text{ odd},
 \end{cases}\quad0\le\theta\le1.
\]
**Proof of exactness:** expand any three-bit distribution in Walsh/Fourier monomials \(Z_i=(-1)^{\text{bit}_i}\). Fair one-bit and pairwise independence make all one- and two-way coefficients zero. Only the third-order coefficient \(m_{123}=2\theta-1\in[-1,1]\) remains; nonnegative atom masses impose this exact interval, and the displayed parity laws attain all values. Thus the missing \(\Pr(J=H=0,Y=1)=(1-\theta)/4\) is a *third-order* original-demand/queue coincidence, not recoverable even from fully populated pairwise incident/order panels. Both extreme parity worlds have identical J/H/Y univariate and **all pairwise** distributions, T technical qualifications, each arm's costs, source data rights and customer net values. \(\square\)

### Bellman policy enumeration (no future demand lookahead)

For P-R, worker H is at most one job and is cleared by t4; after pilot cost P-R contributes \(-1/8+(7/8)(1/2)=5/16\) above baseline.

For P-T-wait, K=0. Date-4 Y can pay iff J+H is 0 or 1. Under the exact law, \(\Pr(Y=1,J+H\le1)=(1-\theta)/4+\theta/2\). Its **full** incremental net is
\[
 V_{P,T\mathrm{-wait}}-6=1/8+\theta/4.
\]

For P-T-serve, at J=H=0 a site-2 customer pays +1/2, then K blocks t4; at J+H=1 the job clears and Y may pay at t4; at J+H=2 one job remains. Its full incremental net is
\[
 V_{P,T\mathrm{-serve}}-6=-1/8+(1/2)(1/4)+\theta/2=\theta/2.
\]
When t2 T is forced, date-3 serve and wait exchange preference at \(\theta=1/2\). But once the safe P-R **option** is restored, T-wait is never globally optimal: for \(\theta\le5/8\), it is at most \(9/32<5/16\); for \(\theta\ge5/8\), T-serve strictly exceeds it. Thus the sharp full-program value is
\[
 \boxed{J_P(\theta)=6+\max\{5/16,\ \theta/2\}.}
\]
A regime-informed P controller uses t2 T and site-2 serve only at \(\theta>5/8\). A P *technical* qualification of 1 under T is held fixed across all \(\theta\); its economic contribution changes because future original demand coincides differently with two admitted recovery jobs and one newly induced job K. This is not negative transfer, and no second data premium is added.

**Sharp P/G/E ranking reversal:** at \(\theta=0\), increments obey E=13/32 > G=3/8 > P=5/16. At \(\theta=1\), P=1/2 > E=13/32 > G=3/8. Therefore the same pairwise evidence gives the **exact conditional identified** oracle bound
\[
 \boxed{J_P-J_E\in[-3/32,+3/32].}
\]
Its endpoints are attained by actual queue-feasible structural worlds and complete nonanticipative policies. P's oracle beats E precisely if \(\theta>13/16\); this threshold is **specific to stipulated example payoffs**, not a general robot investment rule.

**Deployable policy result:** absent any lawful pre-t2 signal about \(\theta\), any fixed P mixture earns at most 5/16 at \(\theta=0\), while P-R earns 5/16 in *every* regime. So P's robust absolute guarantee is \(6+5/16\), E's is \(6+13/32\), and E wins by \(3/32\) under this explicitly chosen maximin criterion. The favorable \(\theta=1\) oracle P increment of 1/2 cannot be represented as the return of a controller that knew nothing about the environment. Conditional information about \(\theta\) acquired early enough can change this decision, but a postcommitment report cannot change the already purchased embodiment.

## Evidence and contribution boundary

The intervention-relevant estimand is a **whole original-buyer panel**, especially \(\Pr(Y=1,J=H=0\mid\mathrm{do}(T),\text{lawful qualified cluster})\), including *orders and no-orders from customers that never received service*. A selected successful-service log loses precisely the queue-blocked offers needed to identify it. Prospective data must include separate job IDs and durations J,H,K, service/discharge timestamps, at-risk/available operator capacity, legal cross-site rights, learner checkpoint/version and independently validated Q, original-buyer eligible order/no-order timestamps, accepted and rejected output, cleared receipts and refunds, and the actual t2/t3 policy observation clock. Without supported T-versus-R or P/G/E interventions, all four program causal distributions remain counterfactual; signed rights and independent E resources are not identifiable from a vendor demonstration.

The [unpopulated identification protocol](GLOBAL_MULTI_JOB_ORIGINAL_BUYER_EVIDENCE.md), exact Python Fraction model/output, independent Node BigInt queue audit, [replication instructions](GLOBAL_MULTI_JOB_REPLICATION.md), and separate [exercises](GLOBAL_MULTI_JOB_EXERCISES.md) and [instructor solutions](GLOBAL_MULTI_JOB_SOLUTIONS.md) accompany the argument. Alternative worker service capacities, no K generated by t3 service, revocation of training rights, buyer substitution across sites or changing accepted contract prices all require **recomputing** the structural kernel and policy bounds. No general positive or additive technical-transfer assumption is necessary, nor does optional free data alone lower optimized value if the old menu remains available.

Existing foundations explicitly include Farboodi–Koh–Xia [*Data-Driven Automation* (2026)](https://arxiv.org/abs/2606.10127), which **already** values future data and complementary aggregation; Iyengar [robust DP (2005)](https://doi.org/10.1287/moor.1040.0129); Li–Kuhn–Sutter [nonrectangular robust MDPs, published February 9, 2026](https://doi.org/10.1137/24M1631250); and Li–Shapiro [rectangularity/duality, published November 2025](https://doi.org/10.1007/s10107-025-02297-y). Fourier expansions, finite policy LPs and queue conservation are standard mathematics. Candidate synthesis: *typed lawful data source → joint transferable qualification → changing original customer orders × physically conserved incident/workforce history → qualified net paid production → implementable capital allocation*. Neither scientific originality nor any measured robotics return has been independently established.

**Status, 22 Nov 2026:** No physical authorized P/D/G/E comparison, original-buyer accepted/cleared panel, verified cross-site training permission, actual observed multi-job transition law, measured separate E worker resource, or new verified numerical BEA/BLS interindustry input–output coefficients. November 22 Models A/B scientific acceptance stays **OPEN**. Next proof/evidence gap: replace the fully stipulated pairwise parity family with *observationally supported, selected/censored original-buyer and shared-operator cross-arm structural support*, and test real policy implementability under simultaneous learner, buyer and worker responses. Preserve ~60–70% theory emphasis through December 6, full empirical/production/ownership/manufacturing roadmap, November 29 and later milestones, and December 25, 2026, 23:59 America/New_York delivery.
