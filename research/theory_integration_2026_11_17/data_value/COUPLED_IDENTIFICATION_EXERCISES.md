# Exercises — coupled transfer, customer response and the value of joint evidence

**Student copy; November 18, 2026.** All quantities invented and normalized. No solutions in this file; see [COUPLED_IDENTIFICATION_SOLUTIONS.md](COUPLED_IDENTIFICATION_SOLUTIONS.md).

### 1. Reconstruct the identified joint law

Two binary pre-action variables have Pr(H)=Pr(D)=1/2. Set t=Pr(H,D). Derive all four joint probabilities and the sharp interval of t without assuming independence. If R and G have total captured-service type payoffs [13,5,5,5] and [7,7,9,7], compute R-G's sharp lower and upper values. Give an explicit primal law attaining each and a valid linear dual lower certificate.

### 2. Choose the economic criterion

E and S return 6 and 5 across all four types, and the independent production program can allocate x of its fleet to R and 1-x to G with linear additivity. Prove the maximin x and its guarantee. Then calculate the **minimax-regret** x relative to the clairvoyantly best pure route at the same t. Are the two x values equal? When might neither fraction be feasible?

### 3. Does learning the entire population parameter necessarily pay?

A costless, safe oracle reveals t before an investment, but not each subsequent customer's latent H. Compare guaranteed maximin contribution before and after the oracle if (a) a **single indivisible** route must be selected and (b) fractional R/G fleet allocation is feasible. State why a zero incremental worst-case value in (b) does not imply zero Bayesian or individual-state information value.

### 4. Derive the report bridge rather than assuming a true label

Baseline Pr(D)=.5. A safe diagnostic Z has sensitivity 0.9 and false positive rate 0.1 to a persistent aligned H, with both rates invariant across D. An observed co-occurrence interval Pr(Z=1,D=1) in [.34,.40] is reported. Compute the corresponding t bounds and the sharp R-G value range. What fails if sensitivity varies by D or the only H label is an unsafe target attempt?

### 5. Budget support and data value

A diagnostic path uses operator 1 with probability .9999 and operator 3 with probability .0001, compared with an approved hard remaining capacity of 2. Does its low expected resource use qualify the diagnostic? Propose a compliant fallback. Explain how the customer acceptance, training/data rights, free no-train arm, and demand registry would enter a valid commercial valuation without double counting future data.