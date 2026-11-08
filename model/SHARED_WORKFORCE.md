# Shared staffing, competing work and complete service

Edition 0.35. [Decision findings](../research/shared_workforce.md), [complete executions](results/shared_workforce.json) and [sole-writer review](../reviews/shared_workforce_review.md). Every work rate, staffing term and price in this module is a synthetic premise. No hospital quantity, labor rule or empirical staffing reduction is calibrated here.

## One execution and one named site crew

`_WorkforceArchitecture` extends the existing architecture/annual-resource policy. `architecture_resources_result` is extracted as a formatter of an already-completed execution; it does not run another fleet or Treasury. The new run keeps unit IDs, qualified parts, manufacture, support, integration, model/integrator roles, physical costs and all dated payments. Existing worlds retain their original behavior.

The new resource `site-service-crew` supplies four activities: local robot attention, separately identified inventory jobs, robot-zone handling and manual cleaning. Every booking has a unique task ID and one worker resource ID. The four earlier engineering, demonstration, professional support and integration pools remain distinct. Local attention is an additional explicitly assumed site responsibility; it is not a relabeling of the provider's already-priced support labor.

Standard cases retain the 500-zone monthly cleaning obligation for July 2026–February 2027. A second buyer requires 20 inventory jobs per month, each with a unique ID and 120 crew minutes. The surge changes only the last four months to 40 jobs. Inventory jobs are indivisible; cleaning zones retain the existing model's divisible service abstraction. Their quantities are never combined into one output denominator. Deadlines are month-end; no within-shift routing, congestion, clinical service or labor-law compliance is established.

## Staffing policy and funded work

The opening contract guarantees two 4,800-minute capacity blocks per month. Each costs $2,000 from the existing assumed $25 hourly wage. This is a paid capacity convention, not a headcount estimate. Digital-assisted manual cleaning uses the current annual path's minutes per zone; inventory work receives no automatic digital uplift. Local attention requires 60 minutes per supported robot, plus two crew minutes per robot-cleaned zone.

Execution month indices start at zero in July 2026. Beginning in month one (August), a notice may be issued only after a completed prior month supplied the entire combined obligation and had at least two supported robots. The default notice becomes effective two months later (October) and reduces the guaranteed commitment to one block. Its decision uses no future demand. After commitment, the notice is binding in this model: later scarcity requires paid extra capacity or appears as missed work. Longer notice retains additional paid blocks. No automatic payroll credit is earned from released task minutes. Severance, training and other transition charges beyond the notice-period commitment are unmodeled; real rights and costs remain unknown.

After physical support, commissioning and starts, the operator determines the minimum additional crew minutes needed for the full current obligation. It requests the lesser of the whole-minute ceiling of the shortfall and the declared overtime cap. The invoice is issued in phase five and prepaid at the opening of phase six, before service. Full funding is required. A refused optional booking pays nothing, allocates no time and cancels the contingent invoice; earlier staffing and physical expenses remain. This policy does not reserve overtime cash before physical investment and is not an optimal allocation rule.

Work priority is local robot attention, inventory jobs, then cleaning using the lower marginal crew-minute method. If required attention is incomplete, robot service is unavailable. Robot output remains bounded by the actual qualified supported-unit capacity; humans cover only what their remaining paid time permits. Unused minutes expire, and later time does not repair missed jobs. Regular capacity is unavailable when mandatory operating obligations are overdue, even though its unpaid staffing commitment remains a liability. The inherited calendar bridge's retained/released task-hour fields describe the cleaning task only. The additional `retained_site_crew_hours` and workforce bookings include local attention, handling and inventory work; inspect them for the complete crew obligation.

## Cash and organizational boundaries

The separate inventory buyer has its own opening account. It is invoiced only for completed jobs at an assumed $60 per job, collected one month later. Delivery is not a receipt: the zero-buyer-cash case retains delivered jobs and unpaid claims. Future-due receivables and overdue receivables are separately reported. No credit-based cancellation of the fixed service obligation is assumed.

Staffing and overtime are already included in enterprise outlay; inventory receipts are already included in external sales. Do not add them again to consolidated cash. Logical-role allocations are summed where roles share one legal account. In the licensed profile, customer and operator share an account: setting only operator-role cash to zero does not make that account unfunded. Tests exhaust both allocations when testing an unfunded site crew.

The resource-cash comparison is a bounded window of actual payments. Opening hardware, terminal assets, future material bills, uncollected buyer invoices, unmodeled transition work and other lifecycle obligations prevent a full ROI interpretation. Inspect the Treasury rather than treating lower cash outlay as lower complete-service cost.

## Replay, interface and limits

Run `python3 scripts/export_shared_workforce.py` or `--check`. `--case FILE --output FILE` replays complete opening physical, Treasury, business, finance, calendar, architecture, annual-resource, component and workforce inputs; submitted outcomes and hashes are ignored. `GET /api/shared-workforce` checks current source fingerprints and exposes the nine-world catalog plus one full reference. `POST` requires exactly `inputs` or `saved_case`; invalid shapes fail closed. Fractions use decimal-string numerators and denominators throughout the browser wire format.

Learning, Customer and Commercial views share one applied execution. Controls change notice, paid capacity, competing jobs, handling/attention and payer cash. Pending or invalid inputs retain the applied export; stale responses cannot replace newer edits. Imported complete cases replay their full inputs and remain read-only in shortcut controls until a standard world is selected. Annual scenario controls do not silently change this separate contract.

This joins a site crew and two service obligations to the existing architecture/resource/parts/Treasury loop. It does not simultaneously execute all six cells, competitor/customer renewal, acquisition/recovery or endogenous R&D. The stronger human-dispatch world assumes cleaning efficiency rises from 0.15 to 0.25 under the existing site-software charge; it is a conditional alternative, not measured AI or conventional-software performance. The hospital audit supplies the accounting question only, never these coefficients.
