"""Conditional intelligence-layer resources and transfers around shared economics.

All inputs are synthetic. Integer cents are used for scheduled charges/transfers;
annual equivalents divide lifetime amounts without introducing a discount rate.
"""
import copy
from decimal import Decimal, ROUND_HALF_UP
from fractions import Fraction
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT/"model/architecture_assumptions.json"
ROLES = ("customer", "operator", "oem", "model_supplier", "integrator")
GATES = ("assume_compatible", "assume_rights_available", "assume_service_quality")
MAX_CENTS = 2**53-1


def catalog():
    return json.loads(CATALOG.read_text())


def finite_number(value):
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        return False
    try:
        return math.isfinite(value)
    except OverflowError:
        return False


def cents(value, *, derived=False):
    if not finite_number(value) or value < 0:
        raise ValueError("Monetary inputs must be finite nonnegative numbers")
    amount = Decimal(str(value))*100
    if amount > MAX_CENTS:
        raise ValueError("Monetary amount exceeds exact JSON cent range")
    rounded = amount.quantize(Decimal("1"), rounding=ROUND_HALF_UP)
    if not derived and amount != rounded:
        raise ValueError("Monetary inputs must have cent precision")
    if rounded > MAX_CENTS:
        raise ValueError("Monetary amount exceeds exact JSON cent range")
    return int(rounded)


def resolve(overrides=None):
    """Resolve all inputs before calculation; export the complete effective state."""
    data = catalog()
    p = copy.deepcopy(data["defaults"])
    if overrides is not None:
        if not isinstance(overrides, dict) or set(overrides)-{"common", "profiles"}:
            raise ValueError("architecture_overrides supports common and profiles only")
        common = overrides.get("common", {})
        profiles = overrides.get("profiles", {})
        if not isinstance(common, dict) or set(common)-set(p["common"]):
            raise ValueError("Unknown architecture common parameter")
        if not isinstance(profiles, dict) or set(profiles)-set(p["profiles"]):
            raise ValueError("Unknown architecture profile")
        p["common"].update(common)
        for name, changes in profiles.items():
            if not isinstance(changes, dict) or set(changes)-set(p["profiles"][name]):
                raise ValueError("Unknown parameter in architecture "+name)
            p["profiles"][name].update(copy.deepcopy(changes))
    for group in [p["common"], *p["profiles"].values()]:
        for key, value in group.items():
            if key in GATES:
                if type(value) is not bool:
                    raise ValueError(key+" must be an explicit boolean assumption")
            elif key == "role_entities":
                if not isinstance(value, dict) or set(value) != set(ROLES) or any(not isinstance(v, str) or not v.strip() or len(v)>64 for v in value.values()):
                    raise ValueError("role_entities must map every logical role to a named entity")
            elif key == "customer_path":
                if value not in ("incumbent", "newco"):
                    raise ValueError("Unknown customer_path")
            else:
                if not finite_number(value):
                    raise ValueError(key+" must be finite, never null or boolean")
                if value < 0 and key != "support_minutes_delta":
                    raise ValueError(key+" must be nonnegative")
                if key == "support_minutes_delta" and not -60 <= value <= 60:
                    raise ValueError("support_minutes_delta must be in [-60, 60]")
                if "usd" in key:
                    cents(value)
                group[key] = float(value)
    return p


def _annual(value, life):
    return float(Fraction(value, 100*life))


def _fee_interval(payer, receiver, amount, lifetime_net, life, common):
    if payer == receiver:
        return {"status": "internal_transfer_eliminated", "payer": payer, "receiver": receiver,
                "lower_usd_year": None, "upper_usd_year": None,
                "reason": "These roles share one entity; there is no external fee to solve for."}
    payer_before = lifetime_net[payer]+life*amount
    receiver_before = lifetime_net[receiver]-life*amount
    low = max(0, math.ceil(Fraction(-receiver_before, life)+cents(common["receiver_surplus_usd_year"])))
    high = math.floor(Fraction(payer_before, life)-cents(common["payer_surplus_usd_year"]))
    feasible = high >= low
    other_ok = all(value >= 0 for entity, value in lifetime_net.items() if entity not in (payer, receiver))
    return {"status": "feasible_interval" if feasible else "no_nonnegative_fee_interval",
            "payer": payer, "receiver": receiver,
            "lower_usd_year": low/100, "upper_usd_year": high/100,
            "lower_cents_year": low, "upper_cents_year": high,
            "selected_usd_year": amount/100, "selected_within_interval": feasible and low <= amount <= high,
            "other_entities_nonnegative": other_ok, "all_party_interval_feasible": feasible and other_ok,
            "receiver_without_fee_usd_year": _annual(receiver_before, life),
            "payer_without_fee_usd_year": _annual(payer_before, life),
            "scope": "Other payments fixed; undiscounted annual equivalent. Integer-cent fee bounds include allocated upfront costs. Other counterparties' viability is shown separately."}


def _case(name, label, cell, system, base_p, cap, common, a, evaluate, validate_parameters):
    failed = [gate for gate in GATES if not a[gate]]
    if failed:
        return {"architecture_id": name, "label": label, "status": "not_admitted_under_assumptions",
                "failed_assumptions": failed, "resource_cost_usd_year": None,
                "resource_cost_missing_reason": "Configuration, rights or quality premise is not assumed satisfied; no ranking is produced.",
                "empirical_qualification": "not_established", "assumptions": copy.deepcopy(a)}
    # The opaque scalar service bundle is replaced, never added a second time.
    effective = {**base_p, "digital_cost_usd": 0,
                 "integration_hours": base_p["integration_hours"]*a["integration_multiplier"],
                 "intervention_minutes": base_p["intervention_minutes"]+a["support_minutes_delta"]}
    effective = validate_parameters(effective)
    e = evaluate(cell, system, effective, cap, digital=True, robot=True)
    human = evaluate(cell, system, base_p, cap, digital=True, robot=False)
    life = int(base_p["retirement_years"])
    mapping = a["role_entities"]
    entities = sorted(set(mapping.values()))
    expense, transfers = [], []

    def cost(period, role, category, value, resource=True):
        expense.append({"period": period, "role": role, "entity": mapping[role], "category": category,
                        "amount_cents": cents(value, derived=True), "resource_cost": resource})

    def transfer(period, payer, receiver, category, value):
        transfers.append({"period": period, "payer_role": payer, "receiver_role": receiver,
                          "payer_entity": mapping[payer], "receiver_entity": mapping[receiver],
                          "category": category, "amount_cents": cents(value, derived=True),
                          "internal_eliminated": mapping[payer] == mapping[receiver]})

    engineering = common["engineering_usd_hour"]
    manufacturing = e["manufacture_cost_per_accepted_robot_usd"]
    integration = e["system_resource_capital_usd"]-manufacturing
    validation = a["validation_engineering_hours"]*engineering+a["qualification_resources_usd"]
    integration_payment = (integration+validation)*(1+common["integration_markup"])
    baseline = cents(human["resource_cost_usd"], derived=True)
    human_residual = cents(e["customer_human_and_digital_cost_usd"], derived=True)
    # The same disjoint labor decomposition as the common engine, with cents
    # rounded once: remaining service work versus paid but unreleased payroll.
    released_value = max(0, baseline-human_residual)
    unavoidable = cents(released_value/100*(1-base_p["labor_avoidability"]), derived=True)
    setup = common["incumbent_setup_usd"] if common["customer_path"] == "incumbent" else common["newco_setup_usd"]
    cost(0, "oem", "accepted_robot_manufacturing", manufacturing)
    cost(0, "integrator", "physical_process_integration", integration)
    cost(0, "integrator", "qualification_and_validation", validation)
    cost(0, "customer", "demonstration_collection", a["demonstration_hours"]*cell["wage_usd_hour"])
    cost(0, "customer", "customer_path_additional_setup", setup)
    cost(0, "model_supplier", "model_adaptation_engineering", a["adaptation_engineering_hours"]*engineering)
    cost(0, "model_supplier", "model_adaptation_compute", a["adaptation_compute_usd"])
    cost(0, "model_supplier", "allocated_model_development_charge", a["model_development_allocation_usd_upfront"])
    transfer(0, "operator", "oem", "hardware_purchase", system["price_usd"]*base_p["price_multiplier"])
    transfer(0, "operator", "integrator", "integration_payment", integration_payment)
    transfer(0, "operator", "model_supplier", "model_upfront_payment", a["model_upfront_payment_usd"])
    model_fee = cents(common["model_fee_usd_year"])
    service_fee = cents(baseline/100*common["service_price_fraction"], derived=True)
    for year in range(1, life+1):
        cost(year, "operator", "remaining_human_service_and_site_digital", human_residual/100)
        cost(year, "operator", "required_robot_operation_and_support", e["provider_operating_cost_usd"])
        cost(year, "operator", "network_resilience_infrastructure", a["network_resilience_usd_year"])
        cost(year, "customer", "unavoidable_released_payroll_cash", unavoidable/100, False)
        cost(year, "model_supplier", "inference_resource_expense", base_p["digital_cost_usd"]*a["inference_resource_multiplier"])
        cost(year, "model_supplier", "model_maintenance_and_support", a["model_maintenance_usd_year"])
        transfer(year, "operator", "model_supplier", "model_fee", model_fee/100)
        transfer(year, "customer", "operator", "service_payment", service_fee/100)
    cash_rows, lifetime_net = [], {entity: 0 for entity in entities}
    for year in range(life+1):
        for entity in entities:
            paid = sum(x["amount_cents"] for x in expense if x["period"] == year and x["entity"] == entity)
            incoming = sum(x["amount_cents"] for x in transfers if x["period"] == year and x["receiver_entity"] == entity and not x["internal_eliminated"])
            outgoing = sum(x["amount_cents"] for x in transfers if x["period"] == year and x["payer_entity"] == entity and not x["internal_eliminated"])
            credit = baseline if year > 0 and entity == mapping["customer"] else 0
            net = credit+incoming-outgoing-paid
            lifetime_net[entity] += net
            cash_rows.append({"period": year, "entity": entity, "baseline_cost_avoided_credit_cents": credit,
                              "expense_cents": paid, "external_receipts_cents": incoming,
                              "external_payments_cents": outgoing, "net_incremental_cents": net})
    resources = sum(x["amount_cents"] for x in expense if x["resource_cost"])
    cash_cost = sum(x["amount_cents"] for x in expense)
    baseline_lifetime = baseline*life
    consolidated_net = sum(lifetime_net.values())
    if consolidated_net != baseline_lifetime-cash_cost:
        raise ArithmeticError("Transfers failed to cancel")
    if cash_cost-resources != unavoidable*life:
        raise ArithmeticError("Labor cash/resource boundary failed")
    if any(abs(v) > MAX_CENTS for v in [resources, cash_cost, *lifetime_net.values()]):
        raise ValueError("Lifetime accounting exceeds exact JSON cent range")
    model_interval = _fee_interval(mapping["operator"], mapping["model_supplier"], model_fee, lifetime_net, life, common)
    service_interval = _fee_interval(mapping["customer"], mapping["operator"], service_fee, lifetime_net, life, common)
    return {"architecture_id": name, "label": label, "status": "synthetic_conditional_reference",
            "customer_path": common["customer_path"], "empirical_qualification": "not_established",
            "assumptions": copy.deepcopy(a), "effective_physical_parameters": effective,
            "accepted_service_units_year": e["accepted_units"], "output_unit": e["output_unit"],
            "robot_accepted_units_year": e["robot_accepted_units"], "retained_human_hours_year": e["retained_human_hours"],
            "horizon_years": life, "resource_cost_usd_year": _annual(resources, life),
            "resource_saving_vs_digital_human_usd_year": _annual(baseline_lifetime-resources, life),
            "cash_benefit_usd_year": _annual(consolidated_net, life),
            "unavoidable_released_payroll_cash_usd_year": unavoidable/100,
            "observed_payroll_removed_usd": None,
            "observed_payroll_removed_missing_reason": "No staffing schedule is observed; cash effects use the declared labor-avoidability proxy.",
            "lifetime_resource_cost_cents": resources, "lifetime_cash_cost_cents": cash_cost,
            "lifetime_baseline_cost_credit_cents": baseline_lifetime,
            "lifetime_consolidated_net_incremental_cents": consolidated_net,
            "asset_owner_entity": mapping["operator"], "role_entities": copy.deepcopy(mapping),
            "asset_contract": "Operator outright purchase; the legacy sale/lease/RaaS selector is a separate reference model.",
            "entities": [{"entity": entity, "roles": [r for r in ROLES if mapping[r] == entity],
                          "lifetime_net_incremental_cents": value, "annual_equivalent_net_usd": _annual(value, life),
                          "nonnegative_at_selected_payments": value >= 0} for entity, value in lifetime_net.items()],
            "all_entities_nonnegative_at_selected_payments": all(v >= 0 for v in lifetime_net.values()),
            "fee_intervals": {"model_fee": model_interval, "service_payment": service_interval},
            "expense_ledger": expense, "transfer_ledger": transfers, "cash_ledger": cash_rows,
            "rounding": "Derived monetary line items round once to cents (half up); annual equivalents divide lifetime cents without intermediate rounding.",
            "cash_boundary": "Allocated incremental case schedule, with baseline cost credits rather than actual customer receipts. Upstream development is a declared allocated upfront charge; no company cash calendar, financing or feasibility is reconstructed."}


def compare(cell, system, p, cap, settings, evaluate, validate_parameters):
    labels = catalog()["labels"]
    common = settings["common"]
    # Validate all effective physical inputs before producing any comparison.
    for a in settings["profiles"].values():
        validate_parameters({**p, "digital_cost_usd": 0,
                             "integration_hours": p["integration_hours"]*a["integration_multiplier"],
                             "intervention_minutes": p["intervention_minutes"]+a["support_minutes_delta"]})
    rows = [_case(name, labels[name], cell, system, p, cap, common, a, evaluate, validate_parameters)
            for name, a in settings["profiles"].items()]
    path_comparison = []
    other_path = "newco" if common["customer_path"] == "incumbent" else "incumbent"
    for name, a in settings["profiles"].items():
        selected = next(x for x in rows if x["architecture_id"] == name)
        other = _case(name, labels[name], cell, system, p, cap, {**common, "customer_path": other_path}, a, evaluate, validate_parameters)
        pair = {x["customer_path"]: x for x in (selected, other)} if selected["status"] == "synthetic_conditional_reference" else None
        path_comparison.append({"architecture_id": name, "status": "equal_technology_reference" if pair else "not_admitted",
            "incumbent_resource_cost_usd_year": pair["incumbent"]["resource_cost_usd_year"] if pair else None,
            "newco_resource_cost_usd_year": pair["newco"]["resource_cost_usd_year"] if pair else None,
            "physical_service_identical": pair["incumbent"]["robot_accepted_units_year"] == pair["newco"]["robot_accepted_units_year"] if pair else None,
            "boundary": "Path labels have no productivity multiplier. Only explicit additional setup costs differ; timing, demand capture, financing and incumbent response are not linked here."})
    human = evaluate(cell, system, p, cap, digital=False, robot=False)
    digital = evaluate(cell, system, p, cap, digital=True, robot=False)
    return {"architectures": rows, "customer_path_comparison": path_comparison,
            "alternatives": {"human_resource_cost_usd_year": human["resource_cost_usd"],
                             "digital_human_resource_cost_usd_year": digital["resource_cost_usd"],
                             "specialized_resource_cost_usd_year": digital["resource_cost_usd"]*cell["specialized_cost_factor"]+5000,
                             "specialized_boundary": "Existing synthetic factor and annual capital allowance; not an observed qualified machine.",
                             "accepted_service_units_year": cell["annual_units_per_site"], "output_unit": cell["output_unit"]}}
