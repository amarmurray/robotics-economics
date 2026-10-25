# Independent review of the monthly deployment fixture

Reviewed 25 October 2026. **Disposition: pass within the isolated stage 2 scope.** No material implementation defect was found in the inspected snapshot. The fixture connects actual payments to integer physical progress and exact rational service under its declared synthetic schedule. It does not complete the full treasury/shared-entrant extension or validate a factory or deployed robot service.

The reviewer read [the implementation](../model/monthly_deployment.py), [owner tests](../tests/test_monthly_deployment.py) and [methods and limits](../model/MONTHLY_DEPLOYMENT.md), against the accepted [treasury extension design](../model/treasury_extension_design.md), [design review](treasury_design_review.md) and [stage 1 review](treasury_core_review.md). Implementation inspection began only after the owner declared the three files frozen. The reviewer edited no implementation, shared documentation, evidence, model assumptions or exports. Additional probes remain in ignored `work/review_monthly_deployment.py`. Launch repository provenance is in ignored `sync_receipt.json`; the requested serving model/reasoning setting remains independently unverifiable.

## Exact phase and accounting witnesses

Witness 8 meets the required event contract exactly:

| Event | Observed fixture Moment | Boundary |
| --- | --- | --- |
| Paid start | Month 0, phase 5 | Components and cash consumed once; one unit enters WIP. |
| Accepted completion | Month 1, phase 4 | The funded unit leaves WIP; acceptance creates no second manufacturing payment. |
| Paid shipment | Month 1, phase 5 | No extra finished-stock month; one unit enters transit with one operator assignment. |
| Paid commissioning plus initial support | Month 2, phase 4 | One commissioning slot, one support slot and service components are consumed. |
| First accepted output | Month 2, phase 6 | Capacity/output 25 at the single quarter ramp. |
| Next month | Month 3 | A separate paid support period permits capacity/output 100. |

The 40,000 USD provider opening balance becomes 2,700 after 36,000 manufacturing, 100 transport, 1,100 commissioning/initial support and 100 later support. These amounts are invented fixtures. They establish charge boundaries and timing, not lifecycle profitability, real prices or deployment durations.

Witness 4 draws from five historical finished robots and two historical installed incumbent robots. It ships two new incumbent assignments and one entrant assignment, leaves two finished, and later has five installed robots under five support slots. The entrant produces 25 in its first month; the incumbent produces 250 from two existing full-rate and two quarter-rate additions. This is a static common-resource allocation with disjoint assumed demand pools, not ENTRY-FG-01, market competition or a financing/title arrangement. Historical opening assets are not counted as new manufacturing.

Unfunded starts consume no components, create no WIP and cannot use later receivables retrospectively. Adequate cash without components likewise produces no start. Unfunded commissioning preserves transit stock, consumes no installation/service components or capacity and yields zero output. A rejected paid start retains its sunk cash and component use; no accepted robot, transport or output appears. A delayed commission applies the ramp at its actual installation month rather than its initially booked month.

## Independent execution

The reviewer executed all **21 owner tests**, including their 27-case adverse matrix; all passed. An additional **10 independent tests** passed. Their substantive coverage was:

| Probe | Result |
| --- | --- |
| Identity and payment replay | Reconstructed each unit's WIP, acceptance/rejection, finished, transit and installed transitions from physical events. Every admitted paid action joins exactly one full settlement at the same Moment, with an earlier invoice issue. Every blocked prepaid booking has zero payment and a cancelled unpaid balance. |
| All six exported witnesses | The independent replay passes all six artifacts, including per-operator supported-unit membership and exact output from actual commissioning dates. No physical unit appears in two operators' operating events in one month. |
| Small exact-cost, mixed-yield case | Two 100-cent starts with one reject pay 200 once; a 2-cent shipment, 10-cent commissioning/support package and 3-cent later support produce total cost 215. Manufacturing consumes four component units and service consumes two. Starting cash 1,000 ends at 785. |
| Restricted cash and unrelated earmark | A provider's minimum reserve, unrelated reserved payable and restricted customer deposit prevent both starts and shipping despite gross bank cash. Parts remain intact. The original earned payable remains outstanding/defaulted with zero cancellation; the restricted refund obligation also survives. |
| Partial batch affordability | Cash 199 cannot admit a two-unit batch costing 200. No fractional start, payment, component use or WIP is produced. |
| Within-phase priority | A funded shipment occurs before that month's planned start. When the transport charge leaves too little cash, the full start is blocked without consuming components. This verifies the documented shipping-before-start policy, not an optimal allocation rule. |
| Overdue commissioning queue | An old unfunded transit unit and a later booking compete for actual installation capacity. A later receipt funds only the unit admitted under the one-slot limit; delayed units remain in transit and are not recharged transport. |
| Assignment cursor and idle output | A failed shipment does not consume a request or advance the allocation cycle. Later successful shipment goes to the next intended operator. An assigned operator's zero demand does not free its unit's output for the other operator. |
| Existing-support priority | Partial support of opening installed stock leaves unsupported units installed, protects unconsumed spares and blocks all new commissioning/shipping/starts for that month. Phase-4 receipts do not retroactively create phase-3 supported output. |
| Mixed-resource and invalid-input challenges | **100 deterministic seeded plans** combine two operators, batches, acceptance counts, cash, components, receipts, support/shipping/commissioning limits and zero/quarter/full ramps. Independent unit/payment/output replay and cash/component conservation pass. **55 invalid numeric-field combinations** reject Booleans, floats, NaN, infinity and negative values. A failure late in a run leaves the supplied Treasury unchanged. Returned artifact edits do not mutate inputs. |

Separate short probes confirm that the Treasury's declared EUR denomination is preserved without implicit conversion and that an opening Treasury containing an event after month 0 phase 1 is rejected without mutation. The owner suite also directly checks CLI/function equality and immutable scenario branching. No implementation correction was needed after these checks.

The tests are finite witnesses, not an exhaustive proof over arbitrary inputs. The seeded matrix is deterministic software coverage, not stochastic robotics performance or an estimate of failure probability. The ignored replay script initially inferred an opening finished unit's original state from its final operator assignment; that reviewer-oracle mistake was corrected to account for its recorded shipment before the final runs. It was not an implementation defect.

## Interpretation and remaining boundaries

The fixture deliberately uses integer robot/component identities and a stipulated integer acceptance count, rather than the larger design's fractional expected-yield convention. Service can be fractional and is retained exactly as a numerator/denominator pair; cash remains integer cents. The output rate already includes assumed downtime and quality, so no second uptime, quality or annual half-year multiplier appears.

Qualified components are consigned until issue. The bundled start payment includes manufacturing component use and conversion; support fees include that period's service components. No receipt or acceptance creates an extra manufacturing charge. Upstream supplier working capital, real input qualification, staff/facility fixed cost, salvage and technical commissioning failure remain outside the fixture. Paid transport/installation/support cannot establish economic sufficiency for those omitted costs.

The implemented clock schedules this fixture's own contingent prepayments, declared opening-receivable attempts, physical actions and support. It is **not** a complete mandatory-obligation, financing, maturity, default or recovery scheduler. Opening unrelated liabilities retain their Treasury terms but are not automatically paid. A defaulted opening obligation does not automatically freeze this fixture's investment. That is a disclosed unimplemented commercial/default policy, not evidence that a defaulting business could continue operating in practice.

Cancelled bookings represent prepaid work that was not delivered. They are not earned fees, manufacturing refunds, written-off legacy debt or a waiver of real contractual claims. Existing installed support has strict priority: any shortfall blocks additions even where a more flexible scheduler might allocate spare resources. Monthly receipts arriving after that support decision cannot rescue the missed month. This conservative policy should remain explicit whenever results are interpreted.

Shipping reserves a future commissioning opportunity and persistent support demand under the local policy; it does not reserve future cash or guarantee timely installation. Overdue units can displace a later booking within the actual monthly slot limit. The run is serial and pure over immutable inputs; assembling a returned financial/physical artifact provides simulation atomicity, not concurrent database, external payment or robot-execution atomicity.

One provider owns all units. Operator IDs assign service and do not create customer cash pools, ownership transfers or title rights. No unit moves between operators, retires or is repossessed. There are no generated robot sales, lease schedules, end-market invoices, newco formation costs, customer switching, endogenous demand, reinvestment or annual-engine/dashboard bridge. The module therefore supports a bounded physical/cash conservation checkpoint; it does not close shared newco financeability or the full eight-witness extension.

The bounded stopping condition is met: exact phases, rejected-action atomicity, yield and service cost boundaries, assignment exclusivity, payment joins and stock/cash conservation have been independently challenged. The next material test belongs to a separately scoped commercial/demand integration on the same physical plan, not more claims about actual field economics from these synthetic inputs.

## Reviewed file identities

SHA-256 of the frozen, tested snapshot:

```text
model/monthly_deployment.py            2fe8ad382176e0febc359a02334343e901dc55386b5ce1412bd45468f24ca425
tests/test_monthly_deployment.py       57575532c692410227fbb8629be2b65f6bee24b0c1202accf27651968cf4ed41
model/MONTHLY_DEPLOYMENT.md            bd1d8e26d471976d94dffe5ec1c22d62965dcd4b288621cff08b7b912e32d345
model/treasury.py                      d1b63a6d977d9ce95e1e6748747b6e5692db05c61c1b56a139779d5492684f9f
work/review_monthly_deployment.py      1797024fd4a421e8b1e3844723800d8d53deba9dba59faa0e78d8473b1db8f94
```

No report integration, output-file export, commit or publication was performed by this reviewer.
