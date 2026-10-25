# Accepted evidence packages and validation

`data/package_index.json` is the explicit accepted-package registry. Each entry supplies a stable package ID, repository-relative JSON path, `accepted` status and an owner lane. A reviewed package can have any JSON filename within `data/`. A filename ending in `_evidence.json` does not make a draft accepted. The lead adds packages after their audits; discovery does not grant acceptance automatically.

`model/packages.py` is the common loader for the local server, scenario evidence hashes and the validator. It reads the same registry, returns parsed records and hashes of the exact bytes, and rejects missing packages, duplicates, unsafe/outside-data paths, unsupported index versions, invalid JSON, duplicate JSON object keys, nonstandard numeric constants and packages without `evidence[]`. It never silently drops a broken accepted file. Catalog errors return an explicit HTTP 503; scenario requests fail instead of pretending to have a complete evidence snapshot. Results identify the registry hash separately from package hashes.

`scripts/validate_evidence.py` validates claim metadata, explicit quantity objects and cross-package references without modifying source records. It does not validate a claim's truth, prove that a sample represents a market, or calibrate a scenario. Source owners resolve violations; the validator does not fabricate dates, units or populations.

## Claim contracts and aliases

Each `evidence[]` record requires a nonempty unique `evidence_id` and these semantic fields. The first present alias is used; records are not rewritten into a different schema.

| Semantic field | Accepted explicit keys |
|---|---|
| Precise claim | `claim`, `precise_claim` |
| Publisher | `publisher`, `source_publisher` |
| Source URL | `url`, `source_url`, `urls` (nonempty list) |
| Evidence status | `epistemic_status`, `evidence_status`, `status` |
| Source class | `source_class`, `source_type` |
| Source locator | `locator`, `source_locator`, `document_locator` |
| Publication date | `publication_date`, `published_at`, `publication_period` |
| Observation period | `observation_period`, `observation_date`, `observed_at` |
| Retrieval date/time | `retrieved_at`, `retrieval_date`, `retrieved_date` |

Known publication/retrieval values use ISO dates or timestamps; year/month precision is allowed. Observation periods can be descriptive nonempty strings because real samples can span irregular dates or releases. Source URLs must be absolute HTTP(S) URLs. A title is not a claim; geography is not a population; retrieval time is not a publication date. Those are deliberately not aliases.

An unknown required field must be **present with null plus an explicit reason**. Supported reason forms are `<field>_missing_reason`, `<field>_missingness_reason`, or a keyed mapping under `missingness`, `missingness_reasons` or `missing_reasons`. A shared `missingness_reason`, `missing_reason` or `reason` is accepted only if the object has exactly one substantive null field, so one generic explanation cannot silently excuse several unrelated unknowns. Empty strings, omitted keys and unexplained nulls fail.

## Quantity contracts

Any object with a `value` field is inspected as a quantity/measurement marker. Objects in explicit `quantities[]` or `metrics[]` arrays require a numeric value or an explicit-null missingness marker. Finite numeric zero is valid and distinct from unknown. Numeric strings, Boolean values, NaN and infinity fail.

A reported numeric quantity requires:

| Context | Keys | Inheritance allowed? |
|---|---|---|
| Unit | `unit`, `units` | No |
| Denominator | `denominator` | No |
| Population | `population`, `applicable_population` | Nearest explicit enclosing record |
| Period | `period`, `observation_period`, `observation_date` | Nearest explicit enclosing record |
| Measurement status | `measurement_status`, `epistemic_status`, `evidence_status`, `status` | Nearest explicit enclosing record |

A denominator may be a nonempty descriptive string or a finite positive numeric population count, such as 175 benchmark tasks with the population described separately. Known context is not inferred from prose, a formula string, a geography label or the value's sign. Derived calculation records containing `value` have the same dimensional requirements as reported source quantities. References to input metrics do not automatically supply a calculation's output population or denominator.

Explicit-null markers such as `{"value": null, "reason": "No exposure denominator was reported"}` describe an unavailable measurement, not a reported quantity. They require a reason; existing dimensional fields are checked, but absent dimensions are not invented merely to pass a quantitative schema. The validation report counts these markers separately from numeric quantities. A numeric quantity with an explicitly unknown context field can use null and a field-specific reason; it remains a context-limited reported value, not a fully qualified estimate. This distinction is visible in the saved record.

Inheritance reuses an explicit containing-record statement; it does not mutate the child. The validator reports how many context fields used inheritance. Metadata from a sibling, unrelated source, or claim prose is never borrowed. A parent null with a valid field-specific reason remains unknown when inherited.

The validator currently targets explicit measurement records; it does not automatically interpret every numeric scalar in a wide classification/source table as a measurement. Dedicated transformations and checks validate the atlas row arithmetic and reconstructed research datasets. The original wide rows remain source snapshots with their documented column contracts.

## Reference contracts

All arrays whose keys end in `evidence_ids` or `evidence_refs`, plus `source_evidence` and `target_evidence`, resolve against the accepted packages' claim IDs. A reference may be an ID string or an object containing `evidence_id`. Source and target fields remain separate. An empty list can represent no supported reference, with its explanation retained in the parent record; an unresolved ID cannot masquerade as an empty result.

`external_evidence_registry` accepts either an ID-to-package-path mapping or a list of objects containing `evidence_id` and optional `path`. Mapping values and supplied list paths must be nonempty strings and agree with the accepted registry; duplicate registry IDs fail. A draft outside the index does not satisfy a reference even if it exists on disk. Duplicate claim IDs across packages fail.

## Reproduction and limits

Run `python3 scripts/validate_evidence.py` and `python3 -m unittest discover -s tests -v`. Fixtures prove that unreviewed filenames are ignored, newly accepted nonmatching filenames are loaded, missing/malformed fields and unresolved references fail, explicit nulls remain distinct from zero, documented aliases/inheritance work without source mutation, and unsafe registry paths fail closed. API tests verify that the catalog and scenario hashes name the same accepted package set.

Source-derived arithmetic is exported separately from scenario results. The atlas and additional field/benchmark reconstructions use explicit functions and source IDs; source formula strings are never evaluated as code. Validation passing is a necessary integrity check, not evidence of calibrated robotics productivity, rights clearance, or completed research coverage.

Unknown extension fields are allowed so heterogeneous research records can retain their original detail. `owner_lane` is descriptive/optional registry metadata, not an authorization check. This validator does not yet enforce typed market/cell/system/actor joins, unit algebra, percentage ranges, statistical identification or the semantic truth of a status label. Those remain separate source/model reviews. The loader reads and hashes each package once per call, but multiple files are not an atomic filesystem snapshot across concurrent edits. Freeze source writes or use a fixed repository revision for publication/reproduction; the recorded hashes reveal the exact individual files used.
