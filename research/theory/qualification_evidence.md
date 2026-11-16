# Transfer performance does not identify a qualification-cost reduction

Theory phase checkpoint 4: first sparse evidence-to-transition slice, not a completed atlas. This freshly inspects two primary sources already present in the historical learning dossier and adds a rubric-based identification bound and explicit source-bundle relationships. Historical records and their retrieval dates remain unchanged. No new field observation or causal estimate is claimed.

## Sources and inspected scope

**DexWild: Dexterous Human Interactions for In-the-Wild Robot Policies**, arXiv **2505.07813v2**, revised May 17, 2026 (initial submission May 12, 2025; dates verified on the versioned abstract page). [Versioned full text](https://arxiv.org/html/2505.07813v2), retrieved November 16 UTC, 2026, HTML SHA-256 `fe3adffd7b204bb25771bfb6cfa3719641442ed5fe1ee428ef8eed701cc2b302`. Inspected §§IV, V-B/C, VI and Appendix VII-A/C/D, particularly the pouring transfer, scoring rubric and downstream processing. HTML includes display text and markup; the hash identifies the retrieved bytes, not an immutable PDF.

**Joel Jang et al., DreamGen: Unlocking Generalization in Robot Learning through Video World Models**, Proceedings of the 9th Conference on Robot Learning, **PMLR 305:5170–5194, 2025**. [Proceedings entry](https://proceedings.mlr.press/v305/jang25a.html); [published PDF](https://raw.githubusercontent.com/mlresearch/v305/main/assets/jang25a/jang25a.pdf), retrieved November 16 UTC, 2026, SHA-256 `d2103c9f0384e16750a8a5692e410cc14da953eb9dd53a395a680471d30968c3`. Inspected the physical generalization experiment/Table 1, §5 limitations, and Appendix K.1/Table 8. Publication year is not retrieval year.

The [structured records](evidence_transitions.json) preserve author-reported status, joint inputs, target configuration, locators, quantities and explicit unknowns. Existing parent records are LEC-003/004/005 in the historical learning-data package; these new relationships do not create additional independent studies.

## The transfer edge is a joint training recipe

DexWild §V-B reports pouring performance after combining **human pouring demonstrations with robot spraying demonstrations**, with no robot pouring demonstrations in this cross-task treatment. The reported metric is 94%, versus 0% for robot-only and 11% for human-only policies. The underlying robot data configuration is xArm with LEAP Hand V2 Advanced (§IV-A); the target evaluation uses in-the-wild extreme scenes and a 1:2 robot:human training ratio.

This supports an author-reported relation from a **bundle** of human target-task data and robot source-task grounding to target-policy performance. It does not show that spraying deployments alone create a qualified pouring service, or that arbitrary source and target embodiments share that relation. Relative training budgets, commissioning effort, contractual reuse rights and the bill payer are not identified by these three performance figures.

The paper's Appendix VII-A assigns pouring scores 0, .15, .25, .75 and 1. A .75 outcome can mean pouring without the full functional-grasp criterion or using a functional grasp without pouring; a full score requires the combined milestones. Thus the prose label “success rate” cannot simply be imported as a binary probability of complete accepted service. The mapping from the reported aggregate to a mean rubric score should be verified against raw trial records before using even the bound below. Trial count/aggregation for the 94% figure is not established in the inspected passages.

## A partial-identification result from a graded score

Suppose an evaluation score X lies in [0,1], full rubric completion has X=1, and every non-full outcome has X<=r<1. If the reported statistic is the mean score s, then the fraction p of full-score outcomes satisfies

`max(0,(s-r)/(1-r)) <= p <= s`.

Proof: nonnegativity gives `E[X]>=p`; the non-full ceiling gives `E[X]<=p+(1-p)r`. Rearranging yields the two bounds. They are sharp over distributions allowing scores 0, r and 1: the upper endpoint mixes 0 and 1; a positive lower endpoint mixes r and 1. For s<=r, zero full outcomes is feasible when the non-full score distribution can realize s. This is a standard elementary mean bound, not a novel statistical theorem or a sampling confidence interval.

**Conditional DexWild implication.** Treating the reported .94 as an exact mean of the stated pouring rubric with r=.75 gives **.76<=p<=.94**. This concerns full rubric points only. It says nothing about liquid volume tolerance, cycle time, intervention burden, sustained reliability or a customer's acceptance contract. Rounding and finite sample restrictions are not quantified without raw trial/aggregation information. The bound is conditional on the metric interpretation, not a re-estimated empirical success rate.

**DreamGen check.** Table 1 reports Pour Water at 55 for the augmented policy and 40 for the baseline. Table 8 gives .5 for picking up and 1 for pouring. Interpreting the percentages as mean normalized rubric scores yields full-score bounds **[.10,.55]** and **[0,.40]**, respectively. These overlap: a higher mean score does not alone establish a higher fraction of full-score trials. Appendix K.1 says ten evaluation rollouts per checkpoint. If a reported mean .55 comes from exactly one such ten-trial checkpoint, discrete counts further restrict full completion to 1–5 of ten. The inspected passages do not establish how many checkpoints feed each table entry, so this stricter count bound is a conditional illustration, not the primary empirical bound.

No bounds above are confidence intervals or a forecast of industrial performance. A research full score is not automatically qualified customer service.

## Why the model's cost transition remains unidentified

DexWild reports 201 versus 43 demonstrations per hour in its collection comparison (§V-C). Its processing pipeline still reconstructs camera/wrist motion, filters tracking failures, clips/smooths actions and retargets motions (Appendix VII-C). These operations demonstrate additional stages, but do not price their full resource use or establish matched cost per qualified target service. Do not replace the [model's cost-reduction loading](learning_funding_alignment.md) with the collection-rate ratio.

DreamGen reports physical-policy gains after embodiment grounding and synthetic generation. Its 14 novel-behavior Table 1 average is 43.2 versus 11.2, with partial credit. Adjacent prose gives 11.8 for a baseline and reports 2,884/2,885 grounding trajectories in different passages; preserve these existing discrepancies rather than choose the most convenient number. The paper reports generating a separate 240,000-sample **RoboCasa simulation** dataset in 54 hours on 1,500 L40 GPUs (§5). That is a resource statement about that synthetic dataset, not a cost denominator for the GR1 field-policy results. It cannot be assigned to each physical target as a measured qualification bill.

Formally, write total prerequisite cost as `C=collection+processing+training+validation+integration+retained support`, consistently allocating reusable work once. A known saving d in one component leaves the net saving `d-(increase in other components)` unidentified unless the other terms are bounded. Even the sign is unrestricted by a policy score alone. For example, identical observed scores and collection rates can coexist with total costs falling from 100 to 80 or rising from 100 to 140 when unreported processing/validation differs. Those numbers are synthetic countermodels demonstrating non-identification, not estimates.

Accordingly, the records contain **null**, not zero, for payer-specific qualification-cost changes, commercial data reuse rights, customer demand and early-transfer permissions. The evidence supports directed research-performance relationships and required processing/grounding stages. It does not calibrate nonnegative ell in the linear cost-transition model.

## Discriminating measurement design

Hold target configuration, starting policy, accepted-service criteria and evaluation workload fixed. Compare source-experience inclusion at a matched adaptation budget, then measure attempts, useful/rejected data, human and compute work, physical validation, integration, retained support and calendar delay by responsible payer. Track full trial outcomes rather than only average partial credit. Randomization or a defensible matched design must address easier sites, extra target data, simultaneous hardware/model changes and selective reporting of successful candidates.

The estimand is the change in **cost to meet the same target acceptance criterion**, including failures and recurring obligations, not the change in benchmark score at an arbitrary training budget. A source can improve performance while raising that total cost, or lower cost while still failing the acceptance gate. Distinguish both from genuinely new service eligibility. This prepared measurement protocol authorizes no outreach.

Theoretical consequence: retain the payer-cut result as conditional on an independently established cost transition. A separate eligibility model may be more faithful to some reported learning results, but its threshold must be grounded in an explicit service requirement rather than chosen to convert a benchmark into deployment.
