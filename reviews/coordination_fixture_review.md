# Independent review: local coordination transaction fixture

Reviewed 25 October 2026. Disposition: **accepted as a bounded synthetic software witness after three corrections**. No remaining publication blocker was found within the declared assumptions. This is a historical review of the content hashes below, not validation of an installed RMF system or a distributed exactly-once guarantee.

## Scope and inspected snapshot

The review covered [the implementation](../model/coordination_transactions.py), [its tests](../tests/test_coordination_transactions.py), and [the fixture explanation](../model/COORDINATION_TRANSACTION_FIXTURE.md), against T4 in [the thesis register](../THESIS_REGISTER.md) and HCR-E009 through HCR-E013 in [the coordination source audit](../research/coordination_reproducibility.md). The reviewer did not edit the implementation, tests, source evidence or economic model. Repository launch metadata remains in ignored `sync_receipt.json`.

| Artifact | Reviewed SHA-256 |
| --- | --- |
| `model/coordination_transactions.py` | `b7b6e38b54ee0c5e3a1e3103fa67b8f87e7141dd42cb95e53477130650d4e9d4` |
| `tests/test_coordination_transactions.py` | `b0dbe69d0e9236757bf83c24d42a895196a4df9db4d9ae88fc5102ded9d55793` |
| `model/COORDINATION_TRANSACTION_FIXTURE.md` | `385961b46787ef8403281c9a5505cec6ed3fd637a73b65f9b2172b7ffdbf5776` |

The requested specialist model designation is not independently observable from this execution environment. This review establishes the code inspection and executions described below, not verification of a particular serving model or reasoning configuration.

## Corrected findings

| Severity | Finding and consequence | Correction and independent disposition |
| --- | --- | --- |
| Medium | A duplicate-task `conflict` could be overwritten during unavailable lookup or cancellation. Subsequent ordinary reconciliation could then clear a condition documented as requiring manual review. The root reviewer and owner also identified this state-guard problem. | `reconcile()` now returns an existing conflict before lookup; `cancel()` rejects it; `observe()` preserves it. Independently checked persistence through unavailable lookup, a contradictory empty history, a later completion observation and attempted cancellation. Resubmission remains blocked. |
| Medium | A completed order credited one accepted output; discovery of a second external task changed its state to `conflict` while silently retaining that credit. The intended accounting policy was unspecified. | `_update()` centrally revokes current `accepted_output` when entering conflict. Documentation distinguishes current verified credit from historical trace snapshots and irreversible external effects. Independently reproduced completed/one-credit to conflict/zero-credit. The effect counter remains unchanged. |
| Medium | A queued task at revision zero became `unknown` during unavailable lookup. Restoring an identical authoritative observation left it unknown because the equal-revision branch returned early. | Consistent equal-revision observations now re-derive the business state; conflicting contents still fail and older revisions remain ignored. Independently reproduced `accepted → unknown → accepted` with revision zero throughout. |

The latter two findings were directly reproduced on the intermediate implementation and rechecked after the owner added regression coverage. The conflict-latch correction was independently challenged after its guard was added. These are resolved findings, not remaining defects in the reviewed snapshot.

## Independent execution and adversarial checks

`python -m unittest tests.test_coordination_transactions -q` passed all **13 tests**. An additional reviewer-owned script, retained only at ignored `work/review_coordination_fixture.py`, exercised seven cases:

1. A duplicate-task conflict remains latched through lookup loss, attempted cancellation and later completion feedback; current credit stays zero.
2. A duplicate discovered after completed-business credit revokes that credit without erasing recorded work.
3. Restored authoritative knowledge resolves transient uncertainty without requiring a new executor revision.
4. After a conflict, even a deliberately contradictory empty external history does not authorize resubmission. Clearing the mock's history here intentionally violates its ordinary complete-history assumption to challenge the latch.
5. A modified mock executes all requested work **before dispatch returns**, followed by the injected crash before local acknowledgment recording. SQLite reopen and cache restart leave persisted uncertainty; unavailable lookup blocks retry. Restored authoritative lookup recovers the single completed task and credits one output. This probes external effect before the local acknowledgment log, beyond acceptance alone.
6. An original message remains pending while the visible task set is empty. Reopen and dispatcher restart do not authorize replacement: reconciliation stays unknown and submission is blocked. Delivering the original later creates exactly one task in this trace.
7. Partial work continues after cancellation acknowledgment, then stops. Stale queued feedback and a delayed acknowledgment do not undo the canceled state or its two recorded effect units. Reopen preserves that result; equal-revision contradictions, newer terminal regressions and attempts to erase effects are rejected.

Two independent CLI executions of `python -m model.coordination_transactions` produced equal, valid JSON: **eight dispatch traces and two cancellation traces**. For each of four matched fault conditions, the naive policy produced two tasks and four invented effect units; the durable policy produced one task and two units. The durable policy credited one verified output in the first three conditions and zero when authoritative lookup was unavailable. The naive policy's business-output value is appropriately null. Each durable case used two additional lookup operations, whose duration and cost remain unpriced.

The cancellation witnesses ended at `canceled` with two of three effect units, or `needs_review` with all three units after completion raced with cancellation. Both credited zero automatic business outputs. These results support the stated distinction between accepting a cancel request and observing its outcome; they do not demonstrate prevention or reversal of physical effects.

## Critical assumptions and claim boundary

The durable local journal establishes intent and remembered uncertainty. A business key plus that journal does **not** establish exactly-once external effect. Recovery additionally relies on a cooperative, authoritative lookup that returns every task for the key, retains terminal history, and establishes **dispatch finality**: no original request can still arrive after absence is declared. The pending-original probe directly tests why an empty visible task list is insufficient. Only complete absence with that finality permits `safe_to_retry`; unknown remains blocked. Production systems would need an enforceable external identity/finality contract or continued uncertainty. Neither the fixture nor the inspected RMF components supplies proof that such a deployment contract exists.

Both comparison policies receive the same order, external capabilities, cache size, fault and lookup availability. The naive policy deliberately declines reconciliation. Consequently the comparison isolates a constructed policy choice against a weak baseline; it does not establish superiority to existing integrations, an LLM's contribution, an empirical incident rate or a physical productivity effect. The two-entry FIFO is an invented cache witness rather than a claim to reproduce RMF's cache implementation.

The fixture and documentation preserve the source boundary: dispatch acceptance is distinct from execution; transport caching is finite and volatile; timeout does not imply no external effect; cancellation acknowledgment does not establish stopping; and feedback authority must come from the integration. No RMF/ROS import, installed compatible stack, network action, robot execution, economic coefficient change or measured physical performance was involved.

Actual process killing, power loss, concurrent writers, deployment-grade SQLite durability, authenticated hostile feedback, history pruning and a real executor's partial-effect contract remain untested. The injected exception plus connection reopen is a useful local state test, not validation of those stronger failure modes. Manual resolution of conflicts and compensation are intentionally outside the implementation.

## Stopping condition and next falsification step

This bounded review is sufficient for publishing the local witness alongside the continuing research campaign. Additional synthetic cases would not establish the missing external authority. The next material test is one independently verified compatible installation with a documented business-key, pending-request/finality, terminal-history and partial-effect contract, followed by the same delayed-original and crash-after-effect probes. That installed-system work remains unperformed and requires its own scope; this review does not activate it or close the physical coordination thesis.
