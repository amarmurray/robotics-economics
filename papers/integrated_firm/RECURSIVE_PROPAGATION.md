> **FROZEN VERIFICATION ARCHIVE — not an active solver queue.** The hourly integrated_firm writer is paused under [AGENTS.md](../../AGENTS.md). All suffix/reservation expansions, further within-block learning/collection, B=16+ binding-cash searches and joint price/mixed-support/market-closure sweeps are frozen. An exact finite run is permitted only for a named Paper 1–3 analytical proposition after its falsification question, minimum domain, command and budget are logged in [ORACLE_REQUESTS](../../research/portfolio/ORACLE_REQUESTS.md). The historical deadlines, lease descriptions and next actions below are retired. [Current canon](../../research/portfolio/CANON.md) · [Current state](../../research/portfolio/state.json).

# Recursive firm theory: equilibrium regions, event time and market feedback

## Research object and current status

The organizing question is: which combinations of capital, capability, learning, financing and organization remain individually optimal when other firms and input markets respond, and what economic evolution do those choices generate?

The object is an equilibrium correspondence together with its induced law of motion. For parameters θ and an initial economic state X, retain the set of mutually optimal contingent policies, values, prices and feasible allocations. Then study the state paths or distributions those policies produce. Equilibrium eligibility, equilibrium selection and dynamic stability are separate questions. An equilibrium path can be nonstationary; cycles or growth do not by themselves imply disequilibrium.

The accepted finite economy already combines service, hardware, ordinary learning, procedure improvement, retained evidence, scope and product-market rivalry. The new [common kit-price certificate](DYNAMIC_KIT_REGION.md) establishes complete-game equilibrium intervals including intermediate mixing. The event-time, multidimensional and market-closure results below are derivations and implementation contracts, except where they explicitly cite implemented results. They do not assert that the expanded economy has already been numerically solved.

The broader contribution sought is a common economic account of capability propagation, funded deployment and improvement of the procedures producing future improvements. Recursive technology receives no automatic payoff premium. Its value must arise from chosen, feasible downstream operations in that account.

## 1. A state and clock that preserve the mechanism

Write a firm's state as
\[
X_i=(K_i,A_i,D_i,\psi_i,B_i,R_i,J_i,O_i,\mathcal I_i).
\]
K is installed and pending hardware; A is qualified executable capability; D is evidence indexed by eligibility and rights; ψ is a stock of learning or research procedures; B is spendable cash; R is dated receivables; J contains unfinished jobs with sufficient age or remaining-work information; O records organizational scope, contracts, obligations and authority; and \(\mathcal I\) is the information needed for decisions. The joint state includes rivals, demand and input-supplier conditions.

These objects remain distinct. A successful experiment is not automatically a released qualification. A qualified policy is not installed hardware. A sale is not collected cash. Evidence that exists is not necessarily evidence that the firm is authorized to use or transfer.

The next decision epoch can be triggered by service completion or failure, evidence arrival, research completion, validation, hardware delivery or commissioning, collection, a market event, or a scheduled review. Permit economically meaningful chosen review times or contingent control plans as well: restricting decisions to exogenous arrivals could exclude a valuable intervention.

A joint event kernel specifies both successor state and elapsed physical time:
\[
Q(dX',d\tau\mid X,u).
\]
The elapsed time can depend on controls, congestion, procedures and the state. A semi-Markov formulation accommodates general durations; a finite-state continuous-time jump model is a useful special case, not a requirement to make every duration exponential.

Using distributions to equity and terminal net assets as the value convention, a finite-horizon decision condition has the form
\[
V_i(t,X)=\sup_{\sigma_i}
\mathbb E_{\sigma_i,\sigma_{-i}}
\left[
 \int_{[0,\tau)}e^{-\rho s}\,d\mathrm{Div}_i(t+s)
 +e^{-\rho\tau}V_i(t+\tau,X')
\right],
\]
with a terminal payoff equal to cash, realizable receivables and salvage less liabilities. Controls, resource payments and contractual obligations determine feasibility inside the interval. Another cash-flow convention is possible, but it must not count inherited cash or collected revenue twice.

Temporally extended contingent policies have a standard semi-Markov foundation [1]. Continuous-time stochastic games can reduce the cost of computing expectations under suitable jump laws [2]. Neither reference eliminates state-space complexity or establishes that a change in economic timing is innocuous. Simultaneous controls, joint shocks and deterministic commissioning delays must retain their intended meaning.

### Exact embedding before extra flexibility

The coarse model does not identify a unique physical duration for training, validation or customer collection. Any within-block duration introduced now is an explicit new primitive. It must be varied and identified rather than described as measured by the old model.

First lift the old block economy into the event representation while keeping its controls, information use, release gates and payment availability at the original boundaries. For every legal coarse action profile, including off-path deviations, require identical aggregate rewards, boundary states, probabilities, resource use, cash and next-date information.

If an interval contains no omitted information, action opportunity or constraint change, its exact discounted compression is
\[
\bar r_i=\mathbb E\!\left[\sum_{k<\tau}\beta^k r_{i,k}\right],
\qquad
\bar P_\beta(x')=\mathbb E[\beta^\tau\,1_{\{X_\tau=x'\}}].
\]
The macro value is \(\bar r_i+\sum_{x'}\bar P_\beta(x')V_i(x')\). This follows by iterated expectations. Restricting the internal policies generally changes the game unless the full relevant contingent-policy set is represented.

This embedding distinguishes preservation of an economy from matching a selected root payoff accidentally.

## 2. What within-block propagation adds

Release four restrictions separately, then jointly.

| Change | New economically relevant decision | Identification requirement |
| --- | --- | --- |
| Earlier observation | Respond to a completed or failed experiment, eligible archive or revised belief | Same physical outcome process; record who learns what |
| Earlier qualified use and dispatch | Apply a released improvement to remaining feasible service | Preserve validation, hardware and rights prerequisites |
| Further learning | Use new evidence in another feasible training or procedure decision | Pay its duration and resources; preserve shared uncertainty |
| Earlier collections | Fund a later purchase, retry or deployment using collected cash | Same sale and risk unless deliberately changed; explicit borrowing rules |

Their effects need not add. Qualification can release labor, making another experiment feasible; collection can finance that experiment; the resulting procedure can change subsequent learning; rivals can then change their own programs.

### Conditional value of flexibility

If old policies remain feasible, the firm can ignore new information, and extra flexibility brings no unavoidable fee or disclosure, then against a fixed complete rival policy,
\[
V_i^{\mathrm{fine}}(\sigma_{-i})\ge
V_i^{\mathrm{block}}(\sigma_{-i}).
\]
The proof is inclusion of the old feasible policy set in the new one.

There is no corresponding general sign for equilibrium profit when both firms adapt. The model must solve the expanded game. Nor does the inequality hold automatically if the new institution removes commitment, forces disclosure or imposes a new cost. Those are economic changes, not pure additions to the policy set.

### Qualification time enters returns directly

For a fixed program, let F be an upfront research cost, p its success probability, τ its conditional-on-success usable time, d its incremental operating margin and T the useful horizon. Then
\[
\Delta V=-F+
p\,\mathbb E\!\left[
1_{\{\tau<T\}}\int_\tau^T e^{-\rho t}d\,dt
\;\middle|\;\text{success}
\right].
\]
At zero discounting this becomes
\[
\Delta V=-F+pd\,\mathbb E[(T-\tau)_+\mid\text{success}].
\]
This is a transparent fixed-program decomposition, not a globally reoptimized threshold. It shows why success probability and usable timing are different dimensions. A mean completion time alone generally does not identify useful operating time when deadlines truncate the payoff.

Moving a successful release from b to an earlier τ, holding the program otherwise fixed, adds the margin earned between τ and \(\min(b,T)\). Reoptimization can add retries, change service or redirect resources beyond that direct effect.

### The prerequisite graph

For a prerequisite graph with activity durations \(d_v\),
\[
T_v=d_v+\max_{u\in\mathrm{parents}(v)}T_u,
\]
with root start times determined by actual authorization, evidence and funding availability. Training and validation can be serial; hardware and data preparation can be parallel. Usable deployment occurs when its relevant prerequisite paths have completed.

For a fixed graph and resource allocation, reducing a noncritical duration does not change final readiness until it becomes critical. Reducing a uniquely critical duration advances readiness until a competing path binds. This produces kinks and moving bottlenecks. With shared resources and endogenous scheduling, the allocation and the graph itself must also be optimized.

Organization can therefore matter by changing a permission, handoff, contracting, validation or funding delay on a binding path. That is a testable channel. Integration can also add coordination cost, reduce specialization or expose the firm to idle capacity; no sign is imposed.

### Preserve physical time

For an exponential completion hazard λ, a step of length Δ has probability
\[
p(\Delta)=1-e^{-\lambda\Delta}.
\]
Discounting is \(e^{-\rho\Delta}\), and resource supplies, depreciation and workload must use the same elapsed-time convention. Keeping a per-step success probability fixed while shrinking Δ manufactures faster learning. Redrawing a common latent regime independently at each event changes the information structure.

The model should distinguish faster decisions, faster physical processes and faster information availability. Each can matter; none should be created accidentally by numerical refinement.

## 3. Receipts, finance and capital velocity

Maintain the identities
\[
dR=d\mathrm{CreditSales}-d\mathrm{Collections}-d\mathrm{Writeoffs},
\]
\[
dB=d\mathrm{Collections}+d\mathrm{Financing}
-d\mathrm{OperatingPayments}-d\mathrm{Investment}
-d\mathrm{DebtService}-d\mathrm{Dividends}.
\]
A credit sale creates a receivable. Collection converts it into cash. Counting both as new wealth and then including the same cash in terminal wealth is incorrect.

For an investment requiring upfront funding F, a useful financing event is
\[
\tau_F=\inf\{t:B_t+\mathrm{drawable\ committed\ credit}_t\ge F\}.
\]
This threshold is subject to other obligations and payment priorities. Expected future revenue is not spendable without an explicit financing contract.

Earlier collection can move \(\tau_F\) forward, enabling a research attempt or hardware order before a deadline. Sufficient bridge funding should remove this investment-feasibility channel, although discounting, credit cost and collection risk can still matter. That is a mechanism test rather than a presumption that “faster cash” always increases growth.

Capital velocity needs several clocks: commitment-to-commissioning, evidence-to-qualified-use, production-to-collection, procedure-to-next-procedure, and free-cash-to-funded-successor. Report the binding clock and cash at risk, rather than compressing all of these into turnover.

As a deliberately restrictive regenerative benchmark, if one deployment creates g funded successor deployments after a deterministic elapsed time τ, with no demand, resource or financial constraint, its growth exponent is
\[
\lambda=\frac{\log g}{\tau}.
\]
This follows by setting \(e^{\lambda\tau}=g\). The benchmark illustrates how both payoff and elapsed time matter; it does not establish exponential growth in the actual economy. Heterogeneous lags should enter the project's existing dated reproduction kernel, with each deployment and cash flow counted once.

### Multivariate returns and recursive procedures

A capability improvement can raise useful output, reduce complementary labor or compute, improve success, shorten validation, expand eligible recipients or speed recovery of cash. These channels interact with installed hardware, rights, demand and organization. A single scalar robot-capital stock is generally insufficient.

For a discrete project, compare the complete continuation value with the best feasible alternative allocation, including stopping, ordinary learning, outsourcing and waiting. Report incremental value, required dated outlays, scarce-resource use and funding delay. A quotient of incremental value by outlay can be informative, but it is not a universal marginal product independent of the state.

For differentiable local analysis, distinguish a derivative of an optimally controlled firm's value holding its environment fixed from the derivative of its value along an equilibrium branch where rivals and prices also respond. At discrete adoption or support changes, use directional differences or one-sided derivatives.

The procedure state ψ should change the same future improvement technology:
\[
\lambda_A=\lambda_A(D,A,\psi,u_A),\qquad
\lambda_\psi=\lambda_\psi(D,A,\psi,u_\psi),
\]
or the corresponding nonexponential kernels. Improving ψ can affect the future production of A and ψ. Both activities consume actual resources and time, and the firm must still choose them over ordinary production and alternatives. This is how organizational and technological recursion enters the common model without a separately awarded recursive dividend.

## 4. From intervals to globally reoptimized surfaces

Let θ include common research costs, kit prices, wages, compute prices, service calendars, qualification and transfer parameters, rights and financing terms. A common parameter must change every applicable action and continuation at every date. Perturbing one selected matrix does not do that.

### Three mathematical regimes

**Fixed behavior, fixed transitions, affine rewards.** Values and deviation slacks are affine. The complete-profile eligibility region is polyhedral. The implemented kit-price result belongs here, including its fixed intermediate mixtures.

**Fixed behavior, parameter-dependent transitions.** Finite-horizon values can already be polynomial or rational. For example, two independent retry opportunities with success p give eventual success \(2p-p^2\); expected attempts are \(2-p\). Thus probability changes affect both useful outcomes and the cost of contingent continuation. A nonlinear parameter response does not require strategic mixing.

**Endogenous mixing within a regular support.** For a two-player continuation game with rational payoff matrices A(θ), B(θ), fixed equal-size supports I,J, and nonsingular indifference systems,
\[
\begin{bmatrix}A_{IJ}&-\mathbf1\\\mathbf1^\top&0\end{bmatrix}
\begin{bmatrix}q\\v_1\end{bmatrix}
=\begin{bmatrix}0\\1\end{bmatrix},
\qquad
\begin{bmatrix}B_{IJ}^\top&-\mathbf1\\\mathbf1^\top&0\end{bmatrix}
\begin{bmatrix}p\\v_2\end{bmatrix}
=\begin{bmatrix}0\\1\end{bmatrix}.
\]
Cramer's rule gives rational probabilities and values. Backward induction propagates those rational functions to earlier states. Branch eligibility requires nonnegative probabilities, positive probabilities for the stated exact support, all outside-support incentive inequalities, feasible actions, valid primitives and nonzero denominators at every continuation.

A vanishing determinant is not proof that equilibrium disappears. It can signal a support change, degeneracy, a continuum or a removable singularity. At a fixed parameter value, arbitrary candidate support pairs can instead be tested with linear indifference and best-response conditions; a positive common lower bound on supported probabilities verifies exact support. This feasibility check does not enumerate all supports. General bimatrix equilibrium algorithms and degeneracy are established tools [3].

### A broader structural proposition

**Proposition.** For a finite-horizon game with finitely many states and actions, semialgebraic parameter domain and menu conditions, and polynomial or rational rewards, transitions and terminal values with valid denominators, the graph of its state-contingent mixed equilibrium correspondence is semialgebraic.

**Derivation.** Introduce values and probabilities at every state-date pair. Expected one-action returns Q are polynomial or rational in parameters, probabilities and downstream values. Impose
\[
\sigma_i(a)\ge0,\quad\sum_a\sigma_i(a)=1,\quad
V_i-Q_i(a)\ge0,\quad
\sigma_i(a)\,[V_i-Q_i(a)]=0.
\]
These finite constraints express mutual best responses at every subgame. Include primitive domains and feasible-menu cases, and safely clear denominators. They form a finite polynomial system. Projection onto parameters, outcomes or support indicators preserves semialgebraicity by the Tarski–Seidenberg theorem [4]. □

For one real parameter, such regions are finite unions of intervals and isolated points. With multiple parameters they can have curved boundaries and disconnected components. This structural result is not a claim that computing the whole set is cheap. If physical-time parameters enter through exponentials such as 1−exp(−λΔ), the polynomial/rational premise is no longer satisfied in those parameters. One can certify probability-parameter regions and retain the explicit mapping to physical time, or use appropriately validated analytic methods; the semialgebraic theorem must not be extended by assertion.

The rational-branch statement is narrower: it uses a regular two-player finite backward recursion. Additional strategic suppliers or entrants generally introduce products of several opponents' mixing probabilities, so branches need not be rational. The semialgebraic formulation remains available under its stated assumptions. Infinite-horizon values also require solving a coupled fixed-point system; finite backward induction does not establish their rationality. Even with two firms, solving nonlinear market-clearing equations for endogenous prices can produce algebraic rather than rational parameter branches. The inner-game rationality statement does not establish rationality of the whole market closure.

### Certification method

1. Partition by legal menus, rights and binding-finance regimes before asserting one formula.
2. Generate a candidate complete support profile and propagate its symbolic values backward.
3. Collect support, determinant, primitive, feasibility and every deviation inequality at every state.
4. Handle denominator signs explicitly. For real N,D with D≠0, \(N/D\ge0\) is equivalent to \(ND\ge0\), not to \(N\ge0\) without a sign condition.
5. In one dimension, isolate all relevant polynomial roots and sign-test the resulting cells. Treat endpoints and singular cases separately.
6. Record an algebraic boundary by its defining polynomial and isolating interval when it is not rational. A decimal approximation alone is not a certificate.
7. In higher dimensions, use certified decomposition or rigorously validated subsets, clearly identifying any uncovered region.
8. Track selector conditions separately from equilibrium eligibility.

Parameter-dependent menu reduction is a concrete risk. An internal and an outsourced learning action can be equivalent at one price or probability but differ elsewhere. Equality at a seed is insufficient to discard either over a region.

This gives a route to globally reoptimized threshold surfaces: discover and certify adjacent complete equilibrium branches rather than extrapolating the return of one frozen program.

## 5. Market closure in the same economy

Product-market competition is already endogenous in the finite game. Wages, compute prices, hardware supplier responses, broad financing terms and operating-firm entry are additional closures.

| Market or institution | Equation or mechanism needed | What it can change |
| --- | --- | --- |
| Human and specialist labor | Supply, skill constraints and wage determination | Opportunity cost of service, validation, supervision and research |
| Compute | Delivered compute capacity, allocation, price and capacity investment | Experiment intensity, execution cost and waiting time |
| Hardware suppliers | Inventories, orders, production, delivery and commissioning | Whether qualified capability has a usable embodiment |
| Finance | Savings/funding supply or explicit lender contracts, collateral, default and payment dates | Which investments are feasible before their opportunities expire |
| Operating-firm entry and exit | Sunk setup cost, waiting option, entry coordination and liquidation | Residual demand, imitation, rents and deployment scale |
| Household demand and ownership | Budgets, factor income, dividends and final expenditure | Where released labor and profits go, and what sustains demand |

A reduced-form input supply schedule can be a useful first closure if labeled as such. With two large firms, a wage or compute price determined by their joint demands creates strategic input-market effects. They must internalize their own influence if that is the specified institution. Calling them price takers would require a different assumption.

Shared physical capacity must hold in each realized allocation. Under independent mixed actions, satisfying capacity only in expectation does not prevent simultaneous overbooking. Use an explicit reservation, auction, rationing or queue mechanism. Simply deleting infeasible joint action pairs changes the strategic feasibility structure and requires a corresponding equilibrium concept.

Entry should include the value of waiting when investment is sunk. In a price-taking free-entry benchmark, entry value is bounded by its cost and equals that cost when a positive entrant mass is active, subject to the model's conditions. A finite oligopoly with strategic entry needs its own timing and coordination game. Hopenhayn provides a standard stationary industry framework in which entry, exit and firm heterogeneity coexist [5]; our recursive capital, learning and procedural state is an extension to solve, not a result borrowed from that model.

Consolidate ownership consistently. An internal transfer price is a cost to one division and revenue to another; it cancels in consolidated firm cash. The labor, compute, hardware and external cash needed for the activity remain real. Outsourcing, acquisition and integration should be compared in that same account, including contracting and coordination costs.

These closures can both damp and strengthen propagation. Greater deployment can raise wages or compute prices, inducing substitution and slowing some investment. It can also justify capacity expansion, spread fixed costs or increase eligible evidence. Which effects dominate is an equilibrium result.

## 6. Dynamics after solving the economy

The repeated economy needs a law of motion for installed and pending hardware, capabilities, evidence, procedures, wealth and obligations, supplier capacity, beliefs and the distribution of firms. Finite-horizon terminal truncation can suppress investments with late returns, so the current four-block result does not establish a long-run outcome.

First distinguish:

- Existence of an equilibrium strategy profile.
- Existence of a stationary equilibrium or stationary distribution.
- Stability of that equilibrium under the specified economic transition law.
- Convergence of a numerical algorithm used to calculate it.

Failure of a pure-equilibrium search establishes none of the negative economic claims above. Mixed equilibrium paths can be nonstationary. A numerical cycle in a best-response algorithm is not evidence that firms' actual economy cycles.

For a finite state space and fixed stationary behavior, distributions evolve linearly under its transition matrix. Nonlinear aggregate feedback arises when policies, prices, supply or transition kernels depend on the evolving economic state or distribution. Bounded state truncations also cannot demonstrate indefinitely unbounded growth.

### How market closure changes local feedback

Suppose solved forward-looking equilibrium policies have been substituted into both an economic state map and contemporaneous market clearing:
\[
x_{t+1}=F(x_t,p_t),\qquad H(x_t,p_t)=0.
\]
On a differentiable, locally single-valued branch with unchanged active constraints and invertible \(H_p\),
\[
p_x=-H_p^{-1}H_x,\qquad
J_{\mathrm{closed}}=F_x-F_pH_p^{-1}H_x.
\]
The derivation is the implicit function theorem followed by the chain rule. Policy responses must be included once in F and H, not omitted and not counted twice.

This expression shows where an input-market response changes feedback among capital, capability and organization. It has no universal sign. Discrete-time local asymptotic stability follows when every eigenvalue has modulus below one; for a continuous-time drift, their real parts must be negative.

If prices adjust slowly, include them as states rather than imposing instantaneous clearing. Hardware pipelines, qualification work and receivable ages likewise belong in the state. Explicit fixed delays outside a finite state representation require delay-system stability analysis. At support switches, capacity boundaries or entry thresholds, use branch-specific and one-sided analysis rather than one smooth Jacobian.

An event-count transition is not a calendar-time growth rate. Elapsed-time distributions must remain in the analysis.

## 7. Cumulative implementation and falsification contract

| Step | Accepted advance now | Next acceptance requirement |
| --- | --- | --- |
| Complete equilibrium regions | Common kit-price intervals include all retained deviations and off-path mixed continuations | Solve adjacent branches and add common research costs without invalid menu reductions |
| Intermediate mixing | Nine exclusive S=10 mixed subgames propagated; endpoint values replay | General supports and degeneracy; endogenous probabilities across common parameter changes |
| Parameter dimensions | Affine, rational-branch and semialgebraic derivations above | Certified multidimensional cells for costs, probabilities, rights, timing and finance |
| Within-block decisions | Exact embedding and causal timing contract specified | Replay the old game, then solve one additional within-block response before expanding cumulatively |
| Long-run dynamics | Defined state, closure and local feedback criteria | Solve repeated or infinite-horizon equilibrium with transversality or terminal-error control, then test dynamics |
| Broader markets | Explicit resource, price, finance and entry mechanisms specified | Add closures to the same dated economy and certify each restriction before combining |

The first event implementation should reuse S=8,9,10, preserving the accepted technologies and calendars. Lock timing to recover every coarse kernel and payoff, then allow one additional response to a specified qualification event. Subsequently allow evidence-driven learning and collected-cash funding. Re-solve all relevant continuation subgames after each expansion.

Required falsifiers include: an unmodeled profitable deviation; a qualification used before release; evidence used without rights; service performed without installed hardware; cash spent before collection or financing; a resource budget reset by the numerical clock; an equilibrium difference driven by a changed primitive rather than flexibility; or a mixed plan that violates realized shared capacity.

Useful mechanism ablations remove remaining service opportunity, improve funding enough to eliminate the liquidity constraint, delay collection past the investment deadline, remove transferable rights, or leave hardware as the binding prerequisite. These isolate why a threshold moved.

Economic RL should eventually learn policies in this same environment and be compared with certified values, feasibility and regret on tractable restrictions. The current exact benchmarks and event specification are not an implemented RL experiment or evidence of a learned firm's empirical performance.

All seven integration obligations and the existing November 27, November 29, December 2, December 6 and December 25 gates remain active. The new sequence integrates with the cumulative theory; it does not reset the clocks or replace the source theories.

## References and provenance

The propositions and proposed contracts above are explicit derivations for this research program. The standard foundations are:

1. Sutton, Precup and Singh (1999), “Between MDPs and semi-MDPs: A framework for temporal abstraction in reinforcement learning.” [Paper](https://people.cs.umass.edu/~barto/courses/cs687/Sutton-Precup-Singh-AIJ99.pdf).
2. Doraszelski and Judd (2012), “Avoiding the curse of dimensionality in dynamic stochastic games,” Quantitative Economics 3, 53–93. [Author-hosted paper](https://kenjudd.org/wp-content/uploads/2021/11/2012-Doraszelski_Judd-Quantitative_Economics.pdf).
3. von Stengel (2021), “Finding Nash Equilibria of Two-Player Games.” [Paper](https://arxiv.org/abs/2102.04580).
4. Bierstone and Milman (1988), “Semianalytic and subanalytic sets,” Section 1, including the Tarski–Seidenberg projection theorem. [Journal archive](https://www.numdam.org/item/PMIHES_1988__67__5_0.pdf).
5. Hopenhayn (1992), “Entry, Exit, and Firm Dynamics in Long Run Equilibrium,” Econometrica 60(5), 1127–1150. [Paper](https://www.edegan.com/pdfs/ERBC/Haltiwanger,%205.17.11/Hopenhayn_1992.pdf).

Input repository revision: 90adeff078811aab2ef02885d432a5cfc47c50e2. New computational claims are restricted to DYNAMIC_KIT_REGION.md and its executable results. This note does not claim empirical identification, a general-equilibrium calibration, globally unique equilibrium, or proven nonlinear long-run behavior.
