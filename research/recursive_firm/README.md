# Recursive Firm Theory

**Canonical Paper 3.** Gate A: in progress; Gate B: pending independent hostile-referee pass; Gate C: pending. This manuscript distills the recursive branch into four analytical pillars and incorporates the later evidence-allocation and generalization syntheses. The [canon register](../portfolio/CANON.md) accounts for all 16 branch Markdown documents. Their immutable source versions and replication scripts remain supporting appendices, not parallel papers. No solver or new synthetic world was run for this consolidation.

## 1. The object: production of future means of production

A firm can use its current machines, workers, models, contracts and experiments to improve a future production method. A stronger form of recursion changes how it chooses and produces those future improvements. The empirical question is whether an inherited procedure helps a recipient produce another useful procedure, after holding its executor, information, resources and ordinary learning opportunities constant.

Let the firm's state contain usable physical capital K, retained execution policies, a joint belief over unresolved production causes, authorized evidence D, a procedure psi for choosing and evaluating investigations, customer obligations, dated cash B, and enforceable control and data-use rights. A policy chooses production, experiments, design, qualification, financing and organization subject to dated feasibility. An action can change service now, the evidence law, the future feasible menu and the cost of future investigation. Those transitions must be specified rather than hidden in an untyped scalar called intelligence.

A recursive capability can be technically feasible yet economically dormant. Its return can arrive after the relevant cohort expires, go to another claimant, require unavailable qualification capacity, duplicate an ordinary experiment, or cost more than its incremental continuation value. Holding rivals' policies and market primitives fixed, access to an additional optional procedure cannot lower the firm's optimized value when it adds no cost or obligation. Forced use, investment in producing the procedure and the choice of whether to use it are different comparisons.

The benchmark is a competent state-contingent organization. It can learn ordinarily, preserve old policies, use the same admissible evidence, buy equivalent external tests, wait and contract where feasible. Better optimization of an unchanged menu is not evidence that the firm has produced a better learning technology. A gain over a weak fixed schedule alone is insufficient.

## 2. P3.1 — Current investigation and successor-procedure production

### A portable successor-value restriction

Research program i resolves a current defect with probability p_i, produces incremental contribution G on success and costs k_i. Conditional on success, the firm can pay c_i to qualify a successor procedure. That qualification succeeds with probability e_i and gives the claimant next-period value S. With discount 0<beta<=1, optimal value is

$$W_i=p_iG-k_i+p_i[\beta e_iS-c_i]_+.$$

G is a payoff, not dated cash B. The positive part preserves the option to decline the successor investment. The target stake is fixed across programs in this restriction; with heterogeneous outcomes the decision must be made conditional on the realized information before averaging.

Suppose k and c are equal across two programs and successor qualification pays under both. Then

$$W_1-W_0=(p_1-p_0)(G-c)+\beta S(p_1e_1-p_0e_0).$$

If G>c, p_1>p_0 and p_1e_1<p_0e_0, the program with the higher current resolution rate loses when

$$S>\frac{(p_1-p_0)(G-c)}{\beta(p_0e_0-p_1e_1)},$$

within the region where both positive parts are active. Subtraction proves the statement. At the boundary or outside that region, use the original option values. This is a conditional ranking result, not a claim that every broader inquiry is better or that recursive improvement accelerates indefinitely.

The continuation S includes only incrementally captured value: fees, margin on genuinely additional equipment and the net value of otherwise unavailable returned evidence. Do not add the same recipient service again as a separate data premium. A recipient may adopt a method without buying another machine. Installed-base expansion requires the adoption, financing and capacity conditions to hold jointly.

[Source proof and complete synthetic restrictions](https://github.com/amarmurray/robotics-economics/blob/af1cabb95772524db1b34dda3b2667a54c203b43/research/recursive_firm/organizational_recursion/README.md#a-better-improver-for-which-generation).

### Three cohorts distinguish reuse from successor production

Assign source production histories independently. At a fresh second cohort, separately transfer the execution model and the procedure for choosing the next costly investigation. Include an ordinary team that receives the same raw records. Match rights, available tests, staff, budgets and baseline upgrades. Record the actual tests chosen, their cost and accepted service. Assigning both teams the same tests is a channel test: disappearance of the gain is consistent with test selection; survival of the gain points to another mechanism.

At a third independent cohort, preserve the first-generation procedure assignments and randomize passage of the incremental procedure produced in the second cohort. The interaction with the original history distinguishes successor production from repeatedly applying the first method. Charge successor production and validation, retain original assignment denominators, and include failures, abandoned installations and zero-success cohorts.

Transfer permission announced before the second cohort changes incentives to produce a successor. Random transfer after it finishes, under common ex ante incentives, measures what the resulting successor transmits. These are different estimands. Direct answers embedded in the carrier, better hardware, extra resources, admission selection and ordinary local specialization remain competing explanations. No such field estimate is claimed here.

### Economic RL: forecast, objective and claimant

Accepted-service MPK_r is a forecastable state-dependent physical response under a stated resource comparison. It is not automatically a reward in money units. A controller can use forecasts of marginal service, qualification, evidence arrival and cash timing to predict feasible action consequences; its reward must represent the selected claimant's dated economic objective and constraints. If a downstream payment already reflects a service improvement, adding a second success reward counts the gain twice.

Rewards based only on today's defect-resolution rate can choose the wrong program in the restriction above. Conversely, adding an arbitrary exploration bonus does not establish that a chosen experiment has positive economic value. Include the opportunity cost, the strongest ordinary alternative and any terminal value actually justified. The branch's trained-agent and symbolic comparisons retain their original finite-world limitations and empirical nulls. [Economic RL source appendix](https://github.com/amarmurray/robotics-economics/blob/af1cabb95772524db1b34dda3b2667a54c203b43/research/recursive_firm/economic_rl/README.md).

## 3. P3.2 — Production changes the speed and composition of evidence

### Deployment-time scaling differs from example-time scaling

Let donor error after n effective independent records be e_i(n)=a_i(n+b)^(-alpha_i), with a_i,b,alpha_i positive. Production offers v>0 opportunities per unit time. Informative admissible records arrive at rate q e_i(n)^gamma per opportunity, q>0 and gamma>=0. Demand, transfer and the observation rule are stable, and processing is slack. With n(0)=0, integration of the fluid arrival equation gives

$$(n+b)^{1+\alpha_i\gamma}=b^{1+\alpha_i\gamma}+(1+\alpha_i\gamma)vq a_i^\gamma t,$$

and therefore

$$e_i(t)\asymp t^{-\alpha_i/(1+\alpha_i\gamma)}.$$

The exponent is derived from the maintained learning and observation laws. It is not an estimate from deployments. Better operation can reduce the arrival of the very incidents that teach it. An independent, continuing positive rate of informative audits restores asymptotically linear record growth under the same stability and processing assumptions, although the crossover can fall beyond the machine's useful life.

A recipient j receiving z=tau n, with tau>0, from this donor, with its own example-time exponent alpha_j and no other evidence stream, has deployment-time exponent alpha_j/(1+alpha_i gamma). With finitely many substitutable independent donor streams and positive fixed weights, the fastest record-growth exponent governs their sum. If complete capability requires all complementary components, the slowest exponent governs their minimum. Duplicated observations, signed interference, changed tasks or binding update capacity require a different aggregation law.

[Scaling derivation and bounded simulations](https://github.com/amarmurray/robotics-economics/blob/af1cabb95772524db1b34dda3b2667a54c203b43/research/recursive_firm/learning_dynamics/README.md). The historical 48–72-shift studies and later panels illustrate specified laws; they are not additional propositions or empirical exponents.

### Source expansion can crowd out recipient learning

Consider a fluid window with source reliability p and chosen source workload x. A source attempt consumes h(p)=h_0+h_1(1-p) shared hours. After source work, remaining hours are R=H-h(p)x. Eligible incident review has capacity I=r(1-p)x. Allocate i<=I hours to incidents, a to independent reference work and y to other accepted service, with i+a+y<=R. Recipient evidence is m=g i+e a, with fixed g>e>0. Let the value of other service U(y) and optimized recipient continuation W(m) be increasing, twice continuously differentiable and strictly concave, with U''<0 and W''<0 in the maintained interior.

In the regime with exhaustive incidents i=I, positive reference work and positive other service,

$$y+m/e=E=R+(g/e-1)I,\qquad U'(y)=eW'(m).$$

Thus

$$\frac{dm^*}{dE}=\frac{eU''}{U''+e^2W''}>0,\qquad E'=R'+(g/e-1)I'.$$

R translates the legacy synthesis's resource-budget symbol B; it is hours, not cash. At fixed source workload,

$$\frac{\partial E}{\partial p}=x[h_1-(g/e-1)r].$$

Improved reliability can reduce recipient evidence if lost high-yield incident opportunities exceed the effective value of released time. This is not harmful transfer from an admitted sample. It is a change in the available and chosen evidence stream.

To endogenize source work, put k(p)=h_0+(h_1-(g/e-1)r)(1-p), so E=H-kx. Let source contribution be S(p,x)=(vp-c)x-dx^2/2, d>0, and let V(E) be optimized U+W. In a feasible mixed interior,

$$vp-c-dx=kV',\qquad
\frac{dx^*}{dp}=\frac{v-k'V'+kk'xV''}{d-k^2V''},\qquad
\frac{dE^*}{dp}=-k'x-k\frac{dx^*}{dp}.$$

The denominator is positive. Even when fixed workload would release effective evidence resources, profitable source expansion can absorb more than it releases. This is a policy-mediated crowdout. New market responses changing W, U, yields or prices add terms and are not signed by this derivative. Corners require the complete feasible frontier, not extrapolation of the interior formula.

The [full proof, corner frontier and saved numerical checks](../../papers/theory_week_20261125/EVIDENCE_REALLOCATION.md) remain a scoped appendix. It also identifies when a learning change alters the physical marginal product of a recipient machine and when demand, cash-time occupancy or commissioning instead blocks new installations. A competent organization with the same menu can implement this allocation; recursion requires production of an improved observation or decision technology, net of its cost.

## 4. P3.3 — What the records identify

### Transfer reliability can be confounded with measurement reliability

In the binary signed-edge restriction of the [generalization synthesis](../../papers/theory_week_20261125/LEARNING_GENERALIZATION_STRUCTURE.md), an observed one-off agreement depends on the product tau_e lambda_e: structural agreement times measurement reliability. An observed deterioration can come from weaker true transfer or noisier observation. More one-off comparisons at that same confounded measurement design need not distinguish them.

Repeated tests of the same stable pair, with independent identically distributed measurement errors, can separately constrain measurement reliability through repeat agreement. Sign normalization and nonzero reliability are required to recover a signed structural quantity; unstable pair truth, correlated errors or selected repeats invalidate the simple separation. Graph reach alone cannot establish successful reuse when link reliability is unidentified. Paid local validation or an equivalent outside test belongs in the decision menu.

This is different from P2.5's Gaussian nuisance-stripping portfolio. Paper 2 owns that design/manufacturing result; this paper owns the consequences of changing, discovering and identifying the transfer and observation technology. [P2 canonical argument](../../papers/autonomous_firm/The_Production_of_Capability.md#7-p25--complementary-diagnostics-carried-into-manufacturing-scale).

### Audit location depends on a joint law

Let U indicate a genuinely new source correction, T a favorable recipient-transfer regime, p=Pr(U), h=Pr(T), and j=Pr(U intersect T). In the scoped release problem, G is the benefit scale and c the commissioning cost. A correction has benefit G on U intersect T, harm G on U intersect not-T, and no benefit when redundant. A perfect source audit reveals U; a perfect recipient audit reveals T. Their optimized release values before audit fees are

$$V_0=[G(2j-p)-c]_+,\quad V_S=[G(2j-p)-pc]_+,\quad V_R=[Gj-hc]_+.$$

The source audit screens redundant commissioning; the recipient audit can screen a harmful release. Compare gains over V_0 net of each audit's actual fee and foregone service. Under independence j=ph, 0<p<1, c>0 and (1+p)/2<h<1, the source option becomes active first, while a sufficiently large stake favors the recipient audit. The crossing, once both options are active, is

$$G^*=\frac{c(h-p)}{p(1-h)}.$$

Knowing the two marginal rates does not establish independence. Feasible joint laws satisfy

$$\max(0,p+h-1)\le j\le\min(p,h).$$

For G>0, sharp bounds on V_R-V_S follow by evaluating those endpoints and the interior breakpoints j=hc/G and j=p(1+c/G)/2 that lie inside the interval. Between breakpoints the difference is affine; each admissible j corresponds to a feasible joint law. A small range of accurately measured marginal dashboards can therefore leave the optimal audit unidentified.

[Joint-law proof and complete decision tree](https://github.com/amarmurray/robotics-economics/blob/af1cabb95772524db1b34dda3b2667a54c203b43/research/recursive_firm/inquiry/audit_location/README.md). If harms, redundant-release payoffs or imperfect audits differ, rebuild the action values rather than reusing these expressions.

### Admission, settlement and observation are separate identification problems

An adaptive organization chooses what enters its records. More selected operating logs need not reveal failures outside its retained support. Preserve an independently assigned reference roster, original case denominators and admission/retention decisions. Aggregate settlement can also be invariant to permutations of hidden failures across stages: a total payment may reward successful production without diagnosing which part should change. Targeted operational variation can break that symmetry when the corresponding likelihood is specified.

These restrictions are kept in [reference coverage](https://github.com/amarmurray/robotics-economics/blob/af1cabb95772524db1b34dda3b2667a54c203b43/research/recursive_firm/reference_coverage/README.md) and [settlement learning](https://github.com/amarmurray/robotics-economics/blob/af1cabb95772524db1b34dda3b2667a54c203b43/research/recursive_firm/settlement_learning/README.md). Structural/noise confounding, an unknown novelty-transfer joint law, admission bias and aggregate-payment symmetry require different discriminating observations. The canon does not collapse them into a generic statement that more data is needed.

## 5. P3.4 — Integration can produce the means to outsource

### A portable specification is an output

An unresolved interface can support incumbent production while remaining difficult for a new supplier to diagnose and qualify. Portability means that an independent team can use a retained test, action specification and acceptance criterion on a fresh lot. Integration may improve the joint chance of obtaining the relevant case, accessing the layers required to test it and validating the resulting procedure. That ranking must be demonstrated against feasible partners; ownership itself imposes no probability ordering.

Let arrangement g have unresolved net flow pi_g(e) and probability r_g(e) of producing the portable interface next period under chosen effort e. Portability is persistent, the environment is stationary within each state, beta is in (0,1), and financing does not block a worthwhile switch. Mature partner production earns m_P>m_I. Entry into integration costs F and subsequent delegation costs D. Then

$$W_P=\frac{m_P}{1-\beta},\qquad W_I=\max\left\{\frac{m_I}{1-\beta},W_P-D\right\},$$

and the best stay-until-maturity value is

$$Q_g=\max_e\frac{\pi_g(e)+\beta r_g(e)W_g}{1-\beta[1-r_g(e)]}.$$

Starting with the partner, integration while unresolved is preferred if Q_I-F>Q_P. Delegation after portability is preferred if (m_P-m_I)/(1-beta)>D. Both can hold. The first organization helps produce a specification that makes a different organization economical later.

For a maintained zero-effort policy, an experiment costing k in current flow and raising portability probability by Delta r improves its value exactly when beta Delta r [W_g-Q_g(0)]>k. This follows by subtracting the stationary continuation values with their positive denominators. Changes in F, D, financing, authority or access alter the comparison. A reserved partner, joint lab, adapter or contingent contract can defeat the ownership ranking. The historical source explicitly contains such a defeating joint-lab example; it remains part of the boundary.

### A speed premium need not rise with the pace of change

Hold opportunities, captured payoff w and the two feasible arrangements fixed. Internal qualification takes d_I periods and the best partner d_P>d_I>0. The method survives each period with probability rho, independently until expiry. Put x=beta rho. A single payoff at qualification yields gross internal-speed premium

$$w(x^{d_I}-x^{d_P}).$$

Differentiation gives its interior maximum at

$$x^*=(d_I/d_P)^{1/(d_P-d_I)},$$

if this point lies in the attainable domain 0<=x<=beta. Very short lives can defeat both teams; sufficiently long lives allow the partner to catch up. Fixed overhead can consequently make integration optimal only in an intermediate region. Immediate internal action, faster external specialists, repeated payoff streams or additional options change the result. The maximum over endogenously changing arrangements need not inherit a single hump.

[Boundary proofs and competent alternatives](https://github.com/amarmurray/robotics-economics/blob/af1cabb95772524db1b34dda3b2667a54c203b43/research/recursive_firm/boundaries/README.md). Grossman–Hart ownership incentives are prior art; the candidate additional object is the endogenously produced portable interface and resulting transition in the economical boundary. Novelty is not yet cleared.

## 6. Globally responding policies and long-run evolution

For parameter vector theta, the relevant equilibrium object is a correspondence of complete strategies, continuation values and any endogenous prices, not one threshold attached to a frozen policy. A policy-region certificate must include every feasible deviation, all relevant off-path continuations, the information available at each decision and a declared continuation-selection rule when more than one equilibrium exists. Root profitability alone does not certify sequential rationality.

Fixed finite-horizon policy values can be affine in a common cost, as Appendix A.COST shows. On regular fixed-support branches of two-player matrix continuation games, rational payoff entries and nonsingular indifference systems give rational mixing and continuation values, including supports larger than two actions. More players, nonlinear/nonrational primitives, singular supports or degeneracy can require more general algebraic or implicit branch analysis. Denominator signs, nonnegative probabilities, inactive-action inequalities and support changes must be tracked. Nonlinearity is a structural possibility, not a computed global equilibrium surface for the current economy.

The preserved integrated game closes its specified product-market institution. Wages, compute prices, supplier capacity, financing and entry are not all endogenously closed. A new analytical proposition may isolate one response and state what remains fixed. The current charter prohibits reopening a market-closure combinatorial sweep as a discovery program. A finite verification run is allowed only after a named proposition and falsification question are recorded in [ORACLE_REQUESTS](../portfolio/ORACLE_REQUESTS.md).

Once a repeated economy is actually solved, distinguish a stationary equilibrium, a nonstationary equilibrium path, multiple equilibrium selections and a disequilibrium adjustment rule. A cycle can occur on an equilibrium path; a failed numerical search is not proof that equilibrium fails to exist. Stability of a policy iteration is not stability of the economy. Long-run distributions, bifurcations or hysteresis require an explicit state transition and a solved policy/selection mechanism. Those objects remain open here.

## Appendix A.COST — A common research cost across all dates

**Status:** analytical derivation for the previously proposed next step; no new solver invocation and no claim of novelty. This is a sensitivity restriction, not a global certificate for the cash-constrained economy.

Consider a finite-horizon extensive-form decision problem with perfect recall against fixed rival behavioral strategies. Histories, information, feasible actions and chance transitions are finite and independent of c on a stated interval. The objective is risk-neutral expected additive monetary payoff; nonlinear utility of terminal wealth is excluded. Terminal payoffs apart from the surcharge are fixed. A designated research attempt at date t adds cost c times n_t>=0, weighted by a stated nonnegative accounting weight d_t. With discounted dated cash-flow utility d_t=beta^t; with undiscounted terminal wealth and no cash carry d_t=1. Use the actual objective rather than inserting a new discount convention. Require uniform feasibility over the interval: either funding is slack throughout or the same complete strategies remain feasible for every c. In particular, changing c may not silently remove a cash-feasible action or change opponents' policy because they condition on a new cash state.

For any fixed complete contingent policy sigma, the induced distribution over histories is independent of c. Define its weighted expected research count

$$N_i^\sigma=\mathbb E_\sigma\left[\sum_{t=0}^{T}d_t n_{i,t}\right].$$

Linearity of expectation gives

$$V_i^\sigma(c)=V_i^\sigma(0)-cN_i^\sigma.$$

Write $A_\sigma=V_i^\sigma(0)$. Here V(0) is the algebraic intercept under the same history law; if zero lies outside the feasible comparison interval it is not a claim that the strategy is economically feasible at zero. For an alternative complete continuation tau against those fixed rivals,

$$\Delta_{\sigma,\tau}(c)=\Delta_{\sigma,\tau}(0)-c(N_i^\sigma-N_i^\tau).$$

The same formula applies conditional on each decision history, with the same objective-consistent relative weights. It accounts for attempts at every later date, not just the immediate action. A policy involving fewer expected future attempts can gain relative value as the common surcharge increases even if the current actions have the same direct cost.

**Best-response envelope.** With finitely many pure contingent policies and the stated expected additive monetary objective, an optimal response can be chosen pure. Its value is the maximum of finitely many affine functions with nonpositive slopes. It is therefore continuous, nonincreasing, convex and piecewise linear in c on the common-feasibility interval. Its slope on a unique-policy segment is minus that policy's weighted expected attempt count. At a kink, several policies can tie; a derivative need not exist.

**Global policy regions and total attempts.** A complete policy sigma is optimal exactly on

$$\mathcal C_\sigma=I\cap\bigcap_\tau\{c:A_\sigma-A_\tau-c(N_\sigma-N_\tau)\ge0\}.$$

This is an interval, possibly empty or a singleton. A two-policy equality is an actual boundary only if no other complete policy dominates there. If c_1<c_2 and sigma_1,sigma_2 are optimal at those costs, adding their two optimality inequalities gives (c_2-c_1)(N_1-N_2)>=0. Optimal expected weighted total research therefore weakly decreases. Current research need not decrease: an early informative attempt can replace several later attempts. The claim is about the complete contingent policy, not each date separately.

**Fixed-mixing restriction.** At an observed decision history in a perfect-monitoring game, keep rivals' and later continuation probabilities fixed. A private-information extension would also have to hold the relevant beliefs fixed and specify the equilibrium concept. Suppose two actions receive positive probability in the same fixed behavioral profile over an open interval of c. Sequential optimality requires their action values to agree throughout that interval. Two affine functions agree on an open interval only if both intercepts and slopes agree. Thus the supported actions must have equal baseline continuation value and equal conditional expected weighted remaining research counts. Equality of the immediate attempt count alone is insufficient. A single-action support imposes no such indifference restriction.

This condition is necessary, not sufficient: inactive actions can dominate, support feasibility can fail, or another history can violate incentives. It does not constrain an equilibrium whose probabilities change with c to keep actions indifferent. Reoptimized rivals, state-contingent responses to cash, endogenous entry, prices, transfers or the learning technology can all break the fixed-history-law comparison and the convex-envelope conclusion for equilibrium payoffs.

**Fixed-profile equilibrium certificate.** In a finite perfect-monitoring game with simultaneous moves allowed at a date, fix a complete behavioral profile sigma at every history, including off-path histories. The profile's parameter region is

$$\mathcal E_\sigma=I\cap\bigcap_{i,h,a}\{c:A_i^\sigma(h)-A_i^\sigma(h,a)-c[N_i^\sigma(h)-N_i^\sigma(h,a)]\ge0\}.$$

Here A_i^sigma(h) and N_i^sigma(h) are the conditional intercept and weighted count under the full profile. A_i^sigma(h,a) and N_i^sigma(h,a) are the corresponding quantities for action a as a unilateral one-shot deviation, averaging over rivals' current actions and then following the fixed continuation. All feasible histories, including those assigned zero probability by the profile, are checked. Backward induction makes all-history one-shot checks sufficient for subgame perfection under these assumptions. The region is an interval, possibly empty or a singleton. A vector of additive research and hardware charges gives half-space intersections and a convex polyhedral best-response value when it preserves the common feasible tree. Private information requires an explicit equilibrium concept, information sets and beliefs; public-state checks alone do not certify sequential equilibrium.

**Analytical counterexample to equilibrium-payoff monotonicity.** To falsify the stronger claim that a common cost must lower every firm's equilibrium profit, consider this one-stage research/entry game. E incurs the common surcharge c; O stays out. These are constructed payoff units, not industrial observations.

| | Firm 2: E | Firm 2: O |
| --- | --- | --- |
| Firm 1: E | (5-c, 1-c) | (10-c, 0) |
| Firm 1: O | (0, 3-c) | (0, 0) |

For 0<c<1 the unique equilibrium is (E,E); for 1<c<3 it is (E,O). Firm 1's strict dominance of E on this range and firm 2's best response prove both statements directly. Firm 1's equilibrium payoff jumps from the branch 5-c to 10-c when the rival withdraws. No numerical sweep is needed. The fixed-rival envelope theorem remains valid; the equilibrium comparison changes the rival's policy. Mixed probabilities can likewise adjust over an open cost interval while the support stays unchanged.

**What remains uncomputed:** the relevant continuation-count differences for the diagnosed intermediate subgames; any interval in which their fixed mixes satisfy the restriction; and the complete reoptimized equilibrium correspondence. These quantities are explicitly null in the portfolio state. Before any targeted verification, identify the owning proposition, exact history and the smallest falsifying comparison. Do not restart the exhaustive queue to fill them.

## 7. Claim status, source preservation and next gate

The four pillars are portable conditional mechanisms, with source proofs and counterexamples retained. They do not establish a measured firm-level recursive multiplier, universal recursive advantage, a fully closed repeated economy or an equilibrium phase diagram. The [single positioning matrix](../portfolio/CANON.md#unified-prior-art-positioning) governs comparisons against Data-Driven Automation, Organizing Intelligence, Grossman–Hart and Cabral–Riordan. Ordinary dynamic programming, value of information, learning-by-doing and incomplete contracting are prior art.

The branch root and all modules are pinned at [af1cabb95772524db1b34dda3b2667a54c203b43](https://github.com/amarmurray/robotics-economics/tree/af1cabb95772524db1b34dda3b2667a54c203b43/research/recursive_firm). The former main [recursive-firm note](../theory/recursive_firm.md) retains nonredundant common-versus-contrast filtering and paid-report/calibrated-authority arguments as a scoped appendix. The source's simulator plans, negative ordinary-planner comparisons, unexecuted live-world fields and empirical nulls remain unchanged. Existing simulation counts are provenance, not milestones.

Gate A still requires proof and notation reconciliation, a complete claim-to-script mapping and explicit disposition of every inherited qualification. Gate B must then challenge the four pillars against competent outside alternatives, observable information and the closest prior mechanisms. Gate C needs actual state-variable mapping; the preliminary [Symbotic packet](../portfolio/empirical_target_symbotic.json) can inform rights and timing, but does not demonstrate successor-procedure production. A third-cohort observational or experimental design remains an empirical research target.
