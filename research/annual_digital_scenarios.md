# Annual digital progress changes the adoption comparison

Status: implemented synthetic mechanism, model 0.2.0. The annual-path design is now executable through the common model, local API, dashboard and exports. This is a new local implementation of the accepted design; the unpublished cloud edits described in the supplied handoff were unavailable and are not claimed as recovered or verified.

The decision question is whether a robot investment stays attractive as its human-led alternative also improves. A lower combined production cost is insufficient: the customer compares that cost and the commercial payments with the best available alternative, while delivery still depends on support, components, capital and installation. The model now makes that comparison at every year rather than holding the digital baseline fixed across the horizon.

## Three changes with different meanings

The resolver accepts independently specified annual levels for human time reduction, signed robot coordination and the robot's additional digital-service expense. These replace their scalar settings in that year's economic ranking, site eligibility, manufacturing-demand signal and operating output. Omitted channels repeat the scalar. Capability and funded learning remain separate mechanisms. Full-horizon validation rejects missing periods, nonfinite values, booleans and unknown fields before fleet calculations; there is no smoothing or extrapolation.

Human efficiency reduces the hours required by the human comparator and the human work retained after robot service. Coordination changes accepted robot capacity before the site-demand cap; it can worsen. Robot digital-service expense changes resource costs and the model's assumed cost-plus payments. It is an annual service bundle, not a per-token inference price. Neither a cheaper service nor favorable coordination directly improves the capability index, hardware qualification or learning transfer.

These distinctions follow the [accepted design](digital_trajectory_design.md) and its [independent design review](../reviews/digital_trajectory_design_review.md). The digital dossier's H-QJE-2025 and H-METR-2026 evidence motivates heterogeneous human baselines; H-COORDINATION-2026 and the [benchmark/coordination analysis](coordination_reproducibility.md) motivate signed coordination and a strong conventional comparison. The [learning-data analysis](learning_data_economics.md) separates collection from validated improvement. These sources constrain the interpretation. **None supplies the levels or slopes of the synthetic paths.**

## What the six counterfactuals establish

The generated [annual comparison](../model/results/annual_digital_comparison.json) contains six five-year paths with learning disabled: a constant reference, improving human efficiency, cheaper robot service, worsening coordination, a joint path, and the same improving human process with conventional robot control and no additional coordination/service bundle. Every result retains its complete inputs, annual comparisons, fleet ledger, source hashes and limitations.

In the tote-handoff illustration, an improving human baseline lowers both the human-only and combined resource costs. It can nevertheless close new robot admission because the human alternative improves more. The existing robot stock remains on the ledger. Its output can fall under the inherited current-eligibility cap; that is a limitation of the continuation rule, not evidence that an operator would optimally idle or retire the robot. The report's generated table shows the exact costs and gate outcomes without independently recalculating them.

A cheaper robot-service bundle can restore positive customer savings under the assumed contract. The resource saving and the allocation of that saving are different quantities: the cost-plus rule passes a price reduction to the customer and reduces the provider's dollar markup. The exact toy witness reduces resource expense by $1,500, raises customer cash gain by $1,725 and reduces provider recurring margin by $225. The net resource gain remains $1,500. This does not establish actual pricing, margin or bargaining behavior.

The conventional combined case is the relevant counterfactual for additional orchestration. It retains the same digitally improved human process, configured robot, maintenance, required control and site software. It removes only the added coordination effect and robot digital-service bundle. C10 alone is insufficient because it also removes the human digital improvement. The extra bundle may help or harm; the six scenarios do not identify a real scheduler's performance.

## What changes for the research program

1. **Deployment sequencing:** screen adoption against the contemporaneous human-led alternative. A favorable robot-cost trend alone cannot justify faster penetration. Inspect the customer contract and payback gate as well as consolidated resource cost.
2. **Value capture:** separate changes in resource use from payments among customer, model supplier, OEM and operator. Workstream K's model-architecture comparison must price adaptation, inference, supervision and rights explicitly before attributing margin to a superior policy.
3. **Capability and learning:** keep service prices, policy capability and deployment-mediated exposure separate. A model company reporting lower inference expense supplies no automatic robot-capability coefficient. A larger simulated installed base supplies no empirical learning effect.

The annual path now addresses the evolving-comparator mechanism in W1-006. W1-TRAJECTORY remains partial: hardware retrofit diffusion, contract vintages, failure/recovery queues and engineering critical paths still need their own mechanisms and evidence. A physical-requirements/employment crosswalk and K dossiers remain subsequent research work; this implementation does not claim those missing artifacts exist.

## Boundaries retained and verification

Annual admission and lifetime margins extrapolate current conditions over the assumed life; they are not forward-looking valuations of the entire path. All compatible installed cohorts receive current software and price conditions without upgrade expense or rollout delay. Supported available robot-hours remain the learning-exposure variable, even when economic eligibility suppresses accepted service. Annual capital budgets are nonrevolving allowances. The separate monthly entrant, treasury, monthly physical fixture and initial-year commercial tables are not one jointly feasible company model.

The [implementation review](../reviews/annual_trajectory_review.md) records sole-agent verification rather than a new independent review. The frozen model 0.1.1 comparison covers every existing numerical field across eight presets and both onboard configurations. Adverse cases test overlap, harmful coordination, cost-only changes, stock retention after admission reversal, zero capability, invalid late periods and shared resource accounting under nonconstant paths. API/CLI replay and the browser's selected-year table, trace and export/reload use the same result object. No GPU, robot, external service or empirical calibration was executed.

**Next question:** which measured physical requirements and support obligations would change one of these adoption comparisons enough to alter the preferred deployment sequence or model-provider architecture?
