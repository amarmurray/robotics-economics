# Funded asset recovery and the surviving service obligations

Edition 0.28. [The decision analysis](../research/asset_recovery.md) extends the existing calendar/finance/enterprise/commercial/physical/Treasury execution chain. One optional transition in the shared physical engine moves an identified installed robot back into transit. The policy neither creates another physical engine nor assumes a legal right to seize property. [The sole-writer review](../reviews/asset_recovery_review.md) records validation and limitations.

## Declared transaction and service boundary

The eight-month synthetic cleaning fixture, months 0–7, has 900 due zones per month: 500 assigned to the incumbent and 400 previously unmet requests assigned to the entrant before operation. Assignment changes no demand total. One entrant robot predates the cash window. Opening assets receive no invented valuation or paid acquisition history. Staff, overhead, digital service and customer collections use the existing enterprise ledger. Model-derived fractional zones are expected accepted service, not observations of unique completed jobs.

The entrant receives a funded $20,000 loan, with zero interest and month-one maturity in the reference. A separately declared inherited $15,000 engineering payable consumes actual cash and is classified once as an external resource expense. It is neither free capital nor an asset purchase price. The weakly staffed buyer starts with $200,000. A stronger human comparator funds the existing full staffing allowance; no staff are removed automatically when the robot arrives.

The reference makes one month-one offer for the entrant's identified asset: $20,000 consideration plus $1,000 initial relocation resources, with two months in transit. These amounts, rights and timing are assumptions. They are not quoted offers, salvage estimates, secured priority, jurisdictional rules or a financial recommendation. The supported positive transaction is limited to an installed asset actually owned by the operating customer under a sale arrangement, sold to a distinct operating customer under another sale arrangement. An independently owned lease asset cannot be sold by the defaulted lessee. Lease repossession, service-contract novation, lender seizure and auctions remain unmodeled.

## Exact sequence, permissions and actual funding

1. Phase 1 prepares separately identified contingent purchase and relocation invoices. Their eligibility and due time are phase 3 of the declared offer month.
2. The existing collection, committed operating obligations and debt settlement run first. The owner must be in the current debt-default set, own the installed unit and have explicit declared old-site release and configuration-transfer permission. The buyer must be a distinct eligible operating account. One shared shipping slot is required.
3. An immutable candidate Treasury settles both purchase and initial relocation. If either cannot be fully paid, the candidate is discarded and both contingent invoices are canceled in the actual Treasury. Title, cash and physical location remain unchanged. The previous owner's actual obligations are retained.
4. A funded accepted transaction transfers title, cancels the old site's contingent current support/software booking and moves the same unit ID from installed to transit. It consumes one shipping slot also used by new hardware. The asset cannot serve either site during the transfer month. The lender never becomes its owner automatically.
5. At or after the declared arrival month, the existing loop must separately fund and admit commissioning, qualification, support, software and finite engineering resources. A blocked later qualification does not undo the completed sale. The buyer retains the paid, unavailable asset in transit, which denotes the not-yet-commissioned pipeline rather than a claim that a truck keeps driving.
6. Sale receipts can repay claims only at the next applicable scheduled debt settlement. They do not reopen the debt phase already executed that month. Interest, remaining principal, customer assignments, old staff/payables and each legal cash account remain in their original ledgers.

The physical audit enforces `installed_close = installed_open + commissioned − relocated` and `transit_close = transit_open + shipped + relocated − commissioned`. Shipping plus relocation cannot exceed that month's shared slots. Transfer invoices must be current, separate and fully paid; one payment cannot fund two units. Cases without a recovery policy retain their original physical result shape and calculations.

## Three distinct economic views

The buyer pays actual consideration, initial relocation and subsequent funded obligations. The seller receives the consideration and retains credit claims and operating commitments. The lender recovers only actually settled principal and interest. At the consolidated operating boundary, asset consideration is an internal transfer; initial relocation is an external resource expense counted once. It is included in enterprise outlay and must not be added again from the recovery summary. Existing physical/enterprise/finance outputs preserve all actor accounts, vendor resources, loan cash and remaining claims.

The reference lender has already recovered $9,858.71 before the sale and retains $10,141.29 principal at the end of the sale month. Actual later cash clears that claim in month two. It would be wrong to attribute all $20,000 of recovered principal to the sale. No debt forgiveness or extra terminal asset value is inserted. A low $3,000 sale restores buyer service but leaves $8,091.29 principal unpaid at the end of the window.

The exact purchase-plus-initial-relocation boundary is $19,714.00 buyer opening cash: actual receipts and already paid obligations leave $21,000 available at the offer. One cent less blocks both transfers. At the exact boundary the buyer ends the sale month with zero cash; later receipts nevertheless fund month-three commissioning in this fixture. This boundary proves the declared transaction rule, not complete future financing or realistic forecasting to the cent.

## Reproduction and interface

[The saved artifact](results/asset_recovery.json) contains fourteen complete worlds, opening inputs, exact rational output, source fingerprints, case identities, title/physical/debt history and four lineage records. Run `python3 scripts/export_asset_recovery.py --check`. Replay a downloaded complete case with `--case downloaded.json --output replay.json`. Replay restores inputs and discards saved outcomes; historical reproduction needs matching source code. Malformed or incomplete inputs fail instead of trusting cached results.

The local `/api/asset-recovery` GET validates source hashes and returns the reference, presets and summaries. POST accepts exactly one `inputs` object or `saved_case`. Customer adoption and Commercial models expose price, relocation, dates, actor cash, shipping/commissioning capacity, rights, qualification and the stronger human buyer. Pending edits, invalid requests and stale responses preserve the last applied display/export. Imports are read-only until a standard witness is selected; files are limited to 2 MB. Annual cell/year selectors do not relabel this fixed cleaning fixture.

The extension advances bounded DE-CF11/12 and DE-04. Fourteen named families remain, now with 158 saved worlds. Legal priorities, realistic valuation, restructuring, optimized recovery/investment and empirical whole-life economics remain unresolved.


## Public-document challenge, edition 0.29

FG-AUDIT-03 in the existing customer package is evidence navigation, not an additional recovery policy. [The follow-up](../research/asset_recovery.md#supplier-contract-challenge-edition-029) does not resolve the model's release, transfer or qualification flags for a target. Those remain assumptions. `recovery_contract_summary` in `research_calculations.py` checks source identity, population, period, units, a positive planned clock and financing duration. It reports two currency-specific divisions and component totals without overwriting source headlines or importing them into any scenario. Complete equation/input/source lineage is in [observed_research_summary.json](results/observed_research_summary.json); six missing target outcomes remain null.
