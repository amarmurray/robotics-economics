# Replicate the sequential S/M buyer-worker counterworld

Proof: SEQUENTIAL_ADAPTIVE_BUYER_WORKER_POLICY.md. Source: sequential_adaptive_policy_exact.js. Frozen result: sequential_adaptive_policy_results.json.

Run from the repo root using Node 18+:

    node research/theory_integration_2026_11_17/data_value/sequential_adaptive_policy_exact.js

This script enumerates four equally likely independent fair (U,V) worlds per action. It tests S-before-M original demand monotonicity atomwise, one exclusive t3 worker, no more than two payable C units, all full S histories common across regimes, both M demand and worker marginals, paid-service values and the t0 minimax-regret lottery. It returns JSON with **1,026** scoped assertions. The source body was executed in a V8 isolate before Git creation; an independent Python 3 Fraction calculation repeated the endpoint paid-service values and regret identity, but whole-repo CI and a post-commit Node CLI reexecution have not been performed. Run the committed script before treating a later revision as reproduced.

Expected exact economic values: R=19/10, P=21/10, E=11/5, G/S=2, G/M-low=1/2, G/M-high=5/2; S original C demand weakly dominates M at the same latent U,V; the S t4 coincidence is 1/4, while M's t4 coincidence ranges from 0 to 1/2 with the same individual M marginals of 1/2. The minmax-regret independent-cluster G/M share is 3/20; worst regret 51/200.

The enumeration is an arithmetic check **not a proof**. Algebraic g-formula identification and the support/counterworld argument are in the chapter. The M marginal bounds are hypothetical extra information and **not** identified from old S records. There are no robot physics, live model training, customer payment observations or independently validated novel theorems. November 22 scientific acceptance is OPEN, and December 25, 2026 23:59 Eastern remains the final target.
