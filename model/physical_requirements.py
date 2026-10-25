"""Observed ORS/OEWS crosswalk; never a robot-addressability calculation."""
import copy
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = "data/physical_requirements_crosswalk.json"
ROWS = "data/sources/physical_requirements/selected_rows.json"
ORS_URL = "https://www.bls.gov/web/ors/ors-complete-dataset.xlsx"
OEWS_URL = "https://www.bls.gov/oes/special-requests/oesm25nat.zip"
ORS_PERIOD = "2025 preliminary reference year; samples August 2023 through July 2025"
OEWS_PERIOD = "May 2025; six panels November 2022 through May 2025"
METRICS = {
    "01003": ("standing_mean", "Mean workday standing or walking", "percent of workday (mean)"),
    "00997": ("sitting_mean", "Mean workday sitting or lying down", "percent of workday (mean)"),
    "00771": ("gross_manipulation", "Gross manipulation required", "percent of workers"),
    "01262": ("fine_manipulation", "Fine manipulation required", "percent of workers"),
    "00830": ("reaching_at_below_shoulder", "Reaching at or below shoulder required", "percent of workers"),
    "00831": ("reaching_overhead", "Overhead reaching required", "percent of workers"),
    "01216": ("low_postures", "Low postures required", "percent of workers"),
}
TARGETS = {
    "372011": ("Janitors and cleaners, except maids and housekeeping cleaners", "CELL-M11-floor-cleaning-US-2025"),
    "472061": ("Construction laborers", "CELL-M04-construction-install-US-2025"),
    "512092": ("Team assemblers", "CELL-M05-auto-assembly-US-2025"),
    "537062": ("Laborers and freight, stock, and material movers, hand", "CELL-M08-3pl-tote-US-2025"),
}


def observation(text, unit, denominator, population, period, footnotes=(), standard_error=False):
    """Preserve ranges and SE thresholds as bounds, not invented point values."""
    result = {"value": None, "unit": unit, "denominator": denominator,
              "population": population, "period": period,
              "epistemic_status": "official_preliminary_estimate", "source_text": text}
    if text is None:
        result.update(value_missing_reason="No matching row is published in the source workbook; absence does not identify zero or a reason for nonpublication.", measurement_status="not_published")
    elif text == "-":
        if standard_error and ("5" in footnotes or "6" in footnotes):
            bound = .05 if "5" in footnotes else .5
            result.update(comparison="<", bound=bound, measurement_status="published_threshold",
                          value_missing_reason=f"Exact standard error is not published; footnote specifies less than {bound}.")
        else:
            result.update(measurement_status="not_available", value_missing_reason="Standard error unavailable per footnote 15." if standard_error and "15" in footnotes else "Source dash: estimate not publishable or no workers with the requirement; no point value inferred.")
    elif str(text).startswith(("<", ">")):
        result.update(comparison=text[0], bound=float(text[1:]), measurement_status="published_range",
                      value_missing_reason="Only the published range is known; its boundary is not the underlying point estimate.")
    else:
        result.update(value=float(text), comparison="=", measurement_status="published_point")
    return result


def _claim(eid, claim, url, publication, period, locator, limitations):
    return {"evidence_id": eid, "claim": claim, ("urls" if isinstance(url, list) else "url"): url,
            "publisher": "U.S. Bureau of Labor Statistics", "publication_date": publication,
            "observation_period": period, "retrieved_at": "2026-10-25",
            "source_class": "official_statistics_and_methods", "epistemic_status": "bounded_source_observation",
            "locator": locator, "limitations": limitations, "geography": "US"}


def build_package(root=ROOT):
    raw = json.loads((root/ROWS).read_text())
    ors = {}
    for r in raw["ors_rows"]:
        key = (r["cells"]["2018 SOC CODE"], r["cells"]["ESTIMATE CODE"])
        if key in ors:
            raise ValueError("Duplicate ORS key")
        ors[key] = r
    occupations, requirements = [], []
    for soc, (name, cell_id) in TARGETS.items():
        display_code = soc[:2]+"-"+soc[2:]
        matches = [r for r in raw["oews_rows"] if r["cells"]["OCC_CODE"] == display_code and r["cells"]["O_GROUP"] == "detailed"]
        if len(matches) > 1:
            raise ValueError("Ambiguous OEWS detailed occupation match")
        matched = matches[0] if matches else None
        employment = {"value": matched["cells"]["TOT_EMP"] if matched else None,
                      "unit": "wage-and-salary jobs", "denominator": "national cross-industry occupation employment",
                      "population": "OEWS nonfarm establishments, ownership 1235; full- and part-time jobs",
                      "period": OEWS_PERIOD, "epistemic_status": "official_employment_estimate"}
        if not matched:
            employment["value_missing_reason"] = "No exact 51-2092 detailed employment row. The workbook's broader 51-2090 category is not Team Assemblers alone."
        occupations.append({"crosswalk_id": "PRC-"+soc, "soc_2018": display_code, "occupation": name,
                            "cell_ids": [cell_id], "employment": employment,
                            "oews_source_row": matched["source_row"] if matched else None,
                            "join_status": "exact_code_population_mismatch" if matched else "no_exact_employment_code",
                            "population_equivalent": False,
                            "requirement_ids": [soc+"-"+code for code in METRICS],
                            "physical_work_hours": None,
                            "physical_work_hours_missing_reason": "ORS marginal requirement incidence/duration and OEWS jobs do not supply a matched annual physical-work-hour denominator.",
                            "robot_addressable_jobs": None,
                            "robot_addressable_jobs_missing_reason": "No configured robot capability, workflow coverage, accepted output or economic substitution estimate is inferred.",
                            "evidence_ids": ["PRC-001", "PRC-002", "PRC-003", "PRC-004", "PRC-005"]})
        population = f"ORS civilian workers in 2018 SOC {display_code}; private industry plus state/local government"
        for code, (metric, label, unit) in METRICS.items():
            source = ors.get((soc, code))
            row = source["cells"] if source else {}
            fn = {key: str(row.get(column) or "").split(",") if row.get(column) else [] for key, column in
                  [("estimate", "DATA FOOTNOTE"), ("standard_error", "STANDARD ERROR FOOTNOTE"), ("series", "SERIES FOOTNOTE")]}
            denominator = "each sampled job's workday, summarized as a mean" if "workday" in unit else "workers in the specified ORS occupation, not work hours"
            requirements.append({"requirement_id": soc+"-"+code, "soc_2018": display_code,
                "occupation": name, "cell_ids": [cell_id], "metric": metric, "label": label,
                "estimate_code": code, "series_id": row.get("SERIES ID"),
                "source_row": source["source_row"] if source else None,
                "source_sheet": raw["ors_sheet"], "source_text": row.get("ESTIMATE TEXT"),
                "estimate": observation(row.get("ESTIMATE"), unit, denominator, population, ORS_PERIOD, fn["estimate"]),
                "standard_error": observation(row.get("STANDARD ERROR"), "percentage points", "standard error of the indicated ORS estimate", population, ORS_PERIOD, fn["standard_error"], True),
                "footnote_codes": fn,
                "footnotes": {kind: [raw["ors_footnotes"][f] for f in codes] for kind, codes in fn.items()},
                "evidence_ids": ["PRC-002" if metric in ("standing_mean", "sitting_mean") else "PRC-003", "PRC-006"]})
    evidence = [
        _claim("PRC-001", "The 2025 ORS source is preliminary third-wave evidence from two samples collected August 2023 through July 2025; it is not a time series of robot capability or physical-work change.", ORS_URL, "2026-01-16", ORS_PERIOD, "File information!A1:B1; Footnote codes P; ORS 2025 dataset", "Preliminary aggregate, not a single-date census. No comparisons across ORS waves are treated as a trend."),
        _claim("PRC-002", "Published mean workday standing shares are 97.7% for janitors, 89.2% for construction laborers, 95.6% for team assemblers and 93.7% for hand material movers. Team assemblers' mean sitting row is absent from this workbook.", ORS_URL, "2026-01-16", ORS_PERIOD, "ORS 2025 dataset, estimate codes 01003 and 00997; exact rows in selected_rows.json", "Standing includes walking; sitting includes lying down. These duration measures are not the share of work a robot can perform. The missing sitting estimate is not filled as 100 minus standing."),
        _claim("PRC-003", "The four occupations have distinct published manipulation, reaching and low-posture requirements; the selected team-assembler reaching rows are absent. Incidence measures describe workers with a requirement, not the fraction of their hours spent on it.", ORS_URL, "2026-01-16", ORS_PERIOD, "ORS 2025 dataset, estimate codes 00771, 01262, 00830, 00831 and 01216; exact source rows retained", "Requirements can overlap in a worker and time interval. No marginal percentages are added or multiplied into joint prevalence or employment."),
        _claim("PRC-004", "OEWS detailed codes match janitors, construction laborers and hand material movers, with 2,209,760, 1,096,780 and 2,950,280 jobs respectively. No exact Team Assemblers 51-2092 row exists. The broader 51-2090 category appears as both broad and detailed rows with the same 1,405,030 jobs.", OEWS_URL, "2026-05-15", OEWS_PERIOD, "national_M2025_dl rows 720, 988, 1163, 1164 and 1389; AREA=99, NAICS=000000, OWN_CODE=1235", "The two 51-2090 rows are classification aliases, not additive employment. Their total is not assigned to Team Assemblers. Matching codes still do not align survey populations."),
        _claim("PRC-005", "ORS civilian workers exclude federal, military, agricultural, private-household and self-employed workers. OEWS covers nonfarm wage-and-salary jobs including federal executive/Postal employment and selected agricultural industries. The same SOC code does not by itself make these populations interchangeable.", ["https://www.bls.gov/ors/factsheet/orsprofiles.htm", "https://www.bls.gov/oes/current/oes_tec.htm"], None, "2025 reference definitions", "ORS profiles: General terms, civilian workers; OEWS technical note: Scope, industry coding and concepts", "No employment times ORS incidence or workday percentage calculation is permitted without a reconciled population and duration design."),
        _claim("PRC-006", "ORS source dashes carry different meanings: footnote 6 means standard error below 0.5, while footnote 15 means unavailable. Estimate ranges such as >99.5 and >95 are not point values; the two range types have different construction rules.", [ORS_URL, "https://www.bls.gov/ors/factsheet/range-estimates.htm"], "2026-01-16", ORS_PERIOD, "Footnote codes!A2:B35; range-estimates methodology; selected row footnote columns", "The >99.5/<0.5 endpoint ranges do not incorporate a confidence interval; other published ranges use the BLS one-sided interval method. Bounds are retained, not replaced with endpoints or midpoint assumptions."),
        _claim("PRC-007", "ORS gross and fine manipulation can occur concurrently; fine manipulation in the third wave includes keyboarding. These requirements therefore cannot serve as a clean measure of economically substitutable physical labor.", "https://www.bls.gov/ors/factsheet/gross-and-fine-manipulation.htm", None, "2025 third-wave definitions", "Definitions and concurrent-requirement examples", "Requires task/workflow, tooling, quality, supervision and useful-output evidence before a robot comparison. No standalone dexterity score or annual-hour conversion follows."),
    ]
    for claim in evidence:
        if claim["publication_date"] is None:
            claim["publication_date_missing_reason"] = "Live methods page does not expose a verified publication date; definitions are explicitly labeled for the 2025 data."
    return {"schema_version": "physical-requirements-crosswalk/1.0", "status": "observed_subset_with_explicit_join_limits",
            "scope": "Four selected occupations linked qualitatively to existing market-stage cells; not a national physical-labor or robot-addressability estimate.",
            "source_hashes": {**{s["path"]: s["sha256"] for s in raw["sources"]}, ROWS: hashlib.sha256((root/ROWS).read_bytes()).hexdigest()},
            "source_rows": ROWS, "evidence": evidence, "occupational_crosswalk": occupations,
            "physical_requirements": requirements,
            "join_policy": "Exact detailed code match only; preserve unmatched codes, duplicate classification aliases and survey-population differences. No employment multiplication.",
            "scenario_coefficients_supplied": False}


def physical_requirements_summary(root=ROOT):
    package = json.loads((root/PACKAGE).read_text())
    rows = []
    for occupation in package["occupational_crosswalk"]:
        requirements = {r["metric"]: r for r in package["physical_requirements"] if r["soc_2018"] == occupation["soc_2018"]}
        rows.append({**copy.deepcopy(occupation), "requirements": requirements})
    return {"schema_version": "physical-requirements-summary/1.0", "status": package["status"],
            "scenario_inputs_used": False, "occupations": rows,
            "published_ors_rows": sum(r["source_row"] is not None for r in package["physical_requirements"]),
            "unpublished_selected_rows": sum(r["source_row"] is None for r in package["physical_requirements"]),
            "exact_code_matches": sum(r["join_status"] == "exact_code_population_mismatch" for r in rows),
            "source_hashes": {**package["source_hashes"], PACKAGE: hashlib.sha256((root/PACKAGE).read_bytes()).hexdigest(),
                              "model/physical_requirements.py": hashlib.sha256(Path(__file__).read_bytes()).hexdigest()},
            "boundary": package["scope"], "join_policy": package["join_policy"]}
