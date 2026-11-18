# Robust policy identification — independent study questions
**Private teaching packet, 18 November 2026. Use ROBUST_POLICY_IDENTIFICATION.md; solutions are intentionally separate.**

1. **Decision versus intervals.** A customer pays optimized incremental contribution 8 for a complete B-and-C accepted service. R preserves 1 unit of qualified current production, E does not. The individual component pass rates are (0.75,0.75) under R and (0.9,0.9) under E. Derive sharp ranges for the joint event and expected accepted-production value. Can you rank R and E? Construct opposite rankings.

2. **Paired identification.** Suppose a defensible matched protocol adds the inequality \(q_E-q_R\le0.1\). Prove that R beats E in *every* compatible joint-law world, and test against a specialist worth 6. Why is comparing separate value intervals insufficient? Give a valid 2-by-2 acceptance table at a sharp endpoint.

3. **Diagnostic threshold.** There are fixed regimes X,Y. A matched terminal recipe yields customer contribution 8, a mismatched one 2, specialist 4; terminal safety consumption 1. Routine P produces 1 now and supplies no information. D produces zero now, costs one unit of operator capacity and additional \(c=0.1\) in real curation, and reports regime with conditional accuracy \(\alpha_H\ge \underline\alpha\ge1/2\) separately in each regime. Total operator budget 2.1. Compute P's maximin value (randomization allowed), D's report-following lower value, and the minimum \(\underline\alpha\) making D better. Does this guarantee D beats every deterministic P policy?

4. **Safety rejection.** Same model, but the final wrong-regime action now consumes 2 operator units and the matched action 1. Reports are 99% accurate. Can D follow its report with the target route under a strict 2.1 pathwise cap? Explain why expected resource demand is irrelevant, then propose a *different* feasible fallback or reserve condition.

5. **A diagnostic about diagnostics.** Assume n independently labelled Bernoulli reports per regime and 80% correct in each. Derive a 95% simultaneous Hoeffding lower bound for \(n=400\), and compare it with Question 3's threshold. Explain why this calculation cannot certify true hidden transfer regimes, absent observations, tail recoveries or stationarity.

6. **Ambiguity semantics and value.** A probe perfectly reveals a persistent H, terminal matched service is 8 and mismatched is 2. Compare an adversary selecting one fixed H for the entire two-stage history with an adversary freely switching H after the probe. State a practical robotics mechanism that could make the first model invalid. Explain why optional free additional information need not be assigned a standalone dollar premium.
