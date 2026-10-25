"""Independent balances and adverse witnesses for the bounded monthly fixture."""
from dataclasses import FrozenInstanceError, replace
from fractions import Fraction
import json
import subprocess
import sys
import unittest

from model.monthly_deployment import Collection, Operator, Plan, Start, System, monthly_witnesses, run_monthly
from model.treasury import Account, Moment, Treasury, usd


def cash(cents=10_000_000, reserve=0):
    return Treasury((Account("provider", cents, reserve), Account("manufacturer", 0),
                     Account("deployment_vendor", 0), Account("buyer", 10_000_000)))


def plan(**changes):
    p = Plan("test", 4, (Operator("incumbent", 10, (1000,) * 4),), ("incumbent",),
             (0,) * 4, (10,) * 4, (10,) * 4, (10,) * 4,
             opening_components=100, starts=(Start("A", 0, 1, 1),))
    return replace(p, **changes)


def value(quantity):
    return Fraction(quantity["numerator"], quantity["denominator"])


def output(result, month, operator="incumbent"):
    return next(x for x in result["months"][month]["outputs"] if x["operator_id"] == operator)


class MonthlyDeploymentTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.witnesses = monthly_witnesses()

    def test_witness_8_exact_event_phases_and_single_first_month_ramp(self):
        r = self.witnesses["witness_8_funded"]
        u = r["units"][0]
        self.assertEqual(u["started_at"], {"month": 0, "phase": 5})
        self.assertEqual(u["accepted_at"], {"month": 1, "phase": 4})
        self.assertEqual(u["shipped_at"], {"month": 1, "phase": 5})
        self.assertEqual(u["commissioned_at"], {"month": 2, "phase": 4})
        self.assertEqual([value(output(r, m)["accepted_output_units"]) for m in range(4)], [0, 0, 25, 100])
        self.assertEqual([r["months"][m]["closing_stock"]["transit"] for m in range(4)], [0, 1, 0, 0])
        self.assertEqual([r["months"][m]["closing_stock"]["wip"] for m in range(4)], [1, 0, 0, 0])

    def test_witness_4_fixed_common_pool_allocation(self):
        r = self.witnesses["witness_4_static_allocation"]
        self.assertEqual(r["months"][0]["closing_stock"],
                         {"wip": 0, "rejected": 0, "finished": 2, "transit": 3, "installed": 2})
        self.assertEqual(r["months"][1]["closing_stock"]["installed"], 5)
        self.assertEqual(r["months"][1]["closing_stock"]["finished"], 2)
        self.assertEqual(r["months"][1]["support"]["used"], 5)
        self.assertEqual(value(output(r, 1, "entrant")["accepted_output_units"]), 25)
        self.assertEqual(value(output(r, 1)["accepted_output_units"]), 250)
        self.assertEqual(output(r, 1, "entrant")["assigned_installed"], 1)
        self.assertEqual(r["unshipped_requested_additions"], {"incumbent": 2, "entrant": 9})

    def test_finance_vs_components_are_distinct_admission_failures(self):
        poor = self.witnesses["unfunded_future_receipt"]
        scarce = self.witnesses["funded_without_components"]
        for r in (poor, scarce):
            self.assertTrue(all(x["flows"]["started"] == 0 for x in r["months"]))
            self.assertEqual(r["months"][0]["components"]["start_consumed"], 0)
            self.assertEqual(r["units"], [])
        self.assertIn("funding:", next(e["reason"] for e in poor["events"] if e["action"] == "start"))
        self.assertEqual(next(e["reason"] for e in scarce["events"] if e["action"] == "start"),
                         "start_components_after_service_reserve")
        self.assertEqual(poor["months"][0]["closing_cash_cents"]["provider"], usd("10000"))
        self.assertEqual(poor["months"][1]["closing_cash_cents"]["provider"], usd("70000"))
        self.assertEqual(scarce["months"][0]["closing_cash_cents"]["provider"], usd("40000"))

    def test_blocked_commission_preserves_transit_parts_and_zero_output(self):
        r = self.witnesses["unfunded_commissioning"]
        for month in (2, 3):
            row = r["months"][month]
            self.assertEqual(row["closing_stock"]["transit"], 1)
            self.assertEqual(row["closing_stock"]["installed"], 0)
            self.assertEqual(row["components"]["service_consumed"], 0)
            self.assertEqual(row["flows"]["commissioned"], 0)
            self.assertEqual(value(output(r, month)["accepted_output_units"]), 0)
        self.assertEqual(r["units"][0]["commissioned_at"], None)
        paid = [i for i in r["closing_treasury"]["invoices"] if i["category"] == "commission"]
        self.assertTrue(paid and all(i["paid_cents"] == 0 and i["outstanding_cents"] == 0 for i in paid))

    def test_late_collection_funds_delayed_install_with_one_actual_first_month_ramp(self):
        t = cash(usd("36100")).issue_invoice("old-sale", "late-receipt", "buyer", "provider", usd("2000"),
                                            Moment(0, 1), Moment(3, 2), Moment(3, 2), provenance="synthetic_old_receivable")
        r = run_monthly(plan(collections=(Collection("late-receipt", 3),)), t)
        self.assertEqual(r["units"][0]["commissioned_at"], {"month": 3, "phase": 4})
        self.assertEqual(value(output(r, 2)["accepted_output_units"]), 0)
        self.assertEqual(value(output(r, 3)["accepted_output_units"]), 25)
        self.assertEqual(sum(i["paid_cents"] for i in r["closing_treasury"]["invoices"] if i["category"] == "ship"), usd("100"))
        self.assertEqual(sum(i["paid_cents"] for i in r["closing_treasury"]["invoices"] if i["category"] == "commission"), usd("1100"))

    def test_declared_cost_packages_each_paid_once(self):
        r = self.witnesses["witness_8_funded"]
        self.assertEqual(r["months"][-1]["closing_cash_cents"]["provider"], usd("2700"))
        charges = {}
        for invoice in r["closing_treasury"]["invoices"]:
            charges[invoice["category"]] = charges.get(invoice["category"], 0) + invoice["paid_cents"]
        self.assertEqual(charges, {"start": usd("36000"), "ship": usd("100"),
                                   "commission": usd("1100"), "support": usd("100")})

    def test_paid_yield_loss_is_sunk_and_never_paid_twice(self):
        r = run_monthly(plan(starts=(Start("batch", 0, 2, 1),)), cash())
        self.assertEqual(r["months"][1]["flows"]["accepted"], 1)
        self.assertEqual(r["months"][1]["flows"]["rejected"], 1)
        self.assertEqual(r["months"][-1]["closing_stock"]["rejected"], 1)
        manufacturer = next(a for a in r["closing_treasury"]["actors"] if a["actor_id"] == "manufacturer")
        self.assertEqual(manufacturer["cash_cents"], 2 * System().bundled_start_cents)
        self.assertEqual(r["months"][0]["components"]["start_consumed"], 4)
        reject = self.witnesses["paid_rejected_start"]
        self.assertEqual(reject["months"][-1]["closing_cash_cents"]["provider"], usd("4000"))
        self.assertTrue(all(value(output(reject, m)["accepted_output_units"]) == 0 for m in range(4)))

    def test_paid_shipping_required_and_assignment_not_consumed_if_blocked(self):
        r = run_monthly(plan(starts=(), opening_finished=2), cash(0))
        self.assertTrue(all(x["closing_stock"]["finished"] == 2 for x in r["months"]))
        self.assertEqual(r["unshipped_requested_additions"]["incumbent"], 10)
        self.assertTrue(all(u["operator_id"] is None for u in r["units"]))
        self.assertEqual(sum(x["flows"]["shipped"] for x in r["months"]), 0)

    def test_existing_support_has_priority_and_failed_service_preserves_stock(self):
        p = plan(operators=(Operator("incumbent", 10, (1000,) * 4, 1),),
                 opening_components=2, support_slots=(0, 0, 0, 0), opening_finished=1)
        r = run_monthly(p, cash())
        for row in r["months"]:
            self.assertEqual(row["closing_stock"]["installed"], 1)
            self.assertEqual(row["components"]["protected_unconsumed_for_existing"], 1)
            self.assertEqual(row["components"]["closing"], 2)
            self.assertEqual(row["flows"]["started"], 0)
            self.assertEqual(row["flows"]["shipped"], 0)
            self.assertEqual(value(row["outputs"][0]["accepted_output_units"]), 0)
        self.assertEqual(r["months"][0]["closing_cash_cents"]["provider"], 10_000_000)

    def test_service_spares_before_manufacturing_even_when_start_cash_exists(self):
        p = plan(operators=(Operator("incumbent", 10, (1000,) * 4, 1),), opening_components=2)
        r = run_monthly(p, cash())
        self.assertEqual(r["months"][0]["components"]["service_consumed"], 1)
        self.assertEqual(r["months"][0]["components"]["start_consumed"], 0)
        self.assertEqual(value(output(r, 0)["accepted_output_units"]), 100)
        self.assertEqual(r["months"][2]["support"]["unsupported_installed"], 1)
        self.assertEqual(r["months"][2]["closing_stock"]["installed"], 1)

    def test_current_receipt_can_fund_parts_for_start_but_not_retroactive_service(self):
        p = plan(opening_components=0, qualified_component_receipts=(2, 0, 1, 1))
        r = run_monthly(p, cash())
        self.assertEqual(r["months"][0]["flows"]["started"], 1)
        self.assertEqual(r["months"][2]["flows"]["commissioned"], 1)
        self.assertEqual(value(output(r, 2)["accepted_output_units"]), 25)
        # Month-3 parts arrive after phase-3 support; they remain protected for month 4.
        self.assertEqual(value(output(r, 3)["accepted_output_units"]), 0)
        self.assertEqual(r["months"][3]["components"]["protected_unconsumed_for_existing"], 1)

    def test_longer_leads_and_distinct_future_commission_bookings(self):
        p = Plan("long", 6, (Operator("incumbent", 3, (1000,) * 6),), ("incumbent",),
                 (0,) * 6, (1,) * 6, (3,) * 6, (1,) * 6,
                 system=replace(System(), assembly_lead_months=2, commissioning_lead_months=2),
                 opening_components=20, starts=(Start("A", 0, 1, 1), Start("B", 1, 1, 1)))
        r = run_monthly(p, cash(20_000_000))
        a, b = r["units"]
        self.assertEqual((a["accepted_at"]["month"], a["shipped_at"]["month"], a["commissioned_at"]["month"]), (2, 2, 4))
        self.assertEqual((b["accepted_at"]["month"], b["shipped_at"]["month"], b["commissioned_at"]["month"]), (3, 3, 5))
        self.assertEqual(value(output(r, 4)["accepted_output_units"]), 25)
        self.assertEqual(value(output(r, 5)["accepted_output_units"]), 125)

    def test_no_delivery_beyond_declared_horizon_or_future_capacity(self):
        for changes, reason in (({"commissioning_slots": (0,) * 4}, "future_commissioning_slots"),
                                ({"support_slots": (0,) * 4}, "future_support_slots"),
                                ({"system": replace(System(), commissioning_lead_months=4)}, "commissioning_outside_horizon")):
            r = run_monthly(plan(starts=(), opening_finished=1, **changes), cash())
            self.assertTrue(all(x["flows"]["shipped"] == 0 for x in r["months"]))
            self.assertEqual(next(e["reason"] for e in r["events"] if e["action"] == "ship"), reason)

    def test_output_demand_assignment_and_exact_rational_no_rounding(self):
        p = plan(operators=(Operator("incumbent", 1, (0, 0, 1000, 9)),),
                 system=replace(System(), full_output_units_per_robot_month=101))
        r = run_monthly(p, cash())
        self.assertEqual(value(output(r, 2)["accepted_output_units"]), Fraction(101, 4))
        self.assertEqual(value(output(r, 3)["ramped_capacity_units"]), 101)
        self.assertEqual(value(output(r, 3)["accepted_output_units"]), 9)
        self.assertTrue(all(type(i["face_cents"]) is int for i in r["closing_treasury"]["invoices"]))

    def test_idle_assigned_capacity_cannot_serve_another_operators_demand(self):
        p = plan(starts=(), operators=(Operator("incumbent", 0, (0,) * 4, 1),
                                      Operator("entrant", 0, (1000,) * 4)),
                 allocation_cycle=("incumbent", "entrant"))
        r = run_monthly(p, cash())
        for month in range(4):
            self.assertEqual(value(output(r, month)["ramped_capacity_units"]), 100)
            self.assertEqual(value(output(r, month)["accepted_output_units"]), 0)
            self.assertEqual(value(output(r, month, "entrant")["ramped_capacity_units"]), 0)
            self.assertEqual(value(output(r, month, "entrant")["accepted_output_units"]), 0)

    def test_collection_eligibility_and_no_automatic_start_retry(self):
        t = cash(0).issue_invoice("future", "receipt", "buyer", "provider", 5_000_000,
                                  Moment(0, 1), Moment(1, 2), Moment(1, 2), provenance="synthetic")
        before = t.snapshot()
        r = run_monthly(plan(collections=(Collection("receipt", 0),)), t)
        self.assertEqual(r["months"][0]["closing_cash_cents"]["provider"], 0)
        self.assertEqual(next(e["reason"] for e in r["events"] if e["action"] == "collect_opening_receivable"), "not_yet_eligible")
        self.assertEqual(r["units"], [])
        self.assertEqual(t.snapshot(), before)

    def test_minimum_reserve_is_not_deployment_funding(self):
        t = cash(4_000_000, 500_000)
        r = run_monthly(plan(), t)
        self.assertEqual(r["months"][0]["flows"]["started"], 0)
        self.assertEqual(r["months"][0]["components"]["closing"], 100)
        self.assertEqual(r["months"][0]["closing_cash_cents"]["provider"], 4_000_000)

    def test_actual_payments_match_every_admitted_physical_action(self):
        for r in self.witnesses.values():
            invoices = {i["invoice_id"]: i for i in r["closing_treasury"]["invoices"]}
            for e in r["events"]:
                if e["action"] not in ("existing_support", "commission", "ship", "start"):
                    continue
                i = invoices[e["invoice_id"]]
                self.assertLess((i["issued_at"]["month"], i["issued_at"]["phase"]),
                                (e["at"]["month"], e["at"]["phase"]))
                if e["status"] == "blocked":
                    self.assertEqual(i["paid_cents"], 0)
                else:
                    self.assertEqual(i["paid_cents"], i["face_cents"])
                    payments = [x for x in r["closing_treasury"]["events"]
                                if x["kind"] == "invoice_payment" and x["reference_id"] == i["invoice_id"]]
                    self.assertEqual(len(payments), 1)
                    self.assertEqual(payments[0]["at"], e["at"])

    def test_resource_cash_and_unit_conservation_under_adverse_matrix(self):
        for money in (0, 3_600_000, 10_000_000):
            for parts in (0, 2, 7):
                for accepted in (0, 1, 2):
                    with self.subTest(money=money, parts=parts, accepted=accepted):
                        r = run_monthly(plan(opening_components=parts, starts=(Start("batch", 0, 2, accepted),)), cash(money))
                        cumulative_starts = 0
                        for row in r["months"]:
                            c, f, a, z = row["components"], row["flows"], row["opening_stock"], row["closing_stock"]
                            cumulative_starts += f["started"]
                            self.assertEqual(c["opening"] + c["qualified_receipts"] - c["service_consumed"] - c["start_consumed"], c["closing"])
                            self.assertEqual(sum(z.values()), cumulative_starts)
                            self.assertEqual(z["wip"], a["wip"] + f["started"] - f["accepted"] - f["rejected"])
                            self.assertEqual(z["transit"], a["transit"] + f["shipped"] - f["commissioned"])
                            self.assertEqual(sum(row["closing_cash_cents"].values()), sum(row["opening_cash_cents"].values()))
                            self.assertTrue(all(x >= 0 for x in row["closing_cash_cents"].values()))
                            self.assertLessEqual(row["support"]["used"], row["support"]["slots"])
                        self.assertEqual(len({u["unit_id"] for u in r["units"]}), len(r["units"]))

    def test_input_validation_and_immutable_input_branches(self):
        t = cash()
        before = t.snapshot()
        invalid = [lambda: replace(System(), bundled_start_cents=True),
                   lambda: replace(System(), shipping_cents=1.5),
                   lambda: replace(System(), assembly_lead_months=0),
                   lambda: replace(System(), first_month_ramp_numerator=5),
                   lambda: Start("x", 0, 1, 2), lambda: Start("x", 0, 1.0, 1),
                   lambda: plan(qualified_component_receipts=(0,)),
                   lambda: plan(allocation_cycle=("missing",)),
                   lambda: plan(provider_actor="manufacturer"),
                   lambda: plan(starts=(Start("same", 0, 1, 1), Start("same", 1, 1, 1)))]
        for call in invalid:
            with self.assertRaises(ValueError):
                candidate = call()
                if isinstance(candidate, Plan):
                    run_monthly(candidate, t)
            self.assertEqual(t.snapshot(), before)
        p = plan()
        with self.assertRaises(FrozenInstanceError):
            p.months = 10
        run_monthly(p, t)
        run_monthly(replace(p, opening_components=0), t)
        self.assertEqual(t.snapshot(), before)

    def test_cli_matches_authoritative_function(self):
        completed = subprocess.run([sys.executable, "-m", "model.monthly_deployment"],
                                   check=True, capture_output=True, text=True)
        self.assertEqual(json.loads(completed.stdout), json.loads(json.dumps(self.witnesses)))


if __name__ == "__main__":
    unittest.main()
