# Identification hierarchy for source data, grounding, embodiment and endogenous qualified production

**21 November 2026 | Continuation of *When Capabilities Become Production*, November 22 Models A/B.** This is a structural correction and formal synthesis of the same research question, not a new numbered problem. It uses established randomization, potential-outcome and dynamic-policy results; scientific originality and actual robotics evidence are not asserted.

## 1. Why the preceding cross-arm copula is not always the research bottleneck

The preceding [cross-arm qualification analysis](JOINT_QUALIFICATION_CROSS_ARM_SUPPORT_AND_DEMAND.md) sharply bounds a latent same-unit qualification response law across R, S, G and SG under unverified pathwise monotonicity or modularity. Those bounds matter if SG is **not actually evaluated**, if one wants a *casewise* nonregression guarantee, or if a single target's potential outcome under alternative intervention arms is required. However, a different and economically central claim follows:

> **An ex ante choice among fully tested S, G, SG and E programs does not require identification of the cross-world copula of individual qualification outcomes. It requires each program's own joint distribution of original-buyer demand, qualified complete-service execution, resource displacement, prices and settlements.**

This is not merely semantic. A comparison of separately randomized whole learner–operator–buyer programs can identify program-average paid production even when we cannot tell which particular robot task would improve under S rather than G. Conversely, even *perfect* marginal task-accuracy and separate buyer-demand evidence do not identify a program-average paid-service contribution when their within-program coupling is unknown. The priority for the November 22 argument is therefore to distinguish **within-program economic coupling**, **cross-program potential-response coupling**, and **dynamic data/market transitions**.

S means newly available, lineage-audited and legally reusable source episodes; G-train means target-grounded training or alignment of the existing archive; SG means their budget-controlled combination; G-observe is an *additional predecision signal* for a fixed trained learner and is not interchangeable with G-train; E changes physical embodiment/recipe capacity; R is an existing retained and physically admissible control policy. Field successes, failures/recoveries, teleoperation, simulation, synthetic rollouts, public pretrained inputs and production-generated trajectories remain distinct origins with rights, selection and compute costs. A dataset added to the firm's option set is not the same intervention as mandatory consumption of the dataset in training.

## 2. Common economic environment

Index complete **interference-closed** research units by c: a unit must encompass the mutually dependent customer order cohort, robot fleet, operator pool, integrator, dispatch/production network and the learner checkpoint/shared-weight exposure relevant to its outcomes. Interference *inside* that unit is allowed; between units it must be absent or represented by a predeclared exposure mapping. An individual order or source episode is generally the wrong randomization unit.

Let W_c be eligible preassignment state including target tasks, predeclared offered buyer population, site/device/rights and resource covariates. Let Z_c range over physically approved whole-program interventions. For program z, define Y_c(z;pi_z) as **all** net original-customer accepted/settled contribution from its predeclared production/dispatch/continuation rule pi_z over the horizon, including nonpurchase, failures, refunds, customer diversion, operator displacement, outside customer alternatives and all signed physical constraints. Prices, demand composition and arrival intensity *may respond to z*. Denote incremental *non-double-counted* investment/rights/training/manufacturing costs K_z(W_c). A consistent objective is

\[
\mu_z=\mathbb E[Y_c(z;\pi_z)-K_z(W_c)],\qquad z\in\mathcal Z_{\mathrm{approved}}.
\]

For a multistage program, Y includes current accepted contribution and the discounted future contribution realized under the **specified continuation** pi_z. Nothing called a separate data premium may be appended to Y. When future continuation will be reoptimized, the policy evaluated must include that reoptimization and possess sequential experimental support.

The earlier Model A table remains the within-program optimized production operator
\[
F_z(q,d,N)=\max_{a\in\mathcal A_z(q,d,N)} C_z(a;q,d,N),
\]
with legally signed recipes, accepted customer work and scarce physical/organizational resources. If a specific environment's qualified state has two services, its fixed-demand expansion r+a p_A+b p_B+\kappa h is still correct. **But** if the entire original buyer demand/resource law changes with z, treating those four F cells as invariant across arms is an *additional transport assumption*, not an implication of learning.

## 3. Proposition: program-value identification needs no cross-world joint law

**Proposition (signed whole-network program means).** Suppose (i) the eligible network-unit population and W distribution are specified *before* assignment; (ii) randomized assignment or justified conditional exchangeability gives
\[
Z\perp \{Y(z;\pi_z):z\in\mathcal Z\}\mid W;
\]
(iii) every program to be compared has positive conditional assignment probability e_z(W)>0 on the target W support; (iv) consistency and the declared interference/exposure closure hold; (v) the observed complete Y records accepted and settled original buyer contribution, signed resources and follow-through at the same horizon; and (vi) policy pi_z and its prices/dispatch/continuation are exactly the programs assigned. Then for each supported z,
\[
\boxed{\mu_z=\mathbb E_W[\mathbb E(Y\mid Z=z,W)-K_z(W)].}
\tag{1}
\]
All pairwise average investment rankings and the **factorial economic complement**
\[
\boxed{\Delta_{S,G}\mu=\mu_{SG}-\mu_S-\mu_G+\mu_R}
\tag{2}
\]
are identified if all four programs are supported. Equations (1)–(2) do **not** require identifying any same-unit joint distribution of (Y(R),Y(S),Y(G),Y(SG)) or imposing pathwise monotonicity, qualification modularity, independent tasks or fixed demand.

**Proof.** Under consistency, the observed Y equals Y(z;pi_z) for a unit assigned z. Conditional exchangeability makes its conditional distribution the z potential-outcome distribution at the same W. Average over the common **preassignment** W population and subtract the observed/declared program cost. The linear contrast (2) follows by subtraction. At no point does the proof condition on another program's unobserved outcome for the same unit. This is standard randomized-policy identification. QED.

**Important scope:** Randomizing a single task, data *episode*, or robot within a common learner fleet does not deliver (1) if shared weights, operator capacity or buyer substitution connect those units. If commercial activity contaminates other target cohorts, the unit must be enlarged or exposure mappings justified. A signed robot safety policy cannot be assumed merely from a formal estimand. Conditioning on buyer acceptance observed *after* treatment creates selection; original eligible offered orders, nonpurchases and displaced work are in the denominator.

**Conditional targeting.** If W is observed before choosing programs and valid across supported arms, a W-conditional rule d(W) has identified value
\[
V(d)=\mathbb E_W\left[\sum_z{\bf1}\{d(W)=z\}\{\mathbb E(Y\mid Z=z,W)-K_z(W)\}\right].
\tag{3}
\]
Learning the **distribution** of individual benefits Y(z)-Y(z') is different; it remains unidentified without cross-world assumptions. Equation (3) does not license choosing on a post-intervention report available under only one arm without modeling its generation.

## 4. Counterexample: same arm averages, different individual complementarity

Let an unobserved target type U be an equally likely binary variable, and let potential *binary normalized paid-service success* under (R,S,G,SG) have either of two response laws:

- **Common-type law:** (U,U,U,U).
- **Parity-type law:** (U,1-U,1-U,U).

Under **both** laws every arm succeeds with probability 1/2 and the population S×G interaction in (2) is exactly zero. Under the first law the individual factorial contrast Y(SG)-Y(S)-Y(G)+Y(R) is **zero for every unit**. Under the second it is −2 or +2, equally likely. The arm-average production choice is the same; individual response synergy and nonregression are not. Randomized assignment to separate whole units can identify the former, not the latter. Requiring a cross-arm copula before accepting a valid **average** production contrast would therefore overstate the identification problem.

This example contains no actual robots and should not be read as evidence that source data and grounding are technically substitutable in the field.

## 5. What *does* require a joint distribution: buyer demand and co-qualification **within an arm**

Suppose the same SG program yields service-A and service-B qualifications Q_A and Q_B, each with probability 1/2. A hypothetical original buyer buys a legally signed end-to-end bundle contributing 12 normalized units only if both are qualified. SG's program cost is 1; an independently supported E alternative returns net 4.

In **concordant SG** units, (Q_A,Q_B)=(0,0) or (1,1) with probability 1/2 each. SG net is 12(1/2)-1=5, so SG wins. In **discordant SG** units, outcomes are (0,1) or (1,0), also equally likely. Both qualification marginals remain 1/2, but SG net is −1, so E wins. This is a **within-SG** missing-copula problem, not an unobserved correlation between what S and G would each have done to a single unit.

Without paired SG qualification evidence, the sharp Fréchet interval is h_SG∈[0,1/2], and the SG net interval is [−1,5]. If paired SG complete-service qualification is measured on the correct unit and the original buyer's full signed production payoff table is actually identified under SG, its program value can be estimated without the S/G/R cross-world response law. If SG has never been run, even complete R/S/G evidence cannot determine its full policy response *unless* experimentally justified structural learning/market restrictions are imposed. The earlier monotone [1/4,9/20] and modular [3/10,9/20] conditional examples are legitimate **extrapolation bounds** under their stipulations, not obligatory constraints for an observed SG arm.

## 6. Production-created data turns the *within-arm* question into a dynamic one

Let H_t record original eligible customer orders and refusals, gross/net settled contribution, qualified physical service, operator/network occupation, source episode family and modality, licensed data rights, learner version, and retained admissible old policy. A production policy affects both current customer work and the distribution of future H. Under sequentially exchangeable and positive (possibly cluster-randomized) interventions, the two-date value of a predeclared adaptive policy pi=(pi_0,pi_1) is identified from **within-policy history/transition kernels**:

\[
V(\pi)=\mathbb E_{H_0}\sum_{z_0}\pi_0(z_0\mid H_0)\int
 P(dH_1,dY_0\mid H_0,z_0)
 \sum_{z_1}\pi_1(z_1\mid H_1)
 \int P(dY_1\mid H_0,z_0,H_1,z_1)
 [Y_0+\beta Y_1-K_0-\beta K_1].
\tag{4}
\]

Here costs must be recorded with their actual time/resource scope; conditioning on a post-treatment state for a direct-effect claim is *not* the same exercise as evaluating the policy in (4). A production-generated sample that cannot legally be retained for training is not an available state-transition input. The kernels must represent shared fleet/learner, operator and buyer interactions, not independently multiplied task marginals.

A minimal synthetic warning: production-generated rights-cleared useful data D and future accepted qualified sale Q each have marginal probability 1/2. If future contribution 8 requires both D=1 and Q=1 and the licensed data program costs 1, the program contributes 8Pr(DQ)-1. Under joint probability 1/2 it yields 3, beating a hypothetical E alternative net 1; under joint probability 0 it yields −1, losing. Identical marginals cannot decide. **This observational joint association is not proof that D caused Q**; determining the effect of data on learning needs an actual randomized or otherwise defensible retention/training/use intervention. Correlation across data genealogy and original buyer quality can reflect environmental selection.

**Free option theorem (preserved).** If new licensed data are freely *optional*, all old checkpoints, qualified service and rights/compute/capacity policies remain feasible with exactly the same costs and environment, the feasible optimization set expands and maximized value weakly increases. Forced training, curation expenditure, compute diversion, altered legal rights, shifted buyer demands and unsafe controller loss violate those premises and can produce negative observed effects. Do not reclassify the negative effect of an imposed update as negative value from a free optional archive.

## 7. Identification frontier, nonparametric comparison and acquisition choice

The feasible-investment decision is not identified by a single accuracy table. At minimum distinguish:

| Evidence available | Economically identifiable object | Not identified without more |
|---|---|---|
| Per-arm separate qualification and market marginals | Bounds on within-arm paid co-production under stated feasible table | Joint buyer-Q/operator-resource payoff law, program ranking |
| Per-arm paired original-buyer orders, joint qualifications and net settlement with signed policy | Arm-average gross paid contribution, conditional on complete market support | Cross-arm casewise uplift; unsupported program E/SG |
| Randomized complete R/S/G/SG/E units with same target population and horizon | Ex ante whole-program comparison and population economic S×G interaction | Individual response copula, optional future reoptimization outside support |
| Stagewise randomized or justified sequentially exchangeable production/data/learning choices | Value of supported adaptive policies including future data inside continuation | Off-support embodiment, illegal data reuse, causal mechanisms not intervened on |
| Only R/S/G tested, not SG/E | Conditional bounds or assumptions-driven model extrapolation | Nonparametric SG/E investment value |

For program z with jointly feasible identified-value uncertainty set M, a robust claim that z is preferable to every rival requires
\[
\inf_{m\in M}(\mu_z(m)-\mu_j(m))\ge0\quad\text{for all }j.
\tag{5}
\]
Checking lower and upper *separate* marginal intervals is a convenient sufficient condition but may be conservative when outcomes, buyer demand and network resources are coupled. **Do not pay to measure the S/G cross-world response distribution if the actual decision can instead be resolved with permitted whole-program arm measurements.** When some arms are economically or physically inaccessible, restrict claims to supported menus or explicitly stated partial identification.

The high-value *next* research step is a prospective choice of which **lawful within-program data** would discriminate S, G, SG and E in complete customer production, at fixed eligible-market and physical-network scope. Technical episode genealogy remains essential for learning mechanisms and generalization, but is not a substitute for accepted paid service. A design must fix accepted-update/compute budgets, report both program-choice intent-to-treat and trained-learner per-protocol effects, follow original eligible buyer outcomes, retain failures and refusals, and record actual displaced paid outside work. It must also account for manufacturing lead time, supplier constraints, ownership and cross-end-market production network spillovers when E is compared.

## 8. Nearest prior art and honest contribution

This proposition restates established potential-outcome/random-assignment identification and the g-formula at an intervention granularity appropriate for entire robotic production networks. It uses standard Fréchet joint-event bounds, potential-outcome coupling, Bayesian decision sufficiency, and finite-horizon dynamic-policy evaluation. See: Holland (1986), *Statistics and Causal Inference*, JASA; Rubin (2008), *For objective causal inference, design trumps analysis*, https://arxiv.org/abs/0811.1640; Mealli and Zigler (2019), *Causal inference with interfering units for cluster and population level treatment allocation programs*, https://doi.org/10.1111/biom.13049; Lee, Zeng and Hudgens (2022), *Efficient Nonparametric Estimation of Stochastic Policy Effects with Clustered Interference*, https://arxiv.org/abs/2212.10959. DDA (Farboodi, Koh and Xia, arXiv v1, posted 8 June 2026, https://arxiv.org/abs/2606.10127) already analyzes endogenous data generation, spillovers and future value; its §5 and Appendix B are **not** novelty claims here.

Our **candidate programmatic contribution** is the consistent empirical interface joining heterogeneous source interventions, *whole* learner qualification, original-market demand and net captured production, optional fallback and embodiment, plus dynamic data feedback. It remains an unverified research program rather than newly demonstrated mathematical or empirical science. All worked values above are strictly synthetic; no benchmark percentage is converted directly into money.

**November 22 gate:** the clarified Models A/B argument, logical estimand hierarchy and exact finite examples are ready for review. Real arm-randomization/signed physical/network access, original customer settled order data, cross-end-market demand, quantitative official BEA/BLS production flows, independent scientific novelty review and full-repository CI remain absent. The scientific gate is OPEN; the December 25, 2026, 23:59 America/New_York final target is unchanged.
