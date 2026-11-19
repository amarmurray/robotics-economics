# Economically valuable sequential data acquisition without cross-world qualifications

**19 November 2026 UTC, private theoretical continuation of When Capabilities Become Production.** All propositions are conditional applications of established causal inference and decision theory, not empirical robotics results or new general statistical mathematics.

## A meaningful gap in the prior argument

A static source × grounding four-arm experiment may identify each complete-policy arm's average customer production and their factorial interaction, but it does not identify the cross-policy joint distribution of technical qualification or the outcome of deliberately buying target grounding *after source training fails*. The preceding adaptive-menu result therefore correctly refuses to rank an unobserved sequential policy using an assumed static coupling t or transition r.

There is, however, a direct route to the **economic decision estimand**, provided a much stronger experiment is independently physically admissible. We need not identify all potentially qualified controllers on the same network to determine whether *offering an approved grounding acquisition after source failure* improves accepted service relative to retaining the qualified incumbent.

## Unit, outcome and policies

Fix a baseline opportunity population and commercial horizon. One unit must be an entire **policy-closed network**, including robots, shared learner, operator, dispatch, customer demand/order effects and possible cross-site resource interactions under *either* proposed policy. The first-stage source-data experiment, training recipe and full-target qualification test are identical across this policy comparison. Let H be the first-stage history observed **before second-stage randomization**, including original B orders, eligible A customer opportunities, deadlines, controller/source hashes, recovery, target-support coverage, financial/rights and operator availability. Let D=1 signify failure to qualify the complete target service; let E=1 signify that both alternative second-stage policies have prospectively documented physical approval, rights and operational feasibility.

On a history with D=E=1, continuation B=0 retains a qualified original F controller or competent specialist S with no extra grounding acquisition. Continuation B=1 buys a specified source-conditioned target-grounding/training/verification step, admitting the learned robot to production **only after its complete service and physical safety are separately approved**, otherwise falling back to F/S. E must be determined before assignment; don't condition on subsequent successful qualification. An embodiment-change alternative h is another policy requiring separately demonstrated manufacture/lead time, rights and physical approval, not a free substitute for B=1.

Let Y_i(b) denote captured **full remaining-horizon net contribution** of all accepted A and retained/displaced/failed/unattempted original B customer orders, accounting for time windows, customer demand reaction, dispatch/attention, actual test/curation/compute/manufacturing, recovery, collection and rights under complete policy b. This is the same optimized production value as the established qualified-production model, now evaluated at different controlled continuations. It includes continuation learning effects already, not a second priced data premium. It is not a raw technical success percentage, industrial wage, or automatically social welfare.

## Proposition (direct sequential policy identification)

Suppose (i) eligible H,D,E are realized before stage-two assignment, (ii) assignment B is randomized with positive probability for each **physically approved** competing complete policy conditional on eligible H, (iii) full-policy consistency and complete outcome measurement hold, and (iv) policy-closed network units have no **between-network** learner, human, dispatch, resource or customer-demand interference. If eligible networks are independently drawn, standard superpopulation inference applies.

Then for every supported pre-B eligible history stratum h,

    delta(h) = E[Y | B=1,H=h,D=1,E=1]
             - E[Y | B=0,H=h,D=1,E=1]
             = E[Y(1)-Y(0) | H=h,D=1,E=1].

Averaging over the *observed first-stage* distribution of eligible histories identifies delta, the mean **whole-network incremental economic effect of the adaptive continuation**. Let pi=P(D=1,E=1) among the original baseline opportunity population. Comparing complete baseline regimes identical everywhere else, their net value difference is

    Delta = pi * delta.

**Proof.** Conditional stage-two random assignment makes each arm's observed mean equal its corresponding potential complete-policy mean. Consistency connects assigned/received policy and complete Y. Integrate over eligible pre-B histories. The policies agree everywhere except D=E=1, so the law of total expectation produces pi delta. This is an ordinary sequential-randomization or dynamic-treatment-regime result (Murphy 2003), not a novel theorem.

**Why it matters:** Neither the unobserved static Q_source/Q_ground overlap t, nor source-conditioned technical success r, nor an assumed equal post-exit controller/recovery continuation is needed to identify this **reduced-form policy contrast**. These remain important if the objective is to decompose causal *technical transfer*, evaluate a different untested embodiment, or optimize a larger unobserved menu. The randomization does not reveal the counterfactual robot skills a given individual network might have obtained. Any cross-network common updater or customer pool invalidates the result unless incorporated in a larger independent cluster. Randomizing robots inside one connected market is not sufficient.

**Approved outcomes can change demand and occupancy:** neither arm must share final customer demand, B-order losses, recovery nor controller state distribution. These differences properly enter the *economic* Y(b). But if the resulting mean gain arises from better commercial allocation rather than improved robot learning, the policy effect is still identified; its *technical mechanism* is not. No field intervention is undertaken or authorized by this theorem.

## Bounded precision certificate and its limit

For independently sampled eligible network observations, with a genuinely established common outcome range Y(b)∈[L,U], R=U−L, n1 treated and n0 fallback groups, and confidence level 1−alpha, Hoeffding and a two-arm union bound give

    |d_hat-delta| <= w,
    w = R * [sqrt(log(4/alpha)/(2*n1)) +
             sqrt(log(4/alpha)/(2*n0))]

with probability at least 1−alpha. This is an independent-superpopulation bound; complete randomization of a **fixed finite population** requires its own dependence-aware argument. A positive lower endpoint d_hat−w>0 indicates the approved grounding continuation has positive mean net economic value among enrolled eligible networks at the stated confidence, not individual-site superiority or a safety certificate. If pi>0, the baseline policy effect has the same sign; estimating its magnitude also needs uncertainty for pi. An interval containing zero is inconclusive. If networks do not exist independently or the range is unverified, this bound is inapplicable.

An illustrative normalized outcome range R=4 with alpha=.05 and equal arms n requires n≥561 **per arm** for a desired half-width w≤.5. This is pure precision arithmetic, *not* power, physical trial scale, a claim of data availability or a scientific milestone gate.

## Explicit hypothetical comparison

On source-failure eligible networks, qualified fallback contributes 2 normalized whole-network units. Grounding continuation yields

    Y(0)=2,   Y(1)=1.4 + 2Q_ground_after_source.

Here qualification Q=1 adds 2 units of **complete accepted** A service; 0.4 incumbent B service/order displacement and 0.2 paid validation/training are already deducted once in 1.4. The actual after-source conditional success r gives delta=2r−0.6. At r=3/4, delta=.9 and with hypothetical eligible fraction pi=.5, the baseline policy benefit is .45. At r=1/5, delta=−.2 and the baseline policy loss is −.1. The static standalone q or potential-outcome overlap t cannot simply be inserted as r. No robotics test, commercial dollar value or safety validation is encoded in these inputs.

The [executable](sequential_policy_identification.js) enumerates all 20 balanced assignments of 6 hypothetical complete network outcome pairs to verify the expected assignment estimator and checks the cost/recovery arithmetic and sample precision; checks **do not establish the proposition**. [Proof ledger](SEQUENTIAL_POLICY_PROOF_LEDGER.md), [prospective evidence protocol](SEQUENTIAL_POLICY_EMPIRICAL.md), [exercises](SEQUENTIAL_POLICY_EXERCISES.md) and separate [solutions](SEQUENTIAL_POLICY_SOLUTIONS.md) distinguish proofs, synthetic computations, public technical sources, and missing field observations.

## Falsifiers, alternative formulations and close predecessors

Demand-specific eligibility, data rights and fixed physical approval are part of the policy definition; an unsafe grounding path simply is not a feasible arm. Eligibility determined by successful post-randomization training biases comparison. Incomplete original B-order records omit displaced value. Shared dispatcher/customer/resource networks violate treatment isolation. Unknown horizon/returns invalidate a numeric economic interval. A competent specialist may dominate even a technically superior grounded robot. A freely available optional passive log can enlarge the feasible decision set without lowering its optimum, but costly/forced training can decrease realized contributions. Such objections are tests of assumptions, not grounds to declare data useless.

The argument is close to Murphy, *Optimal Dynamic Treatment Regimes* (2003), https://doi.org/10.1111/1467-9868.00389; conventional sequential multiple assignment randomized trial logic; Hoeffding's bounded concentration; Fréchet potential-outcome bounds; and LP resource-price/process-flexibility foundations. *Data-Driven Automation* (Farboodi/Koh/Xia, 2026, https://arxiv.org/abs/2606.10127), §5 and Appendix B, already studies economically valuable production-generated learning and complementary data aggregation. Scientific novelty of the assembled robotics-production synthesis is open.

**Exact next evidence question:** do there exist independently approved versioned policy-closed controller/dispatch/operator/customer networks, and a signed original A/B full accepted-order service panel, capable of a direct source-first-failure continuation comparison? Without that, retain previous partial-identification bounds; public robot demonstration successes cannot decide customer production economics. The Nov22 scientific synthesis, Nov29 backbone, Dec6 contribution choice and final December 25, 2026, 23:59 Eastern target remain unchanged.
