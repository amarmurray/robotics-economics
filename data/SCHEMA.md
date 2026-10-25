# Campaign evidence contract v0.1

The authoritative economic unit is end market × value-chain stage × operating archetype × geography × observation period. `market_evidence.json` owns market/cell definitions. Other lane files extend this shared universe through stable IDs; they do not create additive opportunity totals.

Evidence files use a versioned JSON object containing named arrays. Each evidence record has `evidence_id`, precise `claim`, `url`, `publisher`, `publication_date`, `observation_period`, `retrieved_at`, `source_class`, `epistemic_status`, `locator`, and `limitations`. A source can support multiple claims; source duplication does not create independent corroboration. Missing fields use null with a reason. Quantities additionally require value, unit, denominator, period, population and measurement status. Dates of publication, observation and retrieval are distinct.

Evidence prefixes: A (economic atlas), BDE (capability/learning), FG (customer/commercial), H (digital ecosystem), HI (digital infrastructure), IJ (physical supply/field). Earlier lane-local prefixes may be retained if globally unique. Source records, benchmark records, analogy records and scenario assumptions are separate objects. In particular, an analogy carries separate source and target evidence, a falsifier, and permitted use; it cannot silently set a calibrated coefficient.

Every quantitative input to `model/engine.py` is either an explicitly labeled scenario assumption or an evidence-linked observation. Synthetic scenarios never populate empirical labor totals. Employment is not physical-work hours; hours are not accepted output; accepted output is not removed payroll. Monetary flows between participants cancel in consolidated value creation.

Operational records live in ignored `work/` and `sync_receipt.json`. Accepted research artifacts and exact content hashes are registered in `artifact_manifest.json`. The manifest does not contain its own hash or containing commit ID.

One writer owns each artifact during a wave. Lead owns report, acceptance audit, schema, roadmap, handoff and manifest. Specialists own their assigned research/evidence pairs. Implementation owns model, dashboard, scripts, tests and reproduction instructions. Independent review writes separate review artifacts and requests corrections from the owning writer.

## Accepted-package discovery and executable validation

`package_index.json` explicitly lists accepted source packages. `model/packages.py` is the common loader for dashboard/API, scenario evidence provenance and validation. Filename patterns do not grant acceptance. The stricter contracts, documented aliases, explicit null reasons, quantity-context inheritance and reference checks are in [PACKAGE_VALIDATION.md](../model/PACKAGE_VALIDATION.md). Validation does not determine claim truth or the semantics of every wide source table. Source arithmetic remains separate from synthetic model parameters; `model/research_calculations.py` reconstructs the hospital and archived benchmark figures without executing formula strings.

The accepted `onboard_workload_qualification.json` packet adds OWQ claims, a configuration/workload benchmark card, source calculations, unresolved table conflicts and target-application tests. Published component timings, hardware modes, recipe settings, source-file dates and missing experiment dates remain distinct. Its arithmetic helper checks units, common population/period, positive rates and saved calculation agreement; it preserves unknown deadline-miss rate and sustained throughput. It enters the observed summary only through explicit registry acceptance. Static patch application and Python parsing do not count as workload execution.

The evidence-field panel uses exact top-level recorded values without inferred classifications or cross-record joins. Openness facets require the explicit `openness-1.0` schema. See [filter semantics](../dashboard/EVIDENCE_FILTERS.md). This navigation layer is not a substitute for complete entity/dimension validation.
