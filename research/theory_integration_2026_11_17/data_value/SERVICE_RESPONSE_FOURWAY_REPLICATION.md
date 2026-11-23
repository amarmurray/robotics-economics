# Reproduce the synthetic four-way service-response certificate

From repository root with Node 20 or later:
\`\`\`sh
node research/theory_integration_2026_11_17/data_value/service_response_fourway_exact.js
\`\`\`
Compare stdout as parsed JSON to \`service_response_fourway_results.json\` (object-key order is inessential). The executable requires no packages, purchases, physical model or external data. Model variables are H = paid accepted t2 C quality, A/C = **original** late offers, W = free shared recovery worker; E has independent mobile/worker capacity. A and C offers are generated *after* H from latent U,V, while the t2 job uses the same U,V and realized H before t3; there is no backward causation.

The source enumerates eight H/U/V histories in each of two parity regimes, verifies every 1-,2-,3-way subtable is uniform, conserves one terminal shared service and the two-unit C buyer budget, verifies the inclusion-exclusion G payoff and R/P/E values, and checks the minimax mixture on a twentieth-grid (the exact continuous optimum follows algebraically). It returns 214 scoped exact JavaScript assertions, with synthetic theta0 G=9/5, theta1 G=23/10, E=43/20 and regret 21/200. The source was executed through an isolated V8 JavaScript function before publication; this is not a claim that the Node CLI, all repository tests or CI ran. Independent Python \`fractions.Fraction\` enumeration in the research session reproduced parity, values, threshold 3/80 and minimax regret, but no separately committed Python interpreter script is claimed as executed.

The generalized finite-law identification and prospective audit claims follow the written algebra and stated causal assumptions, not the test count. Program-invariant R-to-G transport is **not** assumed. Numeric BEA interindustry coefficients, customer payments, signed G rights, physical randomization, independent E resources and external scientific-priority review are unavailable.
