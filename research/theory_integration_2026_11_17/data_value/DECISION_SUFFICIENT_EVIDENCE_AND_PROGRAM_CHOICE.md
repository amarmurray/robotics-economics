# Decision-sufficient evidence for source-grounding versus embodiment investment

**21 November 2026 | Same *When Capabilities Become Production* Models A/B program.** Continuation of [program-value identification](PROGRAM_VALUE_IDENTIFICATION_HIERARCHY.md). The immediate question is **which permitted observation changes the economically justified S/G/SG/E choice**, rather than which benchmark improves. Results below are exact *conditional* decision-theoretic constructions. They are not new robots, observed paid returns, a finite-sample experiment, or demonstrated mathematical novelty.

## 1. Production environment and estimand

Preserve the signed operator/robot/customer network, original eligible buyer cohort, intervention budgets, data rights, retained admissible R controller, and the *entire* period-0 plus policy-consistent continuation payoff. For a legally admissible program z, let J_z equal mean original-buyer **accepted, settled and net** contribution, including resource displacement, nonpurchases, refunds, manufacturing/access/training costs and production-generated future data *inside* the specified continuation. Earlier optimized production F_z(q,d,N) remains the operator mapping competence, joint qualification, buyer orders and scarce physical/organizational resources into J_z. New source episodes S, target G-train, their combination SG, target G-observe as a separately priced information procedure, and embodiment E are distinct interventions.

Focus *conditionally* on SG versus E after other programs have been screened and an R fallback remains legal. The synthetic network has one paid complete original-buyer bundle of normalized contribution 12 when (i) the complete signed service is jointly qualified, (ii) a buyer actually accepts an original eligible offer, (iii) scarce operator/robot service can be delivered, and (iv) the receipt settles without reversal. Write k for the **joint event probability**, not task accuracy or just Pr(Q_A=Q_B=1). If the SG program costs 1, then

\[
a=J_{SG}=12k-1,\qquad 0\le k\le\tfrac12.
\tag{1}
\]

Thus a∈[-1,5]. The alternative E has complete net contribution b∈[3,5], conditional on its own approved recipe/market/cost envelope. The interval for E is a deliberately **partially supported program** uncertainty set, not a measured embodiment result. The uncertainty set M=[-1,5]×[3,5] is rectangular: it allows all combinations of economically possible arm means, not statistical independence of individual treatment potential outcomes. These toy intervals are never calibrated by benchmark success percentages.

If a retained or other approved program exceeds either candidate in some state, expand the action menu; the two-arm calculation is then only a subproblem. An E with no physical authorization is an analytical comparator, not an available deployment.

## 2. A general observation-selection proposition

Consider two approved complete programs A and B with net contributions a∈[a_L,a_U], b∈[b_L,b_U], and a closed rectangular uncertainty set. A feasible decision can allocate the ex ante fraction p of **independent interference-closed customer/learner/operator clusters** to A, 1-p to B. This mixed policy cannot be interpreted as fractionally testing an unsafe robot or splitting shared weights. If only one indivisible network can be selected, restrict p to {0,1}.

Define ex post absolute regret against the better feasible program as

\[
r(p;a,b)=\max\{a,b\}-[pa+(1-p)b].
\tag{2}
\]

Let u=(a_U-b_L)_+ and v=(b_U-a_L)_+. **Proposition (rectangular minimax regret):**

\[
\boxed{R_{\rm mix}(M)=\frac{uv}{u+v},\quad p^*=\frac{u}{u+v};\qquad
R_{\rm pure}(M)=\min\{u,v\}.}
\tag{3}
\]

Use R=0 if u+v=0. A perfectly revealing but costly A-program observation partitions M by a; after observing a, its residual randomized regret is

\[
R_A(a)=\frac{(a-b_L)_+(b_U-a)_+}{(a-b_L)_++(b_U-a)_+},
\tag{4}
\]

with the zero-denominator convention, and the robust **ex ante residual** is sup over a∈[a_L,a_U] of (4). Observing exact b analogously yields

\[
R_B(b)=\frac{(a_U-b)_+(b-a_L)_+}{(a_U-b)_++(b-a_L)_+}.
\tag{5}
\]

The observation can always be ignored; hence a free perfect observation weakly reduces minimax regret. The reduction R(M)-sup R_A or R(M)-sup R_B is **not** Bayesian expected value of sample information, physical learning gain or extra cash from data. An observation cost c is compared with that reduction only if paid in the *same normalized original-customer contribution units* and the measurement does not alter the deployment market, rights or feasible program set. No information dividend is appended to J.

**Proof.** At a≥b, r=(1-p)(a-b) with rectangular supremum (1-p)u. At b≥a, r=p(b-a) with supremum pv. Their maximum is minimized by equalizing them, p=u/(u+v). A pure action has worst regret u if selecting B and v if selecting A. After a noiseless exact-arm report, simply substitute a_L=a_U=a in the same result; likewise for B. Each maximizer is attainable at a rectangle corner or a report value within a compact interval, giving sharpness. QED. This is standard zero-sum treatment-choice/minimax-regret algebra, not a novel theorem.

A more general *decision-sufficiency* statement follows: on any post-observation identified set C⊆M, an action is uniformly optimal iff its gap against every competitor is nonnegative throughout C. An observation cannot justify uniform dominance if the posterior set contains two admissible worlds with opposite rankings. For a nonrectangular joint resource/market response polytope use its genuine feasible vertices, not separately maximized interval endpoints. For stochastic finite-sample tests one must optimize over their entire sampling kernels; (4)–(5) are **perfect-oracle upper benchmarks**, not sample-size guarantees.

## 3. Same synthetic program, different observation types

In (1), first consider an *idealized exact observation of k including paid original-buyer outcomes* (equivalent to an exact revelation of a), versus an idealized exact whole-E-program net-outcome observation (revelation of b). The exact results are:

| Observable before commitment | Worst randomized regret | Worst deterministic regret |
|---|---:|---:|
| No observation | 3/2 | 2 |
| Complete SG original-buyer joint-paid outcome a | 1/2 | 1 |
| Whole-E-program paid contribution b | 4/3 | 2 |
| Both exact means | 0 | 0 |

For A-observation, when 3≤a≤5, R_A(a)=(a-3)(5-a)/2, maximized at a=4 with value 1/2; for a≤3 the E program uniformly dominates. For B-observation, R_B(b)=(5-b)(b+1)/6, maximized at b=3 with value 4/3. With no test, p_SG^*=1/4 and regret 3/2. In this *specific* uncertainty structure, observing the complete SG paid-production joint event has a larger robust decision benefit (1) than observing E alone (1/6), even though E is a credible competitor. The former is favorable only if its cost is below 1, the latter only if its cost is below 1/6; SG measurement is preferred between the two if c_SG-c_E<5/6. These are test design inequalities under stipulated uncertainty/cost comparability, not predicted dollars, sample costs or permission to run interventions.

**Crucial negative result: paired technical qualification alone is not the first observation in the table.** Let h=Pr(Q_A=Q_B=1), and let C represent actual buyer willingness, deliverable operator access and successful settlement. k=Pr(Q_A=Q_B=1,C=1). With h=1/2, one can choose the conditional buyer/settlement distribution so k takes any value in [0,1/2]. Thus revealing h *perfectly* can leave the full a∈[-1,5] uncertainty and the original 3/2 randomized worst regret. At other h the bound k≤h may help, but **without coupling evidence there is no strictly positive guaranteed minimax-regret improvement** in this example. Buyer willingness and qualification can each have marginal probability 1/2 while k=1/2 (concordant) or k=0 (discordant). Then complete SG net is 5 or −1 and its ranking against a hypothetical E with b=4 reverses. The technical distributions and buyer-demand marginals are identical. Qualification-only correlation, paid-only selection and benchmark percentage translations cannot substitute for the original eligible offered-order joint ledger.

This contrast supplies the prospective choice: among permitted measurements, prioritize a report linking **the same complete qualified recipe, eligible buyer demand, physical operator capacity, refusal/recovery, paid settlement and subsequent data rights** before adding another marginal skill score. Whole-arm trial comparisons are sufficient if each fully supported arm's *actual* original-buyer net outcome can be measured. Cross-world individual copulas are unnecessary for those mean comparisons; within-arm production-response coupling remains indispensable when only proxies are measured.

## 4. Interpretation, limitations, and empirical discrimination

The paired complete SG observation is strictly a *logical information experiment*: even if signed SG operation is feasible, sampling estimates its mean with error, prices/market demand can respond to assignment, one buyer's purchase may displace another, and rights/learning/admission may change future outcomes. Finite trial design needs cluster-level e_z(W)>0 on the relevant W population, a fixed original offered-order cohort, confidence/robustness treatment, signed physically approved controllers, learner checkpoint/version and interference closure. The ideal perfect E report is even less available if E has no embodiment production/approval. If tests themselves generate useful field/teleoperation/failure data or alter manufacturing capacity, their physical **production/training** effects must be evaluated inside the adaptive horizon, not as separate "information gains" above J.

An alternative market/capacity structure changes the sign and size of resource complementarity κ, so 12k may no longer be the right F table. The opportunity set may be nonrectangular; market uncertainty may be Bayesian rather than adversarial; safe randomization across independent clusters may be impossible. Each change requires recomputation, not reuse of the numerical theorem. Demand can react to S/G/E interventions and can be endogenous within the program; original buyer recruitment, procurement parent and prices must be fixed *as an estimand*, not assumed behaviorally invariant.

The closest prior art is Charles F. Manski, ["Statistical Treatment Rules for Heterogeneous Populations"](https://doi.org/10.1111/j.1468-0262.2004.00530.x), *Econometrica* (2004), and Jörg Stoye, ["Minimax Regret Treatment Choice with Finite Samples"](https://doi.org/10.1016/j.jeconom.2009.02.013), *Journal of Econometrics* (2009). Both already develop minimax regret for treatment choices; our conditional rectangular-oracle formulas are simple special cases, **not** claims of discovery. [Data-Driven Automation](https://arxiv.org/abs/2606.10127) §5 and Appendix B already value future data and data-source aggregation. The potential contribution is a defensible *full-stack robotics data-to-qualified-paid-production observational interface*, not renaming this mathematics.

**November 22 scientific gate OPEN:** no original-buyer paired paid data, independent eligible cohort, physical S/G/SG/E approval, empirical learning effects, manufacturer economics, numerical BEA/BLS input-output coefficient, full repository CI or independent peer novelty review obtained. Retain the larger roadmap (multilayer production, cross-market demand, manufacturing, adoption/ownership/rights, source modalities, dynamic learning) and the final December 25, 2026, 23:59 America/New_York deadline.
