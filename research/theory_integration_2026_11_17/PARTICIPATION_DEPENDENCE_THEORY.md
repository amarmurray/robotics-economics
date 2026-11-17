# When Capabilities Become Production — buyer participation, qualification–payment dependence, and the financing of a production network
**November 17, 2026 | integrated private theory continuation | synthetic assumptions, not empirical estimates.** The source revision for the preceding contingent-claims comparison is f3484326f921193c31ee6d53cff79d1757a6d8ae. This note develops **the same production/qualification argument**, not a new standalone paper.

## Question and constructive answer

The preceding argument used the customer B's expected retained surplus as a possible qualification advance, and B's collectible invoices as lender collateral. That is incomplete when (1) qualifying on hardware already serving A reduces the *A buyer's* own welfare, (2) the payment shock is correlated with successful qualification or surviving demand, and (3) a competent contract can refund a pilot advance if qualification fails.

**Result:** Under an explicitly defined ambiguity set, the same marginal technical qualification and payment probabilities admit a sharp interval of financeable B receipts. B buyers and B lenders have different adverse dependence exposures, so a single contract cannot value both using an independence forecast unless dependence is justified. A compensable A customer can block shared-capacity development even while that program has positive total operating value. A qualified refundable pilot can restore financeability in a precisely specified example, without creating production surplus or changing any hardware skill. The important object is the *joint qualified production–buyer–claim network*, not the average skill rate, invoice face value, or aggregate surplus alone.

This is an application of elementary Fréchet bounds and contract participation, not a claimed novel theorem. The counterexample is more interesting than its numeric threshold because a stronger financing contract **repairs** the tempting first conclusion.

## Economic environment and payer rights

There are three parties with substantive production stakes: an incumbent **A buyer**, a future **B buyer**, and a robotic provider; a fourth party, a nonrecourse lender, may advance funds. All values are incremental to an actual feasible alternative. The provider initially supplies complete accepted A service. A development route j may displace an accepted A service, thereby losing provider margin d_j and **separately** losing A buyer retained value a_j. If the A agreement permits volume reduction upon compensation, the A buyer can consent for a date-1 payment of at least a_j. If the A contract instead requires two non-substitutable accepted A services, the shared route is infeasible regardless of the financing inequalities. Do not call robot moves complete A orders.

Let Q be the binary B qualification outcome, with probability p_j. Let S indicate that the second B service opportunity survives to date 3, with marginal probability s. Here Q and S are independent solely to isolate the **payment-dependence** question; we do **not** assume independence of payment shocks from qualification or demand. At dates 2 and 3 the *accepted* B service counts are respectively N_2=1_Q and N_3=1_Q 1_S. The B buyer receives incremental gross value V per accepted complete service and is billed invoice face R for each; the provider pays real operating cost k per accepted B service.

Define Y_2 and Y_3 as **potential payment events**, with ex ante marginal probabilities r_2 and r_3. These events are meaningful even where Q=0 and no invoice can arise: they represent potential payment capacity or honorability in a counterfactual service world. Actual B collections are R(1_Q 1_Y2 + 1_Q 1_S 1_Y3). Realized nonpayment is modeled only as a transfer from provider to buyer. Any bankruptcy deadweight cost, denial of service acceptance, loss of buyer consumption value, collection/legal expense, or correlation with A defaults must be separately modeled. In actual warehouse data, these potential Y events may be unobservable in the unqualified states; their assumed marginal distributions are **not identified from paid invoices alone**.

A nonrecourse lender can be assigned at most fraction theta of actual B collections, and requires at least zero expected return under *every* distribution in the specified dependence set. A B buyer can make an informed, fixed date-1 pilot advance P, and requires nonnegative expected retained value under every distribution. A buyer requires immediate compensation a for any displaced incumbent value. A lender advances L at date 1; its repayment is a fraction eta of collections, with eta<=theta. Provider voluntary service and dated pathwise liquidity are additional constraints, never inferred from aggregate expectation.

## Proposition 1 — sharp collected-claim bounds holding accepted service fixed

Write h=p_j s and n=p_j+h=E[N_2+N_3]. Hold Q independent of S, but allow arbitrary dependence of Y_2 and Y_3 with Q,S and each other, subject only to their specified marginals.

Then expected B receipts X obey the **sharp** bounds

    X_low / R = max(0,p_j+r_2-1) + max(0,h+r_3-1)
    X_high / R = min(p_j,r_2) + min(h,r_3).

The independent-payment forecast would instead be

    X_ind / R = p_j r_2 + h r_3.

**Proof.** Each paid service is the intersection of its qualified acceptance event (Q, or Q AND S) and its potential payment event Y_t. For events of probabilities u and v, the exact intersection range is [max(0,u+v-1), min(u,v)]. These are the classical Boole–Fréchet bounds. Since no cross-window relation among Y_2,Y_3 is prescribed, choose each payment event's conditional allocation on the *same* Q,S probability space to attain either endpoint, and couple the two payment events conditional on Q,S arbitrarily. Thus the sum endpoints are feasible simultaneously, not merely two incompatible separate inequalities. An independent 16-atom linear-programming oracle, which fixes P(Q), P(S), P(Q AND S), P(Y2), P(Y3), attained both displayed extremes for each synthetic route. This argument is specific to the limited set of constraints; observed within-customer cross-window correlations or safety/default states generally tighten the bound.

**Interpretation.** Neither two marginal payment rates nor a marginal qualification benchmark identifies receivable pledgeability. Published technical task success or aggregate tote counts cannot identify these joint events.

## Proposition 2 — robust buyer/lender participation is a joint claim-allocation constraint

Under risk-neutral, zero-discount, enforceable date-1 transfers, nonrefundable P, and the B buyer retaining gross accepted-service value V even if an invoice defaults, define

    U_min = V n - X_high                 (B buyer's worst retained surplus)
    M_min = theta X_low                 (lender's robust pledge ceiling)
    D_j = K_j + q_A,1,j - 2             (date-1 funding gap before A compensation).

For a fixed nonrefundable P and L to meet the *initial* participation and funding conditions across all possible dependences, it is necessary and sufficient that

    0 <= P <= U_min,   0 <= L <= M_min,   P+L >= D_j+a_j.

Consequently, an initial-funding split exists **if and only if**

    D_j+a_j <= U_min + M_min.

This equivalence applies **only to the initial funding split**. Full implementation ALSO requires the A buyer's contractual permission and consent, provider nonnegative expected continuation value, voluntary service after qualification, legal collection rights, and nonnegative dated cash on every required outcome path. We verify those separately in the examples.

**Proof.** The B buyer is worst off when B invoices are most likely paid; hence P cannot exceed Vn-X_high. The lender is worst off when collections are least likely; hence eta X_low >= L, so L <= theta X_low. If a_j is paid up front to obtain A consent, the provider's date-1 funding need rises by exactly a_j. Necessity follows by addition; sufficiency for initial disbursement follows by splitting the total gap between the two intervals. The two worst distributions generally differ: the robust bound protects **two counterparties** over the same ambiguity set, not a purported single worst joint realization.

For a **fully refunded pilot on Q failure**, assume repayment of P at a late settlement date is legally enforceable and *pathwise affordable*. The B buyer's expected net pilot payment is p_j P, so the corresponding initial split uses

    p_j P <= U_min,   L <= M_min,   P+L >= D_j+a_j.

The resulting maximum initial advance can rise to U_min/p_j+M_min (p_j>0). This does not imply that every such advance is implementable: the provider must repay refunds on Q failure and satisfy its own participation incentive. A buyer-funded loan without actual refundable security should not be described as this contract.

## A serious counterexample, and its repair

Keep the prior note's exact synthetic inputs: s=r_2=r_3=9/10, V=24, R=16, k=2, theta=1/2; shared Q probability 3/4, cost K=13, provider A-margin loss d=4; specialist Q probability 9/10, K=20, no A displacement. Both provide identical **qualified B complete service**; only development resource use and success differ. The incumbent A production has the same date-0-to-date-5 flow as the earlier exact waterfall, with opening liquid cash 4, two A costs at date 0, and twelve units of A collections at dates 2, 4 and 5, plus 7 or 12 date-3 A collections depending on whether shared hardware displaces one date-1 A service. No A payment default is assumed.

| Exact synthetic measure | Shared A hardware | Independent specialist |
| --- | ---: | ---: |
| Expected accepted B services n | 57/40 = 1.425 | 171/100 = 1.71 |
| B receipts under independent payment | 513/25 = 20.52 | 3078/125 = 24.624 |
| Sharp receipts interval [X_low,X_high] | [98/5, 114/5] = [19.6,22.8] | [604/25,684/25] = [24.16,27.36] |
| Robust B buyer pilot ceiling U_min | 57/5 = 11.4 | 342/25 = 13.68 |
| Robust B lender ceiling M_min | 49/5 = 9.8 | 302/25 = 12.08 |
| Total robust **nonrefundable** initial financing ceiling | 106/5 = 21.2 | 644/25 = 25.76 |

The prior shared pilot P=12 passed B buyer participation under independent receipts (B retained value 13.68), but it fails under a permissible positive qualification/payment coupling (B retained value only 11.4). This failure occurs with **unchanged p, s, both payment marginals and qualified service productivity**.

Now endogenize **A buyer participation**, instead of silently giving the displaced A customer zero residual value. With a modest hypothetical A retained-service loss a=3, a shared contract P=11 plus robust lender L=4 covers the full initial gap 12+3=15, compensates A, and leaves B buyer, lender and provider nonnegative under every coupling. Specialist P=12 plus robust loan L=8 covers 20 with no A injury. For both alternatives, the minimum date-by-date provider liquid cash over all 16 binary outcome paths is **zero**, and the robust service margins are positive. Total real value relative to A-only is shared 227/20=11.35 and specialist 881/50=17.62; these include the A customer's incremental lost value and are invariant to payment correlation under the stated no-deadweight-default assumption.

To test a harder incumbent-buyer objection, set a=10 **without changing robots, the B service, acquisition probabilities, or receipts**. Shared total real value remains positive, 87/20=4.35. But immediate A compensation expands its funding need to 22. With *independently* priced B claims and nonrefundable buyer participation, the available envelope is 1197/50=23.94, seemingly adequate. Under unrestricted payment dependence, its robust nonrefundable envelope is only 106/5=21.2, so **no fixed nonrefundable P, L split** satisfies all initial funding and participation conditions. This is a conditional impossibility for that contract class, not an impossibility for robotic deployment generally.

**Competent repair rather than novelty inflation:** Offer an enforceable, success-contingent B pilot P=14, refunded in full if Q fails, alongside a robust nonrecourse B loan L=8. Ex ante B buyer cost of the pilot is (3/4)*14=10.5, below its worst retained value 11.4. The loan receives fraction eta=20/49 of actual B collections, below the half-receipts cap, and earns at least its 8-unit advance under every allowed coupling. The twenty-two units received at date 1 fund shared qualification plus the A buyer's full ten-unit compensation. Exact model outcomes give worst expected incremental provider value **1/4**, worst B buyer value **9/10**, lender zero in its worst dependence distribution, A buyer exactly compensated, and minimum liquid provider cash **zero over every path**, including Q failure and its date-5 refund. (The buyer, provider and lender worst expectations need not arise under the same coupling, so do not add them as though they do.)

This demonstrates the boundary honestly: *dependence and incumbent participation can defeat an independently costed, nonrefundable pilot; a stronger conditional contract can restore a productive opportunity*. It is a precise economic-design issue, not a general preference for vertically integrated firms or specialists. If the refund is not credibly collateralized, if A requires two undisturbed orders, if A collections can default, or if the B buyer cannot legally commit, the repair may fail.

## Explicit accounting, prior art and empirical tests

For any path, with N accepted B services and Y collected B invoices, B gross customer value VN, B operating resource cost kN, qualification cost K, A provider margin displaced d, and A buyer surplus lost a, the **sum of incremental** provider, A buyer, B buyer and lender payoffs is

    VN - kN - K - d - a.

All pilot payments, refundable advances, secured loans, loan repayments and A consent payments cancel as transfers in that identity. In the example the aggregate is *not* X, and B receipt default alone does not alter real value. With bankruptcy administration, lost accepted orders, real verification costs or safety incidents, add those real effects and possibly correlated lost value. Ex-post bankruptcy and performance moral hazard are not settled by ex-ante IR.

**Prior theory (not novelty):** Boole–Fréchet intersection bounds are classical; one useful methods reference is https://dberleant.github.io/papers/Sandia04.pdf (2004, §2.3). Holmström and Tirole, *Financial Intermediation, Loanable Funds, and the Real Sector*, QJE 112(3), August 1997, DOI 10.1162/003355397555316, already analyze capital constraints, pledgeability and intermediaries: https://academic.oup.com/qje/article-abstract/112/3/663/1926881 . We make **no priority claim** for probability bounds or contract-theoretic funding conditions. The paper's candidate contribution remains their measurement-linked organization within qualified multi-service robotic production.

**Primary operational relation (not contract terms):** GXO and Agility reported a live Digit–AMR–conveyor tote-handoff workflow and RaaS agreement on June 27, 2024: https://gxo.com/news_article/gxo-signs-industry-first-multi-year-agreement-with-agility-robotics/ . Their October 26, 2026 update reports 100,000-plus totes moved at the existing Flowery Branch facility and **planned** additional sites starting in early 2027: https://investors.gxo.com/news-releases/news-release-details/gxo-and-agility-robotics-expand-partnership-accelerate . These releases do **not** identify complete accepted buyer orders, task-learning transfer, A customer's marginal retained service value, B qualification outcomes, invoice collection risks, assignment rights, B pilot deposits or enforceable failure refunds. No model parameter is fitted from these issuer figures. A verified assignment/legal audit would require the actual contract and jurisdictional documents, not generalized Article 9 text.

**Empirical test that distinguishes mechanisms:** At matched customer sites, record each complete accepted A and B order; whether missing A work had a competent human/specialist alternative; customer gross willingness to pay and retained surplus, rather than provider margin alone; data/training and qualification provenance; customer B demand surviving after qualification; payer creditworthiness *even during unqualified counterfactual periods*; invoice face versus cash collection dates; and exact up-front pilot/refund/recourse/priority rights. Estimate Q/S/payment dependence conditional on buyer and site, separately from marginal task success. Test whether qualified specialist production wins because it avoids A customer displacement, not merely because shared-hardware invoices are delayed. A strong negative control is the fully funded/same-qualified-service setting: cash-claim assignments alone should not alter accepted operating productivity in this frictionless model.

## Reproduction and status

New files in this directory: **participation_coupling.js**, **test_participation_coupling.js**, **participation_results.json**, with separate teaching and solutions. The source and test are dependency-free Node.js scripts (run node test_participation_coupling.js), but the Node command and historical repository suite have **not** been executed here. The exact source string was evaluated in a V8 isolate and checked against 35 exact-rational assertions from the committed test string (the separately committed Node file includes equivalent assertions). An **independent local Python fractions/scipy LP** suite passed 13 tests, including sharp extrema over all 16 joint event states for both routes and pathwise refund-solvency checks. Do not relabel this as independent peer review or real robotics calibration.

**Exact next intellectual action:** Relax the certain A collections that collateralize late refunds. Couple A collection default and site-level demand/qualification failures, introduce the real loss of complete orders when defaults interrupt service, and determine whether the refund-based restoration survives **statewise collateral, A buyer renegotiation, and a competent specialist alternative**. Keep the November 22 theory synthesis, November 29 empirical backbone, December 6 contribution review and December 25 delivery targets; none is declared passed.
