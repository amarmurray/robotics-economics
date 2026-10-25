# Independent review: annual digital trajectory design

Reviewed 25 October 2026. **Pass for the proposed bounded implementation stage; no required design correction remains.** This accepts an implementation contract and independently reproduced point witnesses. It does not establish that a trajectory runner exists, that an end-to-end trajectory test has passed, or that any coefficient is calibrated.

The inspected [design](../research/digital_trajectory_design.md) has SHA-256 `142ca7bfb5b478f2ef1885700b6809720cb0c8232cb22e4fd44206ec9eb5d16f`. Its numerical compatibility baseline is corrected model **0.1.1**, engine SHA-256 `0c35c6f2602d29a60a6bc187c013c0e4dd9a3597064cf67bed5a1ecc616a8d07`. The separately accepted [high-memory correction](high_memory_cost_review.md) establishes equal configured hardware costs in C10 and C11. Repository session identifiers remain in ignored `sync_receipt.json`.

## Separation of mechanisms and accounting

The three proposed level paths have distinct meanings: human time per accepted unit, incremental robot coordination capacity, and additional robot digital-service expense. The last is a bundled annual service cost at a fixed usage/quality boundary, **not an inference price per token**. The fixed $600 site software charge remains common to C01 and C11. Separate inference usage, failed attempts, latency and human-license pricing remain outside this stage; the design therefore meets a narrower cost-path objective rather than a complete inference-economics model.

The four-way equations match the inspected shared functions. Human efficiency applies to the full human comparator and only retained human work in C11; it does not independently increase robot capability. Coordination changes robot capacity before the site-demand cap without reducing support or power automatically. A cheaper service does not improve competence directly. Required embedded control remains in C10, so that branch is not a robot without digital technology.

The design preserves `joint_saving = digital_alone + robot_alone − cost_interaction` and adds no separate synergy credit. Its proposed annual reference uses the same exogenous capability in both robot branches, with no learned increment. That is appropriately distinct from the fleet's funded, exposure-dependent learning and divergent deployment history. Adoption-mediated exposure effects can occur in a rerun, but neither an extra data premium nor a second learning saving is added. Annual matched-site cost contrasts are not labeled realized fleet savings.

The strong orchestration comparator is also appropriate: the same digitally improved human process and configured robot, with no incremental coordination or robot service bundle beyond the required base stack. C10 alone would confound the absence of human digital improvement with the incremental orchestration intervention. A real alternative scheduler's incremental costs would still need their own explicit terms.

## Does adoption use the moving comparator?

The reviewer inspected `operation()`, `matched_economics()`, `eligible_sites()`, `fleet_model()`, `joint_comparisons()` and `run_scenario()` in the baseline engine, plus its methods and existing tests. The design explicitly requires one resolved `p_t` in the savings ranking, economic eligibility, stored economics, operation/output, released human hours and current economic flags used for manufacturing demand. This is the necessary propagation; changing only the annual comparison display would fail the design.

Customer screening must use robot-covered work valued at that year's `h*(1-d[t])`, rather than a frozen original human comparator. At the same time, additive activity remains in fixed baseline-equivalent hours. Price transfers remain separate from consolidated resource cost, payroll removed remains unknown, and labor avoidability remains an explicit assumption.

Four material limitations are preserved clearly:

- Admission payback and lifetime margins extrapolate **current** conditions over the assumed life. The proposal does not implement forward-looking path-aware investment valuation.
- Installed assets stay in the stock ledger, but output remains capped by eligibility that includes a new-acquisition/payback test. Lower modeled output is not demonstrated optimal continuation, mothballing or retirement.
- All compatible installed cohorts inherit current capability, coordination and service conditions without an upgrade cost, compatibility rollout or contract-vintage model. Physical vintage still controls stock and retirement.
- Learning exposure is supported available robot-hours and can accrue when eligibility suppresses accepted output. It is neither accepted-service exposure nor measured useful training data.

Legacy commercial tables explicitly retain initial-capability, year-zero-condition lifetime scope. The monthly entrant example, supply backcast and separate treasury experiments do not acquire an implicit trajectory linkage. Annual envelopes remain nonrevolving allowances. These boundaries prevent an annual cost/adoption extension from being mistaken for a reconciled company cash model.

## Independent numerical checks

The reviewer rebuilt the stated artificial site and system and called the current shared `matched_economics()` and `eligible_sites()` functions. All A–F witness families reproduced within displayed rounding:

| Witness | Independently reproduced result |
| --- | --- |
| A: overlapping savings | Costs `(10000, 8600, 6000, 5800)`; joint saving $4,200, versus $5,400 if standalone savings were incorrectly added. Interaction $1,200. |
| B: harmful coordination | C11 rises from $6,800 to $8,720; robot units fall from 600 to 360; retained human hours rise to 512. Robot value against C01 changes from $1,800 to −$120. |
| C: cost-only improvement | C11 falls from $7,800 to $6,300 while robot units remain 600 and retained human hours 320. Customer annual cash gain rises $1,725 and provider recurring margin falls $225, conserving the $1,500 resource gain. |
| D: complementarity | C11 $2,920; robot capacity 960; interaction −$1,680 and joint saving $7,080. The accounting permits complementarity as well as overlap. |
| E: adoption reversal | With unchanged capability, technical/economic/ready counts move from `12/12/10` to `12/0/0`; customer savings move from $3,000 to −$600 and payback from 2.5 to 6.25 years. |
| F: existing catalog anchor | For the tote cell at period 4, C01 moves from $49,560 to $38,040 and C11 from $27,473.942857 to $25,606.057143. Savings move from $6,316.371429 to −$922.714286; payback from 3.351365 to 5.387133 years; economic sites from 12 to zero. |

These executions are **point evaluations of existing functions**, not executions of proposed nonconstant paths. In particular, E's full adoption/stock witness still needs the future runner; its period indices 2 and 3 require at least a four-year fixture, separate from the document's three-year input example. Preservation of stock after the reversal must be asserted rather than inferred from the point economics.

## Required implementation acceptance checks

The design's validation and reproducibility contract is adequate: full-horizon finite arrays, scalar fallback only for omitted channels, explicit replacement precedence, fixed year alignment, bounds, rejection of booleans/nulls/unknown fields and unsupported versions, and no implicit smoothing or extrapolation. Complete effective arrays, scalar inputs, catalog, schema and every numerical helper's source hash enter scenario identity. Evidence snapshots remain separate from calibration. The same result object must serve exports, API and dashboard; selected-year displays must consume the annual rows.

The next implementation review should require all of the following before accepting a new numerical edition:

1. Constant-path equivalence against frozen **0.1.1** outputs for all eight presets and both hardware configurations, across every existing numeric field. New provenance identities and explicit additional metadata are expected; unexplained numerical drift is not.
2. Reproduction of the A–F point checks through the path interface, plus an actual multi-period E reversal that verifies contemporaneous admission, subsequent production/commissioning consequences and retained installed stock.
3. A nonmonotone coordination/cost path preserved exactly; invalid late-period values rejected before calculation; zero capability with no learning producing no robot work despite rising coordination.
4. A cost-only change at fixed stock/capability leaving output and exposure unchanged, distinguished from an endogenous rerun where changed adoption can later change exposure.
5. Component, finished inventory, commissioning, retirement, installed-site workload, support and shared funding invariants after nonconstant paths. The inherited continuation and exposure conventions must remain visible in outputs.
6. Saved-input replay through the common engine/API/export path, including a hash change when any numerical helper changes and no silent reuse of an older result identity. Commercial year-zero reference labels and unchanged separate entrant/treasury scopes must be inspectable.

No additional source research or calibration is required to implement this bounded synthetic adapter. Empirical claims would require matched target outcomes and complete support/cost denominators; neither benchmark progress nor the successful point witnesses supplies those inputs. A reviewed working implementation can address the evolving-comparator gap, while broader trajectory, inference-load, retrofit-vintage and dynamic-finance requirements remain open.
