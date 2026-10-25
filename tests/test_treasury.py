"""Exact settlement witnesses; monetary inputs below are cents unless usd()."""
from dataclasses import FrozenInstanceError, replace
from decimal import Decimal, localcontext
import json
import subprocess
import sys
import unittest

from model.treasury import Account, Credit, Event, Moment, Posting, Treasury, financial_witnesses, usd


P = {"provenance": "synthetic_test_contract"}
A, B, C = Moment(0, 1), Moment(0, 2), Moment(0, 3)


def ledger(cash=100, reserve=0, counterparty=0):
    return Treasury((Account("payer", cash, reserve), Account("payee", counterparty)))


def invoice(t, iid="A", amount=100, **terms):
    return t.issue_invoice("issue-" + iid, iid, "payer", "payee", amount, A, B, C, **P, **terms)


def facility(cash=100, limit=100, revolving=False):
    t = Treasury((Account("lender", cash), Account("borrower", 0), Account("supplier", 0)))
    return t.authorize_credit("authorize", "line", "lender", "borrower", limit,
                              A, B, Moment(2, 2), Moment(3, 3), revolving=revolving, **P)


class TreasuryTests(unittest.TestCase):
    def assertRejectedUnchanged(self, state, call):
        before = state.snapshot()
        with self.assertRaises((ValueError, FrozenInstanceError, TypeError)):
            call()
        self.assertEqual(state.snapshot(), before)
        self.assertTrue(state.audit())

    def test_exact_financial_witnesses_and_intermediate_balances(self):
        cases = financial_witnesses()
        def actor(name, who):
            return next(a for a in cases[name]["actors"] if a["actor_id"] == who)
        def balance_after(name, who, event_id):
            cash = actor(name, who)["opening_cash_cents"]
            for e in cases[name]["events"]:
                cash += sum(p["delta_cents"] for p in e["postings"] if p["actor_id"] == who)
                if e["event_id"] == event_id:
                    return cash
            self.fail("Missing event")
        no = "witness_1_unfunded"
        yes = "witness_1_funded_next_month"
        self.assertEqual(actor(no, "provider")["cash_cents"], usd("30000"))
        self.assertEqual(actor(no, "provider")["available_cents"], usd("20000"))
        self.assertEqual(cases[no]["events"][-1]["status"], "blocked")
        self.assertEqual(balance_after(yes, "provider", "pay-start"), usd("10000"))
        self.assertEqual(actor(yes, "provider")["cash_cents"], usd("50000"))
        self.assertEqual(cases[yes]["credits"][0]["drawn_cents"], usd("20000"))
        self.assertEqual(cases[yes]["credits"][0]["outstanding_cents"], 0)
        loss = "witness_2_start_costs_once"
        self.assertEqual(balance_after(loss, "provider", "cash-start-2"), usd("28000"))
        self.assertEqual(actor(loss, "provider")["cash_cents"], usd("88000"))
        deposit = "witness_3_restricted_deposit_refunded"
        self.assertEqual(balance_after(deposit, "provider", "place"), usd("50000"))
        self.assertEqual(balance_after(deposit, "customer", "place"), usd("10000"))
        self.assertEqual(actor(deposit, "provider")["cash_cents"], usd("30000"))
        self.assertEqual(actor(deposit, "customer")["cash_cents"], usd("30000"))
        default = "witness_5_unpaid_fee"
        self.assertEqual(actor(default, "entrant")["cash_cents"], usd("8000"))
        self.assertEqual(actor(default, "financier")["cash_cents"], 0)
        self.assertEqual(cases[default]["invoices"][0]["outstanding_cents"], usd("10000"))
        self.assertEqual(cases[default]["invoices"][0]["status"], "defaulted")
        earmark = "witness_7_earmark_consumed"
        self.assertEqual(actor(earmark, "payer")["cash_cents"], 0)
        self.assertEqual(actor(earmark, "payer")["reserved_cents"], 0)
        self.assertEqual(cases[earmark]["invoices"][1]["face_cents"], usd("1000"))
        for result in cases.values():
            self.assertEqual(sum(a["cash_cents"] for a in result["actors"]),
                             sum(a["opening_cash_cents"] for a in result["actors"]))
            for event in result["events"]:
                self.assertEqual(sum(p["delta_cents"] for p in event["postings"]), 0)
                self.assertTrue(event["provenance"])

    def test_future_receivable_is_not_cash(self):
        t = ledger(0, counterparty=100)
        t = t.issue_invoice("future", "sale", "payee", "payer", 100, A, Moment(1, 2), Moment(1, 3), **P)
        t = invoice(t)
        t = t.settle_invoice("early", "sale", B, **P)
        self.assertEqual(t.events[-1].reason, "not_yet_eligible")
        t = t.settle_invoice("cannot-spend", "A", C, **P)
        self.assertEqual(t.balance("payer"), 0)
        self.assertEqual(t.invoice("sale").outstanding_cents, 100)
        t = t.settle_invoice("collect", "sale", Moment(1, 2), **P)
        t = t.settle_invoice("pay", "A", Moment(1, 3), **P)
        self.assertEqual(t.invoice("A").outstanding_cents, 0)

    def test_own_reservation_settles_atomically_and_cannot_pay_another(self):
        t = invoice(invoice(ledger(), "A", 100), "B", 1)
        t = t.reserve_invoice("reserve", "r", "A", 100, B, **P)
        self.assertEqual(t.available("payer"), 0)
        blocked = t.settle_invoice("block", "B", C, **P)
        self.assertEqual(blocked.reserved("payer"), 100)
        paid = blocked.settle_invoice("pay", "A", C, **P)
        self.assertEqual((paid.balance("payer"), paid.reserved("payer")), (0, 0))
        self.assertEqual(paid.events[-1].reservation_uses, (("r", 100),))
        self.assertRejectedUnchanged(paid, lambda: paid.settle_invoice("repeat", "A", C, **P))
        self.assertRejectedUnchanged(paid, lambda: paid.release_reservation("repeat-release", "r", C, **P))

    def test_cancel_releases_only_unpaid_earmark_without_refunding_paid_cash(self):
        t = invoice(ledger(), policy="partial_allowed", cancellable=True)
        t = t.reserve_invoice("reserve", "r", "A", 100, B, **P)
        t = t.settle_invoice("part", "A", B, amount_cents=40, **P)
        self.assertEqual((t.balance("payer"), t.reserved("payer")), (60, 60))
        t = t.cancel_invoice("cancel", "A", C, **P)
        self.assertEqual((t.balance("payer"), t.available("payer")), (60, 60))
        self.assertEqual((t.invoice("A").paid_cents, t.invoice("A").cancelled_cents), (40, 60))
        self.assertRejectedUnchanged(t, lambda: t.cancel_invoice("cancel-twice", "A", C, **P))

    def test_release_preserves_obligation_and_cannot_overreserve(self):
        t = invoice(ledger())
        t = t.reserve_invoice("reserve", "r", "A", 100, B, **P)
        self.assertRejectedUnchanged(t, lambda: t.reserve_invoice("over", "r2", "A", 1, B, **P))
        t = t.release_reservation("release", "r", C, **P)
        self.assertEqual(t.available("payer"), 100)
        self.assertEqual(t.invoice("A").outstanding_cents, 100)
        self.assertRejectedUnchanged(t, lambda: t.cancel_invoice("cancel", "A", C, **P))

    def test_partial_and_full_or_nothing_preserve_minimum_reserve(self):
        for policy, paid in (("full_or_nothing", 0), ("partial_allowed", 70)):
            t = invoice(ledger(80, 10), policy=policy)
            t = t.settle_invoice("pay", "A", C, **P)
            self.assertEqual(t.invoice("A").paid_cents, paid)
            self.assertEqual(t.balance("payer"), 80 - paid)
            self.assertEqual(t.invoice_status("A"), "defaulted")
            self.assertEqual(t.balance("payee"), paid)

    def test_explicit_partial_request_is_partial_obligation(self):
        t = invoice(ledger(), policy="partial_allowed")
        t = t.settle_invoice("part", "A", C, amount_cents=10, **P)
        self.assertEqual(t.events[-1].status, "partial")
        self.assertEqual(t.invoice_status("A"), "defaulted")
        t = t.settle_invoice("rest", "A", C, **P)
        self.assertEqual(t.invoice_status("A"), "paid")

    def test_due_grace_and_historical_query_policy(self):
        t = invoice(ledger(0), grace_months=1)
        self.assertEqual(t.invoice_status("A"), "not_yet_payable")
        self.assertEqual(t.invoice_status("A", B), "payable_not_due")
        t = t.settle_invoice("miss", "A", C, **P)
        self.assertEqual(t.invoice_status("A"), "due")
        self.assertEqual(t.invoice_status("A", Moment(1, 3)), "due")
        self.assertEqual(t.invoice_status("A", Moment(1, 4)), "defaulted")
        self.assertRejectedUnchanged(t, lambda: t.invoice_status("A", A))

    def test_disjoint_deposit_reservation_and_minimum_restrictions(self):
        t = invoice(ledger(30, 10, 20), amount=40)
        t = t.place_deposit("deposit", "d", "payee", "payer", 20, B, Moment(1, 2), **P)
        self.assertEqual((t.balance("payer"), t.restricted("payer"), t.available("payer")), (50, 20, 20))
        blocked = t.reserve_invoice("reserve-too-much", "r", "A", 30, B, **P)
        self.assertEqual(blocked.events[-1].status, "blocked")
        self.assertEqual(blocked.reservations, ())
        t = t.reserve_invoice("reserve", "r", "A", 20, B, **P)
        t = t.refund_deposit("early-refund", "d", C, **P)
        self.assertEqual(t.events[-1].reason, "not_yet_eligible")
        t = t.refund_deposit("refund", "d", Moment(1, 2), amount_cents=5, **P)
        self.assertEqual((t.balance("payer"), t.restricted("payer"), t.reserved("payer")), (45, 15, 20))
        t = t.refund_deposit("refund-rest", "d", Moment(1, 2), **P)
        self.assertEqual((t.balance("payer"), t.restricted("payer")), (30, 0))
        self.assertRejectedUnchanged(t, lambda: t.refund_deposit("again", "d", Moment(1, 2), **P))

    def test_spendable_deposit_leaves_refund_liability_after_cash_spent(self):
        t = invoice(ledger(0, counterparty=100), amount=100)
        t = t.place_deposit("deposit", "d", "payee", "payer", 100, B, Moment(1, 2), restricted=False, **P)
        t = t.settle_invoice("spend", "A", C, **P)
        t = t.refund_deposit("refund", "d", Moment(1, 2), **P)
        self.assertEqual(t.events[-1].status, "blocked")
        self.assertEqual(t.deposit("d").outstanding_cents, 100)
        self.assertEqual(t.balance("payer"), 0)

    def test_unfunded_deposit_has_no_phantom_cash_or_liability(self):
        t = ledger(0)
        t = t.place_deposit("deposit", "d", "payer", "payee", 100, A, B, **P)
        self.assertEqual(t.events[-1].status, "blocked")
        self.assertEqual(t.deposits, ())
        self.assertEqual(t.balance("payee"), 0)

    def test_credit_commitment_not_cash_and_lender_must_fund(self):
        t = facility(cash=50, limit=100)
        self.assertEqual(t.balance("borrower"), 0)
        self.assertEqual(t.credit("line").undrawn_cents, 100)
        t = t.draw_credit("draw-too-much", "line", 100, B, **P)
        self.assertEqual(t.events[-1].reason, "lender_cash_insufficient")
        self.assertEqual(t.credit("line").drawn_cents, 0)
        t = t.draw_credit("draw", "line", 50, C, **P)
        self.assertEqual((t.balance("lender"), t.balance("borrower")), (0, 50))

    def test_revolving_only_reopens_after_actual_principal_repayment(self):
        for revolving, redraw in ((False, 0), (True, 40)):
            t = facility(revolving=revolving)
            t = t.draw_credit("draw", "line", 100, B, **P)
            t = t.draw_credit("exhausted", "line", 1, C, **P)
            self.assertEqual(t.events[-1].reason, "commitment_exhausted")
            t = t.repay_principal("repay", "line", 40, C, **P)
            self.assertEqual(t.credit("line").undrawn_cents, redraw)
            t = t.draw_credit("redraw", "line", 40, C, **P)
            self.assertEqual(t.credit("line").drawn_cents, 100 + redraw)
            self.assertEqual(t.credit("line").outstanding_cents, 60 + redraw)

    def test_credit_dates_purpose_and_no_automatic_interest_refinancing(self):
        t = facility()
        t = t.draw_credit("early", "line", 100, A, **P)
        self.assertEqual(t.events[-1].reason, "outside_draw_window")
        self.assertRejectedUnchanged(t, lambda: t.draw_credit("bad-purpose", "line", 1, B, purpose="dividend", **P))
        t = t.draw_credit("draw", "line", 100, B, **P)
        t = t.draw_credit("expired", "line", 1, Moment(3, 3), **P)
        self.assertEqual(t.events[-1].reason, "outside_draw_window")
        self.assertEqual(t.credit("line").outstanding_cents, 100)
        self.assertEqual(t.balance("borrower"), 100)
        t = t.repay_principal("late-principal", "line", 100, Moment(4, 3), **P)
        self.assertEqual(t.credit("line").outstanding_cents, 0)

    def test_failed_and_partial_repayment_do_not_reopen_unpaid_credit(self):
        t = facility(revolving=True)
        t = t.issue_invoice("issue-cost", "cost", "borrower", "supplier", 80, A, B, C, **P)
        t = t.draw_credit("draw", "line", 100, B, **P).settle_invoice("cost", "cost", C, **P)
        t = t.repay_principal("blocked", "line", 100, C, **P)
        self.assertEqual(t.credit("line").undrawn_cents, 0)
        t = t.repay_principal("partial", "line", 100, C, policy="partial_allowed", **P)
        self.assertEqual((t.credit("line").outstanding_cents, t.credit("line").undrawn_cents), (80, 20))
        self.assertRejectedUnchanged(t, lambda: t.repay_principal("overpay", "line", 81, C, **P))

    def test_money_is_finite_exact_nonnegative_and_context_independent(self):
        for value in (True, False, 1.0, float("nan"), float("inf"), -1, "NaN", "Infinity", "-1", "0.001"):
            with self.subTest(value=value), self.assertRaises(ValueError):
                usd(value)
        for value in (True, 1.0, float("nan"), -1, Decimal(1)):
            with self.subTest(cents=value), self.assertRaises(ValueError):
                Account("a", value)
        with localcontext() as context:
            context.prec = 3
            self.assertEqual(usd("123456789012345678901234567890.12"), 12345678901234567890123456789012)
        self.assertEqual(usd("0.01"), 1)
        self.assertEqual(usd(Decimal("1.20")), 120)

    def test_invalid_actions_leave_all_state_unchanged(self):
        t = invoice(ledger())
        calls = [
            lambda: t.settle_invoice("bad", "A", B, amount_cents=True, **P),
            lambda: t.settle_invoice("bad", "A", B, amount_cents=101, **P),
            lambda: t.settle_invoice("bad", "A", B, amount_cents=50, **P),
            lambda: t.settle_invoice("bad", "missing", B, **P),
            lambda: t.settle_invoice("issue-A", "A", B, **P),
            lambda: t.settle_invoice("bad", "A", B, provenance=""),
            lambda: t.reserve_invoice("bad", "r", "A", -1, B, **P),
        ]
        for call in calls:
            self.assertRejectedUnchanged(t, call)
        paid = t.settle_invoice("pay", "A", C, **P)
        self.assertRejectedUnchanged(paid, lambda: paid.issue_invoice("backdate", "B", "payer", "payee", 1, A, B, C, **P))

    def test_date_input_validation_and_equal_moment_events(self):
        for args in ((True, 1), (0, True), (-1, 1), (0, 0), (0, 8), (0.0, 1)):
            with self.assertRaises(ValueError):
                Moment(*args)
        t = ledger()
        self.assertRejectedUnchanged(t, lambda: t.issue_invoice("bad", "A", "payer", "payee", 1, A, A, C, **P))
        self.assertRejectedUnchanged(t, lambda: t.issue_invoice("bad", "A", "payer", "payee", 1, A, C, B, **P))
        t = invoice(invoice(t, "A", 50), "B", 50)
        t = t.settle_invoice("payA", "A", C, **P).settle_invoice("payB", "B", C, **P)
        self.assertEqual(t.balance("payer"), 0)

    def test_same_currency_single_legal_actor_and_self_transfer_rejection(self):
        with self.assertRaises(ValueError):
            Treasury((Account("a", 100, currency="USD"), Account("b", 0, currency="EUR")))
        with self.assertRaises(ValueError):
            Treasury((Account("a", 100), Account("a", 100)))
        roles = ["provider", "lessor"]
        t = Treasury((Account("a", 100, roles=roles), Account("b", 0)))
        roles.append("customer")
        self.assertEqual(t.account("a").roles, ("provider", "lessor"))
        self.assertEqual(t.balance("a"), 100)
        self.assertRejectedUnchanged(t, lambda: t.issue_invoice("self", "i", "a", "a", 10, A, B, C, **P))
        self.assertRejectedUnchanged(t, lambda: t.place_deposit("self", "d", "a", "a", 10, A, B, **P))
        self.assertRejectedUnchanged(t, lambda: t.authorize_credit("self", "c", "a", "a", 10, A, B, C, Moment(1, 3), **P))

    def test_immutable_nested_state_and_independent_snapshots(self):
        accounts = [Account("payer", 100), Account("payee", 0)]
        t = invoice(Treasury(accounts))
        accounts.clear()
        t = t.reserve_invoice("reserve", "r", "A", 100, B, **P).settle_invoice("pay", "A", C, **P)
        with self.assertRaises(FrozenInstanceError):
            t.events[-1].provenance = "edited"
        with self.assertRaises(FrozenInstanceError):
            t.events[-1].postings[0].delta_cents = 1
        with self.assertRaises(TypeError):
            t.events[-1].reservation_uses[0][1] = 0
        snapshot = t.snapshot()
        snapshot["events"][-1]["postings"][0]["delta_cents"] = 0
        self.assertEqual(t.events[-1].postings[0].delta_cents, -100)
        purposes = ["working_capital"]
        c = Credit("c", "l", "b", 100, A, B, C, Moment(1, 3), purposes=purposes)
        purposes.append("dividend")
        self.assertEqual(c.purposes, ("working_capital",))

    def test_audit_rejects_unbalanced_or_rewritten_financial_state(self):
        t = invoice(ledger()).settle_invoice("pay", "A", C, **P)
        self.assertRejectedUnchanged(t, lambda: replace(t, invoices=(replace(t.invoices[0], paid_cents=99),)))
        self.assertRejectedUnchanged(t, lambda: replace(t, events=t.events[:-1]))
        bad_event = Event("forged", C, "invoice_payment", "settled", "A", 1, 1,
                          "test", postings=(Posting("payer", -2), Posting("payee", 1)))
        self.assertRejectedUnchanged(t, lambda: replace(t, events=t.events + (bad_event,)))

    def test_cli_is_deterministic_json_from_same_authoritative_function(self):
        result = subprocess.run([sys.executable, "-m", "model.treasury"], check=True,
                                capture_output=True, text=True)
        self.assertEqual(json.loads(result.stdout), json.loads(json.dumps(financial_witnesses())))
        self.assertEqual(financial_witnesses(), financial_witnesses())


if __name__ == "__main__":
    unittest.main()
