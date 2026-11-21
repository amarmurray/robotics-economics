# Partially identified economic value of source/grounding reports under signed action support

**21 November 2026, Eastern.** Continuation of *When Capabilities Become Production*, November 22 Models A–B. The precise open problem following [economically sufficient reports](ECONOMICALLY_SUFFICIENT_REPORTS_AND_DATA_VALUE.md) is how to identify the **value of predecision data** when the physically licensed original-buyer/robot/operator network has only incomplete observations of what *alternative signed actions* would have earned. This note does not posit another learning curve, change the X/G/E/R table, or equate accuracy with revenue. It extracts what can already be certified from incomplete action-specific original-customer outcomes, and what cannot.

## Economic environment and the epistemic boundary

Condition on a fixed original-buyer cohort, fixed network capacity/state h, a fixed learned controller, qualification/recovery permissions, rights, and **the same original signed action menu** under a fine predecision report Y and its coarse version Z=φ(Y). An action is an *entire* feasible joint dispatch/production policy, not an uncosted independent selection for each robot. Let m_d(y)=E[U_d|Y=y,h] be its conditional completed, accepted, refunded and actually paid **captured contribution** (including the scarce operator/fleet shadow use in the production optimum, and any continuation value once). Let p_y>0 be the predecision probability of report y. An unseen alternative receipt is a potential outcome, not an observed one. Safety-ineligible actions do not become permissible because an econometric method needs positivity.

For the transparent two-policy subcase D={A,B}, define the *conditional original-service action advantage* δ_y=m_A(y)-m_B(y). This is **not** the difference between A/B benchmark accuracies or their effects on model weights. Observed eligibility, reward bounds, propensity support, physically certified capacity and refunded buyer outcomes can yield a **set** δ_y∈[ℓ_y,u_y], without point-identifying it. Assume those intervals are jointly attainable independently across report cells conditional on the same original network (a rectangular identified set). This is an assumption to examine—not an implication of the available logs. For a source-X retraining or a grounding-training intervention, the controller and m themselves change; the below fixed-learner comparison is not automatically a total treatment effect.

## Proposition 1: the exact signed-action report-value bounds

For each coarse cell z, write

\[
P_z(\delta)=\sum_{y:\phi(y)=z}p_y(\delta_y)_+,\qquad
N_z(\delta)=\sum_{y:\phi(y)=z}p_y(-\delta_y)_+,
\quad x_+=\max(x,0).
\]

The gross incremental optimized paid-production contribution from allowing the fine rather than the coarse report, with both A and B permitted, is

\[
L(\phi;\delta)=\sum_z \min\{P_z(\delta),N_z(\delta)\}.
\tag{1}
\]

Its **sharp lower identified bound**, for rectangular interval restrictions and known p, is

\[
\underline L=\sum_z\min\left\{
\sum_{y\in z}p_y(\ell_y)_+,\quad
\sum_{y\in z}p_y(-u_y)_+
\right\}.
\tag{2}
\]

For the **sharp upper bound**, classify reports in a cell into a putatively nonnegative-advantage subset S and its complement. S is feasible when u_y≥0 for y∈S and ℓ_y≤0 for y∉S. Then

\[
\overline L=\sum_z \max_{\text{feasible }S\subseteq\phi^{-1}(z)}
\min\left\{\sum_{y\in S}p_yu_y,\quad
\sum_{y\in z\setminus S}p_y(-\ell_y)\right\}.
\tag{3}
\]

For a single report cell no detail is discarded and both bounds are zero. For a nontrivial coarse cell, **fine-report value is robustly strictly positive iff at least one report is forced to favor A (ℓ_y>0) and at least another is forced to favor B (u_{y'}<0)** within that same coarse cell, with their predecision masses positive. Crucially, this certification can hold while an *entire third report's* action advantage is unidentified. It establishes a common-menu **within-program** economic information value; it does not identify the total value of acquiring source episodes, target finetuning or embodiment E.

**Proof of (1).** Subtract the contribution from always using B. With Y, an optimal signed action adds Σ_y p_y(δ_y)_+; with only z, it adds (Σ_{y∈z}p_yδ_y)_+ on each cell. Since Σ_y p_yδ_y=P_z−N_z, their difference is P_z−(P_z−N_z)_+=min(P_z,N_z). This reproduces the fixed-policy Blackwell gap, now expressed in the economically interpretable margins.

**Proof of (2).** For each z, minimizing min(P_z,N_z) over all admissible δ is the smaller of the separate minima of P_z and N_z. P_z is coordinatewise nondecreasing, attaining its minimum at ℓ, whereas N_z is coordinatewise nonincreasing, attaining its minimum at u. The intervals allow the corresponding endpoint vectors. Cells are independent under rectangularity, so lower extrema add.

**Proof of (3).** Fix an orthant's sign pattern. P_z depends only on positive coordinates and N_z only on negative coordinates. Raising a nonnegative δ_y toward its u_y cannot reduce P_z; lowering a nonpositive δ_y toward its ℓ_y cannot reduce N_z. Hence a maximizer exists at the sign-consistent endpoints for some subset S, including weak-zero cases. Exhausting all feasible S yields (3), and every displayed endpoint vector is allowed. Continuity on a connected rectangle implies all intermediate L between the sharp extremes are attainable. For nonrectangular cross-report restrictions, these formulas need not be sharp.

**Why the sign criterion matters.** A sharp positive lower bound is not the same as learning every m_d(y). It instead requires evidence that *two different supported customer states justify different complete network actions*. If all reports can have one common optimizer, a zero-value world remains consistent even when their task predictions differ dramatically. Conversely, if the signed action A is forbidden in a necessary report cell, one must shrink the policy class and recompute; a statistical lower bound cannot authorize A.

## Exact example: one unidentified report does not destroy all information value

Take three equally physically permitted predecision report categories with probabilities p=(1/2,1/4,1/4), all compressed to one coarse report. Let the normalized conditional original-customer A-vs-B contribution differences satisfy

| Fine report | p | identified margin interval δ |
|---|---:|---:|
| y1 | 1/2 | [1/4,1/2] |
| y2 | 1/4 | [−1/2,−1/4] |
| y3 | 1/4 | [−1/2,1/2] |

The y3 comparator is completely ambiguous and could be support-deficient. Nevertheless (2) gives min(1/8,1/16)=**1/16** guaranteed gross fine-report value. Formula (3) gives **1/4** possible value. Sharp witnesses are δ=(1/4,−1/4,0) for the lower bound and δ=(1/2,−1/2,−1/2) for the upper bound. These margins are feasible as bounded potential responses, e.g. taking m_B(y)=1/2 everywhere and m_A(y)=1/2+δ_y gives [0,1] paid-service outcomes, without any direct mapping from robot benchmarks to dollars.

The [exact executable](report_value_support_bounds.js) enumerates 3,375 three-report rectangular identification sets with each endpoint on the grid {−1/2,−1/4,0,1/4,1/2}, brute-evaluates 42,875 feasible action-margin vectors, and checks the analytic lower bound and feasible sign-partition upper bound 6,752 times against direct enumeration. [Stored results](report_value_support_bounds_results.json). An independently written Python enumeration of all 3,375 sets yielded the same result. These finite checks validate implementation for that grid, **not** the general proof or any real robot's paid performance.

**Do not turn the interval into a portfolio return.** If an independently signed, freely deployable E policy earns at least as much as A and B for every report in this example, the enlarged {A,B,E} action menu admits E as a common optimizer and the full fine-report value is **zero**. The E=10 policy in the *existing* stipulated X/G/E/R comparison continues to dominate the entire initial investment menu. Neither the lower bound of 1/16 nor an observation cost creates an extra return on top of that previously optimized E. These illustrations use different normalizations; they cannot be added together.

## Proposition 2: exact finite-action identified bounds reduce to linear programs

The two-policy formula is useful for experimental planning, but full production networks have multiple specialist, R fallback, operator allocations and embodiments. Let \(\mathcal A\) be the **finite set of genuinely signed policies** using Y, and let \(\mathcal B\subseteq\mathcal A\) be those implementable using only Z. For a vector of conditional potential captured contributions m in a *nonempty compact polytope* \(\mathcal M\) built from actual support, physical limits and justified linear restrictions, let \(F_a(m)\) and \(C_b(m)\) denote the population contribution of a fine and a coarse policy. Both are linear in m for fixed report masses. The gross refinement value is

\[
L(m)=\max_{a\in\mathcal A}F_a(m)-\max_{b\in\mathcal B}C_b(m)\ge0.
\tag{4}
\]

Even though L is generally neither convex nor concave in m, its **sharp identified extrema** are computed by *finite collections of linear programs*:

\[
\underline L=\min_{b\in\mathcal B}\quad \min_{m\in\mathcal M,t}\ t
\quad\text{s.t. } t\ge F_a(m)-C_b(m)\ \forall a\in\mathcal A;
\tag{5}
\]

\[
\overline L=\max_{a\in\mathcal A}\quad \max_{m\in\mathcal M,t}\ t
\quad\text{s.t. } t\le F_a(m)-C_b(m)\ \forall b\in\mathcal B.
\tag{6}
\]

**Proof.** Pointwise, \(L(m)=\min_b\max_a(F_a(m)-C_b(m))=\max_a\min_b(F_a(m)-C_b(m))\); the maximum/minimum of independently indexed finite scalars commute after subtracting their own independent maxima. For the global lower endpoint, \(\min_m\min_b=\min_b\min_m\). Holding b fixed, minimize an epigraph variable t of the maximum of finitely many linear functions: (5). For the global upper endpoint, \(\max_m\max_a=\max_a\max_m\). Holding a fixed, maximize a hypograph variable t of the minimum of finitely many linear functions: (6). Compactness attains extrema. All are exact conditional on \(\mathcal M\) representing the feasible economic conditional mean vectors, and \(\mathcal A,\mathcal B\) being truly nested. This is elementary finite linear optimization and partial-identification theory, **not an original general LP method**. It accommodates joint scarce-resource signed policies by treating each as a single action; it does not assume separable per-robot decisions.

If original-customer report masses themselves are unidentified, equations (5)–(6) require a justified joint moment-polytope representation, such as variables \(q_{dy}=p_y m_{dy}\) and linear restrictions, rather than pretending uncertain products remain linear. If behavior of the entire learning network changes with report exposure, there is no single fixed m on both sides and the common-experiment proof fails.

## What the result changes for Model A, Model B and empirical execution

**Model A (qualified customer production).** The action-margin signs tell us which observations can actually switch the production LP's optimal whole-network recipe. On a certified local active production basis, resource-price duals may interpret an action margin, but all feasible alternative columns, demand, qualification and changing shadow prices must be recomputed before asserting report value. Joint operator and customer capacity can make a report useful only when a different *network-wide* allocation is available.

**Model B (recursive learning and production).** An information report that only changes a choice within a fixed trained controller is compared by (1)–(6). More source trajectories, production-generated failures, teleoperation, simulation, curation, target finetuning and a newly manufactured embodiment alter learning, assignment, available actions and sometimes the whole market. Compare the corresponding full dynamic \(J\) once; the cost of data rights, operator displacement, training, qualified fallback and future customer learning belongs in that same J, never appended as an independent data premium. Expanding free optional data cannot reduce an optimized value if the old feasible policies remain available; forced updates can harm a selected recipe.

**Empirical implication.** We need not first identify every unseen return if a policy-relevant sign reversal can be certified from actual qualified original-buyer receipts and finite physical response caps. Conversely, positive model-validation accuracy, positive transfer on an unseen task, or a higher episode count cannot identify even the sign of the paid-service action margin. Restrict target data collection to (i) predecision economically relevant context; (ii) signed alternative action support; (iii) whole learner/operator/customer cluster exposure; (iv) joint completed/accepted/refunded/paid original-service outcomes and a natural buyer denominator. Do **not** run unapproved actions to fill missing cells. If justified support only yields \(\underline L\le c\le\overline L\) for the actual end-to-end observation cost c, an economic go/no-go decision is **not identified**. If \(\underline L>c\), a gross-within-program observation choice is robustly worthwhile, *unless an omitted already-licensed E or R action changes the menu*. If \(\overline L<c\), it is robustly not worthwhile on that fixed program. These are prospective decision conditions, not empirical recommendations.

**Prior art and status.** Blackwell's information order and Jensen report gap, partial-identification approaches in Manski's treatment-choice literature, Caplin–Martin *Comparison of Decisions under Unknown Experiments* (JPE 2021, https://doi.org/10.1086/716104), Christensen–Moon–Schorfheide *Optimal Decision Rules When Payoffs are Partially Identified* (REStud, published March 2 2026, https://doi.org/10.1093/restud/rdag017), and Dudík–Langford–Li *Doubly Robust Policy Evaluation and Learning* (ICML 2011, https://www.microsoft.com/en-us/research/publication/doubly-robust-policy-evaluation-and-learning-2/) provide the principal decision/identification foundations. Farboodi–Koh–Xia *Data-Driven Automation* §5 and Appendix B already treat future productive data and aggregation. We claim only a **conditional synthesis and explicit sharp specialization for the continuing qualified robotics policy model**, not independently established scientific novelty. Checked public publication metadata 21 November 2026; not a comprehensive priority audit.

**Scientific gap.** Nothing here establishes an actual BridgeData/DROID/source-archive learner effect, signed real-world A/B/E/R response panel, episode-lineage transfer, full paid customer cohort or numerical official BEA–BLS industry transaction. November 22 acceptance stays **OPEN**. The immediate proof/empirical dependency is: which action-margin sign changes can be justified without unlicensed counterfactuals, and which physically permitted cluster intervention would tighten the economically decisive missing cell? The complete Models A/B production network and Christmas roadmap are unchanged.
