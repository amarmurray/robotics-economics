# Annual resource commitments in monthly competition

Status: bounded synthetic integration, edition 0.30. This extends the existing competitive cleaning-service execution. It does not execute the other annual markets or create a second fleet or Treasury.

## Contract and equations

Each observed calendar year has exactly one `ResourceYear`. The annual engine's reference pools are the authority: 12,000 support hours and 2,400 integration hours in the standard case. Inputs declare whole minutes already used before this observation window and reserved elsewhere. Omitted balance fields in a valid dated row default to an explicit synthetic zero; complete exports materialize those zeros. They are not missing source observations. Both are assumed opening allocations, not measured workloads. An observed year beginning in January must have zero prior-window use. Missing, duplicate, unordered, out-of-window, negative, Boolean, fractional and overcommitted rows are rejected.

For resource `k` and calendar year `y`:

```
available[y,k] = 60 * annual_pool_hours[k] - prior_use[y,k] - reserved_elsewhere[y,k]
remaining[y,k] = available[y,k] - successfully_booked_here[y,k]
```

A supported unit uses `60 × annual operation support hours / 12` minutes, plus `60 × actual upgrade qualification hours` when a software upgrade is required. New commissioning also uses `60 × integration_hours` in the separate pool. The standard unit requires exactly 650 support minutes per month and 4,200 integration minutes when commissioned. Rational arithmetic preserves other valid fractional requirements; integer-minute controls do not round a booking down.

Both the existing monthly ceilings and remaining annual amounts must admit the complete booking. Support/commissioning, first rent where applicable, robot software and qualification payments retain their existing atomic contingent settlement. A failure commits neither the candidate payments nor annual resource usage. Already committed rent, staffing, site subscriptions, debt and other bills retain their own contracts. Annual capacity is not a cash reserve and cannot pay any of them.

The annual counter advances only by the successful change in the existing monthly resource counters. Assertions check that identity. Installed support precedes new commissioning in the existing deterministic physical order. This order is disclosed; it is not an optimal allocation. Each attempt records its unit, operator, date/phase, required resources, remaining resources, actual commitment and refusal reason. Repeated refusals are attempts, not a count of unique lost robots.

Calendar boundaries follow the existing start year/month, not a rolling twelve-month index. Unused capacity does not carry; January capacity cannot fund December bookings or backfill missed service. Calendar-year output contains only the observed months. Outside reservations do not create an expense, cash transfer, accepted output or claim that an outside obligation was fulfilled.

## Same physical and commercial execution

`_ResourceEnterprise` extends `_CompetitiveEnterprise` and invokes the existing `_BridgedEnterprise.admit`. Manufacture, qualified component receipts, rejection losses, shared shipping, unit identities, commissioning, support and customer service still pass through `run_monthly`. Funded supported capacity feeds the existing conventional bid/renewal rule, locked prices, delivery, invoices and collections. No separate optimizer's result is added to these ledgers.

The unreserved control exactly preserves every prior `prompt_response` execution field other than the explicitly different wrapper identity, source hashes and new resource section. The earlier modules and artifacts remain authoritative and unchanged in substance. Complete replay reconstructs opening physical, commercial, Treasury, enterprise, finance, bridge, competition and resource inputs; it ignores saved output totals.

## Reproduction and interface

```sh
python3 scripts/export_annual_commitments.py
python3 scripts/export_annual_commitments.py --check
python3 scripts/export_annual_commitments.py --case saved-resource-case.json --output replay.json
python3 -m unittest tests.test_annual_commitments -v
```

The accepted export is [annual_commitments.json](results/annual_commitments.json). `GET /api/annual-commitments` supplies the catalog and control case; `POST` accepts exactly one `inputs` or `saved_case` object. The Customer adoption panel exposes annual prior use/reservations and monthly ceilings, exact replay, pending/invalid/stale-response protection and five metric-lineage entries. It remains independent of the ordinary annual cell controls. Export always uses the displayed last valid case.

## Remaining boundaries

This implements annual support/integration allocation within one cleaning-system competitive window. The six-cell annual engine's separate actuation, onboard-compute and memory vectors have no established conversion to the monthly generic component module. No conversion, fractional fleet import or second resource supply is invented. Qualified component deliveries and physical stocks remain explicit in the monthly plan, but a joint annual component/BOM execution remains open.

Outside commitments are a declared unavailable envelope. Their sites, schedules, fulfillment, cash and labor are not simulated. This wrapper does not combine the separate finite-expansion policy, acquisition, recovery or all intelligence architectures into a single company optimization. Source terms, real annual staffing plans, rights, portfolio priorities and full costs are still unknown. See [the decision analysis](../research/annual_commitments.md) and [self-review](../reviews/annual_commitments_review.md).
