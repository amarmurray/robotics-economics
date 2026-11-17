# From capability profiles to economically qualified expansion

17 November 2026. Assistant-led continuation. Input research commit `0bde43c00cceda1fcb258c51468955c94d4834e8`; publication is additive to the assistant branch. The original Christmas milestones remain. Status: analytical model and synthetic examples, not measured deployment returns, an empirical qualification rule, or a selected novel paper contribution.

## 1. Question and contribution to the research program

The preceding expansion model assumed that useful experience lowered a single qualification bill. This note replaces that scalar assumption with a conditional cost-minimization problem: a configuration has several service-relevant weaknesses, those weaknesses differ in how expensive they are to correct, and the customer requires a fixed complete-service criterion. Adaptation effort is chosen, not assigned as a free learning dividend.

The resulting cost feeds back into the existing customer-demand and investment model. This joins capability composition, adaptation, customer value and alternative uses of cash. It does not estimate the technology of learning from published scores. Endogenous acquisition of the initial capability profile, qualification duration and multi-period uncertainty remain next extensions.

## 2. Explicit service and technology assumptions

Define failure events E_r on the same whole-service trial and deployment distribution. Let their true or justified upper-bound marginal probabilities after adaptation x_r be

    f_r(x_r) = l_r + a_r exp(-alpha_r x_r),
    a_r = f_r(0)-l_r >= 0, x_r >= 0.

Here l_r is an irreducible floor for this configured hardware/software/process, alpha_r>0 is an assumed response parameter, and w_r>0 is the marginal resource cost of adaptation. These are synthetic primitives, not fitted scaling laws. The exponential is chosen for a tractable benchmark; published data-scaling results do not establish it.

Use the conservative rule sum_r f_r(x_r) <= epsilon. By the union bound this is sufficient for whole-service success probability >=1-epsilon without assuming independent component failures. It is not necessary; correlated or overlapping failures can make the bound loose. Step-conditional success rates and arbitrary benchmark scores are not the unconditional probabilities used here. Unknown probabilities cannot be treated as verified bounds.

The adaptation program minimizes sum_r w_r x_r subject to this rule. Add a separately stipulated verification/setup cost V>=0. This model computes a cost conditional on a known technology; it does not itself establish statistical confidence, safety approval or regulatory certification. Fixed V is not a claim that industrial validation is universally constant.

## 3. Solution and derivation

Set eta=epsilon-sum(l_r), k_r=w_r/alpha_r, and delta_r=a_r exp(-alpha_r x_r). Excluding zero-amplitude components, the equivalent convex problem is

    minimize sum_r k_r log(a_r/delta_r)
    subject to 0<delta_r<=a_r, sum_r delta_r<=eta.

If initial failures already satisfy the rule, no adaptation is required but V remains. If eta<=0 and positive amplitudes must be reduced, no finite adaptation satisfies this conservative rule. That is a limitation of the specified configuration and criterion, not a universal physical-impossibility result.

Otherwise the optimum is

    delta_r* = min(a_r, k_r/lambda),
    sum_r delta_r* = eta,
    x_r* = log(a_r/delta_r*)/alpha_r.

Proof: the objective is strictly convex in each positive delta, with second derivative k_r/delta_r^2>0. The linear feasible set admits a strictly positive point when eta>0. Cost diverges at a zero delta, so the optimum is attained away from zero. KKT stationarity gives -k_r/delta_r+lambda+nu_r=0; complementarity at delta_r=a_r yields the stated minimum. The sum is continuous, strictly decreasing around its binding positive root, so the relevant multiplier is unique. Zero-amplitude components use no effort. The implementation brackets the root and bisects from the feasible side; the proof, not the numerical routine, establishes global optimality under these assumptions.

Interpretation: expensive-to-improve components optimally receive more of the failure allowance unless separate service constraints forbid it. Imposing equal component budgets can overstate the least cost of meeting the whole-service rule. Conversely, allowing failure-budget substitution is inappropriate when a customer requires a distinct threshold on each component; that alternative is implemented as a comparator.

Away from active-set changes, dC/depsilon=-lambda. If source experience e_s changes reducible amplitudes as a_r(e)=a_r0 exp(-tau_rs e_s), with nonnegative tau and fixed floors/costs, the envelope derivative is

    dC/de_s = -lambda * sum_r tau_rs delta_r*.

For components receiving adaptation, lambda delta_r*=k_r. Improving an untrained component can still free failure allowance for an expensive component. Learning's value depends on the required service and cost vector, not raw data volume or average performance. Free componentwise improvements cannot increase optimized cost because they weakly expand the feasible set. Optional retention of an earlier configuration preserves that dominance when a new candidate has adverse transfer; costly acquisition and changed obligations must be counted separately.

## 4. A checked ranking reversal

All values are synthetic normalized inputs. There are two components, with alpha=(1,1), w=(1,8), floors zero, epsilon=.02 and V=2.

| Initial profile | Initial failure probabilities | Mean component success | Adaptation cost | Total qualification cost |
|---|---|---:|---:|---:|
| Score-rich | (.002,.12) | .939 | 8 log(20/3) = 15.176960 | 17.176960 |
| Bottleneck-rich | (.08,.05) | .935 | log(36)+8 log(45/16) = 11.856109 | 13.856109 |

The higher average-performing profile is more expensive to qualify. Its remaining weakness is in the component that is expensive to improve. This is a counterexample to ranking transferable experience by a mean score, not evidence that these profiles occur in a real robot or that the functional form is correct.

For score-rich, the inexpensive component already uses only .002 failure allowance, leaving .018 for the expensive one. For bottleneck-rich, the optimizer selects (1/450,8/450). Both meet the same conservative whole-service rule. Equal separate .01 budgets produce costs 19.879253 and 14.954945, respectively, preserving the ranking but raising both costs.

## 5. Joined investment comparison

`bridge.py` feeds these costs into the unchanged `takeover_2026_11_17/expansion.py` kernel. It reuses the source-service cash calculations (8 versus 6), customer demand, outside options, unit costs, retained initial fleet and terminal accounting. No published benchmark calibrates the inputs. Initial deployable cash is 30; total qualification costs are rounded UP to .01 cash units, 17.18 and 13.86, with no rounding hidden inside a feasibility threshold.

| Source path | Optimal new A/B units | Value added including current source cash |
|---|---|---:|
| Score-rich/current-cash-rich | 0 / 6 | 28.82 |
| Bottleneck-rich | 1 / 5 | 31.94 |

The lower current-cash path wins because its qualification advantage changes the portfolio it can fund. The correct comparison includes existing-fleet expansion, not only the new configuration's standalone return. Under weaker destination demand, identical source profiles, scarce initial cash of 4, or verification cost V=20, the current-cash-rich source wins. These are selected ablations of a complete small-instance enumeration, not a real-world return forecast.

The inherited tariff is a two-part resource reimbursement plus surplus-sharing fee, not fixed hourly RaaS and not an equilibrium bargaining solution. The earlier hourly-receipts model remains a separate contract comparison. This bridge does not yet solve hourly pricing, time-to-build or uncertain qualification. It must not be presented as having done so.

## 6. Improvement and evidence are separate investments

Even a technically good policy may require costly evidence. As an elementary illustration, freeze a policy and run a prespecified number n of independent, identical, held-out Bernoulli trials. With no failures, the one-sided exact lower success bound at confidence 1-alpha is alpha^(1/n): at a proposed true success p, the probability of observing all successes is p^n. Therefore

    n >= ceil(log(alpha)/log(p_required)).

At alpha=.05 this gives 29, 59, 299 and 2995 trials for requirements .90, .95, .99 and .999. These are mathematical illustrations, not robotics standards, industrial acceptance recommendations or evidence about any current system. Correlated trials, site heterogeneity, repeated testing until success, model selection on the holdout and post-test updates invalidate the simple interpretation. A more capable policy may be more likely to pass the fixed test without lowering its planned trial count. The normalized V in the investment example is not estimated from these numbers.

## 7. Empirical anchor and limits

The paired source observations and hypothetical task-to-market mappings are in `evidence_atlas.json`.

Open X-Embodiment Table I reports RT-1 versus RT-1-X results of 40/27, 30/27 and 92/73 percent across its three large-data evaluation columns. Table II contrasts 75.8 percent emergent-skill performance with 42.8 when Bridge is removed; other design changes are recorded there. These support configuration-specific transfer hypotheses, not a universal positive-transfer coefficient or measured qualification savings. PDF pages 5 and 6 were visually inspected. [S1]

Lin et al.'s version 2 distinguishes normalized step scores from success criteria. Table 1 reports both; Appendix D specifies the task boundaries. Its pouring evaluation caps the bottle, so it is not a liquid-delivery test. The paper's four tasks are laboratory/proxy service evidence, not observed customer revenue or staffing changes. The v2 HTML, Sections 3/5 and Appendices D/E/G, was read; the PDF exceeded the web fetch size limit and is not claimed visually inspected. [S2]

Thus the evidence identifies useful variables and contrasts, not alpha, w, failure floors or customer willingness to pay. The next empirical test must compare matched configurations at one service standard, varying source experience while recording adaptation effort, failed attempts, validation, retained work and payment dates. A score improvement alone supplies none of those cost coefficients.

## 8. Verification, open objections and next work

Seventeen new scoped tests pass, alongside a fresh rerun of the preceding 18 expansion tests. New tests include closed forms, KKT/primal reconstruction, an independent two-component allocation grid, marginal-cost finite differences, monotonicity, validation sample sizes, conservative cost quantization and joined portfolio ablations. No full historical CI, independent review or field validation is claimed.

This is standard convex allocation applied to a deployment question; novelty is unestablished. The important remaining assumptions are known exponential response, separable effort, fixed failure-event meaning, conservative risk aggregation, fixed verification cost, no elapsed adaptation time, no endogenous source-learning choice and an inherited deterministic market. The first paper should not assert a universal ranking or call this a statistical certification model.

Next constructive question: when does a modified embodiment lower an irreducible failure floor or change adaptation productivity enough to justify its development time and capital cost? Compare that with more learning on the existing embodiment and with demand that may expire before qualification. In parallel, build an actual sector backbone and a small matched-workflow contrast rather than extending the same toy indefinitely.

## Replication

From this directory, with its preserved sibling module:

    python qualification.py
    python bridge.py
    python -m unittest -v test_qualification

## Sources

S1: Open X-Embodiment Collaboration, *Open X-Embodiment: Robotic Learning Datasets and RT-X Models*, arXiv:2310.08864, PDF retrieved 17 November 2026; inspected PDF pages 5-6, Tables I-II and Figure 4. https://arxiv.org/pdf/2310.08864 . The unversioned endpoint is identified by retrieval and local hash when available; no unverified version number assigned.

S2: Lin et al., *Data Scaling Laws in Imitation Learning for Robotic Manipulation*, arXiv:2410.18647v2, 12 February 2025. https://arxiv.org/html/2410.18647v2 . The response curves in this note are assumptions, not fitted laws from that paper.
