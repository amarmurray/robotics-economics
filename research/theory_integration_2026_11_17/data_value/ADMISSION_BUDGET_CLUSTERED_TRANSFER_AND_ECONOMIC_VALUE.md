# From proposed source episodes to economically relevant learner exposure

20 November 2026 — an integrated, **conditional** extension of *When Capabilities Become Production*, on the unchanged November 22 original buyer–robot–operator Models A/B gate. The question is whether source X, target grounding G or a newly qualified embodiment E improves **optimized accepted and paid original-customer production**, relative to retained competent R. This chapter extends [source admission](EFFECTIVE_DATA_TRANSFER_AND_LABEL_SUPPORT.md) rather than assigning a monetary price to archive size. No training, field qualification, original order, safety certification, or scientific novelty is claimed.

## 1. Episode availability, relabeled language and admitted transitions are different measures

Index a public/pretrained, simulation, synthetic, teleoperation, deliberate-collection, production, or failure/recovery source by s. A specific version-locked raw episode j in s produces L_{sj} *eligible-for-proposal transitions* after the declared preprocessing/action/observation pipeline. Let p_{sj} be the probability that its relabeled language-goal candidate is nonempty **conditional on that chosen preprocessing**, not an unconditional probability of semantic correctness. For a sweep of full episodes followed by uniformly sampled transitions within s, with one candidate drawn per episode application,

\[
 r_s^{\mathrm{transition}} =
 \frac{\sum_j L_{sj}p_{sj}}{\sum_j L_{sj}},
 \qquad
 r_s^{\mathrm{episode}} =
 \frac{1}{J_s}\sum_j p_{sj}.
\]

These are generally unequal. The equality requires, for instance, equal effective lengths or a vanishing length–eligibility covariance. Under repeated stochastic processing this is a **long-run expectation subject to actual sampler/worker semantics**; finite filtered batches need not equal either formula. A selected language string may be syntactically nonempty but semantically wrong; `p` is admission, not correctness, novelty, or target task utility.

The [original Berkeley pinned converter](https://github.com/rail-berkeley/bridge_data_v2/blob/bc60a35b701a12021c8c95e9d8601274d3acd928/data_processing/bridgedata_raw_to_numpy.py#L180-L206) makes `[""]` the fallback when `lang.txt` is absent. The [pinned BridgeDataset loader](https://github.com/rail-berkeley/bridge_data_v2/blob/bc60a35b701a12021c8c95e9d8601274d3acd928/jaxrl_m/data/bridge_dataset.py#L178-L255) constructs per-source datasets, relabels goals at trajectory scope, unbatches to transitions, samples source subdatasets with given weights, and *optionally* filters nonempty `goals.language` after source sampling. In [`_add_goals`](https://github.com/rail-berkeley/bridge_data_v2/blob/bc60a35b701a12021c8c95e9d8601274d3acd928/jaxrl_m/data/bridge_dataset.py#L376-L398), one language candidate is randomly selected for the trajectory and broadcast to its transitions. `load_language=False` and `skip_unlabeled=False` are defaults; do not infer active filtering or actual retention from code. `skip_unlabeled=True` needs an actually produced `goals.language` field, which is only introduced on the `load_language` path in this pinned code. This is static code reading, not an executed loader-error report.

**Exact synthetic denominator counterexample.** Source S has two episodes, lengths 1 and 9, with hypothetical nonempty-language probabilities 1 and 0 respectively. The episode-average label fraction is 1/2 but the transition-weighted eligibility rate is 1/10. Competing T is fully eligible. With equal per-subdataset proposal probabilities, S contributes **1/11**, not 1/3, of admitted transitions under the stationary iid proposal model below. All these values are stipulated, **not measured BridgeData label rates**. A fixed-length, fixed-proposal archive inclusion trial cannot equate raw episodes, admitted transitions and independent semantic coverage.

## 2. Proposed weights are not a learning dose or a compute budget

Assume, expressly for this proposition, iid transition proposals with source s drawn with weight w_s, acceptance indicator with conditional probability r_s, total R=Σ_s w_s r_s>0, and fixed per-proposal processing cost c_s plus common per-accepted-update cost c_u. Then conditional on acceptance,

\[
 q_s=\frac{w_sr_s}{R}.
\]

There are two **different interventions**:

* **Fixed B proposals:** expected accepted units `B R`; expected accepted source-s units `B w_s r_s`; expected preprocessing-plus-update cost `B Σ_s w_s c_s+B R c_u`. Actual accepted count remains random.
* **Stop at K accepted units:** provided independent proposals and no additional stopping restrictions, expected proposals `K/R`; expected source-s accepted units `K q_s`; expected cost `(K/R)Σ_s w_s c_s+K c_u` by the standard negative-binomial/Wald argument. This ignores source- or time-specific batch/preload overhead, finite archives, repeated episodes and nonstationary language sampling, which must be measured separately.

Proof: successful proposals form the conditional categorical distribution q. Under independent Bernoulli total acceptance R, the expected waiting time for each success is 1/R. Wald applies to the bounded iid proposal-cost increments under this stopping rule. The two designs agree on the *conditional accepted mixture* q but not necessarily on accepted dose K, preprocessing cost, repeated-example diversity or wall-clock delay.

**Synthetic exact resource calculation:** for source S with r_S=1/10, T with r_T=1 and w_S=w_T=1/2, R=11/20 and q_S=1/11. Ten fixed proposals yield expected 11/2 updates, 1/2 accepted S transitions and (at c_s=1/4, c_u=1) total expected cost 8. Ten *accepted* updates instead require 200/11 expected proposals, yield 10/11 S transitions and cost 160/11. A comparison at identical q but different budget is not an equal-investment learning comparison. These are dimensionless normalized costs, not dataset supplier prices or customer receipts.

## 3. Grounding can change the admission mechanism itself

Let g be a lawful, physically meaningful target-specific annotation, alignment or conditioning intervention. Allow both eligibility r_s(g) and the qualified-production-learning response H(q,K,g,e,ω) to change, where e is a particular certified embodiment menu and ω is original-customer demand/operator state. Under fixed proposal weights and R(g)>0,

\[
 \frac{d q_s}{dg}=\frac{w_sr_s'(g)}{R(g)}
                  -q_s\frac{\sum_jw_jr_j'(g)}{R(g)}.
\]

This expression remains well-defined at r_s=0 when r_s' exists; the logarithmic elasticity representation does **not**. For fixed B proposals, K(g)=B R(g) in expectation; for an exogenously enforced K accepted updates, K'=0 and preprocessing cost can vary as 1/R(g). At differentiability points in an *assumed* economic response,

\[
 \frac{dH}{dg}
   =\left.\frac{\partial H}{\partial g}\right|_{q,K}
     +\sum_s\frac{\partial H}{\partial q_s}\frac{d q_s}{dg}
     +\frac{\partial H}{\partial K}\frac{dK}{dg}.
\]

This is a decomposition of a **single** original-customer production response, not three addable data premiums. If g also changes hardware dispatch, customer signaling or source-generation/rights costs, its total policy value must be computed in the full V/J program. Target grounding may unlock previously unused source exposure; it may also substitute for source collection, reduce target report value, or leave qualified customer production unchanged. Image-goal learning and language-conditioned learning must remain separately feasible policies: an empty text label does not imply the episode's images and actions are useless.

## 4. Even equal accepted mixtures and doses do not identify transferable qualification

Consider a purely synthetic learner that receives one accepted unit from source S and one from T (thus q_S=q_T=1/2 and K=2). In each source, a rare customer-relevant failure/recovery context is represented with marginal probability 1/2. Let A and B denote whether the two units represent it. Suppose (only for this countermodel) that the new controller qualifies for one original-customer recipe iff A∨B, under a separately assumed safety-certified service policy.

Without the joint distribution, the sharp Fréchet range is

\[
 \Pr(A\lor B)
 =p_A+p_B-\Pr(A\cap B)
 \in [\max(p_A,p_B),\min(1,p_A+p_B)].
\]

With p_A=p_B=1/2: perfectly correlated units give 1/2 qualification; independent units give 3/4; perfectly anticorrelated units give 1. These worlds have exactly the same admitted source shares, two accepted units and marginal context rates. Stipulate four units of original-customer gross contribution *conditional on qualification* and a separately certified generalist E contribution of 5/2. Expected source-qualified production is respectively 2, 3 or 4; the source-versus-embodiment ranking reverses. This is **not** a benchmark-to-dollar conversion or observed transfer. It proves the negative claim that admission counts and marginals alone are insufficient for this stipulated nonlinear joint qualification map; it does **not** imply the real learner uses such a threshold or that two sources always complement one another.

The right measure is the reproducible *joint* target-qualification response to independently randomized learner-wide archive inclusion and grounding, accounting for repeated episode families, near-duplicate states, failures/recoveries, semantically valid goals, sample size and actual original customer demand. A source with lower apparent raw admission can be more economically valuable if its admitted units cover previously unsupported service bottlenecks. Conversely, identical task benchmarks can support opposite customer-resource allocations. Actual effects remain entirely unmeasured.

## 5. Choice rule, evidence and novelty boundary

For lawful available source X, grounding G and new embodiment E, define each feasible policy's economic value **once** as expected captured, fully qualified original-customer production (including appropriate future continuation) minus source acquisition/annotation, preprocessing/rejected draws, learner updates, physical bodies, manufacturing, shared operator dispatch, access and rights costs. Optimize over the certified policies and information available **before** irreversible decisions. Preserve R and old learning recipes as true options when they are feasible: free optional new archive availability cannot reduce the optimized value because it only expands the choice set. A forced positive sampling weight or a fixed proposal budget that displaces the old recipe can reduce performance/cash and is not this monotone availability comparison.

The novelty candidate is the **economic question and integrated validation architecture**, not the quotient rule, renewal sampling, Fréchet bounds, cluster design effects, or DDA's §5 future-data value and Appendix B complementarities. Prior foundational qualifications, LP resource duals, O-ring bundles, adaptive fallbacks and network interference remain unchanged.

**November 22 acceptance:** requires a version-locked (archive/manifest/loader/conditioning), rights-cleared whole-learner inclusion-versus-collection design and held-out joint customer-task qualification; signed, physically feasible whole-network R/X/G/E and matched original buyer offers/refusals, delivered accepted units and paid receipts, plus operator/machine/compute costs and actual assignment support. The pinned source code does not supply any of these. The [unpopulated prospective protocol](ADMISSION_BUDGET_PROSPECTIVE_VALIDATION.md), [exact rational executable](admission_budget_episode_coverage.js), [recorded result](admission_budget_episode_coverage_results.json), and separate [exercises](ADMISSION_BUDGET_EXERCISES.md)/[solutions](ADMISSION_BUDGET_SOLUTIONS.md) supply a checkable next technical and field-study design. The BEA–BLS quantitative production edge, full historical CI and independent originality remain open. Theory remains the majority through December 6; final target December 25, 2026 at 23:59 Eastern, unchanged.
