# Endogenous report selection, recoverable support and the value of deliberate target audits

**19 November 2026; continuation of _When Capabilities Become Production_.** Conditional sampling/decision mathematics integrated with qualified whole-network customer production; not a robot field result, approved experiment or independently novel statistical theorem. This extends [finite conditional-row confidence](TARGET_ROW_CONFIDENCE_THEORY.md) without replacing its fixed independent target shadow-audit assumptions.

## The immediate scientific question

A productive robot's natural logs are **selected by its own controller, accepted jobs, customer allocation, operator intervention and recovery**. Can such selected records identify the economic contribution of a *target report* and when does a deliberate, separately approved nonactuating audit add information beyond already generated production data? A known original-order denominator is necessary for some designs, but not sufficient when the probability of recording a report itself depends on the unobserved report. This is a precise version of the broader data-transfer challenge, not an assumption that all production logs are low quality.

Let z index original **pre-action** customer-opportunity strata; the fixed, physically approved whole-network controller/embodiment has a qualified action menu A including existing fallback. The latent, frozen, pre-action nonactuating report S∈{h,l} has target kernel q_z=P(S=h|Z=z). For policy π(a|S), demand share p_z and complete, *capturable* original-order production contribution y(a,z), define V(π;p,q) and W(p,q)=max_π V as in the prior [target confidence theory](TARGET_ROW_CONFIDENCE_THEORY.md). These payoffs include accepted and lost service, retained qualified alternatives and scarce fleet, operator, recovery and customer opportunity resources. A classifier score is never assigned a dollar price.

Natural production generates a report **record** only when O=1, where O can depend on the latent S (through admission, action, support, logging permissions or job completion). We observe Z and O for every original-order opportunity in the correct frame and S for O=1. The report must still exist as a well-defined pre-action potential signal for all opportunities; if it only exists after actuation/admission, this frozen-signal estimand is not defined for rejected opportunities and the full physical policy, not a report-kernel bound, must be compared.

## Theorem 1: sharp observation-support interval without selection assumptions

Within stratum z write a_z=P(O=1,S=h|z), b_z=P(O=1,S=l|z), and m_z=1−a_z−b_z. **Knowing the full original-order denominator but not the recording mechanism identifies exactly**

\[
                 q_z\in [a_z,\;1-b_z].                    \tag{S1}
\]

For a finite frozen original-order panel of N_z, H_z selected-high records, L_z selected-low records, and M_z=N_z−H_z−L_z unrecorded reports, the *realized-panel* high-report fraction is sharply bounded by [H_z/N_z,(H_z+M_z)/N_z]. This is not automatically a confidence interval for a superpopulation kernel. Any missing reports can be assigned h or l to attain any lattice-valued panel fraction in the interval. For a superpopulation, any q∈[a,1−b] is attainable by allocating q−a mass of the unrecorded category to h and the rest to l; the observed three-category law remains the same.

Thus an accepted-only file with no selected low reports may have a fully known original denominator yet leave q anywhere from the selected high share to 1. A target audit with independent report sampling, or a known and validated selection mechanism, can reduce this ambiguity. The original-denominator-only repair proposed in the preceding chapter must **not** be overstated as identification under unknown report-dependent recording.

## Theorem 2: conditional recording propensities and positivity

Write ρ_h=P(O=1|S=h,z), ρ_l=P(O=1|S=l,z). They can reflect actual endogenous selection; independence of O and S is **not** assumed. Suppose independent validation justifies bounds 0≤α_s≤ρ_s≤β_s≤1, including the endpoint cases. Then the **sharp population identified set** is the collection of q∈[0,1] satisfying

\[
\alpha_h q\le a\le\beta_h q,\qquad
\alpha_l(1-q)\le b\le\beta_l(1-q).              \tag{S2}
\]

Each inequality is both necessary and, jointly, sufficient under these two conditional-propensity restrictions, by choosing ρ_h=a/q and ρ_l=b/(1−q) when denominators are positive, with the natural zero-mass conventions. For strictly positive bounds this can be written

\[
 \max\{a/\beta_h,\;1-b/\alpha_l,0\}
 \le q\le
 \min\{a/\alpha_h,\;1-b/\beta_l,1\}.             \tag{S3}
\]

Use S2 at zero propensity bounds, where division formulas are not defined. If the high-report recording rate is **known** and positive, then q=a/ρ_h even when no low-report records exist. If ρ_h is unknown, having N alone does not recover q. Recording propensities must be estimated or guaranteed by an actual signed architecture, not inferred from report accuracy or the count of accepted robot trajectories.

For genuinely randomized, known positive inclusion probabilities, inverse-probability weighting recovers the original-report rate using selected records. The unbiasedness of such weighting is standard survey-sampling mathematics (Horvitz–Thompson, 1952), **not a newly discovered transfer principle**. Independence for finite-sample concentration is an additional property: knowing marginal inclusion rates alone does not make correlated customer orders independent.

## Theorem 3: finite confidence under arbitrary report-dependent selection

Suppose N_z independently sampled, original pre-action opportunities within each fixed stratum, with a stable report and observation law. Observe H_z selected-high, L_z selected-low and the unselected count. For m fixed strata, a predetermined global confidence failure δ and ε_z=sqrt(log(4m/δ)/(2N_z)), Hoeffding plus a union bound applied to the two selected-category indicators implies simultaneous coverage (at least 1−δ):

\[
 q_z\in C_z^{sel}:=
 [\max(0,H_z/N_z-\epsilon_z),\;\min(1,1-L_z/N_z+\epsilon_z)] .   \tag{S4}
\]

The confidence set is conservative, and the population identified interval S1 is sharp only with *population* a,b. Do not conflate these. With validated propensity bounds, intersect S2 over a∈[max(0,H/N−ε),min(1,H/N+ε)] and b in its analogous interval, also imposing a+b≤1. The resulting outer confidence set may be narrowed by a proper joint multinomial region; no extra coverage is claimed. This is not optional-stopping valid or cluster-robust. If original opportunities are correlated or redefined by a changed controller, use appropriate clusters/horizon definitions or abstain.

A high volume of repeated successful trajectory records can shrink uncertainty about the **selected conditional law** while failing to reduce uncertainty about q at all. Conversely, selected production records can sometimes identify q without deliberately labeling the failures when their positive selection probabilities and original denominators are independently known.

## Counterexample: original denominators do not solve unknown admission selection

Retain the prior synthetic complete-service table, equally probable H/L original demand, F=(0,0), specialist S=(3/4,3/4), grounded G=(3,−1), changed embodiment T=(4,−6). The approved target report has q_H=3/5 from a genuinely independent hypothetical high-state audit. For the target L row, **both worlds generate exactly the same per-original-order observable distribution**: a selected h report occurs with probability 2/5; otherwise no report is recorded; no selected l report ever occurs. The original N and selected count distribution agree, not merely the conditional labels among selected cases.

* World A: q_L=2/5 and ρ_h=1, ρ_l=0. Complete qualified optimum W=43/40, achieved by G after h and retaining S after l.
* World B: q_L=3/5 and ρ_h=2/3, ρ_l=0. The report is uninformative (q_H=q_L); the complete qualified optimum is constant G=1.

Both have a=q_Lρ_h=2/5, b=0, and P(no record)=3/5. Their report-conditioned production investments differ even with a known N; **nothing about selected-only report accuracy distinguishes them**. Known ρ_h∈[2/3,1] identifies q_L∈[2/5,3/5]. The qualified robust comparison retains G at 1: in the World-B compatible kernel no report policy can exceed 1, and constant G always earns 1. If an independently supported ρ_h=1 is proven, q_L=2/5 and the synthetic optimal report rule yields 43/40. The 3/40 difference is not the expected value of buying a calibration study. It is a change in the identified optimized operating value; any study cost and opportunity loss belong in the same dynamic J.

This is an application of established missing-data partial identification; its merit here is that both observationally equivalent worlds are evaluated against a competent *whole-network* customer-service alternative, not only technical classification accuracy.

## Theorem 4: demand uncertainty compounds report-selection uncertainty

The previous row-width certificate presumed known customer demand p. For a frozen physically approved policy and bounded complete-service contribution y(a,z)∈[y_min,y_max], let a verified original-order panel imply p∈P, and report selection imply rectangular row set q∈C. Define

\[
G(P,C)=\max_\pi\min_{p\in P,\;q\in C}V(\pi;p,q).
\]

For true (p*,q*)∈P×C, define D_P=sup_{p,p'∈P}TV(p,p'), \bar p_z=sup_{p∈P}p_z and R_z=max_a y(a,z)−min_a y(a,z). Then

\[
0\le W(p*,q*)-G(P,C)
\le (y_{\max}-y_{\min})D_P+
       \sum_z\bar p_zR_z\,\mathrm{width}(C_z). \tag{S5}
\]

Proof: split V(π;p*,q*)−V(π;p',q') into a demand-composition change at fixed q* (bounded by the common complete-service span times total variation) and a report-law change at fixed p' (bounded by Σp'_z R_z|q*_z−q'_z|); apply the decomposition to π* optimal at truth and the worst feasible (p',q'). The old fixed-p certificate is recovered when P is a singleton. Product rectangles are conservative outer regions if p and q statistically coupled. If y or the approved action menu also changes with deployment, **S5 does not transport**—that is Model B's full-policy comparison, not a reason to insert invented y bounds.

## What this changes for production-generated versus deliberate data

There are **three distinct information upgrades**, not one undifferentiated label volume: (i) recording the unconditional original customer-order denominator, (ii) validating positive report-specific recording propensities, and (iii) obtaining an independently approved nonactuating *pre-action* report on randomly selected original opportunities. Which dominates depends on current a,b, support gaps, demand p, qualified y span, rights and cost. An independent audit can be extremely valuable at a rare high-displacement state even when the number of natural trajectories there is low. Conversely, production logs with complete original-order frames and known positive recording probabilities may already be sufficient; imposing a paid audit would waste resources.

These information changes are **not** physical target grounding. More source trajectories, teleoperation, failure/recovery, simulation and synthetic data can change the actual controller, joint qualification law, embodiment feasibility, demand allocation and original-order p. Those channels require matched technical interventions and whole-network outcome comparisons. Retaining old qualified controllers makes optional free data nonnegative in optimized value, but forced training, paid data, or audit interference can reduce net J. The controller's continuation data value is already inside J and cannot be added again.

A bounded, safety-approved prospective identification route is given in [the empirical protocol](TARGET_REPORT_SELECTION_EMPIRICAL.md). An exact synthetic diagnostic is in [source](target_report_selection.py) and [recorded output](target_report_selection_results.json). See the [proof ledger](TARGET_REPORT_SELECTION_PROOFS.md), [November 22 Models A/B bridge](NOV22_TARGET_REPORT_SELECTION_MODELS_AB.md) and separate [student exercises](TARGET_REPORT_SELECTION_EXERCISES.md)/[instructor solutions](TARGET_REPORT_SELECTION_SOLUTIONS.md).

## Closest prior art and limits

This theory specializes classic incomplete-data bounds (Manski, [2005 review](https://doi.org/10.1016/j.ijar.2004.10.006)), unequal-probability sampling (Horvitz & Thompson, [1952](https://doi.org/10.1080/01621459.1952.10483446)), concentration (Hoeffding, [1963](https://doi.org/10.1080/01621459.1963.10500830)), and optional-information decision theory (Blackwell, [1953](https://doi.org/10.1214/aoms/1177729032)). DDA [§5/Appendix B](https://arxiv.org/abs/2606.10127) already studies future production data and complementary aggregation. What remains to test is whether qualified robotics *production* generates an identifiable original-order sampling frame and target report observation process that changes the source/grounding/body investment choice. This package claims **no independent statistical novelty, measured robotic data value, physical authorization, numeric BLS–BEA crosswalk or passed Nov22 gate**. Final target: December 25, 2026, 23:59 America/New_York.
