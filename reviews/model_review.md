# Independent model and acceptance review

Reviewed 25 October 2026. The observed input campaign revision belongs in the ignored operational `sync_receipt.json`. Reviewer owns this file only; implementation fixes remain with the model/dashboard owner.

## Result and scope

The functioning engine is suitable as an explicitly synthetic research checkpoint after two consequential accounting defects were corrected. This is **not** acceptance of a calibrated market model, complete enterprise financial model, or the full seven-day specification.

Final accounting snapshot tested:

- `model/engine.py` SHA-256: `5ff697ba757c04edf75bda597867e1b17e4b7e854b04210148bf8ed693bd9ea0`.
- Final `model/assumptions.json` SHA-256: `a71044379485dfe1fd1fd87cfd81f6f5ecde80047911fbb8f843a9d30b82c965`. Operational metadata cleanup followed the numerical audit; the identical numerical catalog and regenerated artifacts were independently rechecked as described below.
- Independent randomized/adversarial run: 150 parameter combinations, seed 9137, plus consequence checks and fresh CLI export/reload; **87,114 assertions, zero failures**.
- Owner-maintained tests, executed independently: `python -m unittest discover -s tests -v`; **15 tests passed**, including local HTTP catalog, recalculation and reload.

This review read the engine, assumptions, export/report/server scripts, interface logic and tests. It inspected the user specifications for physical stock/flow, shared resources, ownership/cash boundaries, entrant demand/funding, learning and the digital/physical comparison. No browser-rendering acceptance is claimed here; this reviewer examined interface code and API behavior. No source-derived numerical coefficient was validated because the engine identifies all numerical parameters as synthetic assumptions.

## Corrected findings

### MR-01 — High: output implicitly moved between uncommissioned sites

The original fleet calculation capped output by all economically ready sites' demand, rather than the demand at sites with commissioned robots. This conflicted with the constructed one-robot-per-site population and the separate matched-site calculation.

Reproduction used:

```python
from model.engine import run_scenario
r = run_scenario({
    "capability": 1, "capability_progress": 0, "uptime": 1,
    "intervention_minutes": 0, "coordination": 0.6,
    "digital_efficiency": 0, "labor_avoidability": 1,
})
```

Before correction, manufacturing in 2029 had eight active robots but 153,600 accepted baseline units, exceeding eight sites × 16,000 units = 128,000. In 2033, six active robots with no commissioning produced the same 153,600 against 96,000 installed-site units. This was not a mere floating-point or waterfall identity failure; it introduced an unmodeled cross-site service arrangement.

The owner now limits baseline output to supported productive robot-years times per-site work, additionally bounded by physical capacity and ready demand. New commissioning has the stated half-year ramp. Expansion demand is bounded at those same sites. The installed-capacity waterfall also caps robot capacity at the per-site workload. Rechecked with the original adverse case and randomized workloads: resolved. This is a conservative annual-flow convention; seasonal concentration or mobile inter-site service would need a separate model.

### MR-02 — High: assembly rejects disappeared from deployed-unit economics

The original fleet and backcast charged manufacturing cost per assembly start and discarded rejected units, but matched resource economics and provider cash charged that same amount per accepted robot. Lower yield therefore increased funding required for physical production while leaving reported deployed-unit resource cost and supplier margin unchanged.

For a humanoid, yields of 1, 0.5 and 0.1 implied expected manufacturing costs of $36,000, $72,000 and $360,000 per accepted robot. Before correction, the resource-capital figure including $4,200 integration stayed at $40,200 and provider initial sale cash stayed at +$24,000 for all three.

The owner made the catalog convention explicit: manufacturing cost is per assembly start. Matched-site economics and commercial cash now use `start_cost / assembly_yield`; production and backcast still charge `starts × start_cost`. Yield is still applied once in the physical flow. Provider and lease-financier lifetime-margin feasibility checks now accompany customer savings/payback gates. Independent tests verified cost ratios, cash cancellation and adverse yield outcomes: resolved. The margins are undiscounted synthetic feasibility screens, not risk-adjusted investment returns.

### MR-03 — Medium: scenario identity omitted the executable engine

Previously, the scenario hash included catalog and parameters but omitted engine code. Two code versions could produce different outputs under the same exported hash if the catalog version string was unchanged.

The result now includes `engine_sha256`; the scenario fingerprint includes that hash, catalog and parameters. Evidence package hashes are separately exposed. Fresh exports reloaded through the same code reproduce exactly. Resolved for the tested snapshot. Any later code change requires fresh exports; a hash is provenance, not evidence of analytical validity.

### MR-04 — Medium: calendar selection concealed fixed reference periods

The joint-cost table uses final-horizon exogenous capability without the learned increment, while commercial lifetime cash uses initial capability. The global calendar selector previously appeared to apply to both.

The interface now explicitly labels these reference scopes and says that the year filter does not change them. The newco case already identifies its separate fixed CELL-M11/monthly-unit scope. This resolves the misleading display boundary, without claiming those reference comparisons have become a cohort-level financial model. Annual fleet rows retain their actual dated capability.

## Independent verification performed

The randomized sample varied horizon, capability and progress, uptime, intervention, digital efficiency and expense, positive/negative coordination, integration, shared support/funding, labor avoidability, supply, yield, spares, retirement, learning, configuration, customer profile and commercial terms. Checks included:

| Boundary | Result |
| --- | --- |
| Compatible components | Opening stock + qualified receipts − service − assembly = closing stock; no negative inventory. |
| Manufacturing | Finished stock reconciles; WIP opening + starts − accepted − rejected = WIP closing. |
| Shipment/commissioning | Transit opening + shipments − commissions = transit closing; explicit annual lag. |
| Fleet | Prior active + commissioned − retired = active; expansion/replacement split and replacement backlog reconcile. |
| Useful output | Baseline output cannot exceed installed-site work after the correction; waterfall remains in one baseline-equivalent-hours denominator. |
| Shared resources | Customer/provider/integration reservations remain within budgets; existing support plus expansion support reservations do not spend the same hours twice. |
| Commercial accounting | Customer, provider and financier cash sum to consolidated incremental cash; inter-party transfers cancel. |
| Manufacturing economics | Per-accepted manufacturing cost × assembly yield equals per-start manufacturing cost. |
| Entry | Served units stay within capacity and won demand; transferred share plus remaining incumbent activity equals baseline activity. |
| Digital/physical contrast | Interaction and incremental/joint savings reconcile from the same four costs. |
| Export/reload | Fresh CLI exports to a temporary directory reproduce exactly through `run_scenario(saved_parameters, saved_preset)`. |

Zero supply, zero provider funding, zero support, zero integration capacity, zero assumed labor cash avoidability, and zero capability/progress each produced zero retained fleet in the tested constructed setting. These are consequences rather than copied implementation formulas.

Representative controls changed their intended outputs. Digital efficiency and coordination changed fleet/joint/commercial values; labor avoidability changed cash and eligibility while leaving opportunity-cost valuation separate; yield changed physical/economic/backcast results; learning changed fleet outcomes; entrant funding and incumbent response changed only the separate entry case; target stock changed the backcast; support capacity changed fleet operation. All 33 parsed dashboard control keys matched supported engine parameters. A validation-cost change with transfer disabled is locally inactive by construction; it is not evidence of a functioning learning estimate.

Observed payroll removed remains null. The explicitly assumed avoidability fraction supplies hypothetical customer cash savings, while resource-cost comparisons value released labor opportunity. This distinction is retained in both code and interface. Evidence is not numerically modified by scenario controls.

## Remaining acceptance limits

| Requirement | Current judgment and consequence |
| --- | --- |
| Physical flow, supported fleet and stock/flow | Pass for the stated expected fractional-unit annual model. This is not a discrete production schedule, maintenance-event simulator or empirically qualified supply estimate. |
| Full customer/provider cash | Partial. One-site lifecycle cash is reconciled, and annual fleet capital envelopes constrain starts/shipments. They do not form one consolidated company treasury with working capital, interim cash shortages, tax, interest, defaults and cash reinvestment. |
| Entry finance and competition | Partial. Monthly ramp, receivables, funding gaps, share transfer, unmet demand, expansion and same-robot-access reference are explicit. Unfunded rows are conditional additional-funding paths. The ten-robot entry case is separate from the six-cell fleet and does not draw from its shared component/commissioning budgets; it must never be added as independently feasible output from those resources. |
| Backcast | Pass as a necessary-condition resource witness with replacement and lead-time accounting. It does not test a demand forecast, capital availability or sufficient feasible capacity. A target can exceed the synthetic 72-site pool only as a separate necessary-condition exercise. |
| Learning and control | Partial. Optional same-configuration exposure/validation affects future capability without a separate data-value premium. Useful data, rights, cross-embodiment transfer, policy selection and causal improvement remain uncalibrated. |
| Physical–digital coordination | Partial. A separate positive/negative coordination parameter and explicit support resources exist. Correlated failures, congestion, queue distributions, enterprise transactions and recovery are not dynamically modeled. |
| Robotics R&D acceleration | Research contribution map only. No executable fixed-objective engineering critical-path/candidate-validation model exists in this engine. |
| Embodiment alternatives | Synthetic comparison only. Specialized-cost factors and the mixed-process allocation are explicit assumptions, now calculated in the common engine. They do not prove an actually feasible configured alternative. |
| One calculation source | Pass for the tested snapshot. API, saved scenarios and quantitative exports call the common engine; report builder consumes exported tables. All eight saved scenarios and 24 exported tables reproduce exactly. No independent dashboard formula remains for the specialized/mixed economic comparison. |
| Dashboard acceptance | API and control wiring reviewed here. The lead's separate [browser review](browser_review.md) records all 13 views, 52 view/filter combinations, eight-scenario comparison, scenario export/import and evidence invariance without page errors. Full accessibility, mobile and cross-browser acceptance remain outside those checks. |

## Final artifact disposition

The owner regenerated the saved results after the accounting corrections. This reviewer then loaded every repository-saved scenario and independently called `run_scenario(saved_parameters, saved_preset)`: **all eight complete result objects matched exactly**, including their current engine and evidence hashes. All **24** component, production and joint CSV tables matched the corresponding result rows, field by field. All **eight** scenario summary rows matched their scenario hashes and cumulative baseline-equivalent-hour totals. After the operational metadata cleanup and another independent full artifact check, the final reference scenario hash is `c1159d455458d55940240379b3854211bc0ea7f91a8276303eeeb6087b1d5c30`.

The lead subsequently moved the observed launch-repository revision out of published catalog/prose metadata to the operational-receipt boundary required by `AGENTS.md`. The engine bytes did not change. This reviewer reconstructed the prior catalog hash by restoring only that metadata field's value and original key placement, confirming that numerical inputs were identical. The changed catalog and evidence metadata correctly produced different scenario hashes. The eight-JSON, 24-table and eight-summary checks above were repeated successfully against the final regenerated files; the earlier numerical tests remain applicable to the unchanged numerical catalog.

`model/METHODS.md` and `REPRODUCE.md` are present and were read in full. They describe the tested annual lags, start-cost/yield convention, installed-site work bound, nonrevolving annual capital envelopes, separate entry case, reference-period scopes and reproducible local commands. The report builder reads the verified summary CSV and authoritative research chapters; final report assembly belongs to the lead's release check and adds no second economic calculator.

The delayed-supply scenario's terminal stock of 60 versus the reference's 44 is sensitive to commissioning and retirement timing. Cumulative output is now included in the common export so an end-date fleet comparison cannot by itself be mistaken for a cumulative service improvement.

**Disposition:** accept the accounting and reproducibility of this bounded, explicitly synthetic checkpoint at the hashes above. Retain the partial statuses in the acceptance table. No unresolved high-severity computational defect was found in this audit after the two corrections; this conclusion neither calibrates the assumptions nor completes the campaign specification.
