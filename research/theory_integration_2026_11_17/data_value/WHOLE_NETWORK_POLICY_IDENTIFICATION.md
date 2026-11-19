# Full-history qualified production: identifying economic policy value without identifying every transfer mechanism

**19 November 2026 — continuation of _When Capabilities Become Production_.** This chapter resolves a specific measurement gap after [joint operator scarcity](JOINT_OPERATOR_INFORMATION_CAPACITY.md): X training, G grounding, A target audits and E embodiment can alter original demand, qualifications, reporter selection and recovery **throughout** a production history. Their fixed-law operator-information/capacity identity cannot be integrated under the old R history distribution. We instead distinguish (i) the entire approved deployment-policy economic estimand; (ii) technical/causal mediation; and (iii) partial support. These are applications of established randomization, interference and partial-identification mathematics, **not established scientific novelty**.

## 1. An economic object with a fixed *pre-policy* denominator

Let i=1,…,N index a pre-specified population of **entire customer–robot–operator–controller-update networks**, including all sites competing for the same recovery crew, training updates, capacity or dispatch. A policy k∈{R,A,X,G,E} is a **complete, physically approved and rights-cleared regime**, specifying controller/data lineage, safe logging or audit, grounding or body, allocation/rollback rules and all adaptive downstream choices. A policy is not a generic data source. It generates its own realized history

\[
H_i(k)=(D_{i0:T}(k),Q_{i0:T}(k),O_{i0:T}(k),S_{i0:T}(k),L_{i0:T}(k),Y_{i0:T}(k)),
\]

where D are **original offered/unserved/rejected orders** (possibly changed by k), Q jointly qualified complete-service recipes, O operator/recovery/dispatch resources, S observed or missing reports, L source lineage and permissions, and Y accepted production. The captured **whole-network** contribution, per *fixed pre-policy network* and common horizon, is

\[
W_i(k)=\sum_{t=0}^{T}\delta^t \Big[\sum_{o\in D_{it}(k)}
g_{iot}(k)\,1\{\text{fully qualified, safely accepted, delivered order }o\}
-\text{displaced incumbent contribution}_{it}(k)\Big]-C_i(k).
\tag{1}
\]

All components are booked once; C includes intervention, training, compute, curation, rights, human attention and lost production not already included in the stage contribution. Future learning enters **inside the induced continuation history** and is **not an extra data premium**. Choose a consistently defined gross/net convention before using (1). This is the common J and optimized qualified-production V evaluated under the entire regime. Define J_k=N^{-1}∑_i W_i(k), Δ_XG=J_X−J_G. Do *not* divide by accepted orders or a post-policy original-order count: those denominators change with k and would change the question. R remains an admissible productive incumbent wherever safe; free legally optional data alone cannot shrink its feasible decision menu.

Unapproved physical policies do **not** have a deployable W_i(k); they cannot be rescued by assigning a guessed number or averaging over hypothetical unsafe histories.

## 2. Policy-closed assignment theorem, not mechanical transfer identification

**Proposition (finite-population whole-policy comparison).** Suppose: (a) N pre-listed complete networks with well-defined W_i(k), no spillovers **between** networks (arbitrary interference *within* each); (b) independently approved complete X and G regimes with stable versions, independent assignment of n_X networks to X and remaining n_G=N−n_X to G by uniform complete randomization; (c) complete original-order and displaced-service contribution over the same horizon, including failures, unattempted and lost service; and (d) no differential loss or hidden post-assignment exclusion. Then

\[
\widehat\Delta=\frac1{n_X}\sum_{i:Z_i=X}W_i(X)-\frac1{n_G}\sum_{i:Z_i=G}W_i(G)
\quad\Rightarrow\quad
E_Z[\widehat\Delta]=J_X-J_G.
\tag{2}
\]

No assumption of independent qualification, common X/G demand, equal reporter selection or known individual source-to-target transfer enters (2). This **intention-to-deploy** estimand includes policy-induced order demand and scarcity. It does not identify the latent overlap of individual qualification gains, transport to unassigned markets, or the causal contribution of a particular training modality. Under finite-population notation \(S_k^2=(N-1)^{-1}\sum_i(W_i(k)-J_k)^2\) and \(S_\Delta^2=(N-1)^{-1}\sum_i([W_i(X)-W_i(G)]-\Delta)^2\),

\[
\operatorname{Var}_Z(\widehat\Delta)=S_X^2/n_X+S_G^2/n_G-S_\Delta^2/N.
\tag{3}
\]

The individual-effect variance is ordinarily **not observed**; dropping the nonnegative last term gives a conservative variance estimator if arm-specific variance estimators are available, not a proof that two policy values are equal. When a controller/data update spills across networks, the unit definition is wrong; cluster the *closed interference graph*, or adopt an explicit exposure mapping. Randomizing individual robots while sharing an operator or online learner does not generally identify (2).

## 3. Exact two-date counterexample with endogenous demand and recovery

The [executable reference table](whole_network_policy_history.js) constructs eight **synthetic** pre-policy closed networks, each with a first original order (value 5) and a possible second original order (value 9). One shared operator is unavailable in period 2 after a failed first attempt, unless a separately safe nonactuating A report permits skipping a doomed first action or E supplies a fully qualified additional slot. X can change first qualification, second qualification *and second original demand*; G can change target qualification and demand. A and E do not automatically train X's capabilities. Fixed per-network illustrative costs are R=0, A=1, X=3, G=1, E=2. All old outcomes use the *same* network as a counterfactual unit; none is a robot observation or calibrated $ number.

Exact total *net contribution over eight networks* is R=29, A=30, X=42, G=39, E=22; thus \(J_X-J_G=3/8>0\). Yet the **mean gross contribution conditional on an accepted service**, an endogenous selected denominator, is X=66/10=33/5, while G=47/7. Therefore accepted-only data prefer G (47/7>33/5) even though whole-network net production prefers X (42/8>39/8). This reversal comes from accepted-order selection, operator recovery and changed original demand; **no benchmark percentage is mapped into money**. A single price per accepted service does not identify the full realized market opportunity or the lost incumbent order.

Enumerating **all 70** balanced assignments of four networks to X and four to G yields exact mean estimator 3/8, despite completely different policy-induced histories. Its assignment variance in this artificial population is 8615/448, computed independently through equation (3). The variance is large: unbiasedness alone does **not** guarantee one small study will favor the correct policy.

## 4. What remains identified without complete policy support?

If both X and G are safely deployable on the target market but we have **complete paired** policy differences only on supported pre-policy mass w, then, for unknown remainder 1−w, with admissible per-unit net ranges W_X∈[L_X,U_X] and W_G∈[L_G,U_G],

\[
\Delta_{XG}\in
\left[w\Delta_{\mathcal S}+(1-w)(L_X-U_G),\
w\Delta_{\mathcal S}+(1-w)(U_X-L_G)\right].
\tag{4}
\]

These are sharp **only relative to unrestricted unsupported joint potential outcomes and payout envelopes**; stable qualification, network and common-budget restrictions can narrow them. In the synthetic reference table suppose even the first six networks' *paired* difference totals 7 but the last two networks have no observations: X∈[−3,11], G∈[−1,13]. The all-network comparison can then be anywhere in [−25/8,31/8], including either sign, despite the true synthetic 3/8. Ordinary randomized data, which observe just one potential outcome per supported network, give less paired information. Missingness tied to accepted output cannot be described as independent support.

Alternatively, enumerate feasible **entire-network response types** θ, containing the potential trajectories of all *approved* policies and recording/market rules. For exact observed moment vector m and a validated response-type matrix M, define \(\mathcal P=\{p\ge0:\mathbf 1^\top p=1,\ Mp=m\}\), and \(d_\theta=W_\theta(X)-W_\theta(G)\). The same-world structural sharp interval is

\[
\underline\Delta=\min_{p\in\mathcal P}d^\top p,\qquad
\overline\Delta=\max_{p\in\mathcal P}d^\top p,
\quad
\underline\Delta=\max_{\lambda,\alpha}\{\lambda^\top m+\alpha:
\lambda^\top M_{\cdot\theta}+\alpha\le d_\theta\ \forall\theta\}.
\tag{5}
\]

Linear programming duality proves the certificate when the finite feasible type list is correct and nonempty. If all policy-dependent demand, recovery and selected recording types are left free, (5) can be weak; imposing independence merely to sharpen it is unjustified. Moment uncertainty requires confidence sets and does **not** turn a source dataset into an X-policy intervention. Unlike (2), this route needs a defensible mapping from logging moments to cross-policy physical trajectories.

**Identification hierarchy:** matched complete network assignments can identify economic policy means without the hidden mechanical decomposition; joint independently validated pre-action qualifications can identify selected mechanism contrasts; accepted-only R logs alone usually identify neither X potential customer demand nor post-failure transport. The old fixed-law information/body identity remains useful **within** a supported common history, not as an X/G cross-policy equality.

## 5. Distinguishing the mechanisms and the investment menu

Maintain field trajectory, failure/recovery, teleoperation, simulation, synthetic and public/pretrained inputs as separate source categories; each may shift competence, joint qualification, target visits, reports and customer demand differently. Deliberate target audit changes what is known; physical grounding may make an existing corpus useful; a new embodiment changes the feasible service/slot network; production-generated data may change later skills at the cost/opportunity already represented by the whole regime. A broad source portfolio has no necessary positive forced-training marginal effect. Optional old trained policies and specialist service survive as alternatives when feasible. The comparison should ultimately optimize feasible **combinations** under budgets, not assume five mutually exclusive long-run investment paths.

The exact new empirical requirement is not another pooled qualification rate: it is a *policy-closed prelisted network* whose approved controller lineage, original and unserved customer orders, full accepted contribution, operator recovery calendars and data-report selection are linked, with no untracked shared operator/model updates across randomized units. A controlled experiment on fully qualified complete service is an **alternative** to recovering every transfer tensor, not evidence that technical mediation has been measured.

## 6. Closest existing theory and limits

The randomization identity and Neyman variance are classical finite-population experimental design; the inside-cluster/outside-cluster interference distinction is related to Hudgens & Halloran (2008), [JASA article](https://pmc.ncbi.nlm.nih.gov/articles/PMC2600548/), and general interference/exposure mappings to Aronow & Samii (2017), [Annals of Applied Statistics](https://isps.yale.edu/resource/estimating-average-causal-effects-under-general-interference-with-application-to-a-social). Conditioning on posttreatment compliance, selection or accepted production is not a randomized whole-policy comparison; cf. Dahabreh, Ung, Hernán & Chiu (2024), [arXiv:2408.14710](https://arxiv.org/abs/2408.14710). Farboodi, Koh & Xia, _Data-Driven Automation_ (2026) already treat production learning and future-data value; §5 and Appendix B are **not** to be claimed as this project's novelty. (4)–(5) use standard missing-support and LP dual reasoning. Source records and current metadata were checked 19 Nov; no full new novelty audit was done.

**Scientific status:** conditional definitions, proof and a self-contained exact synthetic CPU check. Not external peer review, robotics field evidence, independent cost estimates, a signed physical test authorization, observed whole-network source learning, quantitative BLS–BEA crosswalk or full repository CI. The Nov22 integrated scientific gate remains OPEN. Maintain 60–70% theory emphasis through Dec6 and deadline **Dec25 2026 23:59 America/New_York**.
