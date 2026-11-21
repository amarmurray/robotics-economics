# Decision-sufficient economic history: when a source-trained robot can serve the buyer

**21 November 2026 — continuation of *When Capabilities Become Production*, November 22 Models A/B. Scientific acceptance OPEN.**

The preceding [licensed triple theorem](THIRD_ORDER_LICENSED_PRODUCTION_AND_ABSTRACTION.md) identifies a missing third-order original-buyer paid-and-rights event C=UVL. This chapter asks the *next*, not a separate, question: **if C were actually recorded, when would C (or any other compressed learner/operator/buyer/rights state) suffice to choose source data plus target grounding SG versus embodiment E in an adaptive fleet?** The answer is an exact controlled-continuation condition, a quantitative conditional approximation and a counterexample in which matching C and all marginal technical qualification records still makes a compressed economic decision choose the wrong investment. All values below are synthetic normalized finally-paid contribution, not observed robotics revenue.

## Economic histories and program comparison

Let h_t contain the original buyer's offered order (including declined and unattempted orders), full-task qualification, retained model/checkpoint and embodiment, source-specific permitted data and expiry, robot/operator capacity, new learned service recipes, prospective buyer demand, legally permitted actions and finally cleared settlement/refunds. F field success/failure/recovery, licensed T teleoperation, M simulation/synthetic and public/pretrained inputs are *different* interventions; they are not collapsed into a generic human-data quantity. A legally signed program a ∈ {R,S,G,SG,E} determines its nonanticipating lawful action menu A_a(h_t); it can include the old controller R as an option.

For a finite production-and-learning horizon H, define the **one** optimized program value

\[
J_a=\sup_{\pi\in\Pi_a}\mathbb E_\pi\left[\sum_{t=0}^{H-1}r_a(h_t,u_t,\xi_{t+1})\right],
\]

where each r includes accepted and finally paid original-buyer service, returns/refunds, operator and robot opportunity, licensed acquisition/curation/training, manufacturing or embodiment expenditure, and legitimate later paid new customer services **once**. Resources and settled receipts can be incorporated as physical state/feasible actions or supported dual upper certificates; no extra "future data premium" is added. If the operating environment changes customer demand in response to a, use the correct program-specific conditional law. Policies observe the actual lawful buyer/order history, not an artificial dashboard reduction.

## Proposition 1: sufficient economic continuation quotient

For each program a and date t, take a measurable abstraction s_t=σ_{a,t}(h_t) on complete legally reachable histories. Suppose *uniformly across all histories mapping to each s*, not merely conditional on an averaged log sample:

1. All those histories have **the same legally and physically feasible actions** A_a(s), including old-policy fallback, new learned recipes, future services and allowed data uses.
2. For each available action u, the conditional expected complete net paid one-stage contribution equals a common \bar r_{a,t}(s,u).
3. For each available action u, the conditional distribution of the *next abstract state* equals a common \bar P_{a,t}(s'|s,u). Future rights expiry, learner checkpoint/qualification, buyer orders, settlements and shared operator capacity that matter to future actions must be represented inside the next-state law.

Then the Bellman recursion on (s,A,\bar r,\bar P) exactly equals the optimized full-history value at every reachable h. Consequently, comparing two closed programs' quotient values gives the same SG–E economic sign as comparing their original full-history J values, for a common original-buyer market and fully accounted program costs.

**Proof.** At t=H both continuation values are zero. If V_{t+1}(h')=\bar V_{t+1}(σ_{a,t+1}(h')), conditional expectation of the next continuation depends only on \bar P(s'|s,u) by condition 3. By condition 2 the conditional stage return is \bar r(s,u), and by condition 1 the maximization ranges over precisely the same feasible u. Thus V_t(h)=max_{u∈A(s)}{\bar r(s,u)+\sum_{s'}\bar P(s'|s,u)\bar V_{t+1}(s')}=\bar V_t(s). Induct backward. The optimal quotient policy is therefore implementable on the true histories because its actions are lawful everywhere in its cell. No independence of buyers, sources or qualifications is required.

This is a **sufficient**, not a necessary, criterion for a particular economic objective. Some different transitions have exactly offsetting effects on a particular optimized value. It is also *program-relative*: R and SG need not have identical state kernels or action menus. A shared cross-program schema is useful only when it preserves each program separately. A value-equivalent partition for one historic controller need not remain valid after source training generates a new service or an embodiment creates a new physical action.

A constructive finite-system audit is backward partition refinement: at each date group histories only if they have the same lawful action menu and, action by action, identical conditional net return and identical probability mass assigned to every next-date continuation class. Begin with the complete history and merge only certified equivalent cells. This is a controlled state aggregation/bisimulation construction; its economic content comes from what counts as paid service, demand, rights, shared opportunity and lawful future production, not a new general state-abstraction theorem.

## Proposition 2: approximate sign certificate and its scope

Suppose a candidate abstract law for each a has **exact action-menu equality** at every admissible full history, conditional mean stage-reward residual at most ε_{a,t}, and total-variation distance between the next-abstract-state transition laws at most δ_{a,t}, uniformly over every full history and action. Assume all true and abstract one-stage net contributions lie in [-B_a,B_a]; the continuation horizon has H dates. Then

\[
|J_a-\bar J_a|\le
\eta_a=\sum_{t=0}^{H-1}\epsilon_{a,t}
+2B_a\sum_{t=0}^{H-1}(H-t-1)\delta_{a,t}.
\]

With time-homogeneous ε,δ this becomes Hε+B_a H(H−1)δ. In particular the true comparison lies in
\[
J_{SG}-J_E\in[\bar J_{SG}-\bar J_E-(\eta_{SG}+\eta_E),\ 
\bar J_{SG}-\bar J_E+(\eta_{SG}+\eta_E)].
\]
Only a strict non-overlapping sign interval identifies the superior program.

**Proof.** At each history, the difference between two optimal-action maxima is bounded by the largest action-specific difference. Stage mean error contributes ε_t. Add and subtract the same projected true next-value; the continuation error contributes its inductive supremum. For the abstract future value, bounded rewards imply |\bar V_{t+1}|≤B(H−t−1). For distributions separated by total variation δ, the expectation gap of a function bounded in [-M,M] is at most 2Mδ. Sum the errors backward and then integrate over the original same-market initial states. The comparison bound follows by the triangle inequality. This is a standard finite-horizon simulation-type bound, not a new result about neural data scaling.

If program-specific feasibility menus differ *within* a proposed abstract cell, no δ/ε argument above is licensed. An unmeasured action-set gap, an unsupported newly learned embodiment, or invalid retention rights must be handled by a separate lawful full-history opportunity upper bound or a finer state; simply writing ε=0 for observed actions is not a solution. Averaged, logged or on-policy mean error does not satisfy the uniform premise.

## Constructive failure: C=UVL is known exactly but the investment sign flips under compression

Let date-0 U=V=L=1 and C=1 deterministically for both investment alternatives. The initial original-buyer paid contribution 2 is common and therefore cancels from the decision. A single date-1 operator slot can serve **one** subsequent newly qualified whole service. The actual offered order Z∈{A,B} is observed by the operator *before* dispatch, with P(Z=A)=P(Z=B)=1/2. A service attempted for the wrong original-buyer request produces zero cleared payment; a correct one yields 1 normalized contribution. Costs and rights are already included and valid. This is a hypothetical signed law, not actual physical approval.

Old R qualifies only A, so both with and without Z observation its optimized incremental value is 1/2. A licensed source-plus-grounding intervention SG expands qualified legal production to **both** A and B, retaining R. A lawful embodiment E has one generally useful future service with 3/4 finally-paid probability; E also retains R, so its best value is 3/4.

If a dashboard compresses the state to C and thereby **forgets** the offered original-buyer order Z, the best C-measurable SG policy chooses A or B *before knowing which one is wanted*. Its incremental value is max{1/2,1/2}=1/2, so the compressed decision incorrectly ranks E over SG by 1/4. In the actual full-history economy the operator observes Z and dispatches the matching service. SG earns 1, beating E by 1/4. Thus the **same measured C**, the same technical qualification set and the same fixed market can imply opposite investment recommendations if the abstraction loses decision-relevant demand information. A structural transfer law that predicts technical capability B is economically incomplete without the buyer-conditioned feasible dispatch and settlement law.

More generally, for p=P(Z=A), source access to B gives
\[
J_R=p,\quad J_{SG}^{\mathrm{coarse}}=\max\{p,1-p\},\quad
J_{SG}^{\mathrm{informed}}=1,\quad J_E=\max\{3/4,p\}.
\]
The economic interaction of **source-enabled production flexibility** and costless observation of buyer demand is
\[
[J_{SG}^{\rm informed}-J_{SG}^{\rm coarse}]
-[J_R^{\rm informed}-J_R^{\rm coarse}]
=1-\max\{p,1-p\}=\min\{p,1-p\}.
\]
At p=1/2 this is 1/2. Even a perfectly qualified new B service adds **zero** paid economic value in the C-only market because the robot cannot target it to an unobserved order; when the matched order is observable, that same capability adds 1/2. This is endogenous complementarity between a productive option and the relevant buyer-order signal, not intrinsic positive additive neural transfer, and not two separately booked benefits. Data for capability training and data revealing **which order to serve** are different objects.

The failure satisfies exact *average* stage-reward calibration for both A and B under the original 50/50 buyer mix: each appears to pay 1/2. But the conditional action reward in each actual Z history is 0 or 1, giving a uniform residual of 1/2. The one-period η=1/2 bound above is attained. Averages over a pooled operator's customer history are therefore insufficient for a program-level sign certificate even when the global C rate is 100%. The example also retains optional R and lawful E fallback, avoiding a claim that free optional data availability intrinsically destroys old productive value.

## Economic implications and discriminating evidence

The right abstract state is not "everything logged" or a universal C triple. It is a *program- and objective-sufficient continuation*: qualified options × legally usable learned state × actually offered original-buyer demand × scarce physical/operator opportunities × settlement state. On one task/market, C plus a finite rights expiry and demand variable might be sufficient. In a pooled recursive fleet, new learned embodiments, operator substitution, customer repricing, cross-fleet model updates and rights propagation can make it insufficient again. A state refinement should be justified by an **action-conditional economic distinction**, not by added feature count.

One prospective original-buyer study would first register the full lawful customer/learner/operator exposure graph and match interventions for old R, S, G, SG and E. Record when each order actually became observable, offered and accepted, matched signed robot action, complete service qualification, attempted service, refunds and finally cleared payment, cross-task operator capacity, source provenance, training/reuse expiry and which future learned service became feasible. *Only if physically and contractually approved*, test whether action-conditional paid-value and next-qualification/rights transitions differ across histories that a proposed dashboard merges. Where an admissible action has no observed support, use a defensible resource/demand/legal upper envelope or leave SG/E partially identified. Do not infer field ε or δ from our synthetic enumeration or from broad task benchmark pass rates.

Consequences for the full program: the optimized production table is still the value map; data sources/grounding/embodiment shift the legal policy menu and conditional kernels. Multilayer customer-demand feedback and shared operators determine whether any qualified capability becomes paid production. Production-generated licensed data feeds the next learner state; modeling it requires the next-history closure rather than a second option-value term. Generalist versus specialist and new embodiments enter through distinct feasible columns, and ownership/data-rights enter the lawful transition and captured value, not as a disconnected financing contract. Numerical BEA/BLS production-network coefficients, actual customer paid evidence and physically authorized comparative programs are still absent.

## Prior art and status

Li, Walsh and Littman (2006), [*Towards a Unified Theory of State Abstraction for MDPs*](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/camera-ready-9.pdf), develop abstraction properties; Ferns, Panangaden and Precup (UAI 2004; [finite-MDP metric preprint](https://arxiv.org/abs/1207.4114)) study quantitative state similarity. Blackwell (1953), [*Equivalent Comparisons of Experiments*](https://celebratio.org/Blackwell_DH/article/26/), is antecedent to the value-of-demand-information interpretation. Standard finite-horizon dynamic programming, total-variation coupling, flexibility/real-option arguments and the earlier DDA §5/Appendix B already cover relevant methodological foundations. This chapter is a conditional application and candidate roboeconomic synthesis, **not an independently established novel theorem or empirical robot deployment estimate**.

See [unpopulated validation protocol](ECONOMIC_CONTINUATION_QUOTIENT_EVIDENCE.md), [exact synthetic source](economic_quotient_demand.js), [record](economic_quotient_demand_results.json), [independent rational checker](economic_quotient_independent.py), [exercises](ECONOMIC_CONTINUATION_QUOTIENT_EXERCISES.md) and [solutions](ECONOMIC_CONTINUATION_QUOTIENT_SOLUTIONS.md). The JavaScript program checked 146 exact synthetic identities over 17 buyer market compositions; the separately executed Python Fraction audit checked 73 assertions. These are arithmetic tests, **not proofs** of the uniform-field premise or originality.

**Next exact gap:** identify a lawful, closed learner/operator/buyer/rights state and auditable conditional action-menu/paid-production/next-state kernels for the same original SG/E market. If this cannot be supported, retain partial identification, no winner. November 22 Models A/B scientific acceptance OPEN, theory priority through December 6, and December 25, 2026, 23:59 America/New_York final target unchanged.
