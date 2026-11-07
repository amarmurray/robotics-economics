# Executable mechanism model, version 0.3.0

This is an executable, uncalibrated mechanism model, not a forecast of robot adoption or a unit-economics estimate for any named product. Every numerical model input in `assumptions.json` is synthetic. The model's purpose is to expose accounting constraints and consequential assumptions while empirical evidence is assembled. Its 72 constructed sites never enter observed employment totals. `model/evidence.py` separately derives observed atlas statistics from saved official-statistics rows, including all 15 family crosswalks and residuals.

The authoritative scenario function is `model.engine.run_scenario(overrides, preset, digital_paths=None, architecture_overrides=None)`. The local HTTP API, dashboard and exported JSON/CSV all call that function. There is no independent spreadsheet or browser economic calculator. The browser performs display formatting, selection and compatible-row aggregation. The engine also supplies embodiment comparison costs. Scenario IDs include the engine, trajectory-resolver and architecture-helper source hashes, both numerical catalogs, scalar inputs, resolved annual paths and complete architecture parameters. Evidence-package hashes are recorded separately because the quantitative model is not calibrated from those sources.

## Units, populations and dates

The six cells reuse the atlas IDs, whose `2025` suffix identifies the observed baseline definition. Scenario periods begin in 2026 and are conditional, not dated forecasts. Each cell contains twelve synthetic sites and a target of one installed robot per site. Sites have deterministic heterogeneous technical thresholds, authority and readiness conditions. Quantities are continuous expected units. Fractional robots, sites, assembly starts and service parts are a relaxation for inspecting resource mechanisms, not a physically executable production plan.

Accepted units are specific to a cell: component handoffs, tote handoffs, cleaning zones, supply deliveries, material-positioning services or inspection records. They are never added across cells. Multiplying each cell's accepted units by its fixed baseline human-hours-per-unit converts to **baseline-equivalent human hours**; that is the only additive activity denominator used across the scenario cells. It is not measured physical-work hours, employment, payroll, value added or provider revenue.

All costs are constant 2026 USD. Inflation, tax, financing interest, discounting, terminal value and debt default are not modeled. Annual resource costs use capital consumption over the assumed service life. Cash-allocation views count capital at deployment and do not subtract depreciation again. The fixed monthly newco case is a separate normalized example, not a component of the annual fleet totals.

## Capability and matched output

The capability parameter is an uncalibrated threshold index. It is not a benchmark score or success-rate estimate. A site's technical predicate combines its threshold with a minimum scenario uptime. Exogenous annual progress changes this index; optional learning changes it separately. Required embedded robot control/software is held fixed across the robot row of the digital comparison.

One supported full-year robot's productive hours are:

```text
2000 scheduled hours × uptime / (1 + intervention_minutes / 60)
```

Accepted output equals productive hours × cell-specific units per robot-hour × capability index × (1 + coordination change). The coordination parameter may be negative. This is a specified response mechanism, not an empirical response surface. Support demand is 2000 × intervention_minutes / 60 plus maintenance hours. Software/coordination operating cost is separately charged. High-memory configuration consumes two compatible embedded boards and adds power/cost; it provides no automatic capability gain.

Model 0.1.1 corrects the matched high-memory comparison: its synthetic $800 annual configuration charge belongs in both robot branches, alongside the additional 0.1 kW power burden. Only the additional digital-service cost belongs exclusively in C11. At 2,000 operating hours and $0.16/kWh, each robot branch therefore incurs $832 more than its standard-board counterpart. The earlier 0.1.0 implementation omitted the $800 charge from C10, overstating the cost interaction by $800. All eight standard-configuration preset numerical results are unchanged; source/version hashes change. The prior committed version remains available for historical reproduction. See [independent correction review](../reviews/high_memory_cost_review.md).

Matched annual economics use a fixed site's accepted-output requirement. Robot work is capped at that requirement and residual work stays with humans. The digital-efficiency control reduces human time in both the human comparator and the robot site's retained work. At fleet level, commissioned units contribute half-year exposure. Output cannot exceed the workload of installed, supported and ramped sites; faster robots cannot silently service uninstalled sites. Optional extra demand is limited to the installed sites and reported separately.

The 2 × 2 table uses annual **resource/opportunity cost**, not observed cash savings:

| Cell | Definition |
|---|---|
| C00 | Human operation with baseline conventional systems |
| C01 | Human operation with additional digital improvement and site software cost |
| C10 | Robot-assisted operation with required embedded software, without the additional digital intervention |
| C11 | Combined system with changed human time, coordination and digital operating expense |

`C01 − C11` is robotics value against the digital-improved baseline. `C11 − C10 − C01 + C00` is the cost interaction; negative means complementary cost savings. The contrast is not a causal estimate. Digital assumptions can improve the incumbent enough to reduce robot adoption. The table follows the selected calendar year, using its resolved digital conditions and exogenous capability without the optional learned increment. The `joint` export remains a final-year alias; `joint_by_year` contains every annual reference. Annual fleet economics use the actual period's modeled capability, including its separately funded learned increment.

Observed payroll removed remains null. A separate, visible `labor_avoidability` assumption determines the fraction of released labor value treated as avoided customer cash. Default 0.75 is illustrative. At zero avoidability, labor-time release alone does not satisfy the customer cash/payback gate. No demand-revenue credit or information-value premium silently fills the difference.

## Annual digital levels and reference boundaries

`digital_paths` uses schema `digital-annual-paths/0.1`, the catalog base year and `epistemic_status: synthetic_assumption`. Optional channel arrays are `digital_efficiency` (0–0.6), `coordination` (−0.4–0.6) and `digital_cost_usd` (0–20,000 constant-2026 USD per supported robot-year). Every supplied array must have exactly `years` finite numeric levels. Booleans, nulls, extra fields, wrong years/versions and invalid late periods are rejected before calculation. No interpolation, extrapolation, compounding or last-value carry is allowed. An omitted channel repeats its scalar; a supplied channel replaces that scalar in every period.

The same resolved parameters drive each year's economic ranking, eligibility, planned manufacturing demand, operation and released human hours. Baseline-equivalent hours retain the fixed original activity denominator. Digital paths do not directly change capability, hardware, learning or component capacity. They can change admission and hence subsequent supported exposure. `reference_scopes` records inherited limitations: all compatible installed vintages receive current software/price conditions for free; supported available hours can accrue despite an economic output cap; admission and lifetime-margin tests extrapolate current conditions rather than valuing the future path.

One-site lifetime commercial references freeze initial capability and resolved year-zero digital conditions. The normalized monthly entrant, fixed-target backcast and isolated treasury/monthly experiments have no new path linkage. Annual funding envelopes still refresh exogenously. Consequently no joint company cash feasibility or optimal continuation policy is established.

The [annual analysis](../research/annual_digital_scenarios.md) connects six engine-generated counterfactuals to decisions. The [implementation audit](../reviews/annual_trajectory_review.md) records exact 0.1.1 scalar compatibility and sole-lead verification. The earlier [design](../research/digital_trajectory_design.md) and independent design review are preserved as historical contracts, not silently relabeled implementation reviews.

## Conditional deployment and shared resources

Every site's technical, economic and readiness predicates are evaluated on the same cohort. Economic eligibility requires positive assumed customer savings, a finite payback within the chosen customer's criterion, and nonnegative undiscounted expected provider/financier lifetime margins. These criteria are assumptions, not established financing terms. Customer profiles change explicit approval delay, scope of process authority, site cash ceiling, implementation slots and investment criterion. Their labels have no productivity multiplier.

The waterfall remains in baseline-equivalent hours: relevant work → capability compatible → economically attractive → operationally ready → installed capacity → realized baseline output. It does not multiply arbitrary independent gate percentages. Installed stock can remain after conditions worsen; readiness limits productive utilization rather than erasing existing robots.

Deployment allocations use a stable, descending-customer-savings heuristic across the six cells. It is not a globally optimal policy. Shared installation hours, support capacity and customer/provider cash are allocated once. Existing-fleet support consumes capacity before incremental shipments. Resource views show the full portfolio pool even when a selected-cell view is displayed, with that reference scope labeled explicitly.

Annual customer and provider capital envelopes refresh exogenously. Manufacturing cash is reserved at assembly starts, including starts that later fail final test; it is not charged again at shipment. Shipment uses the customer's acquisition/integration cash and integration/support reservations. The engine does **not** assume provider sale receipts or operating cash fund additional manufacturing. Consequently this edition tests envelope feasibility, not a fully revolving provider treasury model. Sale, lease and service arrangements reallocate cash and asset ownership; none removes physical manufacturing expenditure.

## Component, factory and cohort accounting

Qualified component receipts are assumed already accepted and **net of external commitments**. Outside allocations are therefore zero rather than subtracted again. Three compatible pools exist: humanoid actuators, quadruped actuators and a hypothetical common embedded-LPDDR board pool. The actuators are not interchangeable. Datacenter HBM, remote inference and training resources are outside these pools; shared supplier names do not establish fungibility.

For every component and period:

```text
closing inventory = opening inventory + qualified net receipts
                    − installed-fleet service parts − assembly consumption
                    − rework − other allocations
```

The demonstration sets rework and salvage to zero explicitly. Service parts are reserved before new starts. A parts shortage reduces supported fleet fraction; it never becomes negative inventory. Final assembly consumes a full BOM at the start, takes one annual period, and applies final-test yield once. Rejected units have no salvage. Manufacturing cost in the catalog is **per start**; expected manufacturing cost per accepted system is `cost_per_start / assembly_yield`. Both matched economics and provider cash use that accepted-unit cost, consistent with the start-based supply ledger.

Finished inventory conserves opening stock + accepted completions − shipments. Commissioning takes a further annual period after shipment. Work in progress and the commissioning pipeline are separate. New commissioning, retained active stock, retirement, replacement and expansion are recorded independently. Unfilled replacement obligations persist as a backlog; a replacement is not net growth. The model does not anticipate replacement starts before retirement, so its forward trajectory can reveal replacement-related capacity gaps. This is a conservative scheduling mechanism, not a claim that actual OEMs cannot plan replacements.

The backcast names a retained-active-stock target and deadline. A constructed linear net-addition path, with replacements, yields required starts, compatible components, spares, staffing, manufacturing cash, indicative 25-start/year lines and latest start/qualification dates. Its fixed 5:1 H:Q mix is illustrative. It is a necessary-condition witness, not proof of demand or adoption; a target can exceed the demonstration's 72-site demand pool. Funding, facility commitments and actual accessible component deliveries still need evidence. If lead times prevent any commissioning by the deadline, the backcast returns infeasible rather than silently reducing lags.

## Learning, evidence and rights

Experience is recorded as cumulative supported robot-hours. It is not automatically useful or legally reusable training data. With nonzero optional transfer and sufficient provider validation cash, pooled prior exposure within a virtual system changes next-period capability up to a scenario limit. The H pool includes the five H cells; that cross-context same-configuration transfer is an explicit unvalidated hypothesis. H↔Q transfer is absent. Validation costs are charged each applicable year. The model does not credit an additional data premium or represent information-value optimization.

Research packages preserve source and target evidence separately. Benchmark scores, vendor claims, released weights, missions and deployment announcements never automatically calibrate any engine coefficient. Openness is displayed artifact by artifact and never becomes a generic cost/adoption multiplier. These evidence objects are read-only; scenario overrides change only the synthetic parameter object.

## Customer/provider allocation and entrant finance

Commercial cash views use a selected cell at **initial capability** across its assumed asset life. The sale customer owns the asset; under a lease a third-party financier owns it; under service the provider owns it. Workflow authority remains with the customer. Model/data rights remain a separate contract question. Provider, customer and financier cash sums reconcile to consolidated resource cash after eliminating internal transfers. This accounting is incremental to the assumed cash-avoidable baseline. It omits discounting, taxes, default, service penalties and actual commercial quotations.

ENTRY-FG-01 follows the F/G lane's normalized floor-service case. Ten robots can provide 100 accepted service bundles each per month at full ramp **after reference downtime**. Changing uptime scales this around the explicit 0.85 reference, rather than applying downtime twice. Three months of commissioning precede a 0.25/0.50/0.75/1 ramp. Formation and site setup, customer acquisition, fixed enterprise overhead, robot terms, variable service costs and one-month receivables all consume cash. Incumbents have the identical technology and robot terms; their adoption timing, contested price and demand response are explicit.

Delivered entrant output cannot exceed either useful capacity or won demand. Incumbent share transfer, capture of existing unmet demand and additional demand are nonoverlapping. Acquisition/hybrid route premiums change cash but do not create an extra market. The default demand decomposition includes a labeled 10% new-service hypothesis; the extra demand control adds to it separately. Funding is an assumed equity commitment. Negative cash creates a reported funding gap, not automatic finance; later rows are conditional additional-funding paths. Receivables at month 36 are not called collected cash. Cash balance is not an investor return or valuation.

The eight saved presets include a RaaS entrant with response at month 18 and the same entrant with immediate response. The overall reference preset instead uses equipment sale. Those are different commercial scenarios, not inconsistent accounts of one observed company.

## Current gaps and next validation

The thirteen views contain functioning calculations and sourced record drilldowns, but the model remains an early research edition. It does not calibrate any cell's intervention rate, quality-adjusted throughput, work-time share, commercial price, service life or qualified component receipts. It lacks discrete site/robot scheduling, measured queue/congestion distributions, calibrated retrofit compatibility, priced resource substitution, working-capital evolution of the manufacturing provider, default/cancellation economics, inferred supply-access contracts and validated learning response surfaces. Customer/site observed data are needed before using its rankings for investment or deployment.

Shared cell/year/search/status controls and economic sliders are implemented. Specialized crossfilters for every provider/harness, geography, component grade and openness layer remain incomplete; those dimensions are inspectable/searchable in the saved evidence cards. Every view labels unlinked reference evidence. Source packages and their exact fields are available from each card, including unknown quantities and observation dates. The browser is a local analysis tool, not a deployed public service.

Meaningful checks cover component/finished/WIP/commissioning conservation, service priority and shared budgets, installed-site workload limits, replacement backlog, joint contrasts, commercial transfer cancellation, source-preserving scenario changes, newco demand/cash/receivables/funding constraints, target backcast identities, observed atlas source arithmetic, API validation and export/reload. Independent review caught and corrected cross-site output leakage and inconsistent treatment of assembly rejects in per-unit economics.

## Conditional intelligence-layer architecture reference

`model.engine.run_architecture_comparison` adds four generic structures around the same matched-service functions. It separates physical/model resources from hardware, integration, model and service payments, consolidates logical roles into entities, and calculates conditional fee intervals using integer-cent schedules. Complete effective architecture parameters travel with ordinary scenario exports; selected comparison exports also retain cell/year scope. Prior scalar numerical outputs remain unchanged.

See [ARCHITECTURES.md](ARCHITECTURES.md) for the explicit resource, allocation and cash boundaries. The calculator replaces the scalar digital-service bundle with itemized model costs, holds selected-year conditions over service life, assumes operator purchase and sufficient human fallback, and does not reconstruct an actual company cash calendar or shared-fleet financing. Real vendor prices, rights and qualification remain unknown in the evidence packet. A positive annual equivalent is not proof of available startup cash or customer retention.


## Monthly commercial extension, separately scoped

[Stage 3 methods](MONTHLY_COMMERCIAL.md) compare sale, independent lease and provider-owned availability service on the shared integer physical plan and Treasury. Ten synthetic witnesses expose purchase/title gates, grouped settlement, rent/service arrears, support suspension and refundable deposits. Fully funded arrangements have equal physical vendor outlays; funding failures can change output. The API and Business models witness picker use the same export. These are separately scoped monthly cases: annual sliders, the entrant demand calculation and K lifetime architecture costs do not flow into them. Stage 3 alone excludes common entrant demand and enterprise obligations; stage 4 below adds a bounded shared case. Broader financing and annual/architecture bridges remain partial.


## One shared entrant/incumbent market

[Stage 4](SHARED_ENTERPRISE.md) now adds a common recurring demand ledger, funded human shifts, enterprise obligations, output invoices and actual equity transfers to the same monthly physical/commercial/Treasury loop. The primary Customer adoption view uses this result. It replaces independent entrant capacity in the new world; historical ENTRY-FG-01 remains separate and is never added. Human and robot delivery reconcile once in `WORK-FLOOR-BUNDLE-SYN-02`; no cleaning-zone or labor-hour conversion is inferred. Loan schedules, autonomous reinvestment, recovery, empirical costs and annual/K architecture bridges remain open.


## Regional reported-metric and rights boundaries

[The regional K source audit](../research/regional_frontier_models.md) adds publisher-defined task metrics, artifact grants and operator references to the evidence layer. `frontier_models.regional_source_arithmetic` checks reported means/units and preserves a PDF/HTML count-to-score discrepancy without inventing a corrected empirical effect. Mixed progress is not complete service; a desktop median or control-loop frequency is not an onboard deadline. Public noncommercial weights, permissive code/base releases and private commercial agreements are separate scopes. These source records change no synthetic model parameter or numerical scenario output.


### Customer-service source arithmetic, continuation 7 November 2026

`deployment_source_arithmetic` in `frontier_models.py` uses K-E039's matched population, observation period and reported fold-rate/quality/window units. It reproduces rounded output and an output margin; it supplies no financial return or paid-labor estimate. The additional time-loss sensitivity is conditional on an active-time rate, whose basis remains undisclosed. The base arithmetic applies no extra uptime discount. Dyna mixed task-ceiling and partially credited language metrics cannot become whole-job probabilities, and all source checks remain outside the scenario engines.
