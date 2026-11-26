# Globally reoptimized equilibrium thresholds

*November 26, 2026. Input accepted main: `4f3290f668664ce940b497c0cfcb269223cd685f`. Research direction: Amar's request to seek globally reoptimized equilibrium thresholds, including the possibility of nonstationarity and nonlinear dynamics. Synthetic theory and exact finite-game computations; no empirical calibration.*

## 1. The question changes from a program crossing to an equilibrium region

The economically relevant threshold is where a firm changes its best feasible contingent policy after accounting for the other firms' best responses. Its alternatives include ordinary learning, outside qualification, different service recipes, hardware investment, retaining or discarding evidence, opening or closing its lab, and postponement. A comparison of two frozen programs can explain a mechanism. It cannot, by itself, establish where an equilibrium changes.

The accepted [concurrent manufacturing result](CONCURRENT_WINDOW.md) makes this boundary explicit. Its fixed-program private increment is

\[
g(S)=-17+\frac{33}{16}S,
\]

where S is the number of later service opportunities. The first positive integer is nine. That calculation holds the two contingent programs and their later quantities/prices fixed. The accompanying competitive solver establishes particular equilibria at particular parameter values, but the break-even formula is not a globally reoptimized equilibrium threshold.

This extension makes equilibrium thresholds the organizing target, begins mapping them using the existing technology, and states what a complete parameter-region certificate would require. It does not replace a solved finite economy with a general Bellman equation and call the larger problem solved.

### A result already changes the interpretation

Along an explicit balanced service calendar, globally checked firm best responses give no selected learning through eight later shifts, asymmetric learning at nine, and bilateral learning at ten. At nine there are two pure root equilibria and a separately certified symmetric mixed root equilibrium. The source of the asymmetric region is temporary relief from product-market competition when a rival gives up current service to learn. It does not require access to the rival's proprietary data.

These are exact results of the finite legal-action game under the stated pure continuation selections. They are not an enumeration of every possible dynamic equilibrium or a continuous threshold certificate.

## 2. What must be optimized and what must be mutually consistent

Let the joint state z contain installed robots and inventories, model qualifications, retained evidence and reuse rights, research procedures, lab scope, cash, customer commitments, and information about uncertain transfer. An enlarged model can add supplier capacities, different skills, debt, and other firms' states. State variables must enter a payoff, transition, information set, or feasibility constraint; naming them is not an economic mechanism.

Let a firm choose a dated action vector covering service, human work, inference and copies, retention, learning, procedure improvement, manufacturing, procurement, and scope. Let theta denote primitives such as service windows, demand, learning probabilities, compatibility, input supply, and rights. A policy specifies actions at every admissible state and date, including states that are not reached on the selected path.

The equilibrium requirement is

\[
\sigma_i^*\in\arg\max_{\sigma_i\in\Sigma_i}
J_i(\sigma_i,\sigma_{-i}^*;z,\theta)
\quad\text{for every firm and subgame}.
\]

The maximization is over all feasible own policies. There is generally no common objective whose global maximum produces this equilibrium. Maximizing the sum of firm payoffs is a separate planner problem, or an explicitly stated rule for choosing among equilibria already verified to satisfy individual incentives.

In a unilateral deviation, the other firms' policies are held fixed. Their future actions can nevertheless change when the deviation changes the public state: that response is already specified by their contingent policies. Replacing the whole current equilibrium inside a simultaneous unilateral deviation would be a different experiment. If a first-stage commitment is followed by a quantity game, the deviator correctly anticipates the equilibrium of the resulting downstream subgame, under an explicit continuation selection.

The current economy endogenizes product-market quantities and prices. Wages, compute prices, entry, and supplier capacity are not all market-clearing outcomes. Its equilibria are dynamic industry-game equilibria in a restricted economy, not an unrestricted general equilibrium.

### The threshold is usually a surface

Partition current legal choices into regimes r, for example current investment in a successor, ordinary qualification, or postponement. Define

\[
Q_{ir}(z;\theta,\sigma^*,V_i^*)
=\max_{a_i\in\mathcal A_{ir}(z;\theta)}
\left\{\pi_i(z,a_i,\sigma_{-i}^*;\theta)
+\beta\mathbb E[V_i^*(z')\mid z,a_i,\sigma_{-i}^*]\right\}.
\]

Switching costs and resource commitments belong in pi or the transition, counted once. Continuation value allows future regime changes. Comparing adoption now with a comparator forbidden ever to adopt would answer a different question.

On an equilibrium branch, a regime boundary satisfies

\[
\Gamma_{irs}=\{(z,\theta):Q_{ir}=Q_{is}=\max_\ell Q_{i\ell}\}.
\]

Learning probabilities, capital, demand, finance, timing, and rights generally make this a multidimensional surface. One scalar threshold needs monotonicity or single-crossing conditions. Without them, several switches, disconnected adoption regions, and multiplicity are legitimate outcomes.

For an equilibrium correspondence E(theta), separate the set of parameters at which **some** equilibrium includes a given adoption pattern from the set at which **every** equilibrium does. A single selection rule cannot establish the second claim.

## 3. A constructive exact theorem for threshold regions

Consider a finite-horizon stochastic game with finite state and action sets. On a primitive parameter domain, assume legal menus and transition probabilities are parameter independent, and stage rewards and terminal values are affine in theta. Fix a complete pure Markov policy profile sigma, including off-path subgames.

**Proposition.** Its values are affine in theta. The parameter set on which it is a Markov-perfect equilibrium is the intersection of its one-shot incentive half-spaces. It is a convex polyhedron; with one scalar parameter it is an interval, possibly empty or a singleton.

**Proof.** Terminal values are affine. Backward induction preserves affinity because each chosen action has affine reward and the probabilities multiplying next-period affine values do not depend on theta. Hence

\[
V_i^\sigma(t,z;\theta)=A_i^\sigma(t,z)+B_i^\sigma(t,z)^\top\theta.
\]

For each firm, date, state and legal alternative a_i, form the incentive slack

\[
D_{i,t,z,a_i}^\sigma(\theta)=V_i^\sigma(t,z;\theta)
-\left[\pi_i(z,a_i,\sigma_{-i};\theta)
+\beta\sum_{z'}P(z'\mid z,a_i,\sigma_{-i})V_i^\sigma(t+1,z';\theta)\right].
\]

Every slack is affine, d+e' theta. The profile's equilibrium region is

\[
E_\sigma=\bigcap_{i,t,z,a_i}\{\theta:D_{i,t,z,a_i}^\sigma(\theta)\ge0\}.
\]

All one-shot deviations being unprofitable at all subgames rules out any profitable finite sequence of deviations, by backward induction. This establishes global unilateral optimality within the finite policy set, rather than only a local first-order condition. With rational primitives, the boundaries can be represented exactly. QED.

### Why this is stronger than a dense grid

An implementation can attach each boundary to the deviation that becomes profitable, identify whether the decisive deviation occurs now or in an off-path continuation, and certify the entire interval between boundaries. A dense grid gives samples; it does not prove that no other branch lies between them.

The current extension supplies integer solves and the theorem. It has **not yet implemented interval-wide certificates for all complete policy profiles**. Source-dependent legal menus must retain all relevant alternatives when extending a pointwise dominance reduction to an interval. An action that is cheapest among transition-equivalent actions at one parameter can cease to be cheapest elsewhere.

If a parameter changes transition probabilities, products of probabilities can make values nonlinear. If it changes feasibility or state definitions, first partition the domain into valid regions. Integer service blocks should not silently become a continuous physical horizon. The balanced calendar below uses floor/ceiling explicitly; the analytic diagnostic is a separate continuous relaxation conditional on fixed programs.

### An equilibrium region differs from a selected region

A selector that chooses the highest-total-payoff pure equilibrium must first establish which candidates are equilibria. A profile can be selected, displaced while another equilibrium exists, then selected again. Its selected region can therefore be disconnected even when its own incentive region is an interval.

An exact two-action counterexample for theta >= 0 is

|  | Rival A | Rival B |
| --- | --- | --- |
| Own A | (0, 0) | (3-theta, -1) |
| Own B | (-1, theta) | (2, 2) |

AA is an equilibrium for every theta; BB is an equilibrium exactly on [1,2]; neither off-diagonal profile is an equilibrium. Selecting the pure equilibrium with highest total payoff chooses AA on [0,1) and (2,infinity), and BB on [1,2]. Track both incentive eligibility and ranking changes; selection inequalities are conditional on candidate eligibility.

## 4. The optimized value envelope is not an equilibrium payoff envelope

For fixed rival policies, own optimized value is an upper envelope of policy values. Under the finite affine assumptions it is convex and piecewise affine. A selected equilibrium payoff combines pieces that must satisfy everyone's incentives; it need not be convex, monotone, or continuous.

At a smooth own optimum, envelope reasoning removes the first-order derivative of the firm's own optimized choices. It does not remove the effect of changing equilibrium prices or rival policies. If

\[
W_r(\theta,e)=\max_x f_r(x;\theta,e),
\]

then along a smooth equilibrium environment e*(theta),

\[
\frac{dW_r}{d\theta}=W_{r,\theta}+W_{r,e}\frac{de^*}{d\theta}.
\]

Parameterized constraints require their Lagrangian terms; regime switches require finite comparisons or one-sided derivatives. Reoptimizing both the ordinary and recursive comparator weakly improves each conditional objective. It does not sign the change in their difference or guarantee that the adoption threshold falls. This is standard envelope reasoning, not a new theorem of robotics economics; [Milgrom and Segal (2002)](https://web.stanford.edu/~milgrom/publishedarticles/Envelope%20Theorems.pdf) provides the primary foundation.

## 5. First computation: an integer equilibrium transition with endogenous asymmetry

The code reuses the accepted service-window technology, staggered timing, and concurrent transition-class reduction without changing their primitives. Source SHA-256 checks bind all three antecedent files. The parameter path is

\[
\text{calendar}(S)=(1,1,\lfloor S/2\rfloor,\lceil S/2\rceil),\qquad S\ge2\text{ integer}.
\]

Physical service is available from the first date; digital admission is date three. Both firms start from procedure zero with an installed arm, sufficient cash of 10,000 each, and a mobile-kit price of four. An order and assembly take separate dates. Internal procedure development uses one compute slot with success mass (3+old)/4. Paid licenses and outside research remain available at the accepted costs. The simultaneous-investment regime permits one research and one construction action while preserving shared human and compute constraints. In the exclusive comparison they compete for one investment slot.

The solver enumerates best responses over the retained feasible menus, uses exact scaled integers for payoff comparisons, verifies all original retained-menu deviations after the transition-class reduction, and forward-reconstructs dated cash, resources, state mass and accepted service. Standard dominance reductions already justified by the accepted source remain conditional on its funding and transition assumptions.

### Pure equilibria at the threshold

| Later shifts S | Balanced calendar | Concurrent selected learning | Generated private wealth, firm 0 / firm 1 | Accepted jobs | Customer surplus | Pure root equilibria under each tested continuation rule |
| --- | --- | --- | --- | ---: | ---: | ---: |
| 8 | (1,1,4,4) | Neither firm | 130 / 130 | 36 | 72 | 1 |
| 9 | (1,1,4,5) | Exactly one firm | 147 / 146.5625 | 39 | 77 | 2 |
| 10 | (1,1,5,5) | Both firms | 163.625 / 163.625 | 42 | 84 | 1 |

Private wealth subtracts the initial 10,000 per firm and includes the inherited equipment salvage account. It is not output or social welfare. At nine the second pure equilibrium exchanges the firms' roles and payoffs. The stated selector breaks the payoff-sum tie by firm-0 value; the economic model itself does not give firm 0 a technological advantage.

Every integer S from two through eleven is included in the primary concurrent scan. The scan also includes S=13,15,17,19,21,25,61. The first selected learning investment is at nine, and the first selected bilateral investment is at ten, on this path and under the tested continuation convention. The near-boundary audit covers S=7,8,9,10,11 under both cap-1 and cap-2 and both higher-total and lower-total pure continuation selections. These alternatives agree on the displayed adoption transitions. No second successor is selected in these cases. Agreement of these conventions does not exhaust all possible continuation selections.

At S=61, the old exclusive/concurrent wealth values 925 and 1033.8125 per firm are recovered exactly. This links the threshold study to the accepted earlier result, rather than constructing a separate numerical economy.

### The mechanism, derived from the dated account

Call the no-research manufacturing program P and the successor-plus-training program R. On the relevant fixed-program branch, P produces later service at a net bill giving baseline generated wealth B(S)=15S+10. R pays five more at the first date and gives up twelve in second-date net cash, for an initial difference of -17. Its physical qualification probability is

\[
P(\text{qualified})=\frac34\frac34+\frac14\frac12=\frac{11}{16}.
\]

Qualification saves three per later shift, giving g(S)=33S/16-17. With both mobile robots installed, later quantities remain saturated; this gain is an operating-cost return. When only one firm chooses R, the other continues supplying physical service on date two while the learning firm does not. Its price rises by two under the accepted inverse demand. This explains a second incentive term.

Subtracting B, the diagnostic game is

|  | Rival P | Rival R |
| --- | --- | --- |
| Own P | (0,0) | (2,g) |
| Own R | (g,2) | (g,g) |

R is preferred to P against a producing rival when g>0. Against a learning rival it is preferred only when g>2. Thus the diagnostic has PP for g<0, two asymmetric pure equilibria for 0<g<2, and RR for g>2. At the endpoints there are weak indifferences.

Its analytic boundaries are

\[
S_1=\frac{272}{33},\qquad S_2=\frac{304}{33}.
\]

These are exact **diagnostic-program** boundaries. They are not claimed as certified fractional boundaries of the full game. The actual root-payoff matrix matches this form at S=9,10,11. At S=7 and S=8 some off-equilibrium research continuations reoptimize differently. For example, at S=8 the full-game RR root values are (129.75,129.6875), while the diagnostic predicts (129.5,129.5). This directly demonstrates why matched values at a few points are insufficient for a full continuous threshold theorem.

The new substantive result is the globally checked integer transition and its mechanism. The simple matrix explains that result; it is not substituted for the full feasible menu.

### A mixed root equilibrium is also certified

At S=9, g=25/16. In the diagnostic, R yields B+g, while P against a rival researching with probability p yields B+2p. Indifference gives

\[
p_R=\frac g2=\frac{25}{32}.
\]

The implementation checks this candidate against **all 92 retained root actions for each firm**, after the inherited valid dominance reductions. Both maximum deviation numerators are exactly zero. The pure continuation policies were already solved at all states. This certifies the candidate in the full finite game under those continuation policies, not just the two-action diagnostic.

Independent root randomizations give profile weights (PP,PR,RP,RR)=(49,175,175,625)/1024. The inherited forward accountant then reconstructs the mixed root and all subsequent histories. Both tested pure continuation rules give:

| Quantity | Exact/value |
| --- | --- |
| Each firm's probability of investing in learning | 25/32 |
| Each firm's generated private wealth | 146.5625 |
| Expected accepted jobs | 38.4375 |
| Customer surplus | 76.533203125 |
| Expected first-successor attempts | 1.5625 |
| Orders and assemblies | 2 each |
| Profitable retained-menu deviations | 0 |

The asymmetric pure outcome at the same S has 39 accepted jobs, customer surplus 77, and combined generated private wealth 293.5625. The symmetric mixed outcome has combined generated private wealth 293.125. Equilibrium multiplicity affects real service and customer outcomes as well as the allocation of private rents. No welfare comparison follows from firm wealth alone.

### A pure-only continuation genuinely becomes insufficient

The exclusive-investment comparator at S=10 stops at a date-two off-path subgame with no pure equilibrium under the chosen pure continuation rule. All its retained profile payoffs were checked. This is a missing mixed-continuation solution, not a profile-budget stop, not a zero effect, and not evidence that the finite game lacks an equilibrium.

We therefore do not report an exclusive-equilibrium wealth or an exclusive-versus-concurrent premium for S=10. The number B(10)=160 belongs to the diagnostic P program; it must not be relabeled the solved exclusive equilibrium. The exact state and status are retained in the result JSON.

Finite games admit mixed Nash equilibria under the standard assumptions; [Nash (1950)](https://doi.org/10.1073/pnas.36.1.48) is the primary existence result. The present mixed implementation certifies a specified root support while keeping pure continuations. It is not a general exact mixed solver at every intermediate subgame.

## 6. How this connects to multivariate MPK_r and recursion

The integrated account still distinguishes physical marginal product, operating-cost savings, and dynamic private value. At the saturated later-output frontier in this example, qualified execution reduces paid inputs without increasing later accepted jobs. A positive learning return therefore does not imply a positive increment to that physical output frontier.

In the enlarged theory, a robot's dynamic value depends on the firm's deployment portfolio, qualification network, rights, demand, complementary humans and inference, and the policy used to allocate those resources. A discrete regime comparison Q_r-Q_s includes setup costs, timing, and coordinated changes that a marginal physical-product condition omits. An equilibrium comparative static additionally includes the response of rivals and market prices.

Do not add an unexplained recursion premium to a value function that already includes future learning and investment. Any multiplier should be derived from the transition system. Likewise, a low-adoption trap surviving global own-firm optimization must arise from a real strategic or state constraint: coordination across firms, finance, irreversible commitments, uncertain learning, or timing. A solver stuck at an inferior local own-firm optimum does not establish such a trap.

The present intermediate region is strategic substitution: the rival's research makes continued service more attractive. It is not a zero-learning trap, since PP admits a profitable deviation at S=9. Other extensions can produce strategic complementarity, but that must be derived from their specific learning, supply, standardization, or demand mechanisms.

## 7. Equilibrium, stationarity, and stability are separate tests

The broader objective is a dynamic equilibrium and its induced motion. Equilibrium policies can produce investment waves, growth, cycles, or stochastic variation rather than convergence to a fixed state. [Ericson and Pakes (1995)](https://academic.oup.com/restud/article-abstract/62/1/53/1568000) is a primary foundation for optimizing investment and an equilibrium industry process. A finite four-block game cannot establish long-run stationary stability.

For a deterministic smooth extension, let z' = T(z,a,p;theta), with equilibrium policies a=sigma*(z) and endogenous prices p=p*(z). At a fixed state the economic transition Jacobian is

\[
J=T_z+T_a D\sigma^*+T_p Dp^*.
\]

This formula assumes a and p are separate arguments, so price effects are not counted again inside a. Local asymptotic stability is established if every eigenvalue lies strictly inside the unit circle. A unit-modulus eigenvalue requires additional analysis; an eigenvalue outside signals local instability of that fixed state under the stated economic law. Discrete regime changes require one-sided or nonsmooth analysis. A stochastic invariant distribution requires its own conditions; stability of a mean map is not enough.

The Jacobian of the numerical solver's iteration is a different object. Failure of best-response iteration can be an algorithmic problem even when an equilibrium exists. A cycle in a heuristic agent simulation is evidence about that adjustment process; it becomes an equilibrium cycle only after policies and expectations satisfy the appropriate equilibrium conditions.

Similarly, different selections in upward and downward scans are not, by themselves, economic hysteresis. History dependence needs a specified mechanism, such as installed capital, data rights, switching costs, accumulated capability, or irreversible entry that connects prior states to current choices.

Useful outcomes of the next stage therefore include a unique stable stationary equilibrium; several equilibria with justified selection; a dynamic equilibrium with nonstationary states; a change in stability; a mixed-strategy region; or a rigorously established failure of a particular equilibrium concept. A numerical timeout belongs in none of those economic categories.

## 8. Reproduction, claim boundary, and next execution target

Files: [solver](global_thresholds.js), [results](global_thresholds_results.json). The solver uses Node and the existing three source files; no downloaded data, packages, paid compute, actual LLM training, or robot execution is required.

```bash
node global_thresholds.js --shifts 9 concurrent 2 1
node global_thresholds.js --shifts 9 concurrent 2 1 mixed
node global_thresholds.js --reproduce all
```

`--reproduce selection` and `--reproduce mixed` reproduce individual groups. The complete result contains 34 primary comparison records (33 solved and one pure-continuation gap), 20 near-boundary selection/cap records, and two mixed-root records. These are 51 distinct solves because some primary and selection records overlap. Source hashes, exact wealth denominators, forward dated accounts, profile counts, and deviation counts are recorded. The root-support checker is new; it reuses the accepted equilibrium engine and forward accountant. No independent second implementation of the entire dynamic solver is claimed.

### Established here

1. The globally checked integer adoption transition on the stated parameter path, with asymmetric and bilateral learning separated.
2. Two pure and one explicitly certified mixed root equilibrium at S=9 under the tested pure continuations; actual service and private-value implications.
3. A fixed-profile affine incentive-region theorem, with a counterexample to connected selected regions.
4. A precise distinction between equilibrium regions, own-policy envelopes, dynamic state behavior, and numerical convergence.
5. A diagnosed intermediate-subgame need for mixed continuation in the exclusive S=10 comparator.

### Open and prioritized

**Next dependency:** implement exact parameter-region certificates and propagate mixed continuations at intermediate subgames, beginning with the exclusive S=10 gap. Preserve the explicit ordinary-learning and hardware alternatives. Map feasible equilibrium branches before reporting a single selected curve. Do not extrapolate the diagnostic fractional thresholds into full-game claims.

Then vary the allocation of the service window as well as its total, transfer/qualification probabilities, research and kit costs, and rights. Record the incentive constraint that creates each boundary and the equilibrium-selection dependence. Within-block contingent service and learning remains the next timing extension; it should test whether these regions survive, not replace threshold tracing with isolated new examples. Binding finance, directed transfer, common latent learning, entry and input-market closure remain subsequent cumulative extensions.

After a repeated or infinite-horizon model is actually solved, study stationary distributions or fixed states, policy and price derivatives, basins and stability. Economic RL should be judged against these equilibria or disclosed best-response errors, with the learning/adjustment process specified. Neither successful optimization nor a nonconvergent training run establishes a nonlinear economic result on its own.

The November 27 recursive-pilot, November 29 program, December 2 theory-week, December 6 contribution and December 25 final gates remain intact. This extension changes the order and precision of the next theoretical target, not the program clocks or empirical claim status.

**Subsequent November 26 result:** [Exact intermediate mixed continuation](MIXED_CONTINUATION.md) closes the exclusive S=10 gap and certifies a conditional lab-fee interval. Historical pure-only results above remain as provenance.
