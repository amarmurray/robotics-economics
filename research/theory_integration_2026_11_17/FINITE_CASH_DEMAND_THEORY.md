# When Capabilities Become Production — customer demand, matured cash and capability access
*Integrated theory result 11; November 17, 2026. Private working manuscript extension, not a separate paper.*

## The analytical question

Result 10 established that higher demand for already-qualified A service can reduce the incentive to learn a new B service on productive A hardware, holding B's incremental contribution fixed. That theorem assumed qualification could be funded. But A demand changes the amount and timing of **actually collected** operating receipts. The correct organizational comparison is a finite-cash, dated-receivables learning choice against a fully costed specialist route that preserves incumbent production. A stronger claim that demand must reduce *realized* B learning is false.

This model uses synthetic normalized coefficients and does not calibrate robotics enterprises, customer receipts, or innovation rates. Its mathematics is standard cash-constrained stochastic dynamic programming, not established publication novelty.

## Environment and exact state

Over dates t=0,1,2,3, accepted complete A service q_A is an integer in {1,2}, with an enforceable A floor of one complete service unit per date. An A customer contract generates an earned invoice R_A(q;m)=m q-q(q-1); the provider simultaneously pays operating cost q. The second unit has lower marginal invoice value, hence demand is concave in accepted output. Earned invoice is **not** collected cash: collection arrives exactly L=1 or L=2 dates later. The firm begins with cash 4. Relative to fully operated A, a shared-hardware qualification attempt reduces A from 2 to 1, costs another 13 immediately, and succeeds with probability 3/4. A genuinely distinct specialist facility can train while retaining A at 2, costs another 20 immediately, and succeeds with probability 9/10. Either route, once successfully qualified, allows identical accepted B production in a separate feasible service window: a new B invoice of 16 with immediate resource expenditure 2, or incremental net operating contribution 14. Outcomes are retained; retries are allowed if affordable. The A and B customer services are **not** robot motion counts; postqualification B uses a non-overlapping window, avoiding double-allocation of the same saturated physical resource.

The state is (C,P_1,...,P_L,z) = liquid cash, ordered receivables awaiting maturity, and retained B qualification. At date t, spendable cash is C+P_1. Action a=(q_A,q_B,i) must satisfy q_A>=1, q_B<=z, and immediate expenditure E(a)=q_A+2q_B+k_i<=C+P_1, with k_i in {0,13,20}. Then

    C' = C+P_1-E(a)
    (P'_1,...,P'_L) = (P_2,...,P_L, R_A(q_A;m)+16q_B)
    z' = z or Bernoulli(p_i).

The exact finite-state Bellman equation chooses the highest expected V_{t+1} across feasible actions and success/failure. Its terminal condition is V_4=C+sum(P_j). All terminal receivables are assumed fully collectible at par and discount is set to zero. Under those explicit assumptions, telescoping the cash ledger yields **terminal wealth = opening cash + earned accepted invoices − immediate operating/qualification costs**, regardless of when the invoices mature. Payment dates change which actions can be financed, not the arithmetic economic contribution of a fixed feasible path. A real credit-risk or discount extension could also change the objective.

## Proposition: non-monotone realized capability investment

After A=2 in t=0 with one-date payment maturity, cash available for a t=1 investment is 4−2+(2m−2)=2m. Shared B training at A=1 needs 1+13=14, and is liquid only for m>=7. Specialist training at A=2 needs 2+20=22, liquid only for m>=11. If training at t=1 is successful, two later B service windows remain. For the single-attempt comparison, relative to carrying on with A=2:

    Shared premium = (3/4)*2*14−13−[(2m−4)−(m−1)] = 11−m.
    Specialist premium = (9/10)*2*14−20 = 26/5.

For any already affordable shared route, demand raises the cost of displaced A production at slope +1 and hence reduces its *incremental* value. Yet crossing the threshold m=7 opens a previously forbidden cash-feasible path; crossing m=11 opens the separately equipped route without sacrificing A. Thus one cannot extrapolate Result 10's within-feasible-path comparative static into a monotonic global investment prediction. The policy may jump from no learning to shared learning and later to specialist training as demand rises.

This is a proof by feasible-set thresholds plus net-return arithmetic, and a finite globally optimized counterexample; it is **not** a general theorem that all demand curves exhibit this exact ordering. It does not arise by granting the specialist free capital, zero labor, or an extra customer service benefit.

## Globally adaptive exact instance and a falsification

The Python model exhaustively optimizes q_A∈{1,2}, the hard A floor, qualified B service, both routes, retrials, available cash and future invoice maturities with rational arithmetic, rather than imposing the proposed t=1 route. The globally optimal expected terminal-equity premiums over A-only operations are:

| A intercept m | L=1 | L=2 | Optimal t=1 route when L=1 |
|---|---:|---:|---|
| 4 | 0 | 0 | produce A |
| 7 | 4 | 0 | shared B development |
| 11 | 26/5 | 0 | specialist B development |

For the six cases the A-only equity baselines are respectively 20, 44 and 76 at both maturities. The L=1 optimized values are 20, 48, 406/5; the L=2 optimized values equal baseline. With L=2 the opening cash supports required A operating expenditures through t=1 but neither additional development program. Waiting to t=2 is unattractive here: only one B service window remains, so the best one-shot incremental shared payoff is (3/4)*14−13−(m−3)=1/2−m<0 for m>=4 and specialist's is (9/10)*14−20=−37/5<0.

**Negative result worth retaining:** invoice maturity is not automatically a welfare loss. With opening cash 20 rather than 4, at m=7 the exact DP gives the same optimized earned-terminal value under one- and two-date invoice maturity. When cash is slack, risk absent and terminal claims valued equally, payment timing alone has no value in this particular model. Other initial-cash settings permit earlier attempts and retries; these are not suppressed merely to preserve a convenient threshold.

## Enforceable multipayer finance counterfactual

At m=7 and L=2, t=1 shared training lacks 12 in spendable cash. Suppose a customer/supplier/lender with valid assignment rights advances exactly 12 at t=1, receiving principal and fee f at t=4. Along both constructed paths with accepted A>=1, liquidity is nonnegative and cash available at t=4 immediately before repayment is 27 if B never qualified and 39 if it did. Hence repayment of 12+f is pathwise feasible for 0<=f<=15. The **net expected project premium** versus A-only is exactly 4−f: advance principal enters and exits the cash account, and it is not additional operating surplus. A fee of 1 leaves premium 3; f>=4 eliminates the private gain, even though the loan remains technically repayable. This is a narrow constructive contract comparison, not a claim that the actual GXO/Agility deal has pledgeable invoices or that these are industry rates. With default, costly collateral enforcement, or bargaining over B upside, the lender/provider/customer state and objective must change.

## Relation to prior theory and observations

GXO's primary **June 27, 2024** release describes the multiyear RaaS agreement with Agility, its Digit/Agility Arc orchestration inside SPANX fulfillment and the real tote handoff from mobile robots to conveyors: https://gxo.com/news_article/gxo-signs-industry-first-multi-year-agreement-with-agility-robotics/. GXO's **October 26, 2026** update reports more than 100,000 tote moves at Flowery Branch, with expansion to other sites *planned* for early 2027: https://investors.gxo.com/news-releases/news-release-details/gxo-and-agility-robotics-expand-partnership-accelerate. They establish meaningful commercial and production relationships but **do not** establish accepted complete-order rates, training displacement, service-floor penalties, issuance/receipt dates or qualification effects. Do not turn tote moves into complete paid orders or planned deployments into observed operations.

The investment/working-capital mechanism is well established in Fazzari, Hubbard and Petersen's **1987** NBER study (published **1988**): https://www.nber.org/papers/w2387. Kaplan and Zingales' **February 1997** *QJE* challenge is essential: investment-cash-flow sensitivity **does not uniquely identify financing constraints**: https://academic.oup.com/qje/article-abstract/112/1/169/1870889. Thus a site with rising sales and new robot adoption does not confirm this model without demand/quality/selection controls and dated cash evidence.

A discriminating matched-site panel would join: accepted complete-order timestamps, A/B units and comparable human/specialist outside process; service-floor clauses and breach reports; earned invoices, exact contractual maturity, actual collections and assignment/credit rights; cash-funded training costs and separate customer/supplier/lender contributions; field-learning/qualification events; safety/attention and A productive-resource displacement. The key negative control is an **amply financed matched site** with identical accepted task opportunities: under this model, accelerating invoices alone should not change its output or investment decision. The broader BEA sector-level production backbone cannot supply this micro panel.

## Verification and continuation

The one-shot formulas and accounting identity are algebraic; the globally adaptive comparisons are **exact finite-instance** results, not a proof for arbitrary functional forms, stochastic payments or continuous multi-payer equilibria. Code and 18 passing local scoped tests include a separate exhaustive policy-tree implementation, dated cash checks, funding-gate checks, and constructive loan outcome paths. Source and test Git blobs are matched to the locally validated files; historical repository CI and independent review have not been run. Every numerical parameter is synthetic.

**Next intellectual action:** incorporate enforceable contingent financing and payment-default states into the same Bellman environment, then ask if customer-funded paid pilots shift qualification selection *net of the customer's retained surplus*. Test demand expiry and non-overlapping physical service windows rather than giving shared learning an unexplained benefit. Preserve the November 22 integrated synthesis and December 25 final target.
