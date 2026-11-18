# Student exercises — safe pool factorial identification

Use only the conditional synthetic setup in [SAFE_POOL_FACTORIAL_THEORY.md](SAFE_POOL_FACTORIAL_THEORY.md). Do not infer that a physical robot is authorized to run a policy.

1. **Full-policy identification.** Prove the finite-population Horvitz–Thompson mean is unbiased under known, positive independent pool-level vector assignment. State why a complete customer registry and cluster rather than robot assignment is essential.
2. **Third-order complementarity.** Given three-slot means f0=7, f1=7.5, f2=7.4 under symmetry, compute the pairwise extrapolated f3, the interval for the third-order term if f3∈[6,9], and the threshold at which f3 exceeds the best observed fixed-one-R assignment.
3. **Safety and randomization.** Expand the Bernoulli three-slot mean as a polynomial in x and unknown z=f3. Find the maximin Bernoulli x and guarantee if z∈[6,9]. Explain what goes wrong if RRR is not certified.
4. **Partial transport.** A/B pre-action shares are 0.7/0.3. The mixed-one-R assignment is known to yield 7.5 in A but only bounded by [5,9] in B. Both baseline G policies yield 7. Find sharp global-mixed economic bounds, the selective A-mixed/B-G value, and the maximum extra segmentation cost for a strict improvement on global G.
5. **Scientific identification objection.** Give two distinct explanations for a positive third-order *economic* coefficient that do not imply useful third-order source-data learning. Propose a held-out intervention and observable that could distinguish technical learning from demand response. State why passing a mean operator-use budget cannot authorize the experiment.
