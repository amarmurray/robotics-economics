# Matched workcell labor and customer cash

Edition 0.56 · 11 November 2026. This adapter replays the unchanged [automotive engine](AUTOMOTIVE_WORKCELL.md) and its [eighteen saved worlds](results/automotive_workcell.json). It adds a comparison, not a new physical simulator, empirical calibration or lifecycle valuation.

## Service before a cost bound

`workcell_comparison.compare` takes exactly two complete engine inputs: `baseline` and `alternative`. Both run through the existing component-flow, qualification, staff-capacity, preparation, support, replacement and Treasury mechanisms. The same tick length, horizon, ordered job/variant/part set, supply/release/deadline and source-closure schedule must apply. Part identity ordering within a kit is irrelevant; production job order is not. Configurations, process arrangements and acquired assets may differ and remain disclosed.

Each execution must deliver every due unique kit on time and have no due unpaid commitment. Late eventual output does not backfill service. Unmatched or failed service produces `bounds: null`, never a cheap failed-service ranking. A successful replacement qualification does not excuse an earlier missed deadline. A failed optional replacement does not itself reject an otherwise fully served/funded obligation; its actual cash and assets remain in the execution.

The fourteen saved pairs are eight eligible comparisons and six ineligible challenges. They reuse existing inputs except for one explicitly reconstructed human comparator facing the exact mixed-family jobs of the fixed-cell case. Its assumed human qualification is inherited from the old fixture, not observed at a new plant. The fourteen pairs are not independent deployments or additions to the historical 271 challenge worlds.

## Work and cash equations

For each role, using executed quantities:

```
modeled person-seconds = (station person-ticks + preparation person-ticks) × tick seconds
customer outlay = staff receipts + station-resource receipts
                + preparation receipts + replacement-equipment receipts
alternative nonstaff cash = alternative outlay − alternative station-staff bill
staff-bill ceiling = baseline outlay − alternative nonstaff cash
net omitted-cost allowance = baseline outlay − alternative outlay
```

An alternative is at window cash parity only if its incremental omitted **net** costs (alternative minus baseline, net of separately demonstrated benefits) fit within the last allowance. Negative allowances are retained. They require an additional cost reduction or proven value; they are not rounded up to zero. A negative staff-bill ceiling means even removing the entire station-staff bill cannot reach cash parity while other recorded bills stay fixed.

The ceiling is necessary accounting, not an executable staffing policy. Paying a lower hypothetical invoice does not make capacity free or prove a shift can be cancelled. The exact paid commitment, notice period and funded residual duties must be evidenced. Changing duties, preparation, demand, timing or staff capacity requires a full replay; changing a price alone is not a wage-productivity estimate. A cent-boundary test confirms arithmetic parity while preserving physical work; a separate staff-capacity test rejects a reduction that loses service.

The model's external payees are **receipt accounts**, not complete supplier businesses. Their receipt sum reconciles customer cash; their input costs, liabilities and profits are unknown (`null`). Do not use receipts as supplier profit, infer consolidated resource cost, or add receipts to the same underlying resources. This automotive boundary cannot inherit the separate utility model's customer/provider consolidation formula.

## Remaining perimeter and uncertainty

All times, staffing bills, startup/resource/preparation charges, support assumptions and replacement prices are **synthetic inherited premises**. No BMW/Figure/Liebherr source amount or performance target calibrates them. There are no probability distributions, confidence intervals or annualization assumptions. The comparison shows consequences of declared alternatives and exact conditional break-even thresholds, not the frequency or expected value of any outcome.

The opening robot, buffer installation and raw stock are assumed available; opening and closing assets differ. Acquisition, integration, depreciation, tax, financing, repair, terminal value, model/compute and actual support rights are incomplete. The disclosed residual is unknown, not an assumed zero. Full payer cost and lifecycle ranking remain indeterminate. Executed station and preparation person-time omits unmodeled engineering, transport, inspection and other plant work. It is neither a measured paid shift nor total factory labor. The kit is a declared three-component service unit, not a vehicle, plant shift or cart-movement workflow.

Use the [A1–A6 evidence sequence](../research/deployment_evidence_sequence.md) for current target qualification and economics. Authorization, executed terms, payment, accepted service, supported change, paid-work effect and total payer cost remain separate empirical claims. This result closes none of them.

## Reproduce and inspect

From the repository root, Python 3.10+ and the standard library suffice:

```sh
python3 -m unittest tests.test_workcell_comparison tests.test_automotive_workcell
python3 scripts/export_workcell_comparison.py
python3 scripts/export_workcell_comparison.py --check
python3 scripts/build_workcell_comparison.py
python3 scripts/build_workcell_comparison.py --check
python3 scripts/serve.py
```

The existing Embodiment dashboard view shows the matched comparison alongside the workcell. Select a saved pair, or compare the **last applied** workcell against a saved complete reference. Pending edits cannot change a displayed/exported result. Service mismatches are shown, not silently normalized. A changed applied workcell marks an older comparison stale. Reload accepts a full saved pair, replays its inputs, and ignores its derived bounds/hash. Invalid input and superseded asynchronous responses retain the last valid pair.

Download a pair and replay it with:

```sh
python3 scripts/export_workcell_comparison.py --case SAVED_PAIR.json --output REPLAY.json
```

The [full artifact](results/workcell_comparison.json) carries every pair's complete inputs, executions, obligations, accounts, assets, limits and deterministic hash. Code, Treasury and source-world hashes pin the calculation. The [decision chapter](../research/workcell_cash_decision.md) is generated from that checked artifact; its narrative keeps source evidence separate.
