"""Synthetic stage-2 integer physical flow coupled to the accepted Treasury API.

One provider-owned system, preplanned actions, exact cents and rational service
output. No commercial sale/title model, automatic investment or annual bridge.
"""
from __future__ import annotations

from dataclasses import asdict, dataclass, replace
from fractions import Fraction
import json

from model.treasury import Account, Moment, Treasury, usd


def _integer(value, minimum=0):
    if type(value) is not int or value < minimum:
        raise ValueError(f"Expected integer >= {minimum}")
    return value


def _name(value):
    if not isinstance(value, str) or not value.strip():
        raise ValueError("Nonempty identifier required")
    return value


def _series(values):
    if not isinstance(values, (tuple, list)):
        raise ValueError("Expected explicit monthly list/tuple")
    for value in values:
        _integer(value)
    return tuple(values)


def _rational(value):
    value = Fraction(value)
    return {"numerator": value.numerator, "denominator": value.denominator}


@dataclass(frozen=True)
class System:
    system_id: str = "SYN-MONTHLY-ONE"
    work_id: str = "SYN-ACCEPTED-BUNDLE"
    components_per_start: int = 2
    service_components_per_robot_month: int = 1
    bundled_start_cents: int = 3_600_000
    shipping_cents: int = 10_000
    commissioning_cents: int = 100_000
    support_cents_per_robot_month: int = 10_000
    assembly_lead_months: int = 1
    commissioning_lead_months: int = 1
    full_output_units_per_robot_month: int = 100
    first_month_ramp_numerator: int = 1
    first_month_ramp_denominator: int = 4

    def __post_init__(self):
        _name(self.system_id); _name(self.work_id)
        for field in ("components_per_start", "bundled_start_cents", "shipping_cents",
                      "commissioning_cents", "support_cents_per_robot_month", "assembly_lead_months",
                      "commissioning_lead_months", "full_output_units_per_robot_month",
                      "first_month_ramp_denominator"):
            _integer(getattr(self, field), 1)
        _integer(self.service_components_per_robot_month)
        _integer(self.first_month_ramp_numerator)
        if self.first_month_ramp_numerator > self.first_month_ramp_denominator:
            raise ValueError("First-month ramp cannot exceed full output")


@dataclass(frozen=True)
class Operator:
    operator_id: str
    requested_additions: int
    demand_units_by_month: tuple[int, ...]
    opening_installed: int = 0

    def __post_init__(self):
        _name(self.operator_id)
        _integer(self.requested_additions); _integer(self.opening_installed)
        object.__setattr__(self, "demand_units_by_month", _series(self.demand_units_by_month))


@dataclass(frozen=True)
class Start:
    order_id: str
    month: int
    quantity: int
    accepted_quantity: int

    def __post_init__(self):
        _name(self.order_id); _integer(self.month); _integer(self.quantity, 1)
        _integer(self.accepted_quantity)
        if self.accepted_quantity > self.quantity:
            raise ValueError("Acceptance count exceeds starts")


@dataclass(frozen=True)
class Collection:
    invoice_id: str
    month: int

    def __post_init__(self):
        _name(self.invoice_id); _integer(self.month)


@dataclass(frozen=True)
class Plan:
    plan_id: str
    months: int
    operators: tuple[Operator, ...]
    allocation_cycle: tuple[str, ...]
    qualified_component_receipts: tuple[int, ...]
    commissioning_slots: tuple[int, ...]
    support_slots: tuple[int, ...]
    shipping_slots: tuple[int, ...]
    system: System = System()
    starts: tuple[Start, ...] = ()
    collections: tuple[Collection, ...] = ()
    opening_components: int = 0
    opening_finished: int = 0
    provider_actor: str = "provider"
    manufacturing_vendor_actor: str = "manufacturer"
    deployment_vendor_actor: str = "deployment_vendor"

    def __post_init__(self):
        _name(self.plan_id); _integer(self.months, 1)
        _integer(self.opening_components); _integer(self.opening_finished)
        for name in ("provider_actor", "manufacturing_vendor_actor", "deployment_vendor_actor"):
            _name(getattr(self, name))
        if not isinstance(self.system, System):
            raise ValueError("System specification required")
        for name, kind in (("operators", Operator), ("starts", Start), ("collections", Collection)):
            values = getattr(self, name)
            if not isinstance(values, (tuple, list)) or any(not isinstance(x, kind) for x in values):
                raise ValueError("Invalid " + name)
            object.__setattr__(self, name, tuple(values))
        ids = [x.operator_id for x in self.operators]
        if not ids or len(ids) != len(set(ids)):
            raise ValueError("Unique operators required")
        if not isinstance(self.allocation_cycle, (tuple, list)) or not self.allocation_cycle:
            raise ValueError("Explicit nonempty allocation cycle required")
        object.__setattr__(self, "allocation_cycle", tuple(self.allocation_cycle))
        for operator_id in self.allocation_cycle:
            _name(operator_id)
        if any(x not in ids for x in self.allocation_cycle) or set(self.allocation_cycle) != set(ids):
            raise ValueError("Allocation cycle must cover exactly the declared operators")
        for name in ("qualified_component_receipts", "commissioning_slots", "support_slots", "shipping_slots"):
            values = _series(getattr(self, name))
            if len(values) != self.months:
                raise ValueError("Explicit capacity/receipt entry required for every month")
            object.__setattr__(self, name, values)
        if any(len(x.demand_units_by_month) != self.months for x in self.operators):
            raise ValueError("Explicit demand required for every operator/month")
        for values, key in ((self.starts, "order_id"), (self.collections, "invoice_id")):
            if len({getattr(x, key) for x in values}) != len(values):
                raise ValueError("Duplicate " + key)
            if any(x.month >= self.months for x in values):
                raise ValueError("Action outside the declared horizon")


@dataclass(frozen=True)
class Unit:
    unit_id: str
    origin: str
    status: str
    accept_when_ready: bool = True
    ready_month: int | None = None
    operator_id: str | None = None
    started_at: Moment | None = None
    accepted_at: Moment | None = None
    shipped_at: Moment | None = None
    commissioned_at: Moment | None = None


def run_monthly(plan: Plan, treasury: Treasury):
    """Return a detached deterministic artifact; never mutate supplied inputs."""
    if not isinstance(plan, Plan) or not isinstance(treasury, Treasury):
        raise ValueError("Plan and Treasury required")
    if treasury.events and treasury.events[-1].at > Moment(0, 1):
        raise ValueError("Opening treasury must precede the first monthly phase")
    for actor in (plan.provider_actor, plan.manufacturing_vendor_actor, plan.deployment_vendor_actor):
        treasury.account(actor)
    if plan.provider_actor in (plan.manufacturing_vendor_actor, plan.deployment_vendor_actor):
        raise ValueError("Cash vendors must be separate legal counterparties")
    for collection in plan.collections:
        if treasury.invoice(collection.invoice_id).payee != plan.provider_actor:
            raise ValueError("Collections must be explicit opening provider receivables")

    spec = plan.system
    prefix = "monthly:" + plan.plan_id + ":"
    provenance = "synthetic_monthly_plan:" + plan.plan_id
    initial_treasury = treasury
    components = plan.opening_components
    units = [Unit(f"opening-finished-{i+1}", "opening_stock", "finished")
             for i in range(plan.opening_finished)]
    for operator in plan.operators:
        units.extend(Unit(f"opening-installed-{operator.operator_id}-{i+1}", "opening_stock", "installed",
                          operator_id=operator.operator_id) for i in range(operator.opening_installed))
    remaining = {x.operator_id: x.requested_additions for x in plan.operators}
    cursor = 0
    events, months = [], []

    def record(month, phase, action, unit_ids=(), status="completed", reason="", invoice_id=None, **detail):
        events.append({"event_id": prefix + "physical-" + str(len(events) + 1),
                       "at": asdict(Moment(month, phase)), "action": action,
                       "unit_ids": list(unit_ids), "status": status, "reason": reason,
                       "invoice_id": invoice_id, "provenance": provenance, **detail})

    def issue(label, amount, month, phase, vendor, issued_phase=1):
        nonlocal treasury
        iid = prefix + f"m{month}:" + label
        treasury = treasury.issue_invoice(iid + ":issue", iid, plan.provider_actor, vendor, amount,
                                          Moment(month, issued_phase),
                                          Moment(month, phase), Moment(month, phase),
                                          provenance=provenance, cancellable=True, category=label.split(":")[0])
        return iid

    def admit(iid, month, phase, physical_reason=""):
        nonlocal treasury
        if not physical_reason:
            treasury = treasury.settle_invoice(iid + ":pay", iid, Moment(month, phase), provenance=provenance)
            if treasury.invoice(iid).outstanding_cents == 0:
                return ""
            physical_reason = "funding:" + treasury.events[-1].reason
        # These are cancellable, contingent prepaid bookings, not overdue earned fees.
        treasury = treasury.cancel_invoice(iid + ":cancel", iid, Moment(month, phase), provenance=provenance)
        return physical_reason

    def counts():
        return {state: sum(u.status == state for u in units)
                for state in ("wip", "rejected", "finished", "transit", "installed")}

    def put(changed):
        for index, unit in enumerate(units):
            if unit.unit_id == changed.unit_id:
                units[index] = changed
                return
        raise AssertionError("Missing unit")

    for month in range(plan.months):
        opening = counts()
        opening_components = components
        opening_cash = {a.actor_id: treasury.balance(a.actor_id) for a in treasury.accounts}
        supported = set()
        service_used = starts_used = 0
        commissioned = shipped = started = accepted = rejected = 0
        existing = [u for u in units if u.status == "installed"]
        arriving = [u for u in units if u.status == "transit" and u.ready_month <= month]
        scheduled = [s for s in plan.starts if s.month == month]
        support_invoices = {u.unit_id: issue("support:" + u.unit_id, spec.support_cents_per_robot_month,
                                            month, 3, plan.deployment_vendor_actor) for u in existing}
        commission_invoices = {u.unit_id: issue("commission:" + u.unit_id,
                                               spec.commissioning_cents + spec.support_cents_per_robot_month,
                                               month, 4, plan.deployment_vendor_actor) for u in arriving}
        start_invoices = {s.order_id: issue("start:" + s.order_id, s.quantity * spec.bundled_start_cents,
                                          month, 5, plan.manufacturing_vendor_actor) for s in scheduled}

        # Phase 2: only explicitly scheduled settlement of opening receivables.
        for collection in (x for x in plan.collections if x.month == month):
            event_id = prefix + f"m{month}:collect:" + collection.invoice_id
            treasury = treasury.settle_invoice(event_id, collection.invoice_id, Moment(month, 2), provenance=provenance)
            record(month, 2, "collect_opening_receivable", status=treasury.events[-1].status,
                   reason=treasury.events[-1].reason, invoice_id=collection.invoice_id,
                   cash_settled_cents=treasury.events[-1].settled_cents)

        # Phase 3: opening installed units have first claim on slots, spares and cash.
        for unit in existing:
            reason = "support_slots" if len(supported) >= plan.support_slots[month] else \
                     "support_components" if components < spec.service_components_per_robot_month else ""
            iid = support_invoices[unit.unit_id]
            reason = admit(iid, month, 3, reason)
            if not reason:
                supported.add(unit.unit_id)
                components -= spec.service_components_per_robot_month
                service_used += spec.service_components_per_robot_month
            record(month, 3, "existing_support", (unit.unit_id,), "blocked" if reason else "supported", reason, iid)
        existing_supported = len(supported)
        unsupported_existing = len(existing) - existing_supported

        # Phase 4 receipts cannot retroactively support phase-3 service bookings.
        receipt = plan.qualified_component_receipts[month]
        components += receipt
        if receipt:
            record(month, 4, "qualified_component_receipt", quantity=receipt,
                   cash_basis="consigned_until_bundled_start_or_service_issue")
        protected_spares = min(components, unsupported_existing * spec.service_components_per_robot_month)
        for unit in tuple(units):
            if unit.status == "wip" and unit.ready_month <= month:
                if unit.accept_when_ready:
                    accepted += 1
                    put(replace(unit, status="finished", ready_month=None, accepted_at=Moment(month, 4)))
                else:
                    rejected += 1
                    put(replace(unit, status="rejected", ready_month=None))
                record(month, 4, "acceptance", (unit.unit_id,), "accepted" if unit.accept_when_ready else "rejected")
        for unit in arriving:
            reason = "existing_support_shortfall" if unsupported_existing else \
                     "commissioning_slots" if commissioned >= plan.commissioning_slots[month] else \
                     "support_slots" if len(supported) >= plan.support_slots[month] else \
                     "support_components" if components - protected_spares < spec.service_components_per_robot_month else ""
            iid = commission_invoices[unit.unit_id]
            reason = admit(iid, month, 4, reason)
            if not reason:
                put(replace(unit, status="installed", ready_month=None, commissioned_at=Moment(month, 4)))
                commissioned += 1
                supported.add(unit.unit_id)
                components -= spec.service_components_per_robot_month
                service_used += spec.service_components_per_robot_month
            record(month, 4, "commission", (unit.unit_id,), "blocked" if reason else "installed", reason, iid)

        # Shipping bookings are issued after actual acceptance in phase 4.
        target = month + spec.commissioning_lead_months
        candidates = [u for u in units if u.status == "finished"]
        ship_invoices = {u.unit_id: issue("ship:" + u.unit_id, spec.shipping_cents,
                                         month, 5, plan.deployment_vendor_actor, issued_phase=4) for u in candidates}
        for unit in candidates:
            awaiting = sum(u.status == "transit" and u.ready_month <= target for u in units)
            booked_for_target = sum(u.status == "transit" and u.ready_month == target for u in units)
            future_installed = sum(u.status == "installed" for u in units) + awaiting
            reason = "existing_support_shortfall" if unsupported_existing else \
                     "shipping_slots" if shipped >= plan.shipping_slots[month] else \
                     "commissioning_outside_horizon" if target >= plan.months else \
                     "future_commissioning_slots" if booked_for_target >= plan.commissioning_slots[target] else \
                     "future_support_slots" if future_installed >= plan.support_slots[target] else \
                     "no_requested_assignment" if not any(remaining.values()) else ""
            iid = ship_invoices[unit.unit_id]
            reason = admit(iid, month, 5, reason)
            if not reason:
                for offset in range(len(plan.allocation_cycle)):
                    index = (cursor + offset) % len(plan.allocation_cycle)
                    operator_id = plan.allocation_cycle[index]
                    if remaining[operator_id]:
                        cursor = (index + 1) % len(plan.allocation_cycle)
                        break
                remaining[operator_id] -= 1
                shipped += 1
                put(replace(unit, status="transit", operator_id=operator_id, ready_month=target,
                            shipped_at=Moment(month, 5)))
            record(month, 5, "ship", (unit.unit_id,), "blocked" if reason else "shipped", reason, iid,
                   earliest_commission_month=target)
        for start in scheduled:
            needed = start.quantity * spec.components_per_start
            reason = "existing_support_shortfall" if unsupported_existing else \
                     "start_components_after_service_reserve" if needed > components - protected_spares else ""
            iid = start_invoices[start.order_id]
            reason = admit(iid, month, 5, reason)
            ids = tuple(f"start-{start.order_id}-{i+1}" for i in range(start.quantity))
            if not reason:
                components -= needed
                starts_used += needed
                started += start.quantity
                units.extend(Unit(uid, start.order_id, "wip", index < start.accepted_quantity,
                                  month + spec.assembly_lead_months, started_at=Moment(month, 5))
                             for index, uid in enumerate(ids))
            record(month, 5, "start", ids if not reason else (), "blocked" if reason else "started", reason, iid,
                   requested_quantity=start.quantity, components_consumed=0 if reason else needed)

        outputs = []
        for operator in plan.operators:
            assigned = [u for u in units if u.status == "installed" and u.operator_id == operator.operator_id]
            active = [u for u in assigned if u.unit_id in supported]
            capacity = sum((Fraction(spec.full_output_units_per_robot_month) *
                            (Fraction(spec.first_month_ramp_numerator, spec.first_month_ramp_denominator)
                             if u.commissioned_at == Moment(month, 4) else 1) for u in active), Fraction(0))
            demand = operator.demand_units_by_month[month]
            output = min(capacity, Fraction(demand))
            outputs.append({"operator_id": operator.operator_id, "assigned_installed": len(assigned),
                            "supported_units": len(active), "demand_units": demand,
                            "ramped_capacity_units": _rational(capacity), "accepted_output_units": _rational(output)})
            record(month, 6, "operate", tuple(u.unit_id for u in active), operator_id=operator.operator_id,
                   capacity_units=_rational(capacity), demand_units=demand, output_units=_rational(output))
        closing = counts()
        row = {"month": month, "opening_stock": opening, "closing_stock": closing,
               "components": {"opening": opening_components, "qualified_receipts": receipt,
                              "service_consumed": service_used, "start_consumed": starts_used,
                              "closing": components, "protected_unconsumed_for_existing": protected_spares},
               "flows": {"started": started, "accepted": accepted, "rejected": rejected,
                         "shipped": shipped, "commissioned": commissioned},
               "support": {"slots": plan.support_slots[month], "used": len(supported),
                           "existing_supported": existing_supported, "new_supported": commissioned,
                           "unsupported_installed": closing["installed"] - len(supported)},
               "commissioning_slots": plan.commissioning_slots[month], "shipping_slots": plan.shipping_slots[month],
               "outputs": outputs, "opening_cash_cents": opening_cash,
               "closing_cash_cents": {a.actor_id: treasury.balance(a.actor_id) for a in treasury.accounts}}
        _audit_month(row)
        if len({u.unit_id for u in units}) != len(units):
            raise ValueError("Duplicate unit identity")
        months.append(row)

    closing_treasury = treasury.snapshot()
    closing_treasury["as_of"] = asdict(Moment(plan.months - 1, 7))
    for item in closing_treasury["invoices"]:
        item["status"] = treasury.invoice_status(item["invoice_id"], Moment(plan.months - 1, 7))
    return {"schema_version": "monthly-deployment/0.1", "scope": "synthetic_isolated_stage_2_fixture",
            "quantity_basis": "integer_robots_components_exact_rational_expected_service",
            "manufacturing_cash_basis": "bundled_per_start_including_consigned_components",
            "ownership": "provider_owned_all_units_operator_assignment_only",
            "plan": asdict(plan), "months": months, "units": [asdict(u) for u in units], "events": events,
            "unshipped_requested_additions": remaining,
            "opening_treasury": initial_treasury.snapshot(), "closing_treasury": closing_treasury}


def _audit_month(row):
    a, z, f, c = row["opening_stock"], row["closing_stock"], row["flows"], row["components"]
    expected = {"wip": a["wip"] + f["started"] - f["accepted"] - f["rejected"],
                "finished": a["finished"] + f["accepted"] - f["shipped"],
                "transit": a["transit"] + f["shipped"] - f["commissioned"],
                "installed": a["installed"] + f["commissioned"], "rejected": a["rejected"] + f["rejected"]}
    if z != expected or any(value < 0 for value in z.values()):
        raise AssertionError("Physical stock conservation failed")
    if c["closing"] != c["opening"] + c["qualified_receipts"] - c["service_consumed"] - c["start_consumed"] or not 0 <= c["protected_unconsumed_for_existing"] <= c["closing"]:
        raise AssertionError("Component conservation/reservation failed")
    if row["support"]["used"] > row["support"]["slots"] or f["commissioned"] > row["commissioning_slots"] or f["shipped"] > row["shipping_slots"]:
        raise AssertionError("Capacity exceeded")
    for output in row["outputs"]:
        value = Fraction(**output["accepted_output_units"])
        capacity = Fraction(**output["ramped_capacity_units"])
        if not 0 <= value <= min(capacity, output["demand_units"]):
            raise AssertionError("Unassigned or undemanded output")


def monthly_witnesses():
    """Exact phase witness and bounded adverse alternatives; all synthetic."""
    def cash(amount):
        return Treasury((Account("provider", usd(amount)), Account("manufacturer", 0),
                         Account("deployment_vendor", 0), Account("buyer", usd("60000"))))
    def one(pid, **changes):
        base = Plan(pid, 4, (Operator("incumbent", 1, (100, 100, 100, 100)),), ("incumbent",),
                    (0, 0, 0, 0), (1, 1, 1, 1), (1, 1, 1, 1), (1, 1, 1, 1),
                    opening_components=4, starts=(Start("one", 0, 1, 1),))
        return replace(base, **changes)
    funded = run_monthly(one("witness-8-funded"), cash("40000"))
    poor = cash("10000").issue_invoice("future-issue", "future-receipt", "buyer", "provider", usd("60000"),
                                       Moment(0, 1), Moment(1, 2), Moment(1, 2),
                                       provenance="synthetic_preexisting_receivable_not_robot_sale")
    unfunded = run_monthly(one("unfunded-future-receipt", collections=(Collection("future-receipt", 1),)), poor)
    no_parts = run_monthly(one("funded-no-parts", opening_components=0), cash("40000"))
    no_install_cash = run_monthly(one("unfunded-install"), cash("36100"))
    rejected = run_monthly(one("all-rejected", starts=(Start("one", 0, 1, 0),)), cash("40000"))
    shared = Plan("witness-4-static-allocation", 2,
                  (Operator("incumbent", 4, (1000, 1000), 2), Operator("entrant", 10, (1000, 1000))),
                  ("incumbent", "incumbent", "entrant"), (0, 0), (3, 3), (5, 5), (10, 10),
                  opening_components=7, opening_finished=5)
    return {"witness_8_funded": funded, "unfunded_future_receipt": unfunded,
            "funded_without_components": no_parts, "unfunded_commissioning": no_install_cash,
            "paid_rejected_start": rejected, "witness_4_static_allocation": run_monthly(shared, cash("10000"))}


if __name__ == "__main__":
    print(json.dumps(monthly_witnesses(), indent=2, sort_keys=True, allow_nan=False))
