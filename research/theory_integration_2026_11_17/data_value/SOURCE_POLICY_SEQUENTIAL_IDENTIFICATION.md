# Identifying data-source policy value without recovering the entire Q × T × Y law

**20 November 2026. Same November 22 Models A–B gate in When Capabilities Become Production.** This is a constructive continuation of paired target-signal support, not a new research question. The previous chapter established sharp partial identification for the *mechanism-specific* value of target reports when source-created qualification Q, natural buyer regime T, and predecision report Y are incompletely paired. The earlier WHOLE_NETWORK_POLICY_IDENTIFICATION.md already proved whole-network randomized policy-value identification. This chapter extends that route to **sequentially assigned, physically permitted source, grounding and embodiment choices**, explaining why detailed three-way mechanism identification can be unnecessary for a supported implementable decision, yet indispensable for some extrapolations.

## 1. Separate an economic decision estimand from a transfer-mechanism estimand

For a fixed original buyer–robot–operator–controller-update network population and common horizon, let π be a *complete, legally and physically admitted adaptive policy*. It specifies source acquisitions, costs, rights, training and qualification, observation/report timing, embodiment and dispatch, fallback, shared operators, natural customer offers, unserved and refused orders, receipts *paid*, penalties and displaced service. Define J(π)=E[W^π], where W includes captured net original-cohort contribution over all policy-induced production and learning dates. Do not add another future-data premium: any future productive learning is already in the continuation history. Old R stays in the feasible menu when admissible. An optional freely available data source can be ignored; forced costly training need not improve J.

By contrast, the fixed-menu structural F/L mechanism in PAIRED_TARGET_SIGNAL_SUPPORT_AND_VALUE.md depends on z=P(Q11,T=A,Y=A) and has gross option premium 4dist(z,B) in its stipulated table. Pairwise Q×T and Q×Y evidence can leave z unidentified. That uncertainty matters when **transporting** the mechanism to a new body, new source or altered original customer cohort. It does not logically prevent evaluation of the captured outcome of one already supportable adaptive policy under a suitable randomized study.

## 2. Proposition: full original-cohort sequential policy identification

Let H_t be the recorded *before-action* entire-network history at decision t, including original prelisted buyer cohort, observable Q and Y when available, training source lineage, remaining budget, physical signoffs, embodiment compatibility, operator capacity and commercial offer version. Let A_t be a permitted whole-network action and p_t(a|H_t) its known randomized assignment probability. A deterministic policy π_t selects only a signed available action using this observed H_t; it cannot condition on inaccessible latent T.

**Proposition (standard sequential inverse-probability identity).** Suppose the pre-source network cohort is fixed; observed complete-network histories obey consistency and stable treatment versions; decisions are conditionally randomized given their full recorded history; all histories under π have strictly positive probability of their selected actions in the logger; no unmodeled interference crosses network-cluster boundaries; and W includes complete original-order, capacity, payment and resource costs, without differential postassignment exclusions. Then

\[
J(\pi)=\mathbb E_{\rm log}\left[W\prod_{t=0}^K
\frac{\mathbf 1\{A_t=\pi_t(H_t)\}}{p_t(A_t\mid H_t)}\right].
\tag{P}
\]

This identifies the mean of the specified **supported, admitted dynamic regime** without measuring latent T or the full Q×T×Y tensor. It does not identify the causal contribution of an individual training modality when the regimes bundle multiple interventions.

**Proof.** Conditional on H_K, sequential randomized assignment makes the expectation of the last weighted matching-action outcome equal to the conditional outcome under action π_K(H_K), by consistency and positivity. Apply the same substitution recursively at K−1 through zero. The iterated conditional expectations replace the logged action kernels by the regime's kernels, retaining policy-dependent future qualifications, demand, observations, dispatch and receipts. The initial cohort law is unchanged, so the result is E[W^π]. No independent qualification, fixed transfer matrix or stable buyer demand across arms is needed. This is established g-formula / IPW decision mathematics, not original causal inference theory. QED.

**Non-negotiable physical qualification.** The policy must be signed as safe for all states compatible with its preaction observations. Statistical support for an action cannot make an unsafe action legal. The old controller must be a certified **pre-attempt fallback**, not a magically available repair after an uncertified failure. If the physical state is not observation-closed, a learned target report or embodiment may be necessary before the policy enters the feasible action set. If source learning spills across experimental networks through shared controller updates, the assumed no-interference boundary is false.

**Whole-network versus sequential designs.** The 19 November WHOLE_NETWORK_POLICY_IDENTIFICATION.md covered prepolicy whole-regime randomization and intention-to-deploy. That remains a simpler way to identify one net policy contrast if enough isolated clusters exist. Sequential randomized assignments can reuse supported conditional paths and identify adaptive policies, but high-dimensional positivity and variance may make them unreliable. No policy-specific receipt data, signed controller or actual field randomization has been established.

## 3. Exact synthetic counterexample: qualification selection reverses economic ranking

Original buyer regimes A and B have equal pre-source frequency. A data-first specialist program X qualifies a complete service only for A; target-grounded G qualifies its own complete service for both. Source development is costly in either case: 1/4 normalized unit, paid whether qualification succeeds or not. A physically certified retained R yields gross 2 units. The gross *paid complete-service contribution* is 5 for qualified X on A and 4 for qualified G on either regime; all values are stipulated, not conversions of technical benchmark percentages. On Q=0, the experiment retains R **before attempting** the unqualified action.

Candidate π_s acquires source program s, deploys if Q=1 and otherwise keeps R. Comparing **successful qualifications only**, X appears better, 5>4. But over the fixed original cohort,

\[
J(\pi_X)=\frac{5+2}{2}-\frac14=\frac{13}{4}
\quad<\quad
J(\pi_G)=4-\frac14=\frac{15}{4}.
\]

Qualification under X selects A customers; it is not a pre-treatment random stratum. Comparing trained-successful X with all G can reverse the economically relevant original-policy ranking even when source S itself was randomized.

For a synthetic sequential logger assigning S=X/G with probability 1/2 at t=0, and then randomly deploying or retaining with probability 1/2 when Q=1 (retaining with probability 1 when Q=0), the matching path weights in (P) equal 4 on qualified-deploy paths and 2 on X-failed-qualification retained paths. The exactly executed source program and independent rational check both yield J_X=13/4 and J_G=15/4.

**Positive source exposure but missing deployment support.** If the logger never deploys qualified X, while logging X qualification, retained outcomes and the approved G policy, the qualified X paid outcome is never observed. Two possible complete-service response worlds, identical on every logged path and original offer, give qualified X gross 3 versus 7. The corresponding whole X policy values are 9/4 versus 17/4, on opposite sides of G=15/4. More routine old-policy experience without X deployment support cannot identify the missing contrast. These hypothetical X policies are assumed physically admitted *only for mathematical comparison*, not authorized in a real robot lab.

## 4. Identification and investment implications

First establish which whole policies are physically signed and original-market admissible. For those only, a pre-source policy-closed whole-network randomized design identifies total development-route contrasts; sequential assignment can identify particular adaptive routes when every action path is supported. In either case preserve **all original buyers and failures in the denominator**. Full source×qualified×report×demand pairing is still valuable to understand technical transfer, design source mixtures and predict out-of-sample adaptation, but not logically required for supported total regime means.

If full routes lack support or physical approval, use the earlier sharp bounds and the actual safe menu; do not impute exposed-policy payoffs from public demonstrations. X field trajectories, failure/recovery, teleoperation, simulation, synthetic and pretrained public inputs are separate intervention components with distinct marginal training and rights costs. Grounding can unlock reuse of already held X data or make an X policy observation-closed; E can expand qualified body actions and capacity. Both can change information *and* the feasible production menu. Optimize source and grounding investments jointly with embodiment lock, customer demand and actual future receipts in V/J, not via detached data prices or benchmark percent-to-dollar mappings.

An empirical study can choose (i) a valid complete adaptive-policy experiment that ranks implementable source-versus-grounding-versus-body strategies, (ii) separately a matched source-specific Q×T×Y measurement to learn mechanisms and transport, or (iii) an honestly partial identified-set comparison when neither is feasible. Do not require a mechanism tensor as a prerequisite for a directly identified regime contrast, and do not treat a direct contrast as proof of which modality caused it.

## 5. Foundations and status

Murphy, *Optimal Dynamic Treatment Regimes* (JRSS B, 25 April 2003), https://doi.org/10.1111/1467-9868.00389, directly precedes the sequential decision formulation. Hudgens and Halloran, *Toward Causal Inference With Interference* (JASA 2008), https://pmc.ncbi.nlm.nih.gov/articles/PMC2600548/, and Aronow and Samii, *Estimating Average Causal Effects Under General Interference* (Annals of Applied Statistics 2017), https://doi.org/10.1214/16-AOAS1005, precede the network design. DDA (Farboodi, Koh and Xia, 2026), https://arxiv.org/abs/2606.10127, already values production-generated future data and discusses aggregation complementarities. The conditional integration is not claimed as peer-reviewed novelty.

No original customer paid panel, signed whole-policy source/grounding/embodiment study, causal source-field intervention, official quantitative BEA/BLS production crosswalk, full repository CI or independent novelty review has been obtained. The Nov22 Models A/B scientific acceptance **remains open**, Nov29 empirical backbone pending, theory-majority through Dec6, Dec25 23:59 America/New_York deadline unchanged.
