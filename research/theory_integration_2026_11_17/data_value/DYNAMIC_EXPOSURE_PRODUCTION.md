# Dynamic influence, joint qualification, and the economic value of source data
**19 November 2026 | Continuation of When Capabilities Become Production. Conditional theory, not robot evidence or established scientific originality.**

This extends [shared-pool interference](SHARED_POOL_INTERFERENCE_THEORY.md), not a separate question. The economically relevant investment contrast is still qualified, capturable **complete original-customer-order production**, with source modality X, retained R, independent target information A, grounded G, and changed embodiment E competing or combining under one feasible budget and one continuation-value calculation. The missing step after the two-site shared operator is **how a source intervention can change controller versions, operator recovery, and customer demand at different dates across nominal sites**, and what evidence would support transporting a local study to a complete-market choice.

## Economic environment and the comparison actually desired

Fix a pre-policy market/catchment register, horizon t=0,...,T, discount factors, feasible qualified service recipes, contracts, embodied/organizational resources, data rights and available retained policies. Include policy-induced subsequent orders as outcomes in that same declared catchment; do not silently redefine the denominator using only accepted service. For each physically approved policy vector z, let W_i(z) denote capturable net whole-service contribution consistently attributed to original customer-production unit i. The feasible operating solver V jointly allocates robots, specialist alternatives, labor, recovery slots, dispatch and customer opportunities. Write F(z)=sum_i E[W_i(z)], with incurred training, collection, validation, rights and embodiment costs subtracted once. Future trained capacity already appears in continuation V; adding a separate terminal "data premium" would double-count it.

In a *binary slice* of this larger five-action investment menu, z_i=1 means a specifically pinned, paid, approved X conversion and z_i=0 a pinned, qualified G or incumbent comparison. R/A/E are still available as separately evaluated candidate policies or as fixed common components of these regimes. A free optional source copy, which leaves all incumbent actions admissible, cannot lower optimized gross value; this fact is not a statement about forced retraining or net rollout returns. The full-market average contrast is T_market=[F(1,...,1)-F(0,...,0)]/N. The previous chapter's independently randomized mixed-saturation direct contrast D(p) is a different estimand when shared resource or learning channels interfere.

Define a *versioned joint state* S_t=(S_{1t},...,S_{mt}) containing any economically material controller snapshot/lineage, qualification and report status, dispatch queue, operator/recovery availability, rights, embodied configuration, original offered/refused orders, potential market demand and learned data. This is a mathematical state description, **not** a claim that all these components are observed. For an explicit structural sufficient condition, let the complete conditional next-state kernel factorize across correctly chosen state blocks:

\[
K_t^z(s'|s)=\prod_{k=1}^m K_{kt}^z(s'_k|s).
\tag{D1}
\]

This is conditional block independence of innovations, NOT independence of qualifications, customers or accepted services. Shared operator and shared learner must be included in the same block or explicitly connected before (D1) can be credible. Latent common noise cannot be removed merely by putting two sites in different rows.

## Finite-horizon influence certificate

Compare two approved vectors differing only at site j while holding focal site i's own policy a unchanged. Suppose both worlds start from a common pre-policy state law. For all otherwise admissible assignments and all histories:

* Changing state coordinate l alone alters next-block k's conditional kernel in total variation by at most A_{kl,t}; all A entries are nonnegative. This covers indirect operator-to-demand and learner-to-qualification links.
* Flipping intervention j, holding identical state input, changes that block kernel by at most b_{kj,t}^{a}. This includes different rights, targeting, training and embodiment effects **only when those full policies have been specified**.
* The complete net customer-contribution path functional obeys a bounded-difference inequality between two coupled histories, \(|W_i(z,s_{0:T})-W_i(z',s'_{0:T})|\le d_{ij}^{a}+\sum_{t,k}L_{ik,t}1\{s_{kt}\ne s'_{kt}\}\), where d includes any direct cross-site assignment cost/value not represented in S. L is a **complete-service contribution span** (including lost/reallocated orders and demand) rather than a technical score.

Define U_{j,0}=0 and the componentwise recurrence

\[
U_{j,t+1}=\min\{\mathbf1,\ A_t U_{j,t}+b_{j,t}^{a}\}.
\tag{D2}
\]

**Proposition.** Under (D1) and the uniform conditions above, for the approved two-policy comparison,

\[
\left|\mathbb E W_i(a,z_{-i})-\mathbb E W_i(a,z'_{-i})\right|
\le \epsilon_{ij}^{a}
:=d_{ij}^{a}+\sum_{t=0}^T\sum_k L_{ik,t}U_{j,k,t},
\tag{D3}
\]

whenever z and z' differ only at j. The bound holds even when controller qualifications, downstream operator recovery, subsequent customer orders and accepted production are correlated through preceding state. Its right-hand side requires **uniform** conditional influences and a correctly grouped state. It is not estimable from accepted-only order samples.

**Proof sketch.** Couple the equal pre-policy initial states. At each transition, for every block k use a maximal coupling of its two conditional kernels; conditional block factorization guarantees the product coupling has the correct two whole-state marginals. The triangle/telescoping inequality bounds the probability of block-k disagreement by b_{kj,t}+sum_l A_{kl,t} times indicators of previous block disagreement, capped at one. Expectations and induction give disagreement probabilities no larger than U. Apply the pathwise L bounded differences, include direct d, and take expectations. Details and alternative joint-kernel condition in [proof ledger](DYNAMIC_EXPOSURE_PROOFS.md).

The previous common-market exposure equation (I9) now has a constructive, but still assumption-dependent, input: replace epsilon_{ij}^a by (D3). For Bernoulli(p) site saturation,

\[
|D(p)-T_{\rm market}|\le N^{-1}\sum_i\sum_{j\ne i}
[(1-p)\epsilon_{ij}^{1}+p\epsilon_{ij}^{0}].
\tag{D4}
\]

No independence across **economic outcomes** is assumed in this step. If operator calendars, buyer substitutions and model broadcasts have unknown external descendants, b/A/L are not bounded and (D4) must be reported as *unidentified*, not numerically replaced by zero.

## An exact causal-path calculation, with a failed tempting conclusion

The [exact synthetic diagnostic](dynamic_influence_production.js) follows blocks Q (qualified controller state), O (shared operator recovery), D (original customer-demand response). Suppose one other-site intervention has first-period block disagreement probability upper vector b=(1/10,1/5,0). Let the hypothetical per-period cross-state influence matrix be

\[
A=\begin{bmatrix}0&1/4&0\\1/5&0&1/10\\0&1/2&0\end{bmatrix},
\qquad L=(2,1,4).
\]

This is **not** a measured robot transition matrix. In four periods, (D2) gives after-date disagreement bounds
(1/10,1/5,0); (1/20,1/50,1/10); (1/200,1/50,1/100); (1/200,1/500,1/100).
Their L-weighted sum is 521/500 whole-service units. Removing the apparently indirect O→D edge gives 273/500, understating the assumed certificate by 62/125. A source change need not directly alter buyer demand at date 0 for its operator consequences to affect that demand at date 2.

To illustrate what this matters for **decision claims**, suppose—not estimate—that a mixed-saturation own-X contrast is 2/5 per site at p=1/2, the two sites have symmetric cross-exposure limits, and incumbent-site effects vanish. (D4) permits complete-market T in [-121/1000,921/1000]: **no sign is identified**. Treating O→D as nonexistent would report the **invalid** [127/1000,673/1000], falsely concluding profitable universal adoption. The calculation tests a declared set of sufficient assumptions and a wrong graph, not scientific calibration.

A second exact whole-service construction makes the error concrete without assuming the matrix bounds are tight. Suppose net site contribution is \(w_i(z_i,z_j)=3+(3/4)z_i-z_i z_j\). The interaction can be implemented by a lagged operator shift that induces buyer substitution, or by a shared model update; specifying the edge is a physical hypothesis. Incumbent market=6; converting exactly one site=27/4; converting both=11/2. Under p=1/2 the focal own-X direct effect is +1/4, yet complete rollout loses -1/4 **per site**. An unrecorded lagged edge makes a formally unbiased local experiment economically misleading for the full-market target.

## Why no purely marginal graph audit suffices

There is a stricter failure of (D1). Two candidate joint next-state laws can assign probability 1/2 to (Q,O)=(0,0),(1,1), or instead probability 1/2 to (0,1),(1,0). The marginal law of each block is identical in both regimes, but a service that **jointly** requires Q=O=1 qualifies with probability 1/2 versus 0. All coordinatewise *same-input marginal* policy TV changes are zero. A certificate that uses those zero marginals while ignoring changed dependence incorrectly declares no economic response. This is a coupling/qualification counterexample, not a claim of empirical cross-embodiment transfer.

**Constructive alternative.** Retain any shared innovation / pooled operator / joint qualification block as a single node and certify its *joint* kernel, not just each marginal. More generally a horizon-level coupling of whole conditional state snapshots gives a coarse valid alternative if the full-kernel TV satisfies
\[
TV(K_t^z(\cdot|s),K_t^{z'}(\cdot|s'))\le\beta_{jt}+\alpha_t 1\{s\ne s'\}.
\tag{D5}
\]
The whole-state disagreement probability h obeys \(h_0=0,\ h_{t+1}\le\min\{1,\beta_{jt}+\alpha_t h_t\}\), and a whole-history payoff span B_{it} gives \(|\Delta E W_i|\le d+\sum_t B_{it}h_t\). This alternative preserves arbitrary within-date correlations but can be too loose for a useful choice. No known joint kernel or empirical \(\alpha,\beta\) is claimed.

## Economic interpretation and model A/B boundary

In **Model A**, controller learning may create a newly qualified complete recipe, but operator scarcity, customer choice, specialist alternatives and simultaneous orders determine whether its technical gains create additional captured production. A qualification and a customer opportunity must coincide under actual recovery/dispatch feasibility. In **Model B**, R, A, X, G and E alter the histories and their rights/costs; a new body may both add a slot and alter transfer or demand, so the difference between one- and two-slot cross differences does NOT isolate congestion without the capacity-only exclusion. Source data can complement target grounding (unlock old representations) or substitute for it, but these are *optimized-production* interactions, not raw dataset overlap coefficients.

The practical value of (D3) is a **condition under which an economically weighted local-to-market sensitivity argument is honest**, with transparent routes through operator and buyer systems. It is not an automatic proof that approximate neighborhood interference decays with graph distance. Without certified causal closure or bounds, the previous direct whole-policy study is valid only for actually independent closed markets, and an observationally selected rollout remains partially identified. Costs and resources for audits, teleoperation, training and embodied capacity belong in J once, with old policies preserved.

## Prior-art positioning and serious objections

Aronow and Samii, *Annals of Applied Statistics* 11(4), 1912–1947 (2017), DOI 10.1214/16-AOAS1005, already formalize randomization/exposure mappings under interference: https://isps.yale.edu/resource/estimating-average-causal-effects-under-general-interference-with-application-to-a-social . Leung, *Econometrica* 90(1), 267–293 (2022), DOI 10.3982/ECTA17841, already develops **approximate neighborhood interference**, including decay rather than strict exclusion: https://doi.org/10.3982/ECTA17841 . Dobrushin-type influence inequalities and path couplings predate this exercise. Farboodi, Koh and Xia's *Data-Driven Automation*, arXiv:2606.10127, §5 and Appendix B already price future data and discuss complementary aggregation: https://arxiv.org/abs/2606.10127 . The claim here is a domain-specific conditional synthesis connecting *complete qualified customer production*, correlated recovery/learning, source-data policies and an economically weighted exposure certificate—not independent novelty in causal inference, coupling or data aggregation. Only abstracts/source descriptions of the two interference papers were checked during this continuation; no entire proof reproduction or originality verdict.

Strong objections: block innovation independence may fail through latent operator state; the bounds may be too loose to rank anything; declared order spans can miss unobserved future entrants; graph closure/rights may change under X; per-site net contributions may not consistently allocate multi-site accepted orders; the A matrix itself is not learned from selected dispatch logs. These are genuine empirical and structural limitations, not solved by synthetic arithmetic. A negative paid full-X rollout is not proof free optional data has negative intrinsic value.

**Exact next obligation:** prespecify a *joint* source update/operator/customer-response block and full original-order registry, then determine whether a safely approved held-out design can establish any useful nonzero upper influence limits. If not, retain an interference-agnostic full-market interval and the competent fallback. Review this condition at the November 22 synthesis gate, which remains open; theory priority continues through December 6; final cutoff December 25, 2026, 23:59 America/New_York.
