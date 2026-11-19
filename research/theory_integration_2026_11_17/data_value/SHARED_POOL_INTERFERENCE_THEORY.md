# Data transfer across shared operator pools: local effects, whole-market policies, and embodiment complementarity

**19 November 2026 | chapter of _When Capabilities Become Production_; synthesized theory, not measured robotics or independent novelty.** Continue [whole-network policy identification](WHOLE_NETWORK_POLICY_IDENTIFICATION.md), rather than starting a new research question. The unresolved problem there is that an X-trained controller can change the qualification, demand, model-update and operator histories of *other* nominal networks. The closed-network randomization identity only identifies a policy contrast if those spillovers are inside the assigned unit. This chapter connects that problem to the original optimized qualified-production value \(V\) and the data-acquisition/investment objective \(J\).

## 1. Target under interference, with an incumbent

Fix \(N\) **pre-policy** customer-site/production units and a common complete horizon. Let \(\mathbf z\in\{0,1\}^N\) specify where a source-data-trained controller X is **paid for and physically admitted** rather than incumbent qualified controller G. For every *approved* policy vector, define \(w_i(\mathbf z)\) as the **capturable, net, complete original-customer-order contribution assigned consistently to site i**, including displacement, qualified dispatch, recovery, retained human work, policy-induced customer demand and subsequent learning **once**. The market operating/investment value is

\[
F(\mathbf z)=\sum_i w_i(\mathbf z)
=\sum_{t=0}^T\delta^t V_t\bigl(Q_t(\mathbf z),D_t(\mathbf z),B_t(\mathbf z),\mathcal R_t(\mathbf z)\bigr)-C(\mathbf z),
\tag{I1}
\]

where \(V_t\) optimizes feasible *whole* accepted-service recipes over demand and coupled operator/robot constraints, and \(\mathcal R_t\) represents physically approved allocation, reporting and controller-update rules. This compressed notation is not an assertion that one can observe or identify those arguments separately. Costs include source adaptation, curation/compute, rights, qualification, displaced production and embodiment, using a consistent gross/net accounting convention. **No extra terminal data premium** is added to (I1); all useful future source data act through \(Q,D,B,\mathcal R\) and continuation production. A fixed market frame prevents policy-induced post-treatment accepted orders from replacing the denominator.

The full-deployment contrast for approved X and G vectors is
\[
T=\tfrac1N[F(\mathbf 1)-F(\mathbf 0)].
\tag{I2}
\]
This is not generally equal to a site-level effect measured while nearby sites use a mixed assignment. If only free optional information is added and incumbent policies, resources and rights remain feasible, the **gross optimized** \(V\) cannot fall. The costly or forced X intervention here is a *different feasible investment*, whose net \(J\) may fall; no negative-transfer inference about optional free data follows.

## 2. A two-site microfoundation inside qualified production

Two pre-listed sites have already-qualified incumbent complete-service production of \(b\) each. Each costly X admission qualifies an *additional* original-customer service worth **net incremental contribution** \(v>0\) if safely delivered. Qualified X service requires one shared operator/recovery slot; there is **one slot across both sites** in the relevant window. X has real per-site acquisition cost \(k\ge0\). When **both** sites use X, their separate versioned source data may improve the *one feasible incremental complete service* by an additional \(\ell\ge0\); \(\ell\) is an explicitly conditional incremental production contribution from complementary learning, not a benchmark score or a second data premium. A separately qualified physical E investment provides a second compatible slot, at cost \(K\), without changing the X learning law. Put \(q=z_1+z_2\), \(e\in\{0,1\}\):

\[
F_e(q)=2b+v\min\{q,1+e\}+\ell\,1\{q=2\}-kq-Ke.
\tag{I3}
\]

This is an optimized accepted-production table under a *maintained* fixed \(v,\ell\), qualifying hardware, demand and operator rules. The incumbent service \(2b\) remains physically feasible for all q. A policy may retain it rather than execute X's added work; investment costs nevertheless remain paid. Two trained sites do not imply two usable extra orders with one slot. Source and embodied investments therefore compete for money but can complement in **physical production**.

The set-value interaction with one slot is
\[
\Delta_{12}F_0=F_0(2)-2F_0(1)+F_0(0)=\ell-v,
\tag{I4}
\]
and with two slots is \(\Delta_{12}F_1=\ell\). Thus
\[
\Delta_{12}F_1-\Delta_{12}F_0=v.
\tag{I5}
\]
Within the separable capacity-only model, cross-site source **substitution** (when \(\ell<v\)) can coexist with *positive* technical source learning \(\ell>0\): capacity congestion masks learning complementarity. Adding a physically qualified embodied slot removes that particular bottleneck, revealing \(\ell\). Equation (I5) is a conditional factorial diagnostic, **not** an identification result when E also changes customer acceptance, transfers, learning, or operator demand. This decomposition is a use of standard discrete complementarity, not a claimed new theorem.

## 3. Why a locally positive source effect can recommend the wrong market rollout

Allocate the incremental service symmetrically among qualified X sites ex ante. Under e=0, for an X site with \(q\ge1\), expected site net contribution is \(b+v/q-k+\ell\,1\{q=2\}/2\); an incumbent G site contributes \(b\). Let another site independently receive X with probability \(p\), keeping the **other-site assignment distribution fixed** when measuring a focal-site direct effect. Then

\[
D(p)=(1-p)(v-k)+p(v/2+\ell/2-k)
=v(1-p/2)+p\ell/2-k,
\tag{I6}
\]
while the all-X versus all-G **per-site market** effect is
\[
T=(v+\ell)/2-k.
\tag{I7}
\]
Therefore
\[
D(p)-T=\tfrac{1-p}{2}(v-\ell).
\tag{I8}
\]
A mixed-saturation direct effect is a real estimand, but it is **not** the market-wide policy contrast unless exposure changes vanish, the interaction exactly cancels, or saturation reaches p=1 with support. The sign of the transport error depends on technical pooling versus operator congestion; one need not assume all spillovers are negative. Randomizing individual robots with shared operators and broadcasting learner updates does not fix the estimand.

**Exact synthetic choice, not robotics calibration:** \(b=3,v=4,k=5/2,\ell=0,K=1\). Net two-site totals for \((q,e)=(0,0),(1,0),(2,0),(0,1),(1,1),(2,1)\) are respectively
\[
6,\quad 15/2,\quad 5,\quad 5,\quad 13/2,\quad 8.
\]
At \(p=1/2\), the observed-in-expectation **site-level own-X direct effect** is \(+1/2\), yet complete X adoption versus complete G is \(-1/2\) **per site**: an actual rank reversal. Selecting one X deterministically is worth \(15/2\); the physically approved source+second-slot portfolio is worth \(8\), the best of these six. E alone costs value because there is no additional qualified X service to use its slot. Independent half-saturation yields only \(13/2\) expected total; the best independent stochastic saturation is \(p=3/8\), worth \(105/16\), inferior to an explicitly coordinated one-X choice. A model trained on selected successful X service could miss precisely the operator displacement that makes indiscriminate rollout worse.

Holding other parameters fixed but setting \(\ell=6\) changes all-X to \(11\), local half-saturation effect to \(2\), and complete rollout effect to \(5/2\) per site; now the same local comparison **understates** market-wide value. It is wrong to posit a priori that technical transfer is always additive and positive, or that the sign of an observed site-level policy effect fixes the market spillover sign.

## 4. A sensitivity certificate and an identification route

For arbitrary physically approved whole-history potential outcomes \(w_i(a,\mathbf z_{-i})\), suppose changing some other site's assignment j changes site i's contribution by at most \(\epsilon_{ij}^{a}\), uniformly over all other assignments and induced histories, for fixed i's own action a. This must cover *all* operator, data-update and buyer-demand spillover channels. Under independent Bernoulli(p) site assignments, define the average randomized own-action direct contrast \(D(p)=N^{-1}\sum_i E_{\mathbf Z_{-i}}[w_i(1,\mathbf Z_{-i})-w_i(0,\mathbf Z_{-i})]\). A telescoping path to the all-X/all-G vectors implies
\[
|D(p)-T|\le {1\over N}\sum_i\sum_{j\ne i}
[(1-p)\epsilon_{ij}^1+p\epsilon_{ij}^0].
\tag{I9}
\]
For the two-site model, \(\epsilon_{ij}^{1}=|v-\ell|/2\) and \(\epsilon_{ij}^0=0\), so (I9) **attains equality** as the absolute version of (I8). This is an *assumption-conditional sensitivity interval*, not an inference that \(\epsilon\) has been observed or bounded from accepted-only logs. If the effects of a model broadcast or demand response are unbounded/unmapped, the certificate is uninformative.

A different identification route uses a **correct, stable exposure mapping** \(e_i(\mathbf z)\) that completely summarizes the dependence of \(w_i\) on other network assignments. If an approved randomization design gives positive assignment probabilities \(\pi_i^1=P(Z_i=1,e_i=e_i(\mathbf 1))>0\) and \(\pi_i^0=P(Z_i=0,e_i=e_i(\mathbf 0))>0\), then a Horvitz–Thompson estimator
\[
\widehat T={1\over N}\sum_i\left[
{1\{Z_i=1,e_i=e_i(\mathbf1)\}w_i(\mathbf Z)\over\pi_i^1}
-
{1\{Z_i=0,e_i=e_i(\mathbf0)\}w_i(\mathbf Z)\over\pi_i^0}\right]
\tag{I10}
\]
is design-unbiased for (I2). Proof is termwise expectation. This does **not** identify source modality mediation and may be unusably variable: under unrestricted dependence the required all-X neighbor exposure can have probability \(p^{d_i+1}\), vanishing with graph degree. If exposure mapping omits shared learning, price substitution or operator recovery, unbiasedness fails. Whole closed-market randomized policy regimes remain the prior chapter's cleaner estimand when independent closures are real; if the entire market is one connected interference component, a conventional many-cluster trial is unavailable.

The canonical next scientific step is to characterize **when a pre-policy graph of operator, update, rights and demand edges is a defensible closure**, and when a version-pinned mixed-saturation/factorial-E design can actually observe the response surface \(F_0(q),F_1(q)\). The algebra itself is not a substitute for approval, original offered/rejected order accounting, and safely qualified whole service. See [proof/rejection ledger](SHARED_POOL_INTERFERENCE_PROOFS.md), [prospective protocol](SHARED_POOL_INTERFERENCE_EMPIRICAL.md), executable [integer check](shared_pool_interference.js), [result](shared_pool_interference_results.json) and separate [exercises](SHARED_POOL_INTERFERENCE_EXERCISES.md)/[solutions](SHARED_POOL_INTERFERENCE_SOLUTIONS.md).

## 5. Prior work, adversarial limits, and scope

Interference and policy-exposure identification are established: Hudgens & Halloran (2008), [JASA](https://midasnetwork.us/papers/toward-causal-inference-with-interference/); Aronow & Samii (2017), [Annals of Applied Statistics](https://isps.yale.edu/resource/estimating-average-causal-effects-under-general-interference-with-application-to-a-social); marketplace design under interference in Bajari et al. (2023), [Statistical Science](https://www.gsb.stanford.edu/faculty-research/publications/experimental-design-marketplaces). _Data-Driven Automation_ (Farboodi–Koh–Xia, 2026), [arXiv:2606.10127](https://arxiv.org/abs/2606.10127), already values future data in production and discusses complementary aggregation. The novelty, if any, would need to reside in a materially validated and discriminating **qualified robotics production** explanation, not in causal estimators, LP duality, cross differences or an invented threshold.

(I3) assumes one identical marginal service value v, equal costs, no binding financing/rights constraints, additive synergy, unchanged original demand and an E that changes capacity only. These are deliberately **challenged**, not smuggled into empirical conclusions. Under endogenous price-demand equilibrium, heterogeneous source costs and qualification bundles, operator priority, intertemporal data feedback, shared model interference and cross-site customer substitution, neither (I5) nor the numerical rankings transport automatically. The exposure sensitivity result (I9) still applies to fully accounted approved potential values *only if valid uniform bounds are supplied*. No field intervention, actual customer-order panel, numeric official BLS–BEA crosswalk, independent novelty review or full repository CI has been obtained. **November 22 scientific gate open; December 25 23:59 America/New_York unchanged.**
