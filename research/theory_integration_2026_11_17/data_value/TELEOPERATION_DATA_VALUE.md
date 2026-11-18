# When Capabilities Become Production
## Teleoperation as production, learning, and information about transfer

**November 17, 2026 (America/New_York)**  
**Private working theory continuation. Conditional derivations and synthetic computations; no industry calibration or scientific novelty claim.**

This chapter continues the same operating/qualification argument and the preceding data-value and endogenous-grounding chapters. It answers the next question in the persistent program: when should a firm use scarce productive capacity to generate ordinary source experience, teleoperate a target task, or run a separate experiment? Amar's additional seed is incorporated explicitly: service has a market price, human intervention has a cost, and the data should ultimately matter for valuable work.

## 1. The economic object

A teleoperated episode can deliver three distinct things:

1. A current accepted service, such as an order completed with retained human assistance.
2. A change in the future technical policy or qualification distribution.
3. Information that changes which future learning, embodiment, or deployment investment is worth making.

These need not move together. A helpful intervention can rescue today's service without improving a retained policy. A demonstration can improve an uncommercialized skill without changing the optimal production plan. A diagnostic can prevent a bad investment without improving any robot's performance. The three channels belong in one continuation account; they must not be added as separate bonuses when their consequences are already counted.

### 1.1 Connection to the specified paper

The source is Farboodi, Koh and Xia, *Data-Driven Automation*, arXiv:2606.10127. In the inspected v1 HTML, Section 2.1 makes data accumulation depend on task production and specifies directed spillovers. Section 2.2 discusses paid human labeling and the strong loss-to-productivity assumption. Section 5 already values future data in a planner problem; Appendix B considers complementary aggregation and new tasks. Our extension specifies controlled human interventions, uncertain transfer and qualified customer service. It does not claim that production-generated data or forward-looking data value is missing from that paper. [S1]

### 1.2 Prices and units

Use \(w_r\) for the payment per accepted unit of service \(r\), and \(w_H\) for compensation per unit of teleoperator time. If a commercial quote instead uses \(w_r\) for remote labor, relabel that quote \(w_H\); the economic distinction is between what the customer buys and the human input used to supply it.

For a feasible operating action \(a\), define current provider contribution

\[
m_t(a;s)=\sum_r w_{r,t}y^{\rm accepted}_{r,t}(a)
          -C^{\rm other}_t(a)-w_{H,t}h_t(a).
\tag{T1}
\]

Count complete accepted service, not each motion as a sale. Include compute, support, resets, integration, switching and expected contractual operating costs where relevant. The actual scarce-resource vector can include robot time, tools, human attention, capacity reserved for existing customers and cash. A high-margin source task is not freely available if it consumes the capacity needed for something else.

This is a provider objective under a stated payment rule. Customer surplus, total resource surplus and distributable cash are different objectives. The existing operating model determines the appropriate contribution weights and cash constraints; this chapter does not change their accounting.

For a matched, finite future quantity \(N\), suppose a provider can deliver with a competent human/specialist recipe costing \(c_A\) per unit or, after qualification, a robot recipe costing \(c_R\). Both receive the same output payment and use the same relevant capacity. The incremental operating value is

\[
W(w_r)=N\left[
 \max\{0,w_r-\min(c_A,c_R)\}-\max\{0,w_r-c_A\}
 \right].
\tag{T2}
\]

This small example exposes why a service price is not a multiplier on an arbitrary benchmark gain. If \(c_R<c_A\), the gain is zero below robot break-even, increases over the entry region, and plateaus at \(N(c_A-c_R)\) once both recipes are profitable. Demand expansion, access to previously unserved orders or a binding capacity constraint changes that calculation and must enter the operating problem explicitly. Throughout, \(c_A\) may be the better of a human and a credible specialized robot option.

## 2. A common controlled-production and learning environment

Retain the program's state

\[
s_t=(D_t,\Pi_t,Q_t,K_t,\omega_t,\mathcal R_t,B_t).
\]

Here \(D_t\) includes data and provenance; \(\Pi_t\) is the belief about transfer and other unknown technical conditions; \(Q_t\) is the collection of retained qualified configurations; \(K_t\) is physical and organizational capacity; \(\omega_t\) is customer demand and its timing; \(\mathcal R_t\) denotes usable rights; and \(B_t\) records the relevant cash position.

An action chooses production mode, human intervention/monitoring, deliberate experimentation, training or investment subject to the same feasible resources. Its joint transition law produces accepted output, observations, new data, possible qualifications and changes in resources. The data law is conditional on the intervention policy and the states actually visited. It is not necessarily a count proportional to total completed jobs.

For a finite horizon, write

\[
J_t(s)=\max_{a\in\mathcal A_t(s)}
 \left\{m_t(a;s)+\beta\,\mathbb E[J_{t+1}(s')\mid s,a]\right\}.
\tag{T3}
\]

The terminal condition contains remaining production opportunities or assets and obligations. It contains no arbitrary premium for possessing a dataset. If current retained cash is carried as an asset in the state, use either dividends plus terminal wealth or another consistent cash objective; do not count it twice.

For two feasible actions, teleoperation \(T\) and a matched alternative \(A\),

\[
\Delta J_t =
m_t(T;s)-m_t(A;s)
+\beta\left(\mathbb E[J_{t+1}(s'_T)]-\mathbb E[J_{t+1}(s'_A)]\right).
\tag{T4}
\]

Equation (T4) is a decision identity, not a new Bellman theorem. It provides the correct test for the user's seed. A negative current contribution difference can be justified by a positive, *incremental* continuation difference. The alternative can itself generate valuable data. Comparing teleoperation with an artificially data-free competitor would bias the result.

Holding the continuation schedule and all other inputs fixed, let \(P\) be a fee for one specified intervention, let \(m_T^0\) exclude that fee, and let \(m_A\) include every already-priced cost of the alternative. The conditional maximum total fee is
\[
P^{\max}=m_T^0-m_A+
\beta\left(\mathbb E[J_{t+1}(s'_T)]-\mathbb E[J_{t+1}(s'_A)]\right).
\tag{T4a}
\]
For a fixed positive duration \(h_T\), divide by \(h_T\) to obtain the corresponding maximum hourly quote. If this value is negative, no nonnegative fee makes that intervention preferable in the specified comparison. This is state-dependent willingness to pay, not an equilibrium wage or an additive price per trajectory. Changing the common wage for both activities is a different comparative static: incremental human hours and any changes in future optimal policies must then be accounted for, as in Section 7.

### 2.1 What changed from the earlier chapter

The earlier transfer model explained how source information and target grounding affect predictive uncertainty, and how uncertainty can change embodiment choice. The present extension makes acquisition arise from rival, dated production activities and makes a grounding episode reveal information before the next expenditure.

This introduces a distinction that a fixed source-value ranking cannot represent: **two deployments can create the same data if both are undertaken, yet their order changes the value of the policy because the first deployment changes whether the second should be undertaken at all.**

## 3. A general two-batch result, without a stipulated learning curve

We first solve a small but complete choice problem with arbitrary terminal production values. It is a transparent local building block for (T3), not the whole program reduced to two tasks.

There are two equal-length operating slots. The same competent routine activity is available in both slots, earning \(c\). Two optional data-generating activities are each available once:

- Source activity \(S\) earns current contribution \(s\) and creates a specified source-data batch.
- Target activity \(G\) earns current contribution \(g\), creates a target-grounding batch, and reports a signal \(Z\) about unknown transfer conditions \(\Theta\).

Write \(k_S=c-s\) and \(k_G=c-g\) for opportunity costs relative to the routine activity. Assume nonnegative \(k_S,k_G\), stationarity over the two slots, no discounting within this short window, and no observation from \(S\) that changes beliefs before slot two. The physical effects of acquiring both batches commute. This means their final production consequences do not depend on order, apart from the opportunity to adapt the second decision.

The declared activities are financeable at their dates. This local benchmark isolates scarce productive slots and acquisition information; it does not solve a new cash or invoice-maturity constraint. Routine output is assumed to provide no additional information relevant to this particular target beyond what is already available. Section 6 explicitly removes that assumption by giving the source batch the same current contribution as routine work.

Let \(F_\Theta(x,g)\) be optimized terminal production contribution conditional on the regime and batches \(x,g\in\{0,1\}\). It can already integrate stochastic policy learning, complete-service qualification, retained configurations and human/specialist alternatives. It need not be a product, exponential curve or independent qualification model. In this benchmark, final validation makes usable configurations observable before terminal service, and an early report changes acquisition decisions but not the payoff of a fixed acquired batch combination. Thus \(F_\Theta\) does not give the operator unobserved-regime foresight when it chooses current actions. If uncertainty remains when final controls are selected, use the corresponding terminal belief-state decision problem instead of silently optimizing separately in unknown regimes.

Define the posterior incremental value of the source batch *after grounding*:

\[
M(Z)=\mathbb E[
 F_\Theta(1,1)-F_\Theta(0,1)\mid Z].
\tag{T5}
\]

### Proposition: production order and adaptive acquisition

Relative to two routine slots and the original terminal production value, the global optimum in this stated menu is

\[
\max\left\{
0,\;
-k_S+\mathbb E[F_\Theta(1,0)-F_\Theta(0,0)],\;
-k_G+\mathbb E[F_\Theta(0,1)-F_\Theta(0,0)]
       +\mathbb E[(M(Z)-k_S)_+]
\right\}.
\tag{T6}
\]

The three terms correspond to retaining routine production, buying only the source batch, and grounding first followed by source acquisition only when its posterior value exceeds its opportunity cost.

**Proof.** If the first activity is routine, only one data batch can be acquired in the remaining slot, so the plan cannot beat the best single-batch alternative. If \(S\) is first, there is no new decision-relevant information; the second choice is routine or \(G\). This yields source-only production or a precommitted pair. If \(G\) is first, the second decision is whether to incur \(k_S\) for the posterior gain \(M(Z)\); pointwise maximization gives the last term. This last term includes grounding alone because the source can always be declined. It also weakly dominates the precommitted pair because
\(\mathbb E[(M-k_S)_+]\geq\mathbb E[M-k_S]\).
All feasible plans are covered. Thus (T6) is global in the declared menu. \(\square\)

The result **does not** say that grounding is always the best first activity. Source-only value may dominate, the routine alternative may dominate, and the assumptions on availability and information can fail. Its constructive content is the complete policy comparison with an arbitrary terminal production technology.

### Information value separated from physical learning

Keep the same grounding batch and production effects, but delay its report until after the source acquisition decision. The gross gain from an early report, conditional on choosing the grounding route, is

\[
I=
\mathbb E[(M(Z)-k_S)_+]
-\left(\mathbb E[M(Z)]-k_S\right)_+\geq0.
\tag{T7}
\]

**Proof.** The positive-part function is convex and posterior conditional expectations preserve the unconditional mean. Apply Jensen's inequality. Strict inequality requires posterior realizations on both sides of the acquisition boundary with positive probability. \(\square\)

This is standard decision-theoretic information value. The economic interpretation is what matters here: the observation can change the desired *data portfolio*, not just the production decision after a fixed portfolio has been collected. In (T7), training quality for any fixed batch combination is identical across early and late reports. The value difference comes from using the report before committing the next scarce production slot.

This distinction prevents the false conclusion that every valuable observation must immediately improve task performance. It also prevents treating a measured performance gain as sufficient evidence of positive net data value.

## 4. A constructive example with positive source margin and noisy transfer diagnosis

All quantities in this section are synthetic normalized units.

A routine activity earns \(c=3\) per slot. Source teleoperation earns \(s=1\), so it is profitable on its own accounting but loses \(k_S=2\) relative to the best current use of the shared capacity. Target teleoperation earns \(g=-1\), so its opportunity cost is \(k_G=4\). These margins include operator compensation and other current operating costs.

Both acquired batches are needed for a new transfer route. In the reusable regime it adds \(W=20\) of future production contribution; otherwise it adds zero. The prior probability of reuse is \(\pi=1/4\). The grounding signal has sensitivity and specificity \(19/20\). These are model primitives, not estimates.

The future increment \(W=20\) is consistent with (T2): five accepted units, robot cost 2, competent alternative cost 6, and common output payment 8 produce a 20-unit cost advantage. The incumbent service alternative remains available in failure states. A successful development program is not a license to deploy an unqualified route.

The positive signal occurs with probability \(11/40\) and yields posterior \(19/22\). The negative signal occurs with probability \(29/40\) and yields posterior \(1/58\). Source acquisition after grounding is chosen after the positive signal and declined after the negative signal.

| Policy | Current and future expected value | Increment over routine baseline |
| --- | ---: | ---: |
| Routine in both slots | 6 | 0 |
| Commit to source and grounding regardless of report | 5 | -1 |
| Ground first, acquire source only after a positive report | \(31/5=6.2\) | \(1/5=0.2\) |
| Same menu, uninformative or delayed report | 6 | 0 |
| Ground first with a perfect diagnostic | \(13/2=6.5\) | \(1/2=0.5\) |

The positive adaptive result is not obtained by assigning a bonus to the dataset. Its incremental account is

\[
\underbrace{20(19/80)}_{\text{future production gain}}
-\underbrace{4}_{\text{grounding opportunity cost}}
-\underbrace{2(11/40)}_{\text{expected source opportunity cost}}
=\frac15.
\tag{T8}
\]

A policy maximizing the probability of acquiring the new capability would always buy both batches, achieving probability \(1/4\). The economic policy acquires it with probability \(19/80\), slightly lower, while obtaining greater net value. The technical objective is a legitimate comparator; it is answering a different question. A competent static profit policy chooses routine activity. The adaptive policy improves on both only because it uses the same information at the time it becomes available.

The example also shows why positive current task revenue is a poor sufficient statistic for source acquisition. A source job can earn a positive accounting contribution and still be an unattractive use of the bottleneck after the target report.

### Joint outcomes remain joint

The binary transfer regime is one actual acquisition outcome, not two invented independent skills. If a complete new production recipe requires two jointly validated components and the program validates both with probability \(1/4\), its joint outcome law can be

\[
P(\varnothing)=3/4,\qquad P(\{1,2\})=1/4.
\]

For value table \((0,0,0,20)\), expected production gain is 5. Multiplying two marginal probabilities of \(1/4\) would instead give 1.25 and would change the economic choice. The code extends the parent's qualification-set value convention with an explicit joint law, and agrees with its independent calculation only when the law actually factorizes.

## 5. The same argument with partial value and the existing Gaussian learning technology

The all-or-nothing example makes the algebra legible, but the proposition does not require that technology. We also reuse the preceding chapter's information mechanism:

\[
S_H(x,g)=\frac{A_H}{a+x}+\frac{C}{b+g}+\rho,
\qquad
q_H(x,g)=\operatorname{erf}\left(\frac{\tau}{\sqrt{2S_H(x,g)}}\right).
\tag{T9}
\]

A source-relevance regime changes \(A_H\); grounding improves the embodiment-specific information term in both regimes. Define
\(F_H(x,g)=W_q[q_H(x,g)-q_H(0,0)]\).
This is the same scalar evaluation proxy as before, not a claim that one Gaussian error test establishes supported industrial qualification.

The scoped computation uses \(A_0=0,A_1=4,a=b=C=\tau=1,\rho=0.1,W_q=30\), the same prior and signal accuracy as above, \(c=3,s=2,g=0\). Grounding alone now has positive value. The best early-information policy still grounds first, then chooses source after a favorable report and routine work after an unfavorable report.

Its objective is approximately 6.83813. Delaying the signal while preserving the learning technology yields approximately 6.35865. Allowing two source batches or two grounding batches, rather than imposing one of each, leaves this particular optimum unchanged. These are numerical checks of a second formulation, not proofs of universal robustness.

This exercise rules out a narrow explanation of the earlier result: the early-information advantage does not depend on setting every partial technical gain to zero or simply stipulating a multiplicative \(xg\) response. It does still rely on informative grounding, a decision that can be adapted, and the stated resource/opportunity costs.

## 6. Strong objections that change the answer

### 6.1 A genuinely better specialist can win

Add a target-only route that occupies one slot, has current net contribution \(-4\), and supplies future incremental value independently of source relevance. With value 6 it is available but does not displace the adaptive route. With value 9 it gives total value 8 when combined with one routine slot, beating 6.2.

The model therefore does not mechanically prefer shared learning to a specialist. The direct route can be undertaken in either slot in this example; the solver uses a stable tie convention and reports routine first, then direct investment. Calling that tie a substantive timing prediction would be incorrect.

### 6.2 Demand expiry can reverse the preferred order

Suppose the source job and its data opportunity exist only in the first slot. With prior \(1/2\), otherwise retaining the binary example, source-first followed by grounding gives total value 10. Grounding first loses access to the source and is inferior.

The stationary interchange argument no longer applies because the same physical/data choice set is not available after the swap. The empirical distinction is observable: availability, expiration and alternative collection cost matter, not just current source and target margins. A source job should not be treated as expiring if a matched, affordable collection alternative remains available in the same window.

### 6.3 A free relevant production by-product removes the timing premium

Suppose a competent routine-production mode supplies the same usable source batch without sacrificing current contribution. Then \(k_S=0\). With optional use and retained policies, \(M(Z)\geq0\), so (T7) becomes
\[
I=\mathbb E[M(Z)]-\mathbb E[M(Z)]=0.
\]
There is no costly source-acquisition choice to avoid. Grounding can still have physical learning value, but an earlier transfer report has no acquisition-timing premium through this channel. In the exact example, setting the source margin equal to the routine margin makes both early and delayed information yield total value 7.

This is a strong comparator to the data-collection story. We must identify why the relevant labels, recovery states, permissions or target conditions require an incremental resource commitment. If ordinary production already supplies them, the original positive opportunity cost is inappropriate. No claim is made that all routine observations are irrelevant or that only human data can transfer.

### 6.4 More precise information need not justify a standalone experiment

The menu also permits a laboratory grounding experiment with a perfect diagnostic and current contribution \(-2\). It produces no customer service in that slot and yields total value 5.5 in the binary example, below the productive noisy diagnostic's 6.2.

Higher information quality is useful conditional on otherwise identical costs and effects. It is not enough when producing the information consumes a more valuable slot. Conversely, a laboratory trial can win if a productive target job is unavailable or if its information advantage exceeds its incremental opportunity cost.

### 6.5 Signal and physical transfer assumptions must be separated

A source batch may itself be diagnostic. Grounding can alter the transfer regime rather than merely reveal it. Observation quality may depend on the chosen policy, current competence, task difficulty or the operator. When either action changes the other's physical outcome or informativeness, one cannot swap their order using (T6). Return to (T3) with the actual joint transition law.

An experiment that appears more informative because it tests an easier target does not identify the proposed mechanism. Likewise, changes in intervention selection can change the distribution on which a learned policy is evaluated. Existing imitation-learning work already treats policy-induced data distributions as central. [S2]

### 6.6 No broad adverse-data conclusion follows

If additional data or information are free, optional and do not remove retained feasible plans, optimized value cannot fall. A compulsory retraining update, a dataset fee, delayed service, loss of usable rights or resource congestion changes that intervention. Our examples price acquisition and the use of scarce capacity; they do not contradict optional-access dominance.

## 7. Teleoperator prices and the timing of human work

The immediate question concerns what to collect and when. One useful comparative-static implication connects it to the user's market-price intuition.

Fix all nonwage primitives, feasible policies and observation laws. For each admissible complete contingent policy \(\mu\), let \(G_\mu\) be its expected contribution before teleoperator pay and let \(H_\mu\geq0\) be its expected discounted teleoperator time. Then

\[
J(w_H)=\sup_\mu\{G_\mu-w_HH_\mu\}
\tag{T10}
\]

is convex and nonincreasing in \(w_H\). Where it is differentiable,
\(J'(w_H)=-H_{\mu^*}\).
For \(w_2>w_1\), any optimizing policies satisfy \(H_{\mu_2}\leq H_{\mu_1}\).

**Proof.** A supremum of affine functions is convex; each affine function is nonincreasing because \(H_\mu\geq0\). Optimality at the two wages gives
\(G_1-w_1H_1\geq G_2-w_1H_2\) and
\(G_2-w_2H_2\geq G_1-w_2H_1\).
Adding yields
\((w_2-w_1)(H_1-H_2)\geq0\).
The derivative statement is the usual envelope result where the value is differentiable. \(\square\)

The result concerns **total discounted human time**, not its timing. Consider the same future accepted service delivered either with four future human hours, or by one current teaching hour plus three nonlabor cost units that eliminate those later hours. At wage \(1/2\), later manual delivery costs 2 versus 3.5 for teaching. At wage 2, teaching costs 5 versus 8. A higher wage raises current teaching from zero to one hour while lowering total hours from four to one.

This is a conditional counterexample to interpreting a high teleoperator wage as always reducing current teleoperation. It is not a claim about wages in general equilibrium. If wages change customer demand, future prices, operator quality, endogenous entry or cash feasibility, the fixed-policy-set argument must be reconsidered. It is also not a claim that every human hour substitutes for later hours: only a task-relevant learning transition can generate that effect.

## 8. Empirical connection: what has actually been observed

The public technical evidence is useful for separating objects, not for calibrating this model.

- **ThriftyDAgger**, primary paper, Section 5.1 and Table 3: its physical cable-routing evaluation reports 12/15 autonomous successes and 15/15 intervention-aided successes for the same trained method. Its intervention/action statistics are conditioned on successful episodes. That distinction makes assisted output and autonomous policy performance separate empirical variables. It supplies no customer price, full operating cost or causal dollar value per demonstration. [S3]
- **HIL-SERL**, authors' method overview: teleoperation supplies reward-classifier examples and demonstrations; online training also uses corrective interventions. These are different uses of human input, so a single count of teleoperation hours does not identify which learning channel changed. [S4]

The cable-routing table was checked both in extracted PDF text and on its rendered page 8. The counts are observations reported by the paper, not new trials executed here. The theory's priors, signal accuracies, margins and payoffs are not estimated from those counts.

### 8.1 A discriminating design

A useful test needs to separate data production, information timing and economic choice.

**Physical-learning arm.** Starting from matched retained policies, vary whether target teleoperation demonstrations/corrections enter training. Fix the allowed training budget, data rights and evaluation protocol. Evaluate autonomous performance separately from service with human assistance. Record failures, resets, monitoring and all attempted orders, not only successful episodes.

**Information-timing arm.** Conditional on the same initial target-grounding procedure, release a transfer diagnostic before or after the next source-acquisition choice. Preserve information needed for safety and operational permissions; only a research-relevant commercial/transfer report can be delayed. Allow both arms the same routine production and specialist alternatives. The mechanism predicts changes in which source batches are acquired. It does not predict that an early report directly improves a fixed trained policy.

**Joint qualification and economic mapping.** Record actual joint qualification outcomes at the complete-service level, current margins and opportunity costs, customer quantities and expiration dates, and future accepted-service gains relative to competent alternatives. Cross-task errors and qualification outcomes must be retained jointly. Marginal benchmark scores alone cannot identify the model.

**Key falsifiers.** The proposed early-information channel is absent if the report does not predict source usefulness, if it arrives after the relevant commitment, or if the enterprise cannot change its next acquisition. The stationary ordering claim is rejected when the source opportunity expires before the diagnostic, not rescued by relabeling that environment stationary.

This is a proposed experiment, not an executed robotics training run or an observed customer panel. The present executed test is an exact finite-policy baseline plus the alternative Gaussian calculation.

## 9. How this strengthens the common paper argument

The argument now has a clearer sequence:

1. The production network determines whether a technical improvement changes feasible, valuable service.
2. Source data, grounding and embodiment jointly determine the technical transition.
3. Production and human intervention determine which observations are generated.
4. Some observations change the next acquisition decision before they change a deployed policy.
5. Customer demand, scarce resources, alternatives and rights determine whether those changes are worth paying for.

The same decision links the broader roadmap. More fleet can increase exposure and congest human attention; coordination can change the cost of a useful intervention; manufacturing and embodiment choices can alter the transfer interface; customer access determines both current margin and which diagnostic states are encountered; ownership and rights determine which party captures the continuation benefit. These are locations for the existing broader models, not assumptions that every channel is already solved.

The first paper should develop this coherent argument, with the present proofs and counterexamples serving as transparent building blocks. The broader atlas retains sector/value-chain/task opportunities, typed learning relationships, finance and contracts, and manufacturing/embodiment alternatives. No original deadline or scope item is canceled, and the November 22 synthesis gate is not marked passed.

## 10. Exact continuation question

The strongest remaining gap is now **endogenous diagnostic quality under selective intervention**. We assigned the signal likelihood. In real collection, the policy decides where and when a human intervenes, so the episode distribution changes with competence, demand and operator allocation.

Next: retain the same state and objective, but derive signal likelihood and transferable learning from intervention states that are selected by the robot's own errors. Ask whether a more autonomous source fleet can reduce the supply of target-relevant corrections, and when deliberate probes, simulation or a different embodiment repair the resulting information gap. Use a matched no-intervention/corrective-intervention likelihood model and a competent safe fallback, not an assumed universal positive data coefficient or a new detached threshold exercise.

Keep the current negative results: source-only or direct specialization can win; task-price increases may saturate in operating value; demand expiry defeats an information-first ordering; and optional extra data do not by themselves reduce optimized value.

## Sources and reading boundaries

**[S1]** Maryam Farboodi, Andrew Koh and Anchi Xia, *Data-Driven Automation*, [arXiv abstract](https://arxiv.org/abs/2606.10127), [inspected v1 HTML](https://arxiv.org/html/2606.10127v1). This run inspected Sections 2/2.1, 2.2 D2-D4, Section 5 and the relevant Appendix B passages. The inherited version-label/display-date discrepancy is unresolved; no claim of equivalence to every current PDF revision. A primary-text extraction was successful after the direct HTML open failed. No new reconstruction of Proposition 6's full proof is claimed.

**[S2]** Stephane Ross, Geoffrey Gordon and Drew Bagnell (2011), *A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning*, [PMLR 15, 627-635](https://proceedings.mlr.press/v15/ross11a.html). Proceedings abstract/metadata inspected for the policy-induced distribution distinction; this run did not reconstruct the regret theorem.

**[S3]** Ryan Hoque, Ashwin Balakrishna, Ellen Novoseller, Albert Wilcox, Daniel S. Brown and Ken Goldberg (CoRL 2021; proceedings 2022), *ThriftyDAgger: Budget-Aware Novelty and Risk Gating for Interactive Imitation Learning*, [proceedings](https://proceedings.mlr.press/v164/hoque22a.html), [paper](https://proceedings.mlr.press/v164/hoque22a/hoque22a.pdf). Sections 3-5, evaluation definitions and Tables 1-3 inspected; page 8/Table 3 visually checked. No code/training replication or external-validity inference.

**[S4]** Jianlan Luo, Charles Xu, Jeffrey Wu and Sergey Levine, *Precise and Dexterous Robotic Manipulation via Human-in-the-Loop Reinforcement Learning*, [authors' project overview](https://hil-serl.github.io/); published article DOI [10.1126/scirobotics.ads5033](https://doi.org/10.1126/scirobotics.ads5033). This run inspected the project method overview and bibliographic record, not the complete experimental supplement.

The proofs above are direct derivations using conditional expectation, finite-horizon optimization, convexity and the already-used Gaussian information model. These are established mathematical tools. Their integration here is a candidate research synthesis; novelty relative to the full economics and robot-learning literatures remains unestablished.

## Reproduction

Run from this directory:

    python -m unittest -v test_teleoperation.py test_data_value.py
    python teleoperation.py --output teleoperation_results.json

The rational benchmark uses Python's Fraction arithmetic. An independent full contingent-policy enumerator integrates over true regimes and signal likelihoods without posterior updates or Bellman recursion. The Gaussian alternative uses the standard-library erf and should be compared within declared numeric tolerances. No GPU, external data access, model training or additional worker is required.

See TELEOPERATION_VALIDATION.json for the actual executed checks and artifact hashes, TELEOPERATION_PROOF_LEDGER.md for claim scope, TELEOPERATION_EVIDENCE.json for the typed source slice, and the separate TELEOPERATION_EXERCISES.md / TELEOPERATION_SOLUTIONS.md for learning material.

