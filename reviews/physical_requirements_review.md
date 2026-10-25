# Physical-requirements crosswalk: source and integration audit

25 October 2026. **Sole-lead review under the one-agent limit.** A second extraction library was used as a cross-check, not described as an independent researcher. The crosswalk is accepted as a bounded observed-source packet; empirical robot-addressability and whole-economy physical-hour requirements remain unresolved.

## Source evidence

The original ORS workbook and OEWS ZIP were downloaded through their official BLS page links after shell retrieval returned HTTP 403. The accepted inputs are unchanged bytes, with SHA-256 hashes, URLs, releases and observation windows in `data/sources/physical_requirements/source_manifest.json`. The OEWS workbook remains inside the original ZIP. No earlier cloud data or test is treated as recovered evidence.

The standard-library extraction scans the full selected worksheets: 73,710 ORS data rows and 1,401 OEWS rows. It preserves 25 ORS rows, the three missing requested occupation/estimate pairs, five OEWS rows, workbook headers and all ORS footnote definitions. A separate read using the bundled `openpyxl` library matched every field in all 25 ORS and five OEWS rows, including original row numbers. This checks two parsers against the same original files; it is not independent corroboration of the underlying survey.

The source checks establish three exact detailed occupation-code matches and no exact Team Assemblers employment match. The two 51-2090 employment rows have different `O_GROUP` labels and identical employment, so they remain aliases. The missing Team Assemblers sitting/reaching rows are not imputed, including no subtraction from the published standing share. Footnote 6 yields an unknown exact standard error bounded below 0.5 points; footnote 15 yields unavailable standard error. Published ranges retain their comparison operator and boundary rather than acquiring a point value.

## Execution and integration

The full suite passes **115 Python tests**. Eight new tests cover source re-extraction, package reproduction, exact/missing/duplicate code joins, three absent ORS rows, range and standard-error semantics, compatible sitting/standing denominators, source-hash tampering and genuine numeric zero. Existing scalar regression checks still preserve all 69,315 numerical fields. The accepted-package gate prevents unaccepted crosswalk data from entering the catalog. **32 JavaScript assertions** continue to pass.

Strict validation reports twelve packages, 137 claims, 253 reported quantity objects and 75 explicit-null quantity markers, with no errors or warnings. These checks validate record contracts and supported joins, not survey truth. Physical hours and robot-addressable jobs remain explicit nulls for every occupation.

Browser checks on the local server confirmed the Team Assemblers missing values, janitor standard-error threshold versus unavailable values, matching scope filters and source links for a claim with two primary URLs. Changing the synthetic preset left the observed crosswalk unchanged. No browser console errors were reported. The updated report includes the substantive analysis and a generated table from the same observed summary; its builder rejects stale declared source hashes. This is a desktop interaction check, not a comprehensive accessibility or browser certification.

## Remaining boundaries

ORS and OEWS populations, sample windows and measurement denominators differ even where codes agree. These national occupations are linked qualitatively to four existing market-stage cells, not allocated quantitatively to industries or sites. Requirement marginals are neither joint probabilities nor task-time shares, and fine manipulation includes keyboarding. No incidence × employment, annual-hours conversion, forecast, robot coefficient or preferred embodiment is generated.

The original labor and substitution research questions remain partial. The packet makes a K architecture comparison more disciplined by specifying which service, configuration, support, rights and data would need to match. It does not establish a completed K dossier, a four-architecture economic result or a complete seven-day campaign.
