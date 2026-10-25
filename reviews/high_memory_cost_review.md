# Independent review: matched high-memory configuration cost

Reviewed 25 October 2026. **Accepted after correction in model version 0.1.1.** The inherited error understated the robot-only cost for the high-memory configuration by $800 per site-year and consequently overstated the cost interaction by $800. It did not affect the standard configuration used by the eight saved presets.

## Finding and invariant

The digital-trajectory design owner identified that `operation()` charged `memory_extra = 800` only when `digital=True`, although extra hardware power applied to both robot branches. The independent reviewer reproduced the consequence: with human digital efficiency, additional coordination and additional digital service cost all zero, high-memory `C11 − C10` was $1,400 rather than the $600 site software fee. Hardware was therefore inconsistently assigned to the additional-digital intervention.

The required invariant is the same configured robot hardware and its associated operating charge in C10 and C11. Extra digital service cost and coordination may differ between those branches; the selected hardware configuration must not. Human-only C00 and C01 must not acquire a robot hardware charge.

The root owner moved `memory_extra` into unconditional robot operating cost and left only `digital_cost_usd` inside the additional-digital branch. `matched_economics()` still excludes robot operating cost when `robot=False`. No capability gain was introduced. The catalog changed only its model-version metadata from 0.1.0 to 0.1.1.

## Independently checked snapshot

| Artifact | SHA-256 |
| --- | --- |
| Corrected `model/engine.py` | `0c35c6f2602d29a60a6bc187c013c0e4dd9a3597064cf67bed5a1ecc616a8d07` |
| Corrected `model/assumptions.json` | `bffc4460c3427c73b7f84f68f3c17feeadb4860308adce311c402d35092d3efb` |
| `tests/test_engine.py` | `a3bc8710756684f41f9fc8daa71fe09961b79de840625b0e208ac123ba421c2b` |
| Tracked pre-correction engine used for comparison | `d31f2b93a639b24b288f9a4c5915a05bd342a63c28e02e75ff8407db2c411f0f` |

The prior engine and catalog were extracted read-only from the tracked checkpoint into ignored reviewer work files. No observed repository commit identifier is published here; session repository metadata remains in ignored `sync_receipt.json`. The reviewer did not change model, catalog, tests or exports.

`python -m unittest tests.test_engine -q` passed **14 tests**. Additional independent checks established:

- All **34,659 numeric fields** across the eight existing saved preset JSONs exactly matched corrected live results before export regeneration. No new numeric fields appeared. Version and hash metadata are deliberately outside numerical equivalence.
- Running the tracked prior engine and catalog separately also reproduced numerical equivalence for all eight presets.
- For the reference scenario with `onboard_configuration="high_memory"`, the only numerical changes against the prior engine were six C10 values increasing by $800 and six `cost_interaction` values decreasing by $800. C11, the fleet, commercial and entrant numerical paths were unchanged.
- Across all six cells, at uptime one and zero intervention time, the 2,000-hour operating witness charged high memory an additional **$832 in each robot branch**: $800 plus 2,000 × 0.1 kW × $0.16/kWh. Human branches were unchanged. With additional digital controls zero, `C11 − C10` was $600 in both hardware configurations, and changing configuration left the interaction unchanged.
- At the reference availability settings, the hardware cost was likewise equal across robot branches; the power increment follows modeled available hours rather than always being $32.

## Disposition and downstream consequence

No remaining blocker was found for this narrow accounting correction. The digital-trajectory design can support both existing hardware configurations against corrected version 0.1.1; a standard-only restriction is unnecessary. Its constant-path compatibility test must use the corrected version as its baseline and explicitly preserve the older checkpoint as a distinct historical version. Updated engine/model hashes are expected even where preset numerical results are unchanged.

The $800 and power assumptions remain synthetic. This correction restores internal comparison consistency; it does not establish a measured hardware price, inference cost, capability improvement or deployment benefit. Review of the separate trajectory design and its future implementation remains necessary.
