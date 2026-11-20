# November 22 adversarial synthesis: optional incumbent policy is not a nested qualified outcome

**20 November 2026 UTC — conditional original-buyer/physical production theory; no measured robot or customer effect. The November 22 scientific gate remains OPEN.**

## The same question, with a necessary logical correction

Under what *implementable* physical and informational conditions does heterogeneous source data X, customer target grounding G or a newly approved embodiment E turn better technical qualifications into additional **paid, safe, complete customer production**? This continues the common optimized production value V(Q;omega) and two-date J, not a separate research project.

A critical distinction is missing from a loose reading of the previous [nested-qualification theorem](NOV22_MONOTONE_QUALIFICATION_THEORY.md):

1. **Policy-set inclusion:** acquiring freely usable, optional source data or retaining the old controller may leave the original complete policy R *selectable*. The maximum expected production value over the enlarged feasible policy set cannot fall, holding the entire environment, rights, payment system and opportunity set fixed.
2. **Outcome nesting:** a specific installed/admitted upgrade F satisfies Q_F(h) >= Q_R(h) on **each original eligible physical/network history** h. This is much stronger. Merely storing or legally retaining R does not create a clairvoyant dispatcher that knows when X fails.
3. **Whole-market option value:** the actual precommitted decision maximizes expected captured contribution net of resources, costs and later production/data value. It may improve without outcome nesting; conversely a new qualified job may be worthless if buyers will not order or a scarce operator displaces a more valuable job.

The prior bound max(0,d-N) <= Delta_paid <= min(d,M) remains mathematically correct **conditional on truly nested Q_F >= Q_R and stable B**. Policy-set inclusion, a positive randomized average gain or a baseline-safe RL *expected-return* guarantee do **not** establish its premise. This note corrects that potential physical interpretation without withdrawing the valid conditional theorem.

## Fixed original-market experiment and selector algebra

Let Z be a preaction, observed, fixed original-buyer/whole-network stratum. Let B be a legally supportable prospective purchase at a precommitted menu/quality, fixed across candidate controllers and recorded even for buyer refusals and zero sales. Q_R and Q_X are binary **complete-service** safe qualification under old R versus proposed source X using each policy's full operator/recovery rights, not isolated benchmark success. In a stable common network define

- b_z = Pr(B=1 | Z=z), h_Rz = Pr(B=1,Q_R=1 | Z=z), h_Xz = Pr(B=1,Q_X=1 | Z=z);
- g_z = Pr(B=1,Q_R=0,Q_X=1 | Z=z), l_z = Pr(B=1,Q_R=1,Q_X=0 | Z=z);
- p_z = Pr(Z=z) over **original eligible** cases, including declines and non-sales.

A legally feasible **preaction selector** invokes X with probability t_z independently of the latent (B,Q_R,Q_X), conditional on Z, otherwise invokes the *entire* incumbent R policy. It must be a physically permitted randomization on an original full network, with no between-arm spillovers; it is **not** an oracle that reads counterfactual success. For fixed captured complete-service margin v_z, incremental per-original-case switching/curation/operator cost c_z and one-off acquisition cost K:

    E[B Q_T | z] = (1-t_z) h_Rz + t_z h_Xz,
    Delta J(t) = sum_z p_z t_z {v_z(h_Xz-h_Rz)-c_z} - K.     (1)

Because h_X-h_R = g-l, (1) is estimable from appropriately randomized *whole-policy arm means* in the common original population without observing individual cross-world transitions. It does not require qualification nesting, but neither does it certify zero harm on formerly successful cases. An optimized menu, demand-changing quality, shared operator pool or second-period data generation requires the original full V/J rather than multiplying job rates by a universal v.

## Sharp regression ambiguity from correctly observed marginals

Only knowing b_z, h_Rz and h_Xz does not reveal *which* R-qualified buyers regress under X. Fréchet overlap yields the **sharp** interval

    max(0,h_Rz-h_Xz) <= l_z <= min(h_Rz,b_z-h_Xz),          (2)
    g_z = h_Xz-h_Rz+l_z.

Every endpoint is attained by an admissible joint distribution inside the original B=1 cell; no independence assumption is needed. For actual physical qualification regression among *all* eligible cases, including B=0, replace b with 1 and h_a with q_a = Pr(Q_a=1 | z). Demand-conditioned l is an economic lost-sale quantity, **not** a substitute for a physical safety certificate.

For an implemented selector to **preserve every originally safe qualification** rather than just expected paid production, it must satisfy

    t_z Pr(Q_R=1,Q_X=0 | Z=z) = 0 for every supported z.     (3)

With truly independent randomization of T conditional on Z and a common, noninterfering potential-outcome world, this is necessary and sufficient for Q_T>=Q_R almost surely. A casewise deterministic selective controller needs the analogous zero-selection-on-loss condition over every complete approved history. Equation (3) is not implied by E[Q_X] >= E[Q_R]. A formal zero loss under exact finite support is not a physical certification of unobserved recovery tails.

### A paired counterworld, not a parameter rerun

Four equally likely original eligible parent/network histories have B=1 and the exact same observed R and X arm marginals:

| History | R | X in nested world | X in crossed world |
|:--|:--:|:--:|:--:|
| A | 1 | 1 | 0 |
| B | 1 | 1 | 1 |
| C | 0 | 1 | 1 |
| D | 0 | 0 | 1 |

In both worlds Pr(Q_R)=1/2, Pr(Q_X)=3/4, the ex-ante X improvement is 1/4 and keeping R selectable creates the same maximal stand-alone expected qualification value 3/4. Yet X's qualification regression is **zero** in one world and **1/4** in the other. If one were somehow allowed to observe the latent outcome and serve with a noninterfering R-or-X oracle, the complete success rate would be 3/4 in the first world and 1 in the second. Neither oracle outcome is delivered by retaining an executable copy of R. The original monotone-bound premise holds in only the first world.

This is a **structural assumption failure**: no amount of more precise measurement of separate R and X averages distinguishes the two worlds. Joint qualification, a rigorously verified safe selector, or a direct whole-policy comparison is needed depending on the decision objective.

## An exact expected-regression-budget / economic-value frontier

Suppose an approved trial may tolerate a predeclared bound alpha on the **expected fraction** of previously qualified original cases lost to a selected controller; this is *not* a license to violate any hard per-case safety standard. Given q_Rz, q_Xz, the largest compatible physical loss probability from marginal arm data is

    rho_z = min(q_Rz,1-q_Xz).

If cross-world coupling remains unrestricted independently within each Z stratum, an outcome-blind selector t has sharp worst-case expected regression sum_z p_z t_z rho_z. Thus the *conditional statistical* feasible choice is the finite-dimensional program

    maximize_t  sum_z p_z t_z {v_z(h_Xz-h_Rz)-c_z}
    subject to sum_z p_z t_z rho_z <= alpha, 0 <= t_z <= 1.  (4)

K is then deducted once from the optimized difference if the intervention is acquired. With fixed stratum gains and costs, (4) is an ordinary fractional knapsack: select all positive-benefit zero-risk strata; among positive-risk strata prioritize net contribution per unit of worst-case regression, allowing a fractional final stratum. If the admissible safety condition is **casewise no-regression**, alpha=0 is inadequate as a field signoff unless each selected stratum has demonstrated or structurally guaranteed rho_z=0; any field uncertainty or unsafe loss event requires rejection. With shared controllers or nonrectangular original networks, summing independent stratum worst cases may not be sharp and (4) cannot be carried over unchanged.

Exact **synthetic**, demand B=1 everywhere: two equal-weight strata. A has q_R=1/2, q_X=3/4, v=8, incremental switch cost 1/2; B has q_R=1/4, q_X=1/2, v=4, incremental cost 0. Each fully switched stratum has worst-case regression contribution 1/8. A's full contribution is 3/4; B's is 1/2. At alpha=1/8, select all A for value 3/4; at alpha=1/16, select half of A for value 3/8. With no regression constraint select both for 5/4. The finite-grid exact executable validates these arithmetic statements; the general optimization conclusion follows from linearity, not enumeration. None of these are robotic customer dollar calibrations or regulatory risk thresholds.

## Safe fallback architecture is a physical claim, not a software toggle

A practical *certified* nested policy must guarantee at least one of the following with full recovery-tail and network accounting: (i) a preaction gate uses observed information proved sufficient to exclude every R-success/X-failure history it admits; (ii) an old certified complete-service path remains reachable after the upgraded action with enough guaranteed time/resources/rights, and retries do not corrupt the physical state; or (iii) a genuine noninterfering redundant embodiment/operator resource provides a qualified OR composition. Each can be expensive or infeasible. Saying "we can always roll back weights" does not prove state, body, operator, buyer SLA or recovery-tail preservation. If the fallback is only *globally* choose R versus X before a shift, it supplies policy-set inclusion and expected-value protection, not nested Q.

That distinction matters for X versus G versus E: target G may unlock new safe state observations but consume one scarce operator; embodiment E may permit a physically distinct redundant fallback only after joint-body qualification and customer acceptance; X may help an on-support subset while harming rare states. Heterogeneous teleop, field recovery, autonomous production logs, simulation, synthetic and public/pretrained sources must therefore be compared on **original-market state support and accepted complete-service changes**, resource usage, rights and actual legal deployability—not a scalar averaged source coefficient.

## Model A/B timing, countermodels and identification

**Model A:** With a fixed lawful buyer menu, no resource interference and valid same-population whole-network randomization, arm-specific (B,Q) marginals identify expected output *differences* even if individual technical regressions remain unidentified. To infer **safe addition** of newly qualified original orders from a marginal technical d with the preceding monotone bound, one needs a distinct *physically proven* Q_F>=Q_R plus stable original B. If capacity/opportunity substitution binds, compute the full optimized V and compare competent R, target-specialist/digital-coordination baselines and E.

**Model B:** Source data availability changes the controller menu, information policy, selected production trajectories and future observations. The right ex-ante dynamic comparison is J with policy/state-contingent complete histories; a noninvasive report may improve dispatch decisions without changing physical Q, while trained admission changes Q and report calibration. Keep full revenue, future learning, costs, rights and demand transitions **inside** J. No second data premium. A retained R strategy protects optimized gross J only if the acquisition leaves its entire state/action/resource/customer law intact and acquisition is optional/free. Forced costly training or market interference defeats that implication.

**Direct-policy alternative:** Where physical nesting, lawful original-buyer commitment or same-world individual-switch bounds cannot be certified, physically approve and randomize *complete learner/operator/customer clusters* among R/X/G/E policies, recording original eligible order zeros, accepted whole-service production and actual payments over a common window. A properly identified arm mean compares policies even without interpreting counterfactual regressions. It may not establish casewise safety, and invalid cross-pool SUTVA/exposure breaks its economics. If even cluster-level support and permission fail, retain an honest unidentified ranking.

## Closest prior work / falsifiers / next evidence

Manski (1997, [Monotone Treatment Response](https://ideas.repec.org/a/ecm/emetrp/v65y1997i6p1311-1334.html)) is the foundation for invoking monotone potential outcomes, *not* for assuming them from optional policy sets. Manski ([Statistical Treatment Rules](https://www.nber.org/papers/t0242), 1999 / Econometrica 2004) already studies policy selection from conditional arm evidence. Laroche, Trichelair and Tachet des Combes ([Safe Policy Improvement with Baseline Bootstrapping](https://proceedings.mlr.press/v97/laroche19a.html), 2019) address baseline-safe expected-return improvement; this is not a robot-wide casewise safety/qualification guarantee. Farboodi, Koh and Xia ([Data-Driven Automation](https://arxiv.org/abs/2606.10127), 2026, §5 and Appendix B) already endogenize productive data and data-source complementarity. LP resource prices, support/Fréchet envelopes and fractional knapsack are established. **No scientific novelty is claimed for these constructions.**

Falsifiers: any R-qualifying complete physical/network history where selected F fails contradicts claimed nesting; any changed original buyer/quality/menu/capture law contradicts fixed B/v; any network learning/operator or dispatch spillover contradicts isolated stratum implementation. The next constructive question is whether actual candidate robots have a signed *whole-history* physical dispatch fallback that converts policy-set inclusion into nesting. If not, prove only an original-order policy-level value comparison, with approved randomized complete-network evidence and competent R/G/E comparators. The November 22 gate, independent novelty, field original-order panel, actual transfer effect and numerical BEA–BLS crosswalk remain open; Christmas deadline remains December 25, 2026, 23:59 Eastern.
