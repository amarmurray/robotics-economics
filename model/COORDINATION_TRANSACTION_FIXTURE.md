# Local coordination transaction-state fixture

This is a deterministic, synthetic research fixture for [thesis T4](../THESIS_REGISTER.md). It tests the difference between submitting work, receiving acceptance, observing execution and reconciling a business record. It makes no network request, imports no RMF/ROS code and controls no robot. It is separate from the calibrated-evidence question and from the synthetic deployment engine.

The implementation is [coordination_transactions.py](coordination_transactions.py), with [invariant and fault tests](../tests/test_coordination_transactions.py). Both use Python's standard library. Run from the repository root:

```bash
python3 -m unittest discover -s tests -p test_coordination_transactions.py -v
python3 -m model.coordination_transactions > /tmp/coordination-transactions.json
```

The second command produces four policy pairs (eight dispatch-fault traces) and two cancellation traces. SQLite files are created in temporary directories and removed when each witness ends. There is no persistent service, deployment, credential, paid API or external state change. Sequence numbers are event order, not elapsed time.

## Research boundary

The [reviewed coordination packet](../research/coordination_reproducibility.md) establishes narrower source facts: RMF dispatch acceptance precedes execution; its response cache is bounded process memory; integrator callbacks supply execution feedback; cancellation acceptance is not observed stopping; and repeated web calls can receive new request IDs. Relevant records are HCR-E009 through HCR-E013. The pinned components were inspected separately and are not a verified installed release set.

This fixture implements an invented protocol inspired by those boundaries. It does **not** reproduce RMF code, message schemas, task allocation, callback timing, timeouts, ROS transport or the observed cache's exact eviction rule. Its capacity of two cache entries is an arbitrary small witness that makes eviction visible. Its integer work units are invented irreversible effects; they are not accepted deliveries, seconds, payroll, incident probabilities or robot throughput. No economic coefficient changes.

## Three stores and the critical gap

1. **External synthetic task truth:** `SyntheticFleet.tasks` records each accepted task, its requested payload, revision, progress and terminal state. This truth survives the mock dispatcher's restart.
2. **Volatile transport response cache:** a bounded FIFO maps request ID to task ID. It only avoids a repeated creation while that response remains cached. A new transport ID, eviction or restart can bypass it.
3. **Local business ledger:** `DurableCoordinator` commits a SQLite record keyed by business intent before crossing the dispatch boundary. It binds the key to the requested integer quantity and rejects reuse with a changed payload. Closing and reopening the SQLite connection preserves that record during the witness.

The ledger commits `uncertain` **before** dispatch. A crash after external acceptance but before local acknowledgment therefore leaves a persisted unknown outcome, not an empty record authorizing another submission. Local persistence cannot determine what happened remotely and is not an atomic distributed transaction.

Reconciliation has a strong, explicit additional assumption: a trusted external lookup can return **all** tasks for the business key, including terminal history, and can establish that no original request remains in flight. The reviewed RMF components do not establish this capability. Both comparison policies have the same mock external capability; the durable policy chooses to use it and pays two additional lookup operations in each paired trace. The fixture does not assign a price or duration to those operations.

If lookup is unavailable, the business state remains `unknown` and resend is blocked. If the original message is still pending, the lookup also returns unknown even though no task exists yet. An empty visible task list alone is not enough: a late original acceptance could otherwise race with a replacement. Only complete absence **and dispatch finality** produces `safe_to_retry`. Multiple matches, a different payload, or disappearance of an already known task produces `conflict`, which ordinary observations cannot clear. A real implementation lacking this authority must retain uncertainty or add an externally enforced business-idempotency/finality contract.

## State and acceptance rules

The normal local path is `prepared → uncertain → accepted → active → completed`. An acknowledgment alone can only reach `accepted`. `accepted_output` becomes one only when trusted executor completion reports all requested units and the same local transaction reconciles that business record. Repeating a completion observation does not add another output. It is current verified credit under these assumptions, not historical revenue or a field success measurement. Discovering a duplicate-task conflict revokes that current credit to zero pending manual review; earlier acceptance snapshots and irreversible effects remain in the trace.

Unknown dispatch outcomes are reconciled before retry. The local key is retained after completion or cancellation; the same key does not authorize a replacement business operation. A new generation, compensation or operator override requires a separate policy, which is not implemented here.

Cancellation persists intent and enters `cancel_pending`. A successful cancel acknowledgment does not stop the synthetic executor. Work may continue until a separate terminal observation. A stopped task retains the units already moved and becomes `canceled`; those effects are not rolled back. If completion races with the cancel request, the record becomes `needs_review` and receives no automatically accepted business output. The fixture does not choose whether the customer should accept, compensate or reverse that outcome.

Observations carry task identity, business key, quantity and monotonically increasing revision. Lower revisions are ignored; equal-revision contradictory state/effect values are rejected. A fresh, consistent authoritative observation can resolve a transient `unknown` even if the executor revision has not changed. Terminal state and effect quantities cannot regress under a newer revision. The fixture assumes feedback is authenticated and authoritative; an invented revision number is not a substitute for that trust in a deployment.

## Paired witnesses and their interpretation

Each pair receives the same two-unit order, cache capacity, fault and external lookup availability. The deliberately naive submitter resends without business-state reconciliation. It is a weak baseline, not a representation of every existing integration or a competitive evaluation of an LLM.

| Injected dispatch fault | Naive result | Durable-reconciliation result |
| --- | --- | --- |
| Acceptance acknowledgment lost; caller retries with a fresh request ID | Two tasks, four effect units | One task, two effect units, one reconciled business output |
| Lost acknowledgment followed by dispatcher/client restart | Two tasks despite the first acceptance | Persistent uncertainty, then one task found and reconciled |
| Response evicted; caller even reuses the original transport ID | Two tasks, showing transport-ID reuse alone is insufficient | Business-key reconciliation finds the original task |
| Lost acknowledgment, restart and unavailable authoritative lookup | Blind retry creates a second task | Resend blocked; one task executes but zero **verified local** business outputs are credited while its outcome remains unknown |

The first three durable traces remove two invented excess effect units under the declared lookup assumption. This is an exact result for constructed traces, not a failure-rate estimate, accepted-throughput gain, recovery-cost saving, real-time result or physical benchmark. The fourth trace exposes the availability tradeoff: preventing a duplicate does not establish completion or restore progress when authoritative reconciliation is unavailable. The comparator has no reconciled business ledger, so its accepted-business-output field is null rather than equating API acknowledgments to output.

Two additional cancellation traces preserve effects after acknowledgment: a three-unit task stops after two units, or completes all three before stopping can take effect. Their final states are respectively `canceled` and `needs_review`; neither automatically earns accepted business output. These are protocol witnesses, not claimed prevention of post-cancel physical effects.

## Verification and limits

Thirteen tests cover acceptance without output, the crash between remote acceptance and local recording, SQLite reopen, unavailable and restored lookup, late original arrival, final absence permitting retry, bounded-cache eviction/restart, changed payloads, multiple external matches and credit revocation, partial cancellation, completion racing with cancellation, stale/duplicate/conflicting observations, wrong task identity and incomplete completion. The paired outputs are deterministic and JSON-roundtrip clean.

The fixture serializes operations in one process. It does not test concurrent orchestrators, actual process kills or power loss, SQLite deployment durability settings, malicious feedback, storage corruption, task-history pruning, distributed transactions, authorization, reservations across sites, service deadlines or physical safety. External truth and pending-message knowledge are explicit cooperative mock assumptions. SQLite persistence is local only; an operator still needs a real external identity, query/finality and reconciliation contract.

The next falsification step is to replace the mock with **one** independently verified compatible installation and repeat the fault cases with its actual business-ID, pending-request, terminal-state and partial-effect contract. Until that separately authorized work exists, HCR-TEST-03's installed-system test remains unperformed. These local witnesses advance software reasoning within the research campaign; they do not activate a production prototype or establish digital/physical productivity value.
