# Student exercises — episode support and qualified production (no solutions here)

**Exercise 1 — denominator and admission.** One source has an A episode with nine accepted-eligible processed transitions and B with one. Source-level proposal is uniformly over transitions. Derive p_A,p_B. Repeat after a target-grounding sampler gives the two episodes equal weight; identify what that transformation can and cannot create. Explain why the code's original JPEG frame count is not the right denominator after latency adjustment.

**Exercise 2 — exact coverage.** Draw K=3 episodes iid with replacement. Prove P(at least one A and B) in terms of p_A, then calculate it at p_A=9/10 and 1/2. Explain what assumption is required to interpret this as qualification rather than a data-count statistic.

**Exercise 3 — distinct recovery.** Suppose a new data collection creates eight new independent B episode families, giving one A family mass 1/2 and nine B families mass 1/18 each. Calculate P(exactly one A and two *different* B) and show why reweighting the single old B cannot meet the same event.

**Exercise 4 — option and comparative statics.** R fallback produces 2, a qualified new policy 12, G costs 2/5, X costs 7/5, and a certified E produces 19/5. Rank R,G,X,E under context-presence and novel-family qualification. Identify which costs are once-counted, why adding an existing free archive cannot lower the optimized value, and what changes under a forced retrain.

**Exercise 5 — robust design.** Given total B probability b, K=3 and at most m_B independent B families but no internal weights, derive sharp bounds for novel-family qualification. At b=1/2,m_B=9, does observing A/B mass alone robustly rank X against E above? Which one additional predeclared statistic is sufficient for the stipulated map?

**Exercise 6 — identification.** Explain why holding realized K fixed by selecting observed clusters from a randomized fixed-proposal assignment is not the same intervention as randomizing fixed-K stopping rules. Specify the randomization unit with shared weights and a complete buyer–robot–operator policy and list evidence needed to turn a technical score into captured original-customer value.
