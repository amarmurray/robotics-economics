# Recorded-field evidence filters

The **Evidence fields** panel filters saved evidence objects by their explicit top-level geography, system/configuration, embodiment, harness, openness layer and license fields. It changes source navigation only; it does not change modeled populations, scenario parameters or empirical values. Counts include claims and supporting objects, not independent sources.

Matching is exact and case-sensitive. A source value such as “UK source; US target” remains one recorded value; selecting “US” does not silently classify that record as a US observation. A system list stored as prose remains one source description. Lists of explicit string values can match any one listed value; selecting different facets requires all of them to match.

The panel makes no nested-field search, cross-record inheritance or inferred geography/system join. **No explicit field** selects objects with no nonempty recorded string for that facet; it means missing classification, not proof that the property is inapplicable. Selecting a recorded value excludes objects without that field. Other evidence search, status and cell controls can narrow the results further. Some valid combinations have no records.

Openness layer and license filters require the explicit `openness-1.0` record schema. A collection name or a word in prose does not grant that classification. The license is an artifact label, not a conclusion about commercial rights, hardware reproduction, model weights, dependencies or deployment feasibility; inspect the full card and source terms. New openness schema versions require an explicit reviewed mapping.

Direct evidence-reference buttons open their requested source even when it lacks the selected fields. This preserves the ability to inspect the source behind a filtered supporting object. **Clear evidence fields** resets these six selectors without changing scenario controls.

This is partial coverage of the requested typed navigation. Dedicated resource-grade classification, normalized geographic ontologies, configuration/version joins and comprehensive entity relationships remain incomplete. Search is still available, but its matches do not acquire a new typed classification.

Validation: `node tests/test_facets.js` runs exact-match, missingness, conjunction, classification and counting assertions. Node is optional for the Python model/server; this browser-helper test uses Node's built-in assertion library. Browser and independent-review scopes are recorded in [the acceptance audit](../ACCEPTANCE_AUDIT.md).
