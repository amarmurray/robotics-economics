# When Capabilities Become Production — policy-closed interference networks and the value of usable learning

**18 November 2026 | continued, private theoretical argument.** This chapter answers the next question after [safe policy support](SAFE_POLICY_SUPPORT_THEORY.md): when can a measured safe eligible-customer benefit legitimately be transported to the *whole* deployed controller/operator/customer network, especially when grounding or a new source dataset changes the network itself? It refines, rather than replaces, the common \(\,x,g,h\mapsto Q\mapsto V(Q;\omega)\mapsto J\,\) construction and the November 22 integration. Every illustrative contribution below is **synthetic normalized captured accepted-service contribution**, not robot skill percentage, an observed price, or a validated safety benefit.

## 1. The economic unit is a complete, approved adaptive policy

Let \(i=1,\ldots,n\) index pre-action customer opportunity/robot-pool accounting units; let \(\theta\) denote one *persistent* transfer, demand, qualification and recovery regime. A complete policy \(p\) fixes its admissible learning, data-rights, source acquisition, target grounding, embodiment, controller lineage and safe-stop rule over the whole horizon. In each realized history it induces qualified accepted-service recipes \(Q_t(p,\theta)\), the actually attainable order and price environment \(\omega_t(p,\theta)\), dispatch and operator loads, and feasible optimized production \(V_t(Q_t;\omega_t)\). One consistent definition is

\[
Y_C(p,\theta)=\sum_{t=0}^{T}\beta^t
\left[V_{C,t}(Q_t(p,\theta);\omega_t(p,\theta)) - k_{C,t}(p,\theta)\right],
\]

for an *entire interference component* \(C\), where \(k\) contains only real costs absent from \(V\). Captured accepted-service value must include original-window zero orders, competitor reallocation and true customer demand; a pre-counted terminal value is never added again. Old qualified controller \(F\), capable specialist \(S\), source-production \(R\), grounding \(G\) and new embodiment \(E\) are alternative **complete** policies; unapproved recovery actions cannot enter the policy set. Human teleoperation, production trajectories, recoveries/failures, simulation, synthetic, and public/pretrained data may have separate observation kernels, retention rights and costs.

The policy contrast \(J(p)-J(q)=\mathbb E_\theta[Y(p,\theta)-Y(q,\theta)]\) integrates both *learning* and *induced demand*. It is not the price of a trajectory, the effect among post-treatment qualified tasks, nor automatically a worst-regime guarantee. A benchmark cannot be translated directly into this object without the customer-service production map.

## 2. Union of *possible* influence paths, not the observed control-period graph

For a prespecified, physically approved comparison menu \(\mathcal P_{\rm safe}\), define a policy-closed graph \(\overline G\) on primitive units before assignment. Include an edge whenever **some** permitted complete-policy assignment, reachable safe history or regime in the maintained uncertainty set allows the policy/action of one unit to change another unit's future learning checkpoint, task allocation, operator availability, opportunity denominator, accepted service or captured contribution. Retain directed and timestamped edges in the audit; use weakly connected components as conservative assignment units. Common demand displacement is an edge even without shared ML weights. Controller checkpoints can merge components after an update; the graph must anticipate the update, not merely reproduce the baseline logs.

**Conditional proposition (policy-closed cluster consistency).** Assume (i) \(\overline G\) contains every assignment-sensitive directed causal path over the complete horizon under the compared safe policies and plausible \(\theta\); (ii) structural equations for outcomes in a component have no assignment-sensitive parents outside it; (iii) fixed pre-action customer/pool denominators, complete outcome measurement and treatment consistency; and (iv) policies use only their independently physically approved action/recovery supports. Then a component's complete-horizon potential outcome depends on its **own** complete policy assignment, not on assignments in other components. Proof: order the structural equations by time, condition on exogenous inputs and induct over each update; an outside assignment could alter an internal variable only through a path forbidden by (i)–(ii). Shared exogenous shocks may correlate component outcomes and complicate confidence intervals; they do **not** by themselves invalidate randomized *expectation* identification if assignments remain exogenous.

**Necessary audit caution.** A graph assembled from observed, status-quo interactions is not automatically policy-closed. Example: baseline has a controller edge A–B and separate nodes C,D, so clusters appear \(\{A,B\},\{C\},\{D\}\). Under an approved grounding/dispatch policy, B can route customer orders to C. The union graph instead has \(\{A,B,C\},\{D\}\). Randomizing A–B independently of C can contaminate both arms. A complete demand market may be one connected component; splitting that market into many robot-level "samples" is not an identification solution. If the audit cannot exclude an unseen path, graph closure remains a **hypothesis**, not a certificate.

## 3. Identification with complete safe policies, even if old and new policies interfere internally

Let independent assignment *units* be the verified components \(C=1,\ldots,N\). Within each enrolled pre-action stratum, randomly assign an entirely specified admissible network policy \(p\) or \(q\) with known strictly positive probability \(\pi_{C,p},\pi_{C,q}\). The policy may contain shared controllers, endogenous user orders and path-dependent learning **within** its component. Under the closure/consistency assumptions, the ordinary Horvitz–Thompson complete-policy contrast

\[
\widehat\Delta=\frac{1}{N}\sum_{C=1}^{N}
\left[\frac{{\bf1}\{Z_C=p\}Y_C}{\pi_{C,p}}
-\frac{{\bf1}\{Z_C=q\}Y_C}{\pi_{C,q}}\right]
\]

has assignment expectation \(N^{-1}\sum_C[Y_C(p)-Y_C(q)]\), conditional on the complete potential-outcome schedule. This is established randomized-design mathematics, not a new causal estimator. Neither the latent common \(\theta\) nor a paired unit-level cross-world outcome must be observed for the *mean* contrast. A valid population transport still requires pre-action target weights and selection support; a common market shock means independent-cluster standard errors may fail. A mean ranking does not establish same-regime dominance or physical admission.

**Improvement to the prior SS2 route:** If two complete selective policies \(H_G,H_F\) are both independently **physically approved over the entire network**, randomizing *the complete policies* across valid independent supernetworks can measure the whole-network contrast directly. This captures controller broadcast, customer displacement and operator sharing instead of invoking SS2's unverified zero-spillover identity or an assumed \(\Gamma\). It does **not** authorize an unsafe action on excluded sites: safe selective implementation may keep the old controller on those sites while altering other admissible market channels. If there is only one connected network and no genuine reset/independent markets, ordinary simultaneous network randomization gives only one assigned complete outcome; period switchback after persistent learning is not a clean replicate. One then needs verifiable interference restrictions, structural partial identification, or more safe, genuinely independent opportunities—not fictitious sample size.

## 4. Isolation and sharing are different investments, not the same data effect with a nuisance coefficient

Consider safely enrolled A and excluded B, pre-action complete contribution \(Y_A(F)=5,Y_B(F)=5\). Grounding increases A's measured accepted contribution to 7 in every considered world. If a **verified** pinned controller/dispatch/operator/customer cut keeps B's actual fallback production at 5, a genuinely new isolation/coordination cost \(c=1/2\) gives a whole-policy increase \(2-1/2=3/2\). Now suppose the cut is only claimed, not proven. With B's new outcome known merely to be in [0,10], the corresponding *cost-bearing* candidate's complete contrast lies in the sharp unrestricted interval

\[
2+[0-5,10-5]-1/2=[-7/2,13/2].
\]

Endpoints keep A's measured effect and B's baseline identical. The eligible-only gain \(+2\) alone does **not** rank the intervention.

A shared-update alternative may have zero isolation cost, but B can deteriorate to 1 (total 8, gain -2), or improve to 8 through transferable competence (total 15, gain +5). The same A-side qualification and accepted contribution coexist with opposite **whole-network** values. This is not a claim that actual shared updates are harmful. It shows why an eligible-only experiment cannot determine whether extra source data, target grounding, or a new embodiment improves the customer network. The economic interaction is induced by the deployment/reuse topology, not only by the technical learning-map Hessian.

In a second four-*independent-network* synthetic exercise, all fallback totals are 10, and a complete shared-grounding policy yields totals (8,15,8,8), while a fully isolated, cost-inclusive grounding policy yields (23/2,23/2,23/2,23/2). Every network's enrolled A-side improvement is +2. Nevertheless, the true mean shared-minus-old is **-1/4**, isolated-minus-old **+3/2**, and shared-minus-isolated **-7/4**. Enumerating all 16 fair assignments of entire networks gives unbiased HT means 39/4 and 10, unlike an A-only estimate. [Executable exact fractions](network_policy_closure.js) and [stored results](network_policy_closure_results.json) verify this illustrative arithmetic, not a general physical model.

The observed contrast between an isolated training branch and a shared training branch is a **total policy effect**. It cannot be labeled a pure "data-transfer effect" unless rights, hardware, operator allocation, customer enrollment and market dispatch are held fixed or separately identified. The isolation policy must be evaluated *as actually implemented*: altering controller pools can alter both learning and demand.

## 5. A qualified optionality statement, not automatic positive transfer

If source-data access \(x'\) is optional and free, all old qualified and physically admissible complete policies remain available after the access, their feasibility, customer environment and costs are unchanged when selected, and the information set is no worse, then \(\Pi(x)\subseteq\Pi(x\cup x')\) implies

\[
\sup_{\pi\in\Pi(x\cup x')}J(\pi)\ge \sup_{\pi\in\Pi(x)}J(\pi).
\]

The inequality follows by feasible-set inclusion. It is weak, not a guarantee of profitable retraining. In a fixed common ambiguity set, the analogous maximin menu value is weakly monotone. Mandatory broadcast, lost fallback feasibility, resource-consuming curation, displaced operator capacity or a changed demand environment violate the premise; an individual negative-transfer recipe is not a counterexample to free optional access.

A useful empirical experiment therefore differentiates: (a) **data availability** with old controller frozen, (b) training/alignment of a controlled new checkpoint, (c) actual approved deployment using the new checkpoint, (d) its induced customer demand and operator/recovery effects, and (e) an admissible embodiment alternative. The data's future production effect is already inside \(Y\); do **not** add a second learned-data premium. The source-by-grounding interaction in the learning map can be positive while its network-captured production effect is negative, and vice versa. A customer market's service mix determines which transfer becomes valuable.

## 6. What would discriminate the mechanisms

The smallest discriminating dataset consists of a pre-treatment opportunity registry including zeros, physical safety/admission envelope for every complete policy, immutable checkpoint hashes and training lineage, source mix and rights, controller broadcast map, dispatch assignment/bid/cancellation records, shared operator reservations and recovery peaks, and matched held-out **joint** qualified accepted service. Whole-network randomized policy assignment (if safely feasible) identifies an economic total effect; additional controlled training branch comparisons and held-out technical tests are needed to attribute that effect to source transfer versus demand shifts or new-body control reachability. Graph edges must be specified **across possible arms**, not learned only from the arm's observed successful trajectories.

The accessible pinned [Open-RMF demo description at commit 05f5e3f](https://github.com/open-rmf/rmf_demos/blob/05f5e3faad507c0d67d9343efc81093ee2e30610/README.md) and [rmf_task description at 92832a6](https://github.com/open-rmf/rmf_task/blob/92832a6dbd204f7fce5b3e6ea000339e0dc4ac96/README.md) provide *public examples* of multi-fleet dispatch/bid pathways. The [ROS 2 multi-robot task guide](https://osrf.github.io/ros2multirobotbook/task.html) likewise describes common task allocation. None proves a target commercial robotics fleet uses Open-RMF, shares weights, has safe human recovery capacity or produces a measured customer-economic effect. **No customer/pool-level source-to-accepted-service panel, approved network trial, official BEA/BLS numeric production crosswalk or physical safety certificate is available here.**

Closest prior foundations include Hudgens and Halloran, *Toward Causal Inference With Interference*, JASA 103 (2008), doi:[10.1198/016214508000000292](https://pubmed.ncbi.nlm.nih.gov/19081744/) (partial interference, two-stage experimental designs); Aronow and Samii (2017), doi:[10.1214/16-AOAS1005](https://doi.org/10.1214/16-AOAS1005) (exposure mapping); and earlier network-coupling and safe-support chapters in this project. DDA arXiv:2606.10127 §5 and Appendix B already contain forward-looking data value and aggregation ideas. We claim **a precise robotics economic research design and falsifiable argument**, not novelty in causal interference estimation, optionality, network graphs or data accumulation. See [proof ledger](POLICY_CLOSED_NETWORKS_PROOF_LEDGER.md), [prospective empirical protocol](POLICY_CLOSED_NETWORKS_EMPIRICAL.md), and [separate exercises/solutions](POLICY_CLOSED_NETWORKS_EXERCISES.md).

**Persistent proof gap and next action:** find a genuinely available, versioned source of *actual target* controller/dispatch/operator/customer-network architecture and approved safe population; without it the proposed union graph is not verified. Specify pre-action shared-market versus independent-supernetwork eligibility and construct the narrowest safely comparable whole-service source/grounding/qualified-specialist policy pair; if the true market is one inseparable connected unit, retain structural partial bounds and do not claim replicated randomized identification. November 22 synthesis and every later scientific gate remain open. Final target December 25, 2026, 23:59 Eastern.
