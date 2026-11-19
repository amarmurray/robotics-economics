# Joint customer-order qualification, operator scarcity and the value of data versus embodiment
**19 November 2026 | Continuing _When Capabilities Become Production_.** Extends [endogenous source qualification and demand alignment](ENDOGENOUS_EXPOSURE_JOINT_SUPPORT.md) and [two-date acquisition](TWO_DATE_DATA_ACQUISITION.md), not a new model family. Conditional standard probability/decision mathematics; no robot experiment, customer dataset, physical approval or independent novelty finding.

## Common production environment
Order-local P(A∩B∩D) is not enough for shared operator deployment economics. Two original customer orders can each have well-identified complete qualifications and yet require the **same scarce recovery/dispatch slot**. Expected optimized production depends on their cross-order alignment. This is distinct from both technical per-skill transfer and within-order joint qualification.

For each *physically approved* acquisition/production policy k∈{R productive retained logging, A independent target audit, X heterogeneous source training, G physical target grounding, E changed embodiment}, retain the two-date whole-network objective
\[
J(k)=E_k[c_0(k)-C_k+\delta V(Q_{1,k},D_{1,k},O_{1,k},S_{1,k})],
\quad V=\max_{\pi\in\Pi_{\rm approved}}\sum_i g_i x_i(\pi),
\tag{J}
\]
where Q are jointly qualified complete-service recipes; D is the **original customer-order** process (not merely accepted orders); O includes available operators, recovery, dispatch and time windows; S is data/report support, rights and versioned lineage. Costs include operator displacement, training, acquisition, curation, rights, embodiment and lost current orders once. V **already contains future learning's contribution**. Old qualified policies must remain feasible where safe and noninterfering. This chapter isolates a fixed-policy slice of J, not a substitution for the full dynamic problem.

## Conditional exact allocation result
Under one fixed k, two simultaneously offered *original* orders require one shared operator slot. Let Z_i=1 when the **entire** recipe for order i is safely qualified on its own and its customer order exists. For now Z_i excludes competition for the one shared slot. Define p_i=P_k(Z_i=1), r=P_k(Z_1=Z_2=1), and contribution g_1≥g_2>0, already net of displaced alternatives. Assume one indivisible slot per attempted complete service, one decision window, no after-the-fact queue, and no demand feedback during this terminal decision. The economically distinct feasible menus are:
1. P: precommit one slot to one customer **before Z is observed**, value \(U=\max(g_1p_1,g_2p_2)\).
2. I: physically approved, nonactuating, perfectly revealing **predispatch joint** report Z, then use one slot, value \(F_1=g_1p_1+g_2(p_2-r)\). A report is not implied by owning trajectories.
3. E: safely add an **independent second slot** and attempt both without altering qualifications or original demand, value \(F_2=g_1p_1+g_2p_2\). This exclusion is a *strong hypothetical embodiment assumption*, not robot evidence.

**Proposition (information–capacity decomposition).**
\[
 I=F_1-U,\quad C=F_2-F_1=g_2r,\quad
 \boxed{I+C=F_2-U=\min(g_1p_1,g_2p_2).} \tag{1}
\]
Proof: precommit selects the higher expected contribution. With joint Z visible before dispatch, prioritize order 1 on Z_1=1; otherwise serve order 2 on Z_2=1,Z_1=0, probability p_2-r. With two safe slots serve both. Subtract and use a+b−max(a,b)=min(a,b). Optional feasible information and capacity are gross nonnegative here. Increasing simultaneous coincidence r while holding p_i fixed **substitutes physical capacity for information**; this is not a general law outside the fixed-menu assumptions.

**Sharp nonidentification from per-order evidence.**
\[
\max(0,p_1+p_2-1)\le r\le\min(p_1,p_2). \tag{2}
\]
The complete ordered atom law is (P_11,P_10,P_01,P_00)=(r,p_1-r,p_2-r,1-p_1-p_2+r); nonnegativity proves necessity, and constructing every r in the interval proves sufficiency. If A provides the safe joint report at cost c_A and E only the second slot at cost c_E, under the *same* qualification and demand law their net contrast is
\[
 J_A-J_E=c_E-c_A-g_2r. \tag{3}
\]
For strict robust A preference require \(c_E-c_A>g_2\min(p_1,p_2)\); for strict E preference require \(c_E-c_A<g_2\max(0,p_1+p_2-1)\). Between these regions even perfect order-local qualification data do not decide. Recording selection can widen uncertainty about p_i themselves.

## Exact two-world reversal — not a robot estimate
Both worlds have **the same two original customer orders** D_1=D_2=1 and per-order complete qualification Z_i=A_iB_i with P(Z_i=1)=1/2. The old one-slot dispatcher selects one of the two orders with a fair independent coin before its outcome; every selected-order success/failure distribution is Bernoulli(1/2) in both worlds. It does not see the unselected order qualification, even with arbitrarily many episodes.

In world **exclusive**, (Z_1,Z_2)=(1,0) or (0,1), each with probability 1/2: r=0. In world **synchronized**, (Z_1,Z_2)=(1,1) or (0,0), each with probability 1/2: r=1/2. No per-order original-order, competence, or selected-service statistic separates these worlds. With synthetic normalized g_1=g_2=8, U=4 in both, but F_1 is 8 versus 4, and F_2 is 8 in both. At audit cost c_A=1, extra-body cost c_E=2, **net A=7 versus E=6** in the exclusive world, and **net A=3 versus E=6** in the synchronized world (retain P=4 in either world). Preferred investment reverses. The partial-information net A−E interval is exactly [−3,1]. Both endpoints attain it; these are not benchmark returns or dollar claims.

Crucially, A=7 presupposes a **safe independently approved predispatch report of BOTH Z** that does not itself consume the scarce operator. If qualification requires an unsafe physical probe, A is unavailable—not worth 7. Likewise the second-slot calculation does not hold when a new body changes qualification, recovery, demand or customer acceptance.

## Endogenous history boundary
At each common predecision history h with identical approved physical menu and law, (1) holds conditionally for p_i(h),r(h),g_i(h); one may integrate under **one common** history distribution μ. Source-trained X and body E generally have **different** μ_X,μ_E and policy-specific qualified/demand/recording laws, so summing h-specific audit/body premiums under μ_R **does not identify** J_X−J_E. Under shared fleets and operators, the true V solves a multiperiod resource allocation network; this is a diagnostic subproblem, not a global closed form. Direct randomized **whole policy-closed network** means of net accepted original-order contribution can identify the economic contrast without separately learning r, provided independent approval, complete horizon accounting, and suitable assignment/coverage. Mechanism attribution requires separate joint same-window qualification and reporter evidence. Selected R logs cannot stand in for X order support.

Data acquisition through production-generated field trajectories, recovery/failure logs, teleoperation, simulation, synthetic inputs and public/pretrained data can affect p_i, r, original demand, reporter quality and operator use differently. Target grounding may unlock data reuse or require altered embodiment; neither is presumed monotone under forced training. Freely optional legal inert data weakly improves an optimized fixed-menu objective by allowing the planner to ignore it. Do not attach a second data premium to continuation.

## Prior art, limits and empirical obligation
Blackwell's decision-experiment comparisons (1951/1953) underlie optional information; Fréchet/Boole bounds are classical; Jordan & Graves, **1995**, _Principles on the Benefits of Manufacturing Process Flexibility_, Management Science 41:577–594, DOI 10.1287/mnsc.41.4.577, studies production flexibility/demand uncertainty; Farboodi, Koh & Xia, _Data-Driven Automation_ (arXiv:2606.10127, June 2026) already study heterogeneous spillovers, production-generated data and future data value. Official abstracts/metadata checked 19 Nov; their full proofs not re-audited. The *candidate synthesis* is connecting such mechanisms to qualified robot-customer orders, jointly selected production, information and embodied operator capacity—not a claim of new probability theory.

Needed: versioned original offered/rejected/unserved customer-order panel, *paired same-window* per-order full qualification and reporter status, shared operator/dispatch/market graph, safely approved R/A/X/G/E alternatives and total accepted/displaced production. No such field evidence or official numerical BEA–BLS sector crosswalk, full repo CI or external scientific novelty review. Nov22 synthesis gate OPEN; theory through Dec6; Dec25 2026 23:59 Eastern unchanged.
