# Learning exercises — endogenous demand and persistent transfer

**Student copy. Conditional synthetic theory, 18 November 2026.** Solutions live only in [ENDOGENOUS_DEMAND_SOLUTIONS.md](ENDOGENOUS_DEMAND_SOLUTIONS.md), not below. No field quantities are assumed.

### Exercise 1 — pairwise dominance versus maximin

The possible persistent regimes are H/L with one unknown prior \(p=P(H)\in[2/5,3/5]\). Four safe policies have complete-history captured contribution vectors R=(14,3), G=(7,10), E=(7.5,7.5), S=(6,6). Assume all four total values include the associated acquisition costs and current accepted service once.

(a) Find each fixed route's worst-prior contribution. (b) Is the route with highest minimum **uniformly better** than R under every possible p? (c) Compare G to E under every p. State why (b) differs from (a).

### Exercise 2 — a nontrivial opportunity from mixing

Suppose a first deployment can be randomized/fractionally allocated across independent, identically eligible opportunities, and expected route contributions add without controller interference. Find a weight x of R and (1−x) of G that makes the two regimes yield exactly the same contribution. Prove your mixture is the optimal maximin among all mixtures of R,G,E,S **without** numerical optimization. Explain one physical/economic setting where the conclusion fails.

### Exercise 3 — why the uncertainty set matters

One latent \(\theta\in\{H,L\}\) persists across a fair future customer order Y independent of it, with \(p\in[1/4,3/4]\). A qualified policy earns one unit only if Y=H and θ=H, or Y=L and θ=L. Calculate the worst value when p is selected once before both branches. Then calculate what a hypothetical adversary obtains by choosing p separately after Y=H and Y=L. Which formulation respects the stipulated independent order and why?

### Exercise 4 — customer economics, not success-rate conversion

For a **single divisible complete-service capacity**, let \(G(a,c,K)=\max_{0\le q\le K}[(a-c)q-bq^2/2]\). Take \(a-c=10\), \(b=2\), capacities \(K_0=2\) and \(K_1=4\), capture fraction \(\rho=1/2\). (a) Compute the optimal production quantities and values. (b) Compute additional captured contribution with \(\Pi_0=0\). (c) Repeat with outside-option surplus \(\Pi_0=18\), using \(\rho\max\{0,G-\Pi_0\}\). Why can neither result be obtained from a robot benchmark success percentage?

### Exercise 5 — data cannot identify what it never observes

A hundred or a million routine R deployments reveal only the exact R histories and no grounding G is ever assigned to the L regime. World W+ has G/L full-service value 10 after acquisition cost; world W− has G/L value 4 after the same cost. In both, G/H value is 7, and E is 7.5 under both regimes. (a) Show the worlds can have identical distributions of all observed R data. (b) Compute G's worst-prior value in each and compare with E. (c) Specify one ethically feasible experimental or identifying assumption that would break this equivalence. Why would weighting only the R observations fail?

### Exercise 6 — audit a claimed robot deployment value

A researcher claims that adding ten thousand free synthetic trajectories creates a 10%-point benchmark improvement, hence \$X of new provider revenue. Identify the essential intervening measurements and at least two competent alternative policies needed to make an economically meaningful causal valuation, while preserving distinct technical transfer and customer demand effects. Discuss when a free *optional* dataset could rationally be discarded after testing.
