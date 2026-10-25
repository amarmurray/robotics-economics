# Independent review of recorded evidence-field filters

Review date: 25 October 2026. **Disposition: pass after correction of the openness type gate.** This review covers `dashboard/facets.js`, its use in `dashboard/app.js`, the new controls in `dashboard/index.html` and `tests/test_facets.js`. It is a browser-independent JavaScript and integration review, not an audit of all dashboard behavior or source truth.

The reviewer changed no implementation, evidence package, model input or result. The requested specialist serving configuration remains independently unverifiable; repository launch provenance remains in ignored `sync_receipt.json`.

## Finding and correction

| ID / severity | Reproduced finding | Correction and recheck |
| --- | --- | --- |
| FAC-R01 / low | The initial openness gate accepted any collection name containing `openness` or any schema beginning `openness-`. An untyped record under `not_openness_objects`, or one declaring `openness-unrelated-not-a-type`, could therefore contribute a layer/license. The current six accepted openness cards were properly typed, so no current-data misclassification was found. | The lead changed the gate to exact `schema_version === 'openness-1.0'`. Collection naming alone no longer suffices. The reviewer independently tested nine collection/schema combinations; only the recognized schema contributes values. All six current cards remain included. The owner's expanded 17-assertion suite passes. |

No unresolved defect was found within the declared exact-field scope. Future openness schemas require a deliberate update; a name resembling the current type is not silently accepted.

## Semantics and independent checks

The six facets read only their declared top-level fields:

| Facet | Read fields and qualification |
| --- | --- |
| Geography | `geography` |
| System/configuration | `system_id`, `system`, `systems` |
| Embodiment | `embodiment` |
| Harness | `harness`, `declared_harness` |
| Artifact layer | `layer`, only on exact `openness-1.0` objects |
| Artifact license label | `license`, only on exact `openness-1.0` objects |

Strings and string members of top-level arrays contribute values. Objects, numbers, nulls and empty/whitespace-only strings do not. Duplicate values within one record count once. Nonempty values preserve original spelling, case and whitespace; a combined geographic description is one complete value and is not decomposed into countries. Structured configuration objects and nested benchmark rows are intentionally outside this filter contract. The system/configuration label is therefore not a claim that every configuration representation is indexed.

Selected facets combine with AND. A record can satisfy a selected system through any of the declared system fields, but a different selected facet must also match. The `missing` selector is distinguished from a literal recorded string `missing` through the `v:` value prefix. Tests also distinguish an actual string beginning `v:` from the selection encoding. No prose, nested-field or cross-record inference supplies missing fields.

The reviewer executed **153 independent assertions** covering exact/case-sensitive comparison, whitespace preservation, duplicate suppression, malformed/nonstring values, absent fields, missing-value sentinel collisions, nested-object exclusion, combined facets, every generated value's record count, input immutability and the dashboard wiring. After FAC-R01 was fixed, the affected schema gate was independently rechecked across nine combinations, the accepted-record population was re-counted, and the complete owner suite was rerun successfully. The underlying dashboard wiring did not change during this correction.

The accepted package index yields **443 saved record objects**, including claims and supporting objects. Observed option coverage was:

| Facet | Distinct values | Objects with no eligible explicit value |
| --- | ---: | ---: |
| Geography | 58 | 191 |
| System/configuration | 40 | 396 |
| Embodiment | 11 | 426 |
| Harness | 6 | 437 |
| Artifact layer | 6 | 437 |
| Artifact license label | 4 | 437 |

These are record-object counts at the reviewed snapshot, not independent source counts, deployment counts or empirical coverage rates. A record with several distinct values appears in several option counts. The displayed scope text correctly says counts include claims and supporting objects, and that search, status and cell scope may narrow them further. Options are generated from the full accepted catalog rather than dynamically recalculated from the current view. Counts do not promise that every matching object is displayed in a view with its own record classes or card limit.

## Dashboard wiring and nonmutation boundary

A controlled Node VM loaded the actual application functions with a minimal DOM and a fetch stub that throws if called. It verified that:

- A selected nonmatching geography excludes a card through the actual `recordMatches`/`cards` path.
- Explicit `showEvidence(id)` still opens that saved source through `cards(..., false)` despite active filters. The source drilldown bypass is intentional and does not change the current filter selection.
- Facet changes call rendering, and the clear button resets all six facets and renders again. Neither operation calls the model API or changes the scenario object.
- The scope count reflects facet matches and the displayed option markup escapes special characters in field values.

The pure facet module likewise leaves the loaded record objects unchanged. The application retains its existing free-text search, source-status search and cell/reference behavior; those older selectors are separate from the new exact-field contract. This review does not recertify their semantics or claim a typed cross-record join system.

The script order loads the facet module before `app.js`; each filter is in a label, and scope feedback uses a status region. Native browser layout, focus, keyboard behavior, real select interaction and rendering are the lead's separate browser-check responsibility. The VM probe is not a substitute for those checks. A closed source dialog can retain its DOM independently of the currently visible filtered card list.

License labels remain artifact-specific text. The UI explicitly says a label alone does not establish commercial or hardware rights. These controls help inspect existing records; they add no rights determination, country classification, field evidence, calibration, economic formula or model result.

## Reviewed file identities

SHA-256 of the final reviewed snapshot:

```text
dashboard/facets.js       122aa592562e01d21e62473fab625182a8ccd10a902ca740a0e01bdbb3b2b775
dashboard/app.js          8f5a2563ba9d5d5033eb6539e5e8991a1e5ffa8c6b18a88eb200b8215a559e8d
dashboard/index.html      6a6426b9116ed3e1b3419ddaab4b467efd7dc6102fe12025d3f4e14cda4179da
tests/test_facets.js      3f5af969d03e4a63a3418248d2df0fe42f9ba66c6114f87d3f6057aeb35c0ef0
data/package_index.json   cd71ad37d2d3721d4fb91350433a0b56ccee9fabff47eaf9919d312fb33794f9
```

This bounded implementation review is complete. Publication, native-browser results and the separate monthly-deployment review are outside this disposition.
