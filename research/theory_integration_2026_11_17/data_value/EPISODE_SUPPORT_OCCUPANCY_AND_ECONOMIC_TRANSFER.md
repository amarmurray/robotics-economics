# Episode support, coverage and the source-versus-grounding-versus-embodiment decision

20 November 2026 (Eastern). Continuation of the same *When Capabilities Become Production* November 22 Model A/B source-X, target-grounding-G, certified embodiment-E and retained-R decision. **Conditional theoretical construction, not an empirical robotics estimate or established novel theorem.** It repairs the remaining gap between the previous admitted-source-mixture/accepted-budget identities and actual learning of distinct failure/recovery contexts. Existing source-data value in Data-Driven Automation §5 and data complementarities in its Appendix B are acknowledged prior foundations, not claims of novelty.

## Precise question and environment

When is it economically preferable to generate more source episodes X, ground and resample an existing archive G, or commission a changed embodiment E, if all three can change the *reachable, safely qualified original-customer production menu*? The decision remains over **complete policies**, not benchmark accuracy or abstract data counts.

Let \(j\) index independently meaningful *source episode families*, not arbitrary filenames. The finite archive has episodes with processed transition lengths \(L_j\), source provenance \(s(j)\), and eligibility \(a_j(g)\in[0,1]\) under a **specified** preprocessing and grounding action g. Source proposal weights \(w_s\) apply before transition sampling. Within source s, assume a transition is proposed uniformly among its \(T_s=\sum_{k:s(k)=s}L_k\) processed transitions; source eligibility is \(r_s(g)=\sum_{j:s(j)=s}L_j a_j(g)/T_s\). If \(R(g)=\sum_s w_s r_s(g)>0\), the conditional distribution of an *accepted episode-of-origin* is

\[
p_j(g)=\frac{w_{s(j)}L_j a_j(g)/T_{s(j)}}{R(g)}.
\]

In a one-source archive, this simplifies to \(p_j=L_ja_j/\sum_k L_ka_k\). The earlier admitted source share is recovered as \(q_s=\sum_{j:s(j)=s}p_j=w_sr_s/R\). The formula **requires** a stable accepted draw kernel; the pinned Berkeley loader can choose one language goal at trajectory scope, so repeated correlations, worker state, deterministic traversal and finite epochs must be recorded rather than silently treated as independent draws.

For theoretical isolation, first suppose the learner receives K **iid with-replacement accepted episode-of-origin draws** at a fixed downstream compute/update budget. Hold a qualified original-customer production value table \(V(Q,D,E,R;P)\) and physical permissions fixed while varying which learning experience is available. Let technical success \(Q=\mathcal L(J_1,\ldots,J_K,g,e)\) be an otherwise unspecified *joint* customer-recipe qualification map. Neither unique episodes nor context presence is assumed to determine a real robot's qualification. Customer orders, capacity, rights, operator displacement, accepted-paid service and costs enter only in the already optimized policy contribution \(J=\max_{P\in\mathcal P_{\rm signed}}\mathbb E[V(Q,D,E,R;P)]-C(P)\). No separate continuation/data premium is appended.

## Proposition 1: episode diversity is a distinct input from source shares and update count

Let \(U_K\) denote the number of different independently meaningful episode families represented in K iid accepted draws. Then

\[
\mathbb E[U_K]=\sum_{j=1}^{m}\{1-(1-p_j)^K\},\qquad
\Pr(J_1=J_2)=\sum_jp_j^2.
\]

Proof: each episode-family indicator is one if selected at least once, with probability \(1-(1-p_j)^K\). Sum indicators by linearity. The second identity sums mutually exclusive same-family events. This is classical occupancy/coupon-collector mathematics.

For K at least 2, \(f(p)=1-(1-p)^K\) is concave, since \(f''(p)=-K(K-1)(1-p)^{K-2}\le0\). Consequently the symmetric sum is **Schur-concave**: any mean-preserving balancing of episode draw probabilities raises (weakly) expected distinct episode-family exposure. With m available equally interpretable families, its maximum is

\[
m\left[1-(1-1/m)^K\right]
\]

at uniform \(p_j=1/m\). A label-only or sampler-only G that can *feasibly* redistribute positive p may therefore raise expected distinct experience at **zero new episode creation**. It cannot create a genuinely novel family where there is only one pre-existing family. This is a diversity *bound*, not a statement that uniform sampling optimizes qualification: task importance, demonstration quality, collection rights and marginal compute cost may make unequal weights economically preferable.

A sensitivity calculation, not an assumed learning law, gives the possible variance consequence. If each family j has an independent mean-zero random effect with variance \(\sigma_u^2\) and each draw has independent noise variance \(\sigma_\epsilon^2\), then a K-draw average has

\[
\mathrm{Var}(\bar Z)=
\frac{\sigma_u^2+\sigma_\epsilon^2}{K}
+\frac{K-1}{K}\sigma_u^2\sum_jp_j^2.
\]

Thus a corresponding random-effects design multiplier is \(1+(K-1)\rho\sum_j p_j^2\), with \(\rho=\sigma_u^2/(\sigma_u^2+\sigma_\epsilon^2)\). This does *not* identify gradient noise, policy generalization or independent information in an actual recurrent learner. The point is to record family identity before equating admitted transition counts to usable independent learning.

## Proposition 2: coverage of a context is not coverage of distinct experiences within it

Split source episodes into customer-relevant archetypes A and B, \(a=p_A\) and \(b=1-a=\sum_{j\in B}p_j\). With K=3 accepted draws, consider **two alternative, explicit** technical-learning maps for the *same proposed original-customer service recipe*:

* **Context-presence map**: a learner qualifies if the three draws include at least one A and one B. Its conditional qualification probability is \(Q_C=1-a^3-b^3=3ab\).
* **Novel-recovery-family map**: a learner qualifies only if the three draws include one A and two **distinct independent** B episode families. Its conditional probability is \(Q_N=3a\big(b^2-\sum_{j\in B}p_j^2\big)\).

Proof: the context-presence event is the complement of all-A or all-B. For the novel-family event, choose the one A position in three ways; the other positions are ordered B pairs with different IDs, total probability \(b^2-\sum_{j\in B}p_j^2\). Both are *countermodel hypotheses*, not robots known to learn by occupancy thresholds.

If B contains at most m_B genuinely distinct episode families and \(a,b\) are known, Cauchy–Schwarz yields

\[
0\le Q_N\le 3ab^2(1-1/m_B).
\]

The upper bound is attained at equal mass across all m_B independent B families; the lower endpoint is attainable with just one active B family, or approached when m_B identifiers all have positive but concentrated weights. At a=b=1/2 and m_B=9, the sharp no-dependence-information interval is [0,1/3]. This is a **partial-identification result**, not a confidence interval. Observing admitted fraction b, K and a nominal count of files is not enough to know which end applies if the true family equivalence/novelty relation is unobserved.

## Synthetic original-customer decision counterexample (same costs and buyer service)

Fix accepted K=3 and a stipulated matched original-customer value of 12 contribution units if newly qualified, with a physically certified and actually available R fallback worth 2 if it fails. E is a *separately* certified generalist whole policy worth 19/5. A source/acquisition program X costs 7/5 and a target grounding/sampling program G costs 2/5 in the same normalized units. These are assumed **complete captured contribution units**: not dataset episode prices, empirical dollars, benchmark-success monetization or independent shadow premiums. Qualification failure leaves the R option under the expressly stipulated physical/rights/admission conditions.

Initial archive: one independent A family has nine processed transitions, one independent B family has one; the source mixture is (9/10,1/10). G matches target semantics and alters eligible sampling so these **same two** families have probability (1/2,1/2), without generating a new family. X instead collects eight *new and independent* B families, each one accepted-weight transition, making A mass 1/2 and nine distinct B families each mass 1/18. Assume identical accepted K and fully specified related processing costs above; no additional effect of G on learning beyond the stated sampling kernel. The resulting exact conditional values are:

| Physically feasible policy | Context-presence Q_C | Value with R fallback | Novel-family Q_N | Value with R fallback |
|---|---:|---:|---:|---:|
| Existing archive + retained R | 27/100 | 47/10 | 0 | 2 |
| G: target alignment / resampling existing archive | 3/4 | 91/10 | 0 | 8/5 |
| X: generate eight independent B families | 3/4 | 81/10 | 1/3 | 59/15 |
| E: already-qualified generalist | not needed | 19/5 | not needed | 19/5 |

Each trained policy's value equals \(2+(12-2)Q-C\) under its stipulations. **Identical aggregated A/B coverage after G and X, identical K and the same buyer service/costs do not identify the investment ranking:** G is best under the context-presence learner, whereas X narrowly beats E and G under the novel-family learner. The old R and all previously feasible training/policy options remain optional, so negative net G under the second hypothesis does not force a loss to the owner of free G data. No historical observation chooses between these learning hypotheses.

The exact [CPU model](episode_support_occupancy.js) / [record](episode_support_occupancy_results.json) enumerates all three-draw ordered histories for the ten-family X archive and verifies the formulas using rational arithmetic. A separate Python Fraction enumeration independently checked the principal fractions. Grid checks for two-family occupancy are *not* proofs of Schur concavity; the derivative above is.

## Distinct feasible interventions and information requirements

1. **G as sampler/annotation treatment.** A feasible G changes p by validating labels, task grounding or weighting *existing admissible episodes*, possibly changing model architecture or compute costs in practice. The pure-resampling counterexample holds those direct effects aside to isolate a missing intermediate channel. If all B training paths are truly ineligible (zero support), simple importance weighting cannot make p_B positive. Grounding that makes previously ineligible but already held episodes admissible is a different, estimable action.
2. **X as source generation or archive inclusion.** New trajectories may enlarge the support m_B; duplicates, correlated rollout clones or replay of one failed recovery do not. Existing archive inclusion (costly training) is distinct from paying to generate new independent failure/recovery data. Source value depends on effective *independent target-relevant* coverage conditional on what the learner already knows and on downstream customer demand.
3. **E as embodiment/menu change.** E may shift which customer services are physically attainable or their resource costs, not merely improve the same classifier. An E that qualifies regardless of A/B training can reduce the marginal economic value of G and X. Physically feasible E availability/lead times and retained R safety are premises to be checked, not inferred from the CPU example.
4. **Production-generated learning.** Service trajectories, errors/recoveries and teleoperation acquired during paid deployment have *both current captured production value and future learning effects*. Account for both through the same dynamic J once, with permissions, qualification and future demand; do not append a standalone data-value bonus to already optimized continuation.
5. **Other source modalities.** Field trajectories, failure/recovery traces, teleoperation, simulation, synthetic and public/pretrained inputs form different provenance, admission and transfer channels. They may substitute or complement after conditional grounding. Nothing in the theorem ranks modalities or makes human data the master ontology.

## Identification and strongest objections

The *technical* evidence must distinguish context presence, episode independence, failure/recovery diversity, qualified held-out original customer recipes and degradation of R. Family identity should be checked through provenance/temporal/scene/controller overlap, not just file hashes. Proposed/admitted weights, episode lengths and accepted update counts need the actual loader version. Equal K matched arms differ from equal proposal cost B; source filtering may change both K and processing latency under a fixed budget. Source/grounding treatments must be learner-wide if shared weights or operator histories cause interference.

The *economic* evidence then needs actual physically signed R/X/G/E policy menus, predeclared original buyer offers (including refused/unserved orders), accepted service, customer payment and refunds, shared operator attention, hardware downtime, rights and current/future resource prices. Whole-policy contribution can sometimes be identified by cluster randomization without attributing every network-mediated causal mechanism; technical mechanism identification needs more orthogonal interventions and may remain only bounded.

The closest prior foundations are occupancy/coupon-collector, majorization/Schur concavity, cluster-effective-sample-size and design effects, factorial causal assignment and the existing DDA future-data/aggregation models. The distinctive intended **synthesis** is connecting legally and physically admitted archive support, learner-wide transfer, joint original-customer qualification and optimized paid production in one falsifiable program; no independent methodological novelty claim is warranted.

**Exact proof gap / continuing intellectual question:** Do version-locked, episode-family-aware archive and loader measurements distinguish novel independent failure/recovery information from relabeled or resampled copies, and does a matched learner-wide inclusion × conditioning intervention change *joint qualified service* sufficiently to reverse X/G/E over the *same signed original-customer policy*? If these observations are unavailable, retain the sharp partial-identification bounds rather than assert a field ranking. November 22 scientific gate remains OPEN; theory priority through December 6, full Christmas roadmap and December 25 23:59 Eastern deadline unchanged.
