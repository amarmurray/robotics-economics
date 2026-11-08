# Installed support and finite expansion admission

Edition 0.25. [The analysis](../research/support_expansion.md) tests bounded DE-CF10 on the unchanged calendar/finance/enterprise/commercial/physical/Treasury execution chain. The extension is an admission policy and declared monthly resource calendar, not another physical engine. [Self-review](../reviews/support_expansion_review.md) is by the sole writer.

## Service and actor contract

The eight-month fixture, months 0–7, has 1,000 recurring accepted cleaning zones per month. This is a declared synthetic workload using the existing cleaning work ID, not a new observed site or a conversion from the historical floor-service bundle. No transfer, unmet/new-demand pool or ownership change creates output. One incumbent operator is active; the inherited second operator account is inactive. Its staff allowance supports 117 zones per month for a fixed $800 commitment, with $1,000 overhead and a separately charged site digital bundle. None is a market estimate.

Two opening robots predate the cash window. One additional unit is requested by default; the shortcut permits zero to four. Individually identified one-unit start candidates appear each month. A candidate may proceed only while live non-opening, non-rejected units remain below the finite growth request. WIP, finished, transit and installed units all count. Rejected manufacture remains in the physical ledger with its paid components and cash, but can permit a later distinct replacement candidate. Two candidates in the same phase observe the actual first unit committed by the unchanged loop, not a stale duplicate inventory.

Provider-service contracts place manufacture, shipping, commissioning, physical support and robot software cash with the provider. The operator owes $1,500 per supported robot-month by default, collected after one month; end-market receipts are separately invoiced at the inherited synthetic price. Both payer accounts need real cash. Fees are internal transfers at the combined operator/provider boundary; external resource expenses are counted once. Other inactive/unused opening accounts do not become spendable provider capital. A separate $5,000 zero-interest loan witness is funded by the outside lender, matures in month seven and is repaid through the existing loan policy. It is an illustrative facility, not available financing or a financial recommendation.

## Actual resource execution and the planning rule

Opening installed support has phase-3 priority; commissioning occurs at phase 4, shipping and new starts at phase 5. The physical engine already preserves spares, qualified components, support slots, integration limits and first-month ramp. This extension adds an actual monthly support-hour limit below the declared annual allocation ceiling. Support plus any software qualification hours must fit that current limit. Integration hours retain their separate inherited budget; no work is relabeled to evade either constraint.

The reference actual allocation is 25 hours in months 0–3 and 60 in months 4–7. The announced schedule initially matches it. One current-configured robot requires exactly 65/6 recurring support hours per month under the inherited synthetic mapping; two fit 25, three do not. A separate actual series can fail to deliver the announcement. Start decisions do not read future actual allocation, future yield results, future receipts or future debt outcomes. Full inputs preserve both series so the distinction is replayable.

Three declared policies govern candidate starts:

| Policy | Additional admission rule beyond physical/funding checks |
|---|---|
| Funded only | Require a remaining growth request and potential delivery inside the observed window; otherwise use the inherited actual physical and cash checks. |
| Current capacity and cash reserve | Require the proposed retained-plus-candidate fleet to fit the current actual support allocation, then preserve the declared recurring support cash reserve. |
| Announced capacity and cash reserve | Use announced support at the earliest commission month implied by current assembly and shipping leads, then preserve the same cash reserve. |

All policies preserve actual physical failure reasons, including existing support shortfall and component scarcity. They cannot invent a spare, cancel old obligations, backfill service or bypass the base default policy. A candidate that cannot commission inside the observation horizon is rejected; future value outside that horizon is not inferred. Stable candidate/unit order is an explicit policy choice, not an optimal investment strategy.

Known retained-unit configurations determine their own projected recurring support hours and software prices. Frozen cohorts retain their older cost; a new candidate uses the current configuration as a planning premise, not an assumed future qualified release. The current default mapping is $716.29 physical support plus $125 software per robot-month. Planned support hours sum the known cohort requirements plus the candidate. A planning assertion does not establish qualification or future support availability.

## Cash reserve and its limits

At the start decision:

`reserve = declared reserve months × (sum known retained-unit recurring support/software cents + candidate recurring cents)`.

`cash after manufacture = payer available cash − contingent manufacture invoice`.

The guarded policies require the second value to meet the first. The default reserve is two months. Available cash respects existing reservations and actual settled collections. Fixed current service has already been booked by phase 3; a cancelled start quote consumes no manufacture resources. This does not erase earlier failed manufacture or paid staff.

The exact initial boundary in the ample-hours, three-month fee-collection case is **$42,730.32** provider cash: $1,682.58 current support, $36,000 manufacture and $5,047.74 reserve for three units. One cent below rejects the initial candidate. This is an exact synthetic policy boundary, not evidence that a real budget can be estimated to the cent.

The reserve excludes commissioning, shipping, debt and other future obligations. At the exact boundary the order is admitted in month zero but commissioning fails for funding in months two, three and four, succeeding only in month five. Passing this gate is not full financing. Record future bills, claims and terminal inventory separately; no opening asset valuation, residual sale, investment return or lifetime ROI is computed. Included external operating-resource cash excludes loan principal and financing interest; loan cash/claims remain in the finance section. Zero paid resources in an unqualified/unfunded world is not economical service.

## Replay and interface

[The artifact](results/support_expansion.json) holds sixteen full worlds, complete opening inputs, source hashes, exact rational service/cents and per-case identities. `python3 scripts/export_support_expansion.py --check` recomputes all worlds. `--case downloaded.json --output replay.json` ignores saved results and restores the full physical, Treasury, commercial, enterprise, finance, annual/calendar and expansion-policy inputs. Rational components are decimal strings; integral numeric spellings are canonicalized before hashing. Historical reproduction needs the source revision matching the case.

The local `/api/support-expansion` GET verifies source hashes and serves the reference, presets and summaries. POST accepts exactly one `inputs` object or complete `saved_case`; null/unknown/invalid inputs fail. Customer adoption edits actual and announced hour calendars, admission policy, reserve, requests, actor cash, provider fees/lag, manufacturing lead, acceptance and components. Pending, invalid and stale requests preserve the last applied display/export. Full imports are read-only in shortcut controls until a standard witness is chosen; files are limited to 2 MB. Annual cell/year controls do not relabel this fixed cleaning workload. Four lineage records expose commitments, planning hours, cash reserves and actual service/resource execution.

The policy advances bounded DE-CF10. Full expanding-fleet optimization, observed reliability, qualified production/ramp economics, broader services and actual support contracts remain unresolved.
