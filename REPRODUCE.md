# Reproduce the local research edition

The active decision campaign adds a cell-filtered provisional decision panel to every view. It reads `decision_reassessment` and `decision_packs` from the existing market evidence package. Source gates and explicit unknowns remain fixed when synthetic controls change. Fourteen financed worlds cover bounded DE-CF11/12. Eight calendar/digital worlds add bounded DE-CF01/13 and partial support/frozen-cohort mechanisms; broad campaign coverage remains incomplete. Ten funded monthly architecture worlds add bounded DE-CF08 and engineering-before-expansion mechanisms. Existing commands retain their stated scopes.

Python 3.10 or newer is sufficient. Earlier validation used Python 3.12.14 on Linux; annual-path continuation also runs on the canonical Mac checkout. The model/server/export commands have **no third-party dependencies, credentials, network requests, GPU requirements or paid services**. Node is optional for the JavaScript syntax check. The dashboard needs a current browser with `fetch` and native `<dialog>` support.

From the repository root:

```bash
python3 -m unittest discover -s tests -v
python3 scripts/validate_evidence.py
python3 scripts/extract_physical_requirements.py --check
python3 scripts/build_physical_requirements.py --check
python3 scripts/export_frontier_models.py --check
python3 scripts/export_scenarios.py
python3 scripts/export_experiments.py
python3 scripts/export_monthly_commercial.py
python3 scripts/export_enterprise.py
python3 scripts/export_enterprise.py --bridge
python3 scripts/export_finance.py --check
python3 scripts/export_calendar_bridge.py --check
python3 scripts/export_monthly_architectures.py --check
python3 scripts/export_conventional_coordination.py --check
python3 scripts/export_entry_transitions.py --check
python3 scripts/export_utility_inspection.py --check
python3 scripts/export_automotive_workcell.py --check
python3 scripts/export_trajectory.py
python3 scripts/export_architectures.py --experiments-output model/results/architecture_experiments.json
python3 scripts/build_continuation.py
python3 scripts/build_report.py
python3 scripts/serve.py --port 8765
```

Open **http://127.0.0.1:8765**. The server binds to localhost only. Stop it with Ctrl-C. Opening the HTML file directly does not run the Python calculation API. If the port is occupied, choose another local port with `--port 8766`.

The page presents thirteen linked research views. Select a market-stage cell and annual period, inspect the evidence search/status filters, then change a scenario slider or commercial/customer setting. The Python engine recomputes affected outputs; the scenario hash changes and saved evidence stays fixed. Broad reference totals and fixed-horizon comparisons are labeled. The persistent synthetic label applies to every numerical scenario; it does not turn official employment records into synthetic data.

All empirical/model distinctions, equations, time conventions, resource boundaries and incomplete requirements are documented in [model/METHODS.md](model/METHODS.md). This is an intermediate executable edition. It does not establish calibrated robot unit economics or completion of the full seven-day research campaign.

In the joint comparison tables (Improvement, Digital AI ecosystem, or Analogies), select **Trace inputs and costs**. The dialog shows the four matched branches, their human/digital, robot operating and annual capital costs, accepted robot output, retained human hours, exact inputs and engine function excerpts. It follows the selected calendar year, using that year's resolved digital values and exogenous capability. Changing scope invalidates an open trace. These are synthetic coefficients with no empirical calibration sources. Open **Annual digital paths** to enter comma-separated levels for each year; blank channels retain scalar values. Supplied arrays disable the corresponding scalar sliders. Clear paths before changing the horizon. Invalid paths retain the last valid result and display an error; exports then still represent that last valid result. This drilldown covers joint comparisons only.

Open **Evidence fields** to filter exact recorded geography, system/configuration, embodiment, harness, openness layer or license. These selectors change evidence navigation only. Missing fields are selectable and are excluded by a chosen explicit value; compound source descriptions retain their original wording. See [filter semantics and remaining gaps](dashboard/EVIDENCE_FILTERS.md). With Node installed, run `node tests/test_facets.js` for the browser helper's exact-field checks.

## Export and reload

The export command writes deterministic files under `model/results/`:

- `{preset}.json`: complete parameters, engine/scenario hashes, evidence snapshot hashes, assumptions and results.
- `{preset}_components.csv` and `{preset}_production.csv`: annual inventories, spares, starts, acceptance, WIP, shipments and commissioning pipeline.
- `{preset}_joint.csv`: final-year matched digital/physical 2 × 2 resource-cost comparisons.
- `{preset}_joint_by_year.csv`: the same comparisons for every calendar year, with effective channel levels.
- `annual_digital_comparison.json`: six full five-year counterfactuals with learning disabled; generated by `export_trajectory.py`.
- `scenario_summary.csv`: selected summary measures for all saved presets.
- `observed_atlas_summary.json`: official-statistics source-row arithmetic and reconciliation, computed independently of scenario inputs.
- `observed_research_summary.json`: audited field-study ratios/mean contrasts and archived benchmark-cost reconstruction, when those input packages are accepted.

The separate `export_experiments.py` command writes `treasury_witnesses.json`, `coordination_witnesses.json` and `monthly_deployment_witnesses.json`. These contain isolated synthetic settlement, protocol and paid-physical-flow examples, with code/dependency hashes and event traces. They do not change the annual scenario outputs or calibrate their coefficients. See [the treasury core](model/TREASURY_CORE.md), [coordination fixture](model/COORDINATION_TRANSACTION_FIXTURE.md) and [monthly fixture](model/MONTHLY_DEPLOYMENT.md) for their narrower scope. The full report incorporates these exports and rejects stale experiment code/dependency hashes.

The page's **Export scenario** button downloads the same current engine result, including changed parameters. **Export selected cohort CSV** downloads all annual rows for the selected cell scope. The file input in the sidebar reloads an exported scenario and recalculates it. To rerun one saved result from the command line:

```bash
python3 scripts/export_scenarios.py --scenario model/results/newco_raas.json --output /tmp/robotics-reloaded
```

Compare `scenario_hash`, `model_source_hashes`, supplied and resolved paths, and numerical outputs. Legacy scalar inputs retain their saved horizon and become constant annual levels under the new model; their historical hashes require the old checkout. If engine code or assumptions have changed, a new hash is expected; a saved override object is not a frozen copy of old source code. Check out the matching repository revision for historical reproduction. Evidence hashes identify the saved record snapshots, not proof that those records calibrate the scenario.

Programmatic use:

```python
from model.engine import run_scenario
result = run_scenario({"intervention_minutes": 9, "spares_rate": 0.2}, "reference")
print(result["fleet"]["years"][-1])
print(result["newco"]["funding_gap_usd"])
```

Unknown parameter names, null quantitative overrides, nonfinite values, out-of-range inputs and unsupported choices raise an error. A measured/scenario zero and an unknown evidence value are separate states.

## Files and validation boundaries

`model/assumptions.json` is the numerical source of truth. `model/engine.py` supplies scenario calculations and `model/trajectories.py` validates/resolves annual levels; `model/evidence.py` and `model/research_calculations.py` supply observed-data transformations. `data/package_index.json` explicitly lists accepted evidence packages; filenames alone do not grant acceptance. `model/packages.py` loads that same registry for the server, provenance hashes and validator. See [PACKAGE_VALIDATION.md](model/PACKAGE_VALIDATION.md) for documented aliases, required context and null handling. `research/*.md` holds the associated analysis. `scripts/serve.py` exposes a read-only local catalog and a pure recalculation endpoint. It blocks `.git`, operational paths and arbitrary workspace files.

The tests cover inventory/cohort/financial invariants and adverse scenarios, including zero supply, absent capability, low yield, high service burden, no payroll avoidability and limited funding. Evidence validation checks unique claim IDs and cross-package evidence references. `node --check dashboard/app.js` checks client syntax when Node is installed. Browser interaction/visual checks are reported separately in the campaign acceptance audit; successful unit tests alone do not validate every crossfilter or prove empirical calibration.

Evidence loads from the saved snapshot at browser startup. Reload the browser after adding evidence files. Restart the server after changing Python code; it deliberately has no background auto-reloader. Regenerate exports and the report after an accepted model or evidence change. No command here publishes a website or modifies an external service.

Annual-input browser helpers can be checked with `node tests/test_scenario_io.js` alongside `node tests/test_facets.js` and `node --check dashboard/app.js`. The regression fixture in `tests/fixtures/annual_scalar_v0_1_1.json` checks all 69,315 pre-existing numerical fields across sixteen cases; its generation hash identifies the prior scalar engine. No missing cloud implementation or prior interrupted test is treated as recovered validation.

## Reproduce the physical-requirements crosswalk

The unchanged BLS ORS workbook and OEWS national ZIP are preserved under `data/sources/physical_requirements/`. The source manifest records their URLs, release/observation periods and byte hashes. `python3 scripts/extract_physical_requirements.py --check` scans the two worksheets and compares the saved row extraction, including missing keys and footnote codes. The reader uses only Python's standard library; it does not recalculate or modify either workbook. A separate bundled-library comparison was used during review.

`python3 scripts/build_physical_requirements.py --check` verifies the evidence package and observed summary from the extracted rows. To deliberately regenerate reviewed outputs, run both commands without `--check`, then run evidence validation, the scenario exporters and report builder. A source hash change requires source review; do not relabel a different workbook as the accepted snapshot. The dashboard loads this package only through the explicit registry and displays it in the atlas. Changing a synthetic scenario does not change the observed requirements. Missing occupation matches, unavailable values and threshold footnotes remain distinct. No physical-hours or robot-addressability calculation is performed.

## Reproduce frontier-model source boundaries

`data/frontier_model_economics.json` contains the accepted primary-source claims, actor/model/rights records, ten dossiers and unpriced architecture alternatives. Code and model-card revisions are pinned separately; public model weights and GPU/robot workloads were not executed. `python3 scripts/export_frontier_models.py --check` validates actor/relationship joins, rights uncertainty and explicit absent costs, then reproduces Zebra's seller-disclosure arithmetic. Run without `--check` only to regenerate the reviewed summary, followed by scenario exports and the report builder. The report and local API consume this same source summary.

The helper never adds ARR to cumulative recognized revenue, treats equity/escrow as cash, or ranks incompatible benchmark scores. Evidence filters navigate the new records within the existing thirteen views. Provider roles, model/rights cards and the observed transaction are separate from synthetic scenario controls. A separate conditional architecture calculator is available in Business models; it uses synthetic assumptions and leaves observed costs/rights/qualification unresolved.

## Conditional architecture replay

Run `python3 scripts/export_architectures.py --experiments-output model/results/architecture_experiments.json` for the reference and eight witnesses. Replay a downloaded case with `python3 scripts/export_architectures.py --scenario saved-architecture.json --output replay.json`. Complete inputs, source hashes and cell/year scope are retained; normal scenario exports also preserve architecture parameters.

In Business models, edit fields and select **Apply architecture assumptions**. Pending edits leave displayed/exported results unchanged. Reset uses explicit catalog defaults. Invalid or unadmitted cases are not zero-cost alternatives. All-cell scope uses a labeled manufacturing reference. See [ARCHITECTURES.md](model/ARCHITECTURES.md) for operator purchase, allocated lifetime costs, human fallback, transfer cancellation and financing limits. Legacy sale/lease/service and monthly models remain separate. Historical model identities require their original revision.


## Monthly commercial cases

Business models now includes a fixed five-month sale/lease/provider-service comparison and seven adverse cases. Use its witness picker to inspect cash, supported output and title/custody, then **Export this monthly case**. These are separate from annual scenario controls and the annual import input. Recompute a downloaded case from its complete opening inputs:

```sh
python3 scripts/export_monthly_commercial.py --case monthly-lease.json --output replay.json
python3 scripts/export_monthly_commercial.py --check
```

The default export is `model/results/monthly_commercial.json`; the API is `/api/monthly-commercial`. [Methods and exclusions](model/MONTHLY_COMMERCIAL.md) define all synthetic terms, existing-obligation limits and the absent entrant/annual bridge. Saved-input replay also reconstructs preexisting Treasury events, encumbrances and credit without treating a receivable or commitment as cash.


## Shared incumbent/entrant market

Customer adoption now begins with the shared eight-month market and cash calculation. Choose one of eight witnesses or change entrant opening cash, extra funded equity, incumbent procurement timing, a scheduled customer-return attempt, and collection timing; click **Apply shared-market assumptions**. These controls are independent of annual cell/year controls. The prior ENTRY-FG-01 illustration remains collapsed as a historical separate reference.

```sh
python3 scripts/export_enterprise.py
python3 scripts/export_enterprise.py --bridge
python3 scripts/export_enterprise.py --case shared-enterprise-custom.json --output replay.json
```

The default artifacts are `model/results/shared_enterprise.json` and `model/results/enterprise_funding_bridge.json`. Each downloaded shared case carries complete opening inputs, source hashes and a case hash. The API is `/api/shared-enterprise` (GET witnesses; POST an `inputs` object). Exact cents, dated customer moves, paid human shifts and actual supported robot cohorts are described in [SHARED_ENTERPRISE.md](model/SHARED_ENTERPRISE.md). A different source revision changes case identity; no source claim or annual scenario coefficient is calibrated by these synthetic terms.


## Regional frontier-model source checks

`python3 scripts/export_frontier_models.py --check` verifies the saved source-summary calculation and code/data hashes. `python3 -m unittest discover -s tests -p test_frontier_models.py -v` tests artifact rights, identity/attribution and metric boundaries. The summary now keeps RLDX's mixed ALLEX mean, desktop p50 ratio, RynnBrain's separate final/process means and the unresolved RLDX Table 9 score/count conflict. It does not run a model or repair the source's empirical result.

Providers & systems shows the source checks; Business models shows layered grants; Customer adoption includes operator references with checkpoint/title/operating unknowns. Source buttons open dated records and immutable links where available. The [regional review](reviews/regional_frontier_review.md) documents primary-source/PDF inspection and remaining limits. Source PDFs and retrieval/cleanup receipts remain local operational material, outside the published manifest.


## Generalist/Dyna continuation source boundary

The 7 November 2026 continuation uses the same `export_frontier_models.py` command and existing frontier tests. The summary adds Dyna's reported restaurant rate/quality/window arithmetic, mixed task-ceiling scores and partial-credit language scores. Unknown financial ROI, paid labor removal and observed uptime remain explicit. A conditional time-loss budget is not an extra measured availability factor. Providers & systems shows these source checks; Customer adoption retains four distinct operator/reference cards. See [the analysis](research/generalist_dyna_deployment.md) and [sole-lead review](reviews/generalist_dyna_review.md). No scenario coefficient changes.


## Restaurant workflow and cloud replay, edition 0.12

The existing customer package now includes FG-E015–FG-E018, the separately scoped advertised pay/item-rate quantities, and FG-CMP-03. Customer adoption shows the four alternatives, retained work, measurement protocol, distinct labor outcomes and customer/provider/consolidated boundaries. Source buttons open the original records. This M09 reference is outside the six synthetic cells and remains fixed when annual scenario controls change. No rate or wage enters the assumptions.

Fresh cloud checks ran on Python 3.12.14 and Node 24.22.1, using Chromium for local browser verification. The first unmodified run passed 195 of 196 Python tests: the exact frozen scalar hash failed because two annual-hour sums used Python-version-dependent float aggregation. The engine now preserves their historical addition order; all 69,315 frozen numeric fields match without a changed oracle. All 196 tests then pass; a focused Python 3.13 replay provides a separate portability check. Earlier Mac results remain historical.

See [the sole-lead review](reviews/napkin_workflow_review.md) for the final checks and evidence limits. These checks establish execution and this bounded checkpoint, not continuous weekday uptime or activation of a native goal. No supported goal-creation control is exposed here.


## Dated finance and service continuity, edition 0.14

The Customer adoption view adds **Dated finance, service interruption and cash recovery**. Choose one of fourteen worlds or edit cash, draw/maturity dates, rate, rescue, response, payment priority, default policy and the later-start reserve. Apply recomputes the existing monthly physical/customer/Treasury loop; these controls do not alter annual cell/year scenarios. Rates and contracts are synthetic assumptions. A null default date means no debt-policy default, not necessarily funded service. Trace the equations, exact interest inputs and source hashes before interpreting a difference.

Export financed case downloads all physical, commercial, enterprise, Treasury and financing inputs/results. Reload recomputes the full saved inputs under current code; changing a saved output cannot change the replay. An imported full ledger retains its own work unit and horizon. The monthly table follows the entrant operator where present, otherwise the first operator, and aggregates that actor's loans. Headline financing totals include all loans. Choose a standard witness to return to editable shortcut controls. Historical source changes produce a new hash, with an explicit message; exact historical reproduction needs the corresponding checkout. Invalid or stale requests preserve the last valid display/export.

```bash
python3 scripts/export_finance.py
python3 scripts/export_finance.py --check
python3 scripts/export_finance.py --case /tmp/financed-case.json --output /tmp/financed-replay.json
python3 -m unittest tests.test_enterprise_finance -v
```

`GET /api/enterprise-finance` returns the deterministic witness bundle. `POST` accepts exactly one of `inputs` (validated shortcut controls) or `saved_case` (a complete financed execution). The complete JSON includes five model-source hashes, a case hash, exact cents/rational service, event journals and seven metric-lineage records. No network, credentials or third-party Python packages are required by these commands. See [methods](model/ENTERPRISE_FINANCE.md), [research findings](research/financed_execution.md) and [sole-writer review](reviews/enterprise_finance_review.md).

This adds dated finance and cash recovery. It does not implement collateral sale, legal insolvency, debt restructuring, autonomous investment optimization, empirical financing terms or annual/architecture bridges.


## Annual digital paths inside monthly execution, edition 0.15

The Customer adoption view adds **Annual digital paths inside monthly execution**. Select a complete witness or edit calendar dates, annual path arrays, resource allocations, cohort policy, qualification cost/hours and funding. Apply recalculates actual cohorts, paid invoices and delivered service. A 60-to-65-hour support allocation changes how many robots can upgrade in the January witness. These controls belong to the matched cleaning-service case; the ordinary annual fleet and four intelligence-architecture references remain separately scoped.

The four C00/C01/C10/C11 branches hold staffing and customer moves fixed. Their task-time differences do not reduce payroll automatically. Calendar-year totals contain the months actually observed; no annual extrapolation occurs. Open the trace for seven equation/input/provenance records, unit/cost/resource mappings, exact cohort IDs and rounding lines. The old floor bundle has no inferred conversion.

```bash
python3 scripts/export_calendar_bridge.py
python3 scripts/export_calendar_bridge.py --check
python3 scripts/export_calendar_bridge.py --case /tmp/calendar-case.json --output /tmp/calendar-replay.json
python3 -m unittest tests.test_calendar_bridge -v
```

Export/reload preserves the full physical, commercial, enterprise, finance and bridge inputs. The bridge uses decimal strings for rational numerator/denominator components and rejects unsafe non-rational integers, preserving exact exported data through browser JSON. Replay ignores saved outcomes and recomputes under current source; historical reproduction requires the corresponding checkout. Invalid inputs and late responses preserve the last valid display/export. Imported complete cases keep their unit/horizon and are read-only in the shortcut editor; selecting a standard witness restores editable controls. `GET /api/calendar-bridge` returns the bundle; `POST` accepts exactly one `inputs` or `saved_case`. See [methods](model/CALENDAR_BRIDGE.md), [findings](research/calendar_digital_execution.md) and [sole-writer review](reviews/calendar_bridge_review.md).

## Funded intelligence roles, edition 0.16

Business models now includes a separate monthly architecture panel. It maps the four catalog profiles to funded legal accounts on the existing calendar/physical loop. One active cleaning-service business retains fixed staffing and common demand. Fees redistribute cash; itemized resource bills enter consolidated outlay once. The annual architecture calculator retains its separate lifetime/avoided-cost-credit scope.

```bash
python3 scripts/export_monthly_architectures.py
python3 scripts/export_monthly_architectures.py --check
python3 scripts/export_conventional_coordination.py --check
python3 scripts/export_monthly_architectures.py --case /tmp/monthly-architecture.json --output /tmp/architecture-replay.json
python3 -m unittest tests.test_monthly_architectures -v
node --check dashboard/monthly_architectures.js
```

Ten worlds include the four profiles, fee/capital/resource constraints and a false rights premise. Complete inputs and twelve source/catalog hashes identify each result. Export/reload recomputes the full saved case; saved outcomes cannot replace calculation. Rational components use decimal strings and equivalent integral numeric spellings are canonicalized before hashing. Invalid or stale requests preserve the last valid result. Imported complete cases are read-only in the shortcut controls until a witness is selected. `GET /api/monthly-architectures` returns the bundle; `POST` accepts exactly one `inputs` or `saved_case` object. See [methods](model/MONTHLY_ARCHITECTURES.md), [findings](research/monthly_intelligence_execution.md) and [review](reviews/monthly_architectures_review.md).


## Conventional coordination and mandatory service

Learning & coordination now starts with twelve bounded service-window worlds. Edit proposal delay, planning/verification capacity prices, opening cash, the urgent path, robot availability and the declared standby reserve; click **Apply coordination assumptions**. These are separate from annual/monthly scenarios. Display and export retain the last applied valid case. Complete imported and fixed adversarial-proposal cases are read-only in the panel.

```sh
python3 scripts/export_conventional_coordination.py --check
python3 scripts/export_conventional_coordination.py --case downloaded.json --output replay.json
```

The API is `/api/conventional-coordination`. Complete saved workload/controller inputs are rerun, with saved outcomes ignored. The [methods](model/CONVENTIONAL_COORDINATION.md) define observed-queue exactness, shared authority, all-attempt resource cash, retained paid staffing and the absent real-system/LLM evaluation. The browser trace shows information available at each decision, not just the final accepted count.


## Funded acquisition and hybrid entry

Customer adoption now begins with fifteen entry worlds. Edit buyer/target cash, consideration, separate target or growth equity, diligence/transition bills, closing month, interruption and assumed consent. Pending/invalid edits preserve the last valid result. Complete imported inputs are replayed and shown read-only; choose a standard witness for shortcut controls.

```sh
python3 scripts/export_entry_transitions.py --check
python3 scripts/export_entry_transitions.py --case downloaded.json --output replay.json
```

The API is `/api/entry-transitions`. [Methods](model/ENTRY_TRANSITIONS.md) define funded all-or-none share closing, unchanged operating identities/obligations, fixed wider cash consolidation and unknown terminal value. No asset purchase or real legal/valuation conclusion is inferred.


## Utility inspection service replay

In Embodiment comparisons, use the utility-only inspection panel to inspect eighteen complete worlds or change coverage, review capacity, deadline, staffing contract and operating cash. Results count unique accepted point/windows and complete service separately; changing annual cell scope does not relabel these utility units. Edits are pending until applied. Invalid or stale calculations preserve the last valid export. Reload recomputes complete inputs and ignores saved outcomes. Run `python3 scripts/export_utility_inspection.py --case saved.json --output replay.json` for CLI replay. See [methods](model/UTILITY_INSPECTION.md) for exact units, cash boundaries and missing lifecycle costs.

## Reproduce automotive component flow

Run `python3 scripts/export_automotive_workcell.py --check` to verify eighteen complete workcell worlds. The Embodiment view offers buffer, picking, family-changeover, preparation, support and separately qualified replacement controls. A tick is five synthetic seconds. Every accepted kit requires all three unique components by its own deadline; retained staff, failed attempts and paid preparation remain explicit. Trace components, serial operations, assets and Treasury before comparing cash. These are conditional service tests, not observed automotive takt, whole-plant output or lifecycle ROI.

Export a case, then replay with `python3 scripts/export_automotive_workcell.py --case saved-workcell.json --output replay.json`. Complete inputs are recomputed; stored outcomes are ignored. Imported full cases disable shortcut controls until a standard witness is selected. Invalid or pending edits retain the last applied display/export, and stale replies cannot replace newer inputs. Local uploads are bounded to 2 MB. See [methods and limits](model/AUTOMOTIVE_WORKCELL.md) and [the automotive decision](research/automotive_workcell_decision.md).
