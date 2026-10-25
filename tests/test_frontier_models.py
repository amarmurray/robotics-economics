"""Conserve source boundaries across the intelligence-layer evidence packet."""
import copy
import json
import unittest
from model.frontier_models import ROOT, PACKAGE, validate_packet, acquisition_reconciliation, frontier_model_summary


class FrontierEvidence(unittest.TestCase):
    def setUp(self):
        self.packet = json.loads((ROOT/PACKAGE).read_text())

    def test_filing_components_reconcile_without_calling_noncash_cash(self):
        r = acquisition_reconciliation(self.packet)
        self.assertEqual((r["cash_consideration"], r["equity_fair_value"], r["escrow_fair_value"]), (9, 9, 2))
        self.assertEqual((r["total_consideration"], r["net_assets_sold"], r["seller_gain"]), (20, 15, 5))
        self.assertEqual((r["completion_date"], r["announcement_date"]), ("2026-03-27", "2026-04-15"))
        self.assertTrue(all(r["checks"].values()))

    def test_missing_mixed_unit_and_inconsistent_amounts_fail(self):
        for change in ({"value": None}, {"value": True}, {"unit": "USD"}, {"value": 20}, {"value": float("nan")}):
            packet = copy.deepcopy(self.packet)
            q = next(e for e in packet["evidence"] if e["evidence_id"] == "K-E006")["quantities"][0]
            q.update(change)
            with self.assertRaises(ValueError):
                acquisition_reconciliation(packet)

    def test_rights_conflict_cannot_turn_into_blanket_clearance(self):
        card = next(r for r in self.packet["model_rights_cards"] if r["artifact_id"] == "K-R-VLA-WEIGHTS")
        self.assertEqual(card["rights_status"], "conflicting")
        self.assertFalse(card["commercial_use_resolved"])
        card["commercial_use_resolved"] = True
        with self.assertRaisesRegex(ValueError, "rights"):
            validate_packet(self.packet)

    def test_unpriced_architecture_cannot_import_a_vendor_score_as_cost(self):
        self.packet["architecture_alternatives"][0]["annual_resource_cost_usd"] = 56
        with self.assertRaisesRegex(ValueError, "Unpriced"):
            validate_packet(self.packet)

    def test_source_identity_joins_reject_duplicates_and_missing_actors(self):
        validate_packet(self.packet)
        self.packet["model_labs"].append(self.packet["model_labs"][0])
        with self.assertRaisesRegex(ValueError, "Duplicate"):
            validate_packet(self.packet)
        self.packet["model_labs"].pop()
        self.packet["frontier_models"][0]["actor_id"] = "unresolved"
        with self.assertRaisesRegex(ValueError, "actor"):
            validate_packet(self.packet)

    def test_summary_keeps_run_rate_recognition_and_comparison_limits(self):
        summary = frontier_model_summary(packet=self.packet)
        q = {q["quantity_id"]: q for q in summary["skild_issuer_reported_quantities"]}
        self.assertEqual(q["K-Q-SKILD-ARR"]["unit"], "USD per year")
        self.assertIsNone(q["K-Q-SKILD-ARR"]["value"])
        self.assertEqual(q["K-Q-SKILD-RECOGNIZED"]["unit"], "USD")
        self.assertFalse(summary["scenario_inputs_used"])
        self.assertFalse(summary["architecture_costs_available"])
        self.assertFalse(summary["model_benchmark_ranking_available"])


if __name__ == "__main__":
    unittest.main()
