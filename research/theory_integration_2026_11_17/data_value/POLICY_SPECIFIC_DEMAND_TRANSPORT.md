# Policy-specific buyer-response transfer and economic data value
**19 November 2026 | Continuing *When Capabilities Become Production*. Conditional optimization/partial identification, not empirical robotics results or an originality claim.**

## Same intellectual problem, stronger information structure

The preceding [nonseparable demand and operator-grounding chapter](NONSEPARABLE_DEMAND_OPERATOR_GROUNDING.md) compared X (heterogeneous source training which qualifies additional A capacity), G (target grounding which saves scarce recovery/operator effort on qualified A), and E (qualified new embodied/recovery capacity). Those investments were evaluated in the same original eligible-customer market with a *common* cross-class response coefficient gamma. Here ask whether observing the incumbent coefficient **transfers** to the market after X/G/E, given that training, qualification, physical service quality and buyer alternatives can all change.

Continue to value only optimized **complete accepted customer production**, captured payments, actual physical/operator constraints and incremental costs in one horizon. Failed, refused, specialist-displaced and unattempted original eligible orders matter. R is the competent physically feasible fallback. Field data, recoveries, teleoperation, simulation, synthetic and public/pretrained source inputs remain distinct and require rights, curation, compute and qualification; no source is a master data ontology. Free optional data cannot reduce optimized gross value if it preserves old policies. Paid forced training can. Continuation value is future production counted once, not an added data price.

## Model and a deliberately restrictive same-price anchor

For each p∈{R,X,G,E}, consider the previously solved two-service inverse provider-price model
P_A^p(q)=a_p-2q_A-gamma_p q_B, P_B^p(q)=b_p-2q_B-gamma_p q_A.
For an analytically transparent *restricted* countermodel, set a_p=9+gamma_p/2 and b_p=7+gamma_p/2. Thus at q=(1/2,1/2), even under different policies, prices would be (8,6). **This matched-policy intercept normalization is not established by observing R**. Different service quality, eligible buyers, bargaining, access or rights can invalidate every payoff formula below. The physical feasible sets, prequalified operator savings, resource caps and one engineering slot are exactly those derived in the previous chapter.

Net optimized values in synthetic normalized captured-contribution units are:
- J_R=7;
- J_X(g)=19/4+g/2+(3-g)^2/(4-2g);
- J_G(g)=(65-g)/8-11/10;
- J_E(g)=9-g/4-11/5,
where -1≤g≤1 and each policy evaluates its *own* g=gamma_p. These expressions already subtract their stated investment costs once. They do not turn benchmark percentages into economic returns.

Let the baseline market cross-response be r=gamma_R. A buyer-market audit may establish an interval r∈[L,U]. A separate **policy transport restriction** is |gamma_p-r|≤delta_p, p=X/G/E, with each gamma_p∈[-1,1]. We analyze a common delta for clarity. Such a bound is a hypothesis that needs independent *policy-specific* buyer/service data; it does not follow from incumbent statistical precision.

## Result 1: perfect incumbent demand data can have zero pure robust value

If the policy-specific gammas remain unrestricted in [-1,1] after every incumbent audit report, their admissible payoff sets do not shrink. Exact pure worst-case values are J_X(-1)=83/12, J_G(1)=69/10 and J_E(1)=131/20, all less than R=7. A perfect measurement of gamma_R therefore **cannot change the pure maximin action R** under this rectangular information structure. A paid audit cannot improve that criterion once its real acquisition and foregone-service cost is included.

This is *not* a claim that incumbent data has zero Bayesian information value. A justified correlation/prior connecting r to each policy's response would change the analysis. It is also a precise boundary to the earlier apparently favorable X/G ex-ante lottery: with a common invariant gamma, a 50/50 lottery guaranteed expected at least 561/80>7; if the realized X and G can independently change buyer response, a lottery with X probability t has worst expected net t(83/12)+(1-t)(69/10)<7. Same data quantity, different causal transport assumptions, opposite economic conclusion.

## Result 2: a sharp policy-transport-sensitive payoff difference

Define c(z)=min{1,max{-1,z}} and D(g)=J_X(g)-J_G(g). Direct differentiation gives J_X'(g)=1/[2(2-g)^2]>0, J_G'(g)=-1/8 and J_E'(g)=-1/4, so D'(g)>0.

With common r∈[L,U], gamma_p∈[c(r-delta),c(r+delta)], and **conditionally independently attainable** policy-specific shifts, the sharp attainable interval for
Delta_XG=J_X(gamma_X)-J_G(gamma_G)
is [D(c(L-delta)), D(c(U+delta))].

The lower endpoint jointly selects r=L, gamma_X=gamma_G=c(L-delta); the upper endpoint jointly selects r=U and both gammas c(U+delta). If policy effects are correlated, this is still an outer bound, but sharpness may fail. If quality intercepts or physical feasible sets drift, the entire calculation can be invalid.

The old common-gamma crossover g*=(21-sqrt(401))/10≈0.0975 becomes a **transport margin**, not a threshold automatically inferable from R: X robustly outranks G if L-delta>g*, and G outranks X if U+delta<g* (interior sufficient conditions). This is only a *pairwise* result. Screening R and E needs their policy-specific bounds. Pure commitment values against all compatible worlds include lower X=J_X(c(L-delta)), lower G=J_G(c(U+delta)), lower E=J_E(c(U+delta)), and retained R=7, provided R remains physically feasible.

Two exact examples, under *assumed* delta=1/4 and perfectly audited r:
- r=1/2: X≥197/28, G≤1119/160, E≤539/80, R=7. X is robustly top and exceeds R by at least 1/28 before paying for the audit.
- r=-1/2: G≥1129/160, X≤251/36, E≤559/80, R=7. G is robustly top and exceeds R by at least 9/160 before audit costs.

These narrow normalized gains are not an estimated fair price for buyer data. They are conditional realized-post-report production margins, assuming exact physical/rights/market support. A baseline r close to g* with delta=1/4 may support neither paid policy over R.

## Result 3: statistically precise data can remain economically uninformative

Suppose an incumbent audit reports r_hat with a certified absolute error epsilon. Set L=max(-1,r_hat-epsilon), U=min(1,r_hat+epsilon). A sufficient X/G ranking certificate is r_hat-epsilon-delta>g*; for G>X it is r_hat+epsilon+delta<g*. This makes the economically relevant constraint **statistical uncertainty plus policy-transport uncertainty**. More incumbent-only data can drive epsilon down but cannot drive an unidentified delta to zero.

In an identified *invariant inverse-demand* thought experiment, T_A(q)=P_A(q)+2q_A=a-gamma q_B. Two comparable original-buyer price/mix contexts with h=q_B2-q_B1≠0 identify gamma=-(T_A2-T_A1)/h; two bounded measurement errors |error(T_Ai)|≤eta imply |error(gamma)|≤2eta/|h|. This is an algebraic observation identity, not proof that an operational robot team can freely manipulate quantities or prices. Price/quantity endogeneity, refused quotes, changing eligibility, specialist substitution, shared learner/operator interference and price-intercept drift invalidate the shortcut unless the actual customer market design deals with them.

An audit A, if allowed, must enter the same two-date J objective with its report distribution, lost production, rights, compute, curation and physical qualification costs. The examples' 1/28 and 9/160 are merely ceilings for *realized conditional* audit expenditure that would not erase the corresponding robust production advantage; they are not ex-ante EVSI. Without an identified report distribution, no unconditional data purchase value is determined. A worst-case baseline r near the crossover can deliver no pure robust improvement when delta=1/4, so the guaranteed ex-ante gross improvement may be zero.

## Interpretation, prior art and next obligation

The important data transfer is not just trajectories→technical benchmark performance; it is a **policy-specific, customer-conditioned map** from field/teleop/recovery/simulation/synthetic/public input through qualified source learning to original buyer demand, shared operator recovery, complete accepted service and actually collected contribution. Under policy-induced demand changes, data collected solely on R can become economically redundant even while precisely estimating R; a smaller approved post-intervention buyer audit may be more decisive, conditional on its cost and ability to preserve productive service. No single source modality is intrinsically superior.

This is a specialization of established partial-identification and robust-policy logic, not proven scientific novelty. Kallus and Zhou, *Confounding-Robust Policy Improvement* (NeurIPS 2018), https://arxiv.org/abs/1805.08593 , and *Confounding-Robust Policy Evaluation in Infinite-Horizon RL* (NeurIPS 2020), https://arxiv.org/abs/2002.04518 , address sensitivity to unidentified policy value; earlier multi-product demand work and DDA §5/Appendix B remain prior foundations. None supplies measured robotic economic transfer here.

**Next proof gap:** independently credible policy-specific quality/intercept drift and original eligible-buyer quote/refusal support, alongside physical operator and qualification closure. Derive a valid captured-receipts envelope without assuming invariant price anchors; or preserve an inconclusive ranking and the retained qualified policy where feasible. No observed customer market, robot experiment, policy transport validation, numerical official BLS–BEA crosswalk, complete CI or independent originality review is available. November 22 synthesis gate remains OPEN; final target Dec 25 2026, 23:59 America/New_York.

Related [proof ledger](POLICY_SPECIFIC_DEMAND_TRANSPORT_PROOFS.md), [prospective empirical protocol](POLICY_SPECIFIC_DEMAND_TRANSPORT_EMPIRICAL.md), [Nov22 A/B synthesis](NOV22_POLICY_SPECIFIC_DEMAND_MODELS_AB.md), [exact BigInt CPU source/results](policy_specific_demand_audit.js), separate [student exercises](POLICY_SPECIFIC_DEMAND_TRANSPORT_EXERCISES.md)/[instructor solutions](POLICY_SPECIFIC_DEMAND_TRANSPORT_SOLUTIONS.md).
