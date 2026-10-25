# Reproduce the local research edition

Python 3.10 or newer is sufficient. Development validation used Python 3.12.14 on Linux. The model/server/export commands have **no third-party dependencies, credentials, network requests, GPU requirements or paid services**. Node is optional for the JavaScript syntax check. The dashboard needs a current browser with `fetch` and native `<dialog>` support.

From the repository root:

```bash
python3 -m unittest discover -s tests -v
python3 scripts/validate_evidence.py
python3 scripts/export_scenarios.py
python3 scripts/export_experiments.py
python3 scripts/build_continuation.py
python3 scripts/build_report.py
python3 scripts/serve.py --port 8765
```

Open **http://127.0.0.1:8765**. The server binds to localhost only. Stop it with Ctrl-C. Opening the HTML file directly does not run the Python calculation API. If the port is occupied, choose another local port with `--port 8766`.

The page presents thirteen linked research views. Select a market-stage cell and annual period, inspect the evidence search/status filters, then change a scenario slider or commercial/customer setting. The Python engine recomputes affected outputs; the scenario hash changes and saved evidence stays fixed. Broad reference totals and fixed-horizon comparisons are labeled. The persistent synthetic label applies to every numerical scenario; it does not turn official employment records into synthetic data.

All empirical/model distinctions, equations, time conventions, resource boundaries and incomplete requirements are documented in [model/METHODS.md](model/METHODS.md). This is an intermediate executable edition. It does not establish calibrated robot unit economics or completion of the full seven-day research campaign.

In the joint comparison tables (Improvement, Digital AI ecosystem, or Analogies), select **Trace inputs and costs**. The dialog shows the four matched branches, their human/digital, robot operating and annual capital costs, accepted robot output, retained human hours, exact inputs and engine function excerpts. It uses the current scenario at its final horizon; changing the display-year filter does not change that reference horizon. These are synthetic coefficients with no empirical calibration sources. This drilldown covers joint comparisons only.

Open **Evidence fields** to filter exact recorded geography, system/configuration, embodiment, harness, openness layer or license. These selectors change evidence navigation only. Missing fields are selectable and are excluded by a chosen explicit value; compound source descriptions retain their original wording. See [filter semantics and remaining gaps](dashboard/EVIDENCE_FILTERS.md). With Node installed, run `node tests/test_facets.js` for the browser helper's exact-field checks.

## Export and reload

The export command writes deterministic files under `model/results/`:

- `{preset}.json`: complete parameters, engine/scenario hashes, evidence snapshot hashes, assumptions and results.
- `{preset}_components.csv` and `{preset}_production.csv`: annual inventories, spares, starts, acceptance, WIP, shipments and commissioning pipeline.
- `{preset}_joint.csv`: matched digital/physical 2 × 2 resource-cost comparisons.
- `scenario_summary.csv`: selected summary measures for all saved presets.
- `observed_atlas_summary.json`: official-statistics source-row arithmetic and reconciliation, computed independently of scenario inputs.
- `observed_research_summary.json`: audited field-study ratios/mean contrasts and archived benchmark-cost reconstruction, when those input packages are accepted.

The separate `export_experiments.py` command writes `treasury_witnesses.json`, `coordination_witnesses.json` and `monthly_deployment_witnesses.json`. These contain isolated synthetic settlement, protocol and paid-physical-flow examples, with code/dependency hashes and event traces. They do not change the annual scenario outputs or calibrate their coefficients. See [the treasury core](model/TREASURY_CORE.md), [coordination fixture](model/COORDINATION_TRANSACTION_FIXTURE.md) and [monthly fixture](model/MONTHLY_DEPLOYMENT.md) for their narrower scope. The full report incorporates these exports and rejects stale experiment code/dependency hashes.

The page's **Export scenario** button downloads the same current engine result, including changed parameters. **Export selected cohort CSV** downloads all annual rows for the selected cell scope. The file input in the sidebar reloads an exported scenario and recalculates it. To rerun one saved result from the command line:

```bash
python3 scripts/export_scenarios.py --scenario model/results/newco_raas.json --output /tmp/robotics-reloaded
```

Compare `scenario_hash`, `engine_sha256` and numerical outputs. If engine code or assumptions have changed, a new hash is expected; a saved override object is not a frozen copy of old source code. Check out the matching repository revision for historical reproduction. Evidence hashes identify the saved record snapshots, not proof that those records calibrate the scenario.

Programmatic use:

```python
from model.engine import run_scenario
result = run_scenario({"intervention_minutes": 9, "spares_rate": 0.2}, "reference")
print(result["fleet"]["years"][-1])
print(result["newco"]["funding_gap_usd"])
```

Unknown parameter names, null quantitative overrides, nonfinite values, out-of-range inputs and unsupported choices raise an error. A measured/scenario zero and an unknown evidence value are separate states.

## Files and validation boundaries

`model/assumptions.json` is the numerical source of truth. `model/engine.py` supplies scenario calculations; `model/evidence.py` and `model/research_calculations.py` supply observed-data transformations. `data/package_index.json` explicitly lists accepted evidence packages; filenames alone do not grant acceptance. `model/packages.py` loads that same registry for the server, provenance hashes and validator. See [PACKAGE_VALIDATION.md](model/PACKAGE_VALIDATION.md) for documented aliases, required context and null handling. `research/*.md` holds the associated analysis. `scripts/serve.py` exposes a read-only local catalog and a pure recalculation endpoint. It blocks `.git`, operational paths and arbitrary workspace files.

The tests cover inventory/cohort/financial invariants and adverse scenarios, including zero supply, absent capability, low yield, high service burden, no payroll avoidability and limited funding. Evidence validation checks unique claim IDs and cross-package evidence references. `node --check dashboard/app.js` checks client syntax when Node is installed. Browser interaction/visual checks are reported separately in the campaign acceptance audit; successful unit tests alone do not validate every crossfilter or prove empirical calibration.

Evidence loads from the saved snapshot at browser startup. Reload the browser after adding evidence files. Restart the server after changing Python code; it deliberately has no background auto-reloader. Regenerate exports and the report after an accepted model or evidence change. No command here publishes a website or modifies an external service.
