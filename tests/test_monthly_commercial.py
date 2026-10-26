"""Payment/title witnesses and cross-world invariants on the shared physical loop."""
from dataclasses import FrozenInstanceError, replace
from fractions import Fraction
import hashlib
import json
import random
import subprocess
import sys
import unittest

from model.monthly_commercial import Contract, commercial_artifact, commercial_witnesses, run_commercial, replay_case
from model.monthly_deployment import Collection, Operator, Plan, Start, System, monthly_witnesses
from model.treasury import Account, Moment, Treasury


def plan(**kw):
    return replace(Plan("test", 5, (Operator("site", 2, (1000,)*5),), ("site",),
        (0,)*5, (3,)*5, (3,)*5, (3,)*5, opening_components=30, starts=(Start("A", 0, 1, 1),)), **kw)


def cash(provider=10_000_000, customer=20_000_000, lessor=20_000_000):
    return Treasury((Account("provider", provider), Account("customer", customer), Account("lessor", lessor),
                    Account("manufacturer", 0), Account("deployment_vendor", 0), Account("old_buyer", 20_000_000)))


def contract(mode="sale", **kw):
    return replace(Contract("C", "site", "customer", mode, "lessor" if mode == "lease" else None), **kw)


def run(p=None, t=None, c=None):
    return run_commercial(p or plan(), t or cash(), (c or contract(),))


def quantities(r):
    return [sum((Fraction(**o["accepted_output_units"]) for o in m["outputs"]), Fraction()) for m in r["months"]]


def invoices(r, category):
    return [i for i in r["closing_treasury"]["invoices"] if i["category"] == category]


def balances(r):
    return r["months"][-1]["closing_cash_cents"]


def physical(r):
    return [{k: m[k] for k in ("opening_stock", "closing_stock", "components", "flows", "support", "outputs")}
            for m in r["months"]]


class CommercialTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.cases = commercial_witnesses()

    def test_previous_six_witnesses_unchanged(self):
        self.assertEqual(hashlib.sha256(json.dumps(monthly_witnesses(), sort_keys=True,
            separators=(',', ':')).encode()).hexdigest(), "447ccb1592fe3bdf27f1e0e24a1757749b3caca0d67c63635666c28b2c3ed448")

    def test_funded_worlds_same_physical_outlay_and_output(self):
        a, b, c = [self.cases[x] for x in ("sale", "lease", "provider_service")]
        self.assertEqual(physical(a), physical(b)); self.assertEqual(physical(a), physical(c))
        for r in (a, b, c):
            self.assertEqual(quantities(r), [0, 0, 25, 100, 100])
            cons = r["commercial"]["consolidation"]
            self.assertEqual(cons["external_physical_outlay_cents"], 3_740_000)
            self.assertEqual(cons["included_cash_change_cents"], -3_740_000)
            self.assertEqual(cons["other_boundary_net_cash_cents"], 0)
        self.assertEqual(balances(a)["customer"], 3_870_000)
        self.assertEqual(balances(b)["customer"], 6_870_000)
        self.assertEqual(balances(b)["lessor"], 7_000_000)
        self.assertEqual(sum(i["outstanding_cents"] for i in invoices(c, "service_fee")), 1_000_000)

    def test_price_only_redistributes_with_funded_gates(self):
        for mode in ("sale", "lease"):
            base, changed = run(c=contract(mode)), run(c=contract(mode, purchase_cents_per_robot=6_500_000))
            self.assertEqual(physical(base), physical(changed))
            self.assertEqual(base["commercial"]["consolidation"], changed["commercial"]["consolidation"])
            payer = "customer" if mode == "sale" else "lessor"
            self.assertEqual(balances(changed)["provider"]-balances(base)["provider"], 500_000)
            self.assertEqual(balances(changed)[payer]-balances(base)[payer], -500_000)

    def test_title_custody_and_invoice_join_at_exact_milestones(self):
        for mode, owner in (("sale", "customer"), ("lease", "lessor"), ("provider_service", "provider")):
            r = self.cases[mode]
            monthly = r["commercial"]["months"]
            self.assertEqual(monthly[0]["assets"][0]["title_owner"], "provider")
            self.assertEqual(monthly[1]["assets"][0]["title_owner"], owner)
            self.assertEqual(monthly[1]["assets"][0]["custodian"], "deployment_vendor")
            self.assertEqual(monthly[2]["assets"][0]["custodian"], "customer")
            self.assertEqual(monthly[2]["assets"][0]["workflow_authority"], "customer")
            for e in r["events"]:
                if e["action"] in ("start", "ship", "commission", "existing_support") and e["status"] != "blocked":
                    inv = next(i for i in r["closing_treasury"]["invoices"] if i["invoice_id"] == e["invoice_id"])
                    payment = next(x for x in r["closing_treasury"]["events"] if x["kind"] == "invoice_payment" and x["reference_id"] == inv["invoice_id"])
                    self.assertEqual(payment["at"], e["at"])
                    self.assertEqual(payment["settled_cents"], inv["face_cents"])
            purchase = invoices(r, "hardware_purchase")
            self.assertEqual(sum(i["paid_cents"] for i in purchase), 0 if mode == "provider_service" else 6_000_000)
            if mode == "lease":
                self.assertTrue(all(i["payer"] == "lessor" for i in purchase))

    def test_no_future_purchase_finances_its_own_start(self):
        r = self.cases["purchase_cannot_fund_own_start"]
        self.assertEqual(r["units"], [])
        self.assertEqual(balances(r)["customer"], 10_000_000)
        self.assertEqual(r["months"][0]["components"]["closing"], 20)

    def test_settled_accepted_unit_can_fund_later_start(self):
        p = plan(starts=(Start("A", 0, 1, 1), Start("B", 1, 1, 1)))
        r = run(p, cash(provider=3_600_000))
        self.assertEqual([m["flows"]["started"] for m in r["months"]], [1, 1, 0, 0, 0])
        events = r["closing_treasury"]["events"]
        purchase = next(i for i,e in enumerate(events) if e["kind"] == "invoice_payment" and "purchase" in e["reference_id"])
        start_b = next(i for i,e in enumerate(events) if e["kind"] == "invoice_payment" and "start:B" in e["reference_id"])
        self.assertLess(purchase, start_b)
        self.assertEqual(events[purchase]["at"], {"month": 1, "phase": 5})
        self.assertEqual(r["units"][1]["started_at"], {"month": 1, "phase": 5})

    def test_transport_failure_rolls_back_purchase_and_title(self):
        r = run(plan(starts=(), opening_finished=1), cash(provider=0), contract(purchase_cents_per_robot=9_999))
        self.assertEqual(balances(r)["customer"], 20_000_000)
        self.assertEqual(balances(r)["provider"], 0)
        self.assertEqual(sum(i["paid_cents"] for i in invoices(r, "hardware_purchase")), 0)
        self.assertTrue(all(m["closing_stock"]["finished"] == 1 for m in r["months"]))
        self.assertTrue(all(m["assets"][0]["title_owner"] == "provider" for m in r["commercial"]["months"]))

    def test_purchase_shortfall_preserves_stock_and_shipping_cost(self):
        r = self.cases["lease_purchase_unfunded"]
        self.assertEqual(r["months"][-1]["closing_stock"]["finished"], 1)
        self.assertEqual(balances(r)["lessor"], 5_999_999)
        self.assertEqual(sum(i["paid_cents"] for i in invoices(r, "ship")), 0)

    def test_first_rent_and_commission_are_atomic(self):
        r = run(t=cash(customer=1_000_000), c=contract("lease"))
        self.assertTrue(all(x == 0 for x in quantities(r)))
        self.assertEqual(r["months"][-1]["closing_stock"]["transit"], 1)
        self.assertEqual(balances(r)["customer"], 1_000_000)
        self.assertEqual(sum(i["paid_cents"] for i in invoices(r, "lease_rent")), 0)
        self.assertEqual(r["commercial"]["months"][-1]["assets"][0]["title_owner"], "lessor")

    def test_rent_default_retains_asset_liability_and_no_output(self):
        r = self.cases["lease_rent_default"]
        self.assertEqual(quantities(r), [0, 0, 25, 0, 0])
        self.assertEqual(balances(r)["customer"], 890_000)
        rent = invoices(r, "lease_rent")
        self.assertEqual(sum(i["outstanding_cents"] for i in rent), 2_000_000)
        self.assertTrue(all(i["status"] == "defaulted" for i in rent if i["outstanding_cents"]))
        self.assertEqual(r["months"][-1]["closing_stock"]["installed"], 1)
        self.assertFalse(r["commercial"]["months"][-1]["assets"][0]["supported"])

    def test_old_rent_settlement_restores_support_without_recommission(self):
        t = cash(customer=2_000_000).issue_invoice("old", "customer_funds", "old_buyer", "customer", 3_000_000,
             Moment(0, 1), Moment(4, 2), Moment(4, 2), provenance="synthetic")
        r = run(plan(collections=(Collection("customer_funds",4),)), t, contract("lease"))
        self.assertEqual(quantities(r), [0, 0, 25, 0, 100])
        self.assertEqual(sum(i["outstanding_cents"] for i in invoices(r,"lease_rent")), 0)
        self.assertEqual(r["units"][0]["commissioned_at"], {"month":2,"phase":4})
        self.assertEqual(balances(r)["customer"], 1_880_000)
        self.assertEqual(sum(i["paid_cents"] for i in invoices(r,"commission")), 110_000)

    def test_service_collections_lag_and_no_fee_for_unsupported_period(self):
        r = self.cases["service_late_collection"]
        self.assertEqual(quantities(r), [0, 0, 25, 0, 100])
        fees = invoices(r, "service_fee")
        self.assertEqual([i["issued_at"]["month"] for i in fees], [2, 4])
        self.assertEqual([i["eligible_at"]["month"] for i in fees], [4, 6])
        self.assertEqual(r["units"][0]["commissioned_at"]["month"], 2)
        poor = run(t=cash(customer=0), c=contract("provider_service"))
        self.assertEqual(quantities(poor), [0, 0, 25, 0, 0])
        self.assertEqual(sum(i["outstanding_cents"] for i in invoices(poor,"service_fee")), 1_000_000)
        self.assertEqual(len(invoices(poor, "service_fee")), 1)

    def test_deposits_cancellation_and_sunk_wip(self):
        restricted, spent = [self.cases[x] for x in ("cancel_restricted_deposit", "cancel_spent_deposit")]
        self.assertEqual(restricted["units"], [])
        bank = next(a for a in restricted["commercial"]["months"][0]["cash_state"] if a["actor_id"] == "provider")
        self.assertEqual((bank["cash_cents"],bank["restricted_cents"],bank["available_cents"]),(4_000_000,3_000_000,1_000_000))
        self.assertEqual(balances(restricted)["customer"], 10_000_000)
        self.assertEqual(restricted["closing_treasury"]["deposits"][0]["outstanding_cents"], 0)
        self.assertEqual(spent["months"][-1]["closing_stock"]["finished"], 1)
        self.assertEqual(balances(spent)["provider"], 400_000)
        self.assertEqual(spent["closing_treasury"]["deposits"][0]["outstanding_cents"], 3_000_000)
        self.assertEqual(sum(quantities(spent)), 0)
        self.assertEqual(sum(i["paid_cents"] for i in invoices(spent, "start")), 3_600_000)
        self.assertEqual(spent["commercial"]["consolidation"]["other_boundary_net_cash_cents"], 0)

    def test_late_cash_pays_refund_without_reversing_manufacture(self):
        t = cash(provider=1_000_000).issue_invoice("old", "receipt", "old_buyer", "provider", 3_000_000,
            Moment(0, 1), Moment(3, 2), Moment(3, 2), provenance="synthetic")
        r = run(plan(collections=(Collection("receipt", 3),)), t,
                contract("provider_service", deposit_cents=3_000_000, deposit_restricted=False, cancel_month=1))
        self.assertEqual(r["closing_treasury"]["deposits"][0]["outstanding_cents"], 0)
        self.assertEqual(balances(r)["provider"], 400_000)
        self.assertEqual(r["months"][-1]["closing_stock"]["finished"], 1)
        self.assertEqual(r["commercial"]["consolidation"]["other_boundary_net_cash_cents"], 3_000_000)

    def test_unfunded_deposit_and_cancellation_zero(self):
        r = run(t=cash(customer=1), c=contract(deposit_cents=2))
        self.assertEqual(r["months"][-1]["closing_stock"]["finished"], 1)
        self.assertEqual(r["closing_treasury"]["deposits"], [])
        self.assertTrue(any(e["reason"] == "unfunded_required_deposit" for e in r["events"]))
        r = run(c=contract(deposit_cents=100, cancel_month=0))
        self.assertEqual(r["units"], [])
        self.assertEqual(r["closing_treasury"]["deposits"], [])

    def test_rejected_start_charged_once_in_independent_lease(self):
        r = self.cases["paid_reject"]
        self.assertEqual(sum(i["paid_cents"] for i in invoices(r, "start")), 7_200_000)
        self.assertEqual(sum(i["paid_cents"] for i in invoices(r, "hardware_purchase")), 6_000_000)
        self.assertEqual(r["months"][-1]["closing_stock"]["rejected"], 1)
        self.assertEqual(r["commercial"]["consolidation"]["external_physical_outlay_cents"], 7_340_000)

    def test_multiple_sites_canceled_request_does_not_steal_cursor(self):
        p = plan(operators=(Operator("a", 2, (1000,)*5), Operator("b", 2, (1000,)*5)),
                 allocation_cycle=("a","b"), starts=(), opening_finished=2)
        cs = (Contract("A","a","customer","sale",cancel_month=0),
              Contract("B","b","customer","lease","lessor"))
        r = run_commercial(p, cash(), cs)
        self.assertTrue(all(u["operator_id"] == "b" for u in r["units"]))
        self.assertEqual(r["unshipped_requested_additions"], {"a":2,"b":0})
        self.assertTrue(all(a["title_owner"] == "lessor" for a in r["commercial"]["months"][-1]["assets"]))
        self.assertTrue(all(i["outstanding_cents"] == 0 for i in invoices(r,"hardware_purchase")))

    def test_earned_rent_priority_existing_support_blocks_new_investment(self):
        p = plan(operators=(Operator("site",2,(1000,)*5,1),), opening_finished=1)
        r = run(p,cash(customer=800_000),contract("lease"))
        self.assertEqual(r["months"][0]["flows"]["started"],0)
        self.assertEqual(r["months"][0]["flows"]["shipped"],0)
        self.assertEqual(r["months"][0]["closing_stock"]["installed"],1)
        self.assertEqual(sum(quantities(r)),0)
        self.assertEqual(sum(i["outstanding_cents"] for i in invoices(r,"lease_rent")),5_000_000)
        self.assertEqual(balances(r)["customer"],800_000)

    def test_seeded_funded_worlds_and_cash_stock_conservation(self):
        rng=random.Random(971)
        for _ in range(15):
            n=rng.randint(1,3); accepted=rng.randint(0,n)
            p=plan(starts=(Start("A",0,n,accepted),), opening_components=rng.randint(0,20),
                   support_slots=tuple(rng.randint(0,3) for _ in range(5)),
                   commissioning_slots=tuple(rng.randint(0,3) for _ in range(5)),
                   shipping_slots=tuple(rng.randint(0,3) for _ in range(5)))
            worlds=[run(p,cash(10**9,10**9,10**9),contract(mode)) for mode in ("sale","lease","provider_service")]
            self.assertEqual(physical(worlds[0]),physical(worlds[1])); self.assertEqual(physical(worlds[0]),physical(worlds[2]))
            for r in worlds:
                actors=r["closing_treasury"]["actors"]
                self.assertEqual(sum(a["cash_cents"] for a in actors),sum(a["opening_cash_cents"] for a in actors))
                for row in r["commercial"]["months"]:
                    self.assertEqual(len(row["assets"]), len({u["unit_id"] for u in row["assets"]}))

    def test_invalid_contracts_and_late_failure_leave_inputs_unchanged(self):
        for field in ("purchase_cents_per_robot","rent_cents_per_robot_month","service_cents_per_supported_month","service_collection_lag_months","deposit_cents"):
            for value in (True,1.5,-1,float("nan"),float("inf")):
                with self.assertRaises(ValueError):contract(**{field:value})
        for cs in ((),(contract(),contract()),(contract(customer_actor="provider"),),
                   (contract("lease",lessor_actor="customer"),),(contract(customer_actor="deployment_vendor"),)):
            with self.assertRaises(ValueError):run_commercial(plan(),cash(),cs)
        t=cash(); before=t.snapshot()
        with self.assertRaises(ValueError):run(c=contract(cancel_month=2),t=t)
        self.assertEqual(before,t.snapshot())
        with self.assertRaises(FrozenInstanceError):contract().deposit_cents=5

    def test_artifact_and_cli_exact_deterministic_reproduction(self):
        a=commercial_artifact()
        a["summary"][0]["closing_cash_cents"]["provider"]=-1
        b=commercial_artifact()
        self.assertNotEqual(a,b)
        cli=json.loads(subprocess.check_output([sys.executable,"-m","model.monthly_commercial"]))
        self.assertEqual(cli,b)
        for case in cli["cases"].values():
            self.assertEqual(replay_case(case), case)

    def test_replay_opening_journal_restrictions_and_reservations(self):
        t = cash().issue_invoice("old", "prior", "provider", "manufacturer", 1_000_000,
             Moment(0,1), Moment(0,2), Moment(0,3), provenance="synthetic")
        t = t.reserve_invoice("reserve", "earmark", "prior", 1_000_000, Moment(0,1), provenance="synthetic")
        t = t.place_deposit("deposit", "legacy", "customer", "provider", 500_000, Moment(0,1),
             Moment(1,3), provenance="synthetic", restricted=True)
        t = t.authorize_credit("line", "legacy-line", "lessor", "provider", 1_000_000, Moment(0,1),
             Moment(0,2), Moment(2,3), Moment(3,1), provenance="synthetic")
        r = run(t=t)
        self.assertEqual(replay_case(r),r)
        self.assertEqual(r["months"][0]["flows"]["started"], 0)
        self.assertEqual(r["commercial"]["consolidation"]["included_cash_change_cents"],0)
        self.assertEqual(r["closing_treasury"]["deposits"][0]["outstanding_cents"],500_000)
        self.assertEqual(r["closing_treasury"]["reservations"][0]["remaining_cents"],1_000_000)


if __name__ == "__main__":
    unittest.main()
