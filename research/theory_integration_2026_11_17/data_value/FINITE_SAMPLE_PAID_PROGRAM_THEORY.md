# Finite-sample original-buyer evidence and the source–grounding–embodiment decision

**21 November 2026. Same When Capabilities Become Production Models A/B question, not a separate paper.** The prior [decision-sufficient evidence chapter](DECISION_SUFFICIENT_EVIDENCE_AND_PROGRAM_CHOICE.md) compared perfect information oracles about SG and E. This continuation shows when a *finite* lawful sample of qualified, buyer-accepted, physically delivered and settled production could distinguish those investments, and when even infinite SG-only measurement cannot. All quantities are **conditional, synthetic and normalized**, not actual robotics returns.

## 1. Program-value environment

Keep original customer offers (including nonbuyers), shared scarce robots/operators, complete certified recipes, the retained R policy and the entire period-0 plus policy-consistent continuation in optimized production J. S denotes newly admitted source data, G-train target alignment, G-observe an untrained target report, SG their combined approved program and E a separate manufactured embodiment. Field successes, failures/recovery, teleoperation, simulation, synthetic and public/pretrained inputs have distinct lineage, costs and rights; none is the primitive ontology or automatically valuable. Do not count data twice when continuation J already incorporates its learning effects.

For a finite-sample example *only*, realize the previous SG∈[-1,5] and E∈[3,5] envelopes using different original-buyer complete paid-service events X and Z:

\[
J_{SG}=12k-1,\quad k=\Pr(X=1)\in[0,1/2];
\qquad J_E=8q-1,\quad q=\Pr(Z=1)\in[1/2,3/4].
\tag{1}
\]

X=1 requires whole A+B qualification, actual eligible buyer acceptance, feasible physical/operator service and irrevocable settlement. Every nonbuyer, failure, diverted outside order or refund must enter the full ledger as defined. E has a separately contracted recipe earning 8 per successful completed service; costs of 1 are **already included** in each net program mean. This Bernoulli price/payoff specification *realizes* but is not implied by previous interval bounds. If actual prices or costs vary, test continuous signed net contribution rather than fitting (1).

The economic comparison is \(\Delta=J_{SG}-J_E=12k-8q\). It is a **program average**, not an accuracy gap or a task-level source transfer coefficient. A whole-program study can identify \(\Delta\) without recovering the unobserved same-person cross-world qualification copula, provided the intervention unit encloses learner weights, fleet/operator queues, procurement parents, data rights and all displaced original orders. An E lacking physical/legal approval remains a hypothetical comparator.

## 2. One-sided identification result

**Proposition 1.** Under (1), perfect observation of k alone can certify **weak E dominance** whenever \(k\le 1/3\), since \(J_{SG}\le3\le J_E\). It can **never** establish that SG is *strictly better in every possible E world*, because \(J_{SG}\le5\) while E may equal 5. For \(1/3<k<1/2\), there are consistent E values choosing either program. At \(k=1/2\), SG weakly dominates E but may tie.

*Proof:* The worst SG-versus-E gap is \(12k-6\le0\) and the worst E-versus-SG gap is \(12k-4\le0\) iff \(k\le1/3\). Both endpoints are attainable at q=3/4 and q=1/2 respectively. Strict superiority over E's entire envelope would require k>1/2, outside (1). QED.

**Qualification-only counterworld:** Let Q denote complete technical qualification and C denote eligible buyer willingness, operator availability and final settlement. With \(\Pr(Q)=\Pr(C)=1/2\), the same marginal data admit \(\Pr(Q=C=1)=1/2\) when perfectly concordant or 0 when discordant. SG net 5 versus −1 reverses its ranking against a synthetic E worth 4. Thus perfectly estimating the technical h=Pr(Q) is not the same as observing k=Pr(Q,C); even perfect h and buyer marginal do not identify their economic coupling. This is a construction, not field evidence.

The asymmetric negative result is consequential: with the current E upper bound, another SG-only source-data or task-qualification study cannot certify strict SG economic superiority. Either a real E whole-service comparator, credible further E restrictions or an altered feasible menu is required.

## 3. Fixed-sample original-buyer contribution certificate

Suppose **independent identically distributed interference-closed original-buyer/learner/operator clusters** are assigned to frozen, legally and physically approved SG and E programs from the same eligible population. In the synthetic binary model observe \(n_S\) independent complete paid indicators X and \(n_E\) E indicators Z; every predeclared rejected/failed/refunded offer is recorded as a zero under the fixed payoff model. Use \(\hat\Delta=12\bar X-8\bar Z\).

**Proposition 2 (conditional bounded certificate).** For a prespecified two-sided \(\alpha\in(0,1)\),

\[
\Pr\{|\hat\Delta-\Delta|>r_\alpha\}\le\alpha,\qquad
r_\alpha(n_S,n_E)=\sqrt{\frac{\log(2/\alpha)}{2}
\left(\frac{144}{n_S}+\frac{64}{n_E}\right)}.
\tag{2}
\]

If the empirical winner is chosen, then on the coverage event the true per-cluster choice regret is at most \([r_\alpha-|\hat\Delta|]_+\). If \(|\hat\Delta|>r_\alpha\), its ranking is correct on that event. A uniform guarantee of sign certification whenever the true \(|\Delta|\ge\delta\) follows from \(2r_\alpha<\delta\).

*Proof:* Hoeffding's inequality for the independent bounded summands \(12X_i/n_S\) and \(-8Z_j/n_E\) uses squared ranges totaling \(144/n_S+64/n_E\); invert the two-sided tail. If the empirical winner is wrong while the confidence interval covers the truth, the adverse gap cannot exceed r minus the magnitude of the estimated gap. If the true magnitude exceeds 2r, even an estimate at the extreme of the coverage interval lies beyond zero by more than r. QED. This is classical concentration, not novel probability theory.

These are **fixed-n** guarantees, not the expected value of test information. Optional stopping after repeatedly inspecting an unadjusted interval is invalid. Shared model updates, common procurement, market-wide price effects or interfering robot fleets break the iid network premise. Training generated by the study itself may change future J and must be modeled as the tested adaptive program, not added as an information bonus.

## 4. Cost-aware sample design: optimize actual *measurement precision*, not benchmark scores

**Proposition 3 (worst-range cost allocation).** If every lawful cluster has equal experimental cost and \(n_S+n_E=N\), the squared radius is minimized by

\[
n_S:n_E=12:8=3:2,\qquad
r_{\alpha,\min}=\sqrt{\frac{200\log(2/\alpha)}{N}}.
\tag{3}
\]

For different intervention costs \(c_S,c_E>0\) under \(c_S n_S+c_E n_E=C\), the continuous optimum instead has

\[
n_S/n_E=(12/8)\sqrt{c_E/c_S}.
\tag{4}
\]

*Proof:* Cauchy–Schwarz gives \((144/n_S+64/n_E)(n_S+n_E)\ge(12+8)^2=400\), with equality at the 3:2 split. With costs, apply the same inequality to \((144c_S)/(c_Sn_S)+(64c_E)/(c_En_E)\) or differentiate its strictly convex constrained objective. QED.

At α=.05, a **conservative sufficient** uniform sign guarantee for \(|\Delta|\ge2\) needs \(N>800\log(40)/4\); the first integer N meeting this bound with near-3:2 allocation is 738 independent whole networks. With 600 clusters split 360/240, the radius is ~1.10889 normalized contribution units. At unit costs c_S=4,c_E=1 and budget C=160, the discrete optimum is 30 SG and 40 E networks. These are *synthetic mathematical comparisons*, emphatically not valid field sample sizes or a request to run a trial. Unknown intra-cluster dependence, commercial sample costs and less conservative variance/power calculations can change the optimum. The maximum possible SG gap here is 2 while E can lead by up to 6; obtaining decisive SG-upside evidence is intrinsically harder under these illustrative payoff restrictions.

The ratio 3:2 minimizes a *distribution-free Hoeffding range certificate* only. It need not minimize actual variance, Bayesian expected loss, signed operator cost, opportunity cost of incumbent customers, or the data's Bellman continuation. Actual \(k,q\), price/cost distributions and demand strata matter.

## 5. Matched pairs provide a distinct conditional guarantee

If 2m whole-network clusters can be matched on **preassignment** buyer order mix/site and randomized by fair SG/E swap within each pair (equal cluster weights, no cross-pair interference), let D_i be observed SG net minus observed E net. With net SG potentials in [-1,11] and E potentials in [-1,7], \(D_i\in[-8,12]\). Its fair-swap expectation equals the *pair-average* causal program difference, even conditional on fixed heterogenous potential outcomes. Independent fair swaps imply a conservative randomization-based two-sided radius

\[
20\sqrt{\frac{\log(2/\alpha)}{2m}}.
\tag{5}
\]

At 300 pairs (600 total clusters), it is ~1.56820, **larger** than the iid unpaired 600-cluster range radius ~1.10889. Good matching can nonetheless reduce *realized* randomization variance; the universal range envelope does not certify this. Unequal buyer-parent sizes need appropriate weighting and a new variance analysis. Standard matched-pair cluster literature, including Bai, Liu, Shaikh and Tabord-Meehan (2024), takes this issue substantially further.

## 6. Empirical and scientific gates

A legitimate observation combines the *same original eligible paid buyer order* with training checkpoint, full signed A+B qualification, customer willingness, shared operator/robot capacity and displaced orders, recovery, accepted service, refund/settlement and data reuse rights. A separate approved E arm is needed for actual two-arm estimation. Source modalities and deliberate versus production-generated information are tracked as distinct parents of future competence. A field failure can improve future J only through a licensed admitted update that ultimately changes qualified customer production; it is never a blanket financial premium. Likewise optional zero-cost source availability preserving all old R/specialist policies cannot lower optimized value, whereas forced costly retraining may.

If prices, contracts, embodiment costs, data access, operator constraints, buyer procurement or learning state respond across networks, the simple binary iid result is **not** transportable. Treat observed data as conditional on its supported demand, rights and technical intervention regime. The mechanism-level transfer question still requires matched learner-level source/G interventions with controlled compute/curation and independently validated qualification.

**Bounded closest prior art:** Hoeffding, [Probability Inequalities for Sums of Bounded Random Variables](https://doi.org/10.1080/01621459.1963.10500830), *JASA* 58 (1963); Manski (2004) and Stoye (2009) on minimax-regret program choice (cited in the predecessor); Bai et al., [Inference in Cluster Randomized Trials with Matched Pairs](https://ideas.repec.org/a/eee/econom/v245y2024i1s0304407624002185.html), *Journal of Econometrics* 245 (2024); and [Data-Driven Automation](https://arxiv.org/abs/2606.10127) §5/Appendix B for existing future-data and complementarity ideas. These derived applications are not independently validated scientific novelty.

The [prospective measurement protocol](FINITE_SAMPLE_PAID_PROGRAM_EVIDENCE.md), [executable](finite_sample_paid_program.js), [record](finite_sample_paid_program_results.json), [student exercises](FINITE_SAMPLE_PAID_PROGRAM_EXERCISES.md) and separate [solutions](FINITE_SAMPLE_PAID_PROGRAM_SOLUTIONS.md) accompany this chapter. No actual signed S/G/SG/E robot trials, original-buyer paid cohort, BEA/BLS numeric industry network, complete CI or independent peer validation exists. The November 22 acceptance gate remains **OPEN**. Theory remains the majority workstream through December 6; the final deadline remains December 25, 2026, 23:59 America/New_York.
