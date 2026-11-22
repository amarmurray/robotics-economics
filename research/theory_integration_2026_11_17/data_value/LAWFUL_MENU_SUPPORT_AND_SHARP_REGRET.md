# Lawful production-menu support and sharp partial identification of buyer-information value

**November 22, 2026.** Continuation of *When Capabilities Become Production* / Models A–B; scientific acceptance remains OPEN. This is a conditional mathematical and prospective evidence result, **not** customer economics, an authorized robot trial, or independently established novelty.

## Same economic question, now with missing legal Q outcomes

The preceding menu–information argument proves the economic interaction between an enlarged source-trained qualified menu and a buyer-demand report can be positive or negative, and that a state summary sufficient for the old controller R may cease to be sufficient after source learning. But it assumed that every lawful action's complete accepted-and-paid continuation value was known. Which original-buyer histories actually support that assumption, and what can be inferred if new source-qualified recipes lack a complete paid-service response?

We retain one integrated objective, \(J_a=\sup_{\pi\in\Pi_a}\mathbb E_a[\sum_{t=0}^{H-1}r_t]\), \(a\in\{R,S,G,SG,E\}\). Rewards are finally accepted and settled original-buyer production less resource, training, teleoperation, curation, manufacturing/embodiment, coordination and rights costs, each counted once. \(Q(z,u)\) includes all lawful adaptive future production, learner updates, rights, refunds and future customer services: **no second data premium**. Field trajectories, failures/recoveries, teleoperation, simulation/synthetic and public/pretrained inputs are separate source channels. Free optional source availability preserves old lawful policies and cannot lower optimized gross value; compelled training or nonzero acquisition can lower net return.

**Two orthogonal kinds of support.** First certify a controller/action's *physical and contractual legality* at a full history: certified feasible, approval/right unknown (exclude until resolved), or forbidden (exclude). Only *within* certified feasible actions classify the economic Q response as (i) original-buyer accepted-and-paid/whole-continuation supported or (ii) paid-unsupported but subject, if available, to a defensible lawful full-horizon opportunity bound. A benchmark qualified skill is not a customer-paid recipe. Unapproved actions are not missing-data rows to interpolate or try for positivity. Rights to train, retain, transfer source data, deploy a learned checkpoint and reuse data at a second buyer are distinct.

## Conditional partial-identification proposition

Consider a fixed decision cell hiding original-buyer histories \(z\in Z\), positive \(p_z\), certified lawful menus \(A_z\), and common blind permissible menu \(C=\bigcap_z A_z\). If \(C\) is empty, a blind controller cannot legally take one common action; the state cell must be split. With \(C\ne\varnothing\), suppose each certified action's *full-horizon paid-continuation* value is known only to satisfy \(\ell_{zu}\le Q(z,u)\le r_{zu}\). The intervals must follow from genuinely admissible observations or independently validated resource/demand/rights envelopes. If a shared learner or operator correlates rows, the rectangular collection is at best a conservative outer relaxation.

Define \(F(Q)=\sum_z p_z\max_{u\in A_z}Q(z,u)\) (order observed before commitment), \(B(Q)=\max_{u\in C}\sum_z p_zQ(z,u)\) (one blind commitment with normal future observability), and information loss \(L(Q)=F(Q)-B(Q)\ge0\). Component monotonicity gives the **valid, not generally sharp** certificate

\[
\max\{0,F(\ell)-B(r)\}\le L(Q)\le F(r)-B(\ell). \tag{1}
\]

*Proof.* \(F(\ell)\le F(Q)\le F(r)\), \(B(\ell)\le B(Q)\le B(r)\). Subtraction plus \(C\subseteq A_z\) completes the claim. The two occurrences of each Q entry make independent endpoint subtraction generally loose.

A stronger **robust common-action witness** is possible without directly observing the untried competitors: if one certified \(u^*\in C\) satisfies \(\ell_{z,u^*}\ge\max_{u\in A_z}r_{zu}\) for every state, then \(u^*\) is statewise optimal under every compatible completion and \(L=0\) exactly. This is sufficient, not necessary; across different possible worlds one state can be indifferent and a different common maximizer may work in each. A supposed old-controller witness is not automatically valid once SG learns a new action or E adds an embodiment.

## Exact sharp theorem: two buyer types, two certified recipes

Let \(z\in\{1,2\}\) with probability \(p,1-p\), \(0<p<1\), and common certified actions \(a,b\), where \(a\) is the retained old recipe. Let \(d_i=Q(i,b)-Q(i,a)\in[\underline d_i,\overline d_i]\), with a *genuinely rectangular* identified set for \((d_1,d_2)\). Then

\[
L(d_1,d_2)=p(d_1)_++(1-p)(d_2)_+-[pd_1+(1-p)d_2]_+
=\tfrac12\{p|d_1|+(1-p)|d_2|-|pd_1+(1-p)d_2|\}. \tag{2}
\]

Therefore the **sharp maximum** over the rectangle is

\[
\overline L=\max\left\{
\min[p(\overline d_1)_+,(1-p)(-\underline d_2)_+],
\min[p(-\underline d_1)_+,(1-p)(\overline d_2)_+]
\right\}. \tag{3}
\]

The **sharp minimum** is 0 if \(\overline d_1,\overline d_2\ge0\) (both differences can be nonnegative) or \(\underline d_1,\underline d_2\le0\) (both can be nonpositive). Otherwise, the entire rectangle has strictly opposing signs: if \(\underline d_1>0>\overline d_2\), it is \(\min\{p\underline d_1,(1-p)(-\overline d_2)\}\); if \(\underline d_2>0>\overline d_1\), it is \(\min\{p(-\overline d_1),(1-p)\underline d_2\}\). All extrema are attained under the Cartesian assumption.

*Proof.* Write \(\max(Q_a,Q_b)=Q_a+(Q_b-Q_a)_+\) and cancel old-a terms to get (2). Same-sign differences yield zero regret. When \(d_1\ge0\ge d_2\), \(L=\min\{pd_1,(1-p)(-d_2)\}\), increasing as the differences separate. The maximum is at the upper-first/lower-second corner and the minimum at the closest-to-zero corner; repeat for the opposite quadrant. If either same-sign quadrant is feasible, zero is attained. This establishes (3) and the lower cases exhaustively. The theorem is elementary convex arithmetic; an exact grid checker is not a substitute for this proof.

**Interpretation:** a newly qualified robot task increases the value of knowing the original buyer order only insofar as the paid optimal recipe actually differs by buyer. Technical transfer can be strong while the ex-post incremental opportunity is negligible, or modest but economically decisive if it switches scarce robot/operator allocation. Restricting to a shared state-legal menu is essential; a forbidden learned recipe cannot be treated as a legitimate unknown payoff of zero.

## Same buyer, source, target report and embodiment counterworld

A deliberately synthetic single-slot market has equiprobable eligible original-buyer orders A/B. Retained old action \(a=(1,0)\) is qualified for A, a **hypothetically lawful** source-trained B recipe \(b=(0,q)\), \(q\in[0,1]\), and an E embodiment's hypothetical generalist \(c=(3/4,3/4)\). These vectors are **normalized finally paid net *operating* contributions**, not task benchmark rates and not monetary estimates. A target report reveals the order before dispatch. Source acquisition costs 1/10, report costs 1/20, and embodiment costs 1/10; the report here is an information intervention, **not** the separate skill-changing component of physical target grounding.

For a versus b, \(d_A=-1,d_B=q\): the report's *incremental gross productive value* given S is \(q/2\), sharply ranging from 0 to 1/2 under the unobserved paid B cell. The net program values are \(J_R=1/2\), \(J_S=2/5\), \(J_G=9/20\), \(J_{SG}=7/20+q/2\), and \(J_E=13/20\); thus \(J_{SG}-J_E=q/2-3/10\in[-3/10,1/5]\), changing sign only at the **hypothetical** \(q=3/5\). These invented costs and buyer payoffs are pedagogical, not real robot economics or an empirically calibrated cut-off. SG retains a as an action after upfront program costs. Its old-policy fallback does not imply that buying unnecessary training/report channels has zero cost.

The missing observation of *original buyer B* accepted-and-cleared paid source-trained production, plus all allowed future model/customer/rights continuations, is economically more discriminating here than another task benchmark. But even B evidence does not alone identify a genuinely pooled fleet: the original buyer market and its demand response, interference through learner/robot/operator networks, signed rights and future learned embodiment/services must be jointly covered. If no actual E trial is signed, the E line is **not** an observed lawful real-world comparator.

## Prospective support graph, constructive synthesis and negative results

The candidate full history graph distinguishes original eligible customer/order/no-order and timestamp; accessible buyer report; robot embodiment, checkpoint provenance and end-to-end qualified recipe; available operator and rescue; data-source-specific training/retention/transfer/deletion/expiry rights; actual accepted/declined/failed service and eventual cleared receipts/refunds; subsequent lawful learner updates and newly paid eligible services. Each action edge is separately marked certified legal/physical + paid-supported, certified legal/physical + paid-unsupported, uncertain approval/rights, or forbidden. Use [prospective protocol](LAWFUL_MENU_SUPPORT_EVIDENCE.md); **no physical access or contact is implied**.

Model A can potentially validate a finite lawful recipe graph with full original-buyer paid observations. Model B needs global original-buyer/shared learner/operator exposure and full-horizon adaptive future production, so static accepted task counts cannot validate a one-period resource ceiling. The shared demand and rights graph may invalidate rectangular Q intervals; if so (1) remains a conservative outer bound, while (3)–(4) cannot be called sharp for the true constrained model. Full report costs, target learning/alignment effects, and training-induced customer demand changes also break the one-decision fixed-Q specialization; then return to the full optimized J and matched interventions.

**What we learned at the November 22 synthesis gate:** the science problem is not simply collecting more independent success-rate marginals. A lawful action-by-original-buyer support graph and genuinely bounded full-horizon economic Q are needed before a two-action information result can inform SG-versus-E allocation. The conditional argument is coherent; the scientific gate remains OPEN for lack of actual permitted paid comparative arms, original-buyer cleared receipts and rights, whole-network recursive bounds and a quantitative official BEA/BLS production edge. Theory remains the majority workstream through December 6; the December 25, 2026 23:59 Eastern deadline and other milestones are unchanged.

## Bounded prior art and reproducibility

These finite-menu expectation/maximum and interval-extremum results are standard mathematics, **not independently demonstrated novelty**. Closest conceptual foundations include Blackwell's comparison of information experiments; Manski, *Social Choice with Partial Knowledge of Treatment Response* (2005, Princeton University Press, DOI [10.2307/j.ctv14164s1](https://doi.org/10.2307/j.ctv14164s1)); Givan, Dean & Greig (2003) MDP equivalence; Dong, Van Roy & Zhou, [*Provably Efficient Reinforcement Learning with Aggregated States*](https://arxiv.org/abs/1912.06366); and Farboodi, Koh & Xia, [*Data-Driven Automation*](https://arxiv.org/abs/2606.10127) (June 2026), whose section 5 already studies future data affecting production and Appendix B already treats complementary data aggregation. The plausible **research synthesis** lies in composing source provenance and qualification, accepted-paid customer demand, scarce robots/operators, rights and endogenous learning-generated services, not rediscovering these foundations.

**Reproduction**: exact Python Fraction checker [source](lawful_menu_regret_exact.py) and [record](lawful_menu_regret_results.json), with 675 interval/weight cases and 2,083 checked equalities, plus [separate exercises](LAWFUL_MENU_SUPPORT_EXERCISES.md) and [instructor solutions](LAWFUL_MENU_SUPPORT_SOLUTIONS.md). All numerical cases are synthetic. No complete repository CI or independent scientific review is asserted.
