# Monthly commercial extension: bounded stage 3 design

Reconstructed locally from the accepted Treasury and monthly physical modules. The earlier cloud-only design was unavailable. One agent owns this implementation and review; no independent review is implied.

## Decision and common engine

Compare outright sale, independent lease and provider-owned supported-availability service as alternative worlds over exactly the same requested `Plan`. Reuse `run_monthly` for every component, robot, capacity, assignment and accepted-output transition, and `Treasury` for every cent. A contract may block a requested action; it must not fabricate equal realized output. No entrant demand, annual economics or architecture result is spliced into this fixture.

One contract covers each declared operator/site. Separate legal accounts represent the provider, customer, independent lessor and external manufacturing/deployment vendors. A customer can control several sites, but each site's demand is disjoint by assumption. Historical opening installed assets have the arrangement's declared opening owner; opening finished assets belong to the provider. Their prior capex remains outside the horizon.

## Terms and order

| Arrangement | Purchase/title | Commissioning and physical support | Recurring payment |
|---|---|---|---|
| Sale | Customer pays the provider for an accepted finished robot; title passes only with successful paid shipment. | Customer pays the deployment vendor. | None. |
| Independent lease | Lessor pays the provider for the accepted robot; lessor retains title. Customer never pays that acquisition price. | Customer pays the deployment vendor separately. | Fixed rent per installed robot-month, including the commissioning month, without ramp proration. |
| Provider service | No hardware sale; provider retains title. | Provider pays the deployment vendor. | Fixed fee for each actually supported robot-month, invoiced after phase-6 availability and collected no earlier than a subsequent month. No output-sales revenue is inferred. |

Manufacturing and transport remain provider payments under every arrangement. Bundled manufacturing consumes consigned inputs and is charged once per admitted start, including rejects. These simplified contracts do not assert actual industry terms.

Phase 1 issues existing lease obligations (noncancelable) and conditional first-period rent for eligible transit units. The shared engine issues contingent physical bookings with the correct payer. Phase 2 collects due service invoices and explicitly scheduled opening receivables of any included actor, and attempts declared customer security deposits. Phase 3 attempts deposit refunds and existing lease arrears in oldest-first order before physical support. A failed full payment retains the entire liability; no implicit partial settlement. Phase 4 completes funded manufacture and attempts commissioning. Commissioning and its conditional first rent settle atomically. Phase 4 also issues contingent purchase quotes for each finished unit/site pair. Phase 5 tries one actual assignment using the existing allocation cycle; purchase and transport settle as one serial simulation transaction. All unused quotes are canceled. Phase 6 invoices supported service. Phase 7 records cash, units, title/custody, unpaid obligations and exact service.

**Explicit extension of the earlier conservative timing rule:** an already accepted unit may be paid for and shipped in phase 5, and its *settled* receipt may fund a later start in that phase. There is an actual physical asset before the receipt, and shipment precedes the later start. A future sale, unsigned quote or receivable cannot fund its own manufacture. A failed shipment commits neither purchase payment nor title. This is local immutable simulation atomicity, not an external payment guarantee. Tests must distinguish the legitimate sequential chain from circular funding.

## Default, deposits and cancellation

Lease arrears block the affected contract's support, commissioning and further shipments; already installed assets remain installed and owned by the lessor. Outstanding rent continues to accrue while the customer retains the installed asset. Service arrears block new support and commissioning; no fee is generated for an unsupported period. Paying arrears permits the next actual support attempt. The shared conservative rule still blocks all additions if any existing unit is unsupported. No automatic repossession, asset deletion, recovery proceeds, write-off or legal insolvency outcome exists.

Deposits default to zero. Optional customer security deposits are paid to the lessor for leases and to the provider otherwise. They are explicitly restricted or spendable and remain refundable liabilities, never purchase credit or earned revenue. They can be requested only once at the first month's phase 2; failure leaves the contract unqualified for shipment. Cancellation is permitted only before that site's first shipment or opening installation; it prevents later shipments, retains any funded WIP/finished stock, and requests a full refund in phase 3, retrying later if cash is insufficient. Cancellation in month 0 suppresses deposit placement. No new starts occur when every site has canceled. A provider's overdue noncancelable obligations or failed refund also block discretionary starts; unrelated obligations otherwise require their own explicit payment schedule. This is not a company-wide mandatory-payment/credit/default scheduler.

## Acceptance and exclusions

Verify identical physical use and vendor outlays for fully funded worlds; internal price changes only redistribute cash while all gates remain funded. Challenge thin liquidity, missing components, rejected manufacture, unpaid purchase/transport, unpaid commission/support/rent, late service collection, post-support fees, restricted and spent deposits, cancellation, integer validation, identity and actor separation, multiple sites, immutable failure and exact replay. Preserve the prior six stage-2 witness artifacts byte for byte.

The implementation does not price lease credit risk, interest, depreciation, residual values, human payroll removal, lab economics or end-market sales; allocate uncertain real costs; schedule autonomous reinvestment or financing; model technical commissioning failure; recover assets; or complete the common entrant-demand/annual-model bridge. Title, custody, workflow authority and maintenance responsibility are reported separately; data/IP rights remain explicitly unspecified. A synthetic payment schedule is not evidence of commercial feasibility.
