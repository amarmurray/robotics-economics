"""Observed-data transformations; entirely separate from synthetic scenarios."""
from decimal import Decimal
import json
from .engine import ROOT


def economic_atlas_summary():
    path=ROOT/"data/market_evidence.json"
    if not path.exists():
        return {"status":"missing_evidence","reason":"market_evidence.json not available"}
    d=json.loads(path.read_text())
    dec=lambda x: Decimal(str(x))
    sources={r["matrix_code"]:dec(r["employment_2025_thousands"]) for r in d["source_rows"]}
    row_by_id={r["source_row_id"]:r for r in d["source_rows"]+d.get("sector_source_rows",[])}
    calculations=[]
    for market in d["markets"]:
        expression=market.get("source_row_calculation")
        if expression:
            value=sum((dec(t["coefficient"])*dec(row_by_id[t["source_row_id"]]["employment_2025_thousands"]) for t in expression["terms"]),Decimal(0))
        else:
            value=dec(market["economic_baseline"]["employment"])
        calculations.append({"market_id":market["market_id"],"derived_employment_thousands":float(value),
            "equals_recorded_market_value":value==dec(market["economic_baseline"]["employment"]),
            "source_row_terms":expression.get("terms",[]) if expression else [],"source_row_derivation_available":bool(expression)})
    market_sum=sum((dec(m["derived_employment_thousands"]) for m in calculations),Decimal(0))
    residual_business=sum((sources[k] for k in ("510000","520000","530000","540000","550000")),Decimal(0))
    residual_admin=sources["560000"]-sources["561200"]-sources["561700"]-sources["562000"]
    wage_salary_reconstructed=market_sum+residual_business+residual_admin
    total_reconstructed=wage_salary_reconstructed+sources["TE1100"]
    occupations=sum(r["employment"] for r in d["occupation_screen"])
    denominator=d["accounting"].get("oews_employment_total_jobs")
    if denominator is None:
        denominator=d["accounting"].get("oews_total_employment")
    def result(value,unit,formula,evidence):
        return {"value":float(value) if value is not None else None,"unit":unit,"formula":formula,"evidence_ids":evidence}
    return {"status":"derived_from_saved_official_statistics","scenario_inputs_used":False,
        "geography":"US","period":"2025 industry; May 2025 occupation","market_count":len(d["markets"]),
        "market_source_calculations":calculations,
        "market_employment":result(market_sum,"thousand wage-and-salary jobs","sum(markets[].economic_baseline.employment)",["A-BLS-EP2025"]),
        "other_business_industries":result(residual_business,"thousand wage-and-salary jobs","source rows 51+52+53+54+55",["A-BLS-DETAIL2025"]),
        "other_administrative_support":result(residual_admin,"thousand wage-and-salary jobs","source rows 56−5612−5617−562",["A-BLS-DETAIL2025"]),
        "wage_salary_reconstructed":result(wage_salary_reconstructed,"thousand wage-and-salary jobs","market families + explicit business and admin residuals",["A-BLS-DETAIL2025"]),
        "wage_salary_source_total":result(sources["TE1200"],"thousand wage-and-salary jobs","source row TE1200",["A-BLS-DETAIL2025"]),
        "wage_salary_rounding_difference":result(wage_salary_reconstructed-sources["TE1200"],"thousand jobs","reconstructed − reported; tolerate 0.1 thousand source rounding",["A-BLS-DETAIL2025"]),
        "total_reconstructed":result(total_reconstructed,"thousand jobs","reconstructed wage/salary + self-employed",["A-BLS-DETAIL2025"]),
        "total_source":result(sources["TE1000"],"thousand jobs","source row TE1000",["A-BLS-DETAIL2025"]),
        "selected_occupation_jobs":result(occupations,"OEWS wage-and-salary jobs","sum(eight mutually exclusive major occupation groups); no detailed children added",["A-BLS-OEWS-TABLE"]),
        "oews_total_jobs":result(denominator,"OEWS wage-and-salary jobs","explicit source denominator in accounting record",["A-BLS-OEWS2025"]),
        "selected_occupation_share":result(occupations/denominator if denominator else None,"fraction of OEWS employment","selected occupation jobs / OEWS population; not a physical-work share",["A-BLS-OEWS2025","A-BLS-OEWS-TABLE"]),
        "physical_work_hours":None,"physical_work_hours_missing_reason":"No representative annual-hours and physical-work-share mapping. Employment is not physical hours or robot TAM.",
        "checks":{"all_market_values_recomputed_from_source_rows":all(x["source_row_derivation_available"] and x["equals_recorded_market_value"] for x in calculations),
                  "wage_salary_reconciliation_within_source_rounding":abs(wage_salary_reconstructed-sources["TE1200"])<=Decimal('.1'),
                  "total_reconciliation_within_source_rounding":abs(total_reconstructed-sources["TE1000"])<=Decimal('.1')},
        "limitations":["Market-family boundaries are an analyst crosswalk; arithmetic source-row reproduction does not validate physical-work attribution.","Industry and occupation views overlap and must never be summed.","The occupation subset is neither exhaustive physical labor nor automatable employment."]}
