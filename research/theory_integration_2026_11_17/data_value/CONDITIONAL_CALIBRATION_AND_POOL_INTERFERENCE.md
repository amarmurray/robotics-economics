# When Capabilities Become Production — diagnostic transport and shared-controller interference

**18 November 2026. Private theory continuation of the same integrated argument.** Direct continuation of [COUPLED_IDENTIFICATION_AND_AUDIT.md](COUPLED_IDENTIFICATION_AND_AUDIT.md), [TRANSPORT_AND_SAFETY_IDENTIFICATION.md](TRANSPORT_AND_SAFETY_IDENTIFICATION.md) and the root [THEORY_MANUSCRIPT.md](../THEORY_MANUSCRIPT.md). All payoffs below are constructed *normalized captured contribution from accepted customer service*, not measured robot performance or dollars. No claim of scientific novelty.

## The question left by the coupled response-law result

The response-type LP uses a complete persistent world to compare counterfactual histories, but the preceding diagnostic bridge required sensitivity and false-positive rates to be stable across a **pre-action customer-demand stratum** D. And the earlier 1/5 routine–4/5 grounding hedge required independent learning pools with additive production. Neither follows from a robotics transfer benchmark. What remains identified if both are relaxed, while still retaining competent policies, matched resource limits and complete customer orders?

Use the same \(Q_t\) (body, retained policies, rights, qualified joint recipes and resources), \(\omega_t\) (actual orders including zeros, capture, costs, alternatives), \(V(Q_t;\omega_t)\) (optimized feasible accepted-service contribution), and full-history \(J(\pi;q)\) (current accepted production, costs and terminal operating value each counted **once**). A report is valuable only through a feasible decision and its effect on \(J\); no appended "data premium."

## 1. Pool-level diagnostic calibration does not identify customer-conditioned transfer

Retain the preceding synthetic four-type example: persistent latent transfer alignment \(H\in\{0,1\}\), pre-action high-opportunity customer stratum \(D\in\{0,1\}\), both with marginal 1/2, and \(t=P(H=1,D=1)\). The complete *route* contribution difference is
\[
J_R(t)-J_G(t)=10t-3,\qquad 0\le t\le 1/2. \tag{DC1}
\]
This is a result *inside the constructed response table*, not a new structural or estimated success law.

Suppose a safe binary transfer diagnostic Z has pooled \(P(Z=1\mid H=1)=0.9\) and \(P(Z=1\mid H=0)=0.1\), and an auditable pre-action event gives \(m=P(Z=1,D=1)=0.34\). **Do not** assume the report rates are invariant in D. Write
\[
m-t=P(H=0,D=1,Z=1)-P(H=1,D=1,Z=0).
\]
The first term is between 0 and the pooled false-positive mass \(P(H=0,Z=1)=0.05\); the second is between 0 and the pooled false-negative mass \(P(H=1,Z=0)=0.05\). Consequently
\[
\boxed{t\in[m-.05,m+.05]=[.29,.39],\quad
J_R-J_G\in[-.1,.9].} \tag{DC2}
\]
Both endpoints are attained by *complete* binary distributions sharing all of: \(P(H)=P(D)=.5\), the pooled \(H\times Z\) confusion matrix, and the complete \(D\times Z\) table. Here the rows are \((H,D)=(1,1),(1,0),(0,1),(0,0)\); entries are **joint masses**, not conditional report accuracy.

| Admissible world | Four \(P(H,D)\) masses | Four \(P(H,D,Z=1)\) masses | \(t\) | \(J_R-J_G\) |
|---|---|---|---:|---:|
| Low alignment–demand coupling | (.29,.21,.21,.29) | (.29,.16,.05,0) | .29 | -.1 |
| High alignment–demand coupling | (.39,.11,.11,.39) | (.34,.11,0,.05) | .39 | +.9 |

Every \(Z=1\) cell is no larger than its parent mass. Both have \(P(H=1,Z=1)=.45\), \(P(H=0,Z=1)=.05\), \(P(D=1,Z=1)=.34\), and \(P(D=0,Z=1)=.16\). Hence *even exact pooled classification accuracy and the full observed demand/report table cannot rank routine and grounding*. The lower and upper bounds in DC2 are sharp for these stipulated margins, not generic bounds for other panels. Full proof in [the ledger](CONDITIONAL_CALIBRATION_POOL_PROOF_LEDGER.md).

The earlier \(t=(m-.05)/.8=.3625\), giving \(J_R-J_G=.625\), is valid **only** under the additional \(P(Z=1\mid H,D)=s_H\) invariance. It is a distinct model, not an estimate obtained from the pooled numbers. Likewise, the earlier *interval* \(m\in[.34,.40]\) coupled with only pooled calibration permits \(t\in[.29,.45]\), leaving a pairwise interval \([-.1,1.5]\); it does not retain the earlier strictly positive certificate.

**Operational meaning.** D may affect the difficulty, lighting, substrate, operator gating or coverage of a target-body report even at identical underlying source experience. Such mechanisms are hypotheses, not observed facts. A measurement that labels "transfer" by simulated success while real whole-service acceptance and recoveries differ across customer strata does not validate invariance. Either safely calibrate joint \((H,D,Z)\) using a defensible held-out H criterion, or, preferably where eligible, randomize *complete route policies* at independent controller-pool level and directly follow pre-registered customer accepted-service orders (including zeros). Random assignment identifies mean route effects under its own stability and overlap assumptions without pretending to observe latent H for everyone.

## 2. Independent fractional allocation is an economic/physical assumption

For independently assigned and noninterfering eligible pools, the previous example gave
\[
J_0(x,t)=xJ_R(t)+(1-x)J_G(t)
=8-3x+(10x-2)t,\quad x\in[0,1], \tag{PI1}
\]
where x is routine share. Independent flexible mixture \(x=1/5\) guarantees 7.4 throughout \(t\in[0,.5]\); a perfect **population-level** t audit has zero incremental *maximin* value under that exact convex menu.

Now suppose a controller pool draws two eligible learning slots with independently randomized routes. Their assignments differ with probability \(2x(1-x)\). If route-discordant training on the **same shared controller** causes a *net loss L in accepted-service contribution per slot* from interference, measured after any usable policy retention and safe fallback, the expected per-slot loss is \(2Lx(1-x)\). Denote \(\kappa=2L\). Then
\[
J_\kappa(x,t)=8-3x+(10x-2)t-\kappa x(1-x). \tag{PI2}
\]
For positive \(\kappa\), destructive pool interference; for negative \(\kappa\), a measured incremental **jointly accepted recipe** from complementary exposure with benefit \(-L\). This polynomial has a concrete *random-pair support mechanism* rather than postulating that volume x times grounding share magically creates transfer. Still, constant L independent of H,D is a conditional reduced-form hypothesis to be tested with frozen-controller matched pairs, not a field-established transfer law. If route assignment or pair membership reacts to H or demand, \(2x(1-x)\) no longer automatically holds.

**Conditional policy result.** In this exact population \(t\in[0,1/2]\), if \(\kappa\ge5/2\), \(\max_x\min_t J_\kappa(x,t)=7\), attained by the old *pure grounding* policy \(x=0\). In particular \(L=1.5\), \(\kappa=3\) destroys the independent mixture's 7.4 guarantee: the old 1/5 hedge now guarantees 6.92. This does **not** mean optional free data or a retained old qualified policy reduces the optimal value; the pure G policy remains available and secures 7. The intervention changes the *physical joint learning action* and its resource/cost menu.

With \(\kappa=-3\), genuinely complementary shared-pool learning instead makes the 1/5 routine mixture guarantee **7.88** (compared with 7.4 under independence); it is optimal within PI2 by the same piecewise minimization. The sign and magnitude cannot be recovered from any number of pure-R and pure-G trials, because \(x(1-x)=0\) at both extremes. Both positive and negative pool interactions preserve exactly the preceding pure-route payoff evidence.

**The audit's value depends on the actual feasible menu.** Retain pure R and G, the competent specialist S=5, and embodiment E=6. Permit, as a genuine alternative, isolated independent mixed training at a per-slot incremental coordination/compute/validation expense \(c=0.5\) whenever both routes are used. For \(\kappa=3\), the best unconditional robust policy is G with floor 7: pooled mixing guarantees at most 7 and isolated mixing at most \(7.4-c=6.9\). A perfect costless *population t* report permits choosing a pure route and guarantees \(\min_t\max(J_R,J_G)=7.4\), a **gross audit gain of .4**. If mixed independent pools can instead be maintained costlessly (\(c=0\)), they remain an option securing 7.4, restoring **zero** incremental maximin audit benefit. Thus the earlier zero-information-value example and this positive-information-value example are both correct *for different feasible menus*. No oracle knows individual H, and the report does not itself create competence.

This is not an empirical claim that robot retraining destroys older policies. Frozen checkpoints, specialist fallbacks and opt-out/no-retrain routes remain options. The assumed pool conflict applies to a **new shared update** whose future recipe must be requalified; if an independent retained controller can be deployed at no incremental cost/capacity, negative interaction is avoidable and the model must include that option. No capability can be labeled "qualified" from the illustrative polynomial alone.

## 3. Physical support, identification and the maintained production theory

A pathwise recovery cap is tested on the **whole controller pool** and every supported report/correction path. If a mixed training policy has positive probability of requiring recovery 3 under an approved cap 2 with no certified abort before attempt, that policy is simply not admissible, regardless of its attractive \(J_\kappa\). The examples above assume the pool combinations have already passed the *modeled* hard-cap check; this is not a safety certification.

The prior complete-response-type LP can still represent interference **when its observational unit is the entire pool and a type contains potential histories for the complete joint assignment vector**. What breaks is the attempt to treat robots inside a shared pool as independent individual response types or to infer the mixed-route cell from single-route marginal means. A separate nonlinear stochastic-kernel restriction may further shrink the pool-level LP identified set. This matters for fleet scale, capacity rights, computational reuse, and whether a specialized embodiment is worth its acquisition/qualification delay. A new physical embodiment is neither assumed a free substitute nor automatically compatible with previous source data.

Across field trajectories, recoveries, teleoperation, simulation, synthetic and public/pretrained input, the relevant empirical observables are not an aggregate trajectory count. For each source × target body × controller-lineage × site segment × policy, record eligible exposure and data rights, training recipe and resources, paired controller updates, held-out **joint** customer service acceptance, full order denominator, accepted quantity/alternative specialist, actual recovery tail and separately audited hardware/coordination costs. A benchmark change enters a production parameter only through validated qualification and the customer opportunity system. No duplicate future data premium is added to terminal \(V\).

## 4. Closest literature, alternate structures and falsification

Standard diagnostic misclassification and partial-identification inequalities already explain why a pooled confusion matrix need not transport to a different subgroup. Hudgens and Halloran (2008), *Toward Causal Inference With Interference*, JASA 103(482), DOI [10.1198/016214508000000292](https://doi.org/10.1198/016214508000000292), explicitly develop group interference estimands and two-stage randomization; this is **prior art** to the pool-level design, not a newly invented robotics estimator. DDA already treats production-created data, dynamic valuation and aggregation, and the earlier chapters credit LP, Fréchet, treatment choice and learning-by-doing foundations. The candidate paper contribution remains *integrating actual customer-qualified production, endogenous useful data and safe/physical pool choices* with measured discrimination; uniqueness is not established.

Four alternatives challenge the inference: (i) all differences vanish after target-stratified Z validation; (ii) separate frozen policies make \(\kappa\) effectively zero at affordable capacity; (iii) joint accepted-service complementarity makes \(\kappa<0\); (iv) shared recovery capacity makes otherwise profitable mixing infeasible. Even with correct model arithmetic, the observed pure endpoints do not tell these structures apart. Real world cross-pool spillover, nonrandom demand evolution, controller version switching and learning saturation require potential-history kernels, not PI2.

**Nearest-term tests, not completed evidence:** (a) safely validate report behavior by pre-action D and independently validated target acceptance; (b) compare matched pure versus mixed controller-pool assignments with stable starting checkpoints, full subsequent orders and recovery tails; (c) price actual separate-controller replication/validation resources, not hypothetical RaaS terms; (d) put accepted-service recipe and customer demand in the wider production network. These tests can reject either sign of \(\kappa\); they cannot ethically be conducted using only a model-implied recovery guarantee.

## 5. November 22 synthesis gate and broader roadmap

The tightened spine is now: sources and target grounding alter the distribution of *qualified recipe sets*; controller retention, interference and safety determine which joint learning actions are feasible; customer orders and complements determine production \(V\); demand, information and resources determine the full history value \(J\). Policy comparisons require the same world, the same complete customer denominators and feasible alternative investments. Conditional data elasticity and numerical benchmarks remain **inputs to be tested**, not dollars themselves.

For Models A/B, PI2 reduces to the existing independent production model at \(\kappa=0\), and DC2 reduces to the prior diagnostic inversion only with D-conditional invariance. The earlier cash/investment mechanisms remain available but this run does not expand default contracts. The official BEA and BLS production backbone, actual matched accepted customer panel, independent proofs/originality review and first-paper contribution decision remain open. A genuinely current source route is BEA's [Input-Output table index](https://www.bea.gov/itable/input-output) (page modified 13 Nov 2026, annual table update in late September) and BLS [Table 1.9, 2025–35 industry–occupation matrix](https://www.bls.gov/emp/tables/industry-occupation-matrix-industry.htm); their **published indexes** are verified but a reconciled numeric joint matrix and a robot-addressable task mapping are **not** extracted here.

**Exact continuation:** Identify a feasible, demand-stratified *route × controller-pool interference* measurement or justified kernel restriction that can shrink the same-world response-type decision interval without assuming independence or forcing unsafe diagnostics; then assess whether source/grounding/embodiment economics survive an observed accepted-service panel. The November 22 review is still an open scientific gate; keep theory dominant through December 6 and December 25, 2026 23:59 Eastern as the final target.
