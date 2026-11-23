# Reproduction: variable-duration customer renewal

23 November 2026. Conditional synthetic model, not field data. Run from repository root in a Node-compatible CommonJS runtime:

    node research/theory_integration_2026_11_17/data_value/variable_duration_renewal_exact.js

The [model](variable_duration_renewal_exact.js) enumerates all six choices of the two long K positions among four equiprobable latent types g=(1,1,2,2), under three coherent cross-program duration regimes. The [results](variable_duration_renewal_results.json) record each original A accepted by deadline4, newly authorized B after completion by deadline3, unchanged separated G/K observable histograms, full GK payoff and an observation-timed safe policy. Normalized totals stored as integer **quarters** avoid rounding; divide by four to recover the chapter's per-eligible-cluster contribution.

The model's function ran in a V8 JS execution sandbox with **624 passing assertions** covering queue conservation, acceptance and buyer-budget conservation, observational equivalence, three duration-response forms, sharp ranges, all eighteen coherent common worlds, and the adaptive lower bound. An **independent Python fractions.Fraction** enumeration of the six k-marginal couplings and three duration maps computed neutral J=4-3z, synergy J=9/2, antagonism J=2+z, adaptive neutral/antagonism J=7/2+z, and synergy-safe J=4. No Node CLI execution or full-repository CI is claimed for this tranche; scripted assertions are numerical sanity checks, **not proofs**. Read the [propositions and assumptions](VARIABLE_DURATION_RENEWAL_AND_CUSTOMER_RESPONSE.md).

No customer research, signed transfer rights or real paired controller/worker evidence entered the deterministic model. The interval [2,9/2] is sharp *only for the explicitly declared duration envelope and this common-law family*; altering receipt tiers, cross-action demand, validation budgets, new robot staffing or overlap changes its support.
