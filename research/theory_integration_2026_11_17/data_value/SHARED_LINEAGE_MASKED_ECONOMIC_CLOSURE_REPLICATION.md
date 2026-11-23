# Replication (synthetic only)

Run from this directory:
```sh
node shared_lineage_masked_exact.js
```
Compare printed JSON with shared_lineage_masked_results.json. Integer original-denominator mass 128, released mass 32, mixtures p=j/8. The executable enumerates all nine deterministic report policies and randomized action distributions on a quarter grid, checks full pairwise laws, exact values, known-law optimum, robust midpoint upper bound and weighted symmetric-difference residual inequalities. The general proofs are in the chapter; enumeration is not a proof. Independent Python Fraction enumeration of all nine laws and all nine deterministic policies checked the formulas, full pair distributions, and known-law optimum. The JavaScript source is serialized from the function executed in V8; the CLI was not executed in Node this tranche. No full CI, real field calibration or independent novelty review.
