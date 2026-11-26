# Concurrent manufacturing and the operating-cost return to recursive inquiry

November 26, 2026. Input main `4d64f30acf5a4d7c0fca17735e5d26c01df457ee`; production `8dba84f45e18fe5896e75cd9a98539e4b87a83fb`; recursive `af1cabb95772524db1b34dda3b2667a54c203b43`. Read-only antecedents: production's DEPLOYMENT_TOPOLOGY_AND_REFERENCE_IDENTIFICATION.md (topological experimental investments) and recursive economic_rl/README.md and network_mpk/README.md (accepted-service MPK, captured receipts and continuation value). This is a joint four-block restriction of STAGGERED_WINDOW, not a new independent theory or actual LLM evaluation.

## Economic mechanism and a fixed-program derivation

Hardware investment can substitute for an improved execution model at the level of accepted output: both may release complementary operating resources. Yet once installed capacity saturates feasible sales, an execution improvement can still reduce labor and inference outlays. A shared investment bottleneck can make manufacturing and research substitutes even when their subsequent operating services coexist productively. Remove only the artificial exclusive-investment slot; retain the shared first-shift H=3 human slots and C=5 compute units, dated paid kit inventory, one research action, one construction action, evidence rights, ordinary contingent qualification and paid alternatives. All investments and receipts follow the accepted block timing. Both firms have an installed arm initially; mobile kit price is 4, orders and assembly are separate, and actual deployment starts only after assembly. Digital recipient admission is date 3. No new state is invented between the inherited block boundaries.

Compare the selected exclusive and concurrent programs, conditioning on identical later market quantities and prices. Let p be first successor success, q_1 the qualification probability if successor developed and q_0 otherwise, d the net resource bill saved per qualified operating shift, and S the number of later qualified-use opportunities. When the firm retains the old policy, success or failure does not prevent service. The expected qualification rate is P=p q_1+(1-p)q_0. If the two earlier dated private cash-flow differences sum to -F and terminal equipment salvage is the same, the private difference per firm is

    Delta W(S) = -F + d P S.

This is a decomposition of two fixed contingent programs, not an equilibrium comparative-static theorem. If prices, dispatch, research attempts, or equipment choices change, recompute the game. In the computed case p=q_1=3/4, q_0=1/2, so P=11/16; d=3 cash ticks (one human slot at 2 and one compute unit at 1); S=61; F=17. Thus Delta W= -17+(33/16)*61=108.8125. The conditional break-even S is 272/33, i.e. at least nine integer shifts, not a threshold of globally reoptimized equilibrium. Production gains on a fixed accepted-output frontier are zero during the saturated later blocks, despite a positive operating return and positive dynamic private value. This sharpens the recursive source's distinction among physical MPK, current operating return and dynamic investment value; no internal transfer or future-output bonus is counted.

## Exact competitive solution

Both firms start with procedure zero. Identical initial funding B=10000 each; all regimes satisfy the inherited sufficient-funding bound. Calendar (1,1,30,31), physical market open from date 1, digital market open from date 3, same inverse demand P_m(Q)=A_m-2Q. Both cap-1 and cap-2 regimes select the following outcomes under the higher-total pure continuation selection. Generated private wealth is terminal cash plus equipment salvage minus initial cash, not social welfare. Scope/rights and paid research options are retained.

| Regime | Combined generated private wealth | Accepted jobs | Customer surplus | Orders / assemblies | First successor / training attempts |
| --- | ---: | ---: | ---: | --- | --- |
| Costly kit, exclusive (accepted replay) | 1732.14111328125 | 222.46875 | 419.40625 | 0 / 0 | 2 / 2.25 |
| Cheap kit, exclusive | 1850 | 248 | 496 | 2 / 2 | 0 / 0 |
| Cheap kit, concurrent | 2067.625 | 246 | 492 | 2 / 2 | 2 / 2 |

Both caps have identical selected wealth and dated statistics within each row. Under exclusivity, both firms order at date 1, close the lab, assemble date 2, and serve both markets in dates 3–4. Concurrently, each orders, retains physical evidence and develops the first procedure in date 1; in date 2 each assembles and attempts physical qualification using inherited evidence, foregoing current physical service; they close labs after training. Expected number of firms with qualified physical execution at date 3 is 1.375. Later both firms always sell both services, but qualification saves 3 per shift. The expected dated net cash per firm is:

| Date | Exclusive | Concurrent | Difference |
| --- | ---: | ---: | ---: |
| 1 | 3 | -2 | -5 |
| 2 | 4 | -8 | -12 |
| 3 (30 shifts) | 450 | 511.875 | 61.875 |
| 4 (31 shifts) | 465 | 528.9375 | 63.9375 |

Equal salvage of 3 per firm; both firms gain 108.8125 privately. Relative to exclusivity this is +11.7635% combined private wealth, while accepted jobs and customer surplus each fall approximately 0.8065%. The reduction is from date-2 forgone service, not lower later sales. The same hardware becomes a complementary asset for qualified execution after installation, even though costly hardware and learning previously competed for a single slot. This is a conditional economic result for the specified rival responses, not a general welfare claim. Resource/task displacement at date 2 is explicit. Alternative pure selection, binding cash and within-block policy adaptation remain open.

## Exact solution accelerator and proof boundary

For public state x_i, own dispatch q_i and own dated action a_i, let T_i(a_i) be the distribution of the projected noncash continuation state. The inherited cash clipping bound ensures that current feasible outlays cannot make next-period liquidity bind, even if the rival supplies zero revenue. Conditional on the public state, private transition draws are independent. Hence

    U_i(a_i,a_j) = R_i(q_i,q_j) - C_i(a_i) + E[W_i(T_i(a_i),T_j(a_j))].

Two own actions with equal q_i and identical projected transition law have the same receipts and continuation payoff against every rival action. A strictly more costly such action is strictly dominated; at equal cost retain the earliest equivalent action. Every retained action representative is feasible in the unprojected menu. The result requires cash-independent continuation selection and the same joint transition law, not merely equal marginal distributions in a correlated latent economy. Cash projection is unsafe when the remaining liquidity bound fails; the solver explicitly checks it. The local archive mask may erase bits already qualified because there is no model forgetting, cross-recipient training or archive salvage and neither training, purchase nor retention consults an already-qualified bit for any other purpose. Directed transfer, model obsolescence and archive resale would invalidate that reduction.

Implementation: group own actions by exact rational (quarter-mass) projected successor law, retain the cheapest per dispatch-law pair, and cache integer-scaled expected continuation payoff pairs. First profile pass records both best-response vectors; second pass finds mutual maxima with inherited equilibrium tie-break. No full action-profile payoff matrix is stored (the continuation-class cache may still be quadratic in classes); each of the original retained own menus is explicitly checked against the selected opponent. All terminal outcomes are independently forward-reconstructed by the inherited dated cash and resource checker. This is an exact game reduction, not novelty over dynamic programming or stochastic-game state/action equivalence. Equilibrium selection is over pure equilibria only; absence would be recorded open, not nonexistence of Nash equilibrium.

| Case | Cap | Retained profile evaluations (first pass) | Unique transition-class pairs evaluated | Original retained-menu deviation checks | Memo states |
| --- | ---: | ---: | ---: | ---: | ---: |
| Costly kit replay | 1 | 909789 | 224025 | 97522 | 3450 |
| Costly kit replay | 2 | 1108797 | 267769 | 114578 | 3898 |
| Cheap kit exclusive | 1 | 909789 | 224025 | 97522 | 3450 |
| Cheap kit exclusive | 2 | 1108797 | 267769 | 114578 | 3898 |
| Cheap kit concurrent | 1 | 4782773 | 1360036 | 367736 | 10577 |
| Cheap kit concurrent | 2 | 6431973 | 1768420 | 479768 | 13025 |

The costly-kit accepted replay matches both exact wealth numerators/denominators and every dated result field from the earlier late_entry case. The cheap concurrent cap-2 result replaces the previous budget-limited diagnostic; its 6.43m retained profiles exceed the old 3.5m budget, so the numerical comparison is not a pure speed benchmark at identical budgets. The accelerator reduces repeated continuation-law evaluation; it does not eliminate the need to enumerate legal profile payoffs. Run `node concurrent_window.js [variant]` from this directory. Source SHA-256 guards the two accepted antecedent solvers. The published results record exact denominators, dated statistics and deviation checks. This reuses the accepted technology and independent forward accountant; no second independent equilibrium solver is claimed.

## Seven-obligation audit and next dependency

1. Source crosswalk: the network MPK distinction is recovered at fixed later quantities; source-directed relations and endogenous design remain distinct.
2. Closed restricted economy: actual concurrent construction, research, retained evidence, production and shared dated resources; cash is sufficient rather than scarce, and blocks prohibit intra-block decisions.
3. Exact selected competitive benchmark for economic delegation; physical output, cost savings and dynamic receipts distinct. No learned-policy performance claim.
4. Human and compute flows, copy requirements, coordination and qualified retained execution share resource constraints; no actual pretrained-LLM workload.
5. First successor investment and execution qualification coexist with manufacturing; cap-2 remains a reoptimized null here, not a universal theorem.
6. Fixed-program identity and exact globally selected policy comparisons; cheap kits/slot concurrency change quantities, prices and timing. General mixed equilibria and binding finance remain open.
7. Exact synthetic results with explicit falsifiers: equal-cost external execution, alternative selection, different skill pools, intra-block adaptation, directed transfer and finance. Need actual matched service, validation, retention, staffing and payment data to identify magnitudes; no empirical calibration or novelty claim.

Next: Move from block-constant dispatch to within-block contingent service and learning, with cash funded before each actual shift, retained evidence and dated scope/qualification; first derive a safe event-clock reduction and compare against the just-solved exclusive/concurrent cheap-kit cases. Test alternative continuation selection and whether the additional within-block flexibility changes the cap-2 null. Then binding cash, directed archives and common latent reports. Preserve November 27 recursive-pilot, November 29 program, December 2 week, December 6 contribution, December 25 final gates; no gate automatically passed.
