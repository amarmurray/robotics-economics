from dataclasses import replace
import json
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from model.coordination_transactions import (
    DurableCoordinator, NaiveSubmitter, SimulatedCrash, SyntheticFleet, comparison,
)


class CoordinationTransactions(unittest.TestCase):
    def setUp(self):
        self.directory = TemporaryDirectory()
        self.path = Path(self.directory.name) / "business.sqlite"
        self.fleet = SyntheticFleet()
        self.client = DurableCoordinator(self.path, self.fleet)

    def tearDown(self):
        self.client.close()
        self.directory.cleanup()

    def reopen(self):
        self.client.close()
        self.client = DurableCoordinator(self.path, self.fleet)

    def test_acceptance_is_not_execution_or_business_output(self):
        row = self.client.submit("order", 2)
        self.assertEqual((row["status"], row["moved_units"], row["accepted_output"]), ("accepted", 0, 0))
        task_id = row["task_id"]
        self.fleet.advance(task_id)
        self.assertEqual(self.client.reconcile("order")["accepted_output"], 0)
        complete = self.fleet.advance(task_id)
        self.assertEqual(self.client.record("order")["accepted_output"], 0)
        self.assertEqual(self.client.observe(complete)["accepted_output"], 1)
        self.assertEqual(self.client.observe(complete)["accepted_output"], 1)
        with self.assertRaises(ValueError):
            self.client.observe(replace(complete, state="stopped"))

    def test_crash_between_external_acceptance_and_local_record(self):
        with self.assertRaises(SimulatedCrash):
            self.client.submit("order", 2, fault="after_accept_before_record")
        self.assertIsNone(self.client.record("order")["task_id"])
        self.assertEqual(len(self.fleet.tasks), 1)
        self.fleet.restart_dispatcher()
        self.reopen()
        self.client.submit("order", 2)  # Local persistence alone blocks; does not discover outcome.
        self.assertEqual(len(self.fleet.tasks), 1)
        row = self.client.reconcile("order")
        self.assertEqual(row["task_id"], "task-1")
        self.client.submit("order", 2)
        self.assertEqual(len(self.fleet.tasks), 1)

    def test_empty_lookup_is_not_final_when_original_delivery_is_pending(self):
        self.client.submit("order", 2, fault="delayed_acceptance")
        self.assertEqual(len(self.fleet.tasks), 0)
        self.fleet.restart_dispatcher()
        self.reopen()
        self.assertEqual(self.client.reconcile("order")["status"], "unknown")
        self.client.submit("order", 2)
        self.assertEqual(len(self.fleet.tasks), 0)
        self.fleet.deliver_pending("business:order")
        self.assertEqual(self.client.reconcile("order")["task_id"], "task-1")
        self.assertEqual(len(self.fleet.tasks), 1)

    def test_safe_retry_requires_authoritative_absence_and_no_inflight(self):
        with self.assertRaises(SimulatedCrash):
            self.client.submit("order", 2, fault="before_send")
        self.reopen()
        self.assertEqual(self.client.reconcile("order")["status"], "safe_to_retry")
        self.client.submit("order", 2)
        self.assertEqual(len(self.fleet.tasks), 1)

    def test_unavailable_lookup_blocks_despite_actual_completion(self):
        self.client.submit("order", 2, fault="lost_ack")
        self.fleet.advance("task-1", 2)
        self.fleet.lookup_available = False
        self.assertEqual(self.client.reconcile("order")["status"], "unknown")
        self.client.submit("order", 2)
        self.assertEqual(len(self.fleet.tasks), 1)
        self.assertEqual(self.client.record("order")["accepted_output"], 0)
        self.fleet.lookup_available = True
        self.assertEqual(self.client.reconcile("order")["accepted_output"], 1)

    def test_transport_cache_does_not_replace_business_idempotency(self):
        first = self.fleet.dispatch("wire", "order", 2)
        self.assertEqual(self.fleet.dispatch("wire", "order", 2), first)
        self.fleet.dispatch("other-a", "a", 1)
        self.fleet.dispatch("other-b", "b", 1)
        second = self.fleet.dispatch("wire", "order", 2)
        self.assertNotEqual(first, second)
        self.fleet.restart_dispatcher()
        third = self.fleet.dispatch("wire", "order", 2)
        self.assertEqual(len({first, second, third}), 3)

    def test_cancellation_preserves_partial_effects_and_waits_for_stop(self):
        task_id = self.client.submit("order", 3)["task_id"]
        queued = self.fleet.tasks[task_id]
        self.client.observe(self.fleet.advance(task_id))
        row = self.client.cancel("order")
        self.assertEqual(row["status"], "cancel_pending")
        self.assertEqual(self.fleet.tasks[task_id].state, "active")
        # A cancellation ack does not halt the executor: another effect can occur.
        self.client.observe(self.fleet.advance(task_id))
        self.assertEqual(self.client.record("order")["moved_units"], 2)
        stopped = self.fleet.confirm_stop(task_id)
        row = self.client.observe(stopped)
        self.assertEqual((row["status"], row["moved_units"], row["accepted_output"]), ("canceled", 2, 0))
        self.client.observe(queued)
        self.client.receive_acceptance("order", task_id)
        self.client.submit("order", 3)
        self.assertEqual(self.client.record("order")["status"], "canceled")
        self.assertEqual(len(self.fleet.tasks), 1)
        with self.assertRaises(ValueError):
            self.client.observe(replace(stopped, state="active", revision=stopped.revision + 1))
        with self.assertRaises(ValueError):
            self.client.observe(replace(stopped, moved_units=1, revision=stopped.revision + 1))

    def test_completion_racing_with_cancel_requires_business_review(self):
        task_id = self.client.submit("order", 2)["task_id"]
        self.client.observe(self.fleet.advance(task_id))
        self.client.cancel("order")
        self.fleet.advance(task_id)
        self.fleet.confirm_stop(task_id)  # Cannot reverse already complete work.
        row = self.client.reconcile("order")
        self.assertEqual((row["status"], row["moved_units"], row["accepted_output"]), ("needs_review", 2, 0))

    def test_key_payload_mismatch_and_ambiguous_matches_block(self):
        task_id = self.client.submit("order", 2)["task_id"]
        with self.assertRaises(ValueError):
            self.client.submit("order", 3)
        self.fleet.dispatch("outside-client", "order", 2)
        self.assertEqual(self.client.reconcile("order")["status"], "conflict")
        self.client.observe(self.fleet.advance(task_id, 2))
        self.assertEqual(self.client.record("order")["status"], "conflict")
        self.assertEqual(self.client.record("order")["accepted_output"], 0)
        with self.assertRaises(ValueError):
            self.client.cancel("order")
        self.fleet.lookup_available = False
        self.assertEqual(self.client.reconcile("order")["status"], "conflict")

    def test_wrong_task_feedback_and_incomplete_completion_rejected(self):
        task_id = self.client.submit("order", 2)["task_id"]
        queued = self.fleet.tasks[task_id]
        with self.assertRaises(ValueError):
            self.client.observe(replace(queued, task_id="other"))
        with self.assertRaises(ValueError):
            self.client.observe(replace(queued, state="completed", moved_units=1, revision=1))

    def test_new_duplicate_conflict_revokes_current_credit_not_past_trace(self):
        task_id = self.client.submit("order", 2)["task_id"]
        complete = self.fleet.advance(task_id, 2)
        self.assertEqual(self.client.observe(complete)["accepted_output"], 1)
        self.fleet.dispatch("external-duplicate", "order", 2)
        row = self.client.reconcile("order")
        self.assertEqual((row["status"], row["accepted_output"]), ("conflict", 0))
        self.client.observe(complete)
        self.assertEqual(self.client.record("order")["accepted_output"], 0)
        self.assertTrue(any(e.get("accepted_output") == 1 for e in self.fleet.trace))

    def test_fresh_unchanged_revision_resolves_transient_unknown(self):
        task_id = self.client.submit("order", 2)["task_id"]
        self.client.reconcile("order")
        for advance in (False, True):
            if advance:
                self.client.observe(self.fleet.advance(task_id))
            old = self.client.record("order")
            self.fleet.lookup_available = False
            self.assertEqual(self.client.reconcile("order")["status"], "unknown")
            self.fleet.lookup_available = True
            restored = self.client.reconcile("order")
            self.assertEqual(restored["status"], old["status"])
            self.assertEqual(restored["revision"], old["revision"])
            self.assertEqual(restored["accepted_output"], 0)

    def test_same_faults_expose_duplicate_effects_and_unknown_outcomes(self):
        result = comparison()
        self.assertEqual(result, json.loads(json.dumps(result, allow_nan=False)))
        self.assertEqual(result, comparison())
        for i in range(0, len(result["cases"]), 2):
            naive, durable = result["cases"][i:i + 2]
            self.assertEqual(naive["fault"], durable["fault"])
            self.assertEqual(naive["authoritative_lookup_available"], durable["authoritative_lookup_available"])
            self.assertEqual((naive["external_task_count"], naive["excess_effect_units"]), (2, 2))
            self.assertEqual((durable["external_task_count"], durable["excess_effect_units"]), (1, 0))
            self.assertIsNone(naive["accepted_business_outputs"])
            expected = 0 if durable["fault"] == "lookup_unavailable" else 1
            self.assertEqual(durable["accepted_business_outputs"], expected)
            self.assertEqual(durable["lookup_calls"], 2)


if __name__ == "__main__":
    unittest.main()
