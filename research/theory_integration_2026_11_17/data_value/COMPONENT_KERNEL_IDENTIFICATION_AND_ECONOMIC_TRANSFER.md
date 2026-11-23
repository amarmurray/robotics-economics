# Component-level transfer, original-buyer response and recovery queues: two distinct certificates

**22 November 2026 (Eastern), continuing *When Capabilities Become Production*, Models A/B. November 22 scientific acceptance remains OPEN.** This builds directly on [cross-action occupancy sensitivity](CROSS_ACTION_OCCUPANCY_SENSITIVITY_AND_REGRET.md), not a fresh disconnected model or an empirical estimate. The precise question is whether its unobserved cross-program paid-service discordance cap can be decomposed into learner qualification, buyer response and shared-worker recovery mechanisms **without manufacturing support for never-assigned target grounding**.

## 1. The production object and rights-constrained comparison

For an eligible original customer and fixed task-bundle acceptance recipe in cluster h, program a in {P,G} produces a qualification indicator Q, a genuine buyer order indicator D, and a vector of newly generated recovery jobs J. In a fixed one-worker setting the queue is

    L_{t+1}^a = max(0, L_t^a + J_t^a - S_t^a)

with work-conserving service S limited by actual shared staff/shift capacity. The accepted *paid* target event is Y_t^a = Q_t^a D_t^a 1{L_t^a=0} times a separately verified acceptance, payment and legal-use gate (or include those indicators as additional stages). No model accuracy is automatically a customer order. The same robot and worker cannot serve two customers simultaneously. Target grounding G may change Q, original-buyer D and J; source P generates current paid experience and later target effects; independent embodiment E has separate manufactured equipment, deployment lead time, staff, energy and maintenance. Old safe policy R remains selectable.

The complete economic objective is V_a = sup over lawful nonanticipative policies pi E_a[sum_t r_t(state_t,pi_t)] - C_a. Here r_t is accepted, captured and physically feasible customer service, and C_a includes training, data curation, rights and embodied resources. Learning's future effect is counted in later r_t, **not** again as a data premium. Distinct field, failure/recovery, teleoperation, simulation, synthetic and public/pretrained streams enter the Q transition separately. Free optional lawful data cannot destroy value if the old policy remains available; forced fine-tuning or added costs can.

## 2. Conditional staged transitions are not three marginal success rates

At any **same preaction state x** (including learner checkpoint, prior customer orders, live queue, available worker service, original buyer segment and rights), let a's full one-date transition factor as

    K_a(q,d,j | x) = K_a^Q(q | x) K_a^D(d | x,q) K_a^J(j | x,q,d).

D represents the **original buyer's program-dependent order**, not the model's prediction or a selected accepted-order log. J covers *all* recovery jobs entering the shared queue. A physical deterministic map from (x,q,d,j,actual shared S) then updates the queue. This factorization is always algebraically available for a finite joint kernel; it does **not** assert independence, causal mediation identification, or an implementable intervention that toggles Q while holding the buyer fixed. Additional accepted-service/payment gates can be factored after J. Multiple physical job types belong in vector J, not in independent free-worker draws.

Define conditional total-variation deviations for the two **arm-specific distributions**:

    alpha(x) = TV(K_P^Q(.|x),K_G^Q(.|x)),
    beta(x)  = sup_q TV(K_P^D(.|x,q),K_G^D(.|x,q)),
    gamma(x) = sup_{q,d} TV(K_P^J(.|x,q,d),K_G^J(.|x,q,d)).

The bounds on beta and gamma must cover common conditionals including histories that are rare under one program; equality of separate unconditional Q/D/J marginals is not enough. If conditional rows with zero support are unspecified, a uniform sup bound is unverified and typically 1. Conditional positivity is a property to document, not impute.

**Proposition 1 (distributional transition certificate).** If the three component bounds hold for all relevant common states, then

    TV(K_P(.|x),K_G(.|x)) <= delta(x)
    := 1 - (1-alpha(x))(1-beta(x))(1-gamma(x)).

*Proof.* Couple Q draws maximally, with matching probability at least 1-alpha. Conditional on matched Q=q couple D with match probability at least 1-beta; conditional on both matching couple J with match probability at least 1-gamma. Thus the complete (Q,D,J) draws match with probability at least the product. Applying the deterministic physically conserved queue update cannot increase total variation. The coupling inequality proves the claim. This is established finite coupling algebra; conditional joint dependencies are retained.

The product bound can be **attained** in the unrestricted class: let P always have Q=D=1,J=0, and let G fail qualification with probability alpha, independently lose the original buyer with probability beta, and independently create one queued incident with probability gamma. With one initially free but unserviced recovery worker, its qualified ordered worker-free event has probability (1-alpha)(1-beta)(1-gamma). The absolute expected paid-event loss equals delta. This proves class sharpness, not sharpness after imposing additional true cross-arm mechanism, buyer-marginal or queue-law restrictions.

## 3. Longitudinal economic certificate

Fix *two physically and legally supported nonanticipative policies* pi_P and pi_G with a common state representation. Suppose the full policy-specific post-action transition rows differ by at most delta_t for every state they can both reach, and initial state laws agree. There is a **constructed coupling of arm-specific state distributions** agreeing through date t with probability at least

    1 - e_t,   e_t := 1 - product_{s=1}^t (1-delta_s).

If a common state-based accepted paid-service reward r_t ranges in [0,M_t], its program expectation contrast is bounded by M_t e_t. More generally, with arm-specific r_t^a in [0,M_t] and k_t = sup_x |r_t^G(x)-r_t^P(x)|, then

    |(V_G(pi_G)-V_P(pi_P)) + (C_G-C_P)|
       <= sum_t (M_t e_t + k_t).

*Proof.* While the constructed paths agree, couple their transition rows maximally; once they disagree, retain each correct marginal arbitrarily. The probability of disagreement by date t is at most e_t by induction. The difference in expectations of a common bounded reward is at most its range times the state-law TV bound. For arm-specific rewards insert and subtract E_G r_t^P and use the triangle inequality. Sum dates once and keep the real fixed program costs outside. This is an **outer bound** on a fixed-policy economic contrast, and can be loose when payment, demand, queue and customer-bundle constraints give a smaller feasible joint set.

If policy sets are identical and this comparison holds uniformly for corresponding policies, the inequality |sup f - sup g|<=sup|f-g| transfers the bound to their optimized values. **Do not** silently apply it when G adds new actions, P creates new endogenous information, rights differ, or E brings a separate robot/worker. In those cases enumerate their lawful complete policies under a common history law and optimize jointly, as in the preceding chapters.

The common worker queue satisfies the exact pathwise inequality (for the *same* service-capacity sequence S):

    |L_{t+1}^G-L_{t+1}^P|
      <= |L_t^G-L_t^P| + |J_t^G-J_t^P|.

It follows by the 1-Lipschitz property of the positive part, and inductively bounds backlog divergence by cumulative **jointly coupled** recovery-job discrepancies. The worker-free gate is discontinuous in real-valued duration, so to translate the bound into paid service requires integer job units/minimal nonzero delay or an additional distributional bound near zero; it is not valid to assert a buyer served from a fractional recovery gap. The separate event budget in the previous chapter (Pr(Y_P != Y_G)<=epsilon) is **not** implied by the distributional TV envelope here.

## 4. Crucial non-identification: total variation is not individual causal discordance

**Proposition 2 (counterexample).** Start both programs with a free worker. Let Z be a fair binary exogenous factor, and under P take Q_P=D_P=Z, J_P=1-Z, so the free-worker paid event Y_P=Z. In world I, G uses (Q_G,D_G,J_G)=(Z,Z,1-Z). In world II, G uses (1-Z,1-Z,Z). All worker queues obey L'=J with no recovery service before the target deadline. Each world has **exactly the same complete P law and exactly the same complete G within-program joint distribution**, so TV(K_P,K_G)=0 and expected accepted target production is 1/2 under either program in either world. But the paired individual-event discordance Pr(Y_P!=Y_G) is 0 in world I and **1** in world II.

The two worlds differ in the *cross-world coupling*, which cannot be learned even from both arm-specific marginal distributions without matched structural restrictions. The coupling proof for Proposition 1 constructs a convenient mathematical coupling to compare **distributions**; it does **not** establish the actual unit-level counterfactual pairing. In particular, TV is a **lower** bound on mismatch probability in any particular coupling and is attained only by a maximal coupling. Therefore importing delta as the prior chapter's epsilon would be invalid. Conversely, expected economic value may be identical even when unit discordance is maximal. This distinction is the main corrective contribution of the current tranche.

An alternative certificate requires real **paired causal response assumptions**: if a credible common-shock structural model bounds Pr(Q_P!=Q_G | same history)<=a, Pr(D_P!=D_G | Q matches,same history)<=b, and Pr(J_P!=J_G | Q,D match,same history)<=c, then a sequential coupling **of the actual potential histories** bounds their first departure by 1-(1-a)(1-b)(1-c), with signed outcome effects still requiring service/price information. Those assumptions are strictly stronger than arm-marginal TV. At G historical action-support zero they remain unverified; claim neither measured delta nor epsilon.

## 5. Exact sanity checks and economically discriminating tests

The reproducible [integer source](component_kernel_exact.js) and [record](component_kernel_results.json) enumerate 60 equiprobable conditional gates: qualification mismatch 1/4, original buyer response mismatch 1/3, job mismatch 1/5. G achieves 24/60 accepted paid opportunities versus P 60/60, so the loss is **3/5**, exactly 1-(3/4)(2/3)(4/5). An additional one-in-ten job opportunity at the next date yields 216/600 success and a **16/25** terminal difference, saturating the two-date 1-(1-3/5)(1-1/10) envelope. This is a deliberately extreme synthetic tightness witness, not a calibrated robotics value. Two other finite worlds verify the zero-TV/unit-discordance-one distinction and 1,600 queue-Lipschitz configurations. The committed source can be replayed with Node; tests do not prove empirical assumptions or originality.

**Decision relevance.** Given a measured P paid-production contribution and a legitimately costed independent E, any certified interval for G may support P, E or G. If the G bounds overlap an investment threshold, the result is *partial* identification; a speculative tight beta for original-buyer demand cannot be treated as earned precision. A binding physical queue restriction or audited original-buyer no-offer panel can narrow the full joint feasible set even when the generic product bound remains broad. If **any unobserved G component** (especially demand) retains beta=1, the generic delta=1, making this certificate vacuous regardless of excellent technical transfer. This is a precise reason to prioritize buyers and recovery conditions alongside learner benchmarks.

The researcher's objective is not to make all three components uniformly small. It is to locate **customer-weighted decision-sensitive states** where small lawful changes in source data, target grounding or embodiment shift the maximizing qualified-service recipe and the shadow prices of worker, robot and coordination resources. The original LP resource-price and joint-qualification results remain valid within their assumptions; real downstream value-chain multiplication requires quantitative observed input-output links, not a fictional robotics multiplier.

## 6. Empirical/legal identification protocol, alternatives, prior art

See [component evidence ledger](COMPONENT_KERNEL_EVIDENCE.md) for what could justify each conditional row, including missing-original-buyer orders and multi-job physical accounting. This is a prospective design only: no private customer or employer data, trial, outreach, purchase, training or public submission. Without lawful G assignment, the measured P kernel may be estimated where customer/worker reporting supports it, but **G's action-specific Q,D,J rows remain unidentified**. Mechanically proving a shared worker cannot clear inherited jobs restricts feasible queues; it does not identify G buyer orders or Q. An invalid or legally prohibited G leaves the option set.

Alternative assumptions to test include learner action effects confined to one certified task bundle, contractually locked buyer order processes, queue-dominance rather than equality, source-dependent operator incident severity, worker-sharing across multiple facilities, and customer demand feeding back into data generation. The current finite sup-norm certificate is deliberately conservative, and reachable-state restrictions or a single common-law LP may be tighter. Existing Q/D/J correlation cannot be replaced by independent marginal task benchmarks.

**Prior foundations, not new generic theorems:** Farboodi, Koh and Xia, [Data-Driven Automation](https://www.nber.org/papers/w35320) (NBER WP 35320, June 2026) already studies heterogeneous endogenous data and task spillovers; the paper's future-data valuation and complementary aggregation are prior, not this project's discoveries. Standard coupling inequality and maximal-coupling theory are covered in [*Modern Discrete Probability*, Chapter 4: Coupling](https://doi.org/10.1017/9781009305129.005) (2024). Dynamic finite-state policy/value comparison and missing-action-support identification are established foundations. The **candidate synthesis** is their joint use to compare source learning, licensed target grounding and truly additional embodiment inside qualified paid-service/queue/resource networks; its novelty, external validity and causal conditions are not independently established.

**Next proof gap (persist rather than opening a new arbitrary question):** replace uniform sup component bounds by *reachable-history, price-weighted, rights-feasible* conditional bounds under an explicit action-dependent customer/order/worker transition model. Determine when the physically observed P queue plus lawful engineering constraints restricts G's job kernel despite G action-support zero, and show a counterexample if it cannot. Then derive an implementable robust P/G/E investment or lawful audit choice from the resulting **single common law**, including policy-dependent selection. November 29 stronger theory/empirical backbone, December 6 theory contribution choice and final **December 25, 2026, 23:59 America/New_York** target remain. The November 22 science gate remains OPEN.
