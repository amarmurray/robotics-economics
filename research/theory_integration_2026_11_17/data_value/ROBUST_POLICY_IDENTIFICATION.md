# When Capabilities Become Production
## Robust economic policy certificates under partially identified transfer and joint customer acceptance

**Private conditional theory continuation, 18 November 2026 UTC.** This is the next step of the existing source → qualified-policy → safe production → accepted customer service argument, not a new model family. It takes the finite latent-regime, pathwise-budget model in PARTIAL_OBSERVATION_PATHWISE_THEORY.md as the starting point. Neither theorems from robust control/partial identification nor the synthetic examples below are represented as scientific novelty or hardware certification.

### 1. Decision object: a feasible history-dependent policy, not an isolated skill rate

Let \(\Theta\) be a nonempty identified set of possible **complete** controlled joint laws for transfer regime, visited states, gate detection/misses, retained controller update, realized recovery/operator resource cost, all jointly accepted customer qualifications, and observation reports. Conditional acceptance and current production are mapped through the same previously defined optimized production value \(f(Q;\omega)\), with qualified specialist alternatives, customer calendar, rights, and old policies retained. Each \(\theta\) fixes a *whole* joint history law, including how repeated observations are coupled through a persistent regime; it is not a new adversarial regime draw after each decision.

For nonanticipating policy \(\pi\), let
\[
J(\pi,\theta)=\mathbb E_\theta^\pi\left[
\sum_{t=0}^{T-1}\beta^t m_t(x_t,a_t)
+\beta^T f(Q_T;\omega_T)
\right] - \text{nonduplicated acquisition/curation costs}.
\tag{R1}
\]
Costs already included in \(m_t\) or the resource feasibility set are **not** subtracted twice. The terminal economic envelope may itself include incumbent retained production. A data episode earns no extra independent dollar premium. The policy uses reports and observed budgets but cannot condition on an unobserved \(\theta\).

Call a policy **uniformly pathwise feasible** if for every \(\theta\in\Theta\), every positive-probability history it induces has authorized physical transitions, budgets nonnegative on each path, and a feasible retained-policy/specialist/abandonment fallback for every observed successor. This is stronger than expectation- or percentile-based capacity. When the positive-support union is not established, the following are mathematical conditional certificates only, not authorization to deploy.

For a policy class \(\Pi\) of uniformly feasible full policies define
\[
d(\pi,\rho)=\inf_{\theta\in\Theta}[J(\pi,\theta)-J(\rho,\theta)],\quad
L_\pi=\inf_\theta J(\pi,\theta),\quad U_\pi=\sup_\theta J(\pi,\theta).
\tag{R2}
\]
**Proposition R1 (robust pairwise production certificate).** A feasible \(\pi^\star\) is uniformly economically optimal against *every* policy in the specified class if and only if \(d(\pi^\star,\rho)\ge0\) for every \(\rho\in\Pi\). The conservative \(L_{\pi^\star}\ge\max_{\rho\ne\pi^\star}U_\rho\) is sufficient but not necessary, because it discards cross-policy coupling induced by the same environments, customer demand and acceptance shocks. Where the identified set consists of convex combinations of finitely many **complete potential-history laws**, fixed-policy expectations and their differences are affine in those mixture weights; it suffices to evaluate extreme points or solve a finite linear program. This vertex conclusion is *not valid* merely because interval-valued transition probabilities define a polytope: their repeated-use trajectory probabilities can be nonlinear. Proof: the first equivalence is the definition of uniform optimality; \(J_\pi-J_\rho\ge L_\pi-U_\rho\). Affinity and vertex attainment follow from expectation linearity in a mixture over fixed full-history worlds. Each assertion presupposes the same feasible policy class across worlds, not a world-specific menu chosen after learning hidden \(\theta\).

There are three distinct choices. **Uniform dominance** compares policies in every admitted world; **maximin** chooses \(\arg\max_\pi L_\pi\) and may select a policy that loses to a comparator in some worlds; **minimax regret** minimizes \(\sup_\theta[\max_{\rho\in\Pi}J(\rho,\theta)-J(\pi,\theta)]\), where the benchmark knows the world. These are not interchangeable and no prior customer/operator risk criterion has selected one by fiat. Robust feasibility is imposed before any of the three economic comparisons.

### 2. A sharp decision-relevant relation not recoverable from skill marginals

Retain the prior chapter's \(\Delta=8\) full B-and-C customer bundle, qualified incumbent flow of 1 under routine R, redesigned embodiment E with no interim incumbent flow, and competent specialist S with total value 6. Define \(q_R=P(B=C=1\mid R)\) and \(q_E=P(B=C=1\mid E)\), conditional on held-out, end-to-end accepted-service protocols. Existing component marginals \(p_B=p_C=3/4\) for R and \(9/10\) for E imply
\[
q_R\in[1/2,3/4],\quad q_E\in[4/5,9/10],
\quad J_R=1+8q_R,\quad J_E=8q_E,\quad J_S=6.
\tag{R3}
\]
Without cross-policy measurements, both R>E and E>R are possible. In particular the envelopes \([5,7]\) and \([6.4,7.2]\) overlap, so no uniform ranking follows.

Now suppose a matched joint-acceptance comparison, with justified transport to the same sites, order windows, and feasible resources, identifies the additional **one-sided causal constraint**
\[
q_E-q_R\le d,\qquad d=1/10. \tag{R4}
\]
The resulting identified set is nonempty: \(q_R=7/10,q_E=4/5\) and \(q_R=3/4,q_E=17/20\) both respect the original marginals and (R4). Every endpoint joint law is realized by cells \(P(11)=q,\ P(10)=p_B-q,\ P(01)=p_C-q,\ P(00)=1-p_B-p_C+q\).

**Proposition R2 (coupled acceptance certificate).** For this restricted feasible menu and identified set, \(\inf_\theta(J_R-J_E)=1-8d=1/5>0\), and \(\inf_\theta(J_R-J_S)=1+8(7/10)-6=3/5>0\). Thus R is uniformly preferable to E and S, *although separate optimized-value intervals still overlap*: under (R4), \(J_R\in[6.6,7]\) and \(J_E\in[6.4,6.8]\). More generally the break-even bound is \(d\le1/\Delta\) for a unit of preserved incumbent production, with strict ranking when \(d<1/\Delta\). Proof: subtract the same-world payoffs \(J_R-J_E=1-8(q_E-q_R)\). Bound by (R4); equality is attainable at \(q_R=7/10,q_E=4/5\). The bound against S uses \(q_R\ge7/10\), forced by \(q_E\ge4/5\) and (R4), and is attainable. The limit \(1/\Delta\) is a demand- and contract-conditioned opportunity threshold, *not* a technical demonstration price.

**Important restriction:** This certifies only the declared R/E/S policy menu. It does **not** certify against a feasible adaptive diagnostic, a new hardware route, or unmeasured alternative demand block. (R4) is proposed identifying information, not observed robotics evidence; matching needs a credible crossover/parallel potential-outcomes design and a correct total-service denominator. If merely cross-sectional measurements confound site, safety staffing or service demands with route choice, imposing (R4) is invalid. A paired design can sometimes identify a *difference* more tightly than either absolute probability, and the same physical shock may couple both routes; it cannot assume one robot actually executes incompatible counterfactuals simultaneously.

**Why this is not adding a new arbitrary interaction coefficient:** \(q_E-q_R\) is a difference of joint held-out acceptance probabilities under matched interventions, not a free data-value term. The economic multiplier 8 is the stated marginal contribution of an accepted complete service in \(f\); without an accepted order, \(\Delta=0\) and these differences have no increment. Alternative demand windows or mixed substitute/complement recipes require recomputing \(f\), not keeping \(\Delta\) as a universal market price.

### 3. Safe, partially identified diagnostics: actual information and foregone production

A diagnostic has operational and informational consequences. The following **separate, controlled special case** isolates when the latter pays under a common calendar. There are two fixed target-alignment worlds \(H\in\{X,Y\}\) and two feasible terminal full customer-service recipes X and Y. Each earns 8 units of optimized qualified service contribution when matched to H, 2 when mismatched; a fully qualified specialist terminal alternative earns 4. All terminal actions use at most one operator resource on every supported H path. The total approved operator budget is 2.1. Both incumbent productive first action P and diagnostic first action D preserve old safe fallback. P generates 1 unit of currently accepted incumbent work, uses no operator resource, and reports no information; D generates no current service, uses 1 operator resource, and reports binary y with symmetric regime sensitivity \(\alpha=P(y=H\mid H)\). Both have exactly one terminal slot. No terminal qualification score is converted into a monetary estimate; 8 and 2 are explicitly synthetic outcomes of the same accepted-service production objective under different validated recipe sets.

If P is chosen, robustly optimizing the terminal randomized choice between X and Y gives mixing probability 1/2 and a **maximin** value of \(1+(8+2)/2=6\) in each world; choosing the specialist gives only 5. If D is chosen, following its report with the corresponding target recipe gives
\[
J_D(H;\alpha,c)=8\alpha+2(1-\alpha)-c=2+6\alpha-c,\quad H=X,Y,
\tag{R5}
\]
where \(c\ge0\) is a real additional incremental acquisition/curation cost (the lost first-unit P production is already excluded from D's payoff). The report accuracies are only known to lie in \([\underline\alpha,\overline\alpha]\subseteq[1/2,1]\) for **each world**, not known to equal a point estimate. Since symmetric wrong reports produce the same payoff in each H, the conservative D maximin value is \(2+6\underline\alpha-c\) (never below the option of selecting the competent specialist instead, but the latter cannot improve the threshold at \(c\) small). The D report-following policy dominates the *specified 50/50 productive policy in every possible world* if and only if
\[
\underline\alpha\ \ge\ (4+c)/6. \tag{R6}
\]
Strict inequality yields strict dominance. At \(c=1/10\), the threshold is \(41/60\approx0.6833\). A raw unvalidated interval \([0.6,0.8]\) cannot support D over the productive maximin benchmark: its lower-bound payoff is \(11/2=5.5\). If safe matched evidence justifies \(\underline\alpha=0.7\), the D lower bound becomes \(61/10=6.1\), exceeding 6. At \(\alpha=0.8\), realized D expected payoff would be 6.7 net of \(c\), but an estimated 0.8 is *not* itself a reliable lower confidence bound.

Proof: the productive terminal mixing probability z yields worst-world value \(1+\min(2+6z,8-6z)\), maximized at z=1/2; a specialist offers 1+4. A diagnostic-following policy has \(8\alpha+2(1-\alpha)-c\) in either H. Operator use after D is at most 1+1=2<2.1 on every path; after P at most 1. Compare to 6 to obtain (R6). The stronger signal alone does not guarantee a better complete route because D displaces accepted P production and incurs real c. **Do not call this a uniform ranking of D against each deterministic productive X/Y choice**: one such policy earns 9 in its favored world; D may instead be maximin-optimal or dominate the *specified* productive randomized rule.

**Safety countermodel.** Replace terminal wrong-world operator demand by 2 while keeping matched demand 1 and D first-stage use 1. For any \(\overline\alpha<1\), report-following D has a supported path using 3>2.1. Thus (R6) is no longer an admissible decision certificate; the safe diagnostic policy must choose a resource-feasible fallback (e.g. S) or obtain approved reserve capacity. A positive-probability missed regime in a finite calibration sample cannot be treated as impossible. This is the previous chapter's operator-budget objection applied to the robust diagnostic, not a new external safety approval.

### 4. Information design and the minimal discriminating measurements

The relevant uncertainty is not just the sign of individual transfer. There are two *different* missing measurements:
- **Joint accepted-service relation:** a pre-specified matched comparison can estimate \(q_E-q_R\), with an upper confidence bound below \(1/\Delta\). To certify the R/E ranking, the bound must cover the actual held-out service window and rights/cost/price assumptions.
- **Regime-report and recovery relation:** independently challenge the diagnostic by defensible regime proxies, recording false reports in **both** directions, and establish supported peak resource use with actual safe fallback. To rank D against productive P in the example, a credible *lower* bound on accuracy for each regime must exceed (R6), **and** all branches must be physically approved. One may reduce uncertainty by validating report performance without running the diagnostic in commercial service, but validation itself uses time/resources and does not automatically substitute for an operational rollout.

For orientation only, with \(n=400\) independent, ground-truth-labelled validation trials *per H* and 320 correct per H, Hoeffding plus a two-group union bound at simultaneous confidence at least 95% gives each \(\alpha_H\ge 0.8-\sqrt{\log(4/0.05)/(2\cdot400)}\approx0.726\), in this simplified stationary Bernoulli model. This exceeds \(41/60\). It establishes neither structural support zeros nor pathwise safety, and cannot be used if true H labels, independence, stationarity, or data rights are missing. The sample is **hypothetical**, not an executed experiment or measured robot diagnostic.

**Value of a test is a decision property.** For a proposed safe experiment e, construct report-dependent policies \(\pi_e(y)\) using its *joint* observation/physical/outcome law, then compare \(\inf_\theta J(\pi_e,\theta)\) to the best feasible no-test policy under the same horizon. Do not add a test-information premium to that value; the test's data value is already inside its induced future actions and qualified customer output. A free optional signal that does not change feasible actions can be ignored and cannot reduce the optimized value. A costly/forced diagnostic can have negative net value, while a physically productive routine policy can generate useful free observations.

### 5. Partial identification, robust dynamic programming and prior-art boundary

One must choose uncertainty semantics **before** solving. The same persistent, fixed transfer regime and correlated qualification kernel usually recur across visits; nature cannot silently redraw them independently after each report. Our uniform-comparison rule evaluates complete consistent \(\theta\in\Theta\) from the start. Replacing this by independent worst-case kernels at every history creates a larger rectangular adversary and can make an informative probe appear worthless even when it identifies a physically persistent regime. A dynamic-programming recursion over a rectangular ambiguity set is not automatically an exact algorithm for nonrectangular persistent-world maximin or minimax regret. The counterexample is immediate: if a diagnostic perfectly reveals fixed H and terminal X/Y is rewarded for matching it, the informational route earns 8 before costs; if nature can switch H *after* the report, that guarantee disappears. This is an assumption change, not a negative-technical-transfer observation.

Closest prior art (bounded audit, abstracts/identified sections checked 18 November 2026): Manski, **Statistical Treatment Rules for Heterogeneous Populations**, *Econometrica* 72 (2004), https://doi.org/10.1111/j.1468-0262.2004.00530.x, already develops minimax-regret statistical decisions; Nakao, Jiang and Shen, **Distributionally Robust Partially Observable Markov Decision Process with Moment-Based Ambiguity**, *SIAM Journal on Optimization* 31 (2021), https://doi.org/10.1137/19M1268410, already studies DR-POMDPs; Bovy, Suilen, Junges and Jansen, **Imprecise Probabilities Meet Partial Observability**, IJCAI 2024, https://ijcai.org/proceedings/2024/740, compares static and dynamic uncertainty semantics; Li and Shapiro, **Rectangularity and Duality of Distributionally Robust Markov Decision Processes**, arXiv:2308.11139 (2023), https://arxiv.org/abs/2308.11139, addresses the rectangularity distinction. Existing Fréchet, Blackwell, DAgger, ThriftyDAgger and *Data-Driven Automation* foundations remain inherited. These sources provide neighboring concepts, not evidence that the present robotics-economic synthesis is novel. Complete literature replication, field experiments and peer review have **not** occurred.

### 6. Reconnection to the full production agenda

Robust feasible policy ranking is a statement about a *customer-specific qualified production opportunity*, not global value of a dataset. The existing resource-price certificates and complementary-recipe graph determine \(f\); learning/data/embodiment interventions change the joint distribution over qualified recipes; controller changes endogenously change visited support; safety/crew and calendars restrict feasible routes; customer demand and competitor prices determine whether a qualified bundle actually matters; ownership and rights determine who can use observations and capture the margin. A manufacturing redesign may reduce operator recovery on every path without providing additional informational precision. Simulation, public/pretrained inputs, teleoperated corrections, routine field episodes and recovery labels are **separate candidate causal routes** and require different validation, not a common quantity of demonstrations.

This extension supplies a *conditional robust screening layer* to the earlier finite-budget model. It neither replaces the full network/atlas, multiplies task scores by assumed dollars, nor proves vertical integration superior to competent contracting/specialist supply. The next step is **November 22-level synthesis**, comparing this screening layer to Models A and B in their actual notation and finding an empirical design where either robustness certificate could fail. The precise unresolved technical proof/identification gap is a tractable nonrectangular **adaptive** robust policy comparison when report-conditioned joint qualification, operator recovery tails and customer demand evolve together: full potential-history laws may be too large, and testing their structure against real approved sites remains unperformed.

**Not completed:** actual conditional transfer or joint-service dataset, safe recovery support audit, quantitative official sector production backbone, independently reviewed contribution, full historical CI, or scientifically accepted Nov22 synthesis. The original December 25 23:59 Eastern final target is unchanged.
