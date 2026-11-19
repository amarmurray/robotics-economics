# Transporting data-derived reports across learned controllers: decision regret and customer value

**19 November 2026, conditional theoretical continuation.** This is the next layer of *When Capabilities Become Production*, following [signal disclosure versus qualified controller admission](SIGNAL_VS_ADMISSION.md), the November 22 estimand reconciliation, and the source-to-joint-qualification production model. It addresses a missing assumption: a report calibrated on source-policy trajectories need not remain calibrated after source learning changes the controller, reachable customer states, recoveries or diagnostic distribution. Nothing below is an observed robotic return, a safety approval, or a claim of independently novel decision theory.

## One economic environment, three different operations

Hold a **pre-source** economically relevant customer-opportunity state z with fixed population p(z) and complete-policy net captured contribution y_c(a,z). The contribution is the optimized qualified production value V(Q;omega) and eligible dynamic continuation J, including **all original orders**, displaced specialist service, dispatch, scarce human operators, recovery, customer demand and implementation costs exactly once. A continuation action a must already be independently physically approved; old qualified policies and a competent specialist remain available where feasible. A learned controller c changes the qualified continuation menu M_c and/or the whole-network outcome table y_c. This is *technical admission*, not diagnostic accuracy.

A source-derived **nonactuating report** s has conditional observation kernel K_c(s|z), which may change with the controller or target-data distribution. Merely displaying a frozen, validated report is an information intervention. **Calibration or target grounding of the report** changes the information with which the planner chooses among already approved policies, not their physical qualification. A different operation, **controller grounding**, changes y_c, joint qualification or the safe menu and requires a separate qualification comparison. Embodiment acquisition changes Q, compatible recipes, access/manufacturing delay and scarce resource demand. None can be identified from a benchmark-percent improvement alone.

For a fixed c, common p and noninvasive K, define gross complete-network optimized value

\[
W_c(K)=\max_{\pi:S\to M_c}\sum_{z,s}p(z)K(s\mid z)y_c(\pi(s),z).
\]

A constant policy ignores the report. If its observation, validation or target-label acquisition is costly, charge that real incremental cost once outside W. Do not append a second continuation-data premium to J. Physical actions, customer orders and resource constraints that couple simultaneous reports must be represented as a single *joint* network action and report, rather than pretending independent per-robot choices.

## Proposition: how much source-report transport can move economic policy value

Fix c, a finite approved menu, one economically relevant state population p, and a fixed whole-network outcome table y_c. Let K and K' be two kernels on the same measured state/report meanings and support. Define the **state-specific feasible contribution span** R_c(z) = max_a y_c(a,z) - min_a y_c(a,z), and conditional total variation d_z = TV(K'(.|z),K(.|z)). Then

\[
\epsilon_c(K,K')=\sum_z p(z)R_c(z)d_z,\qquad
|W_c(K')-W_c(K)|\leq\epsilon_c.
\]

If pi_K optimizes under the old source kernel K and is physically approved under the new one, the loss from applying it with K' rather than recalibrating the approved decision rule satisfies

\[
0\leq W_c(K')-\mathbb E_{pK'}y_c(\pi_K(s),z)\leq 2\epsilon_c.
\]

Proof: for each fixed policy, conditional total variation bounds its expected whole-service difference by the contribution span at each z. Supremizing preserves the bound on W. Add and subtract the two old-kernel policy values, using old-kernel optimality. The factor-two bound may be extremely loose. It does **not** establish any economically small calibration error unless both conditional kernel deviations and compatible whole-network contribution spans are independently supported.

A sharper **decision-stability certificate** avoids the generic span. For each report s, alternative approved action a, and source-optimized a_s=pi_K(s), compute the joint payoff margin

\[
D_K(s,a)=\sum_z p(z)K(s|z)[y_c(a_s,z)-y_c(a,z)]\geq0.
\]

The same rule stays optimal after transport if for every s,a

\[
D_K(s,a)\geq\sum_z p(z)|K'(s|z)-K(s|z)|\,|y_c(a_s,z)-y_c(a,z)|.
\]

Indeed the right side bounds the most adverse change in each pairwise joint expected-payoff difference. A tie can remain a tie. This condition concerns **reoptimization regret**; even if the selected mapping stays unchanged, a genuinely improved signal kernel can still raise realized service by matching states to actions more often. Thus “the decision rule did not change” is **not** equivalent to “the additional observations have no economic value.”

If controller admission changes p(z), y, feasible policies, report semantics or policy-induced recovery/dispatch response, these inequalities are *not* valid cross-controller causal certificates. They hold only within a fixed qualified physical configuration. The broader first-exit support bounds, whole-network randomized policy comparisons and intervention-dependent V(Q;omega),J remain necessary.

## Controlled information × qualification versus a drifting report

The preceding chapter held the same K across controller admissions c=0,1. If the source reporter changes from K_0 to K_1, the observed signal-arm contrast can be decomposed, *where cross-play is actually meaningful*, as

\[
W_1(K_1)-W_0(K_0)
=[W_1(K_0)-W_0(K_0)]+[W_1(K_1)-W_1(K_0)].
\]

The first bracket is qualified-controller admission at **fixed report kernel**. The second is kernel transport under the **fixed admitted controller**. If p and y_1 are common and K_0 can actually run on controller 1's target opportunities, the second bracket is bounded in absolute value by epsilon_1. Reverse the algebraic path and one obtains a different component attribution: neither decomposition is a unique natural indirect causal effect, and neither is justified by source validation alone. In particular K_0 may not even have target support when controller 1 enters previously unreachable recovery states. Then W_1(K_0) is not an approved/identified counterfactual and a four-arm policy contrast identifies at most the *complete policy change*, not its information/capability shares.

**Observable implication:** a frozen source-reporter hash and excellent source-domain error rate are insufficient. Need a separately versioned controller, a common pre-treatment customer-opportunity unit, target-grounded report labels, and a signed physically admissible cross-play or an honest unidentified-set statement. Actuation/learning must remain isolated from shadow report computation.

## Exact counterworld: calibrated source report becomes an expensive decision error

Reuse the previous **synthetic**, already qualified complete-service net contribution table for controller c=1 and equally likely high/low customer opportunity z. Retain F=(0,0), specialist S=(3/4,3/4), G=(3,-1), and source-trained target T=(4,-6). Every action here is hypothetically approved and its negative payoff denotes *economic* displacement, not an unsafe maneuver. With a symmetric high/low report correct at rate q, the first coordinate below refers to high-report action and the second to low-report action.

Source-domain testing reports q_source=9/10. The source-optimal report policy is (T,S) with expected production 15/8. Suppose controller-induced target exposure/report reliability instead is q_target=3/5. Executing the *unmodified* source report rule yields only 3/8, below the constant qualified G policy's contribution 1, even though the report itself is noninvasive. Reoptimization for the actual target kernel selects (G,S), yielding 43/40. The **stale-policy regret is 7/10**, while the correct optimized noninvasive report has a positive gain 3/40 over the no-report incumbent. These statements coexist without contradicting optional-information monotonicity: the planner *could* ignore the report, but the stale source-optimized response did not.

The earlier threshold q=5/6 reappears for a different substantive reason: it is the point at which the **source-optimized high-report target action** T first beats G for the admitted controller. For q in [3/5,9/10], the exact stale-report regret is max{0,5/2-3q}; a target kernel that crosses the boundary changes the economically optimal action even though the actual robot skill table is fixed. If controller 1's target kernel is only known to lie between q=3/5 and q=9/10, all sixteen deterministic report policies can be enumerated. (G,S) guarantees 43/40 across this interval; no policy, even randomized, can guarantee more because 43/40 is the fully informed optimum at the low endpoint. Thus the robust old-policy alternative beats blindly trusting an allegedly accurate source reporter. The result does **not** authorize a robot deployment or prove that a field kernel lies in this range.

There is a second distinction. Suppose the true target accuracy is *equally likely* to be q=3/5 or 9/10 and is independent of the pre-source high/low customer state. **Learning q before the customer report** (a different, noninvasive calibration experiment) has expected gross value

\[
\frac12 W_1(3/5)+\frac12 W_1(9/10)-W_1(3/4)
=59/40-11/8=\boxed{1/10}.
\]

The 7/10 loss from a **naively transported policy** in one world is *not* the economically available ex-ante value of buying calibration to a planner who already optimizes under the mixture. The latter is only 1/10 before the cost and opportunity loss of acquiring/validating the target labels. Cost above 1/10 defeats the calibrator under the explicitly stated prior, even though source-report error looks dramatic. An existing free independently validated calibration would erase that paid acquisition advantage.

## Implications for the source/grounding/embodiment choice

The economically relevant choices are: (i) acquire more source experience that changes the validated qualification/outcome kernel or diagnostic information; (ii) ground the *report* to choose better among **already** qualified full customer services, or separately ground the *controller* to qualify new target service; and (iii) acquire a changed body/production arrangement, with distinct manufactured supply, trained control and operator/market requirements. Optimize these as complete admissible policies with common original customer orders and resource/cost horizons in J. A free option to preserve an old policy weakly expands the gross menu, but costly forced training, unapproved action, policy-induced new occupancy and displacing the specialist can lower actual returns.

The general transport bounds give a **maximum possible benefit of policy recalibration** and the margin certificate can establish when reoptimization is unnecessary. Neither tells us whether *physical grounding* or a new embodiment is valuable; that requires target qualified recipe tests and measured complete production changes, not just confusion matrices. The report experiment is a distinct technology from teleoperation, autonomous field corrections, recovery trajectories, simulation, synthetic generation or public pretrained data. Each modality may influence both information and learning, but its provenance and intervention response must be separately measured. A production-generated stream may be cheaper than deliberate collection, yet it can be concentrated on easy, already successful states; acquisition changes who visits hard recoveries and can alter the target opportunity distribution.

## Falsification and closest prior art

Fail this result as a field decision certificate if any: the independently qualified action menu differs across report kernels; the source report cannot run in shadow on the target states; training alters joint customer orders or operator/dispatcher law and those changes are hidden; the report changes customer expectations or physical action directly; target ground truth is post-action rather than pre-source and selection-biased; original-order displacement is missing; or the policy's best action requires unapproved recovery support. In those circumstances report uncertainty is only part of a **whole-history** policy contrast and source-to-service partial identification remains open.

**Prior foundations, not asserted novelty:** Blackwell (1953), *Equivalent Comparisons of Experiments*, DOI https://doi.org/10.1214/aoms/1177729032, provides comparison of fixed experiments; standard total-variation expectation bounds, Bayes decision regret and value-of-perfect-information logic supply the inequalities. Perdomo, Zrnic, Mendler-Dünner and Hardt (2020), *Performative Prediction*, PMLR 119:7599–7609, https://proceedings.mlr.press/v119/perdomo20a.html, explicitly studies prediction-mediated distribution shifts; this chapter does **not** derive their equilibrium results. DDA https://arxiv.org/abs/2606.10127 section 5 already values future data and Appendix B treats complementarity. The potential research contribution is a *well-validated economic production/qualification interface and empirical discriminating architecture*, not generic Blackwell, off-policy or saturation mathematics. Prior-art audit and empirical originality remain incomplete.

**Next proof/evidence obligation:** certify or falsify same-opportunity target shadow report support and fixed-controller cross-kernel evaluation for a version-pinned, safely approved controller/dispatch/operator configuration. If unavailable, quantify the already admitted policy's worst-case safe original-order value under an explicit target-kernel identified set; do not translate source-domain signal accuracy, imitation success or generic robotics datasets into customer contribution. November 22 scientific review stays OPEN; December 25, 2026, 23:59 America/New_York unchanged.
