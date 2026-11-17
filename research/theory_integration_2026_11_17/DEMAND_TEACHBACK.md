# Teach-back: qualified output, demand, and the research/production frontier
*Private problem set · 17 November 2026 · Solutions in DEMAND_SOLUTIONS.md*

The economic environment is defined in DEMAND_CONTRACT_THEORY.md and the no-dependency model demand_learning.py. All illustrative parameters are hypothetical. Work out each algebraic answer before running the code.

1. **Endogenous accepted service.** A buyer's incremental value relative to an available human alternative is Dq-beta*q²/2. A provider captures kappa of this value and incurs cost sq. A qualified platform has capacity K(1-delta*u). Derive optimal accepted output q(u) as a function of D,beta,kappa,s,K,delta,u. State exactly when q(u) equals capacity.

2. **Discounted learning versus production.** B qualification arrives at hazard lambda*u; after success the portfolio earns W per unit time forever. Discount is rho and learning costs c*u while underway. Derive the stationary Bellman equation, show why the value for each fixed u is a ratio, and prove the sign of its derivative in the capacity-constrained case. Is an interior effort choice possible even with a linear acquisition hazard?

3. **Economic demand feedback.** Hold Delta=W-g0 fixed as A willingness to pay m changes. Show that the opportunity-cost premium from acquiring B on the incumbent capacity falls with m when delta>0, even though B's technical hazard and incremental cash reward are fixed. Why does an independent specialist comparator not share this particular effect?

4. **A hard SLA and a priced violation.** Take K=1, m=d=4, eta=0, rho=1, lambda=2, W=4, c=1; a specialist has mu=1 and c_sp=6/5. Solve the optimal shared policy with no SLA and then with the A-output requirement q>=.9. In a separate contract, let the same .9 threshold be violable at ongoing penalty p>0: derive the breach-region derivative and explain why increasing p can accelerate the *conditional* learning policy but reduce net value.

5. **Endogenous production-financed learning.** Let accepted A receipts net of operating cost be g(u)=g0-Lu-hu², mature after fixed delay d_cash, and cost c*u for B effort. Derive the long-run cash-sustainable effort bound from a cash-stock inequality and Jensen. Is a finite loan sufficient to raise that bound permanently? What changes under enforceable minimum customer service?

6. **Discriminating data design.** Using the dated DHL/Stretch and GXO/Digit source descriptions, specify three measurements that would identify a production-resource displacement effect versus (i) pricing, (ii) an unobserved customer-order-completion effect, and (iii) shifting human supervision. Which public source fact *does not* identify any of those effects?
