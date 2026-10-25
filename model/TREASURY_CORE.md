# Treasury stage 1: exact financial settlement

This is the implemented **financial core only** of the [treasury extension design](treasury_extension_design.md), not the completed extension. [treasury.py](treasury.py) is an isolated, standard-library module. It does not change annual scenarios, evidence, entrant robot availability, dashboard calculations, production or commissioning. All supplied witness amounts are synthetic accounting fixtures, not observed financing terms or calibrated robot economics.

The core separates an economic opportunity from cash survival. A hypothetical start costing $40,000 and collecting $60,000 next month has an expected $20,000 gross spread under the fixture assumptions. That future receipt cannot pay today's start. A funded creditor can change the settlement outcome; an undrawn commitment alone cannot. Whether the start produces an accepted robot, whether the customer owes the sale price, and whether the spread covers lifecycle resource costs remain external questions at this stage.

## Run and inspect

From the repository root:

```sh
python -m unittest discover -s tests -p test_treasury.py -v
python -m model.treasury
```

`financial_witnesses()` returns the same deterministic, JSON-compatible data printed by the CLI: six named snapshots covering witness 1 with/without a draw and the financial portions of witnesses 2, 3, 5 and 7. Every snapshot reports `scope: synthetic_stage_1_financial_core_only`, actors, invoices, deposits, reservations, credits and the complete event log. Intermediate balances can be reconstructed from opening cash and the ordered event postings. The standard output is an export; the module does not write files or alter saved annual results.

## Monetary and actor contract

All operational amounts are **integer cents**, not floating-point dollars. `usd("1000.25")` returns `100025`; conversion rejects Booleans, floats, NaN, infinity, negative values and fractional cents. It is exact even under a reduced Decimal arithmetic precision. Raw cent inputs accept only Python `int`, with zero permitted for opening balances and reserves; new obligations and settlement requests must be positive. There is no implicit rounding or currency conversion.

`Account(actor_id, opening_cash_cents, minimum_cash_cents=0, currency="USD", roles=())` defines one legal actor and one cash pool. Roles are descriptive and never add cash. Duplicate actor IDs, self-invoices, self-deposits and self-loans fail. All actors share one currency; mixed-currency construction fails. The three-letter code is a denomination label, not an exchange-rate lookup. Fixtures use USD.

Every counterparty, including suppliers, payroll recipients, customers and lenders, has an explicit account. Opening balances are the only exogenous money in this core. Cash always transfers between two accounts, so total included cash is conserved. An analyst may separately consolidate a subset of actors; the core itself includes all endpoints. A credit commitment is not a bank-created deposit: the modeled lender must actually have spendable cash to fund the draw.

For each actor:

```text
cash = opening cash + settled receipts - settled payments
available for a new action = cash - restricted deposits
                           - unconsumed invoice reservations - minimum reserve
```

Each encumbrance is funded from a disjoint part of the cash balance. Creating a reservation consumes available capacity, not cash. Receiving a restricted deposit increases bank cash and its matched restriction equally. A minimum reserve does not become spendable merely because another obligation is due.

## Immutable API and event time

All state and records are frozen dataclasses; nested lists supplied for roles, purposes, account collections or event postings become immutable tuples. Each operation returns a new `Treasury`; retain the old value for a historical snapshot or scenario branch. `snapshot()` returns detached JSON data, so editing an export cannot change live state. This is in-process immutability and an append-only API, not a signed ledger or a tamper-proof storage system.

Every operation requires a unique event ID, an explicit `Moment(month, phase)` and nonempty `provenance`. Month is a nonnegative integer; phase is 1–7. Events cannot run backward. Several events may share a Moment: their append order is explicit and economically consequential. The primitive does not implement the design's monthly scheduler or automatically execute mandatory payments before discretionary actions. A future integration must enforce that scheduling policy. Phase labels are described in the extension design; this core never infers a manufacturing completion or service exposure from them.

Invoice issuance must precede its earliest settlement Moment, which cannot be later than the due Moment. An invoice issued in phase 6 may settle at a later explicitly specified phase/month; there is no implicit immediate collection. Credit authorization similarly precedes the draw window, and a deposit precedes its refund-eligibility Moment. Equal issue/settlement Moments are rejected. A later API call cannot backdate settlement into an earlier event.

Invalid IDs, terms, money or chronology raise `ValueError` before a new state is returned. The original state and log are unchanged. A valid attempt blocked by liquidity, an unavailable draw window or future eligibility returns a **new state containing a blocked event**; cash, obligations, reservations and drawn credit remain unchanged. Callers must use the returned state to retain that attempted-action provenance. This distinction makes failed execution inspectable without silently changing balances.

```python
from model.treasury import Account, Moment, Treasury, usd

t = Treasury((Account("customer", usd("100")), Account("provider", 0)))
t = t.issue_invoice("issue-1", "invoice-1", "customer", "provider", usd("100"),
                    Moment(0, 1), Moment(0, 2), Moment(0, 3),
                    provenance="synthetic_contract_1")
t = t.reserve_invoice("reserve-1", "earmark-1", "invoice-1", usd("100"),
                      Moment(0, 2), provenance="approved_payment_1")
assert t.available("customer") == 0
t = t.settle_invoice("pay-1", "invoice-1", Moment(0, 3),
                     provenance="synthetic_settlement_1")
assert t.balance("customer") == 0 and t.reserved("customer") == 0
assert t.balance("provider") == usd("100")
```

## Obligations, reservations, deposits and credit

| Operation | Cash and remaining obligation |
|---|---|
| `issue_invoice(...)` | Records face amount, parties, issue/eligible/due Moments, policy, cancellation permission, grace and descriptive category. No cash moves. |
| `reserve_invoice(...)` | Earmarks available payer cash for one existing invoice, no more than its outstanding balance. A reservation has no independent payer override. |
| `settle_invoice(...)` | Transfers payer cash to the named payee and reduces that same invoice. It atomically consumes its own reservations first; reservations for other invoices remain unavailable. |
| `release_reservation(...)` | Frees the remaining earmark without moving cash or cancelling the invoice. Cannot release twice. |
| `cancel_invoice(...)` | If cancellation was permitted, closes only the unpaid balance and releases its remaining reservations. It neither refunds prior payments nor fabricates cash. |
| `place_deposit(...)` | Transfers actual cash and records a refund obligation. `restricted=True` segregates the recipient's matching balance; `False` allows spending but retains the refund liability. |
| `refund_deposit(...)` | Returns actual cash and reduces that deposit's obligation. Its own restriction may fund the refund. Other restricted deposits and invoice reservations remain protected. |
| `authorize_credit(...)` | Records a limit, parties, explicit draw window/maturity, permitted purpose tags and revolving policy. No cash moves. |
| `draw_credit(...)` | Requires time eligibility, an authorized purpose, remaining commitment and lender liquidity. Transfers actual lender cash and increases cumulative draws/principal. |
| `repay_principal(...)` | Transfers borrower cash to lender and reduces principal. A repayment request without settlement does not replenish credit availability. |

Invoice policy defaults to `full_or_nothing`. Insufficient spendable cash leaves the whole requested payment unpaid. An explicit `partial_allowed` invoice pays up to available funds or a specified smaller amount and retains the unpaid balance. Reservations are consumed only for money actually paid; full settlement leaves no orphan earmark. A partial obligation is marked as a partial event even when the caller requested only that part.

`invoice_status()` reports current or future status from the retained state. At the due Moment, an unpaid invoice is `due`; after due plus grace it is `defaulted`. A blocked/partial settlement attempt at or after the grace deadline marks it defaulted immediately. This is a deterministic diagnostic policy, not a legal finding. A later full payment closes the liability; the earlier failure remains in the immutable event history. Historical status queries on a later state are rejected: query the earlier retained state instead.

Deposit refunds are full-or-nothing for the requested refund amount, with explicit partial refund requests allowed. Repeated refund, over-refund and premature eligibility are checked. Spendable deposits can leave an unfunded refund liability after the recipient spends the money. No deposit is automatically converted to earned revenue or to an invoice payment.

Credit tracks two separate quantities:

```text
principal outstanding = cumulative settled draws - cumulative principal paid
nonrevolving availability = original limit - cumulative settled draws
revolving availability = original limit - principal outstanding
```

Principal repayment never restores nonrevolving capacity. Revolving availability reopens only by the principal actually repaid. There is no annual refresh, interest accrual, automatic refinancing or automatic principal collection. The maturity field bounds contractual timing; **maturity does not automatically create a repayment invoice, trigger collection, report credit default or recover assets** in this stage. Repayment may be explicitly attempted before or after maturity. Purpose tags constrain draw authorization; the core does not trace fungible borrowed dollars to later invoices.

## Exact synthetic witnesses and limits

Amounts in this table are USD. The design's witness table uses thousands of USD; conversion is explicit here.

| Witness | Executed financial result | Physical/economic portion still outside the core |
|---|---|---|
| 1, unfunded | Opening provider cash $50,000; payroll $20,000 paid; $10,000 reserve retained. Available cash $20,000 cannot fund the $40,000 start. | The hypothetical $20,000 gross spread does not establish useful output or lifecycle profit. |
| 1, funded | Explicit lender draw $20,000; payroll and start settle; provider cash $10,000 and principal $20,000. Next-month collection $60,000 and principal repayment $20,000 leave **cash $50,000**, principal zero. | The future sale invoice is an external synthetic contractual assumption, not a generated accepted-unit sale. |
| 2 | Two start invoices settle once at $36,000 each: cash $100,000 becomes $28,000. One $60,000 sale receipt gives $88,000, a $12,000 cash loss relative to opening. | No yield draw, accepted inventory, commissioning, title or alternative financier/lease schedule is simulated. |
| 3 | Customer transfers a restricted $20,000 deposit; cash becomes customer $10,000/provider $50,000 with $20,000 restricted. $40,000 start remains blocked. Explicit invoice cancellation and refund restore customer/provider cash to $30,000 each. | Cancellation is contractually allowed in this fixture; physical cancellation/recovery is absent. |
| 5 | Entrant cash $8,000 cannot settle the noncancelable $10,000 availability fee. Cash stays $8,000; financier receives zero; $10,000 remains outstanding and defaulted. | Service suspension, installed robot inactivity, repossession and asset conservation are not implemented. |
| 7 | Cash $100,000 entirely reserved for invoice A. Unrelated B of $1,000 is blocked. A settles and consumes its $100,000 reservation, leaving cash/reservation zero. | No physical action is inferred from the settled invoice. |

Separate tests cover cancellation release, restricted/available cash disjointness, partial settlement, lender liquidity, revolving/nonrevolving exhaustion, exact money/date validation, self-transfer rejection, immutable nested records, rejected-action atomicity and CLI equality. `audit()` runs at construction and after every returned transition. It checks cash conservation, balanced postings, nonnegative cash/free funds, unique record IDs, obligation payment replay, reservation consumption/release, deposit refunds and principal/commitment reconciliation. It is an internal consistency check, not authentication of externally constructed records or a general ledger import validator.

Remaining exclusions include monthly physical supply/commissioning/support, the entrant's shared robot pool, economic feasibility calculations, cohort title/custody, automatic reinvestment, equity schedules, revenue recognition, interest/fees, taxes, FX, dividends, write-offs, recoveries, endogenous credit approval, legal default consequences, persistence/concurrent writers and an annual-model/dashboard bridge. The full extension remains incomplete; these tests close only its bounded settlement foundation.
