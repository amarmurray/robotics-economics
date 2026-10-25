# Independent review: coordination reproducibility

Reviewed on 25 October 2026. Scope: [coordination chapter](../research/coordination_reproducibility.md) and [structured evidence and reconstructed rows](../data/coordination_reproducibility.json). This review concerns source accounting, reproducibility and interface semantics. It does not rerun a benchmark, execute ROS, verify a physical installation or calibrate an economic model. The author retains ownership of the reviewed files.

## Disposition

Accept the bounded investigation after the source and wording corrections below. The TAC reconstruction is independently reproducible from the published rows, Astranomy's disclosed configuration has material boundaries that the chapter preserves, and the RMF claims are supported as separately pinned interface implementations. No evidence here establishes a compatible installed stack, end-to-end business transaction, physical productivity gain or full cost per accepted business service.

Primary sources were retrieved on 25 October 2026 through the GitHub connector, Exa full-page retrieval and direct public-source retrieval for raw HTML, compressed traces and a redirected API endpoint. A read-only second reviewer checked the RMF source paths and release metadata. Downloaded Python/robot code was inspected as text, not executed.

## TheAgentCompany accounting and harness

The [archived run README](https://github.com/TheAgentCompany/experiments/blob/8cc10953909b88b2aa856b05134c344b505e5fcd/evaluation/1.0.0/20250510_OpenHands-0.28.1-gemini-2.5-pro/README.md) contains 175 task rows. This reviewer parsed the source independently and compared every task ID, maximum/earned checkpoint count, call count, displayed cost and perfect-completion indicator with the saved JSON: **all 175 rows match exactly**. The retrieved report hash also matches `dd989928d67a2b9b42a4e0872b520958821ef718e0b22183b88224b69841ad71`.

| Reconstructed source quantity | Independent result |
| --- | ---: |
| Perfect completions | 53 of 175 |
| Total displayed agent cost | $740.34 |
| Perfect-task subset cost | $80.85 |
| Non-perfect-task subset cost | $659.49 across 122 tasks |
| Total cost / perfect completions | $13.9686792453 |
| Total displayed cost / evaluated tasks | $4.2305142857 |
| Mean recorded calls | 27.2342857143 |

The stated $0.875 aggregate rounding bound follows from 175 × $0.005, conditional on ordinary nearest-cent row rounding. This is a rounding bound, not uncertainty about complete program costs. The distinction between non-perfect and worthless is preserved: non-perfect tasks can earn partial credit, and the benchmark tasks are not interchangeable services.

The [pinned summarizer](https://github.com/TheAgentCompany/TheAgentCompany/blob/98b68ef82a47690c316f42fddb05baafaab56851/evaluation/summarise_results.py) suppresses consecutive repeats of a model-response ID, prices its recorded usage without a cache discount, and averages over trajectories rather than successful tasks. This source version is later than the run and is correctly labeled that way. Its Gemini branch uses a per-response 200,000-input-token threshold. It does not establish actual invoices, whether runtime caching occurred, or the costs of external NPC/evaluator processes and infrastructure failures.

The two published compressed traces were independently retrieved, decompressed and parsed without running the agent. Both compressed SHA-256 values match the package. The model ID is `gemini-2.5-pro-preview-05-06` in both. Consecutive-response counting and global unique-response counting agree for these two traces:

| Selected task | Calls | Repriced cost | First-to-last event span |
| --- | ---: | ---: | ---: |
| `pm-create-plane-issue` | 8 | $0.21672 | 40.481206 seconds |
| `sde-close-all-prs` | 100 | $95.91578 | 1,285.5539 seconds |

These match the stored values and rounded README costs. This is two purposively selected traces, not a full-suite raw-token replay or a latency-distribution estimate. The [runner documentation](https://github.com/TheAgentCompany/TheAgentCompany/blob/98b68ef82a47690c316f42fddb05baafaab56851/evaluation/README.md) explicitly permits skipping errors and resuming; a complete set of evaluated task rows does not account for every earlier failed infrastructure attempt.

**Moderate correction: declared harness patch.** The README's Details section specifies OpenHands CodeAct PyPI release 0.28.1 **with a cherry-pick of PR 7679**. The original chapter's plain version omitted that material reproducibility fact. The [PR](https://github.com/OpenHands/OpenHands/pull/7679), titled “Fix cached tokens,” merged on 3 April 2025 at commit `d7f651a06c231fac1448c0c4a3ffd92c8be682c6`; its description handles `None` for cached tokens. The correction preserves this as the report's declared patch, not proof of the exact executed tree or an explanation of the budget discrepancy.

The historical [candidate runner](https://github.com/TheAgentCompany/TheAgentCompany/blob/3a1777e23eec4c075ab095b5a814634b843db031/evaluation/run_eval.py) and its dependency file support 100 iterations, configured budget value 4, OpenHands 0.28.1, a no-op condenser and separate 300/900/600-second sandbox/initialization/grading limits. They do not prove the precise executed configuration or a four-dollar ceiling under the retrospective no-cache price calculation. The $95.92 sampled cost demonstrates the mismatch, but it does not identify its cause. The chapter appropriately leaves runtime enforcement, actual price tracking, overrides and image digests unresolved. The paper's v3 date, 10 September 2025, was independently checked against the arXiv submission history; it is distinct from the May run.

## Astranomy configuration and disclosure boundary

The [report](https://research.nvidia.com/labs/srl/projects/astranomy/) was independently fetched as 1,265,231 raw HTML bytes; its hash exactly matches `087ea1e189899e73b742922f4be463eee0e60204b919f8e89e53618e503271d4`. The raw HTML contains both the immutable RoboLab task-source link and the unpinned NVIDIA GitLab policy-code link described by the chapter. The author's recorded HTTP 403 is a session retrieval result; this review does not infer that no other reader has access.

The final configuration table explicitly gives Direct Policy **3–15-action chunks on 90 tasks and historical 1–15 chunks on 30 tasks**. It also supports the distinct Agentic 1–5-step target hold, persistent history, retained planning/motion feedback, disabled optional tools, and Orchestrated 15-step review horizon. Section 2 supports medium reasoning, three 384 × 216 views, five fixed seeds per task, the 8,192-completion-token per-call limit, paused 15 Hz simulation, and no walltime/retry ceiling. These are distinct limits and cohorts; they must not be collapsed into one uniform real-time test.

Figure 24 and the full token table explicitly condition costs on successful episodes. The Agentic row reports 449 successes, 447 usage-covered successes and $36.40 mean cost. The timing section also conditions its inference/duration analysis on successful episodes. The chapter correctly declines to infer all-attempt cost from this conditional mean or compare it directly with TAC's all-instance mean. The limitations section explicitly says statistical significance of configuration differences has not been established.

The pinned public RoboLab files support `max_steps = env.max_episode_length`, task-supplied `episode_length_s`, and 120 simulated seconds in `FoodPackingByColorTask`. This verifies a task/configuration mechanism, not the private policy harness or its executed overrides. A public task-source pin, prompt displays and rollout examples provide partial disclosure; they do not establish a reproducible complete run. The negative finding about absent complete failed-episode usage remains bounded to the author's inspected report/assets. No exhaustive claim about all possible public or private data is accepted.

## Open-RMF authority, cancellation and retry semantics

The read-only source check supports HCR-E009–013 at the stated revisions and separately verifies the component version/date metadata. The chapter explicitly avoids certifying compatibility between the newer core/schema components and the older web release.

| Source path | Supported interpretation |
| --- | --- |
| `Dispatcher.cpp` request handler | Queues a bid notice and returns success before assignment or physical completion. Queued state and later dispatch status are different from accepted physical output. |
| Dispatcher `ApiMemory` | In-process request-ID cache with `_max_size = 50`; no durable business idempotency ledger is shown. The pre-insert `> 50` eviction test can leave 51 distinct entries, so 50 is correctly labeled a sizing field rather than a strict observed count. |
| Lingering-command publication | Re-publication and ten-second expiration concern unacknowledged dispatch commands, not a physical service deadline. |
| Fleet/EasyFullControl headers | Feasibility and admission callbacks precede integrator navigation/stop/action responsibilities. Defaults vary by API layer. `finished()` is integrator-provided completion feedback, not a model's declaration. |
| TaskManager cancellation | An active task's cancel method is invoked and the handler can return success without observing physical stopping or business rollback. If cancellation is not accepted in the inspected path, the handler sends no response; an explicit negative acknowledgment is not guaranteed. |
| Web bridge and task route | Each call creates a fresh UUID, publishes over ROS and waits by default five seconds. The route stores task/request state after success and has a user dependency; actual business authorization remains installation-specific. |

The timeout/retry consequence is a defensible code-derived hypothesis: a request may have taken effect before the caller times out, and a new call has a new ROS ID, so the dispatcher cache alone cannot deduplicate the business operation. It is not an observed incident or a completed fault-injection test. Cancellation acceptance likewise does not reverse already moved goods, release business reservations safely or establish safety-rated stopping.

## Corrected packaging and retained gaps

The author removed the observed campaign launch revision from published prose/metadata in favor of the operational-receipt pointer, while retaining reproducibility-critical **source** commit pins. Human-facing JSON spacing and cancellation failure wording were corrected. These packaging changes do not alter the independently reproduced numerical table.

The corrected package adds HCR-E014 for the declared OpenHands patch. Final recheck covered 14 evidence records and the unchanged 175-row source reconstruction. The reviewed narrative SHA-256 is `25a8ab99517124baadbc0f2dd100c677405f26321672fcbc3d188e2f2f2fe533`; the evidence-package SHA-256 is `20608051f57646b4d02294043461b7dff5502be9ed15ad1195ee3f2d2d721264`.

### Offline arithmetic helper

The lead subsequently added `tac_cost_summary` in [model/research_calculations.py](../model/research_calculations.py). This reviewer inspected its implementation and ran all four tests in `test_research_calculations.py`, which passed. An independent constructed case with one perfect, one partial and one zero-score task verified that all $11 of cost remain in the numerator while only one perfect task supplies the denominator; $9 of non-perfect cost is retained. The helper derives perfect completion from checkpoint scores and rejects disagreement with the supplied flag. Decimal accumulation reproduces the source totals; the rounding bound is row count × $0.005 under the explicit nearest-cent assumption.

Additional bounded checks verified null cost per perfect completion when no task is perfect, null non-perfect cost fraction when total cost is zero, and rejection of negative/nonfinite/Boolean costs, impossible scores, a false success flag and a stale saved total. The result explicitly leaves full business cost null with a reason. No source formula string is executed and no benchmark number is installed as a scenario coefficient. The field-support portion of the shared helper is outside this source review; passing its included test is not an additional independent field-source audit.

The remaining priority is concrete: obtain the executed TAC manifest and complete attempt ledger; obtain Astranomy's immutable policy/model configuration and failed-episode usage; or test one compatible RMF installation with business-ID preservation, timeout-after-acceptance, process restart, late response and cancellation after partial execution. Until then, accepted physical output, whole-service elapsed time, full cost and measured incremental LLM benefit remain unverified. This review accepts the source investigation and its proposed tests, not those unperformed tests or the entire coordination stack.
