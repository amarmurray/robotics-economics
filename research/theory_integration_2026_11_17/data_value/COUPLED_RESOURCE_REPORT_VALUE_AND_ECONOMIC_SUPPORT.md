# Coupled original-buyer capacity and the economic value of source/grounding reports

**21 November 2026 — conditional theoretical continuation, not observed robotics returns.** This chapter extends [signed action-margin support](SIGNED_ACTION_MARGIN_SUPPORT_AND_REPORT_VALUE.md) inside the *same* November 22 Model A/Model B argument. The previous sharp interval result is valid under rectangular, report-by-report feasible action-margin sets. The precise unresolved question is whether a **common scarce operator/resource opportunity** creates defensible restrictions linking potential economic outcomes across report states, and whether those restrictions change which missing observation is valuable. We do not introduce a new source-training curve or substitute an informational result for the X source/G grounding/E embodiment total-policy comparison.

## 1. Economic environment and the two different kinds of coupling

Consider one original customer cohort per decision epoch together with an outside original, accepted and paid service opportunity that competes for a single signed operator slot. A predecision fine report Y is drawn from an original-buyer distribution p; a coarse report Z=φ(Y) is available without paying for the refinement. A and B are complete, previously qualified and physically approved network policies, including service, outside-order dispatch, human recovery, resource occupancy, acceptance/refund and captured contribution. The old R controller remains available; it cannot be assumed to recover unapproved A/B failures for free. For now the same trained learner and legally feasible A/B menu are held fixed under Y and Z.

For any true economic environment θ, let δ_y(θ)=m_A(y;θ)−m_B(y;θ) denote the **complete original-buyer network** accepted-paid contribution advantage; cash attributable to the outside order is included in m exactly once. The old gross fine-over-coarse report value identity remains

\[
L(\theta)=\sum_z\min\{P_z(\theta),N_z(\theta)\},\quad
P_z=\sum_{y\in z}p_y[\delta_y(\theta)]_+,\quad
N_z=\sum_{y\in z}p_y[-\delta_y(\theta)]_+.
\tag{1}
\]

Two couplings must not be conflated. **Within-world physical coupling** limits which robots/operators/orders can be dispatched simultaneously; A and B must each describe an entire feasible network allocation. **Across-report response coupling** says that alternative report-state conditional outcomes share some stable primitive θ (such as the same verified outside-job contribution or productive resource technology). The first does *not* logically establish the second: Y may affect other-buyer demand, resource prices, rights, arrival rates, or qualification, invalidating a common parameter. The following is an explicit conditional case, not a general fact about robot fleets.

## 2. Proposition: sharp refinement bounds under affine shared primitives

Assume p_y>0 is known for the full predecision original-offer cohort; the coarse partition φ and complete signed action menu are fixed; the action-specific potential captured means are well-defined under the same network policy closure. Suppose a compact nonempty polytope Θ contains the unknown common primitive θ, with

\[
\delta_y(\theta)=a_y+b_y^{\mathsf T}\theta,\quad \theta\in\Theta.
\tag{2}
\]

A known-bounded or partially identified response parameter is not a predecision observable by assumption. We identify the functional L at each admissible true environment. For any feasible joint sign region S, define its closed polytope Θ_S={θ∈Θ: δ_y(θ)≥0 for y∈S, δ_y(θ)≤0 for y∉S}. On Θ_S,

\[
P_z(\theta)=\sum_{y\in S\cap z}p_y\delta_y(\theta),\qquad
N_z(\theta)=-\sum_{y\in z\setminus S}p_y\delta_y(\theta)
\tag{3}
\]

are nonnegative affine functions. The **sharp upper endpoint** of L over Θ_S is the linear program

\[
\max_{\theta\in\Theta_S,\ t_z\ge0}\sum_z t_z
\quad\text{subject to}\quad
t_z\le P_z(\theta),\; t_z\le N_z(\theta)\quad\forall z .
\tag{4}
\]

The **sharp lower endpoint** over Θ_S is the minimum of L evaluated at its vertices. Taking the smallest lower and largest upper across all feasible sign regions gives the globally sharp identified interval. This does not require independent report-cell bounds or independently qualified recipes; the signed whole-network policies are actions.

**Proof.** Equation (1) follows by subtracting the always-B contribution from the optimized Y and Z decision values. Inside a sign region, each P_z and N_z in (3) is affine; their minimum is concave, hence the sum L is a continuous concave piecewise-linear function on a compact polytope. A concave function has a minimizing vertex (express every point as a convex combination of vertices). Its hypograph on this sign region is exactly the linear system in (4), making the upper endpoint an LP. A finite sign cover includes every θ, including overlapping zero boundaries. Compactness and construction establish attainment and sharpness. This is standard finite polyhedral optimization, not a novel general method. For a nonpolyhedral or nonlinear physical-response map, numerical grids do not prove these endpoints.

**Implication.** The earlier rectangular positive-information criterion (some individually forced A-positive report and some individually forced B-positive report in the same coarse cell) is **not necessary under coupled response restrictions**: individually ambiguous reports may be forced jointly to support A somewhere, even though no particular report is uniformly A-positive. Conversely, pretending all cross-report responses share a primitive may invent a positive lower bound. A policy certificate must establish the coupling, not just name a common robot.

## 3. Fully specified original-buyer/operator example

Three predecision original-customer network report states have probabilities p=(1/2,1/4,1/4) and are compressed to one Z. There is exactly one operator slot and one outside original buyer whose accepted, actually paid service contribution per available slot is the *same* λ∈[0,1/2] in all three report states. This invariance is a testable assumption about accepted original orders and an available/qualified outside recipe, not an inferred shadow-price estimate. One buyer's qualified A/B policy uses the slot as follows:

| State | Signed A service contribution | A operator use | Signed B service contribution | B operator use |
|---|---:|---:|---:|---:|
| y1 | 3/2 | 1 | 1 | 0 |
| y2 | 3/4 | 1 | 1 | 0 |
| y3 | 1 | 0 | 1 | 1 |

The unused slot is deployed to the already accepted outside order, earning λ. No resource is used twice. Therefore the **entire network** potential contributions satisfy

\[
m_A=(3/2,\ 3/4,\ 1+\lambda),\qquad
m_B=(1+\lambda,\ 1+\lambda,\ 1),
\]
\[
\delta(\lambda)=(1/2-\lambda,\ -1/4-\lambda,\ \lambda).
\tag{5}
\]

Fine-report policy A on y1 and y3, B on y2 is feasible and *uniformly optimal* over all λ in this interval (weakly so at zero ties). Thus an implementable policy does not require an oracle to reveal λ in order to attain fine-report V. Coarse policy chooses A when λ≤3/8 and B when λ≥3/8; its optimal choice depends on the unknown common economic primitive. Direct evaluation yields

\[
P=1/4-\lambda/4,\quad N=1/16+\lambda/4,\quad
L(\lambda)=\min\{1/4-\lambda/4,\ 1/16+\lambda/4\}.
\tag{6}
\]

Hence **the sharp coupled interval is [1/16,5/32]**. Its minimum occurs at λ=0, its maximum at λ=3/8, and its value at λ=1/2 is 1/8. This is gross captured contribution *inside the fixed hypothetical program*, not dollar ROI or value that may be added to E's prior program payoff.

If we discard the shared-λ constraint and retain only the sharp per-report marginal bounds δ1∈[0,1/2], δ2∈[−3/4,−1/4], δ3∈[0,1/2], the previous rectangular formulas instead yield **[0,3/16]**. Those bounds are sharp for the larger rectangular set, but overly pessimistic and optimistic for the common-capacity model. In particular no single report is *strictly* A-positive over the complete λ range (δ1=0 at 1/2; δ3=0 at 0), although at least one must be A-positive for every λ. The always negative y2 margin gives a strictly positive report value across the common-λ model.

There is a direct falsifying counterworld. Let outside-job opportunity vary by report, λ_y=(1/2,0,0), without changing the three marginal interval bounds or A/B resource requirements. Then δ=(0,−1/4,0) and **L=0**. The [1/16,5/32] inference collapses if the outside order, permissions or its paid contribution are *endogenous to Y*. It would be unjustified to label y-varying λ as measurement noise and retain the positive lower certificate.

## 4. Economically decisive measurement and information timing

Suppose direct, licensed observation of Y costs c=1/8 in the same normalized contribution units, with no effect on demand, controller weights, rights or physical admissibility. By (6), observing Y strictly beats the optimal coarse report *given the true fixed environment* iff 1/4<λ<1/2, ties at λ=1/4 or 1/2, and loses for lower λ. At a cost below 1/16 the within-program observation is robustly worthwhile; at a cost above 5/32 it is robustly not worthwhile. In the intermediate region, the **economically decisive missing quantity** is the common outside-order paid contribution and its cross-report invariance, not one more classifier accuracy point or a complete missing-response cube. An audit to discover λ itself is a separate earlier information decision whose cost and consequences must be modeled, not silently treated as free foresight.

These are identified-value bounds for fixed true payoffs and optimal coarse policies; they must not be confused with expected values under a prior over λ, minimax regret of implementable coarse rules, or a free report on λ. A robust fine action rule exists here because the signs in (5) are weakly uniform. In a different parameterization, the fine optimal rule might vary with λ, and partial identification of oracle value would not by itself exhibit a single robust deployable rule.

The structural restriction is physically substantive: operator capacity, a pre-existing legally qualified outside opportunity, service durations, whole-network accepted paid receipts, and report-invariant access/terms together imply (5). A resource-price dual is at most a **certificate on the appropriate LP basis**; once the report changes basis, demand, feasible recipes or opportunity cost, recompute the complete production optimum. A static shadow price cannot be assumed invariant by naming it λ.

## 5. Integration with data transfer, embodiment and recursive production

**Model A.** This is one fixed learnt controller's eligible qualified-service dispatch comparison, including the shared operator outside option; neither per-robot task accuracy nor independent action rewards equal economic data value. The original demand denominator includes the unused original buyer and actual accepted outside order. The joint resource allocation is explicit rather than allocating a slot twice. The example is a resource-network restriction on the earlier partial identification set.

**Model B.** A source X archive, fresh source episodes, teleoperation, simulation, failures and production-generated field trajectories alter the learner's conditional target qualification and therefore may change the coefficients a_y, b_y, report law p_y, or physical action menu. G-observe (a truly predecision unchanged-kernel refinement) uses (1); G-train/reweighting may alter all those primitives, and E adds an embodiment and new physically permitted whole-network recipes. A new body may relax the shared slot constraint or induce new operator work; that must be optimized in full J across current and future original buyer opportunities, including data rights, curation/compute, manufacturing, market response, fallback and transfer. The existing synthetic E dominance remains intact unless the actual E program changes. Free optional data cannot lower optimized value while old policies remain feasible; forcing updates may lower a particular recipe. No separate data premium is added to J.

**Economic-network atlas.** This model makes a concrete multilayer edge testable: original buyer A/B production tasks, operator capacity, competing outside buyer order and receipt, source/target report, qualification, and learning rights. A BEA/BLS input–output sector matrix cannot infer this firm/customer/operator edge; obtain any numeric official sector cells only from actual versioned quantitative primary material.

## 6. Prior art, limitations and next scientific obligation

The Blackwell comparison of experiments and conditional Jensen gap precede this chapter; finite stochastic programming with recourse and polyhedral partial-identification/treatment-choice tools likewise precede it. Checked source locators: Khan, Yu & Zhang, *Economics Letters* 247 (February 2025), doi:10.1016/j.econlet.2024.112146 (Blackwell theorem); Louveaux & Birge, *Two-Stage Stochastic Programs with Recourse* (2001), doi:10.1007/0-306-48332-7_531; Manski, *Partial Identification of Counterfactual Choice Probabilities* (first published 11 December 2007), doi:10.1111/j.1468-2354.2007.00467.x. This chapter's contribution is a **conditional integration and falsifiable economic-support distinction**, not an independently certified new theorem.

No actual original-buyer paid-receipt/operator-panel, report-invariant outside opportunity, approved A/B customer robot policy, learning intervention, episode lineage, original BEA/BLS numerical input, independent novelty review or full repository CI has been obtained. The [prospective verification design](COUPLED_RESOURCE_EVIDENCE_PROTOCOL.md) is unpopulated and does not authorize unsafe experiments. The [pure CPU executable](coupled_resource_report_value.js), [record](coupled_resource_report_value_results.json) and [separate exercises](COUPLED_RESOURCE_EXERCISES.md)/[solutions](COUPLED_RESOURCE_SOLUTIONS.md) test exactly the declared synthetic model.

**Exact next obligation for November 22:** include the cross-report response restrictions as explicitly *conditional* in Model A/B, then distinguish which lawful original-buyer/whole-network observations establish a common outside opportunity rather than report-conditioned demand. If that restriction fails, revert to the broader polytope/rectangular response set instead of defending the positive certificate. For the subsequent full program, identify physically supported X/G-train/E total policy effects with joint qualification and original paid-service measures, preserving the theory-majority phase through December 6 and the final 25 December 2026, 23:59 America/New_York cutoff.
