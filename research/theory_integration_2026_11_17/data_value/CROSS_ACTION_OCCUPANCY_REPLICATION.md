# Exact replication and scope

This folder contains cross_action_occupancy_exact.js (pure Node-compatible JavaScript, no dependencies) and cross_action_occupancy_results.json. Run from a copy of the private repository:

    node research/theory_integration_2026_11_17/data_value/cross_action_occupancy_exact.js

The model constructs a **single** rational joint law of (Q_G,D_G,F_G,W,A_P) at each t=k/64 for k=0,...,16. G triple retains all fair and pairwise-independent margins; W is inherited worker availability, F_G≤W and A_P≤W. It verifies both the actual cross-program discordance and the physically feasible trial-free P/G/E expected contribution, testing whether ε=3/8 holds iff k≥8.

The same checker exhaustively enumerates **969** four-cell distributions (A,W) in integer units of 1/16, each with 17 discrete ε choices, exhaustively enumerates the allowable two free B-allocation cells, and compares attained extrema with the proven formula, reporting 12,597 feasible bound configurations and 3,876 infeasible ones. It reports 29,345 exact assertions. These cases test sharpness on a discrete grid; the continuous bound comes from the written algebra and convex mixing, not test counts. BigInt is used for exact rational construction; neither floating rounding nor machine learning is involved.

A separate Python Fraction enumeration of all 17 constructed laws with a different probability construction was executed at preparation time (170 exact independent local assertions). It was **not** committed as an independently hash-verified checker and is not independent peer review. The GitHub-committed JS source was executed as the exact same function body in the connected tool environment before publication; rerunning retrieved bytes on a separate Node installation is a future replication step, not a claim already made.

Every output is conditional synthetic normalized production. The economic interpretation needs signed rights, real original-buyer paid/no-order records, physical worker transitions and a verified E resource ledger. No field data, official numeric BEA interindustry coefficient, whole-repo CI or scientific novelty review was performed.
