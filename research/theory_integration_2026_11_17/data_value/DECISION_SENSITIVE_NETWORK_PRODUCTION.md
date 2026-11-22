# Decision-sensitive transition errors in recursive robot production

**22 November 2026 — continuation of *When Capabilities Become Production*, November 22 Models A/B gate OPEN.** This is a conditional theorem about the already defined source-data/target-grounding/embodiment investment comparison, not a new queue or a standalone financial model. It follows [lagged demand, learning, recovery](LAGGED_DEMAND_LEARNING_AND_OPERATOR_OCCUPANCY.md) and [lawful adaptive occupancy](POLICY_OCCUPANCY_DECISION_SUFFICIENCY.md). All numerical quantities below are **synthetic normalized accepted-and-cleared service contributions**, not measured robotic returns.

## The question

The previous chapter showed that the same marginal C qualification and shared-operator outage probabilities can support opposite productive-service decisions because the *joint* Q_C and H law differs. Can we identify or bound the **whole economic consequence** of an imperfect joint learner/customer/operator transition model **without** requiring its every physical state probability to be accurate, or trusting logged-policy occupancy as if it covered an optimized counterfactual?

The relevant object is the *conditional effect of a possible transition on downstream optimized paid production*, not its raw probability error alone. That effect depends on real original-buyer orders, the signed lawful action menu, recovery and safely qualified controllers, demand feedback, costs, and the independent capacity (if any) created by embodiment E.

## 1. Common finite-horizon environment

For each program a in {retained R, productive field P, deliberate target D, source+grounding SG, new embodiment E}, define a finite legal history space H_t containing predecision original buyer order/offers **including unserved and no-order cells**, safely qualified recipe menu, model checkpoint/lineage, human and robot occupation, site network, data provenance/retention rights, production-generated or deliberate learning, and customer information exposure. The lawful operator can condition an action only on available, timely, authorized information; H_t may contain latent variables for analysis, but an implementable policy must be measurable with respect to its legal observable filtration. Its menu A_t^a(h) includes the retained old controller only when it remains physically and legally executable.

Under a *true* arm-specific joint transition K_t^a(h'|h,u) and complete period net accepted/cleared buyer reward r_t^a(h,u), including actual labor, teleoperation, recovery, data, compute, curation, safety and manufacturing costs, set

    J_a(pi) = E_{K^a,pi}[sum_{t=0}^{T-1} beta^t r_t^a(H_t,U_t)] - I_a;
    J_a* = sup_{pi lawful} J_a(pi).

The initial cost I_a can equivalently be placed in r_0; use one convention, never both. We now work with the r_0 convention in the algebra. Future learned-service receipts are already in J, not an additional "data value" prize.

For each program separately, consider an *auditable reference* complete paid-production model (rhat_a,Khat_a) with **the same legal action menus on every relevant full history**, and defined also at every history reachable under K_a. Let Vhat^a_T=0 and

    Vhat^a_t(h)=max_{u in A_t^a(h)} [rhat^a_t(h,u)+beta E_{Khat^a} Vhat^a_{t+1}(H')].

This is not an oracle with access to unknown actual original-buyer reports. Both true and reference models use the same signed predecision information structure. If an embodiment changes the menu, compare *arm-specific* Vhat^E with Vhat^P; do not impose a false common P/E action set. If reference legal support is incomplete, the theorem below cannot certify that missing menu.

Define the reference **opportunity gap** and the *signed value-weighted model residual*:

    g_t^a(h,u) = Vhat^a_t(h) - [rhat^a_t(h,u)+beta Khat_t^a Vhat^a_{t+1}(h,u)] >= 0,
    d_t^a(h,u) = r_t^a(h,u)-rhat_t^a(h,u)
                  +beta (K_t^a-Khat_t^a) Vhat^a_{t+1}(h,u).

Here KV means the conditional integral of V over the full next-history distribution. The joint K includes the *endogenous* learner qualification, next original buyer demand, shared model broadcast, orders from other sites, rescue occupation and rights transitions. Data-source modalities remain separately encoded in K and costs: field successful/failed episodes, recovery, teleop, simulation, synthetic and public/pretrained inputs are not interchangeable observations.

## Proposition — exact policy-specific transition-value identity

For **every implementable adaptive policy** pi, from the same initial history h_0,

    J_a(pi) = Vhat^a_0(h_0)
              + E_{K^a,pi}[sum_{t=0}^{T-1} beta^t (d_t^a(H_t,U_t)-g_t^a(H_t,U_t))].        (1)

Consequently,

    J_a* = Vhat^a_0(h_0)
           + sup_{pi lawful} E_{K^a,pi}[sum_t beta^t(d_t^a-g_t^a)].                       (2)

If **all** reachable lawful action rows have d=0, the reference optimizer (an implementable policy choosing g=0) is also truly optimal and J_a*=Vhat_0, even if the full joint physical transition kernels have a large total-variation distance. Thus model equality at every physical coordinate is sufficient but need not be economically necessary. This is *value-equivalence on a particular continuation function*, not a claim that learner states can always be discarded: if those states affect subsequent qualified menus or rights, Vhat generally changes across them.

**Proof.** Rearrange the definitions:

    r_t(h,u) = Vhat_t(h) - g_t(h,u) - beta K_t Vhat_{t+1}(h,u) + d_t(h,u).

Taking expectation conditional on the actual full history and lawful action, then summing beta^t, cancels all Vhat terms telescopically. Vhat_T=0 leaves Vhat_0, proving (1) without independent qualifications, site independence or Markov aggregation. Taking the supremum over the same implementable policy class proves (2). When d=0 rowwise, all policies have J<=Vhat_0 because g>=0; a reference optimal policy choosing zero-gap actions throughout its actual reachable legal history attains equality. QED.

**Important:** (1) is an equality under the *actual policy-specific* K occupancy, not an assertion that observational replay or the previously logged dispatch distribution is the occupancy of the optimizer. The theorem uses histories to avoid a false Markov assumption after adaptive learning. If real buyer demand is treatment dependent, each arm has its own K and r. If buyer/robot/operator causal interference crosses purported treatment clusters, assignment and estimation of K require network-level exposure, not robot-level randomization.

## Corollary — implementable lower and optimizer-complete upper investment certificates

Suppose audited lawful evidence gives conditional rowwise residual bounds l_t^a(h,u) <= d_t^a(h,u) <= b_t^a(h,u), valid on **all histories/actions reachable by an admissible optimizing policy**, and a nonempty jointly feasible class C_a of full connected-network laws containing the true K_a. For a single *implementable witness* pi0 in program a, define

    L_a = Vhat^a_0 + inf_{K in C_a} E_{K,pi0} sum_t beta^t(l_t^a-g_t^a).
    U_a = Vhat^a_0 + sup_{K in C_a,pi lawful} E_{K,pi} sum_t beta^t(b_t^a-g_t^a).       (3)

Then L_a <= J_a* <= U_a. In particular L_SG>U_E certifies SG>E and L_E>U_SG certifies E>SG **under those audited assumptions**. Missing signed legal actions cannot be treated as zero or included as free optimizer options. If costs are included in r, there is no separate data continuation premium.

**Proof.** Evaluate the feasible witness using (1), its lower residual bound and infimum over a class including true K. Use (2), its upper residual bound, and a supremum that includes the actual full-network K and optimizing policy. Both inequalities follow. QED.

This is a potentially tighter *decision-sensitive* alternative to bounding every transition by TV times the entire range of future paid production. It can also be looser if witness occupancy is unsupported or C includes implausible couplings. A rectangular row-by-row ambiguity envelope may be conservative and **not sharp** when one broadcast checkpoint, shared human recovery roster or customer relationship imposes cross-row restrictions; using arbitrary row combinations as though physically jointly feasible must never be called an identified effect. The signed residual may be bounded directly through next-period paid-production conditional means; raw likelihood fits do not suffice. With no justified support for alternative policies, U may remain vacuous and the sign unidentified.

## 2. Terminal original-buyer and recovery reduction — what really must be measured

Consider date 1, one worker/recovery resource, and a date-2 standing A order valued at v_A>0. Producing A now earns r_A and leaves A feasible tomorrow; producing lower-current-receipt B earns r_B and acquires legally usable field data potentially qualifying higher-paid C (v_C>=v_A). C must be actually safe, signed, offered by its **original** buyer and executable before its date-2 window. Under B, H=1 means complete date-2 human/robot outage. Let

    h_B = Pr(H=1 | do(B)), 
    p_B = Pr(Q_C=1, original C offer=1, H=0 | do(B)).

Assuming B changes neither the standing A original order nor its date-2 price, and A now induces neither C nor outage,

    J_B = r_B + beta[v_A(1-h_B)+(v_C-v_A)p_B];
    J_A = r_A + beta v_A; 
    J_B-J_A=(r_B-r_A)+beta[-v_A h_B+(v_C-v_A)p_B].                   (4)

This is an **economically sufficient two-scalar transition statistic** for this exact last-decision setting: h_B and p_B, not q_C and h_B separately. It is generally neither sufficient for future learning choices nor recoverable from selected successful robot episodes. If B changes A demand, we must instead measure the joint payable intersection terms

    E[V2|B] =
        v_A Pr(O_A=1,H=0|do B)
      + v_C Pr(Q_C O_C=1,H=0|do B)
      - v_A Pr(Q_C O_C O_A=1,H=0|do B),                            (5)

assuming one slot, v_C>=v_A, and qualified C is selected ahead of A. Each event includes safe legal execution. Replacing (5) by a marginal learner score times an assumed buyer order probability is an untested independence restriction. If E adds an actually independent recovery/robot slot, equation (5) must change; a second chassis sharing H does not.

**Proof.** When not H, the optimized one-slot date-2 contribution is v_C on a qualified C original offer, otherwise v_A on an A offer, otherwise zero. With a standing A offer it is v_A+(v_C-v_A) 1{Q_C O_C}. Multiplying by (1-H) yields (4). For arbitrary A offer, expand max(v_A 1{O_A},v_C 1{Q_CO_C}) on not-H; overlap is counted once, giving (5). QED.

Equation (4) also gives an immediate *value-weighted transition sensitivity* at this terminal stage:

    d_B = (r_B-rhat_B) + beta[-v_A(h_B-hhat_B)
                              +(v_C-v_A)(p_B-phat_B)].           (6)

Thus a model can be wrong about Q_C marginal, the order in which failures occur, or other operational states yet exactly right about this specific economic continuation. Conversely tiny changes in a customer-conditioned qualified-and-not-outage event can reverse a narrow investment choice even when marginal transfer and utilization estimates are identical. This identity is conditional on fixed relative buyer values and the one-slot menu, not a universal state compression theorem.

## 3. Exact synthetic counterexample, decision boundaries and TV contrast

Set beta=1, v_A=1, v_C=2, r_A=1, r_B=3/4. Under B, stipulate O_C=Q_C, Pr(Q_C)=5/8 and Pr(H)=1/4, with Q_C/H joint mass j=Pr(Q_C=1,H=1). The feasible *coupled* law is

| Date-2 joint event | Probability |
|---|---|
| Q=1,H=1 | j |
| Q=1,H=0 | 5/8-j |
| Q=0,H=1 | 1/4-j |
| Q=0,H=0 | 1/8+j |

Its legal interval is 0<=j<=1/4. Since p_B=5/8-j, equations (4)–(6) imply

    J_B=17/8-j, J_A=2, J_P*=max(2,17/8-j).
    Reference jhat=0: Vhat_P=17/8; ghat_P(B)=0, ghat_P(A)=1/8.
    True residual: d_B=-j, d_A=0.                                  (7)

Take a separate fully specified hypothetical independent-embodiment comparator J_E*=33/16, with its actual capacity/manufacturing/rights costs already deducted. The **investment** choice P>E requires j<1/16. The within-P **dispatch** choice B>A requires j<1/8. These are different boundaries: between 1/16 and 1/8 the productive B dispatch remains optimal within P but investing in E is better. At j=1/4 the reference ranks P>E (+1/16) while the true optimized retained-old-action P<E (-1/16); the B action itself incurs 1/8 actual regret, yet P retains A and never loses more than its true feasible old-policy value 2. These are hypothetical fractions, not transferable robot thresholds.

A conventional TV bound notices that K_j and K_0 on the four Q/H cells differ by TV=2j; the terminal paid-production function ranges from 0 to 2, so its usual span×TV bound is 4j. But its **actual economic** change in the B continuation is only j by (6), a factor-four gap when j>0. Conversely let K and Khat place all their transition mass respectively on (Q=0,H=1) and (Q=1,H=1). Their TV is 1, but both yield zero date-2 production under shared outage: the value-weighted transition residual is exactly zero at this last horizon. Neither observation licenses dropping Q from an earlier multi-date learning kernel when it may unlock new future services after recovery.

For this finite example, q_C and h marginals alone identify the *sharp* structural range J_P* in [2,17/8], which straddles 33/16. A causal original-buyer **joint** Q/H observation under the B intervention narrows the interval: an audited lower bound j>=1/16 would certify E>=P (strict if >); an audited upper bound j<1/16 would certify P>E. If the interval crosses 1/16, the program investment ranking remains unidentified. No signed field sample is currently available to put a confidence interval on j, and the test is not robust to changing the standing A demand, true E capacity or unforeseen follow-on qualified services.

## 4. Why this changes empirical design and the broader theory

The minimal *terminal* observation differs from the minimum *full-network* history. For a last decision, estimating h_B and p_B, plus actual buyer paid contributions, may suffice under (4); with shifting A demand, equation (5) identifies three original-buyer joint settlement cells. With learner broadcast across sites, persistent data rights, repeat-service customer demand feedback, operator recovery queues or later newly qualified embodiments, those summaries generally cease to be sufficient: the residual at every prior date must price the full next-history Vhat. An econometrician should record the raw joint exposure ledger before choosing a reduced economically sufficient summary.

Proposed signed connected-network intervention ledger is in [the companion evidence design](DECISION_SENSITIVE_NETWORK_EVIDENCE.md). Record predispatch *original buyer* orders including declined/unserved/no order; safe independently certified Q; lawful training provenance and reuse/retention; field/teleop/simulation/synthetic/pretrained source provenance separately; checkpoint broadcast; worker/robot simultaneous recovery occupancy; accepted paid/refunded settlement; and P/D/SG/E counterfactual exposure at network-cluster scale. An intervention certificate requires its own causal assignment, lawful reports and matched feasible service; no observational episode-level proxy, training benchmark improvement or output-sector macro total gives p_B, h_B or d_t.

The wider multilayer network incorporates task → buyer service → upstream provider/manufacturing → robotic and human capacity → new task qualification and original buyer demand; the same r and K interface allows capital choices between source data, teleoperation/target grounding, human coordination, model updates, manufacturing slots and additional embodiments without a finance-only detour. Marginal source data with a free optional old policy cannot reduce optimized gross value by itself; forced retraining, scarce resources, costs or legally lost menus can reduce net value. Data rights and ownership affect lawful transitions and captured receipts, not an arbitrary separately capitalized "data premium."

**Prior-art boundary, checked 22 November 2026.** DDA (Farboodi, Koh and Xia, June 2026, https://arxiv.org/abs/2606.10127) already handles endogenous task-specific data, dynamic future data value and cross-task spillovers. Grimm, Barreto, Singh and Silver, *The Value Equivalence Principle for Model-Based Reinforcement Learning* (2020, https://arxiv.org/abs/2011.03506), explicitly treats equality of Bellman updates rather than predicting all state transitions. Standard Bellman residual / performance-difference and simulation-lemma methods supply the mathematical foundations. The original contribution *candidate* is the economic synthesis connecting original-buyer paid demand, legally usable data, conditional qualification, market response and shared operator/embodiment capacity—**not** a newly discovered Bellman identity, a proof of empirical robotics returns or a fully audited novelty claim. Technical fleet-learning experiments establish neither original-buyer paid nor legal/market/operator transition rows.

## Replication, falsification and open proof gap

[Exact integer model](decision_sensitive_network_exact.js), [record](decision_sensitive_network_results.json), independent [Fraction checker](decision_sensitive_network_fraction.py), [student exercises](DECISION_SENSITIVE_NETWORK_EXERCISES.md) and [solutions](DECISION_SENSITIVE_NETWORK_SOLUTIONS.md) distinguish formal proof from finite checking. Negative result retained: no distribution-free, nonvacuous whole-network P/D/E value certificate follows merely from measured marginal qualification, per-buyer offer rates or human utilization. Scientifically, the theorem **does not** establish that near-value-equivalent full-history models can be learned from deployed robots; that requires real buyer/learner/operator/rights coverage, calibrated conditional residual bounds, and genuine counterfactual optimizer support.

**Exact next question:** under a physically/legally grounded multi-site learner broadcast and shared human recovery graph, which *connected-network action-conditional* original-buyer/rights/qualification/occupation cells can be estimated or sharply bounded, and can their signed residual envelopes certify a P/D/SG/E investment ranking without arbitrary independent-row rectangularization? The November 22 mathematical integration advances but scientific acceptance stays OPEN. Theory majority to December 6, all original Nov29/Dec6/Dec13/Dec18/Dec23/Dec24/Dec25 milestones intact; final December 25, 2026, 23:59 America/New_York.
