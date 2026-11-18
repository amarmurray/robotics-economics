# Robust identification continuation — proof and counterexample ledger

| Statement | Status | Critical domain restriction |
| --- | --- | --- |
| R1 robust pairwise certificate | Proved as a definition/equivalence and affine-mixture vertex fact | Only compares **uniformly pathwise-feasible** policies and a declared feasible class; vertex shortcut only for mixtures over full trajectory laws, not arbitrary uncertain kernels |
| R2 coupled acceptance difference | Exact synthetic sharp bound \(J_R-J_E\ge 1/5\) under matched \(q_E-q_R\le1/10\) | Matched cross-route bound is a **hypothetical identified constraint**, not inferred from individual marginals or observed field trials |
| Independent component benchmarks determine optimal route | Rejected; same component marginals admit both route rankings | Requires joint 00/10/01/11 held-out customer acceptance and appropriate causal matching |
| Separate payoff intervals must be disjoint to identify decision | Rejected; joint feasible set and paired *difference* suffice | Correlation of counterfactual outcomes requires transport and common window; cannot freely combine incompatible world endpoints |
| Diagnostic best against productive maximin | Proven within symmetric two-world, one safe terminal slot; threshold \(\underline\alpha\ge(4+c)/6\) | Does not dominate each deterministic productive policy, and is not a general POMDP result |
| .8 observed accuracy safely identifies near-perfect signal | Rejected; two-sided labels, sampling uncertainty, drift, support and recovery tails matter | Hypothetical Hoeffding calculation only; no data or certified structural zero |
| Pathwise feasibility preserved under diagnostic noise | Rejected if mismatch costs 2 after cost 1 and budget is 2.1 | A feasible fallback or resource reserve is a distinct authorized route |
| Maximin, minimax regret and pairwise dominance synonymous | Rejected | Need chosen decision criterion and comparable feasible policy set |
| Rectangular Bellman always solves fixed-regime robust policy | Rejected | Dynamic adversarial switching is not a fixed latent H or full-history ambiguity model |
| Novelty, calibrated learning value, approved hardware safety | Not established | Standard robust control, partial identification, Blackwell, Fréchet, source-to-production economics foundations and synthetic data |

Proofs and constructive cells are in ROBUST_POLICY_IDENTIFICATION.md. Numerical replication is separate from proof; source reading covers selected descriptions, not reproductions of established papers. The full historical queue and previous released state remain available.
