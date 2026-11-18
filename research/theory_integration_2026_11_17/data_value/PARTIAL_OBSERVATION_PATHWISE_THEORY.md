# When Capabilities Become Production
## Information that is economically useful *and* operationally feasible: latent transfer, joint acceptance, and pathwise intervention budgets

**Private working continuation, 18 November 2026 UTC.** This deepens the existing sequential/multi-step data-value argument. It is a conditional finite-horizon economics/control analysis, not a hardware safety certificate, field estimate, original Blackwell/POMDP theorem, or publication-novelty claim. Values are normalized contributions from the **same optimized accepted-production function**, not prices assigned to data episodes.

### 1. The gap left by multi-step reachability

The previous [multi-step chapter](MULTISTEP_SUPPORT_THEORY.md) determined when approved production trajectories have positive support for a complete customer qualification bundle. A plausible next inference is that a high-probability diagnostic report necessarily makes the target-grounding route preferable to routine production or embodiment redesign. This inference fails when **the report changes which follow-on actions are legally/safely and pathwise resource feasible**. The signal changes both posterior expected qualification and the worst possible recovery load on an actual deployment.

Let a finite, fixed but unobserved transfer/alignment regime H belong to a set \mathcal H. The observed history is h_t=(y_0,c_0,q_1,...,y_{t-1},c_{t-1},q_t), and belief \pi_t(H)=Pr(H|h_t). Controller lineage, embodiment, rights, retained qualified recipe set Q_t, approved reachable state x_t, customer demand \omega_t, and remaining operator/other resources b_t belong in the observed state; latent physical conditions not measured must also be included in the belief. Distinct routine-field, intervention/recovery, teleoperated, simulated, synthetic, and pretrained inputs enter by **different observation and learning kernels**, never one transferable-data scalar.

For an action a, K_H(z|x,a) is the **joint** law of selected visited states, detected and missed interventions, recorded usable information, next qualified recipes and realized resource use c(z). The latter can depend on H and on recovery. A candidate is *almost-sure feasible* at a history if (i) each positive-probability successor under some H in supp(\pi_t) is approved, (ii) c(z)\le b_t componentwise for **every** such successor, and (iii) a safe authorized fallback exists for each successor history. This is a stronger requirement than bounding expected operator minutes or an ex-ante chance of exhaustion; neither is an appropriate substitute without explicit, approved risk policy.

With \beta\in(0,1], the finite-horizon optimized economic value obeys

\[
V_T(x,\pi,b)=f(Q_T;\omega_T),\qquad
V_t(x,\pi,b)=\max_{a\in\mathcal A^{as}(x,\pi,b)}
\left[m_t(x,a)+\beta\sum_{H,z}\pi(H)K_H(z|x,a)
V_{t+1}(x'(z),\pi_z,b-c(z))\right]. \tag{P1}
\]

Here m is current **net accepted customer service** (not a new data premium), and f is the previously specified production optimization including demand, qualified bundles, robot/human throughput, and the competent alternatives. The posterior \pi_z uses the **joint** likelihood of all observed parts of z, including a correction being absent, an independent gate audit and observed resource load when those are informative. All inherited cash, calendar, manufacturing and rights restrictions remain other coordinates of b and x. The admissible-menu test is performed on the full supported conditional transition, *not on an averaged transfer coefficient*.

**Proposition P1 (belief-and-budget recursion; standard).** In the stated finite model with perfect recall, observed budget history and a safe feasible fallback at each reachable history, (P1) equals the best expected accepted-production value among nonanticipating almost-sure feasible policies. Proof: for T, optimize the original qualified-service problem. At t, a policy first chooses one action measurable in its observation history. The pathwise support test is necessary and sufficient for feasibility of that action with safe descendants. The joint kernel and Bayes' rule give the successor belief, accepted recipes and budget. Induction optimizes all descendants. Finite action sets ensure the maxima exist. This is the usual belief-state and resource augmentation for constrained partially observed decision processes. It does **not** establish field safety, because the true transition support and admissibility approvals are empirical/legal inputs.

**Consequence.** Knowing that routine and grounding can each reach B with positive probability, or that grounding's signal is more accurate, is insufficient to order (P1). The menu itself changes with observation precision, allowable recovery resources, rights and embodiment. If a free optional signal is appended to an unchanged route without changing K's physical outcomes/resources or eliminating actions, the optimizer can ignore it, so value cannot fall. A noisy forced redesign that consumes scarce time is not that free-information comparison.

### 2. Sharp, auditable two-slot counterexample: imperfect diagnosis can make grounding unusable

Start with one already qualified production repertoire A; final incremental customer demand requires a *jointly accepted* B-and-C bundle of incremental optimized contribution \Delta\ge0. Both stages are within one customer order window. The enterprise has **2.1 units of shared operator/recovery capacity on every realized path**, not merely on average, and can always preserve A. The first action and its resulting report precede a final mutually exclusive service/qualification decision. There is no separate data-value term.

Let H\in\{A,B\} be equally likely; this A/B *regime label* is not the existing qualified production recipe A. The alternatives are:

| First action | Current net accepted flow | First-stage operator use | Report on H | Final feasible option |
|---|---:|---:|---|---|
| R: ordinary customer production | 1 | 0 | binary accuracy 3/4 | select H-specific target technique; correct H uses 1 operator, wrong H requires 2 for approved recovery; or specialist |
| G: deliberate target-grounding diagnostic | 0 | 1 | accuracy \alpha_G\in[1/2,1] | the same H-specific technique and fallback; or specialist |
| E: redesign the embodied interface | 0 | 1 | no regime signal | a safely supported H-independent new-body technique uses 1 operator and jointly qualifies B,C with probability 9/10; or specialist |
| S: qualified specialist production | 2 | 0 | no signal | repeat specialist for 2 or select ungrounded H-specific technique |

The final H-specific technique earns \Delta if its chosen regime matches H (both customer components jointly qualify), and zero incremental B,C contribution otherwise. Its recovery consumes 2 operator units on a mismatch but is physically approved only if those units are available. The specialist gives 2 of **actual accepted net production** within the last slot, no qualification promise and no operator use from this budget. The E success probability is an explicitly synthetic *held-out joint acceptance probability* and can be invalidated by an actual redesigned-body validation; it is not inferred from a benchmark. No first action automatically purchases a certified robot.

Under a strict pathwise budget 2.1, after R or S a target action's worst use is 2 and is feasible. After G with \alpha_G<1, every observed report leaves positive posterior probability of the opposite regime, so target use could be 1+2=3: **infeasible**, even if the signal is 99% accurate. After perfectly revealing G (\alpha_G=1), report-conditional mismatch has zero probability under the assumed exact model, so G plus the chosen correct technique uses 1+1=2: feasible. E consumes 1+1=2 on every path and is independently feasible.

The first-stage alternatives' optimized values are therefore

\[
\begin{split}
R(\Delta)&=1+\max\{2,(3/4)\Delta\},\\
G(\Delta;\alpha_G<1)&=2,\qquad
G(\Delta;1)=\max\{2,\Delta\},\\
E(\Delta)&=\max\{2,(9/10)\Delta\},\\
S(\Delta)&=2+\max\{2,(1/2)\Delta\}. \tag{P2}
\end{split}
\]

These already optimize a **competent** specialist, including specialist production in *both* slots. At \Delta=8:
- R=7, E=36/5=7.2, S=6.
- With perfect G, G=8 is optimal.
- With 99%-accurate G, G=2 because the risky follow-on target technique is not admissible. **E=7.2 wins**, even though it supplies no diagnostic information; a merely better score for the signal does not order economic routes.
- If the operator budget is actually 3 (and this change is feasible in the same order window), 99%-accurate G can attempt the target route and yields (99/100)8=198/25=7.92, exceeding E=7.2. If a regulator/operator instead authorizes an ex-ante **chance** of budget overflow at most 2%, G is also admitted since its overflow probability is 1%, but this is a different safety/contracting problem, not the original hard-budget solution.

An *expected*-usage budget would also falsely admit the 99%-accurate G action under the stipulated hard cap: its total expected operator use is 1+(99/100)1+(1/100)2=201/100=2.01\le2.1, despite a possible realized use of 3. This arithmetic is why safety feasibility must not be inferred from mean intervention cost. The frontier **jumps** at exactly perfect observation only because the model grants exact zero posterior support to the wrong regime under a hard constraint. It is an analytically useful pathology, **not** evidence that real-world sensors are ever perfectly informative or that a small model-score improvement safely eliminates recovery reserves. Allowing safe abandonment after mismatch *before* the second operator unit, a reserve worker, or a chance constraint changes the conclusion and must be measured independently.

**Proposition P2 (discontinuous feasible target learning).** In this model, with 2<b<3, both latent states initially supported, positive false-signal probability under G, and a last technique whose combined first-and-recovery operator use exceeds b precisely when H is mismatched, no contingent H-specific target action following G is almost-sure feasible. The same action becomes feasible if the report reveals H with probability one. Proof: with positive false-report likelihood, every report has a positive conditional probability of mismatch, consuming 3>b; exact revelation removes this event from posterior support and leaves cost 2\le b. Evaluate (P2) to see that the selected route at \Delta=8 changes from E to G. No claim of unconditional discontinuity across arbitrary control kernels follows.

This checks four structural assumptions simultaneously: latent transfer remains partly unknown; observations can alter the reachable action menu; a target-only **new embodiment** can be safer than extra source or grounding data; and customer demand \Delta determines whether the improvement beats a genuine specialist.

### 3. More informativeness does not rescue an infeasible action

Suppose a report from an ordinary productive route R is a garbling of a report from G, but G also consumes operator capacity, alters reachable target states, or displaces accepted output. Blackwell's experiment comparison *does not* rank the **complete acquisition routes**. Conversely, conditional on the *same* physical and qualified state transitions and demand, if one optional signal Blackwell-dominates another (the weaker signal can be generated from the stronger with a costless random map), and has no greater resource use or lost service, the stronger signal's recipient can simulate every weaker-signal contingent choice; its optimized value weakly exceeds the weaker's. This is the established Blackwell policy-simulation argument, not an original theorem. It does **not** apply if only the H marginal signal is more informative but the reports are differently correlated with future recovery and qualification outcomes.

This is an empirically important distinction: “teleoperation produced a higher-quality diagnostic dataset” says little about whether that route safely fits the actual scarce crew, customer calendar, training rights, target interface, and validated production bundle.

### 4. The second missing object: the *conditional joint* customer-acceptance law

The preceding exact P2 example assumes both B and C qualify together after a correct H-specific technique. General real deployments seldom identify this law from separately reported skill percentages. Let X_B,X_C denote **held-out jointly deployable** binary customer acceptance events after action a at observed report y and latent H=h. If their *conditional* marginals p_B(a,y,h), p_C(a,y,h) were identified but their dependence were not, the sharp Fréchet bounds are

\[
\ell_{ayh}=\max(0,p_B+p_C-1)
\ \le\
Pr(X_B=X_C=1\mid a,y,h)
\ \le\
u_{ayh}=\min(p_B,p_C). \tag{P3}
\]

For a pure complementary customer bundle with payoff \Delta\,1\{X_B=X_C=1\}, this yields, **for one known feasible policy a(y)**, terminal value bounds

\[
\sum_y Pr(y)\left[r_{a(y)}(y)+
\Delta\sum_h\pi(h|y)\ell_{a(y)yh}\right]
\le E[V_a]\le
\sum_y Pr(y)\left[r_{a(y)}(y)+
\Delta\sum_h\pi(h|y)u_{a(y)yh}\right]. \tag{P4}
\]

Add any earlier net accepted production once. The bounds are sharp when action/report/regime-specific potential-outcome copulas may vary independently and qualification outcomes do not affect the safety-feasible menu. For each fixed pair of marginals and any allowed joint q, construct cell probabilities Pr(11)=q, Pr(10)=p_B-q, Pr(01)=p_C-q and Pr(00)=1-p_B-p_C+q. All four are nonnegative precisely for q in (P3). With independently selectable conditional copulas, set each to its lower or upper endpoint. For adaptive choice, an outer max over feasible a(y) can be placed inside each report sum in both bounds; it remains sharp under this **variation-independence** restriction. If there are coupling constraints across counterfactual policies, shared hardware failures, or qualifications that affect operator/safety costs, these simple envelope bounds need not remain sharp.

**Identification warning.** Conditional p_B(a,y,h),p_C(a,y,h) are stronger objects than observed marginal benchmark rates. If H is latent and cannot be proxy-labelled or randomized, even the conditional marginals and \pi(h|y) may be unidentified. Bounds based on *mixture* acceptance rates alone can be wider; one must optimize over compatible latent mixtures and selection kernels, rather than plug inferred H as fact. Gate-selected correction logs alone identify neither exposure to unvisited states nor posterior H nor B,C copulas.

A concrete identified-set counterexample: suppose an approved routine route has *jointly observed in separate evaluations* marginal acceptances p_B=p_C=3/4, while a body redesign has p_B=p_C=9/10. At \Delta=8, if current routine production is 1 and redesign displaces it, the **routine economic interval** is [1+8(1/2),1+8(3/4)]=[5,7], while the **body economic interval** is [8(4/5),8(9/10)]=[6.4,7.2]. These intervals overlap. In one permitted world routine joint success 3/4 and body joint success 4/5 imply routine 7>body 6.4. In another routine joint success 1/2 and body joint success 9/10 imply body 7.2>routine 5. The very same technical marginals admit **opposite economically preferred production systems**. The joint law must be estimated on a matched *complete customer service* rather than manufactured as independent qualifications. This complements, rather than repeats, the earlier full-support copula counterexample by providing a **sharp decision-relevant identification interval**.

When the incumbent/specialist or other recipes are optimized alongside B,C, apply their production envelope to each possible **full joint Q**; (P4) is only for the pure single-bundle incremental special case. A robot accepting a motion is not automatic fulfillment of tooling, recovery, liability, and uptime requirements in Q.

### 5. What this changes in the integrated production argument

The causal chain is **production/diagnostic choice → safely observed exposure and report → posterior supported regime/retained update → safely feasible future policy menu → joint held-out accepted recipes → customer-production f(Q;\omega)**. The useful learning map is now a *decision-dependent controlled observation law*, not a scalar slope fitted to episode counts. Three distinctions are economically necessary:

1. **Information is not capacity.** A more precise target signal can be useless if its acquisition has consumed the recovery budget, while a new body can change the action graph with no superior signal.
2. **Support is not qualified output.** An action with positive reachability may have low completion chance, exceed actual crew availability, miss the customer window, or fail joint acceptance.
3. **Marginals are not portfolios.** Even identified component pass rates do not determine value under complementary production; the copula must be identified or bounded and the complete f optimization run.

No data source is guaranteed to help: routine field observations, intervention/recovery records, teleoperation, simulator probes, synthetic scenes, and public/pretrained inputs can differ in support, bias, rights, training cost and representation alignment. The *optional* availability of each source is not an obligation to spend training resources. When no source alters Q or the feasible policy set, its economic marginal value can be zero despite technical novelty; when a shared recovery bottleneck binds, its value can depend sharply on an unrelated customer opportunity.

### 6. Prior art, falsification and the next proof gap

The mathematics intentionally combines known machinery. Blackwell comparison of statistical experiments (1951/1953) gives garbling/simulation under matched decisions; the QuantEcon [exposition](https://python.quantecon.org/blackwell_kihlstrom) was inspected on 18 Nov 2026 UTC. Fréchet/Hoeffding dependence bounds predate this work; a [2013 account](https://link.springer.com/article/10.1186/2195-5832-1-14) restates the sharp constructions. Chatterjee, Chmelík, Gupta and Kanodia, *Optimal cost almost-sure reachability in POMDPs* ([Artificial Intelligence 234, 2016](https://doi.org/10.1016/j.artint.2016.01.007)) explicitly studies almost-sure POMDP reachability. McMahan and Zhu, *Anytime-Constrained Reinforcement Learning* ([arXiv 2311.05511](https://arxiv.org/abs/2311.05511), initial November 2023), studies never-violate-budget constraints. Santana, Thiébaux and Williams, [RAO*, AAAI 2016](https://doi.org/10.1609/aaai.v30i1.10423), explicitly treats chance-constrained POMDP execution risk. These abstracts/selected descriptions were checked 18 Nov 2026 UTC; full proofs/code were **not** reproduced. DAgger, ThriftyDAgger, and DDA's existing production-data valuation remain the nearest learning/economic seeds. None of the beliefs, robust feasibility, Fréchet arithmetic or static information-order constructions is claimed as new.

**Matched empirical discriminators:** independently audit eligible risky-state exposures and missed gates (including no logged correction); estimate report confusion matrix for a defensible H proxy; record per-branch peak operator/recovery demand, not only averages; safely validate regime-specific body/target actions under a pre-approved coverage protocol; retain policy version and qualified-incumbent alternative; measure joint B,C customer acceptance and accepted service in matched demand windows. A 99%-accuracy claim on a benchmark is not evidence of zero posterior support, nor permission to exceed an actual recovery budget. No such industrial panel or industry-dollar calibration is present.

**Exact next intellectual question.** Under partially identified regime-mixture and joint-qualification laws, what conditions make a particular **resource-feasible deployment policy** robustly optimal for a customer order, and which safe matched diagnostic could shrink the identified set enough to reverse that decision? The next tranche should derive set-valued Bellman bounds or a sharp one-step robust policy certificate without pretending that noisy diagnostics establish safe support. Then review the **whole integrated argument and Models A/B** at the Nov 22 synthesis gate; do not claim that gate passed today.

[Scoped executable model](partial_observed_budget.js) · [proof/counterexample ledger](PARTIAL_OBSERVATION_PROOF_LEDGER.md) · [empirical design](PARTIAL_OBSERVATION_EMPIRICAL.md) · [exercises](PARTIAL_OBSERVATION_EXERCISES.md) · [separate solutions](PARTIAL_OBSERVATION_SOLUTIONS.md).