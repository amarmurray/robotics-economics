# Student exercises — full-stack robotics data economics (three-date customer budget)

Do not use the [separate solutions](THREE_DATE_BUDGET_QUEUE_SOLUTIONS.md) until you have derived your answers.

1. **One buyer, two late offers.** Prove max(bD,cT)=bD+cT-min(b,c)DT for binary D,T. For b=2,c=3, Pr(D)=Pr(T)=1/2, characterize the entire sharp range of optimized one-slot paid service; give physical joint distributions at its extremes.

2. **Why source production is not a free dataset.** A t=1 eligible buyer pays 4/5, and serving produces a licensed learned C qualification. C orders with probability 1/2; an early operation causes a two-shift recovery job with probability 1/5, independently. A's one-unit budget is consumed by t=1 sale. Derive the source paid value and compare with retaining the A budget for a 1/2-probability later order worth 2. Name two ways the result changes if the learned C qualification is not actually useful to a paying buyer.

3. **Regime-dependent grounding and worker conservation.** Under G, target C qualification is available from licensed data, Pr(C order)=1/2, J~Bernoulli(1/2), A late D~Bernoulli(1/2), and x=Pr(D C). Derive G_skip and G_serve. Solve for the x where (i) G dispatch changes and (ii) G_skip beats a separately staffed E with contribution 21/10. Explain why these are different thresholds.

4. **Implementable commitment.** Two coherent, observationally P-identical worlds have x=0 and x=1/2. Compute a minimax-regret commitment lottery over P_serve, G_skip, G_serve, E_skip. Do **not** choose G_serve in the H world after observing an unreported regime. Compare with a maximin-production decision.

5. **Lawful signal and selection.** Under an equal prior and precommitment binary report of W with symmetric accuracy h>=1/2, derive the minimum accuracy that changes the investment, its gross value at h=3/4 and why a P-only report has zero value in this construction. Specify the original-buyer and reporting rows needed to identify x_G under a supported prospective design, and explain why a zero-propensity G action defeats reweighting.

6. **Generalization challenge.** Replace the one-unit A budget with two units or let a paid t=1 service change A's genuine late willingness to order. Give a concrete reason why the static overlap formula alone ceases to determine the full program choice. Distinguish optional free data from mandatory costly retraining.
