"""Synthetic contracts on the shared monthly physical and integer-cent engines."""
from __future__ import annotations

from dataclasses import asdict, dataclass, fields, replace
from fractions import Fraction
import hashlib
import json
from pathlib import Path

from model.monthly_deployment import Plan, Operator, Start, Collection, System, _integer, _name, run_monthly
from model.treasury import Account, Moment, Treasury, Invoice, Reservation, Deposit, Credit, Event, Posting


@dataclass(frozen=True)
class Contract:
    contract_id: str
    operator_id: str
    customer_actor: str
    arrangement: str
    lessor_actor: str | None = None
    purchase_cents_per_robot: int = 6_000_000
    rent_cents_per_robot_month: int = 1_000_000
    service_cents_per_supported_month: int = 1_000_000
    service_collection_lag_months: int = 1
    deposit_cents: int = 0
    deposit_restricted: bool = True
    cancel_month: int | None = None

    def __post_init__(self):
        for value in (self.contract_id, self.operator_id, self.customer_actor):
            _name(value)
        if self.arrangement not in ("sale", "lease", "provider_service"):
            raise ValueError("Unknown commercial arrangement")
        if self.arrangement == "lease":
            _name(self.lessor_actor)
        elif self.lessor_actor is not None:
            raise ValueError("Only an independent lease has a lessor")
        for name in ("purchase_cents_per_robot", "rent_cents_per_robot_month",
                     "service_cents_per_supported_month", "service_collection_lag_months"):
            _integer(getattr(self, name), 1)
        _integer(self.deposit_cents)
        if type(self.deposit_restricted) is not bool:
            raise ValueError("Deposit restriction must be explicit Boolean")
        if self.cancel_month is not None:
            _integer(self.cancel_month)


class _Commercial:
    """Private per-run policy. Treasury and physical state stay in run_monthly."""
    def __init__(self, plan, contracts, treasury):
        if not isinstance(plan, Plan) or not isinstance(treasury, Treasury):
            raise ValueError("Plan and Treasury required")
        if not isinstance(contracts, (tuple, list)) or any(not isinstance(c, Contract) for c in contracts):
            raise ValueError("Explicit contract list required")
        self.contracts = tuple(contracts)
        ids = [c.contract_id for c in contracts]
        sites = [c.operator_id for c in contracts]
        if len(set(ids)) != len(ids) or len(set(sites)) != len(sites) or set(sites) != {o.operator_id for o in plan.operators}:
            raise ValueError("Exactly one uniquely identified contract per operator required")
        self.plan = plan
        self.by_site = {c.operator_id: c for c in contracts}
        self.prefix = "commercial:" + plan.plan_id + ":"
        self.provenance = "synthetic_commercial_plan:" + plan.plan_id
        self.events, self.months = [], []
        self.quotes, self.first_rent, self.owner = {}, {}, {}
        self.cancelled, self.refund_failed = set(), set()
        self.invoice_contract = {}
        parties = {plan.provider_actor}
        for c in contracts:
            treasury.account(c.customer_actor)
            if c.customer_actor == plan.provider_actor:
                raise ValueError("Customer and provider must be independent actors")
            parties.add(c.customer_actor)
            if c.lessor_actor:
                treasury.account(c.lessor_actor)
                parties.add(c.lessor_actor)
                if c.lessor_actor in (plan.provider_actor, c.customer_actor):
                    raise ValueError("Independent lessor must be a separate legal actor")
            if c.cancel_month is not None and c.cancel_month >= plan.months:
                raise ValueError("Cancellation outside horizon")
        if any(c.lessor_actor in {d.customer_actor for d in contracts} for c in contracts if c.lessor_actor):
            raise ValueError("Lessor/customer roles must remain separate in this fixture")
        if parties.intersection((plan.manufacturing_vendor_actor, plan.deployment_vendor_actor)):
            raise ValueError("Resource vendors must be outside the commercial perimeter")
        self.parties = sorted(parties)

    def _id(self, *parts):
        return self.prefix + ":".join(map(str, parts))

    def _record(self, at, action, **fields):
        self.events.append({"event_id": self._id("event", len(self.events)+1), "at": asdict(at),
                            "action": action, "provenance": self.provenance, **fields})

    def _issue(self, t, iid, c, payer, payee, cents, at, eligible, category, cancellable=False):
        self.invoice_contract[iid] = c.contract_id
        return t.issue_invoice(iid+":issue", iid, payer, payee, cents, at, eligible, eligible,
                               provenance=self.provenance, cancellable=cancellable, category=category)

    def _owner(self, c):
        return c.customer_actor if c.arrangement == "sale" else c.lessor_actor if c.arrangement == "lease" else self.plan.provider_actor

    def _deposit_payee(self, c):
        return c.lessor_actor if c.arrangement == "lease" else self.plan.provider_actor

    def _deposit(self, t, c):
        return next((d for d in t.deposits if d.deposit_id == self._id(c.contract_id, "deposit")), None)

    def _arrears(self, t, c, at):
        return [i for i in t.invoices if self.invoice_contract.get(i.invoice_id) == c.contract_id
                and not i.cancellable and i.outstanding_cents and i.due_at <= at]

    def prepare(self, t, month, units):
        for u in units:
            if u.unit_id not in self.owner:
                self.owner[u.unit_id] = self._owner(self.by_site[u.operator_id]) if u.status == "installed" else self.plan.provider_actor
        for c in self.contracts:
            if c.cancel_month == month:
                if any(u.operator_id == c.operator_id for u in units):
                    raise ValueError("Cancellation is supported only before shipment/installation")
                self.cancelled.add(c.contract_id)
                self._record(Moment(month, 1), "contract_cancel", contract_id=c.contract_id,
                             physical_stock_reversed=False)
        for u in units:
            if u.status not in ("installed", "transit"):
                continue
            c = self.by_site[u.operator_id]
            if c.arrangement != "lease" or (u.status == "transit" and u.ready_month > month):
                continue
            first = u.status == "transit"
            iid = self._id(c.contract_id, month, u.unit_id, "first_rent" if first else "rent")
            t = self._issue(t, iid, c, c.customer_actor, c.lessor_actor, c.rent_cents_per_robot_month,
                            Moment(month, 1), Moment(month, 4 if first else 3), "lease_rent", first)
            if first:
                self.first_rent[(month, u.unit_id)] = iid
        return t

    def collect(self, t, month):
        at = Moment(month, 2)
        if month == 0:
            for c in self.contracts:
                if not c.deposit_cents or c.contract_id in self.cancelled:
                    continue
                did = self._id(c.contract_id, "deposit")
                t = t.place_deposit(did+":place", did, c.customer_actor, self._deposit_payee(c), c.deposit_cents,
                                     at, Moment(0, 3), provenance=self.provenance, restricted=c.deposit_restricted)
        return self._collect_due(t, at, "service_fee")

    def _collect_due(self, t, at, category):
        # Preserve oldest-first priority for each legal payer, even across sites.
        blocked_payers = set()
        due = sorted((i for i in t.invoices if i.category == category and not i.cancellable
                      and i.invoice_id in self.invoice_contract and i.outstanding_cents and i.due_at <= at),
                     key=lambda i: (i.due_at, i.issued_at, i.invoice_id))
        for i in due:
            if i.payer in blocked_payers:
                continue
            t = t.settle_invoice(self._id("collect", at.month, at.phase, i.invoice_id), i.invoice_id, at,
                                 provenance=self.provenance)
            if t.invoice(i.invoice_id).outstanding_cents:
                blocked_payers.add(i.payer)
        return t

    def refunds(self, t, month):
        at = Moment(month, 3)
        self.refund_failed = set()
        for c in self.contracts:
            d = self._deposit(t, c)
            if c.contract_id in self.cancelled and d and d.outstanding_cents:
                t = t.refund_deposit(self._id(c.contract_id, month, "refund"), d.deposit_id, at,
                                     provenance=self.provenance)
                if t.deposit(d.deposit_id).outstanding_cents:
                    self.refund_failed.add(d.payee)
        return t

    def mandatory(self, t, month):
        return self._collect_due(self.refunds(t, month), Moment(month, 3), "lease_rent")

    def assignment_enabled(self, operator_id, month):
        return self.by_site[operator_id].contract_id not in self.cancelled

    def dispatch_output(self, month, operator, robot_capacity):
        demand = operator.demand_units_by_month[month]
        return demand, min(robot_capacity, Fraction(demand)), {}

    def payer(self, action, unit):
        if action not in ("support", "commission"):
            return self.plan.provider_actor
        c = self.by_site[unit.operator_id]
        return self.plan.provider_actor if c.arrangement == "provider_service" else c.customer_actor

    def shipping_quotes(self, t, month, units):
        for u in units:
            for c in self.contracts:
                if c.arrangement == "provider_service" or c.contract_id in self.cancelled:
                    continue
                iid = self._id(c.contract_id, month, u.unit_id, "purchase")
                payer = c.customer_actor if c.arrangement == "sale" else c.lessor_actor
                t = self._issue(t, iid, c, payer, self.plan.provider_actor, c.purchase_cents_per_robot,
                                Moment(month, 4), Moment(month, 5), "hardware_purchase", True)
                self.quotes[(month, u.unit_id, c.operator_id)] = iid
        return t

    def _reason(self, t, month, phase, action, operator_id):
        at = Moment(month, phase)
        if action == "start":
            if len(self.cancelled) == len(self.contracts):
                return "all_contracts_cancelled"
            if self.plan.provider_actor in self.refund_failed or any(
                i.payer == self.plan.provider_actor and not i.cancellable and i.outstanding_cents and i.due_at <= at
                for i in t.invoices):
                return "provider_overdue_obligation"
            return ""
        c = self.by_site[operator_id]
        if c.contract_id in self.cancelled:
            return "contract_cancelled"
        if self._arrears(t, c, at):
            return "commercial_arrears"
        if action == "ship" and c.deposit_cents and self._deposit(t, c) is None:
            return "unfunded_required_deposit"
        if action == "ship" and self._deposit_payee(c) in self.refund_failed:
            return "owner_unfunded_refund"
        return ""

    def admit(self, t, iid, month, phase, physical_reason, unit=None, operator_id=None):
        action = t.invoice(iid).category
        if unit is not None and operator_id is None:
            operator_id = unit.operator_id
        reason = physical_reason or self._reason(t, month, phase, action, operator_id)
        extra = None
        if action == "ship" and operator_id is not None:
            extra = self.quotes.get((month, unit.unit_id, operator_id))
        elif action == "commission":
            extra = self.first_rent.get((month, unit.unit_id))
        group = ([extra] if extra else []) + [iid]
        candidate = t
        if not reason:
            for invoice in group:
                candidate = candidate.settle_invoice(invoice+":pay", invoice, Moment(month, phase), provenance=self.provenance)
                if candidate.invoice(invoice).outstanding_cents:
                    reason = "funding:" + candidate.invoice(invoice).category
                    # Retain a failed first payment's diagnostic, never a rolled-back earlier receipt.
                    if invoice == group[0]:
                        t = candidate
                    break
        if not reason:
            return candidate, ""
        for invoice in group:
            t = t.cancel_invoice(invoice+":cancel", invoice, Moment(month, phase), provenance=self.provenance)
        self._record(Moment(month, phase), "blocked_group", invoice_ids=group, reason=reason,
                     committed_cash_cents=0, unit_id=unit.unit_id if unit else None)
        return t, reason

    def shipped(self, month, unit, operator_id, treasury):
        c = self.by_site[operator_id]
        old = self.owner.get(unit.unit_id, self.plan.provider_actor)
        owner = self._owner(c)
        self.owner[unit.unit_id] = owner
        self._record(Moment(month, 5), "shipment_title", unit_id=unit.unit_id, contract_id=c.contract_id,
                     previous_owner=old, title_owner=owner, title_changed=old != owner,
                     purchase_invoice_id=self.quotes.get((month, unit.unit_id, operator_id)))

    def finish_shipping(self, t, month):
        for (m, uid, op), iid in self.quotes.items():
            if m == month and t.invoice(iid).outstanding_cents:
                t = t.cancel_invoice(iid+":unused", iid, Moment(month, 5), provenance=self.provenance)
        return t

    def bill_service(self, t, month, units, supported):
        for u in units:
            if u.unit_id not in supported:
                continue
            c = self.by_site[u.operator_id]
            if c.arrangement != "provider_service":
                continue
            iid = self._id(c.contract_id, month, u.unit_id, "service")
            t = self._issue(t, iid, c, c.customer_actor, self.plan.provider_actor, c.service_cents_per_supported_month,
                            Moment(month, 6), Moment(month+c.service_collection_lag_months, 2), "service_fee")
        return t

    def close(self, t, month, units, supported):
        assets = []
        for u in units:
            c = self.by_site.get(u.operator_id)
            assets.append({"unit_id": u.unit_id, "physical_state": u.status,
                           "title_owner": self.owner.get(u.unit_id, self.plan.provider_actor),
                           "custodian": c.customer_actor if u.status == "installed" else self.plan.deployment_vendor_actor if u.status == "transit" else self.plan.provider_actor if u.origin == "opening_stock" else self.plan.manufacturing_vendor_actor,
                           "workflow_authority": c.customer_actor if u.status == "installed" else None,
                           "support_payer": self.payer("support", u) if c else None,
                           "contract_id": c.contract_id if c else None,
                           "supported": u.unit_id in supported, "data_and_ip_rights": "unspecified"})
        self.months.append({"month": month, "assets": assets,
                            "cash_state": [a for a in t.snapshot()["actors"] if a["actor_id"] in self.parties],
                            "cancelled_contracts": sorted(self.cancelled),
                            "failed_refund_actors": sorted(self.refund_failed),
                            "overdue_contract_invoices": [i.invoice_id for i in t.invoices if i.invoice_id in self.invoice_contract
                                and i.outstanding_cents and i.due_at <= Moment(month, 7)]})

    def result(self, result):
        t = result["closing_treasury"]
        # Only costs incurred by this run; opening unrelated obligations stay outside this subtotal.
        physical_ids = {e["invoice_id"] for e in result["events"] if e.get("invoice_id") and e["action"] != "collect_opening_receivable"}
        expenses = [i for i in t["invoices"] if i["invoice_id"] in physical_ids]
        resource_outlay = sum(i["paid_cents"] for i in expenses)
        opening_cash = {a["actor_id"]: a["cash_cents"] for a in result["opening_treasury"]["actors"]}
        included_change = sum(a["cash_cents"]-opening_cash[a["actor_id"]] for a in t["actors"] if a["actor_id"] in self.parties)
        return {"schema_version": "monthly-commercial/0.1", "scope": "synthetic_stage_3_contracts_on_shared_physical_plan",
                "contracts": [asdict(c) for c in self.contracts], "events": self.events, "months": self.months,
                "consolidation": {"included_actors": self.parties, "external_physical_outlay_cents": resource_outlay,
                    "included_cash_change_cents": included_change, "other_boundary_net_cash_cents": included_change + resource_outlay,
                    "basis": "bundled_vendor_cash_outlays_not_complete_lifecycle_resource_cost"},
                "physical_cost_invoices": [i["invoice_id"] for i in expenses],
                "limits": ["No end-market sales or economic profit inferred", "No interest, taxes, recovery or residual value",
                           "No entrant-demand, annual-path or architecture bridge", "Unrelated obligations need explicit payment schedules",
                           "Security deposits are liabilities, not revenue or purchase credit"]}


def run_commercial(plan, treasury, contracts):
    policy = _Commercial(plan, contracts, treasury)
    result = run_monthly(plan, treasury, commercial=policy)
    result["schema_version"] = "monthly-deployment/0.2"
    result["scope"] = "synthetic_stage_3_commercial_fixture"
    result["ownership"] = "one_title_owner_per_unit_separate_from_custody_and_workflow"
    result["commercial"] = policy.result(result)
    return json.loads(json.dumps(result))


def restore_opening_inputs(saved):
    """Restore the shared plan, complete opening journal and contract inputs."""
    p = dict(saved["plan"])
    p["system"] = System(**p["system"])
    for key, kind in (("operators", Operator), ("starts", Start), ("collections", Collection)):
        p[key] = tuple(kind(**x) for x in p[key])
    opening = saved["opening_treasury"]
    accounts = tuple(Account(a["actor_id"], a["opening_cash_cents"], a["minimum_cash_cents"], opening["currency"])
                     for a in opening["actors"])
    def rebuild(cls, raw, moments=()):
        item = {f.name: raw[f.name] for f in fields(cls) if f.name in raw}
        for key in moments:
            item[key] = Moment(**item[key])
        if cls is Event:
            item["postings"] = tuple(Posting(**p) for p in item["postings"])
        return cls(**item)
    t = Treasury(accounts,
        tuple(rebuild(Invoice,x,("issued_at","eligible_at","due_at")) for x in opening["invoices"]),
        tuple(rebuild(Reservation,x) for x in opening["reservations"]),
        tuple(rebuild(Deposit,x,("placed_at","refund_eligible_at")) for x in opening["deposits"]),
        tuple(rebuild(Credit,x,("authorized_at","available_from","available_until","maturity")) for x in opening["credits"]),
        tuple(rebuild(Event,x,("at",)) for x in opening["events"]))
    return Plan(**p), t, tuple(Contract(**c) for c in saved["commercial"]["contracts"])


def replay_case(saved):
    """Recompute from saved opening inputs; never trust saved results as a calculation."""
    if not isinstance(saved, dict) or saved.get("schema_version") != "monthly-deployment/0.2":
        raise ValueError("A saved monthly-commercial case is required")
    return run_commercial(*restore_opening_inputs(saved))


def commercial_witnesses():
    p = Plan("commercial-reference", 5, (Operator("site", 1, (1000,)*5),), ("site",),
             (0,)*5, (2,)*5, (2,)*5, (2,)*5, opening_components=20, starts=(Start("A", 0, 1, 1),))
    def cash(provider=10_000_000, customer=10_000_000, lessor=10_000_000):
        return Treasury((Account("provider", provider), Account("customer", customer), Account("lessor", lessor),
                         Account("manufacturer", 0), Account("deployment_vendor", 0)))
    def contract(mode, **kw):
        return Contract("C", "site", "customer", mode, "lessor" if mode == "lease" else None, **kw)
    cases = {mode: run_commercial(p, cash(), (contract(mode),)) for mode in ("sale", "lease", "provider_service")}
    cases["lease_rent_default"] = run_commercial(p, cash(customer=2_000_000), (contract("lease"),))
    cases["service_late_collection"] = run_commercial(p, cash(provider=3_720_000),
        (contract("provider_service", service_collection_lag_months=2),))
    cases["purchase_cannot_fund_own_start"] = run_commercial(p, cash(provider=1_000_000), (contract("sale"),))
    for restricted in (True, False):
        cases["cancel_" + ("restricted" if restricted else "spent") + "_deposit"] = run_commercial(
            p, cash(provider=1_000_000), (contract("provider_service", deposit_cents=3_000_000,
                deposit_restricted=restricted, cancel_month=1),))
    cases["lease_purchase_unfunded"] = run_commercial(p, cash(lessor=5_999_999), (contract("lease"),))
    cases["paid_reject"] = run_commercial(replace(p, starts=(Start("A", 0, 2, 1),)), cash(), (contract("lease"),))
    return cases


def commercial_artifact():
    root = Path(__file__).resolve().parents[1]
    hashes = {p: hashlib.sha256((root/p).read_bytes()).hexdigest() for p in
              ("model/treasury.py", "model/monthly_deployment.py", "model/monthly_commercial.py")}
    cases = commercial_witnesses()
    rows = []
    for name, r in cases.items():
        amount = sum((Fraction(**o["accepted_output_units"]) for m in r["months"] for o in m["outputs"]), Fraction())
        rows.append({"case": name, "total_accepted_output": {"numerator": amount.numerator, "denominator": amount.denominator},
                     "external_physical_outlay_cents": r["commercial"]["consolidation"]["external_physical_outlay_cents"],
                     "closing_cash_cents": r["months"][-1]["closing_cash_cents"],
                     "closing_assets": r["commercial"]["months"][-1]["assets"],
                     "outstanding_invoices_cents": sum(i["outstanding_cents"] for i in r["closing_treasury"]["invoices"]),
                     "outstanding_refunds_cents": sum(d["outstanding_cents"] for d in r["closing_treasury"]["deposits"]),
                     "blocked_actions": [{"month": e["at"]["month"], "action": e["action"], "reason": e["reason"]}
                                         for e in r["events"] if e["status"] == "blocked"]})
    payload = {"schema_version": "monthly-commercial-experiments/0.1", "evidence_status": "synthetic_accounting_witnesses",
               "source_sha256": hashes, "summary": rows, "cases": cases}
    payload["artifact_hash"] = hashlib.sha256(json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    return payload


if __name__ == "__main__":
    print(json.dumps(commercial_artifact(), indent=2))
