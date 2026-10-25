# Annual digital trajectories: implementation and integration audit

25 October 2026. **Sole-lead verification; no new independent review.** The user's one-agent usage limit was preserved. The earlier independent design review remains applicable to the contract and toy arithmetic, but did not inspect this implementation. This audit accepts the bounded annual-path mechanism and retains the broader program's empirical and financial gaps.

## Evidence inspected

The implementation uses `model/trajectories.py` only for full-horizon validation and level resolution. `model/engine.py` supplies the existing economic equations, annual ranking/eligibility, manufacturing demand, operating output and conservation ledgers. The selected-year trace recalculates those same functions. The scenario identity includes both numerical source files, the catalog, scalar inputs and complete effective paths. Original supplied paths and resolved levels are exported separately.

The frozen scalar fixture was generated locally from the accepted 0.1.1 engine before editing; its engine hash is recorded in `tests/fixtures/annual_scalar_v0_1_1.json`. It contains digests and field counts for all eight presets and both onboard configurations. Comparison removes only added path/capability metadata and intentionally new provenance identities. **All 69,315 pre-existing numerical fields match exactly** in both omitted-path and explicit-flat-path runs. The older untracked fixture found at session start was preserved and is not part of this new fixture's provenance.

The full repository suite passes **107 Python tests**. New tests reproduce overlap, harmful coordination, complementarity, cost-only incidence, a real four-period admission reversal with retained stock, the accepted tote-cell anchor, zero capability, invalid late periods, source-hash sensitivity, complete API/CLI replay and integer-valued floating horizons. Existing stock/component/WIP/finished inventory/commissioning/replacement/support/funding/site-output invariants now also run on twelve seeded nonconstant paths across both hardware configurations. **32 JavaScript assertions** cover the existing evidence facets and new annual-input/import handling. These tests establish the stated synthetic behaviors; they do not estimate real effect sizes.

## Browser and artifact checks

The local server on `127.0.0.1` was exercised in the Codex in-app browser. An eight-year nonmonotone path was applied through the visible editor. Year selection changed the four-way table; the 2030 trace showed that year's inputs and matching costs. An actual browser JSON download reproduced the entire engine result exactly. Reset followed by reload restored the original path and scenario hash. A wrong-length path was visibly rejected while preserving the last valid displayed/exported result. All thirteen views rendered and the browser reported no console errors. A legacy scalar input and final screenshot are recorded in the local operational receipt after verification. This is a desktop interaction check, not a mobile/accessibility or multi-browser certification.

Eight standard exports, six annual counterfactuals and three isolated experiment packets are regenerated from their authoritative functions. The report checks every declared annual-export dependency hash. Rebuilding and link verification are recorded at publication; no unpublished cloud execution or prior interrupted command is counted as completed work.

## Acceptance and remaining risks

W1-006 is met as an explicitly synthetic, source-context-linked mechanism scenario: matched output and demand, evolving human baseline, independently specified channels and nonadditive interaction are inspectable. This is not empirical calibration. W1-TRAJECTORY remains partial. Installed robots inherit current software/price conditions without rollout expense; admission/payback screening also constrains existing output; learning uses supported available hours; and annual envelopes are not a revolving treasury. Lifetime commercial tables freeze resolved year-zero conditions. The monthly entrant, treasury and paid-physical fixture remain separate.

The physical-requirements crosswalk and stage-3 commercial design described in the cloud handoff were unavailable locally. They are not included or claimed complete in edition 0.5a. Workstream K is registered as active scope with open research needs, not as completed model-lab evidence. The original campaign deadline and sole-agent limit remain in force.
