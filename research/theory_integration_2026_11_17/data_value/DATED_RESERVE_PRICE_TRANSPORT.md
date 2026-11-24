# Dated reserve prices, endogenous reports, and the economic value of shortening a recovery

24 November 2026. Continuation of [shared reserve capacity](SHARED_RESERVE_POOL.md), [dated dispatch](TIME_EXPANDED_DISPATCH_CONSERVATION.md), and [variable-duration renewal](VARIABLE_DURATION_RENEWAL_AND_CUSTOMER_RESPONSE.md). The new issue is not another duration example: when may a portfolio-level price certificate transport across learned controllers and across different dispatch policies? A price on an expected worker-hour is not generally a price on the actual dated worker available to a particular original customer.

## 1. One source-to-production problem

A program g selects retained R, extra source data X, target grounding G, embodiment E, or lawful combinations with actual worker reserve K. Its state contains provenance-tagged data stocks, licensed uses, trained controller menu and complete qualification evidence, uniquely identified customer orders/authorizations and procurement constraints, and dated worker jobs (remaining time, deadlines, skills, travel and commitment). The report h_t is the lawful predecision history; use belief or history if a compressed state is insufficient. The joint safe action set A_g(h_t) includes fallback/abort where actually approved, not an oracle safe switch. Data from field trajectories, failures/recovery, teleoperation, simulation, synthetic and public/pretrained sources are distinct, not counts on one common axis.

For t=0,...,T-1 let r_t be net accepted service receipts minus real variable costs, and phi(s_T) the terminal optimized production contribution under the same accounting. Then

    J_g = sup_{pi in Pi_g} E_g^pi[sum_t beta^t r_t + beta^T phi] - c_g.

c_g includes one-time acquisition/training and committed reserve costs, with actual displacement charged once. The superscript pi matters: both the report law and later customer authorization law can be policy-generated. Each genuine job started at t occupies a worker in the applicable dated intervals until release; let u_t include both carried jobs and new starts at date t. For a feasible policy, u_t <= K_t pathwise, for each skill/location pool. The inequality is necessary, not sufficient for every physical safety constraint. If a job can be interrupted, the state includes the interruption and successor obligations. No mean constraint replaces this. Costs, receipts and terminal contribution are all dated; no added 'value of data' on top of phi.

## 2. A priced dynamic envelope with endogenous report drift

Choose any nonnegative integrable price vector lambda_t(h_t) measurable at the relevant report time, and a relaxed policy family containing every feasible policy. Every true feasible policy satisfies

    gross J(pi) <= E^pi[sum_t beta^t (r_t + lambda_t . (K_t-u_t)) + beta^T phi].  (1)

The inequality follows path by path, including occupancy from earlier commitments. Taking the supremum of the right side over the relaxed policies is a valid upper bound. Its implementation requires a well-defined law even for relaxed actions; alternatively keep the original safe menu and use a Bellman super-solution. A relaxation that allows unavailable information is an upper bound only if all original rules embed and the law is consistently extended. It cannot itself be used as a lower policy.

For a local decomposition, suppose r_t is approximated by sum_i r_it, phi by sum_i phi_i, and u_t by the exact sum of all site occupations; shared occupations must be allocated once. Let reference site potentials v_it(z_it) be arbitrary functions of lawful local summary z_it. Set v_iT=phi_i. Define local residual

    ell_it = r_it^ref(h_t,a_i) - lambda_t(h_t).u_it
             + beta E_i^ref[v_i,t+1 | z_it,a_i] - v_it(z_it).

The local occupation charge must include the true carryover or a supported lower load for an upper relaxation. Suppose for each true admissible h,a the conditional residual of the true priced reward plus change of sum v_i differs from the sum ell by at most d_t^+(h,a) above (and d_t^- below). This is a substantive transport assumption on reward and conditional successor potentials; a shared learning lineage, joint procurement or action-dependent report can invalidate it. If phi-sum phi_i <= d_T^+, the upper potential identity gives

    gross J(pi) <= E sum_i v_i0
       + E^pi[sum_t beta^t (lambda_t.K_t + sum_i ell_it + d_t^+)
              + beta^T d_T^+].                                  (2)

Proof: sum the priced conditional residuals and telescope under the true policy using iterated expectations. The terminal mismatch enters once. Nonnegative slack gives (1). Thus a deterministic uniform bound on the expression in parentheses across reachable histories/actions (or a super-solution for its conditional accumulated maximum) gives a policy-uniform upper certificate; for a specified admissible witness one instead computes its true unpriced reward or subtracts the **actual** slack and the lower residual bounds in the same telescoping identity. No independent site histories or independent next states are required for this proof. Exact local Bellman inequalities ell<=0 follow only if the local reference model and action/information menus actually dominate conditional transitions under the global policy, or the error is covered by d. Otherwise treating independent site optimization as an upper bound is unjustified.

Important special case: when lambda and K are deterministic, or their joint discounted expected product is invariant across feasible policies, it is legitimate to move that term outside the supremum. For endogenous reports or capacity, the expected price revenue must stay inside the optimization or be bounded uniformly across the original population. An incumbent price-revenue expectation is NOT in general an upper bound for a new learned program. This is distinct from the need to transport the local priced continuation residual. A conservative constant upper revenue may be weak but remains valid. A necessary occupancy relaxation is an upper certificate, a sufficient safety rule is a candidate lower witness only.

For a common identified set of complete controlled laws M, compare a lower value of G and an upper value of E on each same m; inf_m of their difference is a robust ranking certificate if positive. If the policy itself must be chosen without knowing m, the implementable lower rule is fixed before m is revealed (or uses genuinely available reports). The supremum over m-specific optimal policies is not an implementable guarantee. A training-induced change in report frequencies requires this same treatment, not an average of incumbent residuals. With time-varying prices the same discounted proof works. With a continuing horizon one additionally needs a finite tail bound.

## 3. Exact two-date counterworld: same mean load, different economic value

One actual worker is free at date 0; an optional recovery A can be started then. Its incremental accepted net receipts are 2 in R and G. The job is either short (one interval) or long (two); when long in G a legally retained recovery trajectory supports an additional distinct, qualified terminal service with net value 1, already inside phi. This terminal service uses distinct stipulated resources and budget. At date 1 a different buyer order B can produce net 6 if authorized (H=1) and the worker is free. A safe loss of B is allowed; unsafe dispatch is excluded. There is no foresight at date 0. Actual duration and B authorization are observed at date 1. Old R is always long and has no extra terminal value; B high with probability 1/2 whether A is chosen or not. Its optimum is skip A, gross 3. Grounding G costs 1/2, allows short with probability 1/2, B high with probability 1/2; first assume H is invariant to the A action. D=1 denotes long and j=P(D=1,H=1). The four atoms (short,not H; short,H; long,not H; long,H) are (j,1/2-j,1/2-j,j), j in [0,1/2]. Old and new worlds have a coherent common potential-history coupling; no assumption of paired field identification. G and R are ex ante versions, old version can be retained after the cost is sunk.

    start gross G = 2 + E D + 6 E[H(1-D)] = 11/2 - 6j,
    skip gross G = 3,
    net G increment vs R = max(2-6j,-1/2).

Retention of the old full program is included in the max. Independent E has net incremental 1, using distinct resources and customer budget by assumption. G beats E iff j<1/6, ties at equality, loses otherwise. At j=0 the increment is 2; at j=1/2 it is -1/2 after committing to G (ex ante do not acquire). An extra source X which adds the same conditional terminal opportunity but does not shorten the old long job makes A worth 3, ties skip gross and cannot justify a positive acquisition cost in this menu. An independently added second worker K costs 3/2; R+K yields gross 5 minus 3/2, G+K yields 11/2 minus 1/2 training and 3/2 reserve. Both net 7/2, independent of j. Here additional reserve removes the benefit of duration shortening; not a universal sign.

The sum of isolated first/second-date options in G is 11/2. In every world always starting A and serving all B has expected date-1 occupation E D+E H=1, so it passes the mean load constraint. Yet its occupation is 2 with probability j, hence it is not feasible for any j>0. The pathwise optimum loses 6j from always-start relative to the isolated sum; it can instead choose skip. Mean durations, local paid outcomes, marginal B frequency, and local successor learning values are identical across the worlds. A joint dated overlap, not additional local benchmark data, resolves the ranking.

Deterministic date-1 price lambda>=0, date-0 price 0, gives the local relaxed upper

    lambda + max(5/2-lambda/2,0) + (6-lambda)_+/2.

Its minimum is 11/2 (all lambda in [0,5] achieve it). Thus this entire constant-price family cannot see j. In contrast, choose a price 6 if H=1 and zero otherwise at date 1. This is a lawful report then, not foresight for A. The A decision evaluates its *expected* carryover charge 6j before starting; B's priced net is zero. The capacity price expectation is 3 under either action. The upper is 3+max(5/2-6j,0)=max(11/2-6j,3), tight because the corresponding start-or-skip policy is feasible and serves B only with a free worker. This is a constructive instance of an economic price field conditioned on actual dated customer opportunity. It does not require predicting H before A starts. It needs the joint action-conditioned occupation-price moment.

If a lawful free report at date 0 reveals D (not H), the gross value is

    4 - 6j + max(3/2,6j) = max(11/2-6j,4).

Proof: always start when short; when long compare 3 with 12j, the conditional expected B receipts. This improves the synchronized gross from 3 to 4, but does not itself prove a positive net investment compared with E. The report must actually exist before commitment; post-recovery logs do not confer this policy.

## 4. Endogenous report countermodel and correction

Let q_0=P(H^skip=1), q_1=P(H^start=1), d=P(D^start=1), j=P(D^start=1,H^start=1). H may be a later distinct authorization generated by a first service or the renewal of a recorded buyer; retain the original population and record the new ticket once. The exact same start/skip optimization is

    V=max(6q_0,2+d+6q_1-6j).

The price lambda=6H yields the same tight bound if its revenue is evaluated on each policy: capacity revenue 6q_0 or 6q_1, priced A contribution 2+d-6j under start. Reusing 6q_0 outside the maximization is invalid. E.g. q_0=0,q_1=d=1/2,j=0, the incorrect upper 5/2 is below true feasible 11/2. This is not a statistical fluctuation but an algebraic failure of an invariance assumption. Measuring overlap alone still does not resolve the problem when buyer authorization response changes. For q_0,q_1,d fixed, j has sharp Frechet range [max(0,d+q_1-1),min(d,q_1)]; each endpoint realized by a four-atom law for start coupled to any skip law. A paired common-law audit of the two action-specific authorization rates plus the dated overlap and terminal value is sufficient for this particular comparison. In a general network, the analogue is the priced occupation plus residual bound (2) over a supported whole-policy history, not a regression on average operator hours.

## 5. Consolidated theorem/assumption map for Models A and B

Model A maps a complete qualified production recipe and dated demand/resource availability into accepted net contribution. Existing LP/resource-price and exchange certificates are exact only under their convexity/additivity or integer witness conditions. Model B composes source-specific acquisition, grounding and embodiment interventions with the *joint* law of Model A's inputs and future rights/qualifications. Its dynamic objective above handles deliberate data and production-generated data in the same law. The following distinct assumptions must not be silently exchanged:

- Technical transfer: matched intervention changes joint qualifications, controller menu or occupation law; no dollars implied by a benchmark. Learning can change the graph and constraint coefficients.
- Economic translation: original paid service and resource/date constraints, including endogenous distinct authorizations, map those changes to contribution. Prices are state-specific bounds unless dual equality or an executable witness establishes exactness.
- Temporal implementability: report availability before each decision and pathwise worker conservation. Expected occupancy and future logs are insufficient. Retain old lawful programs, not physically impossible switches.
- Dynamic composition: policy-dependent report and successor laws enter expectation under that policy; rights, compute/curation, acquisition and displaced service counted once. Optional free data preserves gross optimum by menu inclusion, not by positive transfer in every recipe.
- Empirical closure: identify the joint economically decisive moments with matched whole-pool assignment, or bound the unidentified set and optimize a common implementable witness. No generic superiority of G, X or E follows.

This narrows the candidate first-paper argument to **economic sufficiency of joint, dated source-to-qualified-production effects**, with the overlap-price example as a discriminating mechanism, rather than claiming each standard dual or probability identity as a separate contribution. The November 22 gate remains OPEN. A production backbone, paid original-customer observations, actual interventions, signed data rights, independent staffing verification and independent literature/scientific review remain missing. No official numerical BEA cell is added in this tranche.

Established prior foundations: Adelman & Mersereau, *Relaxations of Weakly Coupled Stochastic Dynamic Programs*, Operations Research 56(3), 712–727 (2008), https://doi.org/10.1287/opre.1070.0445 (publisher abstract inspected 24 Nov); Brown, Smith & Sun, *Information Relaxations and Duality in Stochastic Dynamic Programs*, Operations Research 58(4), 785–801 (2010), https://doi.org/10.1287/opre.1090.0796 (Duke publication abstract inspected 24 Nov, https://scholars.duke.edu/publication/762575). The latter explicitly covers upper bounds from relaxing nonanticipation with penalties; the former treats separable subproblems coupled by constraints. Neither abstract settles novelty of this economic synthesis. The proof here is a direct weak-duality/telescoping construction, not a new general duality theorem. DDA §5 and Appendix B already treat future data value and aggregation. No full-paper literature replication or novelty certification.

Next: consolidate an empirical and mathematical **policy-closed comparison** for the first-paper candidate: one testable common-law source-to-qualified-recipe map with priced occupation and original paid buyer/rights moments, and one countermodel in which inexpensive production data make additional grounding redundant. Work on the actual evidence gap and compress the manuscript argument before adding more isolated queue examples. Retain full roadmap and final 25 December 2026 23:59 Eastern target.
