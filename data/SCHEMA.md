# Campaign evidence contract v0.1

The authoritative economic unit is end market × value-chain stage × operating archetype × geography × observation period. `market_evidence.json` owns market/cell definitions. Other lane files extend this shared universe through stable IDs; they do not create additive opportunity totals.

Evidence files use a versioned JSON object containing named arrays. Each evidence record has `evidence_id`, precise `claim`, `url`, `publisher`, `publication_date`, `observation_period`, `retrieved_at`, `source_class`, `epistemic_status`, `locator`, and `limitations`. A source can support multiple claims; source duplication does not create independent corroboration. Missing fields use null with a reason. Quantities additionally require value, unit, denominator, period, population and measurement status. Dates of publication, observation and retrieval are distinct.

Evidence prefixes: A (economic atlas), BDE (capability/learning), FG (customer/commercial), H (digital ecosystem), HI (digital infrastructure), IJ (physical supply/field). Earlier lane-local prefixes may be retained if globally unique. Source records, benchmark records, analogy records and scenario assumptions are separate objects. In particular, an analogy carries separate source and target evidence, a falsifier, and permitted use; it cannot silently set a calibrated coefficient.

Every quantitative input to `model/engine.py` is either an explicitly labeled scenario assumption or an evidence-linked observation. Synthetic scenarios never populate empirical labor totals. Employment is not physical-work hours; hours are not accepted output; accepted output is not removed payroll. Monetary flows between participants cancel in consolidated value creation.

Operational records live in ignored `work/` and `sync_receipt.json`. Accepted research artifacts and exact content hashes are registered in `artifact_manifest.json`. The manifest does not contain its own hash or containing commit ID.

One writer owns each artifact during a wave. Lead owns report, acceptance audit, schema, roadmap, handoff and manifest. Specialists own their assigned research/evidence pairs. Implementation owns model, dashboard, scripts, tests and reproduction instructions. Independent review writes separate review artifacts and requests corrections from the owning writer.
