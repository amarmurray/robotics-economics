# Embodied investment, retention rights and strategic randomization

November 26, 2026. Input main `e0208e9fa7cf8a180f5e8e58358276740662126a`, production `8dba84f45e18fe5896e75cd9a98539e4b87a83fb`, recursive `af1cabb95772524db1b34dda3b2667a54c203b43`. Extends [COHORT_RIGHTS](COHORT_RIGHTS.md) and [COHORT_SCALE](COHORT_SCALE.md).

## 1. Economic premise and exact restriction

Retaining a manipulation record may allow an older arm to free the human/compute resources that a newer mobile embodiment would otherwise release. Purchasing parts, converting them into installed capacity, and processing evidence are alternative uses of the firm's dated resources. These investments need not be strict complements. A rival's ability to pursue the same options changes expected future output, prices and thus the private value of an archive.

Use the parent rights/scope game unchanged except that procurement and assembly are always available when the remaining clock permits them. Initial hardware is varied, not assigned endogenously in the first period: installed mobile; installed arm plus prepaid mobile kit; prepaid mobile kit only; or no installed machine or inventory. All cases have 3 dates, cash 120 each (fully funded), inherited open lab and procedure 2, digital recipient D1 qualified, no archive, outside qualification fee 18, purchased archive fee 10. Retention rights R=0 or R=1 (physical only) are assigned to both firms. The parent price law, legal service recipes and labor, inference, quadratic coordination, dated maintenance, training success and salvage remain identical. The firm's procedures are inherited, not acquired from zero. No free use of purchased inventory or current evidence: order, assembly, qualification and service are dated. Prepaid kit costs are sunk before this experiment, and terminal salvage of uninstalled kits is zero.

For a fixed rival strategy, let J(a,R) be the expected net receipts plus salvage of a lawful contingent policy a. Optional rights imply max_a J(a,1) >= max_a J(a,0) since old policies remain feasible. They do not imply this comparison when the rival changes strategy. For a fixed continuation selection, define A as an otherwise feasible current action with assembly, and D as retention with continued lab. The relevant difference is current net cash plus the difference in expected next-state value, not a capital or data premium:

    W(D,b)-W(A,b)=c(A)-c(D)+r(D,b)-r(A,b)
                 +E[V(s'_D,z'_b)-V(s'_A,z'_b)].

Even when the same accepted jobs are served now, this difference depends on the rival's current and future service/qualification choices. The cross effect is not sign-restricted: D may release the same complement as A, or a new embodiment may expand useful transfer and make D more valuable. The parent direct local archive technology does not yet model directed cross-embodiment evidence.

## 2. A mixed root is necessary in one specified continuation game

For the arm plus mobile kit and rights case, select the highest-total pure equilibrium at every continuation subgame, with the parent firm-0 tie break. All continuations are solved pure; the initial reduced normal form contains 170 actions per player. Complete enumeration finds no pure equilibrium at the root. This is conditional on these continuation choices, not a claim that no pure subgame-perfect equilibrium exists with other selections.

Two supported actions have the same service quantities (physical human service and qualified D1 digital service), no same-date training or manufacturing. N: no retention, close lab, current cost 9; D: retain physical case, continue lab, cost 10. Their exact continuation payoffs, excluding initial cash but including terminal installed salvage, are:

| F0/F1 | N | D |
|---|---|---|
| N | (52,48) | (50,51) |
| D | (51,50) | (51,48) |

F0 prefers N against N and D against D; F1 prefers D against N and N against D. Thus the incentives cycle within this support. Writing p=P(F0=N), q=P(F1=N), indifference gives 50+2q=51 and 50-2p=48+3p, hence q=1/2 and p=2/5. These are not fitted probabilities. The certificate checks all 170 legal retained action classes for each player with exact integer-scaled inequalities. This is essential: the 2×2 submatrix alone cannot prove equilibrium of the full game. Candidate support was located by fictitious play; its exact inequalities, not convergence of that heuristic, establish the result. Root mixing is independent; realized actions become public before the next date. All selected continuations are exact pure Nash equilibria in the stated reduced public-state games. The combination therefore specifies a finite subgame-perfect Markov continuation for this case, not a general mixed or private-information solver. The earlier conditional cash and terminal projection reductions are used; no equilibrium-selection claim outside their scope.

## 3. Matched results

| Initial stock | Selection | No rights wealth | Rights wealth | No rights jobs → rights jobs | No rights CS → rights CS |
|---|---|---|---|---|---|
| Installed mobile | higher / lower | (175,172) | (176,172) | 12→13 | 18→21 |
| Arm + mobile kit | higher continuations | (174,169) | (171,169.2), mixed root | 12→12.8 | 18→22.4 |
| Arm + mobile kit | lower | (171,170) | (171,170) | 12→13 | 18→23 |
| Mobile kit only | higher | (173,168) | (173,168) | 12→12 | 18→18 |
| Mobile kit only | lower | (170,169) | (170,169) | 12→12 | 18→18 |
| Empty hardware | higher | (173,167) | (173,167) | 12→12 | 18→18 |
| Empty hardware | lower | (167,167) | (167,167) | 12→12 | 24→24 |

These are synthetic quantities, not empirical estimates. In the arm-plus-kit economy without rights, one firm assembles its mobile kit on date 1. With rights and the higher continuation selection, no assembly is selected; retention is expected 1.1 times at date 1, internal qualification 0.8 times at date 2, and accepted jobs rise to 4.8 at date 3. The lower selection also displaces assembly with one retained-case pathway. Thus hardware manufacturing and learning can be equilibrium substitutes, even though both expand future feasible production. Customer surplus rises while combined private wealth falls under the higher continuation convention (343→340.2); the latter comparison uses mixed vs pure root selection and is not a universal equilibrium welfare ranking. The lower convention instead gives no private wealth difference. No kit orders are selected in these cases, although ordering is feasible at the root. With a mobile kit only, one assembly is selected with or without rights and no retention occurs. Inherited mobile reproduces the original positive rights effect with hardware choice restored. Do not infer that the value of hardware is the wealth difference across inherited-stock cases: historical equipment/kit acquisition costs are not in this account.

## 4. Verification and next dependency

Run `node manufacturing_rights.js` to regenerate the [full results](manufacturing_rights_results.json). All 16 cases solve; 15 pure roots, one mixed root. For the mixed case the exact support certificate records payoff matrix, probabilities, deviations and integer wealth numerators (7004160,6930432) over 40960. The forward replay branches over all four mixed root profiles with weights 2,2,3,3, and over the 16 qualification draw pairs per date, reconstructing actual uncapped cash, labor, compute, scope, archive provenance, assembly and kit conservation. Terminal wealth is checked against the exact backward-induction numerators; the decimal dated expectations are display values. This is not an independent implementation of equilibrium selection. Previous projection-off checks remain source evidence, not a new general validation of mixed projections.

Seven-obligation status: (1) the local rights and embodied restrictions now share an actual menu; source topology and network MPK models still require nonlocal transition primitives; (2) concurrent manufacturing, service, retention, learning, scope and cash jointly solved for this three-date prefunded restriction; (3) an exact mixed benchmark now exists in one case, not learned policy evidence; (4) retained procedures and qualified models remain stocks, per-copy token/compute and human flows paid separately; (5) inherited p=2 only, from-zero successor premium remains open; (6) rival response, equilibrium selection and mixing change private returns, no general mixed/private-information solution; (7) exact certificate and cash reconstruction, synthetic witness only. Falsifiers/alternatives: a cheaper outside route, profitable early kit order, different equilibrium selection, binding cash or shorter rights window, complementarity through cross-embodiment transfer, and capable fixed contingent policies. The production branch's topology model explicitly requires noisy relation/reference experiments; the recursive branch's economic RL separates accepted-output MPK and captured dynamic value. Neither is re-established by this local binary game.

Next: Enlarge useful recipient opportunities in the jointly embodied evidence/scope economy and solve matched from-zero cap-0/1/2 with active rival output and paid outside/ordinary-policy alternatives, using streamed profile budgets and a general exact mixed-support or certified numerical equilibrium method when pure continuations fail. Keep the binding-cash extension distinct from prefunded results; restore nonlocal directed archives and common latent public report likelihood (or split types when exchangeability fails). The five-date timeout and positive active-rival second-generation acquisition remain open, not economic nulls. Complete November 27 pilot synthesis at its checkpoint; preserve November 29, December 2, December 6 and December 25 gates.
