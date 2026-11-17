# When Capabilities Become Production
## Endogenous transfer: source data, target grounding, and embodiment choice

**17 November 2026 | Integrated data-value theory, continuation of \`DATA_VALUE_THEORY.md\`.**  
**Status:** conditional analytical contribution and synthetic computation, not a measured robotics learning curve, estimated deployment return, or novelty claim.

### 1. The missing economic choice

The preceding chapter maps data-source exposure into qualification probabilities and then into the **optimized production-value table** \(f(A;\omega)\). It derives the data-value gradient, economic/technical interaction decomposition, and customer-conditioned optimal source mixtures. But its fixed nonnegative transfer matrix does not explain the enterprise decision to *change the transfer mechanism itself*. More source trajectories can be less effective than a small amount of target calibration; redesigned hardware or aligned representations may instead change how source experience applies to a target. These are different investments.

The question of this tranche is: **Under which information and operating conditions should a firm acquire more source experience, ground an existing dataset in the target, or change the embodiment so that existing knowledge becomes useful?** A second, complementary question asks when a short diagnostic evaluation of transferability is more valuable than immediate training.

We continue with the same economic \(V(Q;\omega)\), not a new synthetic dollar premium on data. For one candidate qualified service, put
\[
W_e(\omega)=V(Q\cup\{e\};\omega)-V(Q;\omega)\ge 0,
\]
after applying the same customer-demand, alternative-service, complete-order, scarce-resource and capture assumptions as the parent operating model. If changing embodiment \(e\) changes physically feasible service recipes or retained work, recompute \(W_e\), do not inherit it by fiat. Here, the numerical comparison deliberately holds \(W_e=W\) to isolate information/embodiment technology.

### 2. A structural information model rather than an arbitrary \(xg\) transfer coefficient

Consider a scalar latent task/environment parameter \(\theta\), and an embodiment-specific alignment or action-realization parameter \(\phi_e\). The target requires predicting a component
\[
h_e=k_e\theta+\lambda_e\phi_e.
\]
Assume independent Gaussian priors \(\theta\sim N(0,a^{-1})\) and \(\phi_e\sim N(0,b_e^{-1})\), with \(a,b_e>0\). Effective source observations identify \(\theta\), adding Fisher information \(x\ge0\); paired target/grounding observations identify \(\phi_e\), adding Fisher information \(g\ge0\). Source and target innovations are independent **conditional on these parameters**, and the observation operators are known in this benchmark. For independent Gaussian measurements, prior and sample precisions add. Posterior mean squared prediction error is

\[
S_e(x,g)=\underbrace{\frac{k_e^2}{a+x}}_{\text{source-reducible uncertainty}}+
         \underbrace{\frac{\lambda_e^2}{b_e+g}}_{\text{target-grounding uncertainty}}
         +\underbrace{\rho_e}_{\text{irreducible residual}}. \tag{G1}
\]

This is an elementary Gaussian-conjugacy identity, not a general claim that robotics data are Gaussian, interchangeable, independent, or accurately quantified by a trajectory count. "Effective information" is deliberately measured by posterior precision under a specified model/representation, not raw samples. \(\rho_e\) can include an irreducible operational component but must not stand in for an unqualified safety or support requirement. Source data may be field trajectories, teleoperation or simulation only after separately justifying the information operator and eligibility of that source. For biased or distribution-shifted data the precision-addition step may fail. Target-specific calibration and action feasibility remain explicit.

For a *single scalar evaluation criterion*, qualification occurs when the posterior prediction error is within a fixed tolerance \(\tau_e>0\). Under the stated Gaussian model, ex ante qualification probability is
\[
q_e(x,g)=\Pr(|h_e-\widehat h_e|\le\tau_e)
       =2\Phi\left(\frac{\tau_e}{\sqrt{S_e(x,g)}}\right)-1. \tag{G2}
\]
The threshold is a proxy for one controlled acceptance dimension, not a robot's full safe-service qualification. For an actual complete-order service, compose the relevant verified events and operational recipe and do not reinterpret one scalar success probability as an accepted customer order.

The expected incremental gross production contribution from this qualification is \(W_e q_e\) only when that single new qualification is sufficient for the stated service. A portfolio of qualifications uses the parent \(f(A;\omega)\) and its *joint outcome distribution* instead. Source/grounding expenditure and body-redesign expenditure are real costs, not new productive value.

### 3. Fixed-expenditure allocation: an exact source-versus-grounding solution

Let \(A=k_e^2>0\), \(C=\lambda_e^2>0\), existing source precision \(a>0\), target precision \(b>0\), and marginal information acquisition costs \(c_x,c_g>0\). Suppose the firm elects to spend exactly \(B\ge0\) on these two sources. The optimization is
\[
\min_{x,g\ge0}\; \frac{A}{a+x}+\frac{C}{b+g}+\rho
\quad\text{such that}\quad c_x x+c_g g=B. \tag{G3}
\]
Because \(q\) is strictly decreasing in \(S\), (G3) also maximizes expected gross contribution \(Wq\) for any \(W>0\) at the fixed expenditure \(B\). This is **not** yet the optimal amount of expenditure: the latter compares \(Wq-B\) over different \(B\), and an embodiment redesign also has its own construction/certification cost.

**Proposition G1 (global information allocation).** Put
\[
M=B+c_xa+c_gb,\qquad
\widetilde x=\frac{M\sqrt{A c_x}}{c_x(\sqrt{A c_x}+\sqrt{C c_g})}-a.
\]
Then the unique global optimizer for positive \(A,C\) is
\[
x^*=\operatorname{clip}(\widetilde x,0,B/c_x),\qquad
g^*=(B-c_xx^*)/c_g. \tag{G4}
\]
When both investments are positive,
\[
S_e^*(B)=\rho+
\frac{(\sqrt{A c_x}+\sqrt{C c_g})^2}
     {B+c_xa+c_gb}. \tag{G5}
\]
At a corner the value must be computed directly from (G1), not from the unconstrained expression (G5).

*Proof.* Substitute \(u=a+x\), \(v=b+g\). The constraint is \(c_xu+c_gv=M\). Cauchy–Schwarz gives
\[
\left(\frac{A}{u}+\frac{C}{v}\right)(c_xu+c_gv)
   \ge(\sqrt{A c_x}+\sqrt{C c_g})^2.
\]
Equality requires \(A/(c_xu^2)=C/(c_gv^2)\), giving the displayed unconstrained allocation. The variance objective is strictly convex along the budget line, so projection of its unique stationary point onto the feasible interval yields the unique global minimizer. If \(C=0\), all information spending goes to the source; analogous endpoint statements hold when only target grounding matters. \(\square\)

**Economic implication.** A large inherited stock of source data raises \(a\) and depresses the return to another unit of the same source. Grounding can become the optimal use of the next learning dollar even if it supplies fewer new trajectories. Changing embodiment alters \(C\), \(b\), irreducible variance, qualification tolerance, and possibly \(W_e\), which changes the optimal information mix. A body with lower target-action sensitivity \(C\) may shift budget back toward source collection. These are *conditional* statements in the information model; there is no reason to assume every physical redesign has \(C_{\rm new}<C_{\rm old}\).

**Useful negative result.** With one isolated service and fixed learning expenditure, multiplying its economic value \(W\) by a positive constant does **not** change the source/grounding split in (G4). It changes the optimal *total spend*, the decision to invest at all, and the choice between embodiments. To generate customer-conditioned mixtures of multiple qualifications, use the parent's production-value table, not a fabricated dependence of (G4) on \(W\). This is a boundary of the reduction, not an inconvenience to hide.

### 4. Even independent information channels can become complements or substitutes in qualification value

Let \(q(S)=2\Phi(\tau/\sqrt S)-1\) and \(\varphi\) denote the standard normal density. Direct differentiation yields
\[
q'(S)=-\tau\varphi(\tau/\sqrt S)S^{-3/2},\qquad
q''(S)=\frac{\tau\varphi(\tau/\sqrt S)}{2S^{7/2}}(3S-\tau^2). \tag{G6}
\]
Since (G1) is separable in source and grounding exposures, \(S_{xg}=0\), but
\[
q_{xg}=q''(S)S_xS_g
=\frac{A C}{(a+x)^2(b+g)^2}q''(S). \tag{G7}
\]

**Proposition G2 (conditional interaction sign).** Under this *Gaussian symmetric-tolerance qualification criterion*, data and grounding are locally complements in expected success when \(S>\tau^2/3\), locally substitutes when \(S<\tau^2/3\), and have zero cross-partial at equality. This sign applies to one qualifying event at a fixed embodiment and customer state; it is not a universal rule for robotics data or for the complete production network.

*Proof.* Both \(S_x\) and \(S_g\) are negative, hence \(S_xS_g>0\). Equation (G6) gives the sign of \(q''\). \(\square\)

Why this matters: positive interaction in qualification probability need not come from a multiplicative \(xg\) technology or a production complementarity. It can arise from **how independent reductions in predictive uncertainty pass through an acceptance boundary**. Conversely the interaction can change sign along the learning path without any change in which sources observe which parameters. A controlled experiment must identify whether interactions occur in the information technology, the evaluation/qualification rule, or the downstream production recipe. A forced positive or negative constant transfer edge can miss all three.

### 5. Source data can make a hardware redesign worth paying for

Suppose current and redesigned bodies provide the same incremental accepted service worth \(W\), with the same source parameter and scalar tolerance. They differ in target-grounding sensitivity \(C_{\rm old}>C_{\rm new}\). An optional redesigned body costs a fixed \(F>0\) relative to keeping the old one. At given inherited source exposure \(X\) and target grounding \(g\),
\[
\Delta_{\rm body}(X,g)=W\left[q\left(\frac{A}{a+X}+\frac{C_{\rm new}}{b+g}+\rho\right)
-q\left(\frac{A}{a+X}+\frac{C_{\rm old}}{b+g}+\rho\right)\right]-F. \tag{G8}
\]
This comparison is only a body-choice comparison with the same preexisting data, not the optimal choice over *all* competing learning expenditures.

**Proposition G3 (possible data-stock/body-choice reversal).** If for some \(X_0<X_1\) the gross quality improvement at \(X_0\) is less than \(F/W\), while at \(X_1\) it is greater, the body choice reverses; continuity ensures at least one crossing. There is no general monotonicity assertion for \(\Delta_{\rm body}\) at all stock levels.

An exact synthetic illustration uses \(a=1/5\), \(b=1\), \(A=1\), \(\rho=0\), \(\tau=1\), \(C_{\rm old}=4\), \(C_{\rm new}=1/4\), \(W=30\) and \(F=8\), all in normalized model units. With no extra inherited source experience, gross redesign advantage is approximately \(2.29086<8\). With \(X=2\), it is approximately \(12.06391>8\). The design changes the physical-to-information interface, not the customer contribution or the assumed source technology. This example shows **why knowledge accumulation can change which embodiment it is rational to manufacture**.

A more demanding check admits *all integer investments* in added source information and target grounding, plus the optional redesigned embodiment, under a common finite budget of 8 normalized units. Qualification retains the old policy unless a new option actually improves payoff. At \(X=0\) the global enumerated optimum in this declared discrete action set keeps the old body, buys two units of source information and four of target grounding, and yields about \(5.00764\) incremental net units. At \(X=2\) it redesigns immediately, with no additional training expenditure in that budget window, for about \(4.06391\) incremental net units. Each value is relative to the **different incumbent baseline at that stock**; comparing the two net numbers across different stocks as an effect on total production would be wrong.

Neither the body precision parameters nor the fee are estimated for any vendor. The example demonstrates possibility, not an engineering recommendation. Reallocating cash to a supplier, maintaining two bodies, switch delays, common safety constraints, and altered complete-order feasibility can reverse the chosen route. The old qualified body and its feasible service should be retained as the explicit outside option, rather than assumed destroyed by a failed redesign.

### 6. Pure information about *whether transfer works* can have economic value

The Gaussian benchmark presumes the source parameter is relevant to the target. But **whether a source representation transfers** may itself be unknown. Distinguish a target calibration that mechanically reduces posterior uncertainty from a short diagnostic trial that only reveals the transfer regime.

Let \(H\in\{0,1\}\) denote high versus low reusable-source relevance, with prior \(\pi\). After a diagnostic signal \(s\), the enterprise chooses either (i) source reuse with payoff \(R_H\) or \(R_L\) conditional on regime, or (ii) a competent target-specific/specialist alternative with payoff \(O\). The diagnostic does not directly improve a qualification in this example. Its **gross expected value of sample information** is
\[
\operatorname{EVSI}
=\mathbb E_s\left[\max\{\mathbb E[R_H 1_H+R_L1_{\neg H}\mid s],O\}\right]
-\max\{\pi R_H+(1-\pi)R_L,O\}\ge0. \tag{G9}
\]
The inequality follows from the convexity of a maximum of affine payoff functions and the martingale property of posterior beliefs. Strict value requires a decision-relevant posterior change; precise information that never changes the optimal action has zero decision value. This is standard Bayesian decision/experiment design, not a new theorem.

With a synthetic \(50\%\) prior, \(80\%\)-accurate binary signal, reuse returns \(7\) in the high-relevance state and \(-1\) otherwise, and the alternative returns \(5\). Without the signal the firm chooses the alternative and earns \(5\). After the positive signal it prefers reuse, worth \(5.4\); after the negative signal it stays with the alternative, worth \(5\). Each signal has probability \(1/2\), so expected payoff is \(5.2\), gross EVSI \(=0.2\). A diagnostic costing \(0.1\) is valuable; one costing \(0.3\) is not. This does not assume a new model magically gets better because it was measured.

The diagnostic-selection model and the known-linear-Gaussian technology are **alternative information regimes**, not simultaneous premises. An extension should learn the source-to-target observation operator and jointly choose diagnosis, collection and target alignment; its net value must account for the ability to retain existing policies.

### 7. Joint qualification is not generally independent

A single source parameter learned for multiple target bodies can enter each qualification error. For example,
\[
E_1=k_1\varepsilon_\theta+\lambda_1\varepsilon_{\phi_1},\quad
E_2=k_2\varepsilon_\theta+\lambda_2\varepsilon_{\phi_2},
\]
where the residual errors are independent except for the **shared** source residual. Then
\[
\operatorname{Cov}(E_1,E_2)
=k_1k_2/(a+x).
\]
Even if individual source/ground measurements are conditionally independent, the realized qualification events may be correlated. If target-specific errors vanish, \(E_1=E_2=\varepsilon_\theta\) for matching coefficients and thresholds: the probability that *both* qualify is \(p\), not the product \(p^2\). As source residual variance vanishes with abundant valid source information, target-specific errors can instead become independent under the particular assumptions.

This is a constructive warning to the earlier portfolio data-value model: its product distribution applies only with an actual conditional-independence justification. A joint customer service requiring both qualifications must be valued with the **joint** probability. Source data can affect correlation as well as marginal probabilities. There is no defensible conversion from two separate benchmark success percentages into the probability of an accepted complete order without joint evaluation.

### 8. The common continuation problem and accounting boundary

The existing economic state should be kept intact:
\[
s_t=(D_t,\Pi_t,Q_t,K_t,\omega_t,\mathcal R_t),
\]
where \(D\) denotes data and metadata, \(\Pi\) an inferred source-target transfer/representation state, \(Q\) retained qualified configurations, \(K\) physical capacity/embodiments, \(\omega\) customer production opportunities, and \(\mathcal R\) available data/production rights. At date \(t\), feasible choices include current production, deliberate source observations, target grounding, diagnostic tests, compatible policy updates, embodiment investments, and competent human/specialist service.

The expected current accepted-service contribution plus the *single* discounted optimized continuation value determines the policy. One must not add a separately assigned "value of data" to \(V_{t+1}\) if its production benefit is already reflected there. The Gaussian results above describe one tractable component of the transition, not a solved multiactor general equilibrium or the full dynamical system.

A negative-transfer result under compulsory use of source data does not overturn the basic free-option dominance result from the previous chapter. With costless additional **optional** access, unchanged rights, and retained policies, the feasible choice set grows; its optimized value cannot fall. Forced training, compute congestion, contaminated representation, deprecation of a safe old policy, or acquisition price are different interventions that can reduce value.

### 9. The strongest objections and what would distinguish them

1. **Source and target do not share a latent task variable.** The structural model deliberately assumes a valid common \(\theta\). For a purely target-specific factor, the corresponding \(A=0\); source data then have no effect. A representation that aligns observation or action spaces can alter whether a shared \(\theta\) is identifiable. Independent and correlated noise, label bias and domain shift need explicit alternative specifications.
2. **Gaussian precision is not learned control competence.** Posterior inference accuracy need not translate to a supported, reliable, coordinated robot. The acceptance probability is a scalar *proxy*. Actual field recovery and complete service require additional qualification events and measured operating recipes.
3. **Changes in embodiments change market value, not only noise.** A gripper or tool can affect cycle times, customer demand, maintenance, manufacturing, safety and supervised interventions. Recompute \(W_e\), resources and timeline rather than holding them constant outside the diagnostic example.
4. **Data rights and source eligibility differ.** A public video, action-free trace, simulated trajectory, teleoperation demonstration and target pair can support different observation operators. They cannot be collapsed into one cardinal dataset unless the relevant information contributions are actually identified.
5. **Two average benchmark scores are not a joint service panel.** Use held-out embodiment/site evaluation and joint attained-qualification events. Separate fixed-budget reallocations from more data at additional cost; separate a diagnostic target exposure from target training. At the economic layer record accepted order, real alternatives, operating displacement and contribution. Do not infer industrial dollar returns from normalized qualification probabilities.
6. **A smarter baseline might win.** Compare against a competent target-only specialist, policy-retention, source-only scaling, targeted grounding, and matched redesigned body. The new approach must win without assuming deliberately weak training or a free transfer edge.

**Closest prior art and evidence, bounded audit.** Classical Bayesian experimental design already optimizes information decisions under utility functions: Chaloner and Verdinelli (1995), [_Bayesian Experimental Design: A Review_](https://doi.org/10.1214/ss/1177009939). Farboodi–Koh–Xia, [_Data-Driven Automation_](https://www.nber.org/papers/w35320), June 2026, already contains production-generated heterogeneous data, directed task spillovers, a forward-looking planner and an extended aggregation specification. Sridhar et al., [_Cross-Embodiment Transfer via Behavior-Aligned Representations_](https://arxiv.org/abs/2607.27549), July 30, 2026, report source-dataset/representation interactions in controlled evaluation, including source-size relevance; that work does not estimate customer production surplus. Yan et al., [_ZETA_](https://arxiv.org/abs/2609.02546), September 2, 2026, distinguish strict from pretraining-exposed zero-shot target evaluation and separately study representation, diversity, co-training and target exposure; its controlled tabletop tasks are not our enterprise service measurements. The earlier [_Data Analogies_](https://arxiv.org/abs/2603.06450) (2026) motivates morphology-dependent pairing. Sources inspected as abstracts/HTML on November 17, 2026; no full result reproduction or experimental re-estimation. Claims of scientific novelty are unwarranted at this stage.

### 10. Empirical bridge and the next theoretical gap

The direct test design varies (a) source quantity, (b) paired target-grounding quantity, (c) representation/alignment, and (d) embodiment, while matching target tasks, environment/site, compute budgets, prior/target exposure, data rights, and acceptance protocol. Log trained-policy identity, source eligibility, inherited dataset stock, realized joint qualifications, physical recovery, accepted complete orders, and the best specialist/human alternative. The experiment should test whether the returns match precision-addition, indicate a learned cross-source operator, or exhibit adverse shift/structural failure.

The most important unresolved question is **the dynamic choice of which productive deployment or deliberate experiment to run when it changes both the source-data stock and the information needed to ground that stock in future bodies.** The next derivation should allow a target alignment experiment to change the measured transfer mapping and future deployment choice, with common resources and a credible profit-only comparator. The production atlas and quantitative official backbone remain active but unsolved. The November 22 synthesis gate must judge the integrated data-production argument, not the count of subsidiary models. December 25 remains the final verified package target.

### Reproduction and proof boundary

The associated \`grounding_embodiment.js\` is standard-library JavaScript with an elementary numerical Gaussian CDF quadrature. It implements (G1)–(G9), finite-state diagnostic updating, exhaustive discrete investment comparison, analytical conditional allocation and scoped numerical checks. Its mathematical assertions were executed using the exact JavaScript functions serialized to the committed source blob. Local independent Python/standard-library checks confirmed the key allocation, redesign and diagnostic outcomes. V8 numerical agreement and independent arithmetic are **not proofs**; proofs are the arguments above. Full historical repository CI, Node file invocation and empirical calibration have not been performed in this tranche.
