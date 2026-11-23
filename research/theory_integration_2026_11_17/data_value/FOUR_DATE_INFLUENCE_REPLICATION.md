# Exact replication: t4 continuation and blocked worker risk-set

File: dynamic_riskset_exact.js; frozen result: dynamic_riskset_results.json; proof: FOUR_DATE_ECONOMIC_INFLUENCE_CLOSURE.md. Both worlds use 16 equally likely atoms (H,U,V,Z) and one nonanticipative structural map for G, while R/P/E values and histories remain common. One unit of G early accepted output and at most one subsequent C unit are paid across the lifetime budget. t3 W=0 cannot produce; a newly cleared worker can serve t4 only after the owed repair clears.

Run from repository root:

    node research/theory_integration_2026_11_17/data_value/dynamic_riskset_exact.js

Expected: a JSON object with 239 assertions, R=2, P=21/10, E=43/20, G low=9/5, G high=51/20, risk mass 1/4, conditional D and L each 1/2, joint probability 0 or 1/2, t4 moment 0 or 1/8, switch 7/120, minimax G share 8/15 and regret 14/75. Node 22.16.0 executed 239 assertions on the exact Git-blob-matching source during this tranche. Independently executed Python 3.13 fractions.Fraction enumeration confirmed the two endpoint values, their identical (H,A,C,W) distributions, 8/15 regret solution, and threshold 7/120. That Python check is a supplementary local calculation; no claim of independently reviewed code or GitHub CI.

The enumeration is *not the proof*. The proof uses inclusion-exclusion for t3, the conditional Frechet inequalities for E[DL | H=1,W=0], the common-law construction L=Z or L=1-Z, and exact regret equalization. All program costs and payment units are stipulated. The model is a stylized finite causal decision world, not an industrial teleoperation, robotics physics or language-model execution.

This work intentionally changes the future *information structure* rather than merely rerunning an existing parameter grid: a previously t3-worker-blocked state receives a t4 clearance and original C customer opportunity. The prior H=W=1-only audit is now insufficient even when G's complete t3 history and conditional D/L marginals are known. If future rules allow t3 service to change t4 offers, or allow G-conditioned recovery decisions, recompute the longitudinal policy and identification row space; the scalar t4 joint moment need not remain sufficient.

Scope limits: no signed G rights, lawful randomized assignment, buyer payments, verified E staffing, official numerical BEA I/O flows or independent novelty review. The November 22 scientific gate remains open. Deadline December 25, 2026 23:59 America/New_York.
