# When capabilities become production: demand curvature, contractual acceptance, and the opportunity cost of qualification
*Integrated theory continuation · 17 November 2026 · private manuscript addendum*

## Research question and relation to earlier results

Results 8–9 established that a qualified intermediate service can produce receipts during continued learning, but used a constant accepted-A cash rate and mostly compared financing feasibility or qualification probabilities. That does not yet select the provider's **net-value-maximizing** strategy when the customer can change quantity and has a credible specialist alternative. This continuation endogenizes accepted output, retains a B qualification hazard and working-capital channel, and compares a **qualified shared-asset learning policy** with a real alternative that preserves A throughput. It is not a separate Q-number paper. All numerical examples are synthetic normalized units.

### Economy, source of receipts, and acceptance

The customer has a feasible human/specialist outside process. Relative to that alternative, accepted complete-service quantity q creates incremental gross customer value Dq - beta*q^2/2. A contractual surplus-sharing rule assigns fraction kappa in (0,1] of this value to the deployer, who bears per-order resource cost s. The deployer's **earned net contribution** is

    pi(q) = m*q - d*q^2/2,     m = kappa*D-s,     d = kappa*beta>0.

The buyer retains the residual value and can decline non-accepted work. This is an explicit hypothetical contracting mechanism, not an estimate of an actual hourly RaaS price. If payments are delayed, pi is an earned claim and must be passed through the separate cash-state model in Result 9; the discounted choice below initially assumes prompt, enforceable collections.

A is a qualified complete customer service with capacity K, rather than a robot motion benchmark. Training to add qualified B uses an effort share u in [0,1], reduces contemporaneous available A production to K[1-(1-eta)u], costs c*u per unit time, and produces a retained B qualification event with hazard lambda*u. The qualified AB portfolio earns net flow W after success, including all A/B allocations and obligations: **do not add A receipts to W again**. A competent independent specialist-development alternative keeps A's existing production, qualifies the same AB opportunity at hazard mu while incurring ongoing cost c_sp. Both routes face identical downstream customer acceptance and have the same post-success W. Fixed development-hardware rentals are absorbed in c_sp. There is no assumed free supplier loan, confidential site data or new demand from a robot cycle.

For this theorem take m>=dK (A production is at least weakly capacity constrained before training) and eta in [0,1]. With delta=1-eta, the optimal accepted A quantity conditional on u is q(u)=K(1-delta*u); no unserved order is counted. Thus

    g(u) = pi(q(u)) = g0 - L*u - h*u^2,
    g0=m*K-d*K^2/2,
    L=K*delta*(m-d*K)>=0, h=d*K^2*delta^2/2>=0.                 (D1)

An enforceable A service floor q_min restricts u<=u_max=min{1,(1-q_min/K)/delta} when delta>0, with u_max=1 when delta=0. This is a *hard* contractual constraint; the below-the-floor penalty variant is treated separately.

## Proposition D1: optimal learning intensity with endogenous A demand

With discount rate rho>0, qualifying hazard lambda*u, continuing A flow g(u), learning operating cost c*u and postqualification value W/rho, the best prequalification provider value is

    V_shared = max_{0<=u<=u_max} [g(u)-c*u+lambda*u*W/rho] / [rho+lambda*u].  (D2)

This is the value of an optimal **adaptive** stationary policy before success, not merely a comparison of arbitrary committed routes. Its Bellman equation is rho*V=max_u {g(u)-c*u+lambda*u*(W/rho-V)}. There is no new information before the successful qualification event in this deliberately limited stationary Markov economy, so a maximizing stationary intensity satisfies verification. The zero-effort baseline is g0/rho.

Put A=lambda*(W-g0)-rho*(c+L). For h>0, the derivative of (D2) has the sign of

    A - 2*rho*h*u - lambda*h*u^2.                                  (D3)

This expression is decreasing in u. Therefore, when A<=0, u*=0; when A>=2*rho*h*u_max+lambda*h*u_max^2, u*=u_max; otherwise the unique interior optimum is

    u* = [sqrt(rho^2+lambda*A/h)-rho]/lambda.                      (D4)

For h=0, compare the two endpoints because the objective is fractional linear. This proves a global optimum under the stated concave output and independent exponential-qualification environment. Unlike the constant-receipt/linear lost-throughput benchmark, an interior intensity can be strictly preferable to both stopping and nonstop training. No numerical solver or conjectured switching date is needed for this result.

A competitor preserving A output has value

    V_specialist=max{g0/rho,[g0-c_sp+mu*W/rho]/[rho+mu]}.           (D5)

This compares two competent accepted-service policies on equivalent postqualification service and does **not** give the specialist a fictitious zero-cost training program.

## Proposition D2: increasing incumbent demand can discourage learning on incumbent hardware

Hold fixed K,d,delta>0,rho,c,lambda,mu,c_sp, the qualification technologies, and the **incremental** net cash flow Delta=W-g0>0 unlocked after B succeeds. As customer willingness to pay for A increases m while m>=dK, assume W(m)=g0(m)+Delta. For a given shared effort u, subtracting the optimal no-learning A value yields

    V_shared(u;m) - g0(m)/rho
      = u * [lambda*Delta/rho-c-L(m)-h*u] / [rho+lambda*u].        (D6)

The derivative with respect to m for any fixed u>0 is

    d/dm [V_shared(u;m)-g0(m)/rho]
      = -K*delta*u/(rho+lambda*u) < 0.                             (D7)

The maximized shared learning *premium* is therefore weakly decreasing in m, strictly while a positive unique optimum remains. In contrast the specialist's learning premium, above no learning, is

    max{0,[mu*Delta/rho-c_sp]/[rho+mu]},                           (D8)

independent of m under this matched-Delta experiment. A rise in demand for an already-qualified service may therefore **reverse the preferred qualification organization even though the technical hazards and B's incremental net contribution remain unchanged**. Intuition: A's more valuable output raises the opportunity cost of occupying the incumbent robot, but not the specialist's cost. The result is conditional on a *fixed incremental target opportunity*. If higher A demand also changes Delta, learning rates, supplier costs, demand covariance or future capacity, the ranking requires re-solving. This is ordinary constrained production/revenue management economics applied to the capability sequence, not an established original general theorem.

### Exact falsifying benchmark and capable alternatives

Take K=1, d=4, eta=0, rho=1, lambda=2, c=1, mu=1, c_sp=6/5, Delta=2. These are hypothetical and deliberately allow an independent paid specialist option.

| Accepted A marginal intercept m | Shared training u* | Shared total V | Specialist total V | Winner |
|---|---:|---:|---:|---|
| 4, W=4 | 1/2 | 5/2=2.5 | 12/5=2.4 | Shared learning |
| 6, W=6 | (sqrt(2)-1)/2 ≈ 0.207107 | 9/2-(sqrt(2)-1) ≈ 4.085786 | 22/5=4.4 | Specialist |

For m in [4,7] the shared learning optimum remains interior until it reaches zero, and the ranking switches at m*=31/5-4*sqrt(5)/5 ≈ 4.41115. This threshold is a *property of the synthetic matched-increment experiment*, not estimated market demand or a publication novelty claim.

An important stronger objection survives the comparison: a specialist may also require scarce shared supervisors, manufacturing capacity or customer integration; then its A flow is not g0, and D5 must instead solve the same common production resource program. Conversely, generalist hardware may reassign work with low switching costs, invalidating a fixed A-to-B shadow price. Neither variant can be dismissed from product marketing claims.

## Proposition D3: the customer contract can remove a theoretically attractive learning policy

If acceptance requires q>=q_min during development, u_max falls as q_min rises. Feasible-set inclusion makes V_shared weakly decreasing, while a truly separate specialist's value is unaffected in this baseline. With m=4 and q_min=.9, u_max=.1, so V_shared=67/30 ≈2.233333 and the specialist wins at 2.4; the shared policy had won 2.5 versus 2.4 without the floor.

A *soft* alternative charges the provider p per unit time while accepted q is below the SLA floor q_sla, until B is qualified. The penalized objective in that region subtracts p from the numerator in D2. Its derivative-sign expression becomes A+lambda*p-2*rho*h*u-lambda*h*u^2. **Conditional on operating in the breach region**, higher p can cause faster learning to terminate the costly breach sooner—even though the provider's optimized value falls and may switch entirely to the no-breach or specialist option. The explicit finite-penalty test with q_sla=.9 finds shared learning above the specialist at p=.1 and below it at p=.25. This is not a finding about actual SLA language; if pausing development loses progress or triggers a one-time penalty, a different state/timing model is required.

## Proposition D4: endogenous output changes the long-run cash-sustainable learning share

Connect (D1) to Result 9's *actual dated collections*, not to the unconstrained discounted value. With up-front cash K0>=0, fixed collection delay d_cash>=0, independent accepted A production during B development subject to the modeled capacity tradeoff, and cash cost c*u, the no-success path obeys

    C(t)=K0 - c*int_0^t u(z)dz
           + int_0^(t-d_cash)_+ g(u(z))dz >= 0.                    (D9)

Assume accepted net flow g(u)>=0, divisible production/effort, a stationary willing buyer, costless pause/resume with retained progress, and that the service-floor bound u<=u_max applies at all dates. The supremum long-run fraction of learning effort is

    x*=max{u in [0,u_max]: c*u <= g(u)}.                            (D10)

For (D1), if h>0 the positive boundary root is

    x0 = 2*g0 / [(L+c)+sqrt((L+c)^2+4*h*g0)],
    x*=min(u_max,x0).                                              (D11)

With h=0 the root is g0/(L+c). **Upper-bound proof:** nonnegative terminal cash and Jensen's inequality for concave g give c*E(t)<=K0+(t-d_cash)g(E(t-d_cash)/(t-d_cash)); bounded u means the two average efforts have the same subsequential limits as t grows, hence c*x<=g(x). **Construction:** first operate A without training until the invoice lag matures, then adopt stationary u=x; because g(0)>=g(x)>=c*x, the initial receipts cover development until the lagged receipts from the new output mix arrive. Thus the limit is attainable. A finite initial credit line or any fixed finite collection delay cannot raise the sustainable *asymptotic* effort fraction in this contract class.

For m=4 the share is (sqrt(17)-1)/4 ≈ .780776. Simply replacing endogenous accepted revenue by 2(1-u) would instead give 2/3, which is a materially different resource/accounting assumption. Neither is an observed robot qualification rate or an optimal discounted investment policy. The cash-feasible effort upper bound is only an additional constraint; it is not automatically the answer to the finite-horizon, delayed-cash Bellman problem. With q_min=.9, the hard accepted-service floor instead limits learning to .1 even if cash could pay for more. A lender can relieve cash shortage but cannot make breaching the customer acceptance obligation productive without renegotiation.

## Source evidence and identification boundary

* **DHL / Boston Dynamics:** DHL's January 31, 2023 statement records commercial Stretch trailer/carton unloading and integration with a conveyor. Its May 13, 2025 MOU describes expanded deployment and *future* case-picking work, reporting unloading rates up to 700 cases/hour. These are distinct accepted-service states, not a matched experiment measuring the cost of training on the same deployed hardware, a downstream SLA, or site receipts. Sources: https://www.dhl.com/us-en/home/press/press-archive/2023/dhl-supply-chain-achieves-first-commercial-deployment-of-boston-dynamics-stretch-robot.html ; https://group.dhl.com/en/media-relations/press-releases/2025/dhl-group-signs-mou-with-boston-dynamics-and-accelerates-cross-business-automation-strategy.html .
* **GXO / Agility:** GXO's June 27, 2024 multi-year RaaS agreement followed a pilot; its October 26, 2026 partnership expansion reported 100,000+ totes moved at one site and future 2027 deployments to new sites. Those observations distinguish commercial deployment from announced expansion, but do not give demand curves, net collections, qualified complete-order acceptance or incumbent-output displacement during development. Sources: https://gxo.com/news_article/gxo-signs-industry-first-multi-year-agreement-with-agility-robotics/ ; https://investors.gxo.com/news-releases/news-release-details/gxo-and-agility-robotics-expand-partnership-accelerate .
* **Formic:** its February 2024 webinar materials describe a productive-hours billing model with guaranteed performance. This documents an alternative to the model's share-of-surplus pricing; it does not identify the share kappa or a customer SLA floor/penalty used here. Source: https://land.formic.co/formic-webinar-feb-2024 .

**Closest prior art:** joint demand/capacity decisions and production pricing are long established (Deng and Yano, *Management Science* 2006, DOI 10.1287/mnsc.1050.0491; Maglaras and Meissner, *M&SOM* 2006, DOI 10.1287/msom.1060.0105). Chen, Jasin and Duenyas (*Operations Research*, online 2021, DOI 10.1287/opre.2020.2078) analyze joint learning and pricing under network capacity and unknown demand. Our present model assumes the **demand curve is known** and the uncertainty concerns persistent qualification. These are related but not equivalent problems; abstracts and publisher descriptions were reviewed, not all source proofs. No scientific priority or empirical novelty is asserted.

**Falsifiable panel:** At one customer/site, capture qualified complete-order A acceptance and incremental value relative to a real alternative, order-level willingness to pay and demand/cancellation curve, dated development effort and output *simultaneously*, supervisor/robot capacity, retained version/qualification events, A service-floor and penalty clauses, specialist workcell alternative and actual invoices, credits and **banked receipt dates**. Compare A volume when the same physical robot is diverted for development versus qualified development on independent equipment, holding demand and order mix fixed. Negative control: when A demand is below capacity so q*=m/d<K, small training effort need not reduce A output; D1's positive lost-sales slope is invalid until physical slack is exhausted. Another negative control: if the supposed separate specialist uses the same shared human safety/verification resource, its modeled independence is false. The public examples above lack this joint panel and cannot estimate our m,d,h,lambda or fees.

## Checks, paper integration and next step

The companion Python standard-library core implements D1–D11 and a piecewise soft-SLA check; 19 local scoped tests cover exact values, conditional analytical optima, global dense-grid lower bounds, a separate small-step stochastic Bellman discretization and cash/SLA inequalities. A test grid is not a proof or real-world calibration. The historical repository suite and independent review remain unrun. Preserve the complete first-paper synthesis and empirics/atlas obligations.

**Next exact question:** replace perfect, immediate collections in D2 with the dated cash path D9 *and* contractual accepted-order floors when cash is initially limited; derive a finite-horizon optimal stopping/learning policy against an independent specialist with the same safety, retention, demand and financing rights. Test if demand-induced option reversal survives when increasing A sales also expands financeability. The answer may reject the simple monotone policy, and that negative result should be retained.
