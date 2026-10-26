# Monthly commercial schedules on one physical plan

Stage 3 adds **synthetic sale, independent lease and provider-owned availability service** to the same paid-physical engine. It reuses [monthly_deployment.py](monthly_deployment.py) for every stock, assignment, constraint and output, and [treasury.py](treasury.py) for every financial settlement. The default stage-2 API and its six complete witness artifacts are unchanged. This closes a bounded contract comparison, not the full company, entrant-demand or annual-model integration.

## Reproduction

```sh
python3 -m unittest discover -s tests -p test_monthly_commercial.py -v
python3 scripts/export_monthly_commercial.py
python3 scripts/export_monthly_commercial.py --check
python3 scripts/export_monthly_commercial.py --case downloaded-case.json --output replay.json
```

`run_commercial(plan, treasury, contracts)` returns a detached JSON-compatible case. One frozen `Contract` is required for each operator/site in the shared `Plan`. All prices and fees are integer cents; currency comes from the common Treasury. `commercial_artifact()` returns ten deterministic cases, a summary, the three executed source-file hashes and a content hash. `replay_case(saved)` reconstructs the plan, contract terms and opening financial journal, including deposits, reservations and credit, then calculates new results. It does not accept the saved closing balances as proof of a calculation. Historical reproduction requires the matching source revision.

The local dashboard's existing Business models view and `GET /api/monthly-commercial` expose these same ten cases. The witness picker and dedicated export preserve their exact monthly inputs. Annual sliders, cell/year filters and annual scenario import do not apply to this fixed fixture. A monthly file is replayed with the command above.

## Physical, payment and control boundaries

The [stage-3 design](monthly_commercial_design.md) is the detailed contract. All worlds request one month-0 start, month-1 acceptance/shipment, month-2 commissioning and five months of stated demand/capacity. Adverse inputs may prevent those steps. The same engine applies existing-service priority, consigned components, actual full payment, lead times and a single commissioning-month quarter ramp. Fully funded worlds deliver 0, 0, 25, 100 and 100 accepted service units.

The provider pays bundled manufacture and transport in every world. A sale customer or independent lessor pays the hardware price only when an accepted unit is successfully shipped. Shipment and purchase settle as one returned transaction: a later transport shortfall commits neither purchase receipt nor title. The customer pays commissioning/support in sale and lease worlds; the provider pays them in service. First-period lease rent and commissioning settle as a second atomic group. These are immutable serial simulations; no external payment or robot actuation is executed.

An accepted, paid shipment may finance a **later** start in the same phase. This deliberate extension of the initial conservative design has an actual asset and settled receipt before the subsequent start. A future sale cannot finance its own manufacture. Opening receivable collection schedules may name any included actor in stage 3; stage 2 retains its provider-only rule. No credit line is drawn automatically.

Title remains with the provider for unshipped stock and service robots, passes to the customer for sale, and to the lessor for lease. New WIP/finished/rejected units are assumed in the manufacturing vendor's custody; historical finished stock is at the provider. Transit custody is assigned to the deployment vendor, and installed custody/workflow authority to the customer. These explicit synthetic custody assignments are separate from ownership. Data and IP rights remain unspecified. Opening installed assets use the selected arrangement's historical owner without charging new manufacture or purchase; their prior investment is outside the horizon.

## Obligations and failure

Installed lease rent is a noncancelable obligation, collected before physical support. It continues to accrue while the asset remains installed, even after support suspension. Conditional first rent is canceled if commissioning fails. Service fees are earned only for actually supported robot-months, issued in phase 6 and collected after a positive monthly lag. Availability pricing is independent of demand utilization and includes the commissioning month without fee proration, despite the quarter output ramp. Neither contract creates end-market sales revenue.

Due lease/service obligations are attempted oldest first for each payer. A failed full payment leaves the entire balance outstanding. Contract arrears suspend support, commissioning and new shipments under that contract; there is no automatic cross-default across separate contracts. Paying arrears permits the next actual support attempt, without manufacturing, reinstallation or a second first-month ramp. The shared conservative physical rule also prevents all additions while any existing installed unit is unsupported. Unpaid assets stay installed or in transit; they are not deleted, repossessed or valued as recovery proceeds.

Optional security deposits are actual transfers and continuing refund liabilities. They are never credited against hardware price or converted to revenue. Restricted deposits cannot fund starts; spendable deposits can, but cancellation may leave an unfunded refund. A deposit is attempted only at month 0 phase 2; a failed required deposit blocks shipment. Cancellation is supported only before first shipment/opening installation at that site. It prevents future shipments, requests refunds and retains sunk WIP/finished stock. Failed refunds are retried monthly. No new starts occur when every contract is canceled; provider overdue noncancelable obligations or refund failures also block new starts. An unrelated obligation has no automatic payment schedule in this extension.

## Accounting and interpretation

The consolidation includes provider, customers and lessors; vendors are outside. Internal hardware prices, rents, service payments and deposits cancel from included cash change. The physical-outlay subtotal contains only this run's settled manufacturing, transport, commissioning and support invoices. Opening unrelated obligations and receipts have a separately visible boundary effect. Opening cash for this comparison is the supplied Treasury's actual opening snapshot, including any preexisting journal, not a second injection of its original account balances.

For the funded reference, external physical vendor outlays are **$37,400** in all three arrangements: $36,000 manufacture, $100 transport, $1,000 commissioning and $300 support. This is a bundled cash proxy for included physical work, not a complete economic resource cost: supplier working capital, fixed facilities/staff, human fallback, energy outside the bundle, depreciation, residual value, financing charges and enterprise/customer formation remain outside. End balances, receivables and refunds are not profit.

The sole-lead [review](../reviews/monthly_commercial_review.md) records numerical witnesses, 22 focused tests, 45 seeded cross-world runs, exact old-artifact preservation and saved-input replay. All terms are invented. Real contractual enforceability, cost calibration, technical commissioning, demand competition, entrant formation, reinvestment, loan scheduling and a bridge to annual or K architecture economics remain open.
