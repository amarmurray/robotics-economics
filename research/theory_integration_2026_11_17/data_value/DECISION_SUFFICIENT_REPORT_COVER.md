# Decision-sufficient production reports: action covers, higher-order conflicts, and heterogeneous signal complementarity

**22 November 2026.** A continuation of *When Capabilities Become Production*, not a new question or independent paper. November 22 Models A/B scientific acceptance **OPEN**. All numerical examples below are **synthetic normalized accepted-and-paid contribution**, not robot measurements, forecast dollars, or benchmark conversions.

## 1. Which distinctions does a source-trained producer economically need to remember?

Previous chapters show that a report-blind compressed policy can lose exactly its full-information Bellman occupancy regret; SG can look inferior to a new embodiment E solely because its original-buyer report was discarded. The next constructive problem is narrower: **at a signed production decision, how many distinct lawful report outcomes are sufficient to select an optimal accepted-and-paid service action?** The amount of raw source data is not necessarily the amount of **decision-relevant** data. A dashboard that groups two customer/order/learner/rights states together is harmless only if it preserves the ability to select a common paid-optimal permitted action. With more than two candidate actions, testing pairs of states can fail to detect a higher-order conflict.

Fix one post-observation stage of a full-horizon qualified-service program \(k\in\{R,S,G,SG,E\}\). Let \(H\) be a finite set of physically realizable *available-information* histories, each with positive original-market probability \(p_h>0\). Histories contain the original eligible offered order/no-order opportunity, learner/checkpoint lineage, licensed rights, physical embodiment, robot/operator constraints, customer offer and refund conditions, and information available **before** dispatch; latent customer needs unavailable to either permitted actor do not count as reportable history. Let \(M(h)\neq\varnothing\) be the certified physical and legal action menu at that history. Let
\[
q_h(a)=Q^*_{k,t}(h,a)
=\mathbb E[\text{current accepted, finally settled net production}+
V^*_{k,t+1}(H_{t+1})\mid h,a]
\]
for lawful \(a\in M(h)\). Thus later production-generated data and learning-generated future service are already inside \(q\). Upfront training/body/signal costs are accounted for once in the relevant initial program or explicit signal action, never again as a data premium. This is a **fixed controlled environment**, not an assumption that S/G/E have the same \(q\), operator budget, demand distribution, or action set.

An exogenous, legally deployable report \(\phi:H\to\{1,\dots,L\}\) induces cells \(C_\ell\). A cell action must lie in \(\bigcap_{h\in C_\ell}M(h)\); if this intersection is empty, that report compression is *inadmissible*, not a missing numeric outcome. Its optimized post-report value is
\[
W(\phi)=\sum_{\ell}\max_{a\in\cap_{h\in C_\ell}M(h)}
\sum_{h\in C_\ell}p_h q_h(a).
\tag{1}
\]
The fully available-information benchmark is \(W^*=\sum_h p_h\max_{a\in M(h)}q_h(a)\). An ideal exogenous report is **free at this stage** only when no reporting, physical, rights, inference or time cost is incurred. It is not a claim that acquiring target labels/teleoperation is free.

## 2. Proposition: the exact minimum number of decision-sufficient report symbols is a set cover

Write \(A^*(h)=\arg\max_{a\in M(h)}q_h(a)\) and, for each *identical implementable action* \(a\), \(F(a)=\{h:a\in A^*(h)\}\). The symbol alphabet is a set of genuinely common lawful dispatch actions, not a fiction that differently signed controllers are interchangeable.

**Proposition (optimal-action cover and report budget).** Under the finite, fixed-\(p\), fixed-\(q\), exogenous unrestricted-report conditions above:

1. \(W(\phi)=W^*\) if and only if every positive-mass cell has a common lawful Bellman-optimal action: \(\bigcap_{h\in C_\ell}A^*(h)\neq\varnothing\).
2. The minimum number of positive-probability symbols in a lossless report is
\[
\kappa=\min_{B\subseteq A}\left\{|B|:\bigcup_{a\in B}F(a)=H\right\}.
\tag{2}
\]
3. More generally, if at most \(L\) freely designed symbols can be used, the sharp oracle frontier is
\[
W_L=\max_{\substack{B\subseteq A,\ |B|\le L\\B\cap M(h)\ne\varnothing\ \forall h}}
\sum_h p_h\max_{a\in B\cap M(h)}q_h(a).
\tag{3}
\]
For \(L<\kappa\) there is strict positive regret; for \(L\ge\kappa\), \(W_L=W^*\). Where no \(L\)-action cover of lawful menus exists, the compressed policy is infeasible rather than zero-value.

**Proof.** For every cell action, its difference from the full-information action maximum is a nonnegative weighted sum of pointwise Bellman gaps. Positive probabilities make the sum zero exactly when that same action is optimal at every history in its cell. Selecting one common action per lossless cell yields at most \(L\) actions whose \(F(a)\)'s cover \(H\). Conversely, given any cover of optimal-action sets, assign each history to any covering action and use that action as its signal symbol: all resulting cells have a common lawful optimum. This proves (1)-(2). For general (3), every \(L\)-symbol policy uses at most \(L\) actual actions; its value is bounded by the right-hand sum over those actions. For any feasible \(B\), assign each history a best lawful action from \(B\) and label the report by that action, attaining the sum. QED.

**Crucial implementability qualification.** Equation (3) is a *perfect-observation oracle* for compressing already-reportable histories. In a real fleet, no permitted sensor, legal data right, timely buyer-order report, or available predecision human observer may implement the map \(h\mapsto a\). Feasible signal functions, privacy and reporting latency can make \(\kappa\) unattainable. A signal that itself changes demand, qualification, the learner, safety approval or operator occupancy changes \(q\) and belongs in the full dynamic \(J\), not equation (3).

### Counterexample: a conflict is not necessarily pairwise

Three equally likely original production contexts admit three lawful actions \(a,b,c\). Paid-optimal action sets are \(A^*(h_1)=\{a,b\}\), \(A^*(h_2)=\{b,c\}\), and \(A^*(h_3)=\{a,c\}\). Give each listed optimal action unit accepted-and-paid contribution, each remaining action zero. **Every pair** of contexts shares a paid-optimal action, but **all three do not**. A one-symbol report obtains \(2/3\) against full \(1\), so the report-blind loss is \(1/3\); a two-symbol partition is lossless. The minimal incompatible set is a three-way hyperedge. A pairwise conflict graph has no edges and incorrectly certifies one symbol. As new source-trained recipes and an additional physical embodiment expand the lawful action menu, these higher-order incompatibilities can appear even if every two-context comparison passes.

The fixed exogenous statement is an elementary set-cover/hypergraph application, **not a claim of novel combinatorics**. It is economically useful because deciding how much customer/learner/rights information to preserve is not equivalent to retaining all raw trajectories or testing two-way accuracy rankings.

## 3. Oracle report capacity has diminishing returns; actual signal fields need not

Suppose a common safe retained controller \(a_0\) is physically and legally lawful at every \(h\), with constant fixed \(q\). Let \(B\) be the set of additional candidate *action labels* that a hypothetical perfect report can identify. The incremental optimized contribution
\[
f(B)=\sum_h p_h\big[\max\{q_h(a_0),\max_{a\in B\cap M(h)}q_h(a)\}-q_h(a_0)\big]
\tag{4}
\]
is normalized, nonnegative, monotone and **submodular** in \(B\). For \(B\subseteq C\), the incremental gain of offering action label \(b\) is \(\sum_h p_h\max(q_h(b)-m_B(h),0)\) where \(m_B(h)\) is the current best lawful action payoff; because \(m_C(h)\ge m_B(h)\), its marginal gain decreases. This permits familiar greedy cardinality-bound approximations for an *oracle action-label budget* (Nemhauser–Wolsey 1978 and successors). It does **not** establish submodularity of acquiring source data, paid field trials, report fields or embodiments: those interventions change the state distribution, qualification and the mapping from observable signals to lawful actions.

**Exact synthetic complementarity of two actual report fields.** Let two binary physically observable, legally retainable context fields \(x,y\) be independent and equally likely. The paid-optimal dispatch is \(a\) if \(x\oplus y=0\), \(b\) otherwise; a correct dispatch gives one accepted-and-cleared unit, the other zero. With neither report, \(W=1/2\). With *only x* or *only y*, \(W=1/2\) still: both have **zero marginal economic information value in isolation**. With both, \(W=1\): the report-field interaction is \(+1/2\). This is consistent with (4), because (4) concerns an oracle selecting an action-labeled partition from fully observed context, whereas \(x,y\) are externally constrained measurements. It also shows why a field such as buyer order may require a jointly observed learner-status/robot-body or licensed-rights condition before it changes the correct paid dispatch.

Thus **a measurement plan that retains only individually useful variables can discard a jointly decisive field**. The result uses prior decision-information mathematics, not a discovered robotics data-scaling law.

## 4. S/G/SG/E and recursive production: scope of the certificate

The source-to-qualification learning map changes \(M_k(h)\), \(q_{k,h}(a)\) and potentially the history distribution itself. Source inputs retain separate lineages—successful field trajectories, failures/recoveries, teleoperation, simulation, synthetic and pretrained/public material—with signed training/usage rights, compute/curation and safety costs. \(G_{\mathrm{info}}\) acquires a timely original-buyer or physical-context report, whereas \(G_{\mathrm{train}}\) changes actual physical target ability; \(E\) may create new bodies, operator footprints and throughput. A source-qualified specialist menu may require two report categories where a universal E controller needs only one, although SG can still generate more production in aggregate. Retaining the old controller means optional freely accessible source data cannot lower gross optimized value when the full feasible policy set is nested. It does **not** mean collecting data through productive failure or teleoperation has zero opportunity cost.

For dynamic Model B, the earlier **Bellman occupancy-regret identity** is the correct global test. Conditional on a particular lawful policy's reached full histories at decision time \(t\), any compressed signal with zero program loss must select an action in the full Bellman-optimal set at every reached history with positive occupancy. The action-cover construction gives a *stagewise, fixed-occupancy diagnostic*, not an unrestricted dynamic optimum: acquiring a report, changing dispatch, creating a failure/recovery example, losing data rights or changing buyer demand can change tomorrow's reachable histories. The joint learner/operator/customer/rights controlled transition must still be estimated or bounded, and a report chosen at time 0 cannot assume it knows a future action's full-information state. Missing support for action \(b\) is not \(q_h(b)=0\); unapproved \(b\) is absent from \(M(h)\).

With action-conditional paid-Q bounds, a *sufficient* conservative certification of a proposed compressed action \(a_C\) is \(\underline q_h(a_C)\ge\max_{b\in M(h)}\overline q_h(b)\) for every supported \(h\in C\). If no candidate action even meets the weaker possible-optimum test \(\overline q_h(a)\ge\max_b\underline q_h(b)\) across all \(h\in C\), **no joint Q completion within those valid bounds can yield a common optimum**; ambiguous overlapping bounds must remain unresolved. Actual shared-learner correlated Q restrictions should be enforced jointly, rather than treating independent rectangles as reality. The economically decisive observations are original-buyer offered/no-order demand, lawful action identity, target report timing/rights, accepted/refunded/finally settled production, operator and recoveries, and learned future qualified service—not accuracy percentages.

## 5. Evidence and research implication

This yields a precise prospective audit of a report that has been pooled across customers: (i) construct real approved action identities and original offered-buyer conditional paid-Q tables or defensible bounds, (ii) find the sets of contexts where each action might be optimal, (iii) test *all-way* intersection rather than only pairwise conflicts, (iv) compute attainable reports from physically available, licensed predecision signals, and (v) price the improvement through the same complete-program \(J\) used for S/G/E, including displaced productive time and future learning. An oracle \(\kappa\) smaller than the number of raw recorded states is a research hypothesis about economic **decision-sufficient telemetry**, not a promise that practical sensing or machine learning can achieve it.

[Prospective support protocol](DECISION_SUFFICIENT_REPORT_COVER_EVIDENCE.md), [exact executable](decision_sufficient_report_cover.js) and [record](decision_sufficient_report_cover_results.json), [independent Fraction checker](decision_sufficient_report_cover_independent.py), and separate [exercises](DECISION_SUFFICIENT_REPORT_COVER_EXERCISES.md)/[solutions](DECISION_SUFFICIENT_REPORT_COVER_SOLUTIONS.md) accompany this derivation. The exact enumerator covers 19,600 nonempty optimal-action profiles with 931,401 integer checks, a separate 729 payoff table submodularity audit with 39,366 checks, and independent Python rational counterexample verification. Enumerations corroborate the combinatorial proofs; they are not independently reviewed theory or field validation.

**Closest prior methods:** Blackwell, *Equivalent Comparisons of Experiments* (1953), https://celebratio.org/Blackwell_DH/article/26/ ; standard sufficient-decision/action aggregation and finite MDP policy refinement; Nemhauser and Wolsey, *Best Algorithms for Approximating the Maximum of a Submodular Set Function* (1978), https://doi.org/10.1287/moor.3.3.177 . DDA §5 already values production-generated future data and Appendix B already studies aggregation complementarity. No assertion of first discovery of these foundations or calibrated robotics performance is made. **Candidate contribution** is the physically authorized, economically validated source→learner/rights→optimal production-decision telemetry bridge; that complete empirical bridge remains unestablished.

**November 22 gate:** the full Models A/B synthetic argument and a new implementability-sensitive report-capacity theorem are mathematically constructed; original buyer- and controller-matched paid Q, lawful/physically implementable report classes, actual S/G/SG/E embodiment opportunity sets, numerical official interindustry BLS/BEA production coefficients, complete repo CI and independent novelty review remain unverified. November 22 scientific acceptance remains **OPEN**. Theory remains the majority focus through December 6; the final target is December 25, 2026, 23:59 America/New_York.
