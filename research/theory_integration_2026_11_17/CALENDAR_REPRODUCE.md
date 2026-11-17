# Calendar qualification model: reproducing the integrated result
This directory extends the *same* theory manuscript with dated accepted-service receipts and qualified learning events.

- [Integrated proof note](CALENDAR_FINANCE_CONTINUATION.md), [evidence boundaries](CALENDAR_EVIDENCE.md), [exercises](CALENDAR_TEACHBACK.md), [separate solutions](CALENDAR_SOLUTIONS.md).
- [Standalone JavaScript model](calendar_model.mjs): Node 22 or compatible ESM; standard library only; run the 15 assertions with \`node test_calendar_model.mjs\`. The JavaScript numerical functions were directly checked with 15 V8 assertions **at publication**, while the checked-in Node test file itself was not separately executed in a Node process. Do not misstate those as full CI.
- [Results and checks](calendar_results.json) contain only synthetic normalized values, and independently computed Python/SciPy benchmarks.
- Independent local Python/SciPy exact occupancy/quadrature plus adaptive Bellman module ran 19 tests and reproduced its results byte-for-byte in a clean directory; the local extended source/archive was not uploaded to this Git branch. Its user-accessible conversation artifact is separate. This is not independent expert review.

Model assumptions include distinct development/operating resources, qualified accepted production, immediate net collected cash in the theoretical example, known Poisson hazards, no right to borrow in the cash-path identity, and unlimited finance only for the unconstrained adaptive HJB. The evidence ledger does not estimate these parameters. The next experiment must put receivable maturity, supplier/financier and customer liability into the cash-state recursion. Preserve old Q10/Q11 files and the untouched main branch.
