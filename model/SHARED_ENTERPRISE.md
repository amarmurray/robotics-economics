# Shared market, physical deployment and enterprise cash

Stage 4 executes one synthetic incumbent/entrant market through the accepted monthly physical, Treasury and commercial engines. It replaces independent entrant capacity in this new comparison. Historical ENTRY-FG-01 remains a separately labeled reference for old scenarios; none of its robots, cash or output is added here. The [design](shared_enterprise_design.md) defines the boundary, and the [sole-lead review](../reviews/shared_enterprise_review.md) records checks and limitations.

## Reproduce and inspect

```sh
python3 -m unittest discover -s tests -p test_monthly_enterprise.py -v
python3 scripts/export_enterprise.py
python3 scripts/export_enterprise.py --check
python3 scripts/export_enterprise.py --bridge
python3 scripts/export_enterprise.py --case downloaded-case.json --output replay.json
```

The default artifact is `model/results/shared_enterprise.json`; the fixed-policy funding search is `model/results/enterprise_funding_bridge.json`. Both retain source hashes. Each exported case also contains its executed source-file hashes and a content hash; replay under changed source produces a new identity. `run_enterprise(plan, treasury, contracts, enterprise)` accepts the complete frozen inputs. `replay_enterprise(saved)` reconstructs the same shared physical plan, opening financial journal, commercial contracts and enterprise inputs, then recomputes rather than trusting saved results. `run_shared_case(inputs)` exposes a bounded reference experiment with opening cash, additional equity, incumbent procurement timing, scheduled customer return, collection delay and an incumbent-only alternative.

The existing Customer adoption view is now led by this shared calculation. Select a witness or edit its controls and click **Apply shared-market assumptions**. Invalid inputs leave the prior result/export intact. `GET /api/shared-enterprise` returns eight witnesses; `POST /api/shared-enterprise` accepts an `inputs` object and returns the resolved controls and complete case. The dedicated export is replayed with the command above, not the annual scenario importer. Annual controls do not affect this separate eight-month market.

## One service and customer ledger

The work profile is `WORK-FLOOR-BUNDLE-SYN-02`. Each robot's 100 accepted bundles per full supported month already incorporates stipulated downtime and quality. The single commissioning-month quarter ramp remains in the physical loop. There is no second uptime multiplier or independent ten-robot equation. Both operators use the same system; procurement dates and finite shared resources determine assignments.

Recurring demand has three disjoint, constant pools: 1,000 incumbent-baseline units, 200 existing unmet units and 100 hypothetical new units each month. Baseline customers initially belong to the incumbent; the others start unassigned. The reference entrant attempts to capture 70 baseline, 20 unmet and 10 new units in month 2. Customer moves require sufficient source assignments, paid formation/acquisition and qualification. A scheduled move is attempted once; failure does not create an automatic later retry. An early customer-return attempt can fail because the entrant has not yet captured those customers. This is an explicit reassignment experiment, not a model of strategic bidding or preemptive retention.

Assignments persist even if their operator cannot deliver. Unserved work is lost for that recurring service period and is not automatically added to another operator or to next month's backlog. Robots serve assigned work first; a paid human shift can serve the remainder. Actual delivery is allocated proportionally across that operator's assigned pools, retaining exact fractions. The planning ceiling in each `Operator` is an upper bound, not another independent demand pool. The market ledger is the sole source of actual demand.

`months[].outputs[].accepted_output_units` continues to mean **robot** output in the physical ledger. New fields record human and total output, while `enterprise.months` reconciles each demand pool and operator. The two ledgers join by operator/month; their robot quantities must match. Total accepted delivery equals robot plus human delivery once. Baseline-equivalent human hours remain null because no hours-per-bundle conversion is supplied. Annual cleaning zones are a different work unit.

## Real cash, commitments and service

Every endpoint has an actual Treasury account, including the aggregate end-market buyer, independent lessor, investor, manufacturers and enterprise vendor. No payment creates money. The reference provider funds five starts, two existing incumbent robots are historical stock, and only three additions can fit the commissioning/support constraints. With prompt incumbent procurement, two additions go to the incumbent and one to the entrant; two accepted new robots remain finished. Ten entrant requests are therefore one installed robot, not ten.

Formation/site work, fixed overhead and staffing are explicit noncancelable commitments. They continue while the declared business is active, including after a missed payment; there is no automatic shutdown, waiver or cancellation. An inactive incumbent-only alternative creates no entrant commitments. Human shift capacity requires a positive staffing charge, paid before service. Reduced human work does not automatically remove that payroll. Output-related materials use explicit supplier credit, separate from hardware/start and support components, and become payable after the stated positive lag.

Month 0 phase 1 records future equity commitments; no cash moves yet. Phase 2 collects eligible end-market receivables and funded equity, then inherited service-contract receipts/deposits. Phase 3 attempts refunds and due operator obligations before support. Oldest due dates have priority, then issue time, then stable invoice ID. This deterministic tie rule is explicit and is not an optimal or legally mandated waterfall. Opening operator obligations must have phase-3 due dates; unsupported opening calendars are rejected rather than silently paid late. Opening commercial collections retain their explicit schedules.

A missed due obligation blocks the affected operator's procurement, customer acquisition and delivery. Old debts, installed assets and customer assignments survive. The shared physical rule still reserves existing support before additions; one unsupported existing unit can block further starts/shipments/commissioning across this conservative plan. Paying arrears allows later execution when other constraints permit. There is no assumed repossession, lender recovery, bankruptcy discharge or free customer switchback.

Phase 5 attempts customer moves after physical shipment/start actions. Phase 6 creates sales invoices only for accepted delivered service and materials invoices only for actual modeled use. Service availability charges retain their separate stage-3 contract rule. Prices are integer cents per bundle; an exact fractional charge is rounded once per operator/month/invoice to the nearest cent, half up. The export retains unrounded rational cents and the rounding difference. A zero rounded charge has no cash invoice. Collection lag is positive, and uncollected invoices remain receivables rather than cash.

## Fixed-policy capital bridge

The reference entrant starts with $25,000. Its formation/site commitment is $5,000, monthly overhead $2,000, acquisition charge $50 per captured recurring unit, lease rent $1,500 per installed robot-month, and material-use charge $10 per delivered unit. Hardware, installation and support are charged only through their shared commercial/physical contracts. All are invented terms.

The separate bridge experiment starts the entrant with $1,000 and searches additional month-0 equity up to $24,000. Twenty-one bisection candidates identify **$18,950** of extra upfront equity for the fixed path: total opening/funded cash is $19,950, and minimum actual cash reaches zero. A one-cent-smaller contribution misses the month-3 support payment and fails to deliver the reference path. The investor must hold and transfer the contribution. An unfunded commitment or late injection cannot finance earlier formation or retroactively reclaim already allocated robots/customers.

This minimum is conditional on the declared interval, exact deterministic action path and its monotone cash-feasibility condition. It is not optimal staged fundraising, an estimated capital-access probability, a valuation or an investment recommendation. Explicit financing promises are excluded from operating sales. The consolidation separately reports end-market cash, equity receipts, physical vendor outlays, enterprise vendor outlays and any other opening boundary flows. Cash change is not profit: the horizon ends with receivables, material obligations and assets; opening assets' prior cost and terminal values are outside the experiment.

## Remaining boundaries

The shared comparison now connects an incumbent/entrant demand ledger, actual assigned robots, commercial title and enterprise payment gates. It does not complete the larger treasury design: autonomous reinvestment, scheduled borrowing/repayment/interest/maturity, optimal allocation, customer contract renewal, endogenous demand, asset recovery, broader configurations and annual/K-architecture cost bridges remain open. Supplier and staffing-provider working capital and fixed productive capacity are not reconstructed. Human capacity, rights, customer retention, prices, qualification and labor removal are not calibrated by observed deployments. W1-CASH remains partial.
