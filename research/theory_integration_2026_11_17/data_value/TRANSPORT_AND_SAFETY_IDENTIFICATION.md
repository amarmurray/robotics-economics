# When Capabilities Become Production
## Transporting a matched production certificate across customers, sites, and recovery regimes

**Conditional continuation, 18 November 2026. Private research draft; not externally published.** This chapter continues the exact question left by [ROBUST_POLICY_IDENTIFICATION.md](ROBUST_POLICY_IDENTIFICATION.md): when does a paired, same-world qualification difference actually license a production/grounding/embodiment decision in the customer population that will buy the service? It challenges the previous hypothetical constraint, rather than inventing a fresh transfer coefficient or a detached small model. The existing Model A/B and operator-budget results remain in force where their assumptions hold.

### 1. The estimand is a target customer's feasible production difference

Let \(z=(s,w,o,d)\) designate a pre-action site, window, accepted-order definition, and observable demand/customer state. The target collection of commercially feasible orders gives weights \(\mu_z\ge0\), \(\sum_z\mu_z=1\). This is a *specified policy target population*, not the distribution of logged robot trajectories. The enrolled validation distribution is \(\nu_z\). These can differ even if both label their records "industrial manipulation." Production eligibility, data rights, site configuration, staffing, contract capture and calendar must be the same definitions under both policies or explicitly included in \(z\).

Retain complete and **held-out** customer acceptance of complementary tasks \(B,C\). For route \(j\in\{R,E\}\), \(q_j(z)=P(B=C=1\mid do(j),z)\) is the *joint* probability of a customer-accepted bundle, including adaptation, validation and qualified delivery within the window. It is not a marginal model score. For now route \(R\) is routine production with optional learning byproduct and retention of an incumbent qualification; \(E\) is a target embodiment change that displaces that incumbent unit. Grounding, specialist and safe diagnostic remain feasible comparators for the full eventual decision; this chapter's first inequality only compares \(R,E\).

Define \(b_z\) as the captured value of current *accepted incumbent service* preserved by R relative to E; \(k_z\) as additional net real resource/acquisition/curation cost of R relative to E, excluding amounts already netted in \(b_z\); and \(\Delta_z\ge0\) as the additional contribution of an available, jointly accepted bundle **computed from the same optimized customer production envelope** \(f(Q;\omega_z)\). When the only route-sensitive terminal event is full B/C acceptance and its incremental contribution is \(\Delta_z\) independent of route, expected policy difference is
\[
D_\mu:=J_\mu(R)-J_\mu(E)
=\sum_z\mu_z\{b_z-k_z-\Delta_z d_z\},\qquad
d_z:=q_E(z)-q_R(z). \tag{T1}
\]
This identity requires a fixed target population, same customer value/capture conditional on a qualified bundle, no cross-unit pooled-controller spillovers, and no route-specific demand changes left unconditioned. Retained specialist/old policies are inside the value envelope; continuation revenue is not added again as a "data premium." If learning across sites or route selection changes the target order population, (T1) is **not** a valid universal evaluation shortcut; use the original state-dependent \(J(\pi,\theta)\).

**General nonbinary statement.** If customer value is a nonlinear \(f(Q;\omega)\) over *several* jointly qualified recipes, use \(\sum_z\mu_z E[f(Q_R;\omega_z)-f(Q_E;\omega_z)\mid z]\) instead of \(-\Delta_zd_z\). This is why complete-service 00/10/01/11 outcomes and joint resource occupancy matter. It is an expectation of a *single optimized production objective*, not an independent technical-value bonus.

### 2. Conditional transport certificate and its sharp domain

Suppose a matched, policy-isolated, full-service trial or a causally justified design establishes conditional **upper bounds**
\[
q_E(z)-q_R(z)\le u_z\quad\text{for every }z\text{ with }\mu_z>0. \tag{T2}
\]
Such bounds may differ across sites. They may arise from direct paired end-to-end comparison with calibrated uncertainty or, less sharply, from valid marginal-only Fréchet constraints. A pooled source sample upper bound \(E_\nu d_z\le d_0\) is **not** (T2). A selection-on-observables adjustment requires both conditional exchangeability/transport invariance and positive study support for the target \(z\), not just known importance weights.

**Proposition T1 (demand-weighted robust route certificate).** If R and E are both uniformly feasible under the admitted complete physical-history laws and (T1) holds, then
\[
J_\mu(R)-J_\mu(E)\ge
L_{\rm transport}:=\sum_z\mu_z[b_z-k_z-\Delta_z u_z]. \tag{T3}
\]
A positive bound establishes uniform R-over-E ranking under all jointly admissible environments. A zero bound establishes weak ranking. If the identified set permits each site's endpoint \(d_z=u_z\) simultaneously, this lower bound is *sharp*. If site-specific laws are coupled by one persistent latent transfer regime, the endpoint vector may be impossible; (T3) is still sufficient but need not be sharp, and the correct lower bound is the optimization over the **common complete-law** identified set. A negative \(L_{\rm transport}\) therefore means "not certified," **not** "E must win."

Proof: multiply each \(d_z\le u_z\) by \(-\mu_z\Delta_z\le0\), add \(b_z-k_z\), and sum. Under rectangular sitewise identified bounds with admissible endpoints, direct product construction attains equality. This is standard partial-identification/robust-decision algebra, not a claim of publication novelty. The previous \(d\le1/\Delta\) threshold is the single uniform-site special case with \(b=1\), \(k=0\).

There are two distinct transport routes:
1. **Conditional transport**: identify \(d_z\) or its bound at each \(z\), then recombine with target \(\mu_z\) and actual \(\Delta_z\). If \(d_z\) is stable across study and target, \(\sum_z\mu_z\Delta_zd_z=\sum_{z:\nu_z>0}\nu_z(\mu_z/\nu_z)\Delta_zd_z\) on overlapping support. The ratio corrects observed site mix; it cannot create a missing site's potential outcome.
2. **Direct matched target experiment**: choose a randomized/crossover/cohort design whose target weights and order definitions match the deployment decision, subject to no carryover or a separately modeled controller lineage. This directly targets the **economic difference**, not the average per-trajectory success improvement.

Site matching alone cannot repair differences in unmeasured failure severity, operator quality, customer order composition, conditional demand or controller-update spillovers. In particular, using a *post-treatment* variable such as the state the controller chose to visit as an ordinary site covariate can select on the intervention itself.

### 3. A constructive reversal with identical component skill marginals

Keep precisely the previous synthetic component marginals: \(P(B=1)=P(C=1)=.75\) under R and .9 under E **at each site**. Any joint acceptance value \(q\) in \([\max(0,2p-1),p]\) has nonnegative 00,10,01,11 cells \((1-2p+q,\ p-q,\ p-q,\ q)\).

There are two eligible sites:
- At site A, \(q_R=.75,\ q_E=.80,\ d_A=.05\).
- At site B, \(q_R=.50,\ q_E=.85,\ d_B=.35\).

Both site's reported component marginals are identical within each route, and all four underlying joint laws are valid. Hold \(b=1,\Delta=8,k=0\) constant, so **only site mix changes**. A validation sample with \(\nu=(.9,.1)\) reports an average paired difference of \(.9(.05)+.1(.35)=.08\), under the earlier hypothetical bound .1. Its average \(R-E\) contribution is \(1-8(.08)=+.36\). The target commercial fleet has \(\mu=(.4,.6)\): the actual target difference is \(.4(.05)+.6(.35)=.23\), so \(J_\mu(R)-J_\mu(E)=1-8(.23)=-.84\). **The old pooled certificate reverses under transport**, even though the technical component marginals, unit production value, incumbent benefit and physical choices are unchanged.

This is a Simpson/selection-type counterexample to transporting a pooled acceptance difference. It does not disprove the earlier conditional R2 proposition, whose matched constraint was asserted *for the target population*. It identifies the missing assumption that makes that proposition actionable. For any real claim, site eligibility, customer-window weights and held-out joint bundle outcomes must be observed under a defensible intervention—not replaced by robot picks/hour.

### 4. Unsupported sites: a sharp coverage threshold, not false precision

Let a fraction \(1-\varepsilon\) of target customer orders be covered by valid conditional matched evidence with \(d_z\le d_m\), while unsupported orders have only \(d_z\le u_m\) from admissible marginals. With uniform \(b,\Delta>0,k=0\), the worst-case target difference is bounded by
\[
D_\mu\ge b-\Delta[(1-\varepsilon)d_m+\varepsilon u_m]. \tag{T4}
\]
If the upper endpoints can be jointly attained, this is sharp. For \(u_m>d_m\), a strictly positive certificate requires
\[
\varepsilon<\frac{b/\Delta-d_m}{u_m-d_m}, \tag{T5}
\]
provided the right side is between zero and one; handle the empty/all cases directly. This is a **coverage sensitivity frontier**, not an experimentally estimated tolerance.

Using the same old technical marginals, an unsupported site can have \(q_R=.5,q_E=.9\), hence \(u_m=.4\). If the measured part truly justifies \(d_m=.1\), \(b=1,\Delta=8\), then the largest tolerable unsupported target fraction at the weak boundary is \(1/12\) (8.33%). At \(\varepsilon=.05\) the bound is +.08; at \(\varepsilon=.10\) it is −.04. The latter is **inconclusive**, not an E certificate. Constructing \(q_R=.7,q_E=.8\) on measured sites and \(q_R=.5,q_E=.9\) on missing sites attains both endpoints with valid four-cell laws, so the stated loss of certification is not a floating-point artifact.

This result does not say every unsupported site will be bad. It quantifies how far the positive same-world comparison could fail if the unobserved joint acceptance relation is unfavorable. Missing mass in the **commercial order population** matters, not simply missing mass among robot logs. A credible simulation or public-data target proxy may narrow \(u_m\), but cannot be assigned the status of a matched accepted-service evaluation without validation.

### 5. Demand can reverse a route ranking without any change to learned qualification

The same previous construction with a stable \(q_R=.7,q_E=.8\), hence \(d=.1\), and \(b=1\) gives R-E = +.2 when \(\Delta=8\) but −.2 when customer demand/contract capture makes \(\Delta=12\). No source-to-target transfer effect or robot success probability changed. Thus neither a fixed technical \(d\) nor a transported site mix is sufficient without the relevant customer demand window.

Model A supplies an interpretable, non-arbitrary \(\Delta\) for a *single divisible accepted-service capacity increase*. With \(G(a,c,K)=\max_{0\le q\le K}[(a-c)q-bq^2/2]\), the added captured operating value of an expansion \(K_0\to K_1\) is
\[
\Delta_A(a,c,K_0,K_1;\Pi_0,\rho)=
\rho\left\{\max[0,G(a,c,K_1)-\Pi_0]-\max[0,G(a,c,K_0)-\Pi_0]\right\}. \tag{T6}
\]
For fixed marginal costs and outside option, this is nonnegative but changes with \(a\), capacity saturation and \(\rho\); it can be zero. It is **not** automatically the value of a discrete B/C service bundle: there the full optimized recipe envelope must be evaluated instead. With route-specific end-market effects, output prices, customer sorting or capacity competition, compute the **route-specific** \(f(Q;\omega)\) and the new \(\mu\). Do not multiply a technical benchmark percentage directly by \(G\) or by a quoted robot wage.

There is also a time dimension: end-market demand may change between the source experiment, qualification and paid service. A structural customer-demand forecast or bounded scenario belongs inside the admissible complete world; it is not an automatic continuation-value premium. Data can have technically positive transfer and *zero* current economic value if demand is saturated or a qualified specialist is cheaper.

### 6. Correlated recovery outcomes alter the feasible information policy

The previous robust diagnostic assumed physical pathwise feasibility of every report-contingent terminal action. Consider a controlled first diagnostic costing one operator-resource unit, followed only on report **good** by a target action. A normal target action needs one more unit; a high-recovery realization would need two. Approved remaining total budget is 2.1; after a bad report, the policy takes a feasible specialist fallback without attempting that target action.

World W0 assigns probabilities \(P(good,low)=.5,\ P(good,high)=0,\ P(bad,low)=.4,\ P(bad,high)=.1\). World W1 assigns \(P(good,low)=.4,\ P(good,high)=.1,\ P(bad,low)=.5,\ P(bad,high)=0\). In both worlds, marginal good-report frequency is .5 and high-recovery probability is .1. Yet **acting on good** is resource-feasible on all supported paths in W0 (cost 2) and infeasible in W1 (a supported cost-3 path). Increasing the approved total capacity to 3 removes the particular obstruction, subject to the remaining safety requirements.

The cost variable here is a **potential resource requirement of an attempted target action**, not permission to actually violate an operator cap and count the resulting throughput. Under W1 the plan must use a safe abort/fallback, redesign the procedure or obtain approved reserve; one cannot simply multiply expected success by a discount and call the original plan feasible. It follows that separate unconditional accuracy and recovery-tail marginals do not identify the report-conditional positive support needed for a pathwise operating decision. The same objection applies if intervention gates censor latent failure recovery when the controller changes the states it visits. Source/target/correction records need report × exposure × error × recovery × full acceptance joint histories.

**Proposition T2 (support-sensitive feasible menu).** A policy that attempts an action on observed report \(y\) is uniformly feasible under the complete-law identified set only if its action's worst positive-support pathwise cumulative resource requirement fits its authorized budget for **every** law with \(P(y)>0\), with a feasible continuation/fallback. Marginal resource and marginal report distributions alone cannot establish this property. Proof: the definition of uniform pathwise feasibility quantifies over each possible world and every positive-support history; the two constructed joint laws have identical marginals but different support for the selected history. This is a direct application of the prior safe-support logic, not a new safety standard.

### 7. The information question is now where to validate, not how to fit another rate

The previous chapter sought a matched upper bound on \(q_E-q_R\). The new result shows exactly what that statement must condition on. A decision-focused validation program first enumerates target *customer order* strata and authorized recipe/rights windows, then distinguishes:
- whether a site × demand × service stratum has positivity under each **frozen controller lineage/embodiment**;
- its full-route joint 00/10/01/11 held-out outcome distribution and paired route difference, not independently reported successes;
- the qualified-incumbent output preserved or lost, complete resource cost and actual incremental captured contribution from \(f\);
- report-conditional eligibility, missed gate events, intervening recoveries and **positive-support peak resource cost**, including observed safe aborts;
- policy-induced data feedback: whether a source-rich routine controller visits the target rare states that deliberate grounding would expose.

A within-site crossover may reduce environmental variance but suffers from *carryover*: if R learns a better controller from the first exposure, E's potential second outcome is different than under E-first. Freeze independent lineages, randomize order and model carryover, or cluster assignment at controller-update pools. Choosing sites by what the current policy already successfully attempts creates missing-support bias. Unlogged zero-correction periods are not proof of no failures; audit independent eligible-state denominators.

The **next economical diagnostic** is targeted coverage of a small but high-\(\mu_z\Delta_z\) unsupported stratum or a report-conditional high-recovery tail, if one exists and the experiment itself is safe. The value of this measurement is whether its result can change the feasible route ranking after foregone production and testing cost. The formulas identify where information is potentially decision-relevant; they do not authorize trials, estimate an optimal sample size or imply that free, optional data cannot be retained.

### 8. Closest prior art and the contribution that remains open

This chapter is an application and connection of established methods: Pearl and Bareinboim (AAAI 2011) formalize causal **transportability** under source/target differences; Stuart, Cole, Bradshaw and Leaf (JRSS A, online 2010) address generalizing randomized studies using participation weighting; Manski (Econometrica 2004) develops **decision rules under heterogeneous incomplete evidence**; Zivich et al. (Epidemiology 2024) explicitly address nonpositivity in transport; Hudgens and Halloran (JASA 2008) study interference, the issue raised here by shared controller learning. The sources were checked on their publisher/abstract pages on November 18, 2026, not fully replicated; none is claimed as original robotics theory.

- Pearl and Bareinboim, "Transportability of Causal and Statistical Relations: A Formal Approach," AAAI 25(1), 2011, https://doi.org/10.1609/aaai.v25i1.7861.
- Stuart et al., "The use of propensity scores to assess the generalizability of results from randomized trials," Journal of the Royal Statistical Society A 174(2), first online November 30, 2010, https://doi.org/10.1111/j.1467-985X.2010.00673.x.
- Manski, "Statistical Treatment Rules for Heterogeneous Populations," Econometrica 72(4), 2004, https://doi.org/10.1111/j.1468-0262.2004.00530.x.
- Zivich et al., "Transportability Without Positivity: A Synthesis of Statistical and Simulation Modeling," Epidemiology 35(1), 2024, https://doi.org/10.1097/EDE.0000000000001677.
- Hudgens and Halloran, "Toward Causal Inference With Interference," Journal of the American Statistical Association 103(482), 2008, https://doi.org/10.1198/016214508000000292.

The candidate *integrated economic argument* now links transferable source experience → action/grounding/embodiment → safely supported state visits → **jointly** qualified accepted service → demand-weighted customer production and capture → the next investment. Its individually familiar mathematical ingredients are not evidence of a new theorem. DDA already makes production and data future value endogenous; there is no new credit for simply doing that. The challenge is a credible robotics-specific economic comparative static under observable assumptions, together with customer data that can distinguish it. Neither external novelty review nor a calibrated accepted-service panel has occurred.

### 9. What this tranche has and has not settled

**Established conditionally:** a valid conditional matched acceptance bound yields a demand-weighted same-world certificate; incomplete target support admits a sharp missing-share bound; identical component marginals and pooled study differences can reverse under site selection; changing demand alone can reverse the route rank; and separate report/recovery marginals cannot certify a pathwise action. The constructed synthetic cases were checked by direct four-cell laws, finite copula enumeration and exact-source JavaScript execution. These are theoretical counterexamples and conditional algebra, not robotics observations.

**Open:** globally optimal adaptive multi-slot policy with controller-induced customer selection and nonrectangular latent transfer; joint regime/report/recovery/accepted-service field evidence; safe validation approvals; the official quantitative production/value-chain atlas; independent proof review; and a credible novelty claim for the first paper. These limitations remain part of the Nov 22 Models A–B integrated synthesis gate.

**Exact next question:** when the choice of routine data, targeted grounding or embodiment itself changes future *customer order weights* and jointly accepted recipe support, can a tractable nonrectangular robust policy bound be derived without mistaking source-study support for target-demand support or invoking unrealistically adversarial regime switching? The next work must strengthen the common \(J(\pi,\theta)\) or deliver a clear impossibility/identification counterexample, not just alter a synthetic parameter set.
