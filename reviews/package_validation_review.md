# Independent review of accepted-package loading and validation

Reviewer: capability/learning lane, independent of the implementation author. Review date: 25 October 2026. Scope: `model/packages.py`, `scripts/validate_evidence.py`, `data/package_index.json`, `tests/test_evidence_validation.py`, `model/PACKAGE_VALIDATION.md`, and the API/engine/export call sites needed to assess shared discovery. This review does not re-audit research claims or certify every model calculation.

**Disposition: pass for the documented structural-validation and accepted-package scope; no remaining blocking finding from this bounded review.** The implementation owner corrected all six findings below, and the reviewer independently rechecked the stable implementation. The reviewer did not edit implementation or reviewed evidence files. This disposition does not claim a full semantic schema, all typed joins, or scientific validity of the source claims.

## Concrete findings and correction requirements

| ID / severity | Reproduced behavior | Required correction and check |
| --- | --- | --- |
| PKG-R01 / medium | A `metrics` field changed from an array to a string or object could pass; the container-type check applied only to `quantities`. | Enforce array type for both explicit measurement containers; reject scalar, object and null containers. |
| PKG-R02 / medium | An external registry list containing a correct entry followed by the same evidence ID with a wrong package path passed. Lookup selected the first matching entry for both checks. | Inspect each declaration, report duplicate external IDs, and validate every supplied locator against its resolved accepted package. |
| PKG-R03 / medium | With the accepted catalog snapshot restricted to capability evidence, `/api/catalog` still returned the 15-market observed atlas. The exporter also wrote the atlas before consulting accepted paths. | Gate observed atlas output by its accepted package, as with the continuation research summary. For export, write an explicit unavailable result rather than leaving an old derived artifact looking current. |
| PKG-R04 / medium | A package path of `.` caused an uncaught `IndexError` at the first path component, rather than a structured failed validation result. | Reject empty normalized path components before indexing them; cover `.` and `./`. |
| PKG-R05 / low | A source URL containing host whitespace and a timestamp with an arbitrary `x` separator passed the initial checks. | Reject whitespace and malformed URL host/port syntax; require the documented calendar-date/timestamp form before date parsing. This remains syntax validation, not a network reachability check. |
| PKG-R06 / low | Duplicate members in a JSON object silently selected the last value, including two different `claim` strings. | Reject duplicate object members during parsing, so the parsed claim does not silently discard a competing value in the hashed source bytes. |

These cases used temporary fixtures or in-process mocks; no accepted source or index was mutated. The catalog exclusion probe changed only the returned test snapshot and made a local loopback request. The initial ten focused evidence/API tests passed, demonstrating why additional negative cases were necessary rather than implying those tests already covered the defects.

**Closure:** PKG-R01 through PKG-R06 are resolved. Both measurement containers now require arrays; every external-registry locator is checked and duplicate IDs are rejected; atlas and continuation summaries are gated in the catalog and exporter; empty normalized paths produce structured failures; URL/timestamp syntax checks reject the reproduced malformed cases; and the JSON parser rejects duplicate object members. Source values and quantitative research conclusions were not changed to obtain this pass.

## What the common loader establishes

The index explicitly identifies accepted JSON packages. Filename globbing does not grant acceptance: a malformed unreviewed `_evidence.json` file is ignored, while an explicitly accepted file with another JSON filename is loaded. The loader returns parsed package records and SHA-256 hashes of their exact bytes, plus a separate hash of the registry. Missing files, invalid JSON, unsupported index versions, missing `evidence[]`, nonaccepted status, duplicate package IDs and duplicate package paths fail rather than silently dropping a package.

The API's evidence catalog, engine evidence-provenance hashes and validator import the same loader. The API and scenario tests compare the returned accepted path sets and registry identity. Path checks constrain accepted packages to JSON files inside `data/`, reject absolute paths and `..`, and resolve symlinks before enforcing that boundary. Duplicate resolved paths are also rejected; aliases such as `data/./a.json` cannot load the same package twice.

This is a package-discovery and provenance boundary. It is not an access-control system for every repository file. Research-document listing and permitted static file serving are separate features. Likewise, sharing a loader does not create a transactional filesystem snapshot across concurrent edits: comparisons concern a stable set of reviewed files. A source change produces a different hash, but the loader does not freeze the workspace.

## Claim metadata, nulls and quantity scope

The validator requires a nonempty evidence ID and explicit claim, publisher, HTTP(S) URL, evidence status, source class, locator, publication date, observation period and retrieval date, using the documented aliases. It does not substitute a title for a claim, geography for a population, or retrieval time for publication. Date precision can be a year or month; observation periods can be descriptive strings. Unknown values must be represented explicitly as null with a reason, rather than an omitted field or empty string.

The missingness policy is appropriately narrow: field-specific reason keys or keyed mappings can describe multiple unknowns, while a shared reason applies only when exactly one substantive field is null. An explicit child null is not replaced by known parent metadata. Numeric zero remains a measured value and does not become an unknown. Null quantity markers with a reason are counted separately from reported numeric quantities; omitted dimensions are not fabricated for an unavailable measurement.

Every object containing `value` is checked as an explicit quantity marker. Numeric quantities require a finite numeric value, unit and denominator, plus population, period and measurement status. A numeric denominator must be positive; a descriptive denominator must be nonempty. Boolean values and numeric strings do not qualify as numeric measurements. Unit and denominator cannot be inherited; population, period and status may use the nearest containing record's explicit field. This behavior is documented and tested without changing saved source data.

The intended output contract also applies to derived records with `value`. A formula string and references to input metrics cannot substitute for an output denominator, population and period. The field-support calculation records were supplied with those explicit contexts by their source owner; the validator did not infer costs or silently repair their evidence.

This remains structural validation. A nonempty unit string is not proof of dimensional compatibility; a descriptive denominator can be wrong; a population can be unrepresentative. Percentages are not automatically constrained to their scientific domain, and count units are not universally distinguished from rates by this validator. Separate source-derived calculation helpers have their own guards and tests. Wide source tables and other numeric scalars without explicit measurement objects are outside this automatic quantity contract.

## Reference integrity and deliberately limited schema coverage

Evidence-reference fields ending in `evidence_ids` or `evidence_refs`, plus `source_evidence`, `target_evidence` and the external evidence registry, resolve against the accepted packages' claim IDs. Draft files outside the index do not satisfy a missing reference. Duplicate evidence IDs across packages fail. Directed source/target reference fields stay distinct rather than being replaced by an unrelated single-source fallback.

The external registry supports ID-to-path mappings and list entries with IDs and optional paths. Any supplied locator must agree with the accepted package containing that evidence record. Resolving the identifier does not prove the source supports the assertion or that two records represent independent underlying observations.

Additional extension fields are allowed; this is not a closed schema for every research package. The validator does not establish all typed joins among markets, cells, actors, systems, benchmarks or scenarios. It does not establish ownership of a data right, commercial deployment stage, statistical identification, causal transfer, or source truth. Those remain source-owner and independent-review responsibilities. Optional/descriptive index metadata should not be represented as a validated domain ontology.

## Final verification and review limits

The current accepted-package run reports ten packages, 126 evidence records, 192 explicit numeric quantities, 46 null measurement markers and 18 inherited context fields, with no errors. These totals count structured records, not independent verified sources or calibrated parameters.

The reviewer ran `python -m unittest tests.test_evidence_validation tests.test_api -v`: **14 tests passed**. These cover positive accepted-package discovery, deliberate draft exclusion, required claim metadata, null versus zero, aliases and context inheritance without mutation, unresolved references, malformed quantity containers, external-registry conflicts, duplicate JSON keys, unsafe paths, malformed dates/URLs, local API behavior, and catalog/scenario package-set agreement. The API exclusion test supplies an accepted subset and asserts that neither unaccepted observed transformation is invoked.

The reviewer also reran ten separate temporary negative probes: string/object `metrics`, a duplicate external ID with a conflicting second locator, a null mapping locator, whitespace in the source host, an invalid timestamp separator, `.` and `./` package paths, duplicate resolved paths, and a symlink pointing outside `data/`. All ten returned structured failed validation. The duplicate-JSON-member regression passed in the focused suite. Exporter gating and explicit unavailable-output writes were checked in the implementation; the reviewer did not independently regenerate scenario exports. The implementation owner separately reported the full 31-test suite passing and regenerated exports; that report is corroboration, not an additional independent execution claim.

The accepted-package validator itself was executed independently and produced the totals above with zero errors. Scope documentation now explicitly preserves unknown extension fields, optional/descriptive `owner_lane`, limits on typed joins and unit semantics, and the absence of an atomic multi-file snapshot. The requested Astra Ultra serving configuration cannot be independently verified from the reviewer runtime; conclusions here rest on code inspection and executable checks.

This review stops at the stable implementation handoff. It excludes the separately reviewed source claims and research-calculation semantics, full engine accounting, security certification of the HTTP server, exhaustive malformed-input fuzzing, and the separate dashboard presentation fix. Later changes to these reviewed contracts require their own targeted verification.
