"""Single deterministic engine for API, report tables and exports.

All model parameters are synthetic illustrations. Evidence records are never used
as numerical coefficients without an explicit mapping; none is calibrated in this edition.
See model/METHODS.md for dimensions, accounting boundaries and known limitations.
"""
from __future__ import annotations

import copy
import hashlib
import json
import math
from pathlib import Path
from .packages import accepted_package_hashes
from .trajectories import CHANNELS, resolve_paths, parameters_at
from .architectures import resolve as architecture_parameters, compare as compare_architectures, finite_number

ROOT = Path(__file__).resolve().parents[1]
ASSUMPTIONS = ROOT / "model" / "assumptions.json"


def catalog():
    return json.loads(ASSUMPTIONS.read_text())


BOUNDS = {
    "years": (3, 15), "capability": (0, 1), "capability_progress": (0, .10),
    "uptime": (0, 1), "intervention_minutes": (0, 60),
    "labor_avoidability": (0, 1),
    "digital_efficiency": (0, .6), "coordination": (-.4, .6),
    "digital_cost_usd": (0, 20000), "integration_hours": (0, 1000),
    "integration_budget_hours": (0, 50000), "support_budget_hours": (0, 100000),
    "customer_capital_usd": (0, 20000000), "provider_capital_usd": (0, 20000000),
    "price_multiplier": (.25, 3), "learning_transfer": (0, .15),
    "learning_cost_usd": (0, 500000), "demand_expansion": (0, 1),
    "demand_capture": (0, 1), "newco_funding_usd": (0, 10000000),
    "incumbent_response_month": (0, 120), "qualification_delay": (0, 10),
    "expansion_delay": (0, 12), "supply_multiplier": (0, 10),
    "assembly_yield": (.1, 1), "spares_rate": (0, .5),
    "retirement_years": (2, 12), "target_active_stock": (1, 10000), "target_year": (2, 14),
}
CHOICES = {
    "customer_profile": ("incumbent", "constrained", "integrated"),
    "arrangement": ("sale", "lease", "raas"),
    "onboard_configuration": ("standard", "high_memory"),
    "formation_route": ("build", "acquire", "hybrid"),
}
INTEGER_KEYS = {"years", "incumbent_response_month", "qualification_delay", "expansion_delay", "retirement_years", "target_year"}


def parameters(overrides=None, preset="reference"):
    c = catalog()
    if preset not in c["presets"]:
        raise ValueError("Unknown preset")
    p = copy.deepcopy(c["defaults"])
    p.update(c["presets"][preset]["overrides"])
    for k, v in (overrides or {}).items():
        if k in BOUNDS:
            if not finite_number(v):
                raise ValueError(f"{k} must be a finite number, never null")
            lo, hi = BOUNDS[k]
            if not lo <= v <= hi or (k in INTEGER_KEYS and int(v) != v):
                raise ValueError(f"{k} must be in [{lo}, {hi}]" + (" and an integer" if k in INTEGER_KEYS else ""))
        elif k in CHOICES:
            if v not in CHOICES[k]:
                raise ValueError(f"Invalid {k}")
        else:
            raise ValueError(f"Unknown scenario parameter: {k}")
        p[k] = v
    return p


def capability_at(p, t, learned=0):
    return min(1, p["capability"] + p["capability_progress"] * t + learned)


def operation(cell, system, p, cap, digital=True):
    """One full-year supported robot; output is accepted units, not attempts."""
    d = p["digital_efficiency"] if digital else 0
    coord = p["coordination"] if digital else 0
    # Hardware/memory configuration changes power and cost, not competence.
    available_hours = 2000 * p["uptime"] / (1 + p["intervention_minutes"] / 60)
    accepted_units = available_hours * cell["robot_units_per_hour"] * cap * (1 + coord)
    support_hours = 2000 * p["intervention_minutes"] / 60 + system["maintenance_hours_year"]
    memory_extra = 800 if p["onboard_configuration"] == "high_memory" else 0
    electricity = available_hours * (system["power_kw"] + (0.1 if memory_extra else 0)) * .16
    # The board configuration is shared by both robot comparison branches.
    # Its annual resource charge must not depend on additional digital software.
    opex = system["maintenance_usd_year"] + support_hours * 38 + electricity + memory_extra
    if digital:
        opex += p["digital_cost_usd"]
    return {"accepted_units": accepted_units, "available_robot_hours": available_hours,
            "support_hours": support_hours, "robot_operating_cost_usd": opex,
            "human_hours_per_unit": cell["human_hours_per_unit"] * (1 - d),
            "digital_site_cost_usd": 600 if digital else 0}


def matched_economics(cell, system, p, cap, digital=True, robot=True):
    """Fixed output/quality, residual work completed by humans; annual USD."""
    q = cell["annual_units_per_site"]
    op = operation(cell, system, p, cap, digital)
    robot_units = min(q, op["accepted_units"]) if robot else 0
    residual = q - robot_units
    human_cost = residual * op["human_hours_per_unit"] * cell["wage_usd_hour"] + op["digital_site_cost_usd"]
    integration = p["integration_hours"] * 60 if robot else 0
    price = system["price_usd"] * p["price_multiplier"]
    life = p["retirement_years"]
    operating = op["robot_operating_cost_usd"] if robot else 0
    # This catalog cost is per assembly start. Accepted-unit economics bear
    # expected final-test rejects; the stock ledger still applies yield only once.
    manufacturing = system["manufacture_cost_usd"] / p["assembly_yield"] if robot else 0
    # Resource cost excludes between-party price transfers. Separate cash model below.
    resource_cost = human_cost + operating + (manufacturing + integration) / life
    if not robot:
        payment = capital = 0
    elif p["arrangement"] == "sale":
        payment, capital = operating * 1.15, price
    elif p["arrangement"] == "lease":
        payment, capital = operating * 1.15 + price * .24, 0
    else:
        payment, capital = (operating * 1.2 + price * .28), 0
    baseline = q * op["human_hours_per_unit"] * cell["wage_usd_hour"] + op["digital_site_cost_usd"]
    assumed_avoided_cash = (baseline-human_cost)*p["labor_avoidability"]
    annual_cash_gain = assumed_avoided_cash - payment
    customer_cost = baseline-assumed_avoided_cash+payment+(capital+integration)/life
    upfront = capital + integration
    payback = upfront / annual_cash_gain if annual_cash_gain > 0 else None
    provider_lifetime_margin = ((price-manufacturing) if p["arrangement"] in ("sale","lease") else -manufacturing) + life*(payment-operating-(price*.24 if p["arrangement"] == "lease" else 0)) if robot else 0
    financier_lifetime_margin = price*(.24*life-1) if robot and p["arrangement"] == "lease" else 0
    return {"accepted_units": q, "output_unit": cell["output_unit"], "robot_accepted_units": robot_units,
            "retained_human_hours": residual * op["human_hours_per_unit"],
            "released_human_hours": robot_units * op["human_hours_per_unit"],
            "removed_payroll_usd": None, "removed_payroll_missing_reason": "No avoidable staffing schedule is observed; released time is not payroll savings.",
            "assumed_avoided_labor_cash_usd": assumed_avoided_cash,
            "labor_avoidability_assumption": p["labor_avoidability"],
            "resource_cost_boundary": "Labor opportunity cost at matched output; not a payroll or cash statement",
            "resource_cost_usd": resource_cost, "customer_cost_usd": customer_cost,
            "customer_savings_usd": baseline - customer_cost,
            "annual_customer_cash_gain_before_capex_usd": annual_cash_gain,
            "payback_years": payback, "customer_upfront_usd": upfront,
            "provider_recurring_receipts_usd": payment,
            "provider_operating_cost_usd": operating,
            "provider_asset_investment_usd": 0 if p["arrangement"] == "sale" else manufacturing,
            "manufacture_cost_per_accepted_robot_usd": manufacturing,
            "provider_lifetime_margin_usd": provider_lifetime_margin,
            "financier_lifetime_margin_usd": financier_lifetime_margin,
            "system_resource_capital_usd": manufacturing + integration,
            "customer_human_and_digital_cost_usd": human_cost,
            "capital_consumption_usd_year": (manufacturing + integration) / life}


def eligible_sites(cell, system, p, t, cap):
    profile = catalog()["customer_profiles"][p["customer_profile"]]
    e = matched_economics(cell, system, p, cap)
    sites = []
    for i in range(12):
        threshold = cell["capability_threshold"] + (i % 4) * .035
        technical = cap >= threshold and p["uptime"] >= .65
        economic = technical and e["customer_savings_usd"] > 0 and e["payback_years"] is not None and e["payback_years"] <= profile["max_payback_years"] and e["provider_lifetime_margin_usd"] >= 0 and e["financier_lifetime_margin_usd"] >= 0
        ready = economic and t >= profile["ready_delay_years"] + (i % 2) and i < profile["authority_sites"] and e["customer_upfront_usd"] <= profile["site_cash_limit_usd"]
        sites.append({"site_id": f"{cell['cell_id']}:S{i+1:02d}", "threshold": threshold,
                      "technical": technical, "economic": economic, "ready": ready})
    return sites, e


def fleet_model(c, p, resolved_paths=None):
    base_parameters = p
    resolved_paths = resolved_paths or resolve_paths(p, c["base_year"], BOUNDS)
    cells = c["cells"]
    systems = {s["system_id"]: s for s in c["systems"]}
    stocks = {x["cell_id"]: [] for x in cells}
    replacement_backlog = {x["cell_id"]: 0.0 for x in cells}
    exposure = {s: 0.0 for s in systems}
    inv = {"actuator_h": 0.0, "actuator_q": 0.0, "embedded_lpddr_boards": 0.0}
    finished = {s: 0.0 for s in systems}
    production_queue, transit_queue = [], []
    years, cell_rows, component_rows, production_rows = [], [], [], []
    for t in range(int(base_parameters["years"])):
        p = parameters_at(base_parameters, resolved_paths, t)
        year = c["base_year"] + t
        prior_stock = {cid: sum(q for _, q in cohorts) for cid, cohorts in stocks.items()}
        retired = {}
        for cid, cohorts in stocks.items():
            retired[cid] = sum(q for born, q in cohorts if t-born >= p["retirement_years"])
            replacement_backlog[cid] += retired[cid]
            stocks[cid] = [(born, q) for born, q in cohorts if t-born < p["retirement_years"]]
        # Accepted completion occurs one period after a start; scrap is charged once.
        completed = {sid: sum(q * p["assembly_yield"] for due, sid2, q in production_queue if due == t and sid2 == sid) for sid in systems}
        rejected = {sid: sum(q * (1-p["assembly_yield"]) for due, sid2, q in production_queue if due == t and sid2 == sid) for sid in systems}
        production_queue = [x for x in production_queue if x[0] > t]
        prior_finished = finished.copy()
        for sid in systems:
            finished[sid] += completed[sid]
        commissioned = {x["cell_id"]: 0.0 for x in cells}
        for due, cid, amount in transit_queue:
            if due == t:
                stocks[cid].append((t, amount))
                commissioned[cid] += amount
        transit_queue = [x for x in transit_queue if x[0] > t]
        replacements = {cid: min(commissioned[cid], replacement_backlog[cid]) for cid in stocks}
        for cid in stocks:
            replacement_backlog[cid] -= replacements[cid]
        active = {cid: sum(q for _, q in cohorts) for cid, cohorts in stocks.items()}
        active_by_system = {sid: sum(active[x["cell_id"]] for x in cells if x["system_id"] == sid) for sid in systems}
        # Receipts already qualified, net of outside allocations. Expansion is conditional.
        ramp = 0 if t < p["qualification_delay"] else min(1, .5 + .25*(t-p["qualification_delay"]))
        expansion = 1.6 if t >= p["expansion_delay"] else 1
        scale = p["supply_multiplier"] * ramp * expansion
        receipts = {"actuator_h": 1200*scale, "actuator_q": 420*scale, "embedded_lpddr_boards": 75*scale}
        prior_inv = inv.copy()
        for k in inv:
            inv[k] += receipts[k]
        board_coeff = 2 if p["onboard_configuration"] == "high_memory" else 1
        required_service = {"actuator_h": active_by_system["SYN-H"]*24*p["spares_rate"],
                            "actuator_q": active_by_system["SYN-Q"]*12*p["spares_rate"],
                            "embedded_lpddr_boards": sum(active.values())*.02*board_coeff}
        service_fractions = {sid: min(1, inv[s["actuator_pool"]]/required_service[s["actuator_pool"]] if required_service[s["actuator_pool"]] else 1,
                                     inv["embedded_lpddr_boards"]/required_service["embedded_lpddr_boards"] if required_service["embedded_lpddr_boards"] else 1) for sid, s in systems.items()}
        service_used = {k: min(inv[k], required_service[k]) for k in inv}
        for k in inv:
            inv[k] -= service_used[k]
        support_required = sum(active[x["cell_id"]]*operation(x, systems[x["system_id"]], p, 1)["support_hours"] for x in cells)
        support_fraction = min(1, p["support_budget_hours"]/support_required) if support_required else 1
        support_available = max(0, p["support_budget_hours"]-support_required)
        budgets = {"integration_hours": p["integration_budget_hours"], "customer_capital_usd": p["customer_capital_usd"],
                   "provider_capital_usd": p["provider_capital_usd"], "support_hours_reserved": support_available}
        used = {k: 0.0 for k in budgets}
        available_start_capacity = {"SYN-H": 50*scale, "SYN-Q": 25*scale}
        starts = {sid: 0.0 for sid in systems}
        shipped = {sid: 0.0 for sid in systems}
        learning_spend = 0.0
        learned = {sid: 0.0 for sid in systems}
        # This explicit directed same-configuration effect is a scenario hypothesis.
        for sid in systems:
            if p["learning_transfer"] > 0 and exposure[sid] > 0 and budgets["provider_capital_usd"]-used["provider_capital_usd"] >= p["learning_cost_usd"]:
                learned[sid] = p["learning_transfer"] * min(1, exposure[sid]/100000)
                learning_spend += p["learning_cost_usd"]
                used["provider_capital_usd"] += p["learning_cost_usd"]
        ranking = sorted(cells, key=lambda x: matched_economics(x, systems[x["system_id"]], p, capability_at(p, t, learned[x["system_id"]]))["customer_savings_usd"], reverse=True)
        for cell in ranking:
            cid, sid = cell["cell_id"], cell["system_id"]
            s = systems[sid]
            cap = capability_at(p, t, learned[sid])
            sites, econ = eligible_sites(cell, s, p, t, cap)
            eligible = sum(x["ready"] for x in sites)
            in_transit = sum(q for _, c2, q in transit_queue if c2 == cid)
            shortage = max(0, eligible-active[cid]-in_transit)
            customer_cash = econ["customer_upfront_usd"]
            # Manufacturing resources always financed somewhere; sale prepayment offsets provider need.
            provider_cash = 0  # Manufacture was funded at assembly start, never twice.
            requirements = {"integration_hours": p["integration_hours"], "customer_capital_usd": customer_cash,
                            "provider_capital_usd": provider_cash, "support_hours_reserved": operation(cell, s, p, cap)["support_hours"]}
            # Support is reserved for shipments and the newly commissioned fleet; no double use.
            limit = min(shortage, finished[sid], c["customer_profiles"][p["customer_profile"]]["implementation_sites_year"])
            limiting = []
            for k, v in requirements.items():
                if v > 0:
                    allowance = max(0, budgets[k]-used[k])/v
                    if allowance < shortage-1e-9:
                        limiting.append(k)
                    limit = min(limit, allowance)
            if finished[sid] < shortage-1e-9:
                limiting.append("accepted_finished_supply")
            send = max(0, limit)
            finished[sid] -= send
            shipped[sid] += send
            if send:
                transit_queue.append((t+1, cid, send))
            for k, v in requirements.items():
                used[k] += send*v
            # Installed fleets remain stock even if economic/readiness gates subsequently close.
            op = operation(cell, s, p, cap)
            supported = min(service_fractions[sid], support_fraction)
            productive_robot_years = max(0, active[cid]-.5*commissioned[cid]) * supported
            potential = productive_robot_years*op["accepted_units"]
            baseline_demand = 12*cell["annual_units_per_site"]
            # One target robot belongs to one site. Excess throughput cannot serve
            # uninstalled sites without a separately modeled relocation mechanism.
            site_workload = productive_robot_years*cell["annual_units_per_site"]
            baseline_output = min(potential, eligible*cell["annual_units_per_site"], site_workload)
            expansion_output = min(max(0, potential-baseline_output), site_workload*p["demand_expansion"])
            exposure[sid] += productive_robot_years*op["available_robot_hours"]
            unit_h = cell["human_hours_per_unit"]
            physical_pool = baseline_demand*unit_h
            stage_values = {"relevant_work": physical_pool,
                            "capability_compatible": sum(x["technical"] for x in sites)*cell["annual_units_per_site"]*unit_h,
                            "economically_attractive": sum(x["economic"] for x in sites)*cell["annual_units_per_site"]*unit_h,
                            "operationally_ready": eligible*cell["annual_units_per_site"]*unit_h,
                            "installed_capacity": min(eligible*cell["annual_units_per_site"]*unit_h, active[cid]*min(op["accepted_units"],cell["annual_units_per_site"])*unit_h),
                            "realized_baseline_output": baseline_output*unit_h}
            cell_rows.append({"year": year, "period_index": t, "cell_id": cid, "system_id": sid,
                              "prior_active": prior_stock[cid], "retired": retired[cid], "commissioned": commissioned[cid],
                              "replacement_commissioned": replacements[cid],
                              "expansion_commissioned": commissioned[cid]-replacements[cid],
                              "replacement_backlog": replacement_backlog[cid],
                              "active_stock": active[cid], "shipped": send, "support_fraction": supported,
                              "accepted_baseline_units": baseline_output, "accepted_expansion_units": expansion_output,
                              "baseline_equivalent_hours": baseline_output*unit_h,
                              "released_human_hours": baseline_output*op["human_hours_per_unit"],
                              "capability": cap, "exogenous_capability": capability_at(p, t),
                              **{name: p[name] for name in CHANNELS},
                              "learning_increment": learned[sid], "sites": sites,
                              "waterfall": stage_values, "waterfall_unit": "baseline-equivalent human hours/year",
                              "economics": econ, "binding_constraints": limiting or (["capability/economics/readiness"] if not shortage else [])})
        # Pooled future supply is subtracted once from pooled demand, never once per cell.
        current_rows = [x for x in cell_rows if x["year"] == year]
        for sid, s in systems.items():
            forecast_need = sum(max(0, sum(site["economic"] for site in row["sites"])-row["active_stock"]-
                sum(q for _, cid, q in transit_queue if cid == row["cell_id"])) for row in current_rows if row["system_id"] == sid)
            future_finished = sum(q*p["assembly_yield"] for _, ss, q in production_queue if ss == sid)
            start_need = max(0, forecast_need-finished[sid]-future_finished)/p["assembly_yield"]
            count = max(0, min(start_need, available_start_capacity[sid], inv[s["actuator_pool"]]/s["actuator_units"],
                inv["embedded_lpddr_boards"]/board_coeff, max(0,budgets["provider_capital_usd"]-used["provider_capital_usd"])/s["manufacture_cost_usd"]))
            starts[sid] = count
            used["provider_capital_usd"] += count*s["manufacture_cost_usd"]
            inv[s["actuator_pool"]] -= count*s["actuator_units"]
            inv["embedded_lpddr_boards"] -= count*board_coeff
            if count:
                production_queue.append((t+1,sid,count))
        consumed = {"actuator_h": starts["SYN-H"]*24, "actuator_q": starts["SYN-Q"]*12,
                    "embedded_lpddr_boards": sum(starts.values())*board_coeff}
        for k in inv:
            component_rows.append({"year": year, "resource_id": k, "unit": "compatible component units", "opening_inventory": prior_inv[k],
                                   "qualified_net_receipts": receipts[k], "service_required": required_service[k], "service_consumed": service_used[k],
                                   "assembly_consumed": consumed[k], "rework_consumed": 0, "other_allocations": 0, "closing_inventory": inv[k]})
        for sid in systems:
            production_rows.append({"year": year, "system_id": sid, "assembly_starts": starts[sid], "accepted_completions": completed[sid],
                                    "rejected_completions": rejected[sid], "opening_finished": prior_finished[sid], "shipments": shipped[sid],
                                    "closing_finished": finished[sid], "work_in_progress": sum(q for _, ss, q in production_queue if ss == sid),
                                    "commissioning_pipeline": sum(q for _, cid, q in transit_queue if next(x for x in cells if x["cell_id"] == cid)["system_id"] == sid)})
        yr = [x for x in cell_rows if x["year"] == year]
        years.append({"year": year, "active_stock": sum(active.values()), "commissioned": sum(commissioned.values()), "retired": sum(retired.values()),
                      "accepted_baseline_equivalent_hours": sum(x["baseline_equivalent_hours"] for x in yr),
                      "released_human_hours": sum(x["released_human_hours"] for x in yr), "resource_budgets": budgets, "resource_used": used,
                      "support_existing_required": support_required, "support_existing_used": min(support_required, p["support_budget_hours"]),
                      "support_existing_fraction": support_fraction, "learning_validation_cash_usd": learning_spend,
                      "cumulative_exposure_robot_hours": exposure.copy(),
                      "allocation_rule": "Descending illustrative customer savings; stable cell tie break; heuristic, not globally optimal."})
    return {"years": years, "cells": cell_rows, "components": component_rows, "production": production_rows}


def joint_comparisons(c, p, final_cap):
    systems = {s["system_id"]: s for s in c["systems"]}
    rows = []
    for cell in c["cells"]:
        costs = {}
        for r, d in ((0,0),(0,1),(1,0),(1,1)):
            costs[f"C{r}{d}"] = matched_economics(cell, systems[cell["system_id"]], p, final_cap, bool(d), bool(r))["resource_cost_usd"]
        rows.append({"cell_id": cell["cell_id"], "unit": "constant 2026 USD/site/year at matched accepted output", **costs,
                     "joint_saving": costs["C00"]-costs["C11"], "robotics_saving_on_digital_baseline": costs["C01"]-costs["C11"],
                     "cost_interaction": costs["C11"]-costs["C10"]-costs["C01"]+costs["C00"],
                     "interpretation": "Negative cost interaction means complementary savings; positive means overlap or added cost. Scenario contrast, not causal estimate."})
    return rows


def cash_allocation(c, p, cell=None):
    cell = cell or c["cells"][0]
    s = next(x for x in c["systems"] if x["system_id"] == cell["system_id"])
    e = matched_economics(cell, s, p, p["capability"])
    price = s["price_usd"]*p["price_multiplier"]
    manufacturing = s["manufacture_cost_usd"] / p["assembly_yield"]
    sale = p["arrangement"] == "sale"
    integration = p["integration_hours"]*60
    # Lifetime matched-output allocation; third-party lessor only in lease case.
    customer_upfront = -(price if sale else 0)-integration
    provider_upfront = price-manufacturing if sale else -manufacturing
    financier_upfront = 0
    if p["arrangement"] == "lease":
        provider_upfront = price-manufacturing
        financier_upfront = -price
    rows = [{"period":0,"customer_cash_usd":customer_upfront,"provider_cash_usd":provider_upfront,"financier_cash_usd":financier_upfront,
             "consolidated_incremental_cash_usd":-manufacturing-integration}]
    for t in range(1,int(p["retirement_years"])+1):
        financier = price*.24 if p["arrangement"] == "lease" else 0
        customer = e["annual_customer_cash_gain_before_capex_usd"]
        provider = e["provider_recurring_receipts_usd"]-e["provider_operating_cost_usd"]-financier
        rows.append({"period":t,"customer_cash_usd":customer,"provider_cash_usd":provider,"financier_cash_usd":financier,
                     "consolidated_incremental_cash_usd":customer+provider+financier})
    return {"cell_id":cell["cell_id"], "arrangement":p["arrangement"], "cashflows":rows,
            "rights": {"robot_asset_owner": "customer" if sale else "financier" if p["arrangement"] == "lease" else "provider",
                       "workflow_authority":"customer site operator", "model_rights":"separate license; no inferred ownership", "data_reuse":"unknown, no exclusive premium"},
            "scope":"One matched site; avoided baseline cash is an assumption. No tax, financing interest or terminal value. Lease financier receipt is shown separately; internal transfers cancel."}


def newco_model(c, p):
    """ENTRY-FG-01: same robot access, monthly matched accepted service bundles."""
    a = c["newco"]
    n = a["robots"]
    route = p["formation_route"]
    upfront = a["formation_and_site_usd"] + a["upfront_customer_acquisition_usd"]
    upfront += a["acquisition_premium_usd"] * (1 if route == "acquire" else .5 if route == "hybrid" else 0)
    if p["arrangement"] == "sale":
        upfront += n*a["robot_price_usd"]*p["price_multiplier"]
        monthly_asset_payment = n*500  # explicit service-only assumption for bought assets
    elif p["arrangement"] == "lease":
        monthly_asset_payment = n*(a["robot_price_usd"]*.24/12+500)*p["price_multiplier"]
    else:
        monthly_asset_payment = n*a["raas_robot_month_usd"]*p["price_multiplier"]
    response_month = p["incumbent_response_month"]
    rows, receivable = [], 0.0
    cumulative_need, peak_need = upfront, upfront
    for month in range(36):
        service_index = month-a["commissioning_months"]
        ramp = 0 if service_index < 0 else min(1,(service_index+1)*.25)
        capacity = n*a["units_per_robot_month_after_downtime"]*p["uptime"]/a["reference_uptime"]*ramp
        responded = month >= response_month
        if service_index < 0:
            demand = 0
        else:
            demand = a["won_demand_service_months"][min(service_index,5)] * p["demand_capture"]/.35
            demand *= a["response_demand_retention"] if responded else 1
        # Three non-overlapping demand sources: incumbent share, existing unmet demand, new service.
        share_demand = demand*a["share_transfer_fraction"]
        unmet_demand = min(a["unmet_baseline_units_month"],demand*a["unmet_demand_fraction"])
        new_demand = min(a["expansion_ceiling_units_month"],demand*(a["new_demand_fraction"]+p["demand_expansion"]))
        desired = share_demand+unmet_demand+new_demand
        served = min(capacity,desired)
        share_served = served*share_demand/desired if desired else 0
        unmet_served = served*unmet_demand/desired if desired else 0
        new_served = served*new_demand/desired if desired else 0
        price = a["response_price_per_unit_usd"] if responded else a["price_per_unit_usd"]
        revenue = served*price
        receipts, receivable = receivable, revenue
        fee = monthly_asset_payment if service_index >= 0 else 0
        operating = served*a["variable_cost_per_unit_usd"]+a["overhead_month_usd"]+fee
        cashflow = receipts-operating
        cumulative_need -= cashflow
        peak_need = max(peak_need,cumulative_need)
        cash_balance = p["newco_funding_usd"]-cumulative_need
        inc_service = month-response_month-a["commissioning_months"]
        inc_ramp = 0 if inc_service < 0 else min(1,(inc_service+1)*.25)
        incumbent_capacity = n*a["units_per_robot_month_after_downtime"]*p["uptime"]/a["reference_uptime"]*inc_ramp
        rows.append({"month":month+1,"capacity_units":capacity,"demand_units":desired,"served_units":served,
            "share_transferred_units":share_served,"unmet_demand_served_units":unmet_served,"expansion_units":new_served,
            "incumbent_remaining_baseline_units":a["incumbent_baseline_units_month"]-share_served,
            "existing_market_units":a["incumbent_baseline_units_month"],"revenue_usd":revenue,"cash_receipts_usd":receipts,
            "operating_cash_usd":operating,"cashflow_usd":cashflow,"cash_balance_usd":cash_balance,"receivables_usd":receivable,
            "incumbent_same_robot_capacity_units":incumbent_capacity,
            "human_incumbent_variable_cost_for_same_output_usd":served*a["human_cost_per_unit_usd"],
            "same_robot_incumbent_variable_cost_for_same_output_usd":served*a["variable_cost_per_unit_usd"],
            "conditional_on_funding":cash_balance<0})
    first_gap = 0 if p["newco_funding_usd"] < upfront else next((x["month"] for x in rows if x["cash_balance_usd"]<0),None)
    return {"scenario_id":a["scenario_id"],"cell_id":"CELL-M11-floor-cleaning-US-2025",
        "unit":"normalized accepted service bundles/month; distinct from annual fleet cleaning-zone units",
        "status":"synthetic_illustration","assumptions":a,"formation_route":route,"upfront_usd":upfront,
        "funding_committed_assumption_usd":p["newco_funding_usd"],"peak_funding_required_usd":peak_need,
        "funding_gap_usd":max(0,peak_need-p["newco_funding_usd"]),"first_unfunded_month":first_gap,"rows":rows,
        "limitation":"Unfunded rows are a conditional additional-funding path, not financeable operations. All technology terms identical for entrant and incumbent. Equity availability, contract retention, taxes and debt terms unknown. Acquisition premium purchases existing operations and creates no activity. One-month receivables remain uncollected at horizon. Baseline service includes a 10% new-demand hypothesis, separate from optional additional expansion."}


def backcast(c, p):
    target = p["target_active_stock"]
    deadline = int(p["target_year"])
    life = int(p["retirement_years"])
    # Necessary-condition witness: linear additions over eligible retained cohorts.
    first = max(2,int(p["qualification_delay"])+2)
    if first > deadline:
        return {"status":"infeasible_lead_time","target_active_stock":target,"target_year":c["base_year"]+deadline,
                "reason":"No commissioned cohort can arrive by the target after qualification, assembly and commissioning lags.","rows":[]}
    periods = deadline-first+1
    increments = target/periods
    cohorts = []
    rows = []
    for t in range(first,deadline+1):
        retirement = sum(q for born,q in cohorts if t-born >= life)
        cohorts = [(born,q) for born,q in cohorts if t-born < life]
        commissions = increments+retirement
        cohorts.append((t,commissions))
        starts = commissions/p["assembly_yield"]
        active = sum(q for _,q in cohorts)
        # Illustrative fixed 5:1 H/Q mix, explicit; not inferred global market composition.
        h, q = starts*5/6, starts/6
        board = 2 if p["onboard_configuration"] == "high_memory" else 1
        rows.append({"commission_year":c["base_year"]+t,"latest_assembly_start_year":c["base_year"]+t-2,
                     "latest_funded_qualification_year":c["base_year"]+t-2-p["qualification_delay"],
                     "commissioned_required":commissions,"retirements":retirement,"retained_active":active,"assembly_starts_required":starts,
                     "actuator_h_for_starts":h*24,"actuator_q_for_starts":q*12,"embedded_boards_for_starts":starts*board,
                     "actuator_spares_active_year":active*(5/6*24+1/6*12)*p["spares_rate"],
                     "board_spares_active_year":active*.02*board,
                     "integration_hours_required":commissions*p["integration_hours"],
                     "support_hours_required":active*(2000*p["intervention_minutes"]/60+(30*5+25)/6),
                     "manufacturing_cash_required_usd":h*36000+q*24000,
                     "assembly_lines_required_at_25_starts_year":math.ceil(starts/25)})
    return {"status":"necessary_conditions_only","target_active_stock":target,"target_year":c["base_year"]+deadline,
            "mix":"Illustrative 5:1 humanoid/quadruped starts", "rows":rows,
            "reason":"Resource witness and latest start dates, not a forecast. Requires sufficient qualified receipts including spares, orders, retained demand and financed production. Target may exceed the 72-site demonstration pool; no expanded demand is inferred."}


def run_scenario(overrides=None, preset="reference", digital_paths=None, architecture_overrides=None):
    c = catalog()
    p = parameters(overrides,preset)
    resolved = resolve_paths(p, c["base_year"], BOUNDS, digital_paths)
    architecture = architecture_parameters(architecture_overrides)
    architecture_catalog_sha256 = hashlib.sha256((ROOT/"model/architecture_assumptions.json").read_bytes()).hexdigest()
    fleet = fleet_model(c,p,resolved)
    initial = parameters_at(p, resolved, 0)
    annual = []
    for t in range(int(p["years"])):
        current = parameters_at(p, resolved, t)
        cap = capability_at(p, t)
        annual.append({"year": c["base_year"] + t, "period_index": t,
                       "capability": cap, "scope": "exogenous_capability_reference",
                       "effective_digital_parameters": {name: current[name] for name in CHANNELS},
                       "comparisons": joint_comparisons(c, current, cap)})
    evidence=accepted_package_hashes(ROOT)
    engine_sha256 = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    model_source_hashes = {name: hashlib.sha256((ROOT / name).read_bytes()).hexdigest()
                           for name in ("model/engine.py", "model/trajectories.py", "model/architectures.py")}
    fingerprint = hashlib.sha256(json.dumps({"model":c,"parameters":p,
        "resolved_digital_paths":resolved,"model_source_hashes":model_source_hashes,
        "architecture_parameters":architecture,"architecture_catalog_sha256":architecture_catalog_sha256},sort_keys=True).encode()).hexdigest()
    result = {"schema_version":c["schema_version"],"model_version":c["model_version"],"status":"synthetic_illustration",
              "input_commit":c["input_commit"],"scenario_hash":fingerprint,"preset":preset,"parameters":p,
              "engine_sha256":engine_sha256,"model_source_hashes":model_source_hashes,
              "digital_paths":copy.deepcopy(digital_paths),"resolved_digital_paths":resolved,
              "architecture_parameters":architecture,"architecture_catalog_sha256":architecture_catalog_sha256,
              "joint_by_year":annual,
              "reference_scopes":{
                  "joint":"Final-year alias of joint_by_year; exogenous capability, no learned increment",
                  "commercial":"Initial capability and resolved year-zero digital conditions held over life; not a path cash forecast",
                  "newco":"Separate monthly normalized entrant case; no annual digital-path linkage",
                  "backcast":"Fixed-target necessary-condition resource witness; no annual digital-path linkage",
                  "installed_vintage":"current_conditions_all_installed_legacy; no upgrade cost or compatibility diffusion",
                  "learning_exposure":"Supported available robot-hours, not accepted-service hours or validated training yield",
                  "output_gate":"Current acquisition/payback eligibility also caps existing output; not optimal continuation policy",
                  "capital":"Exogenous nonrevolving annual allowances; no path-aware provider treasury"},
              "metadata":{"currency":c["currency"],"geography":c["geography"],"denominator":c["denominator"],"empirical_aggregate_inclusion":False},
              "evidence_snapshot_hashes":evidence["hashes"],"evidence_package_index":evidence["index"],
              "catalog_cells":c["cells"],"assumptions":c["assumptions"],"customer_mechanisms":c["customer_profiles"][p["customer_profile"]],
              "fleet":fleet,"joint":annual[-1]["comparisons"],
              "commercial":cash_allocation(c,initial),"newco":newco_model(c,p),"backcast":backcast(c,p),
              "commercial_by_cell":[cash_allocation(c,initial,cell) for cell in c["cells"]],
              "limitations":["No model coefficient is a calibrated market estimate; all synthetic cells are excluded from empirical labor totals.",
                "Site eligibility uses constructed matched cohorts, not products of independent gate shares.",
                "Annual model uses expected fractional robots and a greedy allocation heuristic; it is not an optimizer or a factory plan.",
                "Source/target analogy evidence never automatically becomes a numerical transfer coefficient.",
                "A synthetic commercial price change reallocates cash; it does not change total physical resource cost.",
                "Detailed ERP transactions, queue distributions, grade substitution, tax, default and information-value optimization remain unmodeled."]}
    result["embodiment_comparisons"] = []
    for joint, cell in zip(result["joint"],c["cells"]):
        result["embodiment_comparisons"].append({"cell_id":cell["cell_id"],"human":joint["C00"],"digital":joint["C01"],"robot":joint["C11"],
            "specialized":joint["C01"]*cell["specialized_cost_factor"]+5000,"mixed":.5*joint["C01"]+.5*joint["C11"],
            "fit":cell["specialized_fit"],"status":"synthetic_illustration","unit":"constant 2026 USD/site/year at matched output",
            "assumptions":"Specialized total cost = digital human resource cost × explicit cell factor + 5000 annual capital allowance. Mixed system splits output and entire process cost 50:50; no duplicated full-output benefits. Neither comparison is a measured feasible configured design."})
    return result


def run_architecture_comparison(cell_id, overrides=None, preset="reference", digital_paths=None,
                                year=None, architecture_overrides=None):
    """One conditional service reference, using the common physical equations."""
    c = catalog()
    cell = next((x for x in c["cells"] if x["cell_id"] == cell_id), None)
    if cell is None:
        raise ValueError("Unknown architecture comparison cell")
    parent = run_scenario(overrides, preset, digital_paths, architecture_overrides)
    if year is None:
        year = parent["joint_by_year"][-1]["year"]
    if isinstance(year, bool) or not isinstance(year, int):
        raise ValueError("Architecture comparison year must be an integer")
    annual = next((r for r in parent["joint_by_year"] if r["year"] == year), None)
    if annual is None:
        raise ValueError("Architecture comparison year is outside the scenario horizon")
    current = parameters_at(parent["parameters"], parent["resolved_digital_paths"], annual["period_index"])
    system = next(x for x in c["systems"] if x["system_id"] == cell["system_id"])
    scope = {"cell_id": cell_id, "year": year}
    identity = hashlib.sha256(json.dumps({"scenario_hash":parent["scenario_hash"],"scope":scope},sort_keys=True).encode()).hexdigest()
    result = compare_architectures(cell, system, current, annual["capability"],
                                   parent["architecture_parameters"], matched_economics, parameters)
    return {"schema_version":"architecture-comparison/0.1", "model_version":c["model_version"],
            "status":"synthetic_conditional_reference", "empirical_aggregate_inclusion":False,
            "scenario_hash":parent["scenario_hash"], "case_hash":identity, "comparison_scope":scope,
            "parameters":parent["parameters"], "preset":preset, "digital_paths":parent["digital_paths"],
            "resolved_digital_paths":parent["resolved_digital_paths"],
            "architecture_parameters":parent["architecture_parameters"],
            "cell":cell, "system":system, "capability":annual["capability"],
            "source_hashes":{**parent["model_source_hashes"],
                             "model/assumptions.json":hashlib.sha256(ASSUMPTIONS.read_bytes()).hexdigest(),
                             "model/architecture_assumptions.json":parent["architecture_catalog_sha256"]},
            "evidence_snapshot_hashes":parent["evidence_snapshot_hashes"],
            "reference_scope":"One supported configured robot/site; selected-year conditions held for its service life, without learned increments. No fleet allocation, financing, adoption timing or company liquidity is simulated.",
            "digital_cost_scope":"The scalar robot digital-service bundle is replaced by itemized costs; digital_cost_usd supplies the reference inference-resource expense, multiplied per synthetic architecture. Model fees are separate transfers.",
            "real_source_boundary":"All vendor target costs, contract rights and qualified compatibility in data/frontier_model_economics.json remain unestablished. These are generic architectures, not named-product rankings.",
            **result}
