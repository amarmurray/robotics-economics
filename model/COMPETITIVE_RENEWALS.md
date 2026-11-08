# Funded customer renewals on the shared execution loop

Edition 0.24. This is a synthetic recurring cleaning-service contract on the existing `_BridgedEnterprise` → finance → enterprise → commercial → monthly physical → Treasury chain. It replaces predeclared customer moves only within this extension. No older engine, empirical coefficient or saved scenario is replaced. [The findings](../research/competitive_renewals.md) and [review](../reviews/competitive_renewals_review.md) delimit the decision.

## Service, customers and technology

The default window contains twelve explicit months, indexed 0–11. Ten identified lots each require fifty accepted cleaning zones every month. Their total remains 500; switching providers creates neither demand nor output. Eight and twelve months are separate observation windows, not annualized records. The shortcut allows 8–24 months and at most 650 zones. Installed service uses the existing exact rational capacity abstraction, not discrete clinical jobs, measured reliability or a stochastic queue.

Both businesses request two robots from the same financed supplier and qualified configuration, with no opening installed robot. The shared start, allocation cycle, delivery, commissioning, rent, support and retained human contracts remain explicit. The incumbent's paid human capacity is 588 zones; the entrant's is 117. Their monthly staff commitments are $4,000 and $800, with respective $1,000 and $2,000 overhead. Entrant formation is $5,000. Initial cash is $500,000 incumbent, $100,000 entrant, $200,000 provider and $500,000 lessor. These are inherited synthetic test inputs, not source estimates. Annual capability progress is zero; no disclosure-audit prices or company financials calibrate the fixture.

Human capacity, robot support and current obligations must be funded before a new award. At phase 5, after support and commissioning admission, available capacity is the paid human allowance plus actually supported robot capacity, less already locked/awarded lots. An award requires a whole lot to fit. This is a current-period admission rule, not a guarantee that a six-month contract can be served in every future month. Locked work can subsequently be under-served.

## Renewal and pricing policy

A lot is eligible when its expiry arrives, it is unassigned, or its previous-month delivery fell below the explicit 90% threshold and the contract allows breach exit. Only prior delivery and currently admitted resources enter the decision. Initial contracts expire in month zero by default. A six-month contract awarded in month zero expires in month six.

The incumbent bids $29 per accepted zone before response and $25 after its response threshold is met; the entrant bids $27. Robot-linked response needs actual supported incumbent units, not an order or a calendar date alone. It first occurs in month two in the default. A separate human-led comparator responds in month two without incumbent robot procurement. A supported-unit rule can cease to apply after loss of support; the reported first-response month does not assert permanent response. Offer changes never reprice a locked contract.

For each eligible lot, process candidates in ascending order of:

`term months × lot units × offered accepted-unit price + buyer switching resource cost`.

Equal scores retain the existing provider; otherwise stable operator name breaks a tie. Lots are processed in stable ID order. This greedy, conventional rule is neither an optimal auction nor an estimated buyer preference or competitive equilibrium. With one month, fifty zones and a $2 price gap, $100 of buyer switching work exactly ties; $99.99 permits the lower-price offer, subject to capacity and funding. Recipient onboarding is a separate resource bill, $10 per recurring zone by default; it is not added again to buyer preferences or customer price.

Conditional onboarding and buyer-switch quotes are issued at phase 1 with phase-5 eligibility. An immutable candidate Treasury settles both; the award commits only if both payments settle completely. A failed candidate leaves the prior ledger intact and the next eligible bid can be tried. Unused quotes are cancelled at phase 5. The failed hypothetical payment is never posted as real resource consumption. Fixed formation, staff and overhead commitments still remain. The first prototype's attempted same-phase issue/settle was rejected and corrected before acceptance.

## Revenue, cash and boundaries

Actual provider service is distributed proportionally over its lots. Each contract line records exact accepted units, locked price and unrounded cents. Sum these once per provider/month, then round that invoice once. Actual collections follow the invoice's dated settlement. There is no invented per-lot cash allocation. Base business price arrays are validated projections of the initial offers; locked lot prices alone govern actual revenue.

At each monthly close:

`cumulative operating cash = bank cash − opening bank cash − paid equity − (actual loan draws − principal repayments)`.

`cash after recorded bills = cumulative operating cash − all recorded noncancellable unpaid operating obligations`.

The second expression reserves issued bills even if not yet due. Opening invoices and preexisting credits are rejected: inherited servicing requires a separate supported contract. The base enterprise policy also rejects operator-funded equity; injections must come from a distinct outside investor. Interest remains an expense. A capital inflow cannot create cash break-even. Receivables are not spendable cash. First break-even is the first nonnegative value after an earlier negative month; the separate maintained-through-horizon date requires every remaining observed month to be nonnegative. A null date is not observed within this window, not a proof of perpetual failure. An operator never negative does not acquire an invented startup-recovery event.

This is a bounded cash-flow diagnostic, not distributable returns, recovery of an opening asset stock, enterprise valuation, lifetime ROI or a fully financed future. Unissued future commitments, beyond-window service, residual assets and liquidation/restructuring are not valued. Fixed staff and leases continue after customer loss unless the inherited contract says otherwise; no optimizing shutdown or frictionless downsizing is granted. Recorded arrears can continue to grow.

Recipient onboarding is already included in enterprise outlays. Buyer switching work is paid to the external resource vendor and reported separately outside the operator/provider consolidation. End-market sales and internal lease/service transfers retain the inherited actor boundaries. The finance boundary audit must leave no unclassified cash. All actors together conserve cents; assigned and unassigned lots conserve demand; missed work is not backfilled.

## Reproduction and interface

[The JSON artifact](results/competitive_renewals.json) contains seventeen complete worlds, their shortcut inputs, exact event/contract/Treasury records, summaries, source hashes and per-case hashes. `python3 scripts/export_competitive_renewals.py --check` recomputes every world. `--case downloaded.json --output replay.json` restores all opening physical, Treasury, commercial, enterprise, finance, calendar and competition inputs; stored outputs are ignored. Rational numerator/denominator values are decimal strings for exact browser transport. Equivalent integral float spellings in permitted older inputs canonicalize before hashing. Historical source identity requires the corresponding checkout.

`GET /api/competitive-renewals` verifies exported source hashes and serves the reference plus small world presets and summaries. `POST` accepts exactly one `inputs` object or complete `saved_case`. Invalid, null or unknown shortcut inputs fail visibly. The local upload/body bound is 8 MB. Customer adoption exposes bids, term, breach exit, cash, support, qualification and receipt timing. Pending, failed and stale requests preserve the last applied display/export. Full imports are replayed and read-only in shortcut controls until a standard witness is selected. Annual cell/year controls do not relabel this cleaning fixture.

The four lineage records trace awards, switch thresholds, locked-price invoices and funding-adjusted cash. This advances bounded DE-CF05. The existing partial support mechanisms remain partial DE-CF10: this extension does not optimize expanding fleets, entry/exit, pricing strategy, learning or investment.
