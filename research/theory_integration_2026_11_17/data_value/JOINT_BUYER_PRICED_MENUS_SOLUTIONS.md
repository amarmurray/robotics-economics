# Instructor solutions — buyer choice, data transfer and production

**Separate from [student exercises](JOINT_BUYER_PRICED_MENUS_EXERCISES.md).**

1. A-only7 and B-only7 are separate *counterfactual assortments*. With both offered, at most one sale yields7, not14. The original procurement/decision group, complete offered menu, chosen and rejected alternatives, no-purchase field, total buyer budget and full accepted service resolve the accounting.

2. X at price8 is certainly accepted since w_A≥8; J_X=8−1−2=5. A price7 produces4, price9 is unavailable, so robust optimum is5. G at5 is certainly accepted for J_G=5−0−1=4; price6 can be refused, giving −1 in the worst state. R3, so X wins under the stated support and qualified capacity. Correlation plays no role in this one-purchase guarantee. But if X changes customer quality enough to violate [8,9), the conclusion disappears.

3. The buyer-aware LP has x_A+x_B≤1 and x_A+x_B≤2, so max 7. Dual upper expression at λ=0 is max{7,7,0}=7. With two distinct buyers and one physical slot, λ=7 gives 7+2max(0,7−7)=7, matching a feasible single sale. Summing two product maxima double counts the first buyer; omitting λ capacity double counts in the second setting.

4. At price7: X receives 7−3−2=2, G receives no sale and loses1, E sells A for 7−3−3=1. At optimal prices: X chooses8 and nets3, G chooses6 and nets5, E can offer B alone at6 and nets3. Choice quality w is a buyer ceiling, not captured provider payment; the provider receives posted price less actual delivery and investment costs. If pricing occurs after a previously unseen market regime, an oracle maximum is not ex-ante implementable.

5. With normalized utilities zero for A, B and outside, solo probability1/2, joint probability1/3 for each product and outside1/3. Joint receipt expectation at price7 is 14/3, not the sum of separately offered expected receipts7. Unbounded Gumbel shocks allow rare preference reversals no matter how favorable a deterministic finite margin; require actual choice/no-purchase outcomes and a validated model or conservative probability bounds, plus resource and captured-payment envelopes.

6. Add a new X-only qualified buyer to an otherwise identical retained market with captured payment M unbounded; every R observation matches, while X gross value grows without a finite ceiling. If free data only enlarges an optional information/action set, the old optimal policy remains feasible so V cannot fall. A mandatory update can remove the old policy, compete for operator minutes or change buyer confidence; that is a different feasible set, so nonnegative optionality no longer follows.
