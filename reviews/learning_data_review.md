# Independent review: learning-data economics

Reviewed on 25 October 2026. Scope: [research chapter](../research/learning_data_economics.md) and [four structured evidence records](../data/learning_data_economics.json), against the versioned primary papers below. This reviewer owns only this review; the lead made the source-package corrections. No engine or numerical scenario parameter was changed by this review.

## Disposition

Accept this bounded source investigation after the corrections recorded below. The principal numerical claims match the papers, and the revised interpretation distinguishes cloud charges, human collection rates, retained data, batch sampling and validated physical performance. It does not establish a labor-inclusive cost per useful demonstration, a commercial data-production ROI or a causal deployment learning coefficient.

The review used full primary text and direct arXiv submission histories, retrieved on 25 October 2026. A second read-only reviewer independently checked the DexWild quantities and mixture definitions. No experiment was rerun and no unpublished collection log was available.

| Primary source | Version/date independently checked | Relevant locators |
| --- | --- | --- |
| [Cobalt v2](https://arxiv.org/html/2605.19138v2) | [Submission history](https://arxiv.org/abs/2605.19138v2): v1 18 May 2026; v2 20 May 2026 | IV-A participant design; IV-B RQ3/RQ4; IV-C Tables V/VI and filtering; IV-D physical Franka Lift experiment |
| [DexWild v2](https://arxiv.org/html/2505.07813v2) | [Submission history](https://arxiv.org/abs/2505.07813v2): v1 12 May 2025; v2 17 May 2026 | III-B batch composition; IV-A human/robot datasets; V-A sampling ratios; Section V collection-efficiency comparison and Figure 8; VII-C processing; Appendix Tables III/IV |

Publication/version dates are not the dates when every experiment was conducted. The evidence package correctly leaves the exact collection dates unspecified.

## Verified claims and economic boundaries

**LEC-001 — Cobalt compute charges.** Section IV-B explicitly assumes an estimated T4 instance price of $0.92 per hour and 120 demonstrations per user-hour. The arithmetic reproduces: $0.92 / 120 × 1,000 = $7.67 rounded; dividing by four concurrent users gives $1.92. The paper reports feasible operation with eight users but says it limits active sessions to four for user experience. These are conditional infrastructure costs. They do not include wages, all attempted collection, onboarding, environment development, curation, equipment, training or physical validation. The chapter correctly refuses to translate a roughly fourfold compute saving into a fourfold whole-program saving.

**LEC-002 — Cobalt collection and policy populations.** Table V's six manipulation-task counts sum to 6,746; adding 764 user-study demonstrations gives 7,510. The listed durations sum to 50.61 hours. These are dataset trajectory durations, not a complete paid-human-time account. Section IV-C selects demonstrations “within the 50th percentile for total path length”; that rule does not by itself reconcile attempted, recorded and retained dataset counts. Table VI reports 50 simulation evaluation rollouts per task and policy. Its kitchen scores are 0.04, 0.02, 0.10 and 0.12. None is a field-service reliability estimate.

Section IV-D separately reports 98 expert demonstrations for physical Franka Lift, followed by BC-RNN performance of 52% over 25 rollouts. This is positive physical target evidence, but a small and separate experiment. It cannot be added to the crowdsourced simulation policy denominator or represented as a retained operating fleet. The revised chapter preserves it rather than reducing all physical evidence to interface illustrations.

**LEC-003 — DexWild collection rates and data types.** The reported comparison is 201 demonstrations/hour for DexWild versus 43 for Gello-based robot teleoperation across five representative tasks. It does not establish an equal-useful-data or labor-inclusive dollar-cost ratio. Section IV-A identifies 9,290 **human** demonstrations across five tasks and 93 environments, separate from 1,395 robot demonstrations. The human task counts and environment counts independently reconcile to those totals. This distinction preserves the actual robot-grounding requirement.

Appendix VII-C states that episodes are discarded if wrist pose “cannot be reliably tracked for more than 75% of the duration.” The chapter follows that wording without converting it to a measured rejection percentage. Tracking reconstruction, filtering, clipping, smoothing and retargeting are genuine downstream steps; training steps and batch sizes do not disclose their full compute or labor bill. The ten users mentioned for hardware deployment do not establish the sample size or complete timing protocol for the separate collection-speed comparison.

**LEC-004 — data amount and batch composition are different experiments.** Appendix Table III's reported aggregate scores rise across the listed dataset fractions: 0.287, 0.351, 0.523 and 0.678. Individual rows do not rise monotonically: spray changes from 0.605 at half the human data to 0.565 at all of it; toy cleanup is 0.514, 0.442, 0.440 and 0.792. The chapter appropriately states these as point estimates, without claiming that the decreases are statistically significant or fitting a universal scaling exponent.

Table IV labels its ratio **Robot:Human**. Sections III-B and V-A define it as sampling within a training batch. Raising the human sampling share from robot:human 1:2 to 1:5 changes the reported mean from 0.798 to 0.545 in-domain and from 0.751 to 0.509 in-the-wild. This is not a comparison of purchased demonstration quantities, collected dataset sizes or labor hours. Robot-only/human-only/co-trained comparisons and the paper's recovery/tactile limitations support the target-grounding caution, without establishing a universally optimal mix.

## Findings corrected during review

| Finding | Severity and correction |
| --- | --- |
| Cobalt physical learning result omitted | Moderate. Earlier wording could imply that all policy evaluation was simulated. The lead added the separate 98-demonstration, 52%/25-rollout physical experiment to prose and structured quantities. |
| DexWild mixture denominator underspecified | Moderate for economic interpretation. The lead specified training-batch sampling and separated the 9,290 human demonstrations from 1,395 robot demonstrations. Dataset-size and collection-cost interpretations are now excluded explicitly. |
| Cobalt known filtering/concurrency conditions understated | Minor. The lead added the 50th-percentile path-length rule and the four-active-user choice, while retaining unknown before/after filtering counts. |
| Readability and aggregate wording | Minor. Joined words in JSON were spaced; the improving dataset-size averages were distinguished from the falling means in the mixture experiment. |

No incorrect numerical coefficient was found. The corrections improve source coverage and denominator precision rather than change the chapter's central economic conclusion.

## What remains unresolved

The null full-cost estimate is appropriate. Neither inspected source supplies a complete matched account of attempted versus retained collection, paid person-hours, equipment amortization, processing, training, target validation and commercial reuse rights. Public accessibility of a paper does not establish access to or permission to reuse every underlying dataset artifact.

The proposed next experiment is justified: compare collection mixtures at a fixed target objective and common evaluation budget, charge all incremental human and compute resources, preserve failures and recovery coverage, and measure qualified target-policy gain. The evidence does not yet show whether cheaper collection reduces the complete R&D critical path, or whether physical validation and task development remain limiting. This remains an explicit research gap, not a missing number to fill with a benchmark multiplier.
