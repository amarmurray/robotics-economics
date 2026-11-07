# Annual digital paths in dated monthly execution

Edition 0.15 adds `model/calendar_bridge.py` as a policy on the existing monthly physical, commercial, enterprise, financing and Treasury loop. It uses the existing annual `parameters`, `resolve_paths`, `parameters_at`, `capability_at` and `operation` functions. The nine source/catalog hashes and complete saved inputs identify each execution. No second fleet, bank balance or customer market is added from the annual model.

This is a **synthetic service contract**, not empirical calibration or a conversion of earlier floor bundles. The four intelligence-architecture ledgers remain separate pending their role, resource and commercial contracts. A fixed-staff four-way comparison is implemented; the stronger conventional coordination comparison still requires its own equal-information/authority/resource challenge.

## Unit, scope and calendar

`WORK-CLEANING-ZONE-BRIDGE-SYN-01` explicitly uses one monthly accepted cleaning zone for one annual accepted cleaning zone in `CELL-M11-floor-cleaning-US-2025`. The original `WORK-FLOOR-BUNDLE-SYN-02` has no known conversion and is rejected by this bridge. The selected annual cell's 6,000 zones/site-year supplies a 500-zone monthly baseline. The new market has 500 baseline, 100 unmet and 50 new recurring zones, with the existing explicit customer moves. These are invented matched quantities, not an estimate of a real facility or a new employment denominator.

The standard horizon is eight whole months, July 2026–February 2027. Annual levels change at January, not every twelve months from the execution start, and are not interpolated. The underlying annual resolver validates the complete three-year path even though only two calendar years enter this horizon. The recorded 2026 and 2027 outputs contain six and two months respectively; partial years are never extrapolated into full-year service.

An annual digital cost is divided by twelve for a whole-month booking. This convention is not day-based accrual. Each cash invoice rounds once to cents, half-up; exact rational pre-rounding amounts and differences remain in the charge lines. The physical operating rate is also divided by twelve and rounded for the monthly booking. Twelve rounded bills can differ from a single annual rounded expense; the exact unrounded rate remains visible.

## One actual stock and explicit software vintages

The integer monthly unit IDs are authoritative. Manufacturing starts, actual acceptance/rejection, shipping, commissioning, support and ramp remain in that loop. A supported cohort contributes:

```text
monthly expected accepted capacity
  = annual operation.accepted_units / 12 × actual first-month ramp
```

The annual function already incorporates capability, uptime, intervention time, throughput and coordination. No second uptime or success discount is applied. Ramp reduces first-month capacity once; it does not discount a full-month support or software booking. The monthly plan's 1,000-zone rated ceiling is only a mechanical bound. It is not extra service: actual effective capacity is separately recorded and cannot exceed that ceiling. Demand and funded human fallback still cap delivery.

Opening units are explicitly assumed already integrated and initially qualified at the starting calendar level. Their prior acquisition/integration cash is outside the opening-balance horizon; this is not a full lifecycle investment comparison. Newly commissioned units receive the level actually admitted at that time. A new model generation is not silently assigned to an old robot.

`frozen_cohort` retains each unit's admitted robot capability/coordination and subscription-rate vintage. Human digital efficiency still follows the current calendar. `paid_calendar_upgrade` uses the current robot level after a changed capability/coordination signature passes a funded qualification booking. A mere calendar tick or human-efficiency change does not require a robot upgrade; unchanged robot levels incur no qualification charge. A subscription price-only change can change the current bill without inventing a performance qualification event. The standard changed-robot assumption is $500 and two qualification hours. These are invented terms, not measured update costs or rights clearance.

If an upgrade booking fails, its cash and resource changes are rolled back, the old vintage remains, and that unit supplies no service for the failed booking. Automatic old-version fallback is not assumed under this selected contract. The paid human process can still deliver if the business is operational. A later funded attempt may qualify the retained unit; no robot is recreated.

## Shared resources and atomic funding

Each supported unit consumes one twelfth of the annual function's support hours, including maintenance. Upgrade qualification consumes the same declared support pool. Initial process integration uses a separate monthly pool. The standard allocation is 60 support/upgrade hours and 200 integration hours per month. Each annualized allocation must be no greater than its annual reference pool. Other annual markets are not simultaneously executed against those pools.

Initial integration is 70 hours per new unit under the standard annual assumptions. Three arrivals therefore cannot all commission inside a 200-hour month: two commission, while the third retains its physical identity in transit and can complete later. Shipping can precede a later resource failure; its actual earlier expense is retained. There is no retroactive refund of completed transport.

Support/commissioning, any first rent, robot software and changed-version qualification are one contingent funded booking. The policy first evaluates them on an immutable Treasury candidate and commits only if all settle. A one-cent software shortfall cannot leave a paid physical booking, consumed support hours or an advanced software vintage behind. Ordinary fixed obligations, including staff and site software, keep their separate due-date semantics.

The annual source already contains an exogenous capability path. Endogenous learning is rejected in this bridge, and no experience/data premium or cross-embodiment improvement is added. This supports a bounded no-transfer cohort comparison; it does not implement the full campaign's learning-resource model.

## Cost mapping and human work

| Annual/reference item | Monthly treatment |
| --- | --- |
| Catalog manufacturing cost per start | Paid on each actual start; accepted/rejected counts remain actual. No second expected-yield divisor |
| Hardware purchase price × price multiplier | A declared monthly contract transfer, separate from manufacturing resource expenditure |
| Process integration hours × $60/hour | Paid once for each newly commissioned unit; already integrated opening stock is distinct |
| `operation(digital=False)` expense | One twelfth per supported monthly booking, with disclosed cent rounding |
| Additional robot digital cost | One twelfth of the applicable annual/vintage level per actually supported robot |
| Site digital cost | One twelfth per active business; fixed subscription obligation |
| Upgrade qualification | Explicit dated per-unit payment and shared resource requirement before the changed level is used |
| Shipping | Additional explicit monthly expense; no separate annual-reference counterpart is invented |
| Qualified components/spares | Conserved monthly synthetic bundles; annual actuator/board inventories are not imported |

The physical support cost/configuration must match this explicit mapping; a saved case cannot silently substitute a different physical bill. Digital and upgrade payments go to one distinct outside supplier account, appear once in enterprise outlay, and reconcile to that supplier's cash. They are not added again to consolidated cost. Existing commercial price transfers and financing principal/interest retain their own classifications.

The selected cell assumes 0.32 baseline human hours/zone and $25/hour. Standard incumbent and entrant shifts correspond to 500 and 100 baseline zones per month. Their scheduled cash commitments remain fixed across the four matched branches. Available human capacity is:

```text
floor(staff cents / (100 × wage/hour × baseline hours/zone × (1 − digital efficiency)))
```

Flooring preserves a conservative whole-zone planning ceiling. Actual human task time is delivered human zones multiplied by the dated hours/zone. The export separates baseline-equivalent service hours, retained task hours, released task hours, scheduled staffing cash and the current-period invoice's actual settled cash. Unpaid wages are not payroll removal. No schedule-elimination rule is inferred from released task time.

## Comparisons and reproduction

Eight standard worlds include C00 human baseline, C01 digital-human, C10 robot base, C11 robot-plus-digital, improving calendar levels, frozen cohorts, sufficient upgrade hours and financing pressure. The four branches share the same staffing and customer-move policy with ample entrant capital. They vary the physical plan and additional digital tools. Their task-hour interaction is the usual four-way difference and is reported once; it is not an extra benefit added to the joint result. These are fixed policies, not optimized staffing, fleet size or conventional coordination.

```bash
python3 scripts/export_calendar_bridge.py
python3 scripts/export_calendar_bridge.py --check
python3 scripts/export_calendar_bridge.py --case saved-case.json --output /tmp/calendar-replay.json
python3 -m unittest tests.test_calendar_bridge -v
```

The Customer adoption view offers witness selection, annual paths, calendar dates, resource allocations, cohort policy, qualification costs and funding controls. Export/reload preserves complete inputs and recomputes through the same engine; saved outcomes cannot override the calculation. Rational numerator/denominator components are decimal strings in this new wire format, so JavaScript JSON parsing cannot round integers above its safe range. Non-rational integers, including cash/count fields, must stay within the browser safe-integer range; larger inputs or derived values fail visibly instead of exporting rounded data. Displayed ratios are approximate formatting; complete stored components and case hashes remain exact. Invalid and stale requests retain the last valid result. Imported complete cases are read-only in the shortcut editor; selecting a witness restores the standard controls. Historical code changes produce different hashes and require the original checkout for historical reproduction.

`GET /api/calendar-bridge` returns the full witness bundle. `POST` accepts exactly one `inputs` or `saved_case` object. Seven metric-lineage records connect equations, source inputs, implementation and evidence boundaries. Full-stock annual integration, four intelligence architectures, optimized conventional coordination, acquisition/hybrid transitions, actual rights/qualification and empirical whole-system costs remain open. No target recommendation becomes calibrated merely because the bridge replays.
