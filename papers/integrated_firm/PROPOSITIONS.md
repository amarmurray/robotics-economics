# Propositions, derivations and boundaries

These statements apply to the environment in [UNIFIED_MODEL.md](UNIFIED_MODEL.md). Their mathematical foundations are standard. The contribution of this edition is a common, solved economic account and its specific comparisons, not a claim to have invented dynamic programming, information value or potential games.

## P1. Existence and the cash account

**Statement.** Suppose the horizon is finite, each reachable state has a finite nonempty feasible action menu, outcomes have finite support, and receipts and outlays are finite. The firm's problem has an optimal nonanticipating policy, found by backward induction. With discount factor one, no borrowing and terminal liquidation, paying no intermediate dividend is weakly optimal if retained cash is costless and creates no additional obligation.

**Proof.** At horizon zero, liquidation specifies a finite payoff. Given the next-period value on each reachable state, each feasible current action has a well-defined finite expectation. A maximum over the finite nonempty menu exists. Repeating this argument defines an optimal state-and-time-contingent policy. Reachable cash and posterior states may grow with the horizon, but remain finite for any fixed initial state and finite horizon.

For dividends, take any policy that distributes cash before the terminal date. Retain those distributions in a separate notional reserve, execute the same real actions and pay the accumulated distributions at liquidation. The reserve weakly enlarges feasibility and does not change the other state transitions. With unit discount and no holding cost, terminal wealth is unchanged. The cash identity follows by summing \(B_{t+1}-B_t=\mathcal R_t-C_t-d_t\). It is pathwise, before expectations.

**Boundary.** With impatience, borrowing costs, holding costs, taxation, outside reinvestment or a new obligation triggered by cash, retained dividends need not be optimal. The general dividend problem must then be solved. Cash itself and salvage of endowed equipment must not be mislabeled newly earned profit.

## P2. Optional capability and information cannot reduce optimized value

**Statement.** Suppose a change preserves every old lawful policy, permits the same observations and state transitions when the new option is unused, and adds no compulsory costs or obligations. Optimized value weakly increases.

**Proof.** The old optimal policy remains feasible and earns its old value. The new optimum is at least that value. No differentiability, concavity or positive transfer assumption is required.

For an informational improvement, a sufficient condition is that the old observation can be produced by a state-independent stochastic garbling of the new observation and that the garbling can be implemented at no extra cost. The firm can generate the old signal and follow its old policy. The conclusion is a standard experiment-comparison argument.

**Boundary.** Actual realized outcomes may worsen. A fixed, misspecified rule can lose after being given information it misinterprets. Storage, mandatory requalification, coordination costs and revoked prior policies also invalidate the free-option premise. These are distinct from a harmful effect of *costless optional* knowledge.

The code retains older execution and research procedures. At a model's maximum level it also retains the old cross-domain qualification experiment as a probe. Idle closure is available irrespective of wealth. These are economically material details: without them, a numerical model can manufacture violations of the proposition.

In the presence of competition, the statement concerns a firm's opportunity set holding its environment and rivals' policies fixed. Its equilibrium payoff need not rise when its new opportunities induce an adverse equilibrium response. Equilibrium selection and information disclosure must be specified separately.

## P3. The precise value of a decision-relevant signal

Let two feasible actions differ in total economic continuation value by a random variable \(X\). Given current information \(\mathcal I\), choosing the second action yields an incremental value \((\mathbb E[X\mid\mathcal I])_+\). With an optional signal \(Z\), its gross value is

\[
\operatorname{VOI}(Z\mid\mathcal I)=
\mathbb E[(\mathbb E[X\mid\mathcal I,Z])_+\mid\mathcal I]
-(\mathbb E[X\mid\mathcal I])_+.
\]

**Proof.** Optimize between the two action values conditional on \(\mathcal I,Z\), then integrate over the signal. Subtract the optimized value without the signal. Nonnegativity follows because the positive-part function is convex.

It is strictly positive when the posterior action-value difference has positive probability of being strictly positive and strictly negative. A signal that only moves a probability while preserving the action ranking has zero gross decision value in this two-action problem. More than two actions require the analogous upper-envelope calculation.

**Economic connection.** An interpretable diagnosis, a forecast of robot productivity, and a more confident success probability have value only through a feasible changed decision. Their costs include measurement, transmission, validation and the service displaced before the decision. A large recipient fleet can increase the payoff difference, but can also change the chosen action, support bottleneck and obtainable price.

## P4. One accounting rule for Economic RL

Let the original finite-horizon objective be

\[
G=\sum_{t=0}^{T-1}\beta^t r_t+\beta^T g(s_T).
\]

For any functions \(\Phi_t\), define

\[
r'_t=r_t+\beta\Phi_{t+1}(s_{t+1})-\Phi_t(s_t),
\qquad
g'(s_T)=g(s_T)-\Phi_T(s_T).
\]

Then

\[
G'=G-\Phi_0(s_0).
\]

**Proof.** Expand the sum. Each positive intermediate potential cancels the corresponding negative term one date later. The terminal adjustment cancels the final potential. The remaining term depends only on the initial state, so rankings over feasible policies are unchanged.

This is the finite-horizon form of established potential-based reward shaping; see Ng, Harada and Russell (1999), [original paper](https://people.eecs.berkeley.edu/~pabbeel/cs287-fa09/readings/NgHaradaRussell-shaping-ICML1999.pdf). The proof here shows the exact accounting needed for this firm's terminal wealth.

A counterfactual advantage or department credit may help optimization, but summing departmental credits into external revenue generally double counts joint gains. Similarly, paying both the future operating return and an unadjusted bonus for having created the model that produces it changes the objective.

**Checked example.** The verifier uses \(\Phi=7M_P+3M_D+5\psi+2(D_P+D_D)\). For the four-period baseline, omitting the terminal adjustment adds an expected 1.2 ticks purely because the selected policy leaves a digital capability. That is a proxy windfall, not extra customer payment.

No learned-policy convergence result is claimed here. The exact solver supplies a target for out-of-sample regret comparisons. The earlier branch's tabular RL experiment remains separate evidence about an approximation with matched ordinary comparators.

## P5. Fixed-policy local sensitivity

Consider a finite stationary state space, discount \(0\leq\beta<1\), fixed policy \(\pi\), reward vector \(r_\pi(\theta)\), and stochastic transition matrix \(P_\pi(\theta)\), differentiable in a scalar parameter \(\theta\). Suppose the policy remains feasible. Then

\[
V_\pi=r_\pi+\beta P_\pi V_\pi,
\qquad
D_\theta V_\pi=
(I-\beta P_\pi)^{-1}
[D_\theta r_\pi+\beta(D_\theta P_\pi)V_\pi].
\]

**Proof.** The inverse exists because \(P_\pi\) is stochastic and the spectral radius of \(\beta P_\pi\) is below one. Differentiate the first identity and collect the terms involving \(D_\theta V_\pi\). The inverse can also be expanded as \(\sum_{n\ge0}\beta^nP_\pi^n\).

For a finite horizon, no infinite-horizon stationarity is needed:

\[
D_\theta V_h^\pi=
D_\theta r_h^\pi
+\beta(D_\theta P_h^\pi)V_{h-1}^\pi
+\beta P_h^\pi D_\theta V_{h-1}^\pi.
\]

The terminal derivative must be included. This recursion is the appropriate analogue for the published finite economy.

**Interpretation.** The first direct term is current margin or resource use. The second changes the probabilities of inherited capabilities, information, equipment or cash. The final term propagates previously induced changes. If the complete augmented state includes resources and beliefs, no separate unexplained “feedback payoff” is needed.

With a finite set of policies and a strict optimum that persists in a neighborhood, the same derivative holds for the optimized value there. With continuous controls, an envelope result needs its own regularity and feasibility conditions. At a tie the value is an upper envelope and may have only directional derivatives. Discrete budget and equipment changes should be evaluated as finite changes.

**Boundary.** The stochastic matrix in this result is not the earlier nonnegative matrix counting new installations induced by an installed machine. A stationary Markov resolvent is well defined under discounting even when an investment-response interpretation is inapplicable. Claims about self-reproducing deployment require an economically derived installation map, saturation and new opportunity supply.

## P6. A global comparison separates technological effects and adaptation

Let \(J_e(\pi)\) be the value of policy \(\pi\) in environment \(e\in\{0,1\}\), and let \(\pi_0\) be optimal in environment 0. If it remains feasible in environment 1,

\[
V_1-V_0=
\underbrace{J_1(\pi_0)-J_0(\pi_0)}_{\text{change under the old rule}}
+
\underbrace{V_1-J_1(\pi_0)}_{\text{value of adapting}}.
\]

**Proof.** Add and subtract \(J_1(\pi_0)\) and use \(V_0=J_0(\pi_0)\). Optimality gives nonnegativity of the second term.

This is useful for a new controller, extra cash, an additional embodiment, a changed task mix or a new information channel. It does not assign the first term a universal sign. If the change only adds a free option, both the old-policy emulation and P2 apply.

The identity also exposes a comparison error: an uninformed frozen rule in one environment and an informed reoptimized rule in another confound the intervention with adaptation. Both objects can be useful, but they answer different questions.

For an equilibrium comparison, specify rival continuation strategies and selection when defining each \(J\). A unilateral fixed-rival comparison and a change in equilibrium are different counterfactuals.

## P7. Procedure value is an endogenous difference of continuation programs

Fix a current production plan and a candidate procedure experiment \(e\). Let \(s_1(\omega)\) and \(s_0(\omega)\) denote the next states with and without a qualified successor, including the experiment's current outlays and any correlated observations. If conditional qualification probability is \(\rho_e(\omega)\), its continuation component is

\[
\mathbb E\left[
\rho_e(\omega)\{V_{h-1}(s_1(\omega))-V_{h-1}(s_0(\omega))\}
+V_{h-1}(s_0(\omega))
\right].
\]

Compare this with the **best alternative joint action**, not simply with doing nothing. The full comparison contains displaced current service, changed cash feasibility, alternative experiments and external contracts.

In a special restriction where success changes only the successor coordinate, current costs are \(c_e\), and the remaining state is deterministic, the experiment pays relative to a matched no-experiment action if

\[
\rho_e\Delta_\psi V_{h-1}>c_e+\text{other displaced value}.
\]

The right side is not necessarily the direct invoice: using a scarce validator can sacrifice current service or another research path. The left side is not an assumed constant recipient stake.

**Second generation.** Let procedure 1 improve the chance of producing procedure 2, and let procedure 2 improve subsequent training. An initial choice can then affect the distribution of successors produced using the first improvement. If all downstream procedures are held fixed, this second-generation channel disappears even when first-generation reuse remains valuable. The three-cohort empirical design in the manuscript targets that distinction.

**Boundary.** A finite cap on models and procedures creates saturation. A positive successor effect, or even two successful generations, is not a proof of unbounded or accelerating growth. Such a proof would need a continuing task/opportunity process, the costs and reliability of further successors, and a resource/market closure.

## P8. Why a single local shadow price may fail to coordinate learning

In a concave separable allocation with convex resource constraints and strong duality, a common vector of resource prices can decentralize the optimum. The planner's Lagrangian separates by activity, and complementary slackness reconciles total resource demand with capacity.

The graph study supplies a reason not to assume these conditions universally. Suppose two actions have costs \(b,c\), zero stand-alone benefit, and joint benefit \(G>b+c\). At the idle point the marginal payoff from taking either action alone is negative. Independent actors following unilateral marginal improvement can remain idle although the joint package pays. A common contingent plan or bundle contract can implement the package.

This is not a general impossibility theorem for prices or contracting. Nonlinear tariffs, contingent transfers, centralized choice and a capable ordinary organization can recover the same allocation if allowed. The integration question is which instruments, information and commitments are actually feasible. A recursion label does not itself create a missing contracting advantage.

## P9. Pure equilibrium in the terminal Cournot restriction

Let firm \(i\) choose a feasible accepted-service vector \(q_i\) and associated minimum resource cost \(C_i(q_i)\). Each firm's feasible set can be discrete and can couple markets through labor, compute and cash. Assume those feasible sets are independent across firms at the time of choice, and market \(m\) has inverse demand \(a_m-b_m Q_m\), \(b_m>0\).

Operating profit is

\[
\pi_i(q)=\sum_m q_{im}(a_m-b_mQ_m)-C_i(q_i).
\]

Define

\[
\mathcal P(q)=
\sum_m\left[
a_mQ_m-\frac{b_m}{2}Q_m^2-\frac{b_m}{2}\sum_i q_{im}^2
\right]-\sum_iC_i(q_i).
\]

For a unilateral change \(q_i\to\tilde q_i\), the change in \(\mathcal P\) equals the change in \(\pi_i\).

**Proof.** Hold \(Q_{-i,m}\) fixed. The part depending on \(q_{im}\) becomes
\(a_mq_{im}-b_mq_{im}^2-b_mq_{im}Q_{-i,m}\), plus constants and the firm's own cost. This is exactly its operating-profit dependence. On a finite nonempty profile set, a maximum of \(\mathcal P\) exists and admits no profitable unilateral deviation. Thus a pure Nash equilibrium exists.

The code enumerates **all** terminal pure equilibria, verifies unilateral profit/potential changes, and specifies a selection. At the earlier date, strategic investment changes future feasible sets and selected continuation outcomes. The same potential formula need not hold there. Pure first-period equilibria in the reported cases are computational findings, not consequences of P9.

Generic finite-horizon finite stochastic games have a mixed Markov equilibrium by backward induction through finite stage games. See [Daskalakis and Farina, section S6.3.1](https://www.mit.edu/~6.7980/stochastic_games.html). The present algorithm would need a mixed-equilibrium solver if a later parameter case lacked a pure root equilibrium.

## P10. A shared unknown regime creates correlated outcomes

Suppose two qualification outcomes \(X_1,X_2\) are independent conditional on \(H\), with success probabilities \(p_i(H)\). Then

\[
\operatorname{Cov}(X_1,X_2)
=\operatorname{Cov}(p_1(H),p_2(H)).
\]

**Proof.** Conditional covariance is zero. Apply the law of total covariance.

If both firms perform the baseline cross-training experiment, \(p_i(1)=1/2\), \(p_i(0)=1/4\), and \(\Pr(H=1)=3/5\). Joint success has probability

\[
(3/5)(1/2)^2+(2/5)(1/4)^2=0.175,
\]

while multiplying the marginal success probabilities gives \(0.4^2=0.16\). Their covariance is \(0.015\). Multiplying independently averaged firm kernels would therefore give the wrong competitive continuation value.

The two-period game integrates over \(H\) once for both firms. Because beliefs have no terminal productive role, it may integrate out public posterior labels at the terminal date. A longer game must retain the joint public posterior, and a private-report game needs private beliefs and an equilibrium concept appropriate to that information structure.

