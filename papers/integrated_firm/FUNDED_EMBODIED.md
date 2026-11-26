# When capital funding can be quotiented out of competitive recursion

November 26, 2026. Input main `3b34ca1bd05545cc5fdcac0bb0989d728d838b61`; production `8dba84f45e18fe5896e75cd9a98539e4b87a83fb`; recursive `af1cabb95772524db1b34dda3b2667a54c203b43`. This is a longer restriction of [EMBODIED_GAME](EMBODIED_GAME.md), not a new unrelated technology.

## Economic premise and theorem

The date of a payment matters if it limits another decision. It also can act as a public coordination signal even when liquidity is slack. Separate the two. Let x be all noncash stocks (installed capacity, paid kits, qualified local models, retained procedure); b is inherited cash. For each firm, current receipts R_i(a_i,a_j), outlay c_i(a_i), next x distributed by the declared independent quarter-outcome law, and b'=b+R_i-c_i. Terminal wealth is b plus equipment salvage. Assume receipts nonnegative at every legal profile; a uniform upper bound Cbar on one-date outlay; B_i>=T Cbar initially; no cash-dependent demand, technology, contract or direct preferences other than additive wealth; no debt or intermediate dividends. Then every history and unilateral deviation satisfies b_i>=h Cbar at h remaining dates by induction. Hence cash does not change a future legal menu in this funded region.

Define the continuation as W_i(x_i,x_j,h), *excluding* already-held cash. At terminal W_i=salvage_i. At positive h form the bimatrix

    U_i(a_i,a_j)=R_i-c_i+E[W_i(x'_i,x'_j,h-1)].

At each subgame select a pure equilibrium by highest (or lowest) total U, then highest firm-0 U, then stable action order. Inductively lift this policy to the full public game by ignoring cash and using the same selection on every history. Adding b_i to every payoff for player i does not change best responses, total-payoff ordering or the firm-0 tie-break; the same continuation policy is therefore subgame perfect in the funded region. It is not an assertion that *every* public-history equilibrium ignores cash, nor that strategic cash signaling cannot select another equilibrium. The proof works for an explicitly fixed cash-independent tie-break, not an arbitrary history-dependent selection.

A further exact action quotient follows: if two own actions have identical accepted quantities and the same probability-weighted next noncash state for every rival action, but one has strictly lower outlay, it strictly dominates the other under this continuation convention. Retain minimum cost per (quantities, research target/probability, manufacture target/effect). This removes different operating recipes that only waste resources; there is no carryover of unused slots. Do not remove a less successful old procedure merely because its qualification probability is lower: competitive continuation payoffs need not be monotone in qualification. With binding liquidity or an archive/rights transition that differs between recipes, the proof cannot be applied unchanged.

For the implemented H=3,C=4 and maximum outside fee 10, parts maximum 2 and lab 1, Cbar=23 ticks. B=120 exceeds 4*23. The underlying resource, production, procurement and qualification restrictions are unchanged. The price slope 2 and intercepts (18,14) imply positive prices at all feasible profiles; a rival's extra unit lowers own receipts by 2 for each own unit in that market. The game is not an output-saturation theorem: quantities and competitor responses remain legal endogenous choices. Cash is replayed at the actual date even though it is omitted from the backward state key. Current net receipts are added once and terminal salvage once; there is no continuation premium.

## Exact matched four-date solution

Both firms start with no robot, no kit, model levels zero and procedure zero, and two inherited local archives. All retained research alternatives are present, including ordinary local training, contract work and a guaranteed successor license. Procedure caps 0,1,2 differ only in allowed successor menu; cheap parts (1,2) allow actual orders followed by assembly. Both continuation conventions produce the same initial and realized policy in these cases.

| cap | wealth F0 | wealth F1 | combined newly generated cash | expected salvage | customer surplus | enumerated profiles per selection |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 0 | 160.5 | 159 | 76.5 | 3 | 22.5 | 260754 |
| 1 | 160.5 | 159 | 76.5 | 3 | 22.5 | 1410958 |
| 2 | 160.5 | 159 | 76.5 | 3 | 22.5 | 2413130 |

On date one firm 0 trains digitally while serving a human digital job, firm 1 serves physical work; both order mobile kits. Firm 1 assembles on date two, firm 0 assembles with probability one half. On dates three and four both serve both markets. Actual dated cash, installed capacity and customer surplus are reconstructed in the forward ledger. Expected total accepted jobs are 12.5 (date totals 2, 2.5, 4, 4). All successor-attempt counts and inherited procedure levels remain zero. The horizon admits the earliest chain from zero (two successor acquisitions, then training, then service), but the available jobs and shared costs do not make that chain the selected equilibrium. This is a genuine matched null, not the previous inherited-psi1 test. It rules out a blanket inference from feasible successive improvement to profitable recursion. It does not rule out a bigger recipient set, longer horizon, lower qualification cost or different selection.

The direct finite-cash counterpart, B=16, cap 2, manufacturing allowed, was run with a declared 300,000 profile budget and stopped at profile 300,001 after 33,480 memoized solved subgames. This is a measured computational blocker under that budget, not proof of no pure equilibrium, and not proof that financing is irrelevant. No counterfactual finite-cash wealth is reported. [Diagnostic code](binding_embodied_diagnostic.js) and [result](binding_embodied_diagnostic_results.json) preserve the exact attempt.

## Reproduction and boundary

Run `node funded_embodied.js` and `node binding_embodied_diagnostic.js`. The first solver evaluates exact scaled integer payoffs and checks all retained deviations. Its independent forward ledger enumerates all sixteen paired draws, checks capacity/costs/kit conservation, and matches terminal cash and salvage. The dominated alternatives are covered by the action equivalence proof, not independently enumerated in this enlarged solve. The cap-0 higher-selection result also matches the unpruned-cost quotient in a separate execution. No new empirical or trained RL result is asserted.

The common link to the production branch's deployment-topology investment and reference-identification model is a costed, dated opportunity to qualify useful recipients. Topology value can be complementary across experiments but depends on usable remaining orders and validation slots; this known-local-archive restriction cannot recover that latent graph. The recursive branch's learned/ordinary tie and transfer reversal still bind interpretation: a procedure menu is a technology, not a special claim about learned policy quality. See [pilot preparation](PILOT_PREPARATION.md).

Next: enlarge the recipient state with a justified joint-type quotient, preserving the same embodied recipes and actual acquisition clock. Restore endogenous archive and scope only after their transitions are included in the equivalence key. A positive active-rival cap-2 comparison, general mixed equilibrium and binding-cash solution remain open.
