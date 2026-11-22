# Adaptive recovery queues as a constraint on economic data transfer

**22 November 2026; continuation of *When Capabilities Become Production*, integrated Models A/B.** A conditional finite-horizon theoretical derivation, not a measured robotics result or an independently validated novelty claim. November 22 scientific acceptance remains OPEN. It extends [single-job duration/path transport](QUEUE_DURATION_GROUNDING_AND_TRANSFER.md) and [shared learner/worker carryover](WORKER_CARRYOVER_NETWORK_AND_VALUE.md), without canceling either.

## Exact question

What changes when an economically productive target dispatch both generates transferable learner data and creates a *new* recovery job that obstructs subsequent paid production, while original customers change their ordering behavior in response? The previous one-job restriction implied a nested free-worker path F2<=F3. After new incidents, the worker can become busy again: that nesting is false. We require a **joint nonanticipative causal production kernel**, not independently optimized t2 and t3 worker-availability or customer-order marginals.

## Common full-program environment

A finite connected cluster state at decision date t is s_t=(Q_t,L_t,B_t,O_t,R_t,H_t), comprising target recipe qualification Q, learner/model checkpoint L, outstanding recovery workload B, the *predispatch* original-buyer order and no-order panel O, legal rights R, and robot/worker/production resources H. The worker queue updates through the physical law

    B_(t+1) = [B_t - c_t]_+ + sum_(j in newly admitted incidents at t) d_j.

Here c_t is actual feasible worker service, not an independently assigned utilization probability. New jobs are generated only by feasible actions and outcomes. Training and demand have action-dependent, potentially correlated transition maps

    Q_(t+1) = Phi(Q_t,L_t,lawful_data_t,action_t,xi_t);
    (L_(t+1),O_(t+1)) = Psi(L_t,O_t,Q_(t+1),action_t,xi_t,zeta_t).

Shared disturbances can affect learner broadcasts, buyer orders, and worker recovery. We do **not** impose independent site qualifications, positive transfer, fixed demand, fixed hardware, or universal data-source saturation. Source field trajectories, failure/recovery traces, teleoperation, simulation, synthetic and public/pretrained inputs remain separate typed lawful inputs to Phi. At each site, only *qualified and accepted customer service* can yield a prospective contractually expected paid net reward; cleared settlements/refunds are measured after dispatch, never observed clairvoyantly beforehand.

For program a in {R,P,G,E} and a fully specified physically and legally admissible joint kernel K, define

    J_a(K) = sup_(lawful nonanticipative pi in Pi_a) E_K[sum_t beta^t paid_net_t - actual program/operating costs].

R is the retained safe productive controller; P can generate paid field data and recovery jobs; G lawfully grounds already-held source data; E buys a genuinely extra robot and *independent* recovery/operator capacity. These choices differ in resources, effects, and costs, but are valued in the SAME future customer-production objective. A stagewise Bellman recursion over the full state is valid for a fixed known kernel K; no second continuation/data premium is added.

When available evidence describes a set Gamma of **globally compatible** action-conditioned joint kernels, the sharp *fixed-environment optimized-program* P-E difference is

    [ min_(K in Gamma)(J_P(K)-J_E(K)),
      max_(K in Gamma)(J_P(K)-J_E(K)) ].                 (1)

This is sharp when Gamma is precisely the compact set of all lawful feasible kernels and the finite model has attained optimizers. The same K must govern every program comparison. Different ad hoc adverse transition rows selected for each arm need not correspond to any feasible environment. Equation (1) is *not* the value of an implementable controller ignorant of K: that requires an ex-ante policy, e.g. max_pi min_(K in Gamma) V_a^pi(K), with a specified information clock. A shared nonrectangular Gamma generally precludes naïve stagewise robust Bellman minimization.

## Constructive two-site, three-date example with a newly generated recovery job

All contributions below are synthetic *normalized customer-production net units*, never technical benchmark percentages interpreted as dollars. Dates 2 and 3 each supply retained safe R production worth 2 on the existing robot; baseline is 4. Rights, safety/qualification gates and original eligible-buyer orders are assumed licensed and verifiable, **not observed in reality**.

**P source field pilot.** Before learning future outcomes, a t1 P field pilot costs 1/4 relative to retained safe production and qualifies a site-1 target recipe at t2. Its first recovery job D is one or two windows long, each with probability 1/2. The original site-1 buyer orders at t2 (U2=1). At t2 if D=1 the shared worker has recovered and target T is feasible on the existing robot; if D=2 only R is feasible. Both histories are observed by the t2 dispatcher. D<=2 ensures initial recovery is over by t3.

Choosing T at t2 (when feasible) raises *current* expected net customer contribution by 1/8 relative to R, makes a legally broadcast training checkpoint qualify a **different site-2 recipe** at t3 with probability 1, and changes original site-2 demand to Pr(U3^T=1)=3/4. But T produces a new worker recovery job J in {0,1}, with Pr(J=1)=1/2; J=1 makes that one shared worker unavailable at t3. The target t3 gain of 1 over R is payable only when the new site-2 customer actually orders AND J=0. No target acceptance/settlement information is available before that service.

Choosing retained R at t2 produces no new job. The existing source checkpoint nonetheless leaves the site-2 recipe qualified at t3 with probability 4/5, and the original site-2 buyer orders with probability 5/8; these independent *R-action* outcomes produce target eligible-demand probability exactly 1/2, with t3 worker available. These R-action marginal assumptions are not extrapolated from observed T-service successes. The source pilot can be retained without forcing T. Notice the T action improves both the target qualification marginal (4/5 to 1) and the buyer-order marginal (5/8 to 3/4), but may still tie up the scarce recovery worker.

Write z=Pr(U3^T=1,J=0 | t2 T, D=1, U2=1). This is one policy-specific *original customer demand AND nonbusy worker* intersection. The two known T-action marginals give the sharp Frechet range 1/4<=z<=1/2. A complete coherent table is

| t3 original buyer U3^T | t2 new job J | joint probability |
|---|---|---|
| 1 | 0 | z |
| 1 | 1 | 3/4-z |
| 0 | 0 | 1/2-z |
| 0 | 1 | z-1/4 |

The table is nonnegative exactly on that range. The physical queue update is B3=J if D=1 and T was chosen; otherwise B3=0 (the original D job has cleared). It never invents an independent t3 availability bit. Under D=1, t2 R yields incremental continuation 1/2, while T yields 1/8+z. Thus the t2 decision is T iff z>=3/8 (ties arbitrary). For D=2 only R is available. Taking the t1 pilot cost and all downstream safe production into account,

    J_P(z) = 4 - 1/4 + (1/2)(1/2) + (1/2) max{1/2, 1/8+z}
           = 4 + (1/2) max{1/2,1/8+z}.               (2)

**Proof.** Condition on the observed D; D=2 consumes the worker through date 2, but not date 3, and forces t2 R with exactly 1/2 expected eligible target continuation. If D=1, both t2 actions are lawful: R preserves a 1/2 future target increment without a new job; T yields current incremental 1/8 and future gain only on U3^T=1,J=0, of probability z. There is one physical t2 target robot/worker service and at most one t3 target service, so Bellman maximization gives (2). The exact joint table supplies every endpoint and intermediate z; hence J_P has a sharp conditional identified interval [17/4,69/16] and not merely an outer algebraic bound. The derivative with respect to z is zero below 3/8 and 1/2 above 3/8, with a nondifferentiable policy switch. These are conventional finite Bellman and Frechet results, not a universal capability-scaling law.

**G licensed target grounding.** Already-held lawfully reusable source data is grounded and verified, with t2 retained R and no worker incident; a qualified t3 target order occurs with probability 7/10. Incremental grounding/verification cost is 21/50, giving full J_G=4+7/10-21/50=107/25. G does not add a robot or claim to have generated P field data.

**E independent embodiment.** The old robot preserves both R services; an additional qualified body and independently resourced worker can deliver a site-2 t3 order with probability 9/10, worth 1 extra net unit when served. Full lifecycle program cost is 3/5, so J_E=4+9/10-3/5=43/10. An E arm without *both* physically independent resources cannot use this payoff.

At z=1/4, P=17/4 < G=107/25 < E=43/10. At z=1/2, P=69/16 > E=43/10 > G=107/25. Both worlds have *identical* D distribution, T site-2 qualification, T original-buyer-order frequency, T incident frequency, R counterfactual recipe/demand marginals, program costs and full qualified target prices. They differ only in **when original demand coincides with recovery availability**. This is an action-induced data-and-capacity interaction, not negative technical transfer, a newly invented data premium or an empirical P/G/E recommendation.

## The information and implementation distinction

For a controller knowing the true z, (2) is the correct optimal policy value. If z is not identifiable from lawful original-buyer and worker joint exposure, and no admissible early report reveals it, a t2 dispatcher must choose ONE rule across all compatible worlds. If x is the probability of T conditional on D=1, with no other distinguishing signal, then

    J_P(x,z) = 17/4 + (x/2)(z-3/8).

Its lower envelope on [1/4,1/2] is 17/4-x/16. Therefore the sharp absolute maximin P policy sets x=0 and achieves 17/4. An environment-tailored P oracle can obtain 69/16 in the favorable world; that is not a guaranteed attainable outcome for one uninformed dispatcher. In the specified synthetic, robust absolute program ranking E=43/10 exceeds this maximin P result; any Bayes or regret ranking requires an explicit prior/report/commitment timing model. More data can have zero *actionable* value when rights or the observation clock prevent a policy improvement.

## Evidence, prior art and falsifiers

The required [prospective original-buyer and shared-job protocol](ADAPTIVE_QUEUE_LEARNER_DEMAND_EVIDENCE.md) asks for *both* eligible t2 orders and no-orders, signed P/G/E and old R rights, action-specific site-2 qualification, T versus R original orders, incident arrival/duration, queue service/discharge, separate embodied resources and after-service acceptance/cleared net payments. Observe those for whole randomized or otherwise credibly identified connected clusters, not selected successful robot episodes. Neither the T-action marginals nor a site-3 benchmark alone determines z. The theorem fails if incidents are hidden, jobs can be cleared out of sequence without observed queue discipline, the target t3 service itself consumes more future windows, qualified prices change with unmodeled contracts, or the presumed legal broadcast is unavailable. A longer multiple-job queue is modeled by the general state equation, not by pretending this one-new-job example solves it.

Prior foundations: Farboodi, Koh and Xia, *Data-Driven Automation* (2026, https://arxiv.org/abs/2606.10127), already models future data value and complementary aggregation; Iyengar, *Robust Dynamic Programming* (2005, https://doi.org/10.1287/moor.1040.0129), and Nilim & El Ghaoui (2005, https://people.eecs.berkeley.edu/~elghaoui/pubs_rob_mdp.html) establish robust-DP foundations and the rectangularity issue. Li, Kuhn & Sutter (2026, https://doi.org/10.1137/24M1631250) analyze nonrectangular robust MDPs. Fleet-level learning demonstrations, e.g. *Learning while Deploying* (2026, https://arxiv.org/abs/2605.00416), are technical motivation, **not** paid original-buyer economics or evidence for these stipulated transitions. The candidate synthesis is to embed action-generated learning, offers and recovery workload in one qualified-production choice; scientific originality remains unreviewed.

**Validation status.** [Exact executable](adaptive_queue_exact.js), [recorded synthetic output](adaptive_queue_exact_results.json), an independent Fraction derivation and separate [exercises](ADAPTIVE_QUEUE_EXERCISES.md)/[solutions](ADAPTIVE_QUEUE_SOLUTIONS.md) accompany this conditional proof. No real approved physical cluster experiment, cleared paid original-buyer panel, lawful shared-model broadcast, proven independent E resources, or official numerical BEA/BLS interindustry coefficients. November 22 integrated Models A/B scientific gate stays OPEN. Next substantive step: test whether *multi-job* workload, action-varying service rates and latent shared incidents permit an economically useful **globally nonrectangular** yet identifiable P/G/E ranking certificate, with credible original-buyer counterfactual support. Theory majority through December 6; final target December 25, 2026, 23:59 America/New_York.