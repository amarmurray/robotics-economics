# One shared learner and recovery network: nonrectangular economic-data investment comparisons

**22 November 2026.** Continuation of *When Capabilities Become Production*, November 22 Models A/B gate **OPEN**. Same source-trained/target-grounded/productive versus deliberate-data versus embodiment production argument; not a detached model and not a scientific novelty claim. All numerical receipts below are explicitly **synthetic normalized fully net, accepted-and-cleared customer contributions**, not observed customer outcomes, robotics estimates, technical scores or dollar forecasts.

## Precise open question

The preceding [decision-sensitive network theorem](DECISION_SENSITIVE_NETWORK_PRODUCTION.md) represented the economic consequence of full learner, original-buyer and shared-recovery transition errors with a signed Bellman residual. Its optimization bounds required a jointly feasible class C of complete network laws. But treating each signed policy/action/site/program's uncertainty independently creates transition matrices which cannot all arise from one foundation-model broadcast, one operator recovery roster and one original market. Can an actual common physical uncertainty model identify the **sign** of a prospective learning-versus-embodiment economic comparison even if absolute original-customer return is not identified?

This chapter gives one tractable, deliberately stringent answer: a whole-connected-cluster **exogenous common-factor mixture**. It also establishes what it does *not* prove: robust ranking of optimally tailored programs need not supply a single implementable policy when the common factor is unknown.

## 1. Common production and lawful state

Let a range over R (retained controller), P (production-generated source trajectories and paid field episodes), D (deliberate/teleoperation/target-grounding acquisition), SG (source learning with target alignment), and E (new qualified embodiment/physical capacity). A connected cluster includes two or more original buyer-service windows, model broadcast, site/worker/recovery resource, rights, provenance, manufacturing slots and feedback in future original demand. A lawful adaptive policy pi uses only its timely authorized observation history; no hindsight access to latent customer, safety or licensing information.

A complete conditional accepted/cleared contribution under program a is

    v_(a,pi,z) = E[sum_(t=0)^(T-1) beta^t r_t^a(H_t,U_t) - I_a | do(a,pi), Z=z].

Here r includes customer receipts or refunds; forgone or displaced service; qualified delivery; physical dispatch; teleop and recovery; compute, curation, rights and operating costs. The up-front cost I_a occurs once. Newly qualified later buyer services are included within the same finite-horizon contribution, not added again as a speculative data premium. Each source type remains distinct in the transition kernel (field successes, failures and recoveries, teleoperation, simulator, synthetic and public/pretrained sources). If old R remains physically and legally executable it remains an option in the P menu. After an irreversible E purchase, the retained dispatch policy may still pay sunk embodiment acquisition cost.

**Connected structural restriction.** The latent Z in {0,1} is drawn **once per whole connected cluster/horizon** from Pr(Z=1)=theta, theta in a substantiated closed interval I. Conditional on Z=z and the fixed program/policy, all multi-site demand offers, shared checkpoint updates, rescues, licenses and settlement transitions have a single specified joint causal law K_(a,pi,z). The broadcast or roster shock is **not** separately resampled for each site, action or arm. An intervention can change conditional original-customer demand, qualification and resource response, so K_(P,z) need not equal K_(E,z). The *exogenous prevalence theta*, not conditional posttreatment state or demand, is assumed invariant across compared programs.

This is a **model assumption** needing support, not a claim that shared-model fleet operations are always two-type or have known conditional laws. If a source or embodiment intervention changes the exogenous factor's prevalence, or model updates spill between supposed independent clusters, the common-theta comparison below is inadmissible and must widen.

Conditional on a fixed legal full-history policy pi, its complete expectation is affine in the common mixture:

    J_(a,pi)(theta) = (1-theta) v_(a,pi,0) + theta v_(a,pi,1).

Let Pi_a be the finite set of lawful deterministic policies (including entire adaptive contingent decisions; finite state, time and signals). Randomization gives convex mixtures but cannot improve a known-theta expected-value maximization. Define

    J_a*(theta) = max_(pi in Pi_a) J_(a,pi)(theta),
    Delta_(P,E)(theta) = J_P*(theta) - J_E*(theta).

These are *parameterwise full-program optima*, not the max-min result for an operator who does not know theta. The same factor prevalence couples both program values; do not take its minimum for P and maximum for E at two physically different theta values when claiming a **sharp** difference bound.

## Proposition 1. Exact common-factor economic envelope

For a finite lawful policy class with conditional complete outcomes v_(a,pi,z) invariant in theta, each J_a* is continuous convex piecewise affine in theta. On closed I=[l,u], the sharp min and max of Delta_(P,E) occur among l, u and the in-interval pairwise intersections of policy-value lines **within each arm**. Thus a finite set of attainable common-theta worlds gives an exact investment-ranking interval. Its lower endpoint is at least

    min_(theta in I) J_P*(theta) - max_(theta in I) J_E*(theta),

and can be strictly higher. The independent-extrema expression is a safe *outer* bound under common theta but is not sharp; a rectangular optimization that purports it is sharp can manufacture mutually incompatible network mixtures.

**Proof.** For fixed pi, the law of total expectation under one exogenous Z gives the displayed affine form even if conditional within-regime dynamics are multi-date, adaptive, interference-rich and non-Markov in a compressed state. A maximum of finitely many affine functions is convex, continuous and affine between line-crossing points. On every interval in the union of the two programs' breakpoints, the difference of their two maximizers is affine, so its extreme lies at an interval endpoint. All candidate theta values belong to I and therefore respect the same shared-factor law for every program. For any theta, J_P*(theta) is no lower than min_I J_P* and J_E*(theta) no greater than max_I J_E*. Taking the minimum proves the outer inequality. QED.

There is no permission here to apply a Bellman minimization that changes theta independently after every history. In this common-parameter nonrectangular class, nature picks one exogenous whole-network model before the horizon; robust control under uncertainty about theta is a **commitment/belief-state problem**, not generally a rowwise rectangular recursion. This is standard robust-DP structure, not newly invented theory.

## Proposition 2. Why a positive optimized ranking need not identify an executable controller

Even if Delta_(P,E)(theta)>0 at **every** theta, there need not exist a single initial lawful P policy, or any fixed randomization over P policies, whose contribution exceeds the theta-specific E optimum for all theta. A program-level superiority claim assumes either that theta is known when its optimal P policy is selected, or that a lawful learning/reporting policy can adapt sufficiently; it cannot silently replace a program optimizer by one logged dispatch rule.

**Proof by explicit counterexample below.** The P mixture of retained and productive pilot requires contradictory mixing probabilities at theta=0 and theta=1 to beat E's theta-tailored policy. It follows that the *information about the shared environment needed to choose a data-acquisition policy* is itself an economic input. Its acquisition cost, legal observation timing and induced demand/learning transitions belong in J, not in an independent report dividend. QED.

For completeness, a sufficient but nonnecessary pointwise dominance condition is: for each E policy sigma, there exists a P policy pi (possibly depending on sigma, but not on latent Z) such that v_(P,pi,z) >= v_(E,sigma,z)+delta at both z=0 and z=1. Taking expectations and maxima gives Delta>=delta. The exact envelope proposition may certify a positive delta even when this stronger statewise cover fails.

## 2. Constructive two-site, common-broadcast/recovery example

One shared whole-network exogenous regime Z=0 represents lower original demand, lower transferable C opportunities and a tighter recovery roster; Z=1 represents favorable original demand and technically usable common learner updates. Two old original-buyer service streams yield 2 (bad) and 4 (good) normalized accepted/cleared contributions using retained qualified R. P can instead invest in production-generated field data, using legitimate customer work and future qualified C service when Z=1, but sacrificing service/recovery effort when Z=0. An E purchase pays 0.1 sunk manufacturing cost even when using R; its independent capacity mode yields an extra original buyer service when Z=1 but incurs cost while unused when Z=0. These descriptions merely **construct an internally possible payoff table**; no physical comparison or causal validation is asserted.

| Full-program lawful policy | Z=0 (net) | Z=1 (net) |
|---|---:|---:|
| P: retain old R, decline new source investment | 2 | 4 |
| P: customer-paid field source/data pilot, later qualified new service | 3/2 | 5 |
| E: operate R after embodiment capex | 19/10 | 39/10 |
| E: use genuine independent embodied capacity | 3/2 | 9/2 |

Every entry includes complete program cash opportunity and resource costs. No policy is forced to train on an apparently harmful dataset. Both E alternatives include the embodiment commitment; comparing P's free option to E's sunk investment is intentional.

Consequently,

    J_P*(theta) = max{2+2theta, 3/2+(7/2)theta},
    J_E*(theta) = max{19/10+2theta, 3/2+3theta}.

P switches from retained R to productive field learning at theta=1/3; E switches from R to additional embodied capacity at theta=2/5. Their **sharp common-model gap** over theta in [0,1] is [1/10,1/2]. The gap is 1/10 at 0 and 1/3, 1/5 at 2/5 and 1/2 at 1. Thus P's fully optimized program wins at every admissible common factor prevalence, despite the separately optimized extrema only giving

    min J_P* - max J_E* = 2 - 9/2 = -5/2,

which cannot certify the sign. This difference is **not** a newly estimated robot return: it is what preserving a physically shared uncertainty parameter achieves in an illustrative paid-production table.

**Operational limitation with economic force.** Let rho be any precommitted probability of using P's productive pilot, without observing theta. At theta=0, its expected payoff is 2-rho/2. To match E's tailored optimum 19/10, rho <= 1/5. At theta=1, its payoff is 4+rho. To match E's tailored optimum 9/2, rho >= 1/2. Both conditions cannot hold. Even weak uniform implementable dominance fails without obtaining the requisite information or accepting an explicit decision-risk criterion. The example **does not certify an unknown-theta P deployment choice**, even though it certifies the *pointwise optimized-program* ranking under its joint response assumptions.

**Exact ex-ante policy distinction.** Against an E benchmark allowed to optimize separately at every unknown theta, a fixed P pilot mixture rho has endpoint gaps 1/10−rho/2 at theta=0 and −1/2+rho at theta=1. Since the difference between its affine contribution and E's convex envelope is concave, the worst theta lies at an endpoint. Equating the endpoints gives the optimal hedging mix rho=2/5 with **maximin relative gap −1/10**: no fixed P mix uniformly beats that hindsight E benchmark. This is an **information-asymmetric regret comparison**, not the choice between two equally uninformed programs. If both arms must precommit and each maximizes its own worst absolute receipt, P retains R and guarantees 2 versus E's 19/10. The difference between these legitimate decision criteria is substantive: neither the positive pointwise optimized gap nor the negative asymmetric regret is a context-free investment recommendation.

**Counterexample to pretending a common factor itself guarantees a ranking.** Change only E's independent-capacity conditional net row to (11/5,9/2), representing a different original-buyer access/capacity structure with identical factor prevalence. E capacity then beats its own R row across regimes. P−E is negative at theta=0 (−1/5), positive at theta=1 (+1/2), and equals zero at theta=7/12. Cross-arm common-factor coupling **alone** never manufactures dominance; the conditional original-customer outcomes matter.

The source [executable](coupled_network_envelope_exact.js) and [record](coupled_network_envelope_results.json) enumerate exact rational arm-switch candidates and 601 mixture grid points, with 3,417 scoped JS integer assertions. A separate Fraction calculation checked all 4 exact switch candidates and 1,890 rational grid points. Enumeration is **not** the proof of Proposition 1; the piecewise-affine argument is.

## 3. What support would identify any of this?

A common exogenous factor across programs is **not** the same as access to both individual units' cross-arm potential outcomes. Expected P/E values require (a) stable exogenous factor prevalence in matched connected clusters, (b) causal program and lawful policy conditional outcome means given that **preassignment** factor, (c) original-buyer offered/no-offer and lost-opportunity denominators, (d) safe qualified menus and proper temporal operator/model/rights exposure, and (e) complete cleared economic contributions. Parallel randomized clusters with valid exposure mapping can identify population arm means without observing a robot under both programs. Conversely a posttreatment trained-checkpoint label is **not** an exogenous balancing factor merely because it predicts completion. Conditioning on it can select successful treatments and corrupt the comparison.

A signed full-network exposure ledger must link buyer original requests (including refused/unserved/no-order), deployment windows and displaced customers, earned and cleared payments/refunds, model-checkpoint broadcast/rollback, simultaneous rescue worker occupancy, qualification including held-out service criteria, data retention and training use rights, and embodied bottleneck/manufacturing constraints. Field failures/recoveries, successful trajectories, teleop, sim, synthetic and public/pretrained sources need separate provenance. At a minimum, test whether the same preprogram latent regime can explain *joint* original-buyer order, learner and recovery outcomes across sites and arms. Then test the conditional mean response table and invariance of factor distribution. No such approved customer data or randomization is presently in hand.

If an experiment cannot keep model/checkpoint broadcasts within assigned clusters or supplier/operator resources cross clusters, the interference closure is larger than the nominal pilot site; positive propensity at the **whole reachable legal history/action level** remains required. If the conditional table is only interval-supported, Proposition 1 gives a **conditional plug-in** envelope, not a confidence certificate. For an audited joint feasible family C of conditional tables and theta, the sharp sign test is inf_(c in C) inf_(theta in I) [J_P*(c,theta)-J_E*(c,theta)]>0. Rowwise independent intervals can be used conservatively but never labeled sharp; statistical confidence and causal interference coverage must be added separately.

This common-factor architecture also supplies a practical hypothesis for the wider industrial/value-chain project: common model updates, scarce human recovery capacity, shared manufacturing slots and original buyer order correlation can co-move data transfer and production cash generation across multiple sites. Their economic value is a function of jointly feasible accepted-and-paid recipes, not a task accuracy percentage or a separate priced dataset. More source data, target grounding, a new embodiment and productive versus deliberate learning are candidate actions in the same lawful decision tree.

## 4. Prior foundations, falsification and next proof gap

The factor/rectangularity distinction is already developed in Iyengar, *Robust Dynamic Programming* (2005), https://doi.org/10.1287/moor.1040.0129, and Goyal and Grand-Clément, *Robust Markov Decision Processes: Beyond Rectangularity* (published online 2022; print 2023), https://doi.org/10.1287/moor.2022.1259. Li, Kuhn and Sutter (2023), https://arxiv.org/abs/2305.19004, analyze nonrectangular robust policy optimization. Interference/exposure mapping has a separate prior tradition: Aronow and Samii (2017), https://doi.org/10.1214/16-AOAS1005. DDA (Farboodi, Koh and Xia, June 2026), https://arxiv.org/abs/2606.10127, already includes future data value, endogenous production and cross-task aggregation; no novelty claim on those mechanisms. This chapter's contribution is a **candidate coherent economic-production application and carefully delimited identification test**, not a newly proved general mathematical principle or external peer-validated original robotics result.

**Falsifiers/alternatives:** exogenous factor distribution differs across arms; U is reportable early (replace the present fixed-policy table with lawful conditional choices); qualified menus depend on additional nonbinary broadcast variables; value of the common regime changes with policy-induced scale or cluster size; same-cluster rescue is not simultaneously required; new chassis has no genuinely independent simultaneous service capacity; customer payment is conditional on unobserved original opportunity; rights prohibit transfer; independent connected clusters cannot be formed. Under any failure, widen C or model the additional state rather than reusing the 1/10 illustrative margin.

**Exact next obligation:** derive an actionable ex-ante **implementable** data-acquisition/reporting policy comparison with incomplete theta information and joint learner/recovery response uncertainty, without assuming perfect target reports or re-optimizing unknowable policies after observing theta. Tie the sensitivity/identification protocol to at least one genuine official quantitative interindustry production edge if accessible, preserving the existing BLS sector-output context without claiming it is an input-output coefficient. Continue Models A/B and full robotics/manufacturing/ownership/production-network atlas. November 22 scientific gate remains **OPEN**, theory remains the majority through December 6, and final target stays **December 25, 2026, 23:59 America/New_York**.
