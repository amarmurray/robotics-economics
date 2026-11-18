# Policy-induced target support: a missing link between data transfer and customer production

**Private integrated theory, 18 November 2026.** Continues [shadow learning](SHADOW_LEARNING_AND_TARGET_SUPPORT.md) and [passive data/embodiment choice](PASSIVE_SUPPORT_AND_DECISION_REGRET.md). All numerical values below are exact *hypothetical* captured contribution, not measured deployment effects. This is not a new model track or a claim of novelty.

## Intellectual question

A rights-cleared, causally B-inert copy of existing F production observations may improve an offline A learner, yet A's new policy may visit action/recovery, customer-demand and operator states that neither F nor the previous A version visited. The relevant target support is therefore **induced by the learned controller**, not the volume or marginal success rate of the source corpus. Source learning changes qualification; grounding changes evidence and possibly qualification; new embodiments change the required service recipe. All three pass through the same optimized qualified production value V(Q;omega) and the same complete-history objective J. Neither a diagnostic regret improvement nor a training metric is an extra cash flow outside J.

## Formal environment

Fix a finite horizon t=0,...,T−1 and a learned policy pi, including body, checkpoint, source-data inclusion, safety/rights versions and a specified customer horizon. H_t is the entire relevant history: controller lineage, original B orders, A accepted/rejected orders, customer demand and substitution, shared dispatch, operator queues and hard peak resource commitments, source/recovery data and known physical restrictions. The policy chooses a_t based on its visible information. C_t is a *versioned joint evidence domain* of history-action pairs on which the **whole next-history and accepted-service conditional kernel** has been identified; a sensor observation or separately measured component success does not by itself establish C_t. Physical approval is separate from statistical support. Define tau=inf{t<T:(H_t,a_t) not in C_t}, and tau=T if no exit.

Consider possible complete-network worlds M agreeing on (i) initial-history law, (ii) the joint transition and accrued contribution law on every reachable pair of C_t and (iii) the fixed policy's decisions on these histories. Let the final total captured net contribution Y_pi include paid learning costs, customer displacement, foregone service, and collected cash exactly once, with *global* bounds L≤Y_pi≤U. On no-exit histories the complete return is determined by the identified kernels.

### Proposition: learned-policy first-exit economic envelope

The first-exit probability p=P_pi(tau<T) and K=E_pi[Y_pi 1{tau=T}] have the same value across all M. Therefore,

    K+L p ≤ E_M[Y_pi] ≤ K+U p.

For the unrestricted extension class allowing every exit-history total return to attain either bound consistently with the certified prefix, the interval is sharp. Otherwise it is only an outer bound. In particular, a physical/customer constraint or a known prefix may make either endpoint impossible.

**Proof.** Couple two possible worlds using the identical initial law, chosen actions and *joint* next-history/payoff kernels as long as the history-action remains in C. Induction gives an identical stopped path and no-exit return law, hence common p and K. Decompose expected total contribution into no-exit and exit terms; on exit, Lp≤E[Y1{exit}]≤Up. Under an unrestricted consistent extension, set the exit return to L or U to attain the endpoints. This is a stopped-process support argument, not a result that model uncertainty can be safely probed in the field.

If an exited prefix h has already earned **one counted** value R(h), and remaining accepted service, costs, operator recovery and market substitution lie in [ell(h),u(h)], the sharper bound is K+E[1{exit}(R+ell)] ≤ E[Y] ≤ K+E[1{exit}(R+u)]. The previously derived complete-order LP can tighten these continuation bounds **only with genuinely audited horizon-wide order-loss and resource constraints**, not by declaring an arbitrary k or a benchmark-value-to-dollar translation. Same-world matched comparison may be tighter than subtracting separate A and S intervals.

### Critical condition

p is under the *new learned policy pi*, not the original F data distribution. The stopped law is identified only if its certified target joint kernels and policies permit constructing the rollout *up to exit*; source logs alone need not supply those kernels. A signed read-only copy that is inert for B before A admission does not establish post-admission A occupancy or exclusion of operator/customer demand effects. A rollout absent physical approval is inadmissible, regardless of how attractive the economic lower bound looks. Optional retained F/S and old checkpoints remain in the feasible choice set.

## Structural counterexample and alternative investments

F can stay in s0 indefinitely. Candidate A takes an independently characterized action from s0 and reaches a supported ordinary whole-service state c with probability 3/4 or a target recovery/customer state u with probability 1/4. All F logs and all observed supported A data have identical laws in two worlds, but A's complete market contribution at u differs. No volume of identical F data identifies that target counterfactual without a validated physical/action bridge; the unknown path can include joint qualification failures or displaced B orders.

Assume **hypothetically physically approved** policies with c complete-service contribution 2, u contribution y∈[0,4], and A integration cost 1/10. Then A∈[7/5,12/5], versus competent S=2 and retained F=1. This interval straddles S. The following are three different *conditional* interventions, not one parameter sweep:

1. A controlled, rights-cleared shadow source-copy training comparison independently verifies a change in **joint accepted-service** contribution at c from 2 to 3, retains exactly the old 3/4–1/4 reachability, leaves B/customer/operator states unchanged, and incurs total cost 3/20. A_copy∈[21/10,31/10]. Its guaranteed improvement over S is 1/10 despite no new information about u. This is a *developmental Q effect*. Importantly, if training actually changes Pr(u) to 1/2, its lower contribution is only 27/20, and the claimed guarantee disappears.
2. Independently approved grounding identifies/bounds **complete** u service to [3,4], while leaving c and reachability fixed, with total cost 3/20. A_ground∈[21/10,47/20]. This is improved target **support**, and need not involve a source-training gain.
3. A wholly supported, separately qualified new embodiment supplies gross 11/5 service with body/admission cost 1/4, net 39/20: a zero-support-gap body still loses to S=2 on customer economics.

The changed probabilities and returns are assumed for a structural witness and **never** equated with a test accuracy or operator hours observed at a customer. Any safety, rights, demand, margin or interference failure removes the relevant conditional ranking; unsupported deployment is not approved by these calculations.

## Learning, acquisition and identification

Production logs may have positive transferable developmental value while providing zero information about a persistent unsupported target return. Deliberate grounding, teleoperation recovery, simulation, synthetic and public/pretrained representations can each contribute to target coverage through *different* provenance and validated transfer rules; no modality is the master ontology. More routine source volume need not shrink first-exit probability under a different controller. A source-trained A can also generate its own new recovery states, making routine production-generated data an endogenous process.

A credible matched experiment separates (i) use/no use of versioned B source-copy in offline training, (ii) the attained joint A qualification and qualified customer production under the fixed checkpoint, (iii) that checkpoint's *own* stopped occupancy and recovery load, (iv) explicit target grounding or body change, and (v) old B accepted orders, demand and competent F/S on the identical horizon. Whole-network coupling rules out treating robot-level assignment as independent market units.

## Prior art, objections and next proof gap

Learner-induced covariate shift is established in Ross, Gordon and Bagnell, *A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning* (2011, PMLR 15:627–635, https://proceedings.mlr.press/v15/ross11a.html). Partial offline-RL coverage and robust uncertainty are already addressed in Shi and Chi (2022, arXiv:2208.05767, https://arxiv.org/abs/2208.05767). Farboodi, Koh and Xia, *Data-Driven Automation* (2026, arXiv:2606.10127, https://arxiv.org/abs/2606.10127), already incorporate endogenous data value and aggregation. The stopping bound is standard mathematics; a robotics-economic service/qualification synthesis is not independently validated novelty. An established cross-body invariant or independent certified safe-stop may legitimately shrink the unidentified region; no blanket claim that source data cannot transfer is made.

**Live proof/evidence question:** Is there a real version-pinned B-inert data pipeline and controlled source-copy/no-copy joint-service transition, and what is each *resulting* A policy's safe whole-network first-exit probability—including new customer/order/operator pathways? No target topology, customer panel, physical approval, numeric BLS–BEA crosswalk or independently validated source-to-customer bridge has yet been obtained. Nov22 is an open synthesis gate; Dec25 23:59 Eastern remains the final target.
