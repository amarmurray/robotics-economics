# Independent review: joint-comparison calculation trace

Review edition 0.1 · 25 October 2026. Operational input provenance is recorded in ignored `sync_receipt.json`.

**Disposition: pass after correction of the stale-scenario modal race.** The new trace reproduces the existing engine’s matched-output costs, identifiers and horizon. It introduces no independent economic model or empirical calibration. This review covers `model/lineage.py`, `tests/test_lineage.py`, the `/api/joint-trace` path in `scripts/serve.py`, and trace-related code in `dashboard/app.js`. Engine functions were read to check the delegation boundary; the underlying economic model is not independently validated by this trace review.

The reviewer did not edit implementation, shared documents, engine assumptions or saved results. Only this review and temporary probes outside the repository were written. Requested Astra/Ultra runtime configuration remains unverified.

## Finding and verified correction

| ID / severity | Finding | Disposition |
| --- | --- | --- |
| LIN-R01 / medium correctness | Initially, `showCalculation` compared a response only with the scenario captured when the request began. A pending `run()` could replace the global scenario without invalidating that detail request. A user could start recalculation, open a trace from the still-visible old table, and then see the old trace after the new scenario completed. An already rendered trace could likewise remain visible. A controlled asynchronous probe reproduced an open old-hash trace while the live result had new-hash. | **Resolved by lead and independently rechecked.** `activeTraceHash` now tracks the displayed/requested trace; a changed scenario result invalidates pending detail requests and replaces the trace with a scenario-changed message. The response checks both captured and current hashes. Evidence selection clears trace state; the dialog close handler invalidates pending responses. Both pending and already-rendered race paths now pass. |

No unresolved defect was identified within this bounded review. The synthetic assumptions and evidence gaps remain research limitations; a successful trace does not validate their realism.

## Numerical lineage and scope

`joint_trace` resolves a known modeled cell, runs the authoritative scenario, and uses the returned parameters. Its four branches call `engine.matched_economics` with the same cell, system, capability and robot/digital flags used by `engine.joint_comparisons`. The comparison row itself is selected from the returned scenario. The trace does not implement another version of the cost formulas.

Independently compared all six cells under three configurations: the reference case; an adverse three-year case with zero capability/uptime, maximum intervention time, low assembly yield, negative coordination and high-memory configuration; and a fifteen-year case with capability saturation, learning enabled, high commercial price and zero labor-avoidability assumption. Each branch equals the corresponding engine C00/C01/C10/C11 value. Total resource cost equals customer human/site-digital cost plus robot operating cost plus annual capital consumption. Removed payroll remains unknown. An additional hash check covers every saved preset on a representative cell.

Scenario hashes match the engine results, and the trace’s engine hash matches the current `model/engine.py` bytes in these runs. Reference year is `base_year + years − 1`, equal to the final returned fleet year. Capability uses exogenous progression at that horizon with no learned increment. A separate learning-toggle test held exogenous capability at 0.8: the fleet acquired a positive learned increment, reaching 0.15, while the joint comparison and all six trace capabilities remained unchanged. This verifies the stated separation from learned fleet performance, rather than relying solely on a saturated capability example.

The joint table and modal explicitly identify a matched annual site at the final scenario horizon. They do not claim to trace the selected display year, installed fleet, eligibility, or realized deployment. Exact cell/system/parameter data, scenario and engine hashes, and the four source-function excerpts are exposed. Literal constants remain visible in those excerpts. `empirical_coefficient_sources` is empty; the visible source boundary says the numerical assumptions are synthetic and the dossiers do not calibrate them.

The frontend formats returned values. It uses the engine’s comparison fields for the digital-baseline saving and cost interaction. It does not calculate an independent economic result in JavaScript. The displayed resource boundary distinguishes labor opportunity cost from removed payroll and excludes between-party price transfers. The revised modal separates the monetary table from service quantities; visual layout and the full browser journey were smoke-tested by the lead, not independently certified here.

## HTTP and asynchronous behavior

Started an ephemeral loopback server using the actual handler. All six valid cell requests with adverse overrides returned successful synthetic traces. Twelve invalid request bodies—including missing/unknown/nonstring cell identifiers, unknown keys, nonobject overrides, invalid bounds, null/Boolean/nonfinite numeric inputs and invalid preset type—returned HTTP 400. Three malformed body/encoding cases also returned 400. An oversized request returned 400 before body processing; an unknown endpoint returned 404. No external service or repository mutation was involved.

Inspected the HTTP and engine validation path: body size and object shape are checked, scenario parameters use the existing finite-number/bounds/choice checks, and cell membership is validated before tracing. The trace endpoint is read-only. This was request-validation testing, not a generalized server security or load audit.

A controlled Node VM probe executed the actual dashboard functions with deferred fetch responses and a minimal DOM. It independently checked:

- A new scenario completes while the prior trace response is pending: the old response cannot overwrite the scenario-changed message.
- A trace is already rendered when the new scenario completes: the old calculation is invalidated.
- A newer evidence detail supersedes a pending trace: the evidence detail remains.
- The registered close handler invalidates pending trace delivery and does not reopen the dialog.
- A mismatching response hash produces a recalculation message rather than displaying costs.

These are logic probes, not a replacement for native-browser layout, focus or accessibility tests. The lead owns the browser smoke evidence. The two committed lineage tests also pass after the frontend correction.

## Publication boundary

The trace is reviewable explanation of the current synthetic engine. It is not evidence that any quoted cost, service rate, wage, integration burden or digital contribution has been observed in a deployment. It should remain scoped to the stated matched-site comparison; tracing fleet-year or learned-capability results would require a separate, explicitly defined calculation path.

The source and trace checks were conducted against stable files. Atomic hot-reloading of engine/assumption files during a request was not tested. The scenario hash guard addresses mismatched responses but does not establish a general versioned execution service. No additional work is required for this bounded local checkpoint.
