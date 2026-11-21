# Economically sufficient reports: source data, target grounding and qualified production

**21 November 2026 UTC; sustained continuation of *When Capabilities Become Production*.** The open question is unchanged: which heterogeneous data or target-grounding intervention changes the best *physically signed original-customer production policy*, versus merely improving a prediction score? This note strengthens [qualification-weighted dispatch](QUALIFICATION_WEIGHTED_DISPATCH_AND_SOURCE_VALUE.md) and [the qualification gate](QUALIFICATION_GATE_AND_DATA_VALUE.md), not a detached investment model. The existing X (source), G (target), E (embodiment) and R (retained) program, original buyer and complete operator/controller boundary remain the target.

## 1. The economic experiment, not prediction accuracy, is the primitive

For a **fixed** admitted learner, embodiment, original buyer cohort, capacity state h and permitted whole-network recipes Π(h), let Y be a predecision source/target report and U(d,ω) the **complete** captured original-buyer contribution if signed action d is chosen. U includes joint physical qualification, acceptance, refunds, paid receipts, operator/robot scarcity, retained R feasibility and any discounted learning continuation **once**. An observed held-out task label θ need not determine U. For every report y and signed action d define the *economic conditional response*
```
m_d(y,h) = E[U(d,ω) | Y=y, H=h, fixed learner and original cohort].
```
At a fixed resource state, the economically sufficient vector is (m_d) over the *permitted complete actions*. It is not the signal's classification accuracy or an intrinsic dollar price of its source trajectories. For a closed network with scarce shared operators, d is a **joint** policy/assignment over customers and robots, not a per-robot action; otherwise optimizing each row separately double-counts capacity. LP resource-price certificates apply on certified active faces, not as universal fixed prices.

The one-source experiment Y and its report compression Z=φ(Y) must describe the **same** controller, physical action menu, production outcome kernel and customer environment. This restriction matters: new source training, new embodiment, reweighting, different buyer offers, or a probing action that consumes time are *different treatments*, not free garblings of a common experiment. Predecision target observation (G-observe) is distinct from training/finetuning (G-train). Even if G-observe only measures state, it may require rights, qualified sensing and cost.

## 2. Proposition: exactly when discarded report detail has economic value

Suppose finite Y, finite **common** signed action set D, integrable U_d, and a fixed realized context h. The optimized gross values from full Y and coarse Z are respectively

`V_Y = E_Y[max_{d in D} m_d(Y)]`

`V_Z = E_Z[max_{d in D} E[m_d(Y)|Z]]`.

Then `V_Y >= V_Z` and the **exact gross report-compression loss** is

`L(φ) = E_Z{ E[max_d m_d(Y)|Z] - max_d E[m_d(Y)|Z] } >= 0.`

Equality holds **iff**, for every positive-probability coarse cell z, at least one permitted action maximizes m_d(y) for almost every fine report y in that cell. In particular, a change in predictive accuracy with no change in optimal signed decisions has no operational information value for the fixed program.

**Proof.** A policy using Z can always be implemented as a Y policy by discarding extra details, proving the inequality. On a cell, choose an action maximizing the conditional mean. The expected nonnegative gap to `max_d m_d(y)` is zero iff that action is pointwise maximizing almost surely; finite D ensures a maximizer and this is also necessary. Summing cells proves the identity and equality criterion. This is elementary conditional Jensen/Blackwell decision theory, **not** a new information theorem. It requires a *common implementable action menu*: data that forces requalification or revokes a signed legacy recipe destroys the nesting premise.

**Two signed actions.** For D={A,B}, set Δ(y)=m_A(y)-m_B(y). The exact loss is
`L(φ) = (1/2) E_Z[E(|Δ(Y)| | Z)-|E(Δ(Y)|Z)|].`
This makes the empirical object concrete: **sign reversals of conditional paid-service advantage**, weighted by their size, not classifier mistakes. General networks use the max-vector formula, because third/fallback actions and shared capacity invalidate a two-action shortcut.

**Nonfree context.** A sensor, target inspection or curation investment costing c is preferred *within the unchanged qualified policy* only when L>c, after charging resource/time displacement and changes in acceptance. A training intervention changes U, Y or Π and must be evaluated as a separate full program, not by subtracting its cost from the same Blackwell gap.

## 3. Exact connection to the existing X/G/E/R three-source construction

Keep every assumption and normalization in [QUALIFICATION_WEIGHTED_DISPATCH_AND_SOURCE_VALUE.md](QUALIFICATION_WEIGHTED_DISPATCH_AND_SOURCE_VALUE.md). X yields the full three-bit report S; M=majority(S) is a deliberately compressed one-bit report. Both operate the **same** stipulated signed A/B/R controller, with original-customer qualified-paid matching yields r_A=1/4 and r_B=3/4, symmetric original regime and known conditional source-error law indexed by t∈[0,1/16]. This is *within an already selected X*, not a new data-generation experiment.

The earlier full-report optimal qualified-service probability is
```
q_full(t) = 55/128-t/2,  0<=t<=1/64;
            13/32+t,    1/64<=t<=1/16.
```
Because majority report accuracy p(t)=13/16+2t is at least 13/16, a controller that sees **only M** optimally chooses the majority specialist despite unequal r_A/r_B: the posterior likelihood ratio exceeds the 3:1 paid-success ratio. It therefore achieves
`q_M(t)=(r_A+r_B)p(t)/2 = 13/32+t.`
The exact value of retaining the fine source vector rather than majority-compressing it is
```
q_full(t)-q_M(t)=max{3/128-(3/2)t,0}.
```
The inequality is strict only when t<1/64, where full Y detects a split report whose high-yield B action is better although B is the *minority* prediction. At t=0 the source-program complete-service contribution improvement from preserving the fine report is `10*(3/128)=15/64` normalized units. At t>=1/64 it is **zero**, although full vectors still contain additional raw bits. The cost of X and R fallback are the same on both sides; no continuation premium is added. Enumerating all 256 deterministic full-report binary dispatches and all four majority-conditioned dispatches at 17 exact t points independently reproduces this identity; numerical checks are corroboration, not proof.

The E embodiment in this **same, unchanged synthetic portfolio** has net 10; X can reach at most 103/16 and G=49/8. Therefore no learning of t, or this within-X report refinement, changes the optimal *initial X/G/E/R investment*: E dominates by at least `10-103/16=57/16` if those stipulated net values and physical availability are maintained. The 15/64 is **within-X operational** value; adding it on top of the already full-report X value, or calling it a portfolio gain, would double-count. Nor does E's hypothetical value establish a real robot investment ranking. If E is not physically feasible, faces shared capacity not in this toy table, or its true paid-service yield is uncertain, obtain an entirely new original-buyer policy table before changing the ranking.

## 4. Grounding may have value with *no* improved target-label accuracy

A second deliberately separate finite counterexample isolates an economically relevant physical/operator state Z unrelated to the target *task label* θ. Let θ and Z be independent fair bits; the original buyer is held fixed. Two independently signed complete-service choices A and B yield 8 captured units if matched to Z and 2 through an actually feasible R fallback otherwise. Without observing Z, choosing either yields 5. Observing Z **before** choosing yields 8, a gross improvement of 3 or net 2 after a hypothetical one-unit observational/inspection cost. The best prediction of θ remains 1/2 both before and after observing Z. Thus an observation can be commercially valuable through *joint physical qualification/operational state*, even when it carries exactly zero label information.

These 2/8 values are neither real prices nor transportable to the X/G/E/R t example. The example assumes licensed A/B, a genuinely recoverable R and predecision observation. An unapproved inspection or unavailable R invalidates the claim. This is a negative result for the claim that measuring task-label accuracy is an economically sufficient data objective.

## 5. Source/grounding/embodiment are different treatments and evidence needs

**Fixed source archive or source-origin experiment:** episode family, modality, rights, eligibility, admitted transitions, shared-weight update regime and independent failure/recovery coverage may change the law of qualified service. Field data, teleoperation, scripted/simulation, synthetic and pretrained public sources need distinct provenance and costs. Mere report refinement is a narrower exercise than adding source experience.

**Target grounding:** discriminate (i) an extra predecision observation of target, operator or customer state using the same learner and signed action set; (ii) trained grounding or alignment that changes controller, qualification, report kernel and possibly action permissions; (iii) customer demand measurement that changes posterior original order probabilities but not qualified physical control. Only (i) has the nested report theorem automatically, subject to genuinely free or correctly costed observation. The report vector should be the expected *qualified paid outcome for each signed action* conditional on the original state, not a generic accuracy vector.

**Embodiment:** E can add an admissible production column, remove operator requirements or supply universal recovery; signed safety, manufacturing/fleet availability and cost belong in the production optimization. It cannot be represented as “more report bits.” A source-generated embodiment option can be compared by the previously established dynamic state-contingent J, with its option and future data value counted once.

**Decision-level experiment:** estimate complete signed R/X/G/E original-cohort potential policy outcomes by whole controller/operator/customer cluster assignment and intact eligibility denominators; if an action or report cell is unsafe/unsigned, retain identified bounds instead of inventing positivity. For within-learner report compression, register fine and coarse predecision shadows, report-specific *potential* paid outcomes for every **supported** permissible action, accepted/refunded receipts, customer natural offers, qualification and recovery. Conditional supervised label accuracy is a negative-control outcome, not cash. Observing only the chosen action cannot identify every m_d(y) without assignment support or defensible structural restrictions. A signed experimental team would control safety; this research does not authorize a field experiment.

**What to test next.** Seek a technically feasible predecision grounding signal whose *conditional action advantage* changes sign, then test it under the same qualified customer-production recipe with causal support. Compare source-archive interventions and changed embodiments as complete separate policies, not as automatically Blackwell-ordered reports. The immediate scientific gap is identification of the report-conditioned **action-specific accepted-paid response vector** at a physically closed original-buyer/controller/operator boundary; the currently available public datasets have no such cohort. This gives a discriminating reason to collect a missing report/qualification/customer edge before another transfer-matrix sweep.

## 6. Closest prior art and what has not been established

Blackwell's comparison of experiments and conditional Jensen arguments are the foundational information result. Goel and DeGroot, *Comparison of Experiments and Information Measures* (Annals of Statistics, 1979), DOI https://doi.org/10.1214/aos/1176344790; the 2024 general-state-space Blackwell proof (Economics Letters, DOI https://doi.org/10.1016/j.econlet.2024.112146). Elmachtoub and Grigas, *Smart “Predict, then Optimize”* (Management Science 68(1), 2022), DOI https://doi.org/10.1287/mnsc.2020.3922, already distinguish prediction loss and downstream decision loss. Van Rooyen, *Beyond Blackwell: Constrained Data Processing Inequalities* (arXiv:2611.00510, posted October 2026) explicitly treats constrained admissible decision rules, so **neither the constrained information principle nor our elementary formula is claimed novel**. Farboodi, Koh and Xia, *Data-Driven Automation* (arXiv:2606.10127, June 2026), §5 and Appendix B already treat future data value and aggregation complementarities. These public-source locators were checked 20–21 November 2026. We have not reviewed all full texts or established a distinct scientific contribution.

This is conditional economic production accounting plus elementary Bayesian decision theory, a sharp reanalysis of an existing **synthetic** report experiment, and a separate synthetic counterexample. No raw robot source episodes, real controller training, signed hardware policies, original buyer receipts, source-to-qualification field effects, validated calibration, quantitative BEA/BLS input-output cell, complete repository CI or independent peer review. **November 22 scientific Model A/B acceptance remains open.** Theory majority through 6 December; final target 25 December 2026, 23:59 America/New_York.
