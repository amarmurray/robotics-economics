# Regime-conditioned qualification as information: target grounding versus embodiment flexibility

**20 November 2026. Continuation of the same November 22 Models A–B review in When Capabilities Become Production.** This chapter strengthens [joint qualification timing](JOINT_QUALIFICATION_TIMING_AND_DATA_VALUE.md), not a new research question. It asks whether heterogeneous source learning creates usable embodiments for the *original buyer's complete qualified service*, and how source-generated qualification information changes the incremental value of target grounding and post-report embodiment selection. All contribution values and physical approvals below are **hypothetical**. No live buyer, receipt, signed robot/operator policy or field source-transfer effect is inferred.

## 1. Sequence and economic objects

One original customer regime Θ is A with probability π and B otherwise. Source training yields an **observed before commitment** paired qualification vector Q=(Q_A,Q_B); q=P(Q=(1,1)) is a development-run probability, not the product of separate pass rates. A passive predeployment target observation Y∈{A,B} has symmetric calibrated accuracy α∈[1/2,1], with P(Y|Θ,Q)=P(Y|Θ); **this conditional kernel restriction is essential**, not implied by marginal report accuracy. Retained, independently admitted complete policy R contributes 2 in either regime. Individually qualified complete policies E_A/E_B contribute 4 if the original buyer's regime matches and 0 otherwise. These amounts *already represent accepted complete service, attributable receipts, variable resource use and captured contribution* under one unchanged lawful original offer. No success-rate percentage is priced as dollars.

Policy F can select either physically qualified specialist **after Y** (requiring independently signed flexibility and switching). Policy L must install one specialist **after Q but before Y**, then may use an independently admissible R *before any unsafe attempt*, not a presumed postfailure rescue. Both choose R whenever legally and physically permitted. Their only incremental difference occurs in Q=(1,1): elsewhere neither has a second qualified body to select. Embodiment lead time, switching rights, operator capacity and original buyer purchase are feasibility constraints; none may be granted merely by writing a maximum operator.

Define x=P(Θ=A,Q=(1,1)); in Q=(1,1), demand B occupies q−x. This x is the **regime alignment of joint source qualification**, distinct from its frequency q. Prior [joint qualification timing](JOINT_QUALIFICATION_TIMING_AND_DATA_VALUE.md) imposed Q independent of Θ, making x=πq; that is not generally valid for production-selected training data, especially when the original demand regime shapes field exposures.

## 2. Conditional switching theorem: qualification itself is informative

**Proposition (fixed complete-service payoffs and calibrated signal).** Under the preceding assumptions, the ex ante gross flexible-minus-locked original production contribution is exactly

    D(F,L) = [ (2α−1)q − 2|x−q/2| ]_+,

where [z]_+=max(z,0). This is conditional expected value **inside** the optimized production/continuation objective, not an extra data asset added to J. It has no universal sign for a *source-induced change* because X may change q, x, the observation kernel and the feasible architecture simultaneously. It is always nonnegative for the same fixed Q law and genuinely nested F/L policy sets.

**Proof.** Restrict to the joint-qualified event C. For y=A, the unnormalized state-mass difference between A and B is

    d_A = P(C,Θ=A,Y=A)−P(C,Θ=B,Y=A)
        = x−(1−α)q.

For y=B it is d_B=x−αq. On any observed y, relative to R, installing E_A has expected *unconditional-mass* contribution increment 2d_y, and E_B has increment −2d_y; abstaining contributes zero. Hence F's incremental expected contribution over R across C is 2(|d_A|+|d_B|). L chooses its installed body before Y but may abstain after Y, so its incremental contribution is 2 max{(d_A)_++(d_B)_+, (−d_A)_++(−d_B)_+}. Their difference is

    2 min{(d_A)_++(d_B)_+, (−d_A)_++(−d_B)_+}.

For α≥1/2 the two differences have opposite signs exactly when (1−α)q≤x≤αq. The difference then becomes 2 min{x−(1−α)q, αq−x}; otherwise it is zero. Recenter around q/2 to obtain the formula. Single-qualified and unqualified histories cancel between F and L. QED.

**Interpretation.** Target grounding Y is valuable for *switching bodies* only if its possible realizations can overcome the prior about the buyer's regime already revealed by the observed development outcome Q=(1,1). A source-development outcome can both enlarge the technical menu and itself act as a demand-correlated signal. A calibrated α alone and the joint-qualification frequency q do **not** determine the value of additional grounding once source-selection endogeneity is admitted.

If Q and Θ are independent, π=1/2 and x=q/2, the identity collapses to D=(2α−1)q, exactly recovering the earlier bq formula. It is not a competing result. With the same π=1/2, q=2/5 and α=3/4, a balanced coupling x=1/5 gives D=1/5, whereas x=7/20 gives D=0. Fix, in both worlds, the *entire unconditional* Q law P(11,10,01,00)=(2/5,1/5,1/5,1/5). Both couplings are feasible: in the balanced world assign Θ=A masses (1/5,1/10,1/10,1/10); in the skewed world assign (7/20,1/20,1/20,1/20). All four unconditional qualification cells, π and α match, but the economically relevant value of flexibility differs. The worlds are **not** equivalent if Q and Y are paired and measured; that is the next identification route.

## 3. Sharp partial identification without a demand–qualification panel

Suppose original-customer regime frequency π and the same-run Q distribution are known, but qualification histories have not been paired to Θ. Since q is known, all feasible couplings satisfy

    x∈I=[L,U], L=max(0,π+q−1), U=min(π,q).

These Fréchet limits are **sharp even if the other three unconditional Q cell masses are known**: allocate π−x of A mass arbitrarily among the remaining Q cells, whose aggregate capacity is 1−q. Conversely any feasible joint law must obey the displayed limits. Let b=2α−1 and distance(t,I)=min_{s∈I}|t−s|. The sharp gross flexibility premium range is

    D_low=[bq−2 max{|L−q/2|,|U−q/2|}]_+
    D_high=[bq−2 distance(q/2,I)]_+.

**Proof.** The theorem makes D a tent-shaped continuous function of the one unidentified coupling x. Its minimum on a compact interval occurs at an endpoint, and its maximum at the projection of the center q/2 into that interval. Every x∈I is attainable by a valid four-cell coupling, so both extrema are sharp, not merely loose worst-case certificates. QED.

Examples with π=1/2, α=3/4: q=2/5 implies D∈[0,1/5], which cannot establish a positive return to *costly* F; q=4/5 implies D∈[1/5,2/5], so a hypothetical once-counted flexibility cost below 1/5 is robustly covered under all admissible couplings. The cost is a production/embodiment commitment, not a data premium. Higher q by itself is not an economic monotonicity theorem across different learning policies: x and feasibility may change alongside it.

## 4. Target observation as a *measurement*, not an automatic production receipt

If Y is passively recorded on the same eligible training/customer parent population and its **conditional** kernel is independently calibrated, define m=P(Q=(1,1),Y=A). Then

    m=(1−α)q+(2α−1)x.

For α>1/2, x is point identified by x=[m−(1−α)q]/(2α−1). If α=1/2 the report is uninformative and leaves x unidentified. Sample selection, a source-specific observation kernel, reporting after the embodiment decision, demand changes induced by the observation/menu, or Q-dependent calibration invalidate the naive inversion. If Θ is directly observed, the same-run paired estimate of x is preferable. Target observation may improve regime inference; it neither establishes whole-policy physical admission nor fills missing *customer purchases and paid receipts*. If Y changes the offer, its buyer response belongs to that distinct treatment version.

**Design implication:** the highest-value incremental datum may be the *joint pairing* of source-qualification outcome, predecision target regime evidence and accepted original production, not another unconditioned batch of teleoperation or field trajectories. This is a conditional information/experiment-design proposition, **not** an estimate of the commercial value of any particular dataset. Source types remain distinct: production trajectories, safety/failure/recovery logs, human teleoperation, simulation, synthetic data and public/pretrained weights have different provenance, selection, rights and transfer channels.

## 5. General finite production-value extension when whole policies lack market support

The two-specialist formula assumes complete buyer contributions r(a,Θ) are known and F/L fully admitted. For the actual November 22 gate, neither is assured. Retain the full original buyer–robot–operator cluster as the unit and let H be observed development/qualification history, Y a legally and physically admissible signal, Θ latent original demand state, and A(H,Y) the **set of signed complete network policies**. Suppose the finite coupled law μ(H,Θ) belongs to a nonempty convex polytope C of restrictions genuinely supported by original-parent data. A known stable report kernel κ(Y|H,Θ) yields

    W(μ;r)=Σ_{H,Y} max_{a∈A(H,Y)}
                       Σ_Θ μ(H,Θ) κ(Y|H,Θ) r(a,Θ).

This is the existing optimized captured-contribution V for a finite conditional policy menu, not a second continuation reward. It is the maximum of a **finite collection of linear functions** L_f(μ), one for each complete contingent selection rule f(H,Y). Therefore

    W_low = min_{μ∈C, t} t, subject to t≥L_f(μ) for every allowed f;
    W_high = max_f max_{μ∈C} L_f(μ).

The former is a linear program (epigraph), and the latter a finite family of linear programs. Both are sharp *relative to the stated attainable restrictions C and fixed payoff table r*. An original customer demand/receipt row never observed for an admissible policy cannot be silently set to a benchmark accuracy, a warranty-modified survey response or another vendor's transaction. If independently defensible jointly attainable componentwise receipt/contribution bounds ℓ(a,Θ)≤r(a,Θ)≤u(a,Θ) form a **rectangular** payoff set, use ℓ for the lower envelope and u for the upper. Actual market-menu cross-equation constraints require a joint set, not this shortcut. Without defensible r/C/κ bounds, the numerical identified set is not determined.

Policies X not independently signed as safe must be **excluded** from A. The old policy's genuine optional availability protects optimized gross policy-set value only with unchanged resources, rights and original offer; it does not imply casewise physical regression protection. Deliberate acquisition, production-generated data, embodiment build and later validation are decisions/state transitions inside Bellman J with costs, time and opportunity effects accounted once.

### Comparing acquisition interventions rather than observational mixtures

For distinct acquisition actions d∈{additional source X, target grounding G, embodiment E, retained production R}, the relevant joint law is **interventional** μ_d(H,Θ), with its own source-to-qualification kernel, signal kernel, qualified policy menu, original-customer buyer response and costs. Conditioning on which customers happen to generate routine field data generally does not estimate μ_d under deliberate training or a new offered service. It requires randomized or otherwise defensible matched allocation/transport at the **whole original buyer–robot–operator unit**. The sharp coupling bounds above concern a fixed d, not a free causal comparison between source portfolios. When a policy changes the original offer, the commercial response table is version-specific. Compare the resulting *complete* Bellman J across interventions; keep the baseline R optional where genuinely feasible, subtract training/curation/rights/hardware resources once, and do not add a second continuation "data price" on top of optimized future production. Endogenous collection can alter future qualification support and the buyer regime through network feedback; the finite construction is a disciplined one-period diagnostic, not an assumed stable long-run equilibrium.

## 6. Prior art, falsification and next same-gate obligation

This construction is elementary Bayesian decision theory, a Fréchet coupling problem and finite robust optimization; it is **not independently established scientific novelty**. Close foundations: Farboodi–Koh–Xia, *Data-Driven Automation* (June 2026, https://arxiv.org/abs/2606.10127), already values endogenous future task data and complementary spillovers; Brooks–Frankel–Kamenica, *Comparisons of Signals* (AER September 2024, https://doi.org/10.1257/aer.20230430), emphasizes the *joint* statistical relation of signals and other information; ReMix (CoRL/PMLR 2025, https://proceedings.mlr.press/v270/hejna25a.html) and DataMIL (ICLR 2026, https://proceedings.iclr.cc/paper_files/paper/2026/hash/033d9e8dbbbc0ad90e59222cf1db0fc2-Abstract-Conference.html) examine technical training-data selection, not original buyer payment for jointly certified complete policies. This is an original conditional *synthesis/application in this manuscript*, not a claim of a new statistical theorem.

The [unpopulated prospective test](REGIME_COUPLING_PROSPECTIVE_VALIDATION.md) fixes the customer/menu/version, source-run pairing, report timing, approved hardware and operator recovery, original service acceptance and receipts, and the exact Q–Y/Θ joint statistic needed to discriminate the two coupling worlds. [Exact rational executable](regime_option_check.py) and its [record](regime_option_results.json) check the displayed equalities and sharp envelopes, not physical safety or empirical truth. No original-customer dataset, signed full-network F/L, measured source effect, numerical BEA interindustry cell, full repository CI or independent scientific novelty review was obtained. November 22 scientific acceptance remains **OPEN**. The **next exact question** is whether any defensible original-parent paired Q, predecision Y/Θ and signed whole-policy accepted/paid receipt support actually shrinks the same regime/market identified set enough to rank source X, grounding G and embodiment E after real costs; if not, report nonidentification rather than another synthetic parameter variation. Theory remains majority through December 6, and the final deadline is December 25, 2026, 23:59 America/New_York.
