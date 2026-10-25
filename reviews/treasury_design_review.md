# Independent treasury-design challenge

The lead reviewed the implementation owner's `model/treasury_extension_design.md` v0.2a. This reviews a proposal, not executable code or empirical financeability. The existing engine remains unchanged by the proposal.

The design usefully separates legal actors from roles, real cash from invoices/commitments, stock from custody/title, and funded execution from an additional-financing counterfactual. The six numerical witnesses have coherent arithmetic under their stated boundaries. The bundled all-in-start cost prevents charging components and manufacturing twice, while explicitly leaving supplier working capital outside the actor perimeter. That last boundary may be inadequate for a real supplier-financing decision and must remain an assumption.

Two ambiguities should be resolved before implementation:

1. **Reservation settlement must be atomic and specific to the obligation.** The spendable-cash formula subtracts earmarked commitments, but paying the very invoice backed by an earmark must be allowed to consume that reservation. Otherwise cash 100 with a 100 reservation cannot pay its own 100 invoice, producing a false funding gap. The same amount also cannot be counted simultaneously as restricted cash, minimum reserve and earmarked cash. Define disjoint encumbrance accounting or an explicit priority/overlap rule; test release on payment and cancellation without creating new cash.
2. **Event phases can create an extra monthly lag.** The proposed discretionary shipping phase precedes assembly completion. A lot completed in month m therefore cannot ship in phase 4 of m unless a separate rule permits it; it ships no earlier than m+1. State whether that is the intended conservative convention, and express promised lead times as event/phase pairs. Tests should distinguish a declared assembly duration from a hidden extra period at a phase boundary. Commissioning followed by same-month operation likewise requires an explicit fractional exposure/ramp rule.

Required additional witnesses: (a) cash 100, reservation 100 for invoice A; payment A settles once and closes both cash and reservation at zero, while unrelated invoice B cannot consume it; (b) cancel A before payment and release the reservation without changing bank cash; (c) one assembly lot whose promised completion/shipment/commissioning events fall on adjacent phase boundaries, with the exact expected service exposure stated.

No design-level reason was found to abandon the proposed extension. Acceptance is conditional on these clarifications and the future executable adversarial tests. This document does not convert the proposed monthly treasury, shared entrant supply or default mechanism into an implemented requirement. Actual credit terms, risk, pricing and calibrated demand remain open.

## Owner clarification recheck

The revised proposal resolves both design ambiguities: encumbrances are explicitly disjoint, a payment atomically consumes its own earmark, and unrelated actions cannot use it. Completion now precedes discretionary shipping, with start/acceptance/shipment/commissioning event-phase pairs and a single first-month ramp. Two added exact witnesses cover the reservation and timing cases. The proposal is suitable to implement in bounded stages; it remains unimplemented. During implementation, payment-at-acceptance clauses must also receive explicit settlement phases or a positive collection lag so a milestone invoice cannot accidentally become unearned same-phase cash.
