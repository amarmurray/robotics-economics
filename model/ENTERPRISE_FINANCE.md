# Dated financing on shared monthly execution

This optional policy extends the existing [shared enterprise loop](SHARED_ENTERPRISE.md). It reuses the same physical unit IDs, paid support, demand assignments, commercial contracts, human staffing commitments and immutable Treasury. It is not an independent cash projection attached to an unaffected deployment forecast. Its Python implementation is [enterprise_finance.py](enterprise_finance.py); every contract term is synthetic.

The accepted previous shared case remains unchanged. `run_financed_enterprise(plan, treasury, contracts, enterprise, FinancePlan())` preserves its physical, customer and complete Treasury payloads, apart from the new wrapper, scopes and finance metadata. The default finance wrapper adds a separate funded capital lender. It never edits an opening account to fabricate a draw or a repayment.

## Contract and monthly order

`TermLoan` identifies a lender, borrower, principal, scheduled draw month, maturity month, exact rational monthly rate and principal-repayment rule. The lender is outside the provider/customer/lessor consolidation boundary. A current included actor can borrow; the reference borrower is the entrant, while the robot's independent lessor retains title. The unsecured reference lender therefore does not acquire the leased robot by default.

Each facility is authorized in month 0, phase 1; its only draw window is phase 2 of the declared draw month. Authorization does not create cash, principal or interest. The scheduled draw succeeds only if the lender has sufficient unencumbered funds. A failed draw is not silently retried. To model a different schedule, change the declared inputs. Maturity must follow the draw month and may fall beyond the finite execution horizon; that leaves an outstanding claim, not free capital.

| Phase | Existing execution plus added policy |
| --- | --- |
| 1 | Record ordinary commitments; authorize new facilities at month 0; invoice current interest on opening principal |
| 2 | Collect eligible sales, funded equity and service receipts; execute scheduled funded loan draws |
| 3 | Refund eligible deposits; pay ordinary mandatory invoices and debt according to the selected order; determine debt default/cure; then admit paid support for installed robots |
| 4 | Receive qualified components and commission eligible paid units |
| 5 | Pay/admit shipping and declared assembly candidates; apply customer moves; later starts also face the optional cash reserve gate |
| 6 | Deliver only service supported by actual qualified paid capacity and assigned demand; issue delivered-work invoices |
| 7 / close | Report stocks, cash, unpaid obligations, credit claims, current default state and retained asset title/custody |

The two payment priorities are `operations_then_debt` and `debt_then_operations`. “Operations” here means the already-issued mandatory business/lease/material obligations paid by the shared scheduler. Physical support, commissioning and starts still occur afterward in their existing phases. Neither priority is asserted to be a legal waterfall, a real loan covenant or an optimal survival policy. The generic actor boundary retains unrelated opening obligations explicitly rather than calling them financing or resource costs.

## Interest, maturity and recovery equations

For loan `l` and month `m`, with exact rate numerator `n` and denominator `d`:

```text
interest_cents[l,m] = round_half_up(opening_principal_cents[l,m] × n / d)
closing_principal[l] = actual_draws[l] − actual_principal_repayments[l]
closing_interest_claim[l] = issued_interest[l] − paid_interest[l]
net_financing_cash = actual_draws − actual_principal_repayments − paid_interest
```

A draw in phase 2 first incurs interest in the following month. A repayment in phase 3 pays that month's already-accrued opening-principal charge. This is a coarse monthly arrears convention, with no daily proration, fees, penalty rates, taxes, compounding or interest capitalization. Unpaid principal continues to accrue the same simple monthly charge after maturity. The exact rational charge and its half-up cent rounding are exported. Zero rate and half-cent examples are tested.

Interest is an ordinary noncancellable, partial-payment-allowed Treasury invoice. Principal is a Treasury credit claim and is never also issued as an invoice. At maturity and each later month, the policy attempts recovery of outstanding principal after due interest, using either partial-allowed or full-or-nothing repayment. Distinct loans use a disclosed loan-ID ordering. Interest arrears for a borrower block principal payment; they do not vanish when the business stops. Opening credit facilities without servicing terms are rejected rather than silently ignored.

After phase-3 settlement, an actor is in debt default if due interest remains or principal remains after its maturity. `suspend_until_cured` bars operating admission until those amounts are paid; `stop_permanently` retains the operating halt even after a funded cure. The first default and later cure are recorded. Paying debt does not by itself satisfy unpaid operating commitments or purchase the support needed for service. Existing readiness checks still apply.

This is **cash recovery only**. Previously billed customer receivables may still settle, or an explicitly scheduled investor may fund equity. Recovery uses those actual funds. There is no asset repossession, collateral sale, debt discharge, invented salvage cash or automatic contract cancellation. Installed units, their lessor title, customer assignments, lease obligations and future costs remain in the ledger. A stopped operator can therefore leave demand unserved while continuing to owe money. Full insolvency, secured claims and physical recovery/redeployment require additional policies and evidence.

For a later declared assembly candidate:

```text
reserve_gate = available_provider_cash − candidate_start_invoice ≥ declared_reserve
```

Actual available cash already excludes Treasury encumbrances. The normal support/spares, slot, funding and other admission rules also apply. The reserve gates month-1-and-later candidates; it does not create orders, accelerate receipts, value future receivables or guarantee coverage of every future obligation. A blocked contingent start invoice is cancelled without creating a robot. This is a funded reinvestment policy over declared candidates, not an optimized autonomous investment strategy.

## Cash and resource boundaries

Loan draws and principal recovery are financing transfers, never sales or physical resource expenses. Interest is a payment to the external capital provider in the current consolidation boundary; including that lender would eliminate the transfer rather than remove any underlying capital opportunity cost. No opportunity-cost estimate is supplied here. Hardware purchase transfers among included parties still cancel; manufacture, support and enterprise vendor outlays retain the earlier boundary.

`finance.consolidation` reports actual draws, principal recovered, interest paid, remaining principal/interest claims and any other boundary cash not classified by the existing business ledger. The reference and seeded cases reconcile that residual to zero. Complete Treasury events preserve total cash across **all** actors; minimum reserves, deposits and invoice reservations cannot be spent twice. Claim identities reconcile actual credit events. Terminal cash alone is not profit, valuation, available credit or the full cost of the service.

Every numerical result remains in `WORK-FLOOR-BUNDLE-SYN-02`, the existing invented accepted-service bundle. It is not converted into hospital deliveries, inspection points, components or annual labor hours. The annual digital and four-architecture bridges are still separate work. No source evidence calibrates the loan rate, customer price, service quantity, payroll commitment or recovery terms.

## Replay and controls

```sh
python3 -m unittest discover -s tests -p test_enterprise_finance.py -v
python3 scripts/export_finance.py
python3 scripts/export_finance.py --check
python3 scripts/export_finance.py --case saved-financed-case.json --output replay.json
```

`model/results/enterprise_finance.json` contains fourteen named worlds, full opening inputs, exact Treasury/physical/customer ledgers and code hashes. They develop DE-CF11 and DE-CF12; their number does not establish completion of the campaign's broader counterfactual coverage. The one-cent pair tests a specific service-funding boundary, not a global optimum across policies. The same inputs and source revision reproduce the entire case and hash. Historical results require their matching source revision; recomputation never trusts downloaded result fields.

Customer adoption now includes this financed version of the shared monthly case. Select a witness, edit explicit assumptions and apply. Pending or invalid edits do not replace the last valid display/export. **Export financed case** saves the complete execution. **Reload financed case** recomputes those full inputs; imported cases are inspectable/exportable, and selecting a standard witness restores its editable controls. Original annual and shared-case imports keep their own scopes. New API routes are read-only computation: GET `/api/enterprise-finance` for witnesses and POST with either `inputs` or `saved_case`.

Each new metric includes equation/input/function/provenance lineage. Browser tests cover recalculation, invalid inputs, stale responses and full export/reload. Model tests challenge empty-policy parity, insufficient lender funds, delay, interest rounding, maturity, partial recovery, cure versus permanent stop, lessor default, cash reserve, retained assets/demand, multiple loans, exact replay and seeded cash/principal/demand conservation.
