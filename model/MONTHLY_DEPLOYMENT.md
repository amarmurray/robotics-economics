# Monthly deployment fixture: paid physical progress

Current extension: [stage 3 commercial schedules](MONTHLY_COMMERCIAL.md) now call this same physical loop with explicit payment/title policies. The stage-2 default described below and its six full witness artifacts are preserved exactly. Sale, lease, operator cash and cancellation exist only when the separate `run_commercial` entry point is used; they are not silently added to these historical default examples.

Stage 2 implements a **small, isolated synthetic physical-and-cash fixture** using the accepted [Treasury core](TREASURY_CORE.md). It tests whether paid starts actually pass through acceptance, shipment, funded commissioning and supported output. It does not complete the [treasury extension](treasury_extension_design.md), replace the annual engine, integrate the entrant business, or calibrate any physical/economic coefficient. All scenario inputs are invented accounting and timing witnesses.

The implemented unit is one provider-owned system and one accepted-work profile. The provider pays manufacturing, transport, installation and support. Operators are assignments of physical work, not additional asset owners or separate customer cash models. Opening finished and installed units are explicit historically funded stocks; their purchase cost is outside the simulation horizon, not assumed zero. No sale, lease, title transfer, demand competition, autonomous investment or recovery policy is inferred.

## Reproduce and use

From the repository root:

```sh
python -m unittest discover -s tests -p test_monthly_deployment.py -v
python -m model.monthly_deployment
```

`monthly_witnesses()` returns six named deterministic artifacts, identical to the CLI's JSON. `run_monthly(plan, treasury)` runs a declared `Plan` against an immutable opening `Treasury` and returns detached JSON-compatible data. Neither function writes files or modifies prior scenarios. The opening treasury must have no event after month 0, phase 1. It must contain the provider and the two vendor endpoints; one vendor may perform both vendor roles, but the provider cannot pay itself. The core enforces a common currency, actual funded transfers and minimum/restricted/earmarked cash constraints.

Inputs are frozen dataclasses with explicit validation:

| Input | Contract |
|---|---|
| `System` | One compatible component pool; component use per start and supported robot-month; bundled start, transport, commissioning and monthly support fees in integer cents; positive assembly and commissioning leads; accepted work rate and rational first-month ramp. |
| `Operator` | Stable assignment ID, requested additions, one demand entry per month and opening installed stock. Operators' demand pools are disjoint assumptions. |
| `Start` | One unique preplanned batch ID, month, integer starts and integer future acceptance count. The acceptance outcome is stipulated, not sampled or estimated. A batch is admitted in full or blocked in full. |
| `Collection` | One explicit opening receivable ID and attempted collection month. The initial Treasury supplies its payer, face amount and eligibility. These are preexisting receivables, not generated robot sales. |
| `Plan` | Explicit monthly component receipts, support/transport/commissioning capacities, operators, fixed allocation cycle, opening stocks and start/collection schedules. No annual-to-monthly interpolation or hidden capacity refresh. |

Robot identities and component quantities are nonnegative **integers**. Fractions of robots are rejected. Service is an **exact rational expected accepted-output flow**: a 101-unit full-month rate at a quarter ramp is `{"numerator":101,"denominator":4}`, not a rounded 25. Monetary charges depend on integer robots/batches and remain exact cents; fractional service does not create a rounded invoice. Booleans/floats are rejected for integer inputs. The work rate already includes the fixture's assumed downtime and quality acceptance; there is no second uptime or quality multiplier.

The fixture uses a deterministic acceptance count instead of the broader design's continuous expected-yield convention. Thus two starts with one accepted system mean exactly one reject; neither accepted stock nor money is fractional. This choice makes stock and cash admission auditable for a small witness, not an optimized factory schedule.

## Clock, priority and atomic admission

| Phase | Implemented actions |
|---|---|
| 1 | Issue contingent, cancellable prepayment invoices for opening installed support, eligible transit commissioning, and the month's planned starts. Invoices contain no cash. |
| 2 | Attempt only scheduled opening-receivable collections. Core eligibility and payer cash determine actual receipts. A future receipt or forecast cannot fund an earlier action. |
| 3 | Give opening installed units first claim on support slots, available spares and payment. An unfunded or unsupported unit remains installed and produces no output. |
| 4 | Receive the specified qualified components; finish previously funded WIP; classify each unit as accepted or rejected. Attempt eligible commissioning only after existing support. Issue transport prepayment invoices for actual finished units. |
| 5 | Settle and admit transport/assignment first, then preplanned manufacturing starts. Each requires its physical constraints and an actual full core payment. |
| 6 | Deliver output only from assigned, installed, paid-supported units; apply the single first-month ramp and the operator's demand ceiling. No sales invoices are generated. |
| 7 | Emit stock, output, cash and event records; check conservation. Report invoice status using the existing core's diagnostic rule at this closing Moment, without new collection/default/recovery actions. |

Financial issuance strictly precedes settlement. Starts are invoiced in phase 1 and paid in phase 5; commissioning/support packages are invoiced in phase 1 and paid in phase 4. A system accepted in phase 4 may receive a transport invoice in that same phase and pay/ship in phase 5. No invoice is paid at its own issue Moment. There is no accidental extra finished-stock month.

The exact lead contract is:

```text
start:         month t,       phase 5
accept/reject: month t + L,   phase 4       L >= 1
ship:         month s,       phase 5       s >= t + L
commission:   month s + C,   phase 4       C >= 1, earliest date
first output: commissioning month, phase 6, at one first-month ramp
```

Actual commissioning can be later if cash, slots or support inputs are missing. A delayed unit stays in transit and receives a new contingent commissioning attempt next month. Its first-month ramp follows its **actual** commissioning date. Transport is not charged again. The start schedule has no automatic retry: a blocked start requires another explicitly declared order to be attempted later. There is no autonomous reinvestment rule, even when a scheduled old receivable is collected later.

Existing support is a strict priority. If any opening installed unit remains unsupported, new commissioning, shipments and starts are blocked that month. Its required unconsumed spares remain protected in inventory. Monthly receipts arrive in phase 4, so they cannot retroactively enable a failed phase-3 support booking; reserved components can support the following month. This conservative timing is explicit and can matter materially to output. No late-month service catch-up is modeled.

If existing support succeeds, eligible transit units take commissioning and support capacity before shipments and starts. Each new commission requires one slot, one support slot, its service components and payment of **commissioning plus the first month's support**. That unit is not billed again as an existing robot in the same month. Later months require a normal support payment before output.

Every admitted start, shipment, commissioning or service action has an exact linked Treasury invoice and payment event. Physical constraints are checked before attempting payment. A valid but unfunded payment is logged by the core; the contingent unpaid booking is then cancelled. A physically blocked booking is cancelled without a payment. Neither case consumes parts, slots, assignment demand or unit stock. These are cancellable **prepaid bookings for work not delivered**, not unconditional earned payables being erased. Existing core opening obligations retain their own terms and are not automatically cancelled or paid by this fixture.

The whole run is a pure operation on immutable inputs. Invalid plans fail without changing the supplied Treasury. Cash settlement and physical admission are assembled locally as one returned result; no intermediate paid-but-uncommitted external side effect is published. This is serial simulation atomicity, not concurrent database or real robot transaction safety.

## Manufacturing, spares and capacity accounting

Manufacturing uses one declared cash basis: **bundled all-in cost per admitted start**. Qualified components are consigned/supplier-funded until issue. The start charge includes their consumed cost and conversion work; rejected systems retain that sunk expenditure. Component arrival and acceptance create no extra manufacturing bill. Support fees similarly include the service components consumed for that robot-month. Supplier financing before issue, component price decomposition, salvage and refurbishment are outside the perimeter.

Transport has a separate paid fee and an explicit monthly shipping-slot ceiling. Installation is paid at actual commissioning. There is no unpaid transport/installation capacity hidden inside the work rate. Exogenous support/crew/shipping capacities are inputs, not claims about labor supply or the provider's fixed enterprise overhead; their underlying staffing capex and fixed costs are excluded.

Shipments draw only from accepted finished stock. They also require a declared operator request, a future-month commissioning slot booking and support capacity sufficient for the installed/pending pool. The target month must exist in the input horizon. Units booked for **different** future commissioning months do not share the same commissioning-slot budget; support commitments persist across months. Cash and spares remain checked at actual commissioning, so a shipping booking does not guarantee on-time installation. An overdue transit queue can delay a later booking; actual monthly commissioning remains capped. This is a conservative local allocation policy, not a global schedule optimizer or a promise of fulfillment.

Successful shipments assign units using the fixed operator cycle, advancing only when shipping succeeds and skipping operators whose requests are filled. The witness cycle is incumbent, incumbent, entrant. The units stay with that operator; an operator's idle output capacity cannot serve another operator's demand. Unshipped requests remain requests, not installed robots or output. There is no incumbent response or market-share model.

For every month the executable checks:

```text
closing components = opening + qualified receipts - start use - service use
closing WIP        = opening WIP + admitted starts - accepted - rejected
closing finished   = opening finished + accepted - shipped
closing transit    = opening transit + shipped - commissioned
closing installed  = opening installed + commissioned
closing rejects    = opening rejects + rejected
```

Reservations protect existing-service components within closing inventory; they are not another consumption line. Unit IDs remain unique, cash postings balance through the core, and total included cash is conserved. Output is bounded by the operator's assigned, supported cohorts and demand. Rejected, finished, WIP, transit and unsupported installed units produce zero. Opening stocks are included once in physical conservation and never counted as current manufacturing.

## Deterministic witnesses

Default synthetic costs are $36,000 per start, $100 transport, $1,000 commissioning, and $100 per supported robot-month. Each start uses two compatible component units; each supported robot-month uses one. The full rate is 100 accepted service units per robot-month, with a quarter-rate first month. These are invented test values, not observations.

| Export key | Result and interpretation |
|---|---|
| `witness_8_funded` | One paid start at month 0 phase 5; acceptance and paid shipment at month 1 phases 4/5; paid commissioning at month 2 phase 4; output 25 at phase 6, then 100 in month 3. Opening provider cash $40,000 becomes $2,700 after all stated charges. |
| `unfunded_future_receipt` | Opening cash $10,000 cannot pay the month-0 start. Parts remain unconsumed and no WIP appears. The explicitly eligible preexisting $60,000 receivable is collected in month 1; it neither funds month 0 retrospectively nor triggers a new investment. |
| `funded_without_components` | Opening cash $40,000 does not overcome zero components. No manufacturing payment, WIP or output occurs. |
| `unfunded_commissioning` | Opening cash $36,100 pays one start and its later shipment. No cash remains for the $1,100 commissioning/support package. The unit stays in transit, consumes no commissioning spares/slots and produces zero. |
| `paid_rejected_start` | One paid $36,000 start is deterministically rejected. Cash loss and two consumed components remain; no accepted stock, transport charge or output appears. |
| `witness_4_static_allocation` | Begin with five finished robots and two installed incumbent robots. Three future commissioning slots and five total support slots permit two new incumbent assignments and one entrant assignment. After paid shipping/commissioning, five are installed and two remain finished. The entrant produces **25**, not 1,000, in its first month; incumbent output is 250 (two existing full-rate plus two quarter-rate additions). |

Witness 4 is a static shared-resource allocation replayed across an explicit shipment/commissioning lead. It does not integrate ENTRY-FG-01 or simulate competition. Opening units are historical stocks, not free new robots generated by this module. Witness 8 establishes the event/phase arithmetic under its stipulated inputs, not deployment duration in a real facility.

The owner tests additionally cover mixed acceptance/rejection, delayed commissioning, longer leads and separate booking months, cash/parts/slot shortages, minimum reserves, support/spares priority, exact fractional output and demand caps, immutable inputs, payment/action joins, a 27-case adverse matrix and CLI equality. Independent review is required before report integration.

The remaining exclusions are commercially material: empirical calibration, qualified supply evidence, stochastic failures, heterogeneous BOMs, inventory purchase finance, technical commissioning success, supplier/staff fixed costs, lifecycle economics, human labor release, separate operator cash, sale/lease/title contracts, credit draw schedules, mandatory-obligation scheduling beyond this fixture's own inputs, enterprise formation, endogenous demand, incumbent response, reinvestment, default enforcement/recovery, unit relocation and an annual-engine/dashboard bridge. The full treasury/shared-newco requirement remains partial.


## Optional typed component contract, edition 0.31

The generic module contract and historical results above remain available unchanged. A separately declared `TypedComponentSystem` activates [compatible part accounting](COMPONENT_EXECUTION.md), requires zero generic quantities and an explicit material ledger, and preserves the same phase order and paid physical admissions. Typed stocks replace the generic module balance; they do not supplement it. Manufactured BOMs and named whole-part replacements are explicit, with no inferred conversion from aggregate annual spare use.
