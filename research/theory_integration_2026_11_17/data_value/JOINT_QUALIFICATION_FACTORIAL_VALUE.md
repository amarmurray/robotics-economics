# Causal data-source/grounding value under joint qualification and whole-network production

**18 November 2026 Eastern / 19 November UTC. Private continuation of When Capabilities Become Production.** This chapter is a constructive synthesis of the existing source-to-qualification model, policy-induced target support, and paired continuation bounds. It does **not** establish scientific novelty, safe robot deployment, a causal estimate, or a dataset price. It explicitly preserves DDA section 5 and Appendix B as prior work on production/data feedback and aggregation.

## The same question, a second identification route

We need to decide whether acquiring more source data, performing target-specific grounding, or changing the embodiment makes **additional qualified customer production** economical. The existing paired first-exit analysis asks whether matched learned policies have sufficiently common post-exit whole-network outcomes to justify a nontrivial discrepancy cap eta. No signed controller/customer/operator dataset has yet established that condition. Repeating hypothetical eta values cannot resolve it.

There is a **different prospective identification route**: compare complete, physically approved source/no-source and grounding/no-grounding policies across genuinely independent **policy-closed** customer networks. Randomization identifies the economic *average intervention interaction* directly, allowing training to change joint qualification, visited target states, recovery, resource contention, original B orders, and future demand. This does not identify a universal transfer coefficient, site-specific advantage or unsupported policy, and it does not license a trial without physical approval. If there are no independent networks, the earlier partial-identification/structural certificate remains necessary.

## Environment and economic objective

Fix a pre-treatment population of customer opportunities and a finite service horizon, including existing B orders, prospective A opportunities, all cancellations and non-attempts, alternative specialists, and resources. Let z=(x,g,h) specify a development/deployment policy history: x denotes a **prespecified source-use training intervention** (not mere free availability); g is an independently specified target grounding/alignment intervention; h selects an existing or redesigned embodiment. Source categories are not collapsed: productive field trajectories, failure/recovery examples, deliberate teleoperation, simulation, synthetic generation, and public/pretrained corpora are different treatments with different rights, selection, curation, compute and lost-service costs.

The resulting complete history has a joint qualification set Q_z, learned policy-dependent occupancy, controller and operator/dispatch behavior, and customer response. Its admissible customer-production policy includes only independently physically approved controllers, fallback and qualified service recipes. A failure to qualify is a realizable outcome with retained approved alternatives; it is **not** permission to execute an unsupported target action.

For a fixed embodiment h and an arm z=(x,g), let pi_z(q) be the **joint** probability of qualified recipe configuration q, defined on a common finite union of qualification labels. Let f_z(q) be the optimized, gross, captured **whole-network** customer contribution at q over the given horizon with demand, original-order displacement, resources and fallback under arm z. Costs c_z include acquisition, rights/curation, training, validation, replacement hardware, opportunity losses and support where not already charged to f_z. The one-count identity is

    J_z = sum_q pi_z(q) f_z(q) - c_z.

For dynamic experiments q may encode a complete qualified trajectory/state: this is a law-of-total-expectation representation of the existing dynamic J, not a claim that training changes only a terminal skill. Any continuation benefit from production-generated data is already in f_z or the transition model, never added again as a free-standing data premium. Actor-specific liquidity affects which programs can be implemented; customer welfare is not automatically captured provider value.

The realized economic source-grounding interaction at embodiment h is

    I_h = J_11,h - J_10,h - J_01,h + J_00,h.

It need not be positive. A source can improve a benchmark and fail to change accepted customer production; an apparently valuable qualified bundle may displace a more valuable B order or overload the shared operator. This interaction is a property of the **entire customer-production intervention**, not a constant source-to-skill transfer coefficient.

## Proposition: exact joint-qualification / service-response accounting

For fixed h, let s_11=s_00=+1, s_10=s_01=-1 and reference value table f_00. Then

    I_h =
      sum_q [pi_11(q)-pi_10(q)-pi_01(q)+pi_00(q)] f_00(q)
      + sum_z s_z sum_q pi_z(q)[f_z(q)-f_00(q)]
      - [c_11-c_10-c_01+c_00].

The identity follows by adding/subtracting sum_q pi_z(q)f_00(q) in each J_z and collecting signs. The first term is a **joint qualification-distribution interaction valued at reference whole-service economics**; the second is a **policy-specific response of the whole optimized production table**, which can include demand, controller fallback, resource and order interactions; the third is the nonadditive cost of implementation. Each can have either sign, and the split changes if another reference f is chosen. In particular, it is a bookkeeping identity, **not** an identified mediation decomposition. Values f_00(q) for qualifications reachable only under treated arms can be unobserved; different counterfactual extensions give different component assignments while leaving the total I unchanged.

This matters because the original exponential source map with conditionally independent qualifications makes the derivative of joint outcomes a product of marginal derivatives. That is one **conditional benchmark**, not a general theorem about deployment qualification. In the current model, pi_z is a full joint law, potentially including correlated successes, co-failures, and a body-specific set of reachable recipes. Individual qualification pass rates do not identify pi_z and hence do not identify I_h.

### Constructive sign reversal without changes in marginal qualification rates

Let q comprise two binary qualifications, each having marginal pass probability 1/2 in **every** arm. In arms 00, 10, 01 they are independent, giving probability 1/4 of both passing. In arm 11 two distinct feasible technical worlds have the exact same marginals: perfect positive dependence gives both with probability 1/2, while perfect negative dependence gives both with probability 0. Suppose a single accepted customer recipe pays gross 4 normalized units only when **both** qualify; costs and other responses are held fixed. The observed arm-level factorial interaction is respectively +1 or -1 normalized unit. Both worlds have the same per-skill pass rates in all four arms. Thus even unlimited precision about those marginals cannot determine the sign of the economic data/grounding interaction. The different **joint** probabilities, not an independently estimated data-price factor, explain the sign.

The complementary qualification and shared-resource countermodels are also distinct. With deterministic skills unlocked separately by x and g, a bundled service with contributions [J_00,J_10,J_01,J_11]=[0,0,0,3] has I=+3. If either qualified service independently earns one unit but both compete for one scarce robot/operator, the optimized values [0,1,1,1] yield I=-1 with no negative technical transfer. With an original B contribution of 2 under 00/10/01, a newly A-qualified 11 action that produces A=1 but displaces B=2 makes total values [2,2,2,1], I=-1 even though the **local A-only** comparison is positive. These are constructed production tables, not measured deployment numbers.

In a separate exact joint-law example, reference production pays 4 only for joint qualification. With independent laws in 00/10/01 and perfectly positively associated qualifications in 11, the qualification interaction equals +1. If the 11 policy's complete-service table pays only 2 for that same qualified bundle because of network/demand displacement, the production-response term equals -1, so **net interaction is zero** and each arm has value 1. This is a particularly useful falsifier of “technical source complementarity implies profitable data complementarity.”

## Proposition: what a fully admitted factorial comparison identifies

Let k index independent, prospectively delineated **policy-closed customer networks**, not individual robots or individual service records. A cluster's potential economic result Y_k(z) is the captured complete network contribution, including qualified A service, retained B orders, demand feedback, cancellations, all operator/recovery costs and relevant development expenses. Suppose all four policies are physically approved before assignment, each cluster is eligible for each arm, the opportunity population/clock is specified before assignment, assignment probabilities are positive and known, and no controller updates, learning, shared operator or customer demand spillovers cross cluster boundaries. Assume assignment does not affect another cluster's potential contribution.

Under independent assignment with probabilities e_k(z)>0, the Horvitz–Thompson arm mean

    mu_hat_z = (1/N) sum_k 1{Z_k=z} Y_k / e_k(z)

has randomization expectation (1/N)sum_k Y_k(z). Consequently mu_hat_11 - mu_hat_10 - mu_hat_01 + mu_hat_00 is unbiased for the average whole-network intervention interaction. The same conclusion holds for known-probability complete randomization with the corresponding design weights. It **does not require** a common unsupported post-exit residual eta or independence of joint technical qualifications. It estimates an average effect for the sampled approved network population, not a guarantee in every market, a safety certificate, or the separately reported technical/data mechanisms.

If an arm is not safely admissible, its physical contribution is not an available deployment choice. Randomizing only offline training while leaving the retained controller in charge identifies offline qualification changes but **does not** identify the target policy's accepted-service economic payoff. If a policy has an eligible but unobserved arm with outcome bounded Y∈[L,U], and the other three arm means are identified, the factorial interaction can only be bounded by

    [L-mu_10-mu_01+mu_00, U-mu_10-mu_01+mu_00],

absent other restrictions; the bounds are sharp in the unconstrained potential-outcome class. This missing-cell result must never be interpreted as approval to randomize unsafe machinery.

**Critical failure mode:** if all “clusters” draw updates from a common learner, customer orders shift across sites, or dispatch/operator resources cross boundaries, randomizing them separately does not identify the above policy-level estimand. Assignment changes the **interference closure**. A complete-network intervention may need to encompass the whole market, with too few independent markets for a useful experiment. The earlier matched-policy eta bound remains meaningful only if independently justified; neither route can be declared identified by naming a robot pose or an RL baseline policy.

## The new embodiment is a changed feasible technology, not an extra skill score

For h=old and h=new, define I_h only for independently admissible policies at that embodiment. Their difference is a three-way discrete interaction, but it also reflects changed physical feasibility, installed capacity, failure/recovery, customer acceptance and training rights. It is not a “cross-embodiment transfer percentage.” A defensible comparison first records whether h reaches a previously impossible **complete service recipe** with economically available customers and bounded resource/cash costs. Then compare the **optimal approved policy menu**, including retained F and competent specialist S, over identical customer opportunity horizons. If no new-body arm is approved, preserve it as a qualification/research option and do not project deployment income from simulator accuracy.

**Optionality boundary.** If free source access simply adds the option to train or deploy while retaining every old policy, the optimized value cannot fall: max over an enlarged feasible menu is weakly greater. A **forced** source-trained rollout can have lower J, and costly acquisition can have negative net option value. Likewise optional data access does not imply a nonnegative source-grounding factorial interaction. This is set inclusion, not new theory.

## Empirical consequences and relation to the current eta question

One prospective factorial comparison can identify whether data copying and target grounding interact in **accepted production**, provided all network and approval assumptions truly hold. Separate intermediate records can then investigate whether the effect came from joint qualification, learned occupancy, customer demand, original-order displacement or costs. The exact decomposition terms are *not* independently causal without reference-policy counterfactual support. Capture original B orders before assignment; count dropped or unattempted services; record all four arms' own controller hashes, qualification bundles and target first-exit occupancy; distinguish read-only source copying from use in training and from a post-admission shared-controller update.

This is complementary to—not a replacement for—the previous paired comparison. The eta method can certify a particular same-world contrast if architectural/matched evidence justifies its residual set. The factorial method can identify a population average without eta if **multiple independently randomized whole networks and safely admitted arms** exist. Neither is currently demonstrated. If neither is feasible, the honest answer remains partial identification, a retained approved policy and a staged target-support research decision rather than an invented economic data valuation.

### Closest prior work and scope of claim

Farboodi, Koh and Xia, *Data-Driven Automation*, arXiv:2606.10127 (2026), section 5 and Appendix B, already treat dynamic economic data value and complementary data accumulation: https://arxiv.org/abs/2606.10127. Laroche, Trichelair and Tachet des Combes, *Safe Policy Improvement with Baseline Bootstrapping*, ICML/PMLR 97 (2019), provide previous offline baseline-bootstrapping ideas: https://proceedings.mlr.press/v97/laroche19a.html. Classical factorial randomization, potential outcomes, multilinear probability models and interference restrictions are prior foundations. Our current contribution is an **internally coherent accounting and empirical falsification architecture** for source, grounding and embodiment decisions inside qualified whole-network production, not a proven novel estimator or observed robotics effect. [Proof ledger](JOINT_QUALIFICATION_FACTORIAL_PROOFS.md), [prospective protocol](JOINT_QUALIFICATION_FACTORIAL_EMPIRICAL.md), [executable synthetic check](joint_qualification_factorial.js), [recorded results](joint_qualification_factorial_results.json), [exercises](JOINT_QUALIFICATION_FACTORIAL_EXERCISES.md), and [separate solutions](JOINT_QUALIFICATION_FACTORIAL_SOLUTIONS.md) accompany this chapter.

**Status:** No signed deployment lineage, physically approved four-arm network experiment, matched original B order ledger, valid eta<width, BEA–BLS numerical opportunity crosswalk, independent review, or empirical measured robotics outcome. November 22 synthesis, November 29 empirical backbone, December 6 contribution choice and December 25 23:59 Eastern edition gates remain open.
