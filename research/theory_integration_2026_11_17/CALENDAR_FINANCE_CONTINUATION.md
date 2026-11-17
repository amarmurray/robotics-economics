# Calendar receipts, intermediate production and financing: integrated theory continuation
*17 November 2026 · Private research, not a separate Q-number paper*

**Question.** Does Result 7's short-budget/long-budget ordering of targeted versus joint qualification persist after allowing actual dates, qualified production *during* learning, and competent financing? **Not generally.** Under a different, clearly stated economic environment, the direction of the *calendar-horizon* reversal can run opposite to the earlier *available cash-budget* reversal. Productive intermediate states can finance later development; funding can relieve liquidity while leaving a strictly physical/calendar bottleneck untouched. The classical Bellman and working-capital identities below are not claimed novel.

## 1. Operating and qualification economy

S is a retained, qualified **complete-service** set, not a collection of robot motion benchmarks. Customer state theta_t specifies task demand, price or contract, feasible human/specialist outside option, quality acceptance, rights and time-to-expiry. The operating problem from Results 1–6 chooses accepted q within qualified physical/attention recipes. For example with G_t(q)=(d_t-w_t)q-bq²/2 and qualified capacity K_S, efficient q=min(K_S,max(0,(d_t-w_t)/b)); this is not rated cycle output. Manufacturer, deployer, buyer and lender have separate accounts. r_t(S) below is the deployer's **actually collected net operating cash rate**, not gross welfare, invoice accrual or robot data value. An agreed contract maps accepted q into collections, and collection delays may make receipts differ from billed amounts.

Each qualified service can continue operating on **separate equipment/resources** while one learning program j uses development effort at cost c_j per calendar time; a success at known hazard lambda_j adds a typed bundle A_j and is retained. If training actually displaces the same production asset, replace r_t(S) with the action-dependent feasible flow: the present baseline must not count undeliverable concurrent revenue. No terminal strategic-data premium is added. One active program, optional stopping, no artificial independent labeling of a joint acquisition.

For an unconstrained, sufficiently funded provider, the finite-calendar continuation equation is

\[
-\partial_t J_t(S)=r_t(S)+\max\left\{0,\max_j[\lambda_j(J_t(S\cup A_j)-J_t(S))-c_j]\right\},\quad J_T(S)=0.
\]

The zero option halts **development**, not already-qualified operating service. For fixed r, remaining horizon h=T-t gives a scalar finite-state forward ODE initialized at zero. The first-step Bellman proof and standard martingale verification are identical in form to Result 7, except that benefits are *flowed into production during acquisition*, rather than paid as a terminal lump. This is standard controlled jump-process reasoning. The HJB by itself DOES NOT enforce sample-path liquidity or distinguish invoice/collection delays.

## 2. Exact route result: the calendar reverses the previous conclusion

Take S in {0,A,B,AB}. After A, one accepted service earns net collected rate v; B alone earns zero; AB earns W>v and 0 earns zero. Programs A then B have independent exponential times with rate a, and a **genuine joint outcome** AB arrives with rate mu. Development costs c per active calendar time in either program; no fictitious complementary productivity premium.

For the precommitted paths A→B and joint AB, let
\(I_k(T)=\int_0^T e^{-kt}dt,\quad H_k(T)=\int_0^T te^{-kt}dt.\)
State probabilities in sequential development are
\(P(A\text{-only at }t)=at e^{-at}\),
\(P(AB\text{ by }t)=1-e^{-at}(1+at)\);
the probability active development remains is \(e^{-at}(1+at)\).
For the joint path, \(P(AB\text{ by }t)=1-e^{-\mu t}\).
Integrating actual operating and effort flows yields EXACT expected net path values:

\[
V_{\rm seq}=vaH_a+W(T-I_a-aH_a)-c(I_a+aH_a),
\qquad V_{\rm joint}=W(T-I_\mu)-cI_\mu.
\]

**Proposition C1 (calendar reversal for fixed paths).** With a/2<mu<a, c>0 and 0<v<W, if

\[
(W+c)(2-a/\mu)<v<(\mu/a)(W+c),
\]

then the joint path has strictly greater net value for sufficiently short positive horizons, while the A-first staged path has strictly greater net value for all sufficiently long horizons. Proof: expansion and integration give

\[
V_{\rm seq}-V_{\rm joint}
=\frac{av-\mu(W+c)}{2}T^2+O(T^3)
\]

and

\[
\lim_{T\to\infty}(V_{\rm seq}-V_{\rm joint})
=\frac va+(W+c)(1/\mu-2/a).
\]

The interval between the two v bounds is strictly positive since their difference is \((W+c)(a-\mu)^2/(a\mu)\). This does not require an invented strategic-data reward; accepted intermediate production creates the advantage. It is a **comparison of committed paths**, which can have negative value near T=0 because they keep paying rather than stopping.

**Stronger adaptive benchmark.** Solve the HJB with stopping and switching. For synthetic normalized a=2, mu=1.2, v=4.5, W=10, c=1, the adaptive initial choice is stop at T=.02, joint AB at T=.5 (present value about .8877555), and target A at T=2 (present value about 11.71794). A second independent numerical discrete Bellman calculation in the locally preserved package agrees within the stated errors; the committed JavaScript RK4 implementation agrees with the independent Python/SciPy solver. These numerical decisions do not prove exact switching dates.

**Analytical long-horizon optimality, not merely a fixed-path claim.** If W strictly exceeds all intermediate flow rates and successful programs have finite positive hazards, a completing policy incurs finite expected total **lost W receipts plus development costs**, while a policy permanently failing to complete incurs an unbounded lost-flow gap. Let D(S) be minimal lost-flow-plus-cost until full service. Memorylessness and first-success renewal conditioning yield

\[
D(AB)=0,\quad D(A)=(W-v+c)/a,\quad D(B)=(W+c)/a,
\]
\[
D(0)=\min\{(W+c)/\mu,\ (W+c)/a+D(A),\ (W+c)/a+D(B)\}.
\]

A mid-wait policy switch cannot improve this constant-rate stochastic shortest-path recursion because no information arrives before an acquisition event. The long-horizon HJB has \(J_{T-h}(0)=Wh-D(0)+o(1)\). Under the synthetic example the A-first route has deficit 8.75, the joint route 55/6≈9.16667, and B-first 11. Thus target A eventually becomes strictly optimal even with a competent fully adaptive controller. This is an opportunity-cost calculation, not a new R&D funding theorem.

**Time-varying demand matters independently of learning.** In an explicit dated backward-HJB check, AB receipts are 10 only before an expiry tau=.5 and thereafter equal the A-only flow 4.5. Holding all hazards constant and T=5 lowers beginning provider value from ≈41.2521 to ≈19.9197. If a qualification never changes any future feasible production or receipt after t, paying to acquire it after t is dominated; this is an immediate state-continuation dominance, not an estimated market effect. Future work should make order mix and buyer response theta_t endogenous rather than treat expiry as calibration.

## 3. Financeability is a *dated cash-path* property

For a deterministic plan with paid cost C_u and **collected** receipt R_u in each ordered date bucket, no credit and initial cash B, the necessary and sufficient condition is

\[
B+\sum_{u\le t}(R_u-C_u)\ge0\quad \forall t;
\quad B_{\min}=\max\{0,\max_t\sum_{u\le t}(C_u-R_u)\}.
\]

Necessity and sufficiency follow from the cash-balance identity. Equal total revenues/costs do NOT imply equal peak financing needs: C=(1.5,1.5,1.5), collected R=(0,2,2) requires 1.5 initial cash; the same 4 received *after* the last cost needs 4.5. If spending precedes collection within a date, split the bucket before applying this equation. It is elementary working-capital arithmetic, but essential to avoid calling billed service or customer savings 'cash available for learning.'

A transparent stochastic self-funding case: stage A has hazard a and initially can be paid for only B/c time units from cash B. Upon A success, accepted A service immediately yields *collected* net v>=c while B training still costs c, so B can continue without additional external finance. If B's acquisition hazard is b, the probability that full AB qualification occurs by date T is exactly

\[
P_{\rm staged}(AB\le T)=
\int_0^{\min(T,B/c)} a e^{-as}(1-e^{-b(T-s)})ds.
\]

A joint-only program from the unproductive zero state with legally available **loan/advance** L instead has

\[
P_{\rm joint}(AB\le T)=1-e^{-\mu\min(T,(B+L)/c)}.
\]

For a=b=2, mu=1.2, B=.5, T=2, c=1 and v=4.5, probabilities are ≈.61380492 staged versus ≈.45118836 joint without finance. An additional joint advance of ≈.29284387 cash *matches completion probability* if it is available immediately. It does **not** imply equal expected profit, feasibility of repayment, welfare, customer participation or data rights. An advance cannot surpass the calendar technical ceiling 1−exp(−mu T), however large L is. No supplier credit is assumed free. With delayed A invoices, lost simultaneous production, v<c, or nonpledgeable collections, the bridge may disappear.

**Competent financing baseline:** a nonrefundable 'paid pilot' is not assumed to exist. A buyer advance today against tomorrow's P invoice must be subtracted from the later balance and may carry refund/escrow liability on failure. A manufacturer or equipment financer can shift the date and owner of cash, but intra-coalition transfers do not create gross productive surplus. Private rankings can diverge because receivables, collateral, contract rights and credit constraints are actor-specific. A fully incentive-compatible multipayer credit equilibrium is **not** solved in this tranche; the full cash state would include deployer and supplier balances, receivable maturities, contractual liabilities and contingent success.

## 4. Real workflows, closest prior art, and discrimination

DHL Group [May 13, 2025](https://group.dhl.com/en/media-relations/press-releases/2025/dhl-group-signs-mou-with-boston-dynamics-and-accelerates-cross-business-automation-strategy.html) says Stretch entered commercial unloading in North America in 2023, describes case picking as a further development priority, and identifies testing/co-investment cooperation. This separates a reported incumbent production service from a proposed target but does not establish modeled A/B success events, shared resources, receipts or pilot financing. [Formic, June 29, 2026](https://formic.co/resources/articles/how-to-rent-a-robot-for-cpg-end-of-line-packing), describes flat monthly RaaS rates with performance/service commitments, a **contrast** to instantly collected per-unit flow. [Cardinal Robotics](https://www.cardinalrobot.com/financing.php) self-describes equipment financing involving manufacturer payment and monthly customer rentals, subject to customer and hardware underwriting; it does not validate an unrestricted loan for unqualified development. All are issuer descriptions, not site-calibrating data.

Roberts–Weitzman, *Econometrica* 49(5), 1981, [MIT primary archive](https://dspace.mit.edu/entities/publication/33bd2a42-b38b-4aa3-beaa-33574292681a), establishes sequential R&D funding and stopping as substantial prior art. This project extends application to **simultaneously productive qualification states and actual payer/receipt timing** but has not established original mathematical priority. The introductory terminal-benefit assumption was inspected in the author-hosted PDF text; screenshot retrieval timed out and a full proof replication is not claimed.

**Discriminating data**: same-site complete accepted order/service IDs; alternative staffing/automation output; qualification and failed/censored trials with timestamps; whether A still produces when B is learned; demand order date and expiry; customer price/accepted output; invoice issuance and collection, refunds, actual vendor and financier cash draws, rights and collateral. A negative test is whether A service actually earns cash and does not tie up the training robot. If not, the financing bridge is invalid. A separate macro sector use/supply numeric backbone remains unresolved: do not infer these edges from BEA/IFR aggregate totals.

## 5. Reproduction and research continuation

Runnable source and tests are adjacent in calendar_model.mjs and test_calendar_model.mjs (15 deterministic assertions on exact-integral formulas, unconstrained adaptive RK4 and financeability probabilities; source-code mathematical functions were exercised in a V8 test harness). A richer independently tested Python/SciPy implementation with dated demand expiry, independent finite-step Bellman and quadrature baselines passed 19 scoped tests in the accompanying local research archive. No full historical CI, peer review, commercial calibration or customer panel was performed. All numerical illustrations are **synthetic normalized units**.

**Next question in this SAME investigation:** Solve the next finite-horizon control with stochastic A success, explicit invoice lag, provider/supplier cash balances and a *contingent*, commercially viable pilot/receivable-finance alternative; ask whether the calendar policy reversal survives realistic liquidity and customers' demand selection. Connect to production capacity/learning rights instead of fabricating a new isolated threshold. The Nov22 integrated Models A–B review, Nov29 empirical backbone, Dec6 contribution decision and full Dec25 package remain open.
