# Structural-zero common-law calculation: reproduction and assumptions

Run from repository root:

\`\`\`sh
node research/theory_integration_2026_11_17/data_value/structural_zero_common_law.js
\`\`\`

The source's deterministic exact-integer tick model is under denominator 160, sufficient for every P/G/E net payoff on a rational 1/16 p,θ grid. It covers 81 allowed (p,θ) cases and checks 509 exact assertions, the three program-winner witnesses, sharp G−P and single-program extrema and the unique rights-feasible finite audit allocation. The saved JSON is \`structural_zero_common_law_results.json\`. The grid is a **diagnostic**; the mathematical proof in the chapter covers the continuous trapezoid by linear inequalities and explicit mixture construction.

**Observation table:** reported positive/negative buyer atoms each 1/4, censored mass 1/2; p in [1/4,3/4]. Original buyer demand is invariant across old P/G and T only **for this restrictive counterexample**. Target T is legally and physically *permitted* but never logged; no e_T>0 is asserted. G's retained policy qualifies half of demand independently, its grounded policy pays iff original demand/qualification/worker-free coincide. E is independently resourced and serves a separate constant contract. All are synthetic net amounts, not empirical prices. Do not reuse this bounded result after changing T's demand response, controller support, or E's independence.

**Audit design:** 4 separate missing binary original-buyer entries with weights (6,4,3,1)/16; entry 0 cannot legally be observed, entries 1–3 cost one unit each, budget 2; no physical coupling across the missing bits. Exact minimal remaining width 7/16. The four-entry toy is distinct from the p,θ population sample and does not purport to estimate the same dataset.

No external libraries, confidential files or paid compute. This is scoped arithmetic verification, **not** full-repository CI, peer review, an approved intervention or an actual customer invoice dataset.
