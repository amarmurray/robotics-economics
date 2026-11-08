# Recovery cash and recovered service are different outcomes

Edition 0.28, continuation from accepted `33579d11c03d7906d6924ef8d7b7dbbe590d1cd4`. [Fourteen funded recovery worlds](../model/results/asset_recovery.json) extend the existing physical, calendar, company and Treasury loop. The [methods](../model/ASSET_RECOVERY.md) specify synthetic prices and rights, actual settlements and one unchanged robot identity. This is a bounded execution mechanism, not an observed distressed-asset transaction or a valuation estimate.

An installed robot can have productive capacity while its operator cannot meet obligations. A new buyer may have cash but lack a qualified site. A lender can recover money without restored service; conversely, a robot can return to productive service while an old loan remains impaired. Treating these as one recovery percentage hides both the transaction and its operating consequences.

## Follow the same unit through title, cash and service

The reference customer owns one opening robot and defaults on a funded loan. After that month's scheduled debt settlement, a distinct incumbent buys the unit for a declared $20,000 and pays $1,000 for initial relocation. The old operator's current support is canceled; its customers, staff commitments, remaining debt and legal identity stay behind. The unit is unavailable during months one and two, then separately qualifies and commissions at the buyer in month three. Accepted service remains limited by actual demand, paid human capacity and supported physical capacity.

| Synthetic world | Sale | First supported buyer month | Buyer expected accepted zones, eight months | Remaining seller principal, USD | Final physical state |
|---|---|---:|---:|---:|---|
| Funded reference | Completed | 3 | 3,269.10 | 0.00 | Installed |
| No asset sale | None | None | 2,352.00 | 10,141.29 | Installed at seller |
| Buyer qualification unavailable | Completed | None | 2,352.00 | 0.00 | Awaiting qualification |
| No commissioning slots | Completed | None | 2,352.00 | 0.00 | Awaiting commissioning |
| Low $3,000 sale price | Completed | 3 | 3,269.10 | 8,091.29 | Installed |
| Stronger paid human buyer, purchase | Completed | 3 | 4,000.00 | 0.00 | Installed |
| Stronger paid human buyer, no purchase | None | None | 4,000.00 | 10,141.29 | Installed at seller |

These are expected synthetic cleaning zones, not observed completed jobs or cross-market calibration. The total due workload is 7,200 zones. The reference delivers 4,371.10 across both companies. The stronger buyer already covers all 4,000 zones assigned to it; purchasing and supporting the robot adds no accepted buyer output and removes no paid staffing. It is therefore insufficient to justify the purchase by pointing to available robotic capacity. The model does not infer a benefit from an unpriced option or future customer growth.

The no-sale and ineligible worlds retain physical property and obligations. A lessee cannot sell its independent lessor's asset. Missing release or configuration-transfer permission prevents the sale even with ample buyer cash. With no shipping slot, the offer fails; a completed relocation cannot displace a second new unit into the same slot. These are explicit model permissions and resource checks, not claims about enforceable real-world rights.

## A successful sale can leave a stranded buyer

Purchase and initial relocation settle together or neither does. At the exact synthetic funding boundary, a one-cent deficit prevents title transfer and both payments. Passing the boundary does not prepay all future commissioning, software or support. This fixture's later collections fund month-three commissioning even when the purchase exhausts current cash; that result cannot be assumed for a different collection calendar.

If the buyer configuration never qualifies, the funded sale still stands, the unit remains unavailable and buyer service equals the no-purchase human baseline. The seller can nevertheless settle its loan from actual receipts. An arrival after the observed horizon has the same lack of restored service during the window. No resale proceeds, end-of-window valuation or reversal is invented to repair that unfavorable outcome.

Conversely, the low-price sale permits the same physical restoration while leaving the old seller in default. Principal recovery, lender loss, restored buyer service and the old company's customer obligations need separate reports. In the reference, the lender had already received $9,858.71 before sale proceeds arrived; remaining principal is $10,141.29 at sale-month close and is settled the following month. The entire original loan is not incremental recovery from the asset.

## Use recovery as a gate in the existing decisions

Hospital continuity needs a funded fallback during removal, transport, site acceptance and support qualification. A sale contract or replacement entitlement alone does not satisfy due deliveries. The [hospital contract evidence](hospital_support_contracts.md) establishes why repair, supported software and replacement terms must be inspected; it does not supply a resale price or authorize transfer of a target configuration.

Utility inspection additionally needs current routes, permissions, sensor/reviewer qualification and required coverage during transition. Automotive reuse requires the buyer's integration, safe workcell configuration, takt and commissioning capacity. All three packs inherit the questions, not these cleaning rates, prices or rights assumptions. None gains an empirical ROI or final recommendation from this extension.

The provider/operator/integrator/financier boundary also survives the sale. Consideration transfers cash between buyer and seller; relocation and later support consume separately funded resources. Customer ownership, robot ownership, custody, software rights and lender claims remain separate. Substantial H enters through software cohorts, conventional planning, the stronger human baseline and explicit transfer eligibility; no model release automatically transfers a qualified service stack.

Proceed with a measured recovery case only when the actual owner, permitted release/configuration, capable buyer, dated funds, relocation, site acceptance and retained obligations reconcile. Wait when the buyer's operational qualification or fallback remains unresolved. Reject a recovery claim that sells another party's asset, treats purchase as accepted service, pools legal accounts or cancels debt/customer commitments without an explicit supported transaction. These are research decision gates, not authorization for commercial actions.

DE-04 remains partial: the declared owner sale now executes, while secured priorities, lease repossession, restructuring, valuation and optimized investment remain outside scope. Fourteen bounded families contain 158 worlds; source counts and empirical requirements do not improve merely because the mechanism exists. The same active campaign continues to **2026-11-14T20:12:27Z**. The next integration should connect an unresolved annual fleet/resource or competitive decision, or add target evidence capable of changing a recommendation, rather than multiply favorable recovery variants.
