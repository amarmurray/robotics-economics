# Independent review of the stage 1 treasury core

Review date: 25 October 2026. Reviewer: capability/learning lane, independent of the implementation owner. **Disposition: pass within the documented, isolated financial-core scope. No material implementation correction is required.** The review found no failure of the tested settlement, reservation, deposit, credit, time or conservation rules. This is not acceptance of the full treasury extension or a jointly financed physical engine.

The governing references were [the extension design](../model/treasury_extension_design.md) and [its independent design review](treasury_design_review.md). The implementation scope was [treasury.py](../model/treasury.py), [the owner tests](../tests/test_treasury.py) and [the core documentation](../model/TREASURY_CORE.md). The reviewer wrote only this review, the report-integration addendum and an ignored adversarial probe script. No implementation, evidence, economic input or saved result was edited. Launch repository provenance remains in ignored `sync_receipt.json`; the requested Astra/Ultra serving configuration is not independently observable.

## Verified behavior

The reviewer independently executed all **22 owner tests** and **9 additional adversarial tests**. Both suites passed. The additional script is retained locally at ignored `work/review_treasury_core.py`; it is not a published dependency. Its substantive coverage was:

| Probe | Independently verified result |
| --- | --- |
| Two actors, three invoices and four reservations | Partial payment consumes only the paying invoice's earmarks. Cancelling its unpaid remainder releases only its residual earmark, preserves prior payment and leaves the other actor and unrelated invoice reservations intact. Repeated payment/release is rejected. |
| Three deposits, a minimum reserve and an unrelated invoice reservation | A restricted deposit's refund uses its matched balance. Other restricted deposits, the unrelated reservation and the minimum reserve remain protected. A spendable deposit can remain an unfunded refund obligation after its cash is spent. |
| Restricted deposit beside revolving debt | A borrower with bank cash consisting entirely of a restricted deposit cannot use it for principal repayment. A later actual receipt funds partial repayment, reopening exactly that principal amount; an oversized redraw remains blocked. |
| Lender gross cash versus available cash | A lender's own minimum reserve and invoice reservation block a draw even when its bank balance exceeds the requested amount. Releasing the reservation permits only the newly available funding. |
| Invalid money across eight mutation APIs | **64 combinations** of Boolean, zero, negative, float, nonfinite and Decimal raw-cent inputs raise `ValueError` without changing the original state or log. Separate exact-dollar helper probes reject signaling NaN, infinity and fractional cents. |
| Event identity, chronology and provenance | Backdated events, duplicate event IDs and empty provenance cannot settle, cancel or release an existing encumbrance. Every rejected request leaves the supplied state unchanged. |
| Immutable scenario branches | A partial-payment branch and a cancellation branch from the same prior state remain independent. A valid but blocked attempt returns one new blocked event with no cash postings or changes to invoices, deposits, reservations or credit. |
| Settlement-capacity matrix | **114 cases** vary bank cash, minimum reserve, own and unrelated earmarks, invoice size and payment policy. Settled amounts match the independent cash-minus-protected-funds accounting expectation; the payer never spends another invoice's earmark. |
| Revolving/nonrevolving expiry and repayment | Actual repayment restores only revolving capacity. Neither facility refreshes with time, expired draws remain blocked, principal does not disappear at maturity, and explicitly requested late repayment can settle. Repeated repayment beyond outstanding principal is rejected. |

Cash conservation, nonnegative available balances and balanced event postings were checked throughout these probes. The owner suite additionally exercises future receivables, self-transfer and mixed-currency rejection, nested immutability, grace/default diagnostics, cancellation eligibility, blocked deposit creation, exact Decimal-context independence, immutable export copies and CLI equality. Those owner tests were executed by the reviewer, not merely accepted from the owner's report.

Invalid requests and blocked valid requests have different outcomes. Invalid requests raise without returning new state. Blocked valid attempts return a new immutable event and preserve financial records; callers must retain the returned state to retain the attempt. The review does not mistake an appended blocked event or advancing diagnostic invoice status for a cash mutation.

## Exact witness and export checks

The six snapshots are financial portions of design witnesses 1, 2, 3, 5 and 7. They reproduce the intended cash outcomes:

| Snapshot | Relevant financial result, USD |
| --- | --- |
| Witness 1, unfunded | Payroll leaves provider cash 30,000 and available cash 20,000 after the 10,000 minimum reserve. The 40,000 start remains unpaid despite a future 60,000 invoice. |
| Witness 1, funded then collected | An explicit 20,000 cash draw allows the start; provider cash is 10,000 immediately after payment. Next-month collection and 20,000 principal repayment leave cash 50,000 and principal zero. |
| Witness 2 | Two 36,000 payments leave 28,000; the stipulated 60,000 sale receipt produces 88,000. No second manufacturing charge is introduced. |
| Witness 3 | Restricted deposit cash cannot fund the start. Explicit permitted cancellation and refund restore customer and provider cash to 30,000 each. |
| Witness 5 | Cash remains 8,000; the financier receives zero and the 10,000 full-or-nothing liability remains outstanding and diagnostically defaulted. |
| Witness 7 | Invoice A consumes its 100,000 earmark exactly once. Unrelated invoice B of 1,000 is blocked; ending payer cash and earmark are zero. |

The reviewer called `scripts/export_experiments.exports()` without its write routine. Both stored experiment packets exactly equal fresh function results after JSON normalization, and both recorded code hashes match their current source files. The treasury CLI also passes the owner's directly executed equality test. These checks establish reproducibility at the reviewed snapshot; they are not authentication, publication or a guarantee against concurrent file changes.

The six finance table values in `REPORT.md` match the exported selected-actor balances. One low-severity wording correction was requested and applied by the lead: the heading now says **“a positive assumed spread can coexist with a cash shortfall”**, rather than claiming an economically profitable order. The assumed start/sale spread does not establish lifecycle profit, accepted physical output or observed financing terms. The report also explicitly identifies the missing automatic payment scheduler, credit-maturity collection/default and interest accrual. The companion [report integration review](report_integration_review.md) covers the wider experimental prose and its evidence boundaries.

## Scope limits that remain material

This implementation supplies exact financial primitives, not the design's monthly event scheduler. Equal-Moment events execute in append order; the API does not enforce that mandatory payments precede discretionary ones. A future integration must impose that policy and connect invoices to actual eligible physical events. Synthetic start and sale invoice names do not create manufacturing starts, accepted units, title, commissioning or service exposure.

Every endpoint has an explicit account. A draw transfers cash from a funded lender rather than creating bank deposits, and total included cash is conserved. This is a declared accounting perimeter, not a model of the banking system or endogenous credit approval. Purpose tags govern drawing authorization but do not trace fungible funds through later spending. Currency codes identify a denomination; no FX or currency-registry validation is implemented.

Restricted deposits, reservations and minimum reserves are disjoint constraints. The test results do not establish their legal enforceability, revenue recognition, real-world custody or recoverability. Invoice default is the documented deterministic diagnostic policy, not a legal conclusion. Credit maturity has no automatic collection or default consequence. Interest, fees, taxes, write-offs, equity schedules and automatic reinvestment are absent.

Frozen dataclasses and append-only API operations provide in-process immutability. `audit()` checks internal financial consistency; it does not authenticate caller-built records, prove historical authorization, accept arbitrary untrusted ledger imports, or provide durable storage/concurrent-writer guarantees. This review did not test hostile object subclasses, persistence failures, load, real financial interfaces or concurrent mutation outside the API.

The annual fleet and monthly entrant engines remain separate from this module. Shared robot allocation, physical supply and commissioning, service withdrawal, collateral/recovery and joint feasibility remain unimplemented here. Passing the stage 1 tests therefore does not close the treasury extension, calibrate economics or validate a deployed system. The bounded stopping condition is met: material operations, the exact financial witnesses and their stated limits have been inspected and independently exercised. The next integration test should connect one real model event chain to dated obligations and cash while preserving both financial and physical conservation; that work is not performed by this review.

## Reviewed file identities

SHA-256 values of the tested snapshot:

```text
model/treasury.py                       d1b63a6d977d9ce95e1e6748747b6e5692db05c61c1b56a139779d5492684f9f
tests/test_treasury.py                  d214f63ac60f0dcb84a84b12e8078ceeda771413c32042fec7a682eded1a1224
model/TREASURY_CORE.md                  290c4ea026db61c089f1bf5727bd2dc73697e0c9d2dab0db1936cea73121976b
work/review_treasury_core.py            15256c53f200c7da33b076720212009ebd165376c18cfb70d5e2cbb84264b226
scripts/export_experiments.py           5382d46397fb902cf45f96b75610de0cc8ca558f27324db25e51446ff3c5bc38
model/results/treasury_witnesses.json   3818ca949adf6d2bc8cf981ca105dd2092fcf15713a3aded18ac3cbff3765a36
```
