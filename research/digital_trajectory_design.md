# Design decision: annual digital trajectories in the matched comparison

Status: bounded implementation recommendation, 25 October 2026. This is a design, not an implemented trajectory runner or calibrated forecast. It addresses the missing evolving comparator in W1-006 and part of W1-TRAJECTORY. The existing evidence and numerical engine remain the sources of truth; this document adds no empirical coefficient.

**Recommendation:** implement three independent, explicitly synthetic annual paths by resolving the existing `digital_efficiency`, `coordination` and `digital_cost_usd` controls once per calendar year. Pass the same resolved parameters to every affected annual calculation. Reuse `operation`, `matched_economics` and the fleet's conservation logic. Add an annual four-way reference table and preserve the existing reference scopes for lifetime cash and the separate monthly entrant. Do not add a general scaling law, automatic inference-price-to-capability link, or a second economic calculator.

The compatibility baseline is the independently reviewed **model 0.1.1**, engine source SHA-256 `0c35c6f2602d29a60a6bc187c013c0e4dd9a3597064cf67bed5a1ecc616a8d07`. Its correction places the $800 high-memory configuration charge in both robot branches, consistent with the already shared extra power requirement. See [high-memory review](../reviews/high_memory_cost_review.md). Both onboard configurations can therefore use the proposed paths without changing required hardware cost between C10 and C11. Earlier results remain historical versions, not the constant-path oracle for that corrected charge.

## 1. The minimum input and output contract

Use an optional, versioned trajectory object separate from scalar parameter validation:

```json
{
  "schema_version": "digital-annual-paths/0.1",
  "base_year": 2026,
  "digital_efficiency": [0.15, 0.25, 0.35],
  "coordination": [0.15, 0.10, -0.10],
  "digital_cost_usd": [1500, 1200, 1800],
  "epistemic_status": "synthetic_assumption"
}
```

This example requires a three-year horizon. Index `t` means `catalog.base_year + t`; values are levels, not growth rates or increments. A supplied path replaces its scalar for **all** periods. An omitted channel is filled with the corresponding scalar repeated exactly `years` times. Never add the scalar to the path or compound a level. With no paths, all three are constant. Export both user inputs and complete resolved arrays so precedence is reviewable.

| Channel | Current units and bounds | Direct effect | Exclusions |
| --- | --- | --- | --- |
| `d[t] = digital_efficiency[t]` | Fraction of baseline human hours removed at matched service; 0–0.6 | Human-led comparator and retained human work in C11 | Does not increase robot capability, lower robot support hours, or establish removed payroll. |
| `g[t] = coordination[t]` | Proportional change in robot accepted-unit capacity; −0.4–0.6 | Additional coordination in C11 only, before the demand/site cap | Does not change policy capability index, available robot-hours, technical threshold, or hardware qualification. |
| `f[t] = digital_cost_usd[t]` | Additional robot digital-service expense, constant 2026 USD per supported full robot-year; 0–20,000 | C11 operating expense and the existing synthetic commercial pricing formulas | Is not dollars/token, cost/success, a total enterprise bill, or a shared compute-capacity constraint. |

All arrays must have exactly the scenario horizon, use finite numeric values within current bounds, and reject booleans, nulls, unknown fields, mismatched base years and unsupported schema versions. No interpolation, implicit last-value carry, truncation or extrapolation in the first implementation. Nonmonotone, worsening and declining paths are valid within bounds. Validate **all** periods before any calculation. A longer horizon requires explicit longer arrays or a new constant-path request.

The fixed $600 additional digital site charge remains common to C01 and C11. The initial cost trajectory covers the existing **robot** service bundle only. It does not assume that human software licenses, robot orchestration and model inference share a price decline. A future per-token-price model needs separate human/robot usage, failed attempts, cache behavior and service overhead; the current evidence cannot supply those denominators. Keep this limitation visible instead of relabeling `f[t]` as a universal inference price.

Minimum new outputs: resolved paths with units/status; `joint_by_year` with year, cell, capability reference, four costs and interactions; and each annual fleet row's effective `d`, `g`, `f`, exogenous capability and learned increment. Keep `joint` as the final-year alias if needed for existing consumers, with its scope explicit. The selected-year interface must use `joint_by_year`, not silently continue displaying the old final-year table.

## 2. One contemporaneous four-way calculation

For a fixed cell, let `Q` be its annual accepted-service requirement, `h` baseline human hours per unit and `w` hourly labor opportunity cost. Hold output definition, quality, service exclusions, wage, demand and site boundary fixed. Let `R0[t]` be accepted robot capacity at capability `k[t]`, uptime and intervention settings **before** the additional coordination channel. Then:

```text
R10[t] = min(Q, R0[t])
R11[t] = min(Q, R0[t] * (1 + g[t]))
H00[t] = Q * h
H01[t] = Q * h * (1 - d[t])
H10[t] = (Q - R10[t]) * h
H11[t] = (Q - R11[t]) * h * (1 - d[t])

C00[t] = H00[t] * w
C01[t] = H01[t] * w + S
C10[t] = H10[t] * w + K[t]
C11[t] = H11[t] * w + S + K[t] + f[t]
```

`S = $600/site/year` is the existing human/site digital charge. `K[t]` groups the common required robot operating costs and annual resource-capital consumption already computed by the engine, including the same configured board cost in both robot branches. These equations summarize the existing functions; do not implement another copy of them in a browser or trajectory module. Required embedded control, available robot-hours and configured hardware are held fixed within each year's contrast. C10 retains the required digital robot stack and the exogenous capability path; “robot alone” means without the additional digital intervention. These are matched one-site service comparisons, not additive realized fleet savings.

Derive only from the four computed costs:

```text
digital_alone = C00 - C01
robot_alone = C00 - C10
robot_on_moving_digital_baseline = C01 - C11
joint_saving = C00 - C11
cost_interaction = C11 - C10 - C01 + C00
joint_saving = digital_alone + robot_alone - cost_interaction
```

Negative cost interaction denotes complementary savings; positive interaction denotes overlap or added cost. No independent synergy slider or additive “digital savings” credit is needed. Apply `d[t]` to the human work that remains **after** the robot's contribution, rather than subtracting savings on the original full workload twice. C00 is the no-additional-intervention comparator; C01, not C00, is the relevant human alternative for the combined robot adoption screen.

For the annual **reference** table use `k[t] = capability_at(p,t,learned=0)` in both robot cells. This follows the existing fixed-horizon reference's scope, now repeated annually. Label it `exogenous_capability_reference`. It is neither the fleet's learned-capability outcome nor a causal decomposition of four different deployment histories. Do not feed learned capability from a combined deployment into one robot cell while holding the other fixed.

## 3. Capability, learning and operating vintages remain separate

The fleet continues to compute its funded, same-configuration learned increment from prior exposure, separately from exogenous `capability + capability_progress*t`. Its actual annual capability remains `min(1, exogenous + learned)`. None of `d[t]`, `g[t]` or `f[t]` enters that expression directly. Directed data/rights/validation assumptions do not improve automatically because digital service gets cheaper.

A trajectory can change adoption, which can later change exposure and funded learning. That mediated effect belongs in the rerun fleet outcome once. Do not add a second learning or data-value premium. For a clean direct-channel witness, disable transfer or hold the exposure/stock history fixed. A separate comparison with and without learning must include its validation cost and cannot be added to a joint saving that already includes the improved future operating outcome.

Preserve two inherited assumptions explicitly rather than quietly changing them during this extension:

- All installed compatible robots receive the year's common capability, coordination and digital-service conditions with no modeled upgrade cost or rollout delay. Physical installation vintage still governs stock and retirement, but not software-policy vintage. Name this `current_conditions_all_installed_legacy`; it is an unvalidated compatibility/pricing assumption, not evidence of free fleet retrofits.
- Existing exposure is supported **available robot-hours**, not demonstrated useful data or accepted-service hours. It can accrue while economic eligibility limits accepted output. Preserve its identifier and do not reinterpret it as measured training yield. A different useful-exposure or learning model requires a separate reviewed version.

The initial annual table does not attempt a hardware-generation, integration-capacity or engineering-R&D trajectory. W1-TRAJECTORY therefore remains partial even after a functioning digital-path implementation.

## 4. Cash and stock propagation: what must change, what does not

Create one `p_t` per year. The fleet's savings ranking, `eligible_sites`, stored matched economics, operation/output, released human hours and demand/installed-site caps must consume that same `p_t`. Manufacturing `forecast_need` must use the resulting current-year economic flags. Updating only a displayed joint table would leave the adoption model inconsistent.

| Boundary | Required behavior under a nonconstant path |
| --- | --- |
| Resource comparison | Recompute all four annual costs using the same year's inputs. Keep the original baseline-equivalent-hour conversion `h`, not the improving human-hours coefficient, as the additive activity denominator. |
| Customer cash screen | Recompute assumed avoidable labor cash from robot-covered units × `h*(1-d[t])*w*labor_avoidability`; recompute current-year service payments, customer saving and payback. Observed removed payroll remains null. |
| Provider/financier screening | Use the current-year operating expense and the existing sale/lease/RaaS payment rule once. Keep acquisition price, manufacturing yield and capital transfers separate. The existing lifetime-margin/payback screens freeze current conditions over life; they do not anticipate future path values. Label this **myopic current-condition screening**, not a forward-looking investment calculation. |
| New starts and shipments | A changed eligibility/ranking can alter planned starts, component consumption, shipments and subsequent commissioning through existing constraints and lags. No direct digital multiplier changes manufacturing supply, yield, qualified components or integration slots. |
| Installed fleet | Keep commissioned assets, retirement and replacement backlog on the ledger when the comparator improves. The existing output cap uses current eligible sites, including an acquisition/payback screen; preserve and disclose this admission-versus-continuation limitation. Do not describe lower modeled output as optimal mothballing, retirement or dispatch. |
| Support, energy and learning | `g[t]` does not automatically release support resources or reduce available hours; `f[t]` does not change physical power. Deployment-mediated changes in these totals remain possible. Existing service priority and common resource conservation remain binding. |
| Annual capital envelopes | Remain exogenous nonrevolving start/shipment allowances. Operating digital-service expense affects economics but is not newly debited from an invented treasury. No claim of financed inference capacity or full provider liquidity follows. |
| Legacy commercial cash tables | Keep the initial-capability lifetime **reference** scope, using resolved year-zero digital conditions. Do not present these as cash under the full annual path. A cohort cash schedule with evolving costs, fixed-versus-indexed contract terms and cancellation/default is separate work. |
| Separate newco, backcast and treasury experiments | Existing normalized monthly entry case has no direct `d/g/f` linkage; fixed-target supply backcast remains independent. Do not quietly inject annual paths into either or into a separately reviewed monthly treasury. Label these unaffected reference scopes. |

The current cost-plus commercial rule makes falling operating expense lower customer payments and provider dollar markup. This is a scenario term, not evidence that all real contracts reprice every year. The path metadata must state that installed-fleet operating economics use current conditions while the legacy lifetime cash table is only an initial-year reference. This split is a known limit, not a reconciled dynamic company financial model.

## 5. Exact adversarial numerical witnesses

The following are **synthetic point checks**, independently calculated through the existing `matched_economics`/`eligible_sites` functions. They are proposed acceptance fixtures for the future trajectory runner, not claims that it has already run. Dollar amounts are exact under these invented inputs except displayed decimal ratios.

Common toy site: `Q=1,000`, `h=1`, `w=$10`, 2,000 available robot-hours, rate 0.3 units/hour and fixed capability 1, giving `R0=600`. Uptime is 1; intervention, maintenance, power and integration costs are zero; yield is 1; life is five years; standard onboard configuration; sale; labor avoidability 1. Price and manufacturing cost are each $10,000, hence `K=$2,000/year`; `S=$600`. The base human workload is 1,000 hours. These parameters are intentionally artificial and do not describe any catalog cell.

| Witness | Inputs changed | C00 | C01 | C10 | C11 | Exact consequence |
| --- | --- | ---: | ---: | ---: | ---: | --- |
| A. Overlapping savings | `d=.2, g=0, f=0` | 10,000 | 8,600 | 6,000 | 5,800 | Digital-alone saving 1,400 plus robot-alone 4,000 is 5,400, but joint saving is 4,200. Interaction 1,200 is the overlapping human-work value, counted once. |
| B1. Baseline for harmful coordination | `d=.2, g=0, f=1,000` | 10,000 | 8,600 | 6,000 | 6,800 | Robotics saving against the digital human is 1,800. |
| B2. Harmful coordination | Same, but `g=-.4` | 10,000 | 8,600 | 6,000 | 8,720 | Robot capacity falls from 600 to 360; retained human work rises to 512 hours; robot incremental saving becomes −120. Capability and available hours do not change. |
| C1. Expensive digital service | `d=.2, g=0, f=2,000` | 10,000 | 8,600 | 6,000 | 7,800 | 600 robot units, 320 retained human hours, robot incremental saving 800. |
| C2. Cheaper service, unchanged competence | Same, but `f=500` | 10,000 | 8,600 | 6,000 | 6,300 | Exactly 1,500 lower resource cost; units, human hours and capability are unchanged. No capability gain can be inferred from the lower price. |
| D. Complementarity is possible | `d=.2, g=.6, f=0` | 10,000 | 8,600 | 6,000 | 2,920 | Robot capacity 960, interaction −1,680 and joint saving 7,080. The design must not mechanically force overlap or harmful coordination. |

For C1→C2, the sale payment falls from $2,300 to $575 per year. Customer cash gain before capex rises from $2,500 to $4,225, while provider recurring margin falls from $300 to $75. The net consolidated gain is $1,725 − $225 = **$1,500**, equal to the resource-cost reduction. Do not subtract annual depreciation again from the period cash ledger or count the customer transfer saving as additional resource value.

**E. Moving comparator reverses adoption.** Use the same toy site, but price/manufacturing cost $15,000 each (`K=$3,000/year`), `g=0`, `f=0`, the incumbent profile and a technical threshold of 0.5. At period 2 with `d=0`, costs `(C00,C01,C10,C11)` are `(10,000,10,600,7,000,7,600)`, customer saving is $3,000 and payback 2.5 years. All 12 sites pass the technical and economic gates, with 10 ready under the profile. At period 3 with `d=.6`, costs become `(10,000,4,600,7,000,5,200)`, customer saving −$600 and payback 6.25 years. All 12 remain technically compatible, but economic/ready counts become zero. No capability, service price, hardware or readiness regression caused the reversal. Existing stock must remain in the stock identity even though the current eligibility/output rule can now bind.

**F. Existing catalog anchor.** At period 4 (2030), default capability is 0.9. Holding every other reference control fixed in `CELL-M08-3pl-tote-US-2025`, changing `d` from .15 to .35 lowers C11 from $27,473.942857 to $25,606.057143, yet lowers C01 faster, from $49,560 to $38,040. Customer saving changes from **+$6,316.371429 to −$922.714286** and payback from 3.351365 to 5.387133 years; economic sites fall from 12 to zero. Lower combined resource cost does not by itself imply a stronger adoption case.

Additional invariant witnesses are mandatory: a flat path equals the corrected scalar baseline in **every existing numerical field**; a zero-capability/zero-progress/no-learning path cannot produce robot work because `g` rises; an alternating `g=[.2,-.4,.2]` and `f=[500,2,000,500]` must not be silently smoothed; installed-site output and all component/stock/support/funding identities still hold. Under fixed stock, supported hours and capability, a cost-only path must leave physical output/exposure unchanged. In a full endogenous fleet rerun it may change adoption and later exposure; that is an indirect mechanism, not a failed invariant.

## 6. Strong baseline, versioning and stopping decision

The simpler combined baseline is the **same** digitally improved human process and configured robot with the existing conventional controller/integration, `g[t]=0` and no **additional** robot-digital service expense `f[t]=0`. Required control, board, maintenance, support and the shared site charge remain priced. Compare added orchestration with this baseline as well as C01; C10 alone omits human digital improvement and is an insufficient comparator for an orchestration claim. A real additional conventional scheduler can have its own explicitly costed bundle; zero here means no incremental intervention beyond the already priced base stack.

Reuse reviewed evidence as mechanism constraints only: H-QJE-2025/H-METR-2026 motivate changing but heterogeneous human baselines; H-COORDINATION-2026 motivates signed, task-dependent coordination and a simpler alternative; HCR-E002/E004/E006 prevent mixing all-attempt and success-conditional costs; H-HOSPITAL-2026 preserves target-service exclusions; LEC-001–004 keep cheap collection separate from validated learning. Their measured values do not determine the path levels or slopes. See [digital dossier](digital_ecosystem.md), [coordination audit](coordination_reproducibility.md) and [learning-data economics](learning_data_economics.md).

Implement a pure path resolver and one new trajectory entrypoint around the shared engine functions. If a helper module carries resolver semantics, include **that module and every numerical helper** in `model_source_hashes`; hashing `engine.py` alone is insufficient. Scenario identity must include the trajectory schema, base year, complete effective arrays, scalar parameters, corrected catalog and numerical-source hashes. Evidence snapshot hashes remain separate from calibration. A saved path is never an implicit request to use newer defaults or to extrapolate a changed horizon.

Before accepting implementation, freeze model 0.1.1 regression outputs and verify all eight presets plus both configurations against their constant-path equivalents, excluding only added trajectory/scope metadata and intentionally new provenance identities. New code hashes necessarily produce new scenario identities. Preserve historical exports/revisions and write the new trajectory edition under a distinct schema/version; never pretend it reproduces an older scenario hash. Replaying an old saved scalar input through the new runner means an explicitly constant path and a new versioned result. Exact historical hashes require the historical checkout. The API, report and dashboard must consume the same result object.

The implementation is falsified if a path affects only display, uses mismatched years across gates and output, makes service-price decline alter competence directly, erases installed stock after comparator improvement, counts human savings twice, smooths a worsening path, or changes a constant-path numerical result without an identified versioned correction. An empirical orchestration claim would additionally require matched target outcomes, all-attempt support/cost and a credible deterministic alternative; this design supplies none of that calibration.

**Bounded decision:** proceed with this annual resolver, annual matched table and coherent fleet propagation; retain the stated cash, vintage, exposure and continuation-rule limitations. Stop before adding forward-looking treasury, hardware retrofit diffusion, inference-load pricing or a universal learning curve. Design acceptance alone closes neither requirement; a reviewed working trajectory scenario can address W1-006's evolving-comparator gap, while the broader W1-TRAJECTORY omissions remain explicit.
