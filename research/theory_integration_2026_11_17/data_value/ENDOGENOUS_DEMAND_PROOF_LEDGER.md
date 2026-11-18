# Proof and claim ledger — endogenous demand with persistent transfer

**November 18, 2026; conditional research, integrated with prior data-value and qualified-production theory.** Main chapter: [ENDOGENOUS_DEMAND_PERSISTENT_TRANSFER.md](ENDOGENOUS_DEMAND_PERSISTENT_TRANSFER.md).

| Claim | Logical status | Assumptions necessary | What would defeat an extrapolation |
| --- | --- | --- | --- |
| ED1 full-history robust endpoint formula | Exact algebra, not novel | Single initial Bernoulli latent regime, interval prior, conditional complete kernels fixed, same physical worlds and pathwise safe policies | Unknown regime-specific kernels/feedback, endogenous prior selection, invalid safe action, nonaffine ambiguity set |
| Full-route 14/3, 7/10, 7.5/7.5, 6/6 | Constructed valid example, **not empirical** | Each first/terminal flow captures one period exactly, approved operator max 2, complete held-out B service, R/L uses S fallback | Route-specific customer margins not observed, missing order denominator, operator tail exceeds cap |
| Best pure maximin G, but not robust pairwise G>R | Direct consequence of ED1 under the synthetic example | Risk criterion is ex-ante worst-prior value; routes fixed | Changing prior set, full-history conditional response or policy menu |
| ED2 3/14 R + 11/14 G has floor 8.5 and is optimal within stated mixed menu | Constructed primal feasible mix plus dual admissible prior p=1/2; elementary convexification | Ex-ante randomized/fractional allocation feasible with linear aggregate capture; no interference/pooled controller effects | Indivisible body, customer- or site-correlated regimes, investment indivisibilities, common operating constraints |
| ED4 nonrectangular gap .5 vs .25 | Exact 2-order/2-regime construction | One common uncertain prior, fair observed order independent of regime; genuine complete-law maximin | Rectangular priors intentionally admitted as nature's model, correlation of Y and theta |
| ED3 observationally identical R data, opposite G/E ranking | Constructive proof of no-identification under missing policy support | G/L never observed, no known bridge/structural restriction | Safe G/L randomization, valid simulation-to-field invariant, monotonicity/transport assumption with verified scope |
| Interval bound in main text | Conservative comparison bound, may not be sharp | Joint complete-law set consistent with coordinate intervals | Pairwise dependence can tighten considerably |
| Free optional old policy does not decrease optimized V | Existing menu monotonicity, **not negative-transfer assertion** | Same resources, rights, feasible alternatives, no mandatory training interference | Fixed forced retraining, curation cost, cannibalized compute/operator capacity |

## Finite full-history and economic accounting proof

Take a complete model \(m\), including policies' *potential* customer-order, acceptance and recovery kernels. For policy \(\pi\), define a random path output \(Y_\pi\) as the actual sum of nonoverlapping operating periods and investment costs; \(J(\pi;m)=\mathbb E_mY_\pi\). Under \(P(\theta=H)=p\), fixed conditional path kernels yield \(J(\pi;p)=p w_{\pi H}+(1-p)w_{\pi L}\). Subtract \(J(\sigma;p)\), **with the same p**, and minimize affine expression over [l,u]. If policies have distinct own next-order distributions, their conditional \(w\) differ, but affine mixing still holds because \(\theta\) is assigned once before actions.

In the example all 8 physical terminal paths require no more than 2 approved operator units. B is attempted only when the route's full qualification and safe support conditions are met; R/L instead serves an accepted existing S order. Terminal B values are not counted in the first-period contributions. This establishes internal *synthetic* physical and economic feasibility only, not safety certification or empirical customer acceptance.

At p=.4, R=7.4, G=8.8, E=7.5, S=6. At p=.6, R=9.6, G=8.2, E=7.5, S=6. The G-E paired minimum is min(8.8−7.5,8.2−7.5)=.7; the R-G difference spans [−1.4,+1.4]. The best pure worst-prior value is G's 8.2. For x=3/14, the R/G mixture yields 8.5 in each regime, and at allowed p=.5 no pure action yields greater than 8.5; hence max over all mixed actions min over priors equals 8.5 **within this route menu**.

For the independent fair next-order Y, the *joint* law requires the same p on both order branches: \(E=0.5p+0.5(1-p)=0.5\). Rectangular splicing takes p=.25 for Y=H and p=.75 for Y=L, giving 0.25; this violates the independence/coupling assumption. This example illustrates the difference between a rectangular relaxation and the intended complete-law state, not a flaw in Iyengar/Epstein–Schneider theories.

For the on-policy nonidentification argument, W+ and W− share identical R kernels, including routes' first deployment, report, safety and order histories, and unchanged E,S conditional payoffs. They differ only at the **never assigned** G/L terminal customer qualification/value, 11 vs 5. Thus the R likelihood is identical for every sample size and sampling function. G's robust floor is 8.2 in W+, 5.2 in W−, while E=7.5 in both. The contrasting rankings are not identifiable from R alone. No assumption of random outcomes under unsupported action is silently filled by weighting.

## Verification and limits

The companion script implements explicit pathwise budget/qualification consistency, complete-regime payoffs, prior endpoints, equalizing mixed allocation, an observationally indistinguishable alternate G/L world, and rectangular-splicing comparison. The saved result is from an executed JS model; separate standard-library fractions offer an independently formulated arithmetic check. **Numerical checks do not prove a general theorem**; conditional proofs are given above. No robot/customer field data, authorized intervention, complete CI, independent review, empirical transfer effect, industry quantitative backbone or novelty decision is established.

**Next exact proof gap:** replace fixed known conditional full-history kernels with an identified set of coupled transfer, order-response and recovery laws and determine what safe matched intervention most reduces the decision-relevant *paired* uncertainty. Avoid recasting all feedback as an exogenous target \(\mu\) or automatically introducing an adversary that changes persistent regimes after each report.
