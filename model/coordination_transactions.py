"""Local, synthetic transaction-state witnesses. No RMF, network or robot calls.

The extra authoritative lookup is an explicit fixture assumption, not an RMF
feature inferred from source inspection. Unknown external outcomes block retries.
"""
from collections import OrderedDict
from dataclasses import asdict, dataclass, replace
import json
from pathlib import Path
import sqlite3
from tempfile import TemporaryDirectory


class SimulatedCrash(RuntimeError):
    """Injected crash; already committed local/external state is retained."""


@dataclass(frozen=True)
class Observation:
    task_id: str
    business_key: str
    units: int
    state: str = "queued"
    moved_units: int = 0
    revision: int = 0
    cancel_requested: bool = False


def validate_order(key, units):
    if not isinstance(key, str) or not key:
        raise ValueError("A nonempty business key is required")
    if isinstance(units, bool) or not isinstance(units, int) or units <= 0:
        raise ValueError("Requested units must be a positive integer")


class SyntheticFleet:
    """Task truth survives dispatcher restart; its finite response cache does not.

    Methods change Python records only. Work units are invented irreversible
    effects, not deliveries, seconds, dollars or measured robot output.
    """

    def __init__(self, cache_capacity=2, lookup_available=True):
        if isinstance(cache_capacity, bool) or not isinstance(cache_capacity, int) or cache_capacity < 1:
            raise ValueError("Cache capacity must be a positive integer")
        self.cache_capacity = cache_capacity
        self.lookup_available = lookup_available
        self.cache = OrderedDict()
        self.tasks = {}
        self.pending = {}
        self.trace = []

    def event(self, kind, **details):
        self.trace.append({"sequence": len(self.trace), "event": kind, **details})

    def dispatch(self, request_id, key, units):
        validate_order(key, units)
        if not isinstance(request_id, str) or not request_id:
            raise ValueError("A nonempty transport request ID is required")
        if request_id in self.cache:
            task_id = self.cache[request_id]
            self.event("cached_acceptance", request_id=request_id, task_id=task_id)
            return task_id
        task_id = f"task-{len(self.tasks) + 1}"
        self.tasks[task_id] = Observation(task_id, key, units)
        self.cache[request_id] = task_id
        if len(self.cache) > self.cache_capacity:
            self.cache.popitem(last=False)
        self.event("dispatch_accepted", request_id=request_id, task_id=task_id,
                   business_key=key, accepted_output=False)
        return task_id

    def restart_dispatcher(self):
        self.cache.clear()
        self.event("dispatcher_restart_cache_lost")

    def defer_dispatch(self, request_id, key, units):
        """Hold delivery outside the dispatcher; it may arrive after a timeout."""
        validate_order(key, units)
        self.pending[request_id] = (key, units)
        self.event("request_in_flight", request_id=request_id, business_key=key)

    def deliver_pending(self, request_id):
        key, units = self.pending.pop(request_id)
        return self.dispatch(request_id, key, units)

    def lookup(self, key):
        known = self.lookup_available and not any(item[0] == key for item in self.pending.values())
        self.event("authoritative_lookup" if known else "lookup_unavailable",
                   business_key=key)
        if not known:
            return None
        # Strong explicit assumption: complete current history AND no outstanding
        # delivery for this key. An empty task list alone is NOT dispatch finality.
        return [task for task in self.tasks.values() if task.business_key == key]

    def advance(self, task_id, units=1):
        task = self.tasks[task_id]
        if task.state in {"completed", "stopped"}:
            raise ValueError("Terminal tasks cannot execute more work")
        if isinstance(units, bool) or not isinstance(units, int) or not 0 < units <= task.units - task.moved_units:
            raise ValueError("Invalid incremental work")
        moved = task.moved_units + units
        task = replace(task, moved_units=moved, revision=task.revision + 1,
                       state="completed" if moved == task.units else "active")
        self.tasks[task_id] = task
        self.event("synthetic_execution", **asdict(task))
        return task

    def cancel(self, task_id):
        task = self.tasks[task_id]
        accepted = task.state not in {"completed", "stopped"}
        if accepted:
            self.tasks[task_id] = replace(task, cancel_requested=True, revision=task.revision + 1)
        self.event("cancel_acknowledged", task_id=task_id, accepted=accepted,
                   observed_stopped=task.state == "stopped")
        return accepted

    def confirm_stop(self, task_id):
        task = self.tasks[task_id]
        if not task.cancel_requested:
            raise ValueError("Stop witness requires a cancellation request")
        if task.state != "completed":
            task = replace(task, state="stopped", revision=task.revision + 1)
            self.tasks[task_id] = task
        self.event("terminal_observation", **asdict(task))
        return task


class DurableCoordinator:
    """Single-writer SQLite ledger plus explicit external reconciliation.

    SQLite protects local writes only. It is NOT atomic with dispatch. A crash
    after send leaves 'uncertain'; an unavailable query never permits resend.
    """

    def __init__(self, path, fleet):
        self.fleet = fleet
        self.db = sqlite3.connect(path)
        self.db.row_factory = sqlite3.Row
        self.db.execute("""CREATE TABLE IF NOT EXISTS orders (
            business_key TEXT PRIMARY KEY, units INTEGER NOT NULL,
            status TEXT NOT NULL, task_id TEXT, external_state TEXT,
            revision INTEGER NOT NULL DEFAULT -1, moved_units INTEGER NOT NULL DEFAULT 0,
            cancel_requested INTEGER NOT NULL DEFAULT 0,
            accepted_output INTEGER NOT NULL DEFAULT 0)""")
        self.db.commit()

    def close(self):
        self.db.close()

    def record(self, key):
        row = self.db.execute("SELECT * FROM orders WHERE business_key=?", (key,)).fetchone()
        return dict(row) if row else None

    def _update(self, key, **fields):
        if fields.get("status") == "conflict":
            # Current verified credit is revoked; prior snapshots remain in trace.
            fields["accepted_output"] = 0
        with self.db:
            self.db.execute("UPDATE orders SET " + ",".join(f"{field}=?" for field in fields)
                            + " WHERE business_key=?", (*fields.values(), key))
        self.fleet.event("business_record", **self.record(key))
        return self.record(key)

    def submit(self, key, units, fault=None):
        validate_order(key, units)
        if fault not in {None, "before_send", "after_accept_before_record", "lost_ack", "delayed_acceptance"}:
            raise ValueError("Unknown injected fault")
        row = self.record(key)
        if row and row["units"] != units:
            raise ValueError("Business key reused with a different payload")
        if not row:
            with self.db:
                self.db.execute("INSERT INTO orders(business_key,units,status) VALUES(?,?,?)",
                                (key, units, "prepared"))
            row = self.record(key)
        if row["status"] not in {"prepared", "safe_to_retry"}:
            self.fleet.event("resend_blocked", business_key=key, status=row["status"])
            return row
        self._update(key, status="uncertain")  # COMMIT before the external boundary.
        if fault == "before_send":
            raise SimulatedCrash(fault)
        if fault == "delayed_acceptance":
            self.fleet.defer_dispatch("business:" + key, key, units)
            return self.record(key)
        task_id = self.fleet.dispatch("business:" + key, key, units)
        if fault == "after_accept_before_record":
            raise SimulatedCrash(fault)
        if fault == "lost_ack":
            self.fleet.event("acknowledgement_lost", business_key=key)
            return self.record(key)
        return self.receive_acceptance(key, task_id)

    def receive_acceptance(self, key, task_id):
        row = self.record(key)
        if row is None:
            raise ValueError("Unknown business key")
        if row["task_id"] and row["task_id"] != task_id:
            return self._update(key, status="conflict")
        # A delayed transport acknowledgment must not overwrite execution truth.
        if row["status"] not in {"uncertain", "unknown"}:
            return row
        return self._update(key, task_id=task_id, status="accepted")

    def reconcile(self, key):
        row = self.record(key)
        if row is None:
            raise ValueError("Unknown business key")
        if row["status"] == "conflict":
            return row  # Manual review is deliberately outside this fixture.
        matches = self.fleet.lookup(key)
        if matches is None:
            if row["external_state"] in {"completed", "stopped"}:
                return row
            return self._update(key, status="unknown")
        if not matches:
            # Known task disappearing contradicts the complete-history assumption.
            return self._update(key, status="conflict" if row["task_id"] else "safe_to_retry")
        if len(matches) != 1 or matches[0].units != row["units"]:
            return self._update(key, status="conflict")
        task = matches[0]
        if row["task_id"] and row["task_id"] != task.task_id:
            return self._update(key, status="conflict")
        self._update(key, task_id=task.task_id)
        return self.observe(task)

    def observe(self, observation):
        """Apply trusted mock executor feedback; authenticate it in a real system."""
        row = self.record(observation.business_key)
        validate_order(observation.business_key, observation.units)
        if not row or row["task_id"] != observation.task_id or row["units"] != observation.units:
            raise ValueError("Observation does not match the bound business task")
        if row["status"] == "conflict":
            return row  # A normal task update cannot clear a duplicate-task conflict.
        if any(isinstance(x, bool) or not isinstance(x, int) or x < 0
               for x in (observation.revision, observation.moved_units)):
            raise ValueError("Revision and work counters must be nonnegative integers")
        if observation.revision < row["revision"]:
            return row  # Delayed event, including an old queued state.
        if observation.revision == row["revision"]:
            if (observation.state, observation.moved_units) != (row["external_state"], row["moved_units"]):
                raise ValueError("Conflicting contents at the same executor revision")
            # Fresh authoritative knowledge can resolve transient 'unknown' even
            # when the executor has not advanced its revision. Credit is a flag.
        if observation.state not in {"queued", "active", "completed", "stopped"}:
            raise ValueError("Unknown executor state")
        if not row["moved_units"] <= observation.moved_units <= row["units"]:
            raise ValueError("Effects cannot disappear or exceed requested task work")
        if row["external_state"] in {"completed", "stopped"}:
            if observation.state != row["external_state"] or observation.moved_units != row["moved_units"]:
                raise ValueError("Terminal execution state cannot regress or change effects")
        if row["external_state"] == "active" and observation.state == "queued":
            raise ValueError("Execution cannot return to queued")
        if observation.state == "completed" and observation.moved_units != row["units"]:
            raise ValueError("Completion requires the full task effect")
        if observation.state == "queued" and observation.moved_units != 0:
            raise ValueError("Queued tasks have no execution effects")
        if observation.state == "active" and not 0 < observation.moved_units < row["units"]:
            raise ValueError("Active task must have partial work in this fixture")
        status = {"queued": "accepted", "active": "active", "stopped": "canceled",
                  "completed": "completed"}[observation.state]
        if row["cancel_requested"]:
            status = "needs_review" if observation.state == "completed" else (
                "canceled" if observation.state == "stopped" else "cancel_pending")
        return self._update(observation.business_key, status=status,
                            external_state=observation.state, revision=observation.revision,
                            moved_units=observation.moved_units,
                            accepted_output=int(status == "completed"))

    def cancel(self, key):
        row = self.record(key)
        if not row or not row["task_id"]:
            raise ValueError("Reconcile ambiguous dispatch before canceling")
        if row["status"] == "conflict":
            raise ValueError("Conflicting tasks require manual cancellation/reconciliation")
        if row["external_state"] in {"completed", "stopped"}:
            return row
        self._update(key, cancel_requested=1, status="cancel_pending")
        self.fleet.cancel(row["task_id"])
        return self.record(key)  # Ack alone is NOT an observed stop.


class NaiveSubmitter:
    """Deliberately weak comparator: resends without business-state reconciliation."""

    def __init__(self, fleet):
        self.fleet = fleet
        self.calls = 0

    def submit(self, key, units, request_id=None, lost_ack=False):
        self.calls += 1
        task_id = self.fleet.dispatch(request_id or f"naive-{self.calls}", key, units)
        return None if lost_ack else task_id


def run_witness(policy, fault):
    """Same invented order/fault/external capability for both client policies."""
    if policy not in {"naive", "durable"}:
        raise ValueError("Unknown policy")
    if fault not in {"lost_ack", "restart", "cache_eviction", "lookup_unavailable"}:
        raise ValueError("Unknown witness")
    fleet = SyntheticFleet(cache_capacity=2, lookup_available=fault != "lookup_unavailable")
    with TemporaryDirectory() as directory:
        path = Path(directory) / "orders.sqlite"
        coordinator = DurableCoordinator(path, fleet) if policy == "durable" else None
        naive = NaiveSubmitter(fleet)
        if coordinator:
            coordinator.submit("order-1", 2, fault="lost_ack")
        else:
            naive.submit("order-1", 2, request_id="business:order-1", lost_ack=True)
        if fault in {"restart", "lookup_unavailable"}:
            fleet.restart_dispatcher()
            fleet.event("client_restart")
            if coordinator:
                coordinator.close()
                coordinator = DurableCoordinator(path, fleet)
            else:
                naive = NaiveSubmitter(fleet)
        if fault == "cache_eviction":
            for i in range(2):
                fleet.dispatch(f"other-{i}", f"other-order-{i}", 1)
        if coordinator:
            coordinator.reconcile("order-1")
            coordinator.submit("order-1", 2)
        else:
            # Cache witness even reuses its transport ID; other retries use a fresh ID.
            naive.submit("order-1", 2, request_id="business:order-1" if fault == "cache_eviction" else None)
        targets = [task for task in fleet.tasks.values() if task.business_key == "order-1"]
        for task in targets:
            fleet.advance(task.task_id, 2)
        record = coordinator.reconcile("order-1") if coordinator else None
        result = {"policy": policy, "fault": fault,
                  "status": "synthetic_local_fault_witness_not_RMF_or_physical_validation",
                  "requested_units": 2, "external_task_count": len(targets),
                  "synthetic_effect_units": sum(fleet.tasks[t.task_id].moved_units for t in targets),
                  "excess_effect_units": sum(fleet.tasks[t.task_id].moved_units for t in targets) - 2,
                  "accepted_business_outputs": record["accepted_output"] if record else None,
                  "business_record": record, "authoritative_lookup_available": fleet.lookup_available,
                  "lookup_calls": sum(e["event"] in {"authoritative_lookup", "lookup_unavailable"} for e in fleet.trace),
                  "trace": fleet.trace}
        if coordinator:
            coordinator.close()
        return result


def comparison():
    return {"schema_version": "synthetic-coordination-witness/0.1",
            "calibration": "none; no timing, wage, throughput or incident-rate estimate",
            "naive_output_missing_reason": "Comparator has no reconciled business-output ledger; API acceptance is not counted as output.",
            "cases": [run_witness(policy, fault)
                      for fault in ("lost_ack", "restart", "cache_eviction", "lookup_unavailable")
                      for policy in ("naive", "durable")],
            "cancellation_cases": [cancellation_witness(race) for race in (False, True)]}


def cancellation_witness(complete_before_stop=False):
    """No prevention claim: effects can continue after the cancellation ack."""
    fleet = SyntheticFleet()
    with TemporaryDirectory() as directory:
        client = DurableCoordinator(Path(directory) / "orders.sqlite", fleet)
        task_id = client.submit("cancel-order", 3)["task_id"]
        old_queued = fleet.tasks[task_id]
        client.observe(fleet.advance(task_id))
        after_ack = client.cancel("cancel-order")
        client.observe(fleet.advance(task_id))
        if complete_before_stop:
            fleet.advance(task_id)
        client.observe(fleet.confirm_stop(task_id))
        client.observe(old_queued)
        result = {"complete_before_stop": complete_before_stop,
                  "after_cancel_ack": after_ack, "final_record": client.record("cancel-order"),
                  "trace": fleet.trace}
        client.close()
        return result


if __name__ == "__main__":
    print(json.dumps(comparison(), indent=2, allow_nan=False))
