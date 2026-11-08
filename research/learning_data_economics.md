# Learning-data economics: separate cheap collection from useful policy improvement

Continuation finding, 25 October 2026. This follows the first checkpoint's unresolved data-input and robotics-R&D questions. [Structured evidence](../data/learning_data_economics.json) preserves the inspected versions and quantities. No result here changes a numerical deployment-model parameter.

The decision is whether to fund a data pipeline, not whether demonstrations are generally useful. Two current primary papers expose different bottlenecks: Cobalt improves shared simulation infrastructure and operator access; DexWild changes the embodiment and location of human demonstration collection. Both can reduce a particular collection burden without establishing cheaper accepted physical service, faster complete R&D, or a reusable commercial dataset of known cost.

## Cobalt's inexpensive demonstrations are a cloud-cost scenario

[Cobalt v2](https://arxiv.org/html/2605.19138v2), submitted 20 May 2026 after the initial 18 May version, describes cloud teleoperation using smartphones and other devices. Its architecture separates client sessions, media streaming and simulation services, with an in-memory state exchange and vectorized simulations. That is a direct digital contribution to robotics data production, rather than an analogy from an unrelated industry.

Section IV-B's cost example assumes an NVIDIA T4 instance at an estimated $0.92 per hour and 120 demonstrations per user-hour. It reports $7.67 per thousand demonstrations without vectorization and $1.92 with the proposed sharing. The authors limit active sessions to four per GPU for user experience despite reporting feasible teleoperation at eight. Those are **conditional compute charges**, not an audited labor-inclusive cost per usable demonstration. The arithmetic prices the cloud resource. It does not price the operators, onboarding, unsuccessful attempts, task construction, curation, policy training, hardware or physical validation. Calling the fourfold compute reduction a fourfold reduction in the complete data-production cost would change the denominator.

The same paper provides a useful, different empirical object: Table V contains 7,510 recorded demonstrations and 50.61 hours, comprising 6,746 crowdsourced manipulation demonstrations plus 764 user-study demonstrations. Six manipulation tasks range widely in recorded duration. These are trajectory hours, not a disclosed payroll or fully loaded project-labor account. The paper selects demonstrations within the 50th percentile for total path length and evaluates Table VI simulation policies over 50 rollouts per task. Exact before/after curation counts remain unextracted. The low kitchen-task results (0.02–0.12 across the four reported policies) show why a large collection count is not equivalent to a solved target service.

Section IV-D separately reports a physical Franka Lift experiment: 98 expert demonstrations train BC-RNN, with 52% success over 25 rollouts. This is a small real-robot learning result, beyond a hardware illustration. It remains distinct from the crowdsourced simulation pilot and Table VI evaluation, and neither establishes retained field-service reliability. Those populations must not be pooled. Likewise, a simulated-client stress test measures system load, not how many trained humans can simultaneously operate physical robots at an acceptable safety and task-success standard. The source's small device/training studies inform interface design; they do not establish a world-scale labor supply curve or a universal productivity coefficient for novice operators.

The operational inference is specific: vectorization can reduce the compute share of a simulated collection workflow when concurrency, latency and utilization permit. If labor, task development, quality filtering or physical validation dominates total cost, the whole-program saving can be much smaller. The next investment test should measure these shares and useful target-policy gain at fixed validation quality.

## DexWild changes collection embodiment, with a target-grounding obligation

[DexWild v2](https://arxiv.org/html/2505.07813v2) was submitted on 17 May 2026, a year after the original 12 May 2025 submission. Its human-worn collection system combines motion capture and cameras, then co-trains human and robot demonstrations. The inspected paper reports 9,290 human demonstrations across 93 environments, separate from 1,395 robot demonstrations used for target grounding. Its comparative study reports 201 demonstrations per hour for the human-worn system and 43 for the Gello-based robot-teleoperation comparator across five representative tasks.

That is a reported collection-rate comparison. It is not the same as a labor-inclusive dollar-cost ratio, and it does not establish that a human demonstration and robot demonstration have identical learning value. The paper identifies haptic feedback, resets and hardware setup as practical differences, but the inspected description does not expose a complete cost ledger or enough participant/timing detail to independently reconstruct the whole comparison. Faster capture at a location also does not settle travel, setup, processing and rejection costs across locations.

The downstream pipeline is explicit enough to reveal additional work: tracking reconstruction, filtering, outlier handling, smoothing and retargeting. Appendix VII-C discards episodes when wrist pose cannot be reliably tracked for more than 75% of the duration. That criterion should not be mistaken for a reported rejection fraction; the denominator of attempted versus retained collection is still needed. Table V provides training steps and batch size, but those are not a measured GPU-hour or dollar bill.

The target-policy results also resist a generic scaling rule. Appendix Table III's task rows are not monotonically improving: spray performance changes from 0.605 at half of the human dataset to 0.565 at the full dataset; toy-cleanup scores initially decline before rising at the full dataset. The average improves across the listed fractions, but the author's broader “steady” wording should not erase task-level variation. These are reported point estimates; uncertainty and matched repeated evaluations are needed before attributing significance to a particular decrease.

Table IV provides a second warning: increasing the human sampling share, changing the robot:human training-batch ratio from 1:2 to 1:5 reduces the reported mean score in both in-distribution and in-the-wild comparisons. These ratios concern samples within a training batch, not the sizes of collected datasets. Human-only results are much weaker in those inspected tasks. The paper expressly retains robot demonstrations to bridge the embodiment gap and identifies missing recovery examples and lack of tactile information as limitations. A lower-cost upstream data source therefore comes with a composition and target-grounding problem, not an automatic replacement for robot-specific evidence.

## What changes in the research model and investment question

The existing engine correctly leaves useful-data production and causal learning response uncalibrated. These studies strengthen that boundary. Exposure hours, recorded trajectories, retained datasets, target-training mixtures and validated policies should be separate quantities. Rights and actual access remain additional conditions, not consequences of publicly available paper text.

A prospective collection ledger should distinguish:

1. Attempted collection and all paid human time, including onboarding, resets and quality checks.
2. Recorded and retained demonstrations, with explicit rejection reasons and the same population/time window.
3. Compute, equipment, task construction, travel, processing and physical target-validation costs.
4. Dataset composition, source/target embodiment, rights and reuse restrictions.
5. Change in held-out target policy performance at matched accepted output and operating quality, including recovery and support.

The economic objective is the full incremental cost of a validated target capability, not minimum cloud spend per recorded trajectory. A pipeline can improve one stage yet leave the critical path unchanged because hardware access or validation remains limiting. Conversely, cheaper portable capture could be valuable precisely because it expands environmental diversity, even when it does not reduce total operator hours proportionally. Those are separable, testable mechanisms.

For a humanoid company, this favors a small matched collection-and-validation experiment before a generalized data-factory investment: fixed target tasks, alternate collection mixes, complete human/compute accounts, common policy/evaluation budgets and retained failure/recovery coverage. The public sources support the mechanism and identify risks; they do not supply a commercial wage, usable-data yield, program ROI or field learning coefficient.

## Stopping condition and remaining evidence

This bounded public-source investigation stops with two versioned primary cases that materially distinguish compute cost, collection rate and target usefulness. It does not add a speculative total cost to fill missing components. The next step requires the underlying study logs/supplements or a new controlled operating dataset: full collection person-hours, failed/rejected episodes, target-training/validation compute, equipment amortization and rights. If those remain unavailable, retain the null full-cost estimate and test sensitivities explicitly rather than call the data pipeline commercially validated.

## R&D-to-qualification continuation, edition 0.21

[The qualification analysis](learning_qualification.md) extends this package with DreamGen, XEWorld and two NVIDIA integration/readiness sources. Physical policy partial credit, simulated video metrics, technical self-assessment and supported commercial capacity remain different observations. Inherited grounding, manual preparation, generation compute and retained-cohort regression now inform an explicit measurement contract. Four proposed no-learning/no-transfer/support/supply challenges remain unimplemented as new families; no source score changes the annual learning coefficient.
