# Independent capability, learning and coordination evidence review

Reviewer: customer/value-capture lane, reviewing the separate B/D/E lane.
Review date: 25 October 2026. Input repository revision: `campaign launch snapshot (see ignored sync_receipt.json)`.
Reviewed artifacts: [capability_learning.md](../research/capability_learning.md) and [capability_evidence.json](../data/capability_evidence.json), first-wave version 0.1. This review did not edit those artifacts or independently certify the reviewer's own F/G research.

Initial inspected SHA-256 hashes: research `c18dc0e413bcd191d91d8d68307f899e053b955984ff31607e7f50825c2892a9`; evidence `9945aeb7ddbb3e219492e2385114ba7ce50dd7c5af16f1d088d2ef093e55b22a`. Owner corrections are tracked in the recheck below rather than overwriting this audit trail.

**Disposition after recheck: suitable for a first publication checkpoint within the stated audit scope.** No inspected source overturns the main findings: industrial humanoid evidence is bounded to particular configured workflows; goals are not achieved reliability; transfer is conditional and can have unfavorable comparisons; and learning consumes human and computational work. The two material source-boundary corrections and the machine-readable status correction were integrated and rechecked. This is not an exhaustive audit of every provider or a field replication.

## Corrections by severity

### Medium — RECAP's evaluated population is narrower than its training population

Locations: `research/capability_learning.md`, section “Experience and corrections can improve throughput”; `CAP-E022`, `LEARN-RECAP-005` and `CAP-BM003` in the JSON.

The text describes greater-than-twofold throughput improvement for “diverse laundry” without the decisive evaluation restriction. [RECAP v2, §VI-A, “Laundry (diverse items)”](https://arxiv.org/html/2511.14759v2#S6.SS1) says the policy is trained on 11 item types, but the quantitative experiment measures **button-up shirts** to reduce metric variance. Videos show other clothing; that is a different evidence population.

Required correction: identify button-up shirts as the quantitative diverse-laundry evaluation population in prose, claim/benchmark population and limitations. Retain the broader training mixture as a separate field. The greater-than-twofold result can remain attributed to Figure 7, but cannot become a measured performance estimate across the full laundry mix or a general housekeeping-service coefficient.

Economic consequence: a laundry operator's job mix, failure distribution, throughput and quality cannot be calibrated from this single evaluated item type. This matters even if the model trained on a diverse mix.

### Medium — newer scaling version exists; exact version dates are now resolvable

Locations: `CAP-E018`, `CAP-E022`, `CAP-BM001/003` version metadata and the scaling section's source note.

The inspected v3 source is explicitly pinned, which is good. However, the claim that its exact date is unresolved can now be replaced with direct evidence, and a newer version available before campaign kickoff should be acknowledged. The arXiv **Submission history** pages were read directly because Exa's abstract rendering retained only initial publication dates:

| Source | Verified version history |
| --- | --- |
| [Scaling paper](https://arxiv.org/abs/2410.18647v3) | v1: 24 October 2024; inspected v3: **13 October 2025, 01:44:42 UTC**; newer v4: **26 June 2026, 02:30:53 UTC**. |
| [RECAP](https://arxiv.org/abs/2511.14759v2) | v1: 18 November 2025; inspected v2: **19 November 2025, 04:34:49 UTC**. |
| [RT-X](https://arxiv.org/abs/2310.08864v9) | v1: 13 October 2023; inspected v9: **14 May 2025, 15:22:36 UTC**, confirming the existing v9 date. |

Required correction: preserve initial submission and inspected-version date separately; remove “exact v3/v2 date unresolved.” Record v4 availability and the bounded comparison rather than silently replacing the historical snapshot.

I independently retrieved [scaling v4](https://arxiv.org/html/2410.18647v4). In the checked sections, §4.2 still fits the normalized-score optimality gap with six data points, leaves the 1,191-pair extrapolation unverified, and distinguishes diversity from repeat demonstrations. Table 1 retains success rates 85.0%, 92.5%, 87.5% and 90.0%; Table 2 retains the nonmonotonic action-U-Net comparison. These checked results do not reverse the dossier's argument. I did not perform a complete semantic comparison of every v3/v4 paragraph or re-run experiments.

### Medium — prospective provider claims need an explicit evidence-status label

Locations: evidence records `CAP-E003` and `CAP-E008`.

Both currently use `epistemic_status: operator_reported_observation`, although their decision-relevant contents include announced future work: Figure 03 sequencing in the June 2026 project and Atlas deployment dates in the January 2026 roadmap. The system records and prose correctly preserve their announced/planned stage, so no inflated installed-stock calculation was found in these artifacts.

Required correction: label the claim-level status as an operator-announced plan/configuration, or split observations from plans. Do not let a future dashboard filter on “observation” reclassify an announced deployment as achieved output. This is a data-contract correction, not a reversal of the narrative.

### Low — clarify RECAP's plotted regression and internal data wording

Locations: `CAP-E022`, `LEARN-RECAP-005`, `CAP-BM003`, and the same RECAP prose section.

I viewed [Figure 9's box-assembly throughput image](https://arxiv.org/html/2511.14759v2/figures/experiment3/Box_Assembly_throughput_plot.png) directly after the PDF reader rejected the 25 MB paper. The plotted mean decreases from iteration 0 to iteration 1, then rises at iteration 2. The error bars overlap in the first comparison. Prefer “the throughput point estimate initially decreases” to avoid implying a statistically established negative learning effect. The economic reason to retain nonmonotonic scenarios still stands.

There is also a source wording inconsistency: §VI-C calls the 600 box trials per iteration autonomous trials, while Appendix A-F's “Dataset composition” calls them demonstrations; both give 360 correction/intervention episodes. Preserve the main-section attribution and note the inconsistent terminology if using the count to cost collection. Do not infer a fully unassisted workload from the 600 figure. The paper explicitly retains people for reward labels, corrections, resets, evaluations and robot maintenance.

## Independently checked claims that pass

| Claim and source | Review result and permissible interpretation |
| --- | --- |
| [Figure BMW post, 19 November 2025](https://www.figure.ai/news/production-at-bmw), “Deployment Overview” and reliability section | **Pass.** 84-second total/37-second loading are requirements; greater-than-99% placement is a target; zero human pauses/resets per shift is a goal. The dossier correctly leaves realized intervention intensity unknown. The 90,000-plus parts, 1,250-plus runtime hours, retirement and forearm redesign are reported, with no quantified failure rate. |
| [BMW, 27 February 2026](https://www.press.bmwgroup.com/global/article/detail/T0455864EN/bmw-group-to-deploy-humanoid-robots-in-production-in-germany-for-the-first-time?language=en), “Successful pilot” | **Pass.** BMW supports the cumulative industrial pilot observations and selected highly automated body-shop context. Ten-month production support, Figure's 11-month deployment and six-month daily-runtime statement describe different boundaries; they should not be averaged. Operator corroboration is not independent field auditing. |
| [RT-X v9](https://arxiv.org/html/2310.08864v9), §IV-C, §V, Tables I–II | **Pass.** The repository covers 22 embodiments; experiments train on nine and evaluate across six robots with 3,600 total trials. Table I's Google comparison is RT-1 92%, RT-1-X 73%, RT-2-X 91%. Table II's emergent result is 27.3% versus 75.8%; its separate generalization result is 62% versus 61%. The narrative correctly resists the paper's broader outperforming language and does not pool populations. |
| [Scaling v3](https://arxiv.org/html/2410.18647v3), §4.2, §5, Table 2 | **Pass, with version update above.** The score-gap outcome, six-point fits, two detailed tasks plus two recipe-validation tasks, saturation and nonmonotonic action-network scaling are correctly bounded. No universal exponent or commercial output coefficient is justified. |
| [RECAP v2](https://arxiv.org/html/2511.14759v2), §§VI–VII | **Pass, with population correction above.** Task-specific deadlines, correction-assisted box learning, autonomous-evaluation laundry iterations and batched offline updates are retained. Section VII expressly says the system is not fully autonomous and uses human reward feedback, interventions and resets. Episode throughput does not establish full labor-inclusive field economics. |
| [Mercedes Apollo/MO360 account](https://group.mercedes-benz.com/company/production/production-network/mbdfc-humanoid-robots.html) | **Pass.** The source describes teleoperation/AR knowledge transfer and production-environment data collection, with autonomous operation as the next development step. The dossier does not convert this into autonomous shift replacement. |
| [Atlas RMAC opening, 21 September 2026](https://bostondynamics.com/news/boston-dynamics-opens-robotics-metaplant-application-center-to-train-humanoid-robots-for-manufacturing-tasks/) and [Hyundai January roadmap](https://www.hyundaimotorgroup.com/en/news/hyundai-motor-group-announces-ai-robotics-strategy--to-lead-human-centered-robotics-era-at-ces-2026) | **Pass.** The operating center is a test/training site. Factory sequencing from 2028, component assembly from 2030 and larger manufacturing/deployment quantities are plans. The September source still calls Atlas in development. |
| [BMW Figure 03 project, 25 June 2026](https://www.press.bmwgroup.com/global/article/detail/T0458778EN/bmw-group-advances-the-use-of-physical-ai-in-production-with-figure-03-project-in-spartanburg?language=en) | **Narrative pass; status-label correction above.** It describes a new sequencing workflow linked to tugger/STR transport and human assembly. No inspected claim supports inheriting Figure 02's exposure or reliability. |
| [Tesla Q3 2026 Exhibit 99.1](https://www.sec.gov/Archives/edgar/data/1318605/000162828026066738/exhibit9914.htm), manufacturing table and product outlook | **Pass.** California Optimus is “Early Ramp,” Texas “Construction”; numeric Optimus capacity is blank. The source reports Fremont production beginning, not autonomous labor output or retained external deployments. |

## Scope and remaining limits

The review freshly fetched the consequential source texts above, directly checked arXiv version histories, and inspected the RECAP plot. It checked that configured-system records retain pilots, plans, manufacturing stages and research evaluations separately. It did not audit every Unitree, UBTECH, Sanctuary, 1X, DHL, DataMIL or pi0.5 claim, run hardware, reproduce training, verify customer financial returns or validate the common numerical engine. Those items remain separately scoped evidence or implementation work.

No observed learning result should populate an industry adoption or labor-substitution parameter without a target-side link. The dossier's current prohibition on universal robot-hour learning coefficients, its null commercial intervention rates and its explicit human/specialized alternatives are justified by the inspected sources.

The requested model was GPT-6 Astra with Ultra reasoning. The reviewer cannot independently expose or verify the serving configuration. Review conclusions are source-based, not a claim of model identity.

## Final reconciliation, 25 October 2026

The file owner applied the authorized corrections. I re-read the affected prose, evidence and benchmark fields: the button-up-shirt evaluation boundary is explicit; version dates and the bounded v4 check are recorded; CAP-E003/CAP-E008 now use `operator_announced_plan_or_configuration`; and both the overlapping-error-bar qualification and the inconsistent 600-episode terminology are preserved. All requested medium and low corrections are resolved for this checkpoint. This does not expand the audit to uninspected sources or establish experimental reproducibility.

Rechecked SHA-256: research `a5f092a99c71eb1640ccb36bfaf311cce7fa317f9020e432b0d207b7c669f07f`; evidence `a4d6832fe5646b7fe443ee8de126b86d716c69ce5bf3301cfbb20de8e3b3a33f`. The disposition applies to these versions. The lead and owner were notified; no reviewed artifact was edited by this reviewer.
