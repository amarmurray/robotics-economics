# Lawful structural zeros, sharp economic transfer bounds, and the value of an original-buyer audit

**22 November 2026 — *When Capabilities Become Production*, integrated Models A/B.** This chapter continues [the longitudinal audit and policy-support argument](LONGITUDINAL_AUDIT_AND_POLICY_SUPPORT.md), [the selected-history evidence result](SELECTED_HISTORY_AND_DECISION_SUFFICIENT_EVIDENCE.md), and the [globally coupled learner/demand/multiple-job network](GLOBALLY_COUPLED_MULTI_JOB_PRODUCTION.md). It answers the precise unresolved issue: **what can be inferred and chosen when a historically untried action or a legally unavailable report has exactly zero support?** All numerical examples below are invented conditional production laws, not field evidence. The November 22 science gate remains OPEN.

## 1. One production-value environment, not three disconnected payoffs

The admissible production decision is a *whole program*: P acquires source experience through accepted productive field work; G spends on lawful target-specific grounding of eligible existing source data; E purchases or enables a distinct embodiment with actually independent robot and operator capacity. The feasible controller for each program may retain the earlier safe production policy. Source types (routine trajectories, unsuccessful recoveries, teleoperation, simulation, synthetic generation, and public/pretrained inputs) have distinct lineage, permissions, and learning kernels; neither human intervention nor public data is privileged by definition.

For a connected original-buyer, shared-learner and recovery-worker cluster, let ω be a **complete, globally coherent potential history**: for each lawful intervention it records qualification, target demand and no-orders, cleared worker queue and future jobs, paid accepted original services, physical capacity, data rights, and program-specific costs. A single latent law μ over complete histories governs **all P/G/E comparisons**. A policy π is nonanticipative and must be legally and physically admissible for its own program. Its contribution vector f_{a,π}(ω) contains already accepted paid production, correctly netted costs, and appropriately discounted continuation paid production exactly once. **There is no separate data premium appended to continuation output.**

Finite lawful controller menus Π_a and observable logging map M give the partial-identification set

\[
\mathcal M=\{\mu\geq0:\mathbf1^\top\mu=1,\;M\mu=q,\;C\mu=d\}.
\tag{1}
\]

Here q is a *joint* observable distribution including recorded action/audit selection, not just selected invoices. C expresses justified physical conservation and cross-arm structural restrictions; unknown response to an untried action is **not** inserted into C as a known coefficient. Bounds below are population identification statements conditional on exact q and correct C, not sampling confidence intervals. Without actual q, they are a symbolic design and synthetic demonstration.

### The distinction that changes the investment menu

* **Legally/physically forbidden:** the target policy is excluded from Π_a. Assigning its outcome an unrestricted favorable interval does not make it investible.
* **Permitted but never logged:** a policy remains in Π_a, but its counterfactual action-specific components are generally not observed. An action propensity e=0 cannot be divided into; inverse weighting from the previous chapter fails on that path. Keep a nonparametric identified interval instead of replacing the structural zero with an invented ε.
* **Logged action, missing original-buyer outcome:** the intervention may be supported, but an outcome-dependent report mask identifies only a subset of its buyer process. Additional lawful preoutcome audits can sometimes shrink this uncertainty, but cannot create action support.

The firm may train using newly available free data only if it wishes; therefore the old controller remains an admissible policy. A particular forced training recipe can cause negative technical transfer without implying that free, optional data availability lowers optimized value. Costly curation, compute, rights and displaced capacity can lower **net** acquisition value.

## 2. Sharp finite-menu optimized-value certificate

Write \(F(\mu)=\max_{i\in\Pi_P}f_i^\top\mu\), \(G(\mu)=\max_{j\in\Pi_G}g_j^\top\mu\). We compare entire causal program values, including physically shared worker and buyer paths, rather than optimizing qualification and demand in separate probability worlds.

**Proposition (sharp common-law P–G oracle interval).** For a nonempty compact convex polytope \(\mathcal M\) and finite legal menus,

\[
L=\min_j\;\min_{\mu\in\mathcal M,\,t}
\left\{t:\ t\geq(f_i-g_j)^\top\mu\quad\forall i\right\},
\tag{2}
\]

\[
U=\max_i\;\max_{\mu\in\mathcal M,\,t}
\left\{t:\ t\leq(f_i-g_j)^\top\mu\quad\forall j\right\}.
\tag{3}
\]

Then \(L=\min_{\mu\in\mathcal M}[F(\mu)-G(\mu)]\) and \(U=\max_{\mu\in\mathcal M}[F(\mu)-G(\mu)]\). Each subproblem is a linear program. The bounds are *sharp relative to \(\mathcal M\)*: the optimized payoffs at extremizing feasible **common** histories attain the endpoints.

**Proof.** At fixed μ,
\[
F(\mu)-G(\mu)=\min_j\max_i(f_i-g_j)^\top\mu
=\max_i\min_j(f_i-g_j)^\top\mu.
\]
The finite minimum j commutes with the outer minimum over μ in the first expression; epigraph t converts the remaining maximum i to (2). The finite maximum i commutes with the outer maximum μ in the second; hypograph t converts the remaining minimum j to (3). Compactness gives attainment. This proof does **not** exchange \(\min_\mu\max_i\) with \(\max_i\min_\mu\) for deterministic controllers, nor does it allow each arm an unrelated adversarial μ. The same equations apply to P/E, G/E or a larger network policy set.

A distinct implementable ex-ante guarantee is
\[
\max_{x\in\Delta(\Pi_P)}\min_{\mu\in\mathcal M}
\sum_i x_i f_i^\top\mu ,
\tag{4}
\]
where x is a *committed randomization rule* before learning the true world. With authorized randomization and a convex law family, finite minimax duality applies; a state-contingent oracle action selected after seeing μ is **not** implementable from selected logs. Randomizing indivisible investment choices is meaningful only if the economic objective and physical deployment units actually permit such randomization. Otherwise report deterministic robust menus separately.

**Identification test.** For a fixed policy contrast vector \(v\), observational and physical restrictions identify its value precisely iff \(v^\top(\mu-\nu)=0\) for every feasible \(\mu,\nu\in\mathcal M\). If \(\mathcal M\) has a relative-interior point in the full affine slice \(A\mu=b\), this is equivalent to \(v\) lying in the row span of A. It is a nullspace property of the *economic payoff vector*, not a property of benchmark accuracy. At boundary-only feasible sets use the span of actual feasible differences, not the unrestricted row-span test. A new report row about Y under an old policy cannot kill a null direction affecting only the untried G-action outcome.

## 3. A sharp, fully constructed support-zero counterexample

Take a single terminal service opportunity embedded as a restricted face of the multi-date physical model. Its original eligible buyer order \(Y\in\{0,1\}\) is shared between the **old** P and G recipes. The recorded sample reports the joint fractions

\[
\Pr(S=1,Y=1)=\tfrac14,\quad
\Pr(S=1,Y=0)=\tfrac14,\quad
\Pr(S=0)=\tfrac12.
\tag{5}
\]

Reporting S is permitted to be outcome-dependent; the S=0 episodes have neither full original-offer records nor uncensored old-service receipts, while action identities and safety states are known. Consequently \(p=\Pr(Y=1)\in[1/4,3/4]\) with no missing-at-random assumption. Let \(x=\Pr(S=0,Y=1)\in[0,1/2]\), so p=1/4+x. No reported data select x.

P's source-learned retained controller has a qualified available robot for Y and net accepted paid contribution \(P(p)=p-1/8\), including source-data and deployment cost. Under G's existing lawful controller, a separate fair qualification gate U passes with probability one half independently of Y, giving \(G_R(p)=p/2-1/16\) after licensing cost. A physically permitted **but never dispatched** target-grounding action T reuses existing licensed data and offers new qualification. Its paid reward requires the *joint event* that original buyer Y orders, target qualification succeeds and the one recovery worker remains available:
\[
\theta=\Pr(Y=1,Q^T=1,J^T=0),\quad 0\leq\theta\leq p.
\]
The target-grounding-plus-validation policy earns \(G_T(\theta)=\theta-3/32\), after its **total** cost (including an extra 1/32 relative to retained G); G may choose either policy. An independently staffed E embodiment serves a stipulated other original-buyer contract and gives a certain net contribution \(E=9/20\). This independent contract and worker/robot budget are assumptions, **not inferred from the observed site**.

This construction makes no assumption of fixed universally positive transfer. Q^T and J^T may be arbitrarily dependent with Y, consistent with one robot and one worker; T can create a job that blocks payment. For any allowed (p,θ), split the buyer-positive mass p into θ of qualified-and-available T service and p−θ of unsuccessful/blocked T service. Then split Y among the observed/masked cells according to (5), and draw old G qualification U independently. This provides an explicit common potential-history coupling for **every** (p,θ) in the trapezoid; all its points are feasible. A richer model allowing T to *change* demand would require distinct \(Y^T\) and generally **widen** the identified set—old-buyer auditing alone would not even justify \(\theta\le p\).

Under these precise assumptions,
\[
P^*=p-\tfrac18,\qquad
G^*=\max\{p/2-\tfrac1{16},\,\theta-\tfrac3{32}\},\qquad E^*=\tfrac9{20}.
\tag{6}
\]
Thus the **sharp** G−P interval is \([-5/16,\;1/32]\), with P in \([1/8,5/8]\) and G in \([1/16,21/32]\). Three worlds have **exactly the same *selected* original-buyer/old-service outcome records and zero historical T exposure**. In this counterexample S is also the availability mask for old-action receipts and accepted-service outcomes; a complete uncensored invoice/qualification panel would impose additional restrictions and may reveal p:

| Feasible world | p | θ | P | G (optimized) | E | Optimal |
|---|---:|---:|---:|---:|---:|---|
| A: all unreported buyers are no-orders | 1/4 | 0 | 1/8 | 1/16 | 9/20 | E |
| B: unreported buyers order; T succeeds and has clear worker | 3/4 | 3/4 | 5/8 | 21/32 | 9/20 | G |
| C: buyers order but T never qualifies-and-clears | 3/4 | 0 | 5/8 | 5/16 | 9/20 | P |

**Constructive interpretation.** Every investment can win the **same observational equivalence class**. Ex-ante deterministic maximin values are P=1/8, G=1/16 and E=9/20, so the robust selection is E (under the strong stipulated E guarantee). An authorized complete audit of old original eligible buyer Y that reveals \(p=3/4\) changes the robust choice from E to P (P=5/8; G can still be as low as 5/16). It does **not** identify whether G's untried intervention is worth 21/32; only new, lawful and physically supported action evidence or extra defendable structural restrictions can address that null direction. If T is actually **forbidden** by rights or safety, remove it from G's menu altogether; the B-world G victory then vanishes. An audit cannot legalize an action.

These are exact conditional rational constructions, not measured dollars. The field counterpart requires joint qualification, original buyer offers/no-offers, actual worker job clearing, actual accepted paid orders and costs on **matched service recipes**. A reported classifier/robotics benchmark change is not a cash outcome.

## 4. Which original-buyer audit is economically worth acquiring?

For a fixed supported pair of policies, suppose the remaining unreported **finite original buyer episodes** have binary outcomes \(Y_i\), and, after conditioning on physically known queue eligibility and rights, the *incremental paid contribution contrast* is
\[
\Delta=\Delta_0+\sum_{i=1}^N d_iY_i,
\tag{7}
\]
with no remaining cross-episode restrictions. With independent unrestricted missing bits, the exact identification width before audits is \(\sum_i|d_i|\). Auditing a set \(A\) with verified truthful, lawful original-order reports makes the **remaining** width \(\sum_{i\notin A}|d_i|\), regardless of their observed outcomes. The exact minimum-width permitted audit is the binary knapsack
\[
\max_{A\subseteq\mathcal L}\ \sum_{i\in A}|d_i|\quad
\text{s.t.}\quad \sum_{i\in A}c_i\le B,
\tag{8}
\]
where \(\mathcal L\) is the set of *legally observable* missing episodes and c_i is total audit cost. This prices audits by their effect on the **production decision margin**, not by raw technical entropy or accuracy. For physically constrained joint histories, (7) is no longer separable and one must re-solve common-law LP (2)-(3) after each candidate report; the knapsack must not be asserted universal.

**Separate finite audit example:** four masked original-buyer entries have contrast weights (6,4,3,1)/16. Entry 0 is legally nonauditable; auditing each of entries 1–3 costs 1, and budget B=2. Enumerating all feasible choices proves the unique optimal audit is entries 1 and 2, shrinking exact total contrast width from 14/16 to 7/16. The forbidden first episode contributes an irreducible width 6/16, even with unlimited budget. These audit figures are a second stylized design example, not the population observation law of (5).

**Proof of width and allocation.** Each unseen binary \(Y_i\) can independently take whichever endpoint maximizes or minimizes \(d_iY_i\); fixing a revealed Y_i removes exactly \(|d_i|\) from the upper-minus-lower contrast. With a common fixed budget, minimizing the residual sum is equivalent to maximizing removed absolute weights. If an episode has *known zero paid-service and zero continuation effect because the worker is terminally blocked*, its d_i=0 and buyer reporting is economically unnecessary **for that exact menu/horizon**. In a recursive learner or demand-response system, an unserved original buyer may generate information and have nonzero future effects; do **not** set d_i=0 merely because no current invoice cleared.

### What audit design cannot repair

A recorded original-buyer report under action R can shrink p, but generally leaves \(\theta=\Pr(Y^T=1,Q^T=1,J^T=0)\) unidentified if T has e=0. If T is not physically or contractually permitted, neither T trials nor T-conditional reports belong to the allowed research design; the proper response is menu removal and documentation. If it is permitted but has no existing propensity overlap, any proposed new randomized T trial needs its own safety, rights and customer authorization outside this research remit. No trial is authorized or conducted here.

## 5. Comparison with closest literature and empirical discrimination

These LP bounds are a conditional application of *partial identification and missing-data* mathematics, not a new Manski theorem: see Manski (2005), [“Partial identification with missing data”](https://doi.org/10.1016/j.ijar.2004.10.006), and Lee & Weidner (2021), [limited-overlap treatment-effect bounds](https://arxiv.org/abs/2111.05243). Sequential support and policy valuation rely on Robins/Hernán/Brumback (2000) and [Jiang & Li (2016)](https://proceedings.mlr.press/v48/jiang16.html). The closest economic seed, Farboodi/Koh/Xia [*Data-Driven Automation* (June 2026)](https://www.nber.org/papers/w35320), already models the production and future value of endogenous data, with aggregation complementarities. No claim of discovering that broad mechanism is warranted.

The proposed synthesis is the **intersection** of (a) rights-feasible intervention menus, (b) joint learner/qualified-buyer/operator histories in a physically shared production network, and (c) observation support sufficient to certify an economically meaningful P/G/E investment. The theoretical result that the best *available* action remains optional is distinct from the empirical hypothesis that more data increases deployable qualification. To discriminate: record original buyer/no-buyer denominators rather than selected invoices; compare matched P field trajectories, G rights-cleared grounding and E independently resourced recipes; capture conditional recovery and demand coupling; register preoutcome reporting and action selection; and measure cleared paid service without assuming independent site failures.

The new [prospective field/support ledger](STRUCTURAL_ZERO_ACTION_AND_AUDIT_EVIDENCE.md) and [reproduction](STRUCTURAL_ZERO_REPLICATION.md) identify what would change the sharp set. The [executable rational synthetic model](structural_zero_common_law.js), [record](structural_zero_common_law_results.json), [exercises](STRUCTURAL_ZERO_EXERCISES.md) and [instructor solutions](STRUCTURAL_ZERO_SOLUTIONS.md) are part of the reproducible theoretical package. This chapter does not estimate actual source-to-qualification transfers, work out a BEA/BLS quantitative input-output network, verify independent E deployment staffing, obtain any original-buyer payments or rights, or establish independent novelty.

**Exact next obligation:** extend the support-zero polytope to a *policy-dependent multi-date* learner/customer/recovery kernel and derive a **prospectively feasible economic report allocation** after accounting for within-fleet interference and qualified original demand. Preserve old P/G/E and safe-policy results where their assumptions survive; retain the multilayer diffusion, capital allocation, production atlas, manufacturing, deployment ownership and contract roadmap. November 22 scientific acceptance is **OPEN**; theory emphasis through December 6 and all intermediate milestones are unchanged. Deadline: **December 25, 2026, 23:59 America/New_York**.
