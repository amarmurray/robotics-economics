# Joint procurement budgets, qualified operator capacity and data-value decisions
**19 November 2026 | same When Capabilities Become Production argument | conditional theory, not observed robot economics**

## 1. The unresolved economic object
Prior chapters distinguish source-learning X, target grounding G, new qualified embodiment E, and genuinely retained incumbent R. They show that a robot may qualify a service without creating an additional *sale*, either because a shared operator slot binds or the same original buyer substitutes between services. This extension makes the **parent procurement budget and timing of price information** explicit. The engineering gain from G (two qualified recovery slots rather than one) can be worthless to customers who cannot buy two complete services at the offered prices. Conversely, a legally permissible lower-price menu can unlock two purchases without increasing technical benchmark performance.

Fix an original eligible buyer registry, its parent procurement groups, complete-service commitments, service acceptances and refusal/no-purchase, a safely qualified operator/robot/controller/rights configuration, and a finite precommitted price menu. In policy p and menu m, let j index an eligible customer-service recipe, A_j(theta;p,m) indicate an eligible request *and* technical/safety qualification, P_j be the actual collected sale price, r_j the captured contribution net of variable delivery/collection costs, a_j its vector of physical/organizational resources, and B_b a verifiable parent budget. Let z_j denote actual accepted fulfillment, not merely an offered or benchmark-passing task. Require each original procurement group to buy at most one substitutable service, parent payment sum at most B_b, and aggregate resource use at most H. The complete ex-post production value is the integer allocation maximum sum_j r_j z_j under these constraints, including the ability to refuse unsafe/unprofitable orders **only when legally permitted**. The policy's upfront adaptation/data/body costs K_p are subtracted ONCE, outside the operating maximum. If the old controller and contractual obligations cannot actually be retained, R is not a feasible fallback.

The model is *not* a claim that budgets cause all affordable orders to be purchased. A_j and buyer choice are potential outcomes specific to the entire menu, quality, competitors and policy. Nonparametric market closure needs all original groups and bounded receipts; revenue cannot be inferred from a fixed physical slot alone.

## 2. A price-and-resource economic upper certificate
For a precommitted admissible p,m and complete market state theta, let the integer optimization be

    v(theta) = max {sum_j r_j z_j :
       0<=z_j<=A_j(theta), sum_{j in group g} z_j<=1,
       sum_{j in parent b} P_j z_j<=B_b,
       sum_j a_{kj} z_j<=H_k, z_j integer }.

If lambda_k, eta_b, gamma_g, delta_j are all nonnegative and

    sum_k lambda_k a_{kj} + eta_{b(j)} P_j + gamma_{g(j)} + delta_j >= r_j

for every offer j, then

    v(theta) <= sum_k lambda_k H_k + sum_b eta_b B_b
                + sum_g gamma_g + sum_j delta_j A_j(theta).

The proof is a direct valid LP-relaxation dual bound; integrality may make it loose, so it is not generally sharp. If original eligible request+qualification frequencies have valid upper bounds pbar_j under THIS SAME p,m, take expectations and replace A_j by pbar_j. This holds without independence, with buyer substitution and correlated requests, provided known legal payment/resource ceilings are *really* enforceable. It only upper-bounds production, not its guaranteed floor. For menu optimization, enumerate supported menus and maximize their independently valid upper certificates; do not choose menus after observing unknown future demand if the contract is precommitted.

A finite, approved captured-receipts ceiling, and not merely a bounded robot task count, is required for a cash-value bound. If buyer budgets are not enforceable payment caps, do not insert them as if they were.

## 3. Exact same-original-market countermodel: budget 7 versus 8
Two original eligible divisions of one parent each request one fully qualified service **simultaneously** in a high-demand state H, occurring with probability q; neither requests in the low state. Each division's willingness to pay is 6 for either service under all permitted policy-specific menus {4,5,6}. The parent is contractually willing to buy the maximum count of requested services it can afford (a strong *synthetic* response rule, not a universal behavioral assumption). The parent's common budget B is either 7 or 8. X source-learning safely qualifies both requests but permits only ONE recovery/operator slot. G target-grounding permits TWO slots with upfront cost K_G=1/2. E adds a genuinely approved second embodied slot with cost K_E=2. X costs zero in this normalized example; R is an independent, actually reserved competent customer contribution of 2. All numbers are **normalized invented production contribution units**, not inferred robotics prices.

For each permitted uniform price P, receipts in H are P times min(2, safe slots, floor(B/P)); L gives zero. X optimally chooses price6 and earns J_X=6q. At B=7, G's best price is6, one order; J_G=6q−1/2. At B=8, G's best price is4, *two* orders; J_G=8q−1/2. At q=1/2, B7 ranks X3 over G5/2, while B8 ranks G7/2 over X3. E earns 1 in B7 and2 in B8, and R earns2. A new robot body does not repair a binding buyer budget, despite adding technical capacity. The **only counterworld difference is the parent procurement budget**; request probabilities, customer willingness to pay, controller qualification and slots are the same. At the previously posted price6, both counterworlds show precisely one sale for6 in H and zero in L. Accepted-only receipts, even with exact per-division demand, cannot identify the better investment.

## 4. Joint budget-and-demand identification, and the timing of learning
Let q=Pr(H), b=Pr(B=8) and t=Pr(H,B=8). If budget B is legally observable **before pricing**, the approved G menu may be contingent on B, with price6 for B7 and price4 for B8, selected before the unobserved demand realization:

    J_G^{observed B} = 6q + 2t − 1/2;
    J_X = 6q;       J_G−J_X = 2t−1/2.

If the parent budget is NOT observed at menu commitment, one posted price must serve both B types:

    J_G^{fixed menu} = max(6q, 4q+4t) − 1/2;
    J_G^{fixed menu}−J_X = max(0,4t−2q)−1/2.

Price5 is dominated by price6 within this countermodel. With observed separate marginals q,b but missing matched budget-request timing, the classical joint-event support is

    max(0,q+b−1) <= t <= min(q,b).

Under the *stated* four-cell complete-response type family these endpoints are attainable, yielding sharp comparative bounds 2 max(0,q+b−1)−1/2 and 2 min(q,b)−1/2 for contingent G−X. They are NOT a general theorem about robot firms with menu-dependent demand. At q=b=1/2, that interval is [−1/2,+1/2] despite perfectly identified marginal high requests and budget incidence.

For q=1/2 and t=3/10, knowing B before the offer gives X3, G31/10, E at most its noncontingent price-menu value 6/5, R2; fixed-menu G earns27/10. Thus G alone gains 2/5 from budget-targeted pricing, but the **whole optimized X/G/E/R portfolio gains only 1/10**: with fixed pricing X is already available at3. Do NOT add the 2/5 as a separate information premium or count future data twice. At fixed q=1/2, the comparison G−X crosses zero at t=1/4 if budget-contingent pricing is feasible, but at t=3/8 when one fixed menu must be chosen. This is the economic value of *timely and actionable target grounding/market information*, not an intrinsic price for human teleoperation or any other data modality.

More generally the actionable observation of a parent's joint budget, customer participation, policy-specific service quality and safe recovery resource is a complementary data bundle. Knowing budget marginal alone without joint H/B or without lawful conditional contracting may have no investment-decision value. Technical training data, target grounding, production-generated field histories and synthetic pretraining can all affect A_j, but must be evaluated by their **conditional effects on the complete optimized customer policy**, not benchmark success percentage.

## 5. Preserve the common full-history response set
A response type theta contains *all* potential policy/menu-specific original buyer choices, refusal/nonpurchase, parent payment limits, permissible repricing, joint qualification, shared operator recovery, controller/version changes, and future opportunities under one market history. A finite supported law polytope Pi={pi>=0,1'pi=1,l<=M pi<=u} yields for **precommitted** m_G,m_X a sharp conditional paired comparison inf_{pi in Pi} pi'(v_G(m_G,theta)−v_X(m_X,theta))−K_G+K_X via an LP when the finite type family itself is complete. Do not independently select adversarial X and G worlds that cannot coexist within the approved support. Conversely, if BOTH complete policy mean outcomes are separately identified in the SAME target population, linearity identifies their *mean difference* even without a cross-policy copula; cross-policy dependence still matters for adaptive treatment, joint constraints, dispersion, and heterogeneity. This corrects an overbroad interpretation of the need for paired potential outcomes. Identifying only service marginals or incumbent accepted-only sales does **not** identify the complete policy mean.

If an investment changes original buyer eligibility, competitors, target quality, budget definition, or controller/operator spillover exposure, even these sharp four-type bounds need to be rebuilt. Retain free optional policy/data availability and protect physically approved R. Acquiring data can be costly or training can be forced; an observed negative-transfer training recipe alone does not imply free optimally optional data has negative value. The business can build new embodiments and collect production byproducts, but their value belongs inside the same discounted production problem—not a separate dataset royalty.

## 6. Closest prior art, interpretation and remaining test
The dual certificate is ordinary LP weak duality and the t interval is classical Fréchet coupling. Choice-/assortment-based revenue management is well established (Talluri & van Ryzin, [2004](https://doi.org/10.1287/mnsc.1030.0147)); multi-purchase assortment-and-pricing methods explicitly appear in Luan, Wang, Xu & Xue ([online 2024, journal 2025](https://doi.org/10.1177/10591478241279560)). Farboodi, Koh & Xia's [Data-Driven Automation](https://arxiv.org/abs/2606.10127), sections 5 and Appendix B, already treats future productive data and complementarity. The contribution here is a conditional synthesis and identification target for **qualified robots**, not an independently verified new theorem.

**Next exact question:** which real original-buyer budget/quote and demand/report panels, joined to qualified full-service operator/controller histories, establish the *feasible* common response set and payment ceiling under X/G/E? Without that evidence, the valid result is an interval, not a preferred robotics investment. The adjacent [proofs](JOINT_BUDGET_MENU_PROOFS.md), [empirical design](JOINT_BUDGET_MENU_EMPIRICAL.md), [Model A/B bridge](NOV22_JOINT_BUDGET_MODELS_AB.md), executable and teaching materials preserve this gate. No field customer/robot intervention, physical authorization, official quantitative BLS–BEA task crosswalk, full repository CI or independent originality review was performed. **Nov22 synthesis gate OPEN; Dec25 2026 23:59 America/New_York unchanged.**
