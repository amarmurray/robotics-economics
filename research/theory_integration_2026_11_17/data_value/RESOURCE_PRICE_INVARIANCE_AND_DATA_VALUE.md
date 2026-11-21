# When a shared operator constraint does — and does not — identify economic data value

**21 November 2026 | The same November 22 *When Capabilities Become Production* Models A/B, conditional theory; not measured robot returns.**

The preceding [coupled-resource result](COUPLED_RESOURCE_REPORT_VALUE_AND_ECONOMIC_SUPPORT.md) showed that a report-invariant accepted-paid outside service opportunity restricts missing action margins across target reports, yielding a positive lower certificate for the economic value of finer predecision information. The unresolved question is **what production-system evidence justifies that invariance**. Shared hardware alone does not. Here we link production LP basis stability, original-buyer paid outside-order conditions, and a *sharp relaxation* allowing report-conditioned opportunity. This is constructive sensitivity analysis of the existing argument, not another unrelated learning curve or a claim of a new general theorem.

## 1. Production opportunity and dual price are different objects

For one fixed trained learner, approved controller and original customer/operator network, let Y be a *predecision* report with probabilities p. A and B are entire physically approved customer-plus-outside-order dispatch policies; m_A(y),m_B(y) include all attempted, accepted, refunded and actually paid original-order service and all lost outside contribution **once**. Fine versus coarse information value is the previously derived Blackwell/production gap

\[
L=\sum_{z}\min\{\sum_{y\in z}p_y[\delta_y]_+,\ \sum_{y\in z}p_y[-\delta_y]_+\},\quad \delta_y=m_A(y)-m_B(y).
\tag{1}
\]

No value of source training, new source episodes or embodiment manufacturing is added to this fixed-learner L: those change the complete dynamic program J and need matched total-policy evaluation. R remains optional; any uniformly dominant approved E collapses full-menu report value to zero, even when A/B L is positive.

The **outside-order displacement contribution** λ_y is the accepted paid service actually attainable in state y with the particular signed free slot and time horizon, conditional on the offered order, eligibility, rights and customer acceptance. An LP's **capacity shadow price** π_y is a local derivative/supergradient of its optimum with respect to an extra unit of resource. Equality λ_y=π_y requires more than shared machinery: a comparable signed outside order must be the *actual marginal alternative*, and the full-unit slot displacement must remain in the same optimal regime. An LP dual is a certificate or local bound, not a paid receipt or necessarily the value of a whole unit.

Consider the production LP in standard form with fixed technology A, input RHS b(y), contribution vector c(y), and basis matrix B with basic objective coefficients c_B(y). When the same basis remains primal and dual feasible, the optimal production value is

\[
v_y=c_B(y)^\top B^{-1}b(y),\quad\pi_y^\top=c_B(y)^\top B^{-1}.
\tag{2}
\]

Thus fixed c and B imply the *local* capacity price stays fixed under feasible RHS shifts, but output and original orders may change. If c(y) varies, π_y may vary **with exactly the same optimal basis**. If an RHS change crosses an optimal-basis region, π_y may jump even under fixed c. A full one-slot change need not lie inside the sensitivity region. Conversely an economically stable paid outside contract can furnish common λ across y even if other LP dual multipliers vary; establish the order opportunity directly.

**Two explicit countermodels.** (i) Maximize c_y x subject to 0≤x≤1, with c_y∈{1/4,1/2}. The unique optimal x=1 and same binding-capacity basis persist, but the marginal capacity price equals c_y and changes. (ii) Maximize x+(7/10)z subject to x+z≤1, x≤d_y, x,z≥0. For d=1/5 the optimal (x,z)=(1/5,4/5), captured contribution 19/25 and slot price 7/10; for d=6/5 the optimum is (1,0), value 1 and slot price 1. The physical slot and objective are unchanged; buyer demand shifts the optimal basis and resource price. These are standard parametric LP facts, not evidence about a real robotics deployment.

## 2. Sharp approximately invariant outside contribution

Return **unchanged** to the three original-buyer report states p=(1/2,1/4,1/4), single coarse Z and the *same exact* physically signed synthetic A/B service contributions and slot uses in the previous chapter. Permit an outside service contribution λ_i for report y_i, in [0,1/2]. Then

\[
\delta=(1/2-\lambda_1,\,-1/4-\lambda_2,\,\lambda_3).
\tag{3}
\]

All three original price/acceptance/safety restrictions from the earlier construction remain assumptions; report probabilities, core buyer contributions and joint menu are unchanged. The positive and negative margin masses are

\[
P=1/4-\lambda_1/2+\lambda_3/4,\quad N=1/16+\lambda_2/4,\quad L=\min(P,N).
\tag{4}
\]

The original common-λ chapter sets λ_1=λ_2=λ_3. Rather than assume exact invariance, impose a transparent sensitivity envelope

\[
0\le\lambda_i\le1/2,\quad \exists\lambda\in[0,1/2]: |\lambda_i-\lambda|\le\epsilon\quad(i=1,2,3).
\tag{5}
\]

For scalar λ_i this is equivalent to max_i λ_i−min_i λ_i≤2ε. It is a **structural identified set**, not a sampling confidence interval, technical accuracy tolerance or observed source transfer.

**Proposition (sharp approximate-invariance report-value interval).** For every ε≥0, over precisely (3)–(5),

\[
\boxed{\;\underline L(\epsilon)=\min\{1/16,\,[1/8-\epsilon/2]_+\},\qquad
\overline L(\epsilon)=\min\{3/16,\ 5/32+\epsilon/2\}.\;}
\tag{6}
\]

Every endpoint is attained by an admissible original-network response law. For ε=0 this recovers exactly [1/16,5/32]; at ε≥1/4 it recovers the unconstrained rectangular [0,3/16]. For ε<1/4 the hypothesized bounded cross-report opportunity spread *still guarantees positive fine-report value* despite neither report y1 nor y3 being individually strictly A-favorable in every admissible world. The lower bound remains 1/16 until ε=1/8; it then falls linearly to zero at ε=1/4. The upper bound reaches 3/16 as early as ε=1/16. This exposes asymmetric fragility: uncertainty initially expands the possible upside without destroying the lower certificate.

**Proof (no numerical inference).** δ1≥0, δ2≤0 and δ3≥0 on the entire box, establishing (4). The minimum of min(P,N) over a feasible set equals min(min P,min N). From λ2≥0, min N=1/16, attained at λ1=λ2=λ3=0. The pairwise spread bound implies λ3≥max(0,λ1−2ε), and P decreases in λ1 and increases in λ3; its minimum is [1/8−ε/2]_+, attained at λ1=1/2, λ2=λ3=max(0,1/2−2ε) (for ε≥1/4 the latter are zero). This proves and attains the lower endpoint.

For the upper endpoint, N≤3/16. In addition, 2L≤P+N=5/16+(\lambda_2+\lambda_3-2\lambda_1)/4≤5/16+\epsilon, because λ2−λ1, λ3−λ1≤2ε. Hence L≤5/32+ε/2. When 0≤ε≤1/16 choose λ1=3/8 and λ2=λ3=3/8+2ε, making P=N=5/32+ε/2. When ε≥1/16 choose λ1=3/8, λ2=λ3=1/2, making P=N=3/16. These choices respect (5) and attain the upper endpoint. QED.

This is elementary finite decision and partial-identification optimization with a transparent robustness parameter, **not an empirically validated robot theorem or a scientific novelty claim**. The [exact integer executable](resource_price_sensitivity.js), its [record](resource_price_sensitivity_results.json) and an independently executed Python Fraction grid enumerate 22,185 admissible synthetic laws across nine ε grids and corroborate the closed-form endpoints; the proof above establishes the result for *all real ε*, not just the grid.

## 3. What this sensitivity bound does and does not license

**Informational decision.** If a G-observe report costs c and leaves learning weights, demand, contracts, controller and physically permitted actions fixed, robust within-program net benefit requires c<\underline L(ε); robust non-benefit requires c>\overline L(ε). For the earlier stipulated c=1/8, no feasible ε yields strict robust benefit because \underline L≤1/16, although some worlds cover cost; the earlier precise common-λ cost criterion is recovered at ε=0 with λ known. If c=1/32, robust positive net follows when ε<3/16; equality requires a tie convention. These are *dimensionless synthetic conditional values*, not a deployment price quote. Learning the true λ from an audit is a separate earlier experiment with its own cost, sampling, and induced actions.

**Principal failure modes.** (a) The source/target Y might change buyer offers, outside-job arrivals or service acceptance, not just reveal them; (5) may then be unsupported. (b) A report-conditioned physical-safety or qualified-policy menu changes available actions, breaking (1)'s common A/B action support. (c) Changing rights, time horizons, data provenance or labor recovery costs can change c and the entire full-unit outside opportunity. (d) A common shadow price in an abstract sector LP does not establish a signed real outside customer or a full-unit counterfactual receipt. (e) If source data or G-train changes Y's distribution or qualification, comparison must use dynamic total-policy J, not add this L as a data dividend. (f) If the unchanged synthetic E remains uniformly dominant, full-menu value remains zero for all ε, regardless of the A/B sub-menu interval.

**Empirical discriminant rather than more toy calibration.** The decisive external requirement is a predecision original-offer cohort with Y, outside-buyer offer/eligibility/availability, shared robot/operator slot, complete legal controller signature, conditional accepted-paid outside order and report-conditioned original buyer payoffs. An estimated **bound on the cross-report range** of attainable paid outside orders (after accounting for refusals/refunds and potential unobserved counterfactuals) can select ε. If even an upper bound ε<1/4 cannot be defended, the positive certificate is unearned; use the broader rectangular or coupled multiaction policy set. When natural report changes also move c(y), p_y or feasible recipes, use an explicit larger structural identified set or a supported randomized whole-network policy comparison rather than (6).

## 4. The larger research program still binds

This strengthens a *single bridge* in the original production-value theory: source data, field failures/recoveries, simulation, teleoperation, public pretrained and synthetic inputs can change what is jointly qualified; target G-observe can change information at fixed qualifications, G-train/reweighting changes the learner; E opens hardware/manufacturing/operator recipe columns; original buyer demand and competing capacity determine which qualification matters. Optional old policies and free data availability weakly expand feasible value; costly or forced training can impair a fixed recipe. The network model's buyer/operator/robot link is an empirical atlas edge, not a BEA aggregate input-output coefficient.

**Source/version boundary and prior foundations.** Fixed-basis shadow-price sensitivity is standard LP duality, see [CMU Operations Research notes](https://www.math.cmu.edu/users/math/af1p/Teaching/OR/Notes/OR_notes.pdf), accessed 21 November 2026; Blackwell experiment comparison and polyhedral partial identification are already acknowledged in the parent chapter. [BEA's official I-O guide](https://www.bea.gov/resources/guide-interactive-industry-input-output-accounts-tables) distinguishes sector use and requirements tables from individual customer/service links, accessed 21 November 2026. No numerical official sector cell was retrieved in this tranche; it would be incorrect to impute one from the source pages. DDA §5 already values production-generated data and its Appendix B already discusses complementarities; we do not claim those established mechanisms as novel.

**Exact remaining proof/evidence gap:** Is an empirically defensible joint bound on report-conditioned *attainable outside paid service* compatible with signed whole-network A/B policies and the original buyer's menu/qualification, or are those objects report-endogenous? If it is not, abandon the stronger positive lower certificate rather than substitute a shadow price. Next compare X-existing versus X-new episodes, G-observe versus G-train, and E as **distinct whole-learner, joint-qualification, paid original-customer network policies**. November 22 Model A/B scientific acceptance remains OPEN, theory-majority through December 6, final target December 25 2026 23:59 America/New_York.
