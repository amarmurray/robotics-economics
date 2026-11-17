# When Capabilities Become Production — contingent qualification, expiring demand and multipayer claim rights
*Integrated theoretical continuation, November 17, 2026. Private working draft; synthetic, not a separate paper or empirical estimate.*

## Question and claim boundary

Can a provider rationally invest in a qualification that is profitable after financing, yet fail to raise a required initial advance from **the project's own receivables**? Can a paid customer qualification program and a risk-bearing lender together finance a different, more efficient specialist route? Result 11's exact dated-receivable model established that cash-maturity gates can reverse realized learning choices. We retain its accepted-order production, A-service floor, four operating dates and competent specialist comparator, but change the right to monetize particular future B claims and admit uncertain order demand and nonpayment.

**Constructive conclusion:** In a specified competitive, risk-neutral, enforceable-transfer environment, project-specific collateral and customer willingness to advance funding are distinct pools. Neither is a synonym for total surplus. When the two pools are contractually accessible together, a specialist path can be mutually preferable even though no B-receivables-only lender would cover either route's initial funding gap. This is an application of familiar pledgeability, incomplete-contract and investment logic. It is not a general proof that a particular robotics company is financeable, or a novel theorem.

## Economic environment: same production network, dated accounts

The already-qualified A service is a complete accepted customer service, not a robot movement. Dates 0 through 3 carry A service with an accepted-output floor of one unit. Initially liquid cash is 4. At date 0 two accepted A units cost 2, generate an invoice of 12 collectible at date 2, and leave cash 2. Without development, two A units at each operating date yield terminal fully collected provider cash 44.

At date 1, the provider selects one retained B qualification program:

- Shared: use productive A hardware, provide one accepted A unit at date 1, pay qualification cost 13, and achieve the B qualification with probability 3/4. Immediate cost is 14, a financing shortfall of 12; the opportunity loss from displaced A accepted service is 4.
- Specialist: preserve two accepted A units using separate qualification equipment, pay qualification cost 20, and achieve the B qualification with probability 9/10. Immediate cost is 22, a shortfall of 20. Unlike shared hardware, this route has no displaced A-output contribution.

A qualified B system may deliver **one complete accepted B service** at date 2 and an additional one at date 3 if its customer remains active. Date-2 B demand is certain conditional on qualification; date-3 survival is sigma=9/10. A B service earns an invoice of 16 and costs 2 to operate, with independent probability r=9/10 that the invoice is collected. Successful date-2 B invoices settle at date 3, and date-3 invoices at date 4. The buyer's gross value per accepted B service is 24, inclusive of its feasible service alternative and measured on the same incremental basis. A invoices mature after two dates; the provider can operate B in a **non-overlapping window** without double-using A capacity. Qualification is retained, independent of later buyer payment; customer expiry and invoice nonpayment are exogenous in this diagnostic.

These are deliberately synthetic assumptions. A's customer residual surplus is taken as zero for the accepted A contract, and its invoice schedule equals the value relevant to the provider comparison. For general customer welfare one must separately measure the A buyer's value lost when shared training displaces service.

## Proposition: a claim-specific financeability envelope

For route j with qualification probability p_j, define n=1+sigma as expected B demand windows following success, R as B invoiced price, r as collection probability, V as gross B buyer value, k as cost per B accepted service, K_j as qualification cost and d_j as lost incumbent contribution. Its fixed-route **unfinanced** expected provider premium relative to continuing A is:

$$
\Delta_j=p_j n(rR-k)-K_j-d_j.
$$

The future *actually collectible B invoice* amount in expectation is X_j=p_j n rR. The buyer's expected retained incremental value **before a new pilot fee** is U_j=p_j n(V-rR). Both are conditional on qualified B complete-service acceptance. They are not current liquid cash.

Suppose an unrelated risk-neutral, zero-discount lender provides an immediate **nonrecourse** loan L in exchange for an enforceable fraction eta of actual future B collections, subject to a contractual cap theta. No external claim on A, equipment, guarantees or unrelated assets is permitted. Lender break-even demands L <= eta X_j. A provider that can decline B service after qualification must retain enough expected receipt to pay its operating cost: (1-eta)rR >= k. Therefore the *effective* maximum claim fraction is:

$$
\bar\eta=\min\{\theta,\;1-k/(rR)\},\qquad
M_j=\bar\eta X_j,
$$

provided rR >= k. With a prepaid nonrefundable customer pilot/setup fee P, the buyer's ex-ante individual-rationality condition is P <= U_j. An initial required external funding gap D_j can be covered by these two pools only if

$$
D_j \le M_j + U_j.
$$

Under the additional assumptions that buyer and lender can commit and disburse at date 1, the lender may take fractional claims, the buyer accepts the success risk, and subsequent dated cash balances along every supported outcome path remain nonnegative, this condition is **sufficient** for the initial funding gap as well: choose L <= M_j and P <= U_j with L+P=D_j, and assign eta=L/X_j. For a strictly positive intermediary fee, discounting, adverse selection, financial covenants, competing liens, buyer vetoes or ex-post nonperformance incentives, the inequality is not sufficient.

**Proof:** A lender cannot receive more in expectation than the portion of collectible invoices it can legally seize while leaving the provider willing to serve, yielding L<=M_j. A buyer will not voluntarily surrender more in an ex-ante certain-equivalent nonrefundable deposit than its value from the qualified B program, yielding P<=U_j. Thus their joint date-1 transfer cannot exceed M_j+U_j. Conversely, when the stated enforcement and operating assumptions hold, split the shortfall between the two bounded pools; date-1 expenses are funded. Forward liquidity is a separate condition, verified pathwise below. This is a cash-claim allocation identity with incentive restrictions, not a general implementation theorem.

**Crucial distinction:** A financially valuable project can have X_j substantially below its customer value and can have M_j below its required advance. Nor may a model simply assign the entire customer surplus to the provider without a contract, credible outside option and observed customer consent.

## Exact example and a competent alternative

Take theta=1/2, sigma=9/10 and r=9/10, with the costs and qualification rates above. All amounts are normalized exact rational values.

| Measure | Shared A hardware | Qualified specialist |
| --- | ---: | ---: |
| Date-1 funding gap D | 12 | 20 |
| Expected collectible B invoices X | 513/25 = 20.52 | 3078/125 = 24.624 |
| B-only pledge ceiling M | 513/50 = 10.26 | 1539/125 = 12.312 |
| B buyer's expected retained value U | 342/25 = 13.68 | 2052/125 = 16.416 |
| Unfinanced expected provider premium Delta | 67/100 = 0.67 | 301/250 = 1.204 |
| Maximum combined pledge and customer-funding envelope | 1197/50 = 23.94 | 3591/125 = 28.728 |

Thus **both routes are positive-profit if a competent bridge were available, but neither can borrow its entire funding gap solely against the eligible half of B receivables**. A customer who accepts qualification risk can pay 12 at date 1, satisfying P<=U_shared and fully funding shared development. A specialist route can instead be funded with the same 12 customer payment plus a risk-neutral loan of 8. The specialist lender takes eta=500/1539 of B collections (less than the contractual 1/2 cap), which yields expected repayment exactly 8. A remaining provider share maintains positive operating incentives.

The executable four-Bernoulli-event enumeration checks every qualification/survival/payment outcome and the entire date-0-to-date-5 cash waterfall. All sampled paths have nonnegative liquid cash at every operating date (the smallest cash is zero). Against the A-only provider equity baseline of 44, the **nonrefundable** pilot comparison is:

| Expected incremental payoff | Shared + customer 12 | Specialist + customer 12 + loan 8 |
| --- | ---: | ---: |
| Provider | 1267/100 = 12.67 | 3301/250 = 13.204 |
| B buyer | 42/25 = 1.68 | 552/125 = 4.416 |
| Lender | 0 | 0 |
| Accounted joint value | 287/20 = 14.35 | 881/50 = 17.62 |

Both provider and B buyer prefer the specialist under this **same customer deposit** counterfactual. An apparent provider preference for the smaller shared project's immediate financeability would be an artifact of excluding the competent combined customer/lender arrangement. No financing principal is counted as production output.

**Stronger objection — ex-post risk to the pilot buyer.** The nonrefundable deposit makes the buyer lose 12 if qualification fails; ex-ante IR does not imply ex-post IR. We therefore also test a contractual refund at date 5 only when B qualification fails. The same cash paths can fund the refunds. Expected provider/buyer incremental payoffs become shared (967/100,117/25) and specialist (3001/250,702/125). The lender remains at zero, aggregate joint values remain unchanged, and specialist remains preferable to both provider and buyer under this example. This refund alternative assumes enforceable commitment and sufficient collateral or A income to repay in the failed state; it is not an observed paid-pilot term.

## Pathwise accounting identity and stronger boundaries

For any history with N accepted B services and Y collected B invoices, the provider's incremental return against continuing A, before standard financing fees, is

$$
\Pi_P=R Y-kN-K_j-d_j+P+L-\eta RY-\text{refund},
$$

the B buyer's incremental value is Pi_C=V N-RY-P+refund, and the lender's payoff is Pi_L=eta RY-L. **Path by path** their sum is VN-kN-K_j-d_j. Consequently pure advances, partial defaults and repayment allocations do not by themselves create real surplus in this frictionless accounting; they change actor-specific cash, feasibility and incentives. If failure involves real bankruptcy, verification, rework, litigation, legal enforcement, costly guarantees, customer harm, or discounting, introduce those costs explicitly.

The operating-incentive cap has a genuine bite when eta>1-k/(rR): a lender cannot assume the provider will voluntarily serve accepted orders whose residual expected cash does not cover marginal operating expenses. In this numeric comparison contractual theta=1/2 is the binding cap; the incentive cap is 31/36. Actual claims may also be unavailable or junior despite a large expected invoice face.

**Demand expiry matters twice:** it reduces the provider's expected benefit from acquiring B and shrinks both financeable invoice claims and the buyer's permissible advance. For example, the shared route has positive unfinanced premium only when sigma > 77/93; the specialist route's corresponding threshold is sigma > 221/279. These are economic benchmarks for the constructed finite dates, not sector forecasts. A different B price, superior human alternative, more demanding complete-order acceptance, joint payment/qualification default or later qualification date can shift them or overturn the comparison.

## Primary-source relation ledger and measurement test

- **Observed commercial and physical service relationship, NOT payment terms:** GXO and Agility's June 2024 commercial RaaS agreement and the October 26, 2026 issuer update on Digit tote moves and proposed 2027 sites show a qualified ongoing customer relationship and heterogeneous physical handoffs, not a joined panel of end-customer accepted orders, B qualification success, invoice default, customer deposits, pledge rights or lender claims. Source: https://gxo.com/news_article/gxo-signs-industry-first-multi-year-agreement-with-agility-robotics/ and https://investors.agilityrobotics.com/news-releases/news-release-details/gxo-and-agility-robotics-expand-partnership-accelerate . The planned 2027 sites are NOT 2026 observed deployments.
- **Legal background, NOT contract verification:** New York's UCC section 9-406 as shown November 17, 2026 deals with notice, identification and limitations of assignment. It expressly contains an account-debtor option concerning notice purporting to assign less than a full installment, and separate legal conditions. This cannot prove any project has an assignable half invoice or first-priority enforceable security. Source: https://www.nysenate.gov/legislation/laws/UCC/9-406 .
- **Issuer-described emerging finance model, NOT completed financing:** Zunya's current site discusses contract/robot/site-based fleet finance but explicitly says its first loan disbursements are planned for Q1 2027. Do not count that as an originated 2026 robot finance contract. Source: https://zunya.co/ .
- **Prior theory:** risk-dependent credit rationing and secured/pledgeable income are established corporate finance topics, not new implications of robotics. Stiglitz–Weiss, *American Economic Review* 71 (1981), 393–410, and the earlier Fazzari et al. versus Kaplan–Zingales debate warn against reading financing constraints mechanically from investment and cash flow.

The discriminating site-level panel needs task/site/customer ID, **complete-order acceptance** and alternate feasible human/specialist process, A production displaced by training, qualification success and failed attempts, B demand arrival and expiration, invoice *face*, actual collections/default, contractual payer and deposit/refund schedule, legal claim assignment/notice/priority/recourse, loan timing and whether A or B receivables are pledged, settlement waterfall, and safety staffing. Empirical tests would distinguish (i) technically profitable B opportunities that cannot fund themselves from their own receipts, (ii) funded customer co-investment for the same service, and (iii) the financing and operating ranking relative to a genuinely competent specialist. An amply funded or fully fungible-claims comparator is a necessary negative control. Public product announcements do not identify these observations.

## Exact reproducibility and next step

Files: contingent_claims.js, test_contingent_claims.js and contingent_claims_results.json in this directory. Node.js 18+ has no third-party dependencies. Run node test_contingent_claims.js and node -e "console.log(JSON.stringify(require('./contingent_claims.js').snapshot(),null,2))" from this folder. The 107 scoped exact-arithmetic assertions were executed using the **same committed-source and test strings** in a JavaScript runtime; an independent Python rational event enumeration matched both the refundable and nonrefundable expected distributions. The committed Node test command and full historical repository suite have **not** been run in the connected environment, and no outside audit or robotics calibration exists.

**Next:** Give buyer deposits and assignable claims an explicit contract-formation stage with *endogenous* buyer participation and full A-customer welfare, then challenge the apparent route ranking with bargaining, correlated default and priority claims. Separate actual accepted warehouse orders from token tote moves and link manufacturing scale or digital coordination costs to production feasibility. Keep the Nov 22 synthesis review, Nov 29 empirical backbone target and December 25 final edition, with all unclosed gaps disclosed.
