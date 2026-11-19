# Finite target-row evidence and economically valued qualified information

**19 November 2026.** Continuing the *same* When Capabilities Become Production source→qualification→accepted customer production argument, extending the [partial target report-support result](REPORT_SUPPORT_IDENTIFIED_VALUE.md). Conditional finite-statistical and robust-decision mathematics; no empirical customer/robot calibration, physical signoff or established scientific novelty.

## I. Economic and measurement environment

Fix a physically approved complete-network controller, dispatch/operator resources, existing qualified action menu A (retained specialist and old policy included), pre-action *original customer-opportunity* state z with share p_z, and whole-network contribution y(a,z) including accepted and displaced orders, demand/outside option, recovery, scarce resources and captured value. An inert, independently approved target shadow-report s ∈ {h,l} has conditional high-report probability q_z. An approved randomized rule π(a|s) produces

\[
V(\pi,q)=\sum_z p_z\sum_s K_q(s|z)\sum_a\pi(a|s)y(a,z),\qquad W(q)=\max_{\pi}V(\pi,q).
\]

This is already the operating value in V(Q;ω) and continuation J: do **not** add a second data premium. A benchmark score cannot be converted directly to provider dollars. The preceding exact-row result presumed knowledge of a population target conditional kernel; this chapter removes that presumption.

## II. Finite target rows and a sharp qualified-production lower value

Suppose an independently and prospectively sampled target shadow audit records n_z independent Bernoulli reports conditional on each **pre-action original** opportunity stratum z, with k_z high reports, a frozen kernel and fixed sample sizes. For m observed strata and predetermined overall error δ, define the clipped Hoeffding bands

\[
C_z=[\ell_z,u_z]=[\max(0,k_z/n_z-\epsilon_z),\min(1,k_z/n_z+\epsilon_z)],
\quad \epsilon_z=\sqrt{\log(2m/\delta)/(2n_z)}.
\]

A stratum with n_z=0 retains [0,1]. Hoeffding (1963) and the union bound imply simultaneous population row coverage at least 1−δ. Correlated original orders, report-dependent sampling, hidden opportunity denominators, changing controllers and unplanned optional stopping do **not** inherit this guarantee. Conditional on well-designed independent within-stratum observations, a random fixed row count may be conditionally legitimate; arbitrary cluster counts are not. A time-uniform confidence sequence, not this fixed-n interval, is needed for optional stopping.

For any stochastic report policy let y_π(s,z)=Σ_a π(a|s)y(a,z) and d_π(z)=y_π(h,z)−y_π(l,z). Under independently variable target-row intervals the **sharp** worst contribution is

\[
L_C(\pi)=\sum_z p_z\{y_\pi(l,z)+[\ell_z\,1_{d_\pi(z)\ge0}+u_z\,1_{d_\pi(z)<0}]d_\pi(z)\},\quad
G(C)=\max_{\pi\in\prod_s\Delta(A)}L_C(\pi).
\]

Each row selects its own minimizing endpoint. The general maximin must admit randomized policies; enumerating pure report rules alone is insufficient. If the qualified incumbent can ignore the report, G(C) cannot be worse than retaining that incumbent. On the simultaneous confidence event, G(C)≤W(q_true). This is a *lower confidence certificate* for optimized gross complete-customer production, not economic expected value of purchasing labels.

## III. Economically weighted uncertainty and its proof

Define the statewise span R_z=max_{a∈A}y(a,z)−min_{a∈A}y(a,z). On the confidence event,

\[
0\le W(q_\ast)-G(C)\le\sum_z p_z R_z (u_z-\ell_z).\tag{C3}
\]

**Proof:** For a fixed π, any two kernels in the product interval change state-z contribution by at most p_z |d_π(z)|width_z ≤ p_z R_z width_z. Let π* optimize under q*. Since G(C) ≥ min_{q∈C}V(π*,q), subtracting from W(q*)=V(π*,q*) yields the upper bound; q*∈C gives the lower. The result is an epistemic *certificate-width* upper bound, not a new physical learning scaling law. It can be conservative when report-conditioned action margins are narrow. Recentered confidence regions across different samples are not necessarily nested; one cannot assume every newly observed batch improves the reported worst-case guarantee.

In the unclipped regime, width_z≤2ε_z. A rare original customer opportunity with high potential displacement and capturable service span can thus be more important for economically defensible report transfer than a frequently observed but nearly irrelevant technical state. If R_z=0, report error on that state has zero immediate decision value for this frozen qualified menu even if model accuracy is poor.

## IV. A genuine new optimization dimension: where to sample if a safe audit already exists

Assume independently approved, rights-cleared fixed-architecture target shadows, known economic spans R_z and original state masses p_z. Set w_z=p_zR_z. Given N independent labels across positive-weight strata and the common concentration constant, minimizing the conservative width criterion Σ_z w_z/√n_z yields the interior continuous allocation

\[
n_z^\star=N\,\frac{w_z^{2/3}}{\sum_jw_j^{2/3}}. \tag{C4}
\]

With heterogeneous per-label costs d_z>0 and budget Σd_zn_z=B, the optimizer is

\[
n_z^\star=\frac{B\,(w_z/d_z)^{2/3}}{\sum_j w_j^{2/3}d_j^{1/3}}. \tag{C5}
\]

**Proof:** n↦w/√n is strictly convex for n>0; KKT gives w_z/(2n_z^{3/2})=λd_z, and budget normalization yields the expression. This minimizes a stated *upper bound*, not exact EVSI, a true stopping rule or actual long-run learning return. It ignores clipping, zero-support startup, label discreteness, state-specific confidence allocation and payoff-bound uncertainty. For hypothetical p=(0.1,0.9), R=(10,1), d=(1,1), the economically rare state receives 1/(1+0.9^{2/3})≈0.51755 of labels, not 10%. An improved source-trained controller, target-grounded embodiment or new body changes p, R, approved A and learning: C4–5 must not be transported unchanged to another physical policy.

## V. The prior qualified-service example now has a *finite-evidence* threshold

Re-use the exact conditional, **synthetic and not physically certified** whole-service table on equally likely original H/L opportunities: F=(0,0), competent specialist S=(3/4,3/4), G=(3,−1), T=(4,−6). For report-high →G, report-low →S,

\[
V(G/S;q_H,q_L)=\tfrac34+\tfrac98q_H-\tfrac78q_L.
\]

For intervals C_H and C_L its lower value is 3/4+(9/8)ℓ_H−(7/8)u_L; it beats constant G=1 only if 9ℓ_H−7u_L>2. This is a relative accepted-service margin, **not a pooled report accuracy** threshold. At exactly q=(3/5,2/5), the optimum is 43/40, compared with constant G=1. If an uninformative kernel q_H=q_L is admissible, no report-dependent policy robustly beats G: the report adds no information in that world. To certify the *full randomized* maximin for a rectangular interval, find an admissible corner (ℓ_H,u_L) at which G/S is the ordinary optimum over all action choices; because G/S is also worst at that corner, the policy and corner form a saddle. Alternatively an admissible kernel where constant G is the ordinary optimum certifies G's global robust optimality.

The companion executable tests illustrative precommitted, independent **hypothetical** reports with proportions 3/5 and 2/5 in each of two target strata. At total two-row family δ=0.05 and n=100 or 400 reports **per stratum**, the saddle certificate retains G=1. At n=1600 and 2000 per stratum, robust G/S yields approximately 1.00099 and 1.00880. The exact known-row economic optimum remains 43/40. These deliberately conservative calculations are *not* a robot-data sample size prescription, calibration, financial return or physical permission.

## VI. A negative identification theorem: selected-only reports do not fill a missing target row

Suppose original low-state orders are included in a report audit **only after a high report**, and the original order denominator is discarded. Conditional on any fixed number of selected records, the observed selected high-report labels all equal h when the original target low-state conditional q_L was 2/5 or 3/5. The two worlds are observationally equivalent in the accepted-only file, but their optimized whole-service values differ: 43/40 versus 1 (with q_H=3/5 and unchanged physically approved menu). More accepted-only labels do not identify the missing original-opportunity row. Recording the original denominator, independent inclusion probabilities and all shadow reports before action is an essential repair; known inclusion/selection mechanisms may support valid weighted inference, but acceptance itself does not.

## VII. Transfer to the full agenda, objections and prior foundations

Information about target customer opportunities is not qualification. Source field trajectories, failures/recoveries, teleoperation, simulation, synthetic inputs and public/pretrained datasets remain different channels; their technical transfer can change *joint qualification*, controller recovery, physical embodiment, accepted service, attention and customer demand. Report-only target grounding on a frozen policy can tighten a qualified production certificate; **physical** target grounding and a new body instead change the qualified production table and require independent safety/market evidence. Data and licensing/curation costs enter the existing dynamic J once; optional free data never force negative optimized value, unlike compulsory training or resource use.

Closest foundations: [Hoeffding (1963)](https://doi.org/10.1080/01621459.1963.10500830), [Blackwell (1953)](https://doi.org/10.1214/aoms/1177729032), [Howard et al. (2021)](https://doi.org/10.1214/20-AOS1991) for truly time-uniform confidence sequences, standard missing-data/partial-identification and robust decision theory. [Data-Driven Automation](https://arxiv.org/abs/2606.10127) already values future training data (§5) and complementary aggregation (Appendix B). None of these standard inequalities, KKT formulas, saddle arguments or examples independently establishes scientific novelty. The experimentally discriminating claim would require a *versioned and physically approved* target shadow reporter, unconditional original customer-opportunity registry, independent sample selection and genuine whole-network service value. None has been obtained. The November 22 scientific gate remains OPEN and December 25, 2026, 23:59 Eastern deadline unchanged.
