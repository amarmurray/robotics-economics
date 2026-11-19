# When Capabilities Become Production
## Qualification networks, data acquisition, and investment

**Integrated theory investigation | 17 November 2026**  
**Robotics Economics program | private working draft, not submitted**

### Abstract

Technical capability, qualified service, and economically valuable production are distinct objects. We study how the organization of a production system connects them. A fixed-technology operating problem identifies the activities that can generate value under customer demand, scarce physical capacity, and shared organizational resources. New qualifications add productive possibilities, but their value can be complementary, substitutable, or zero. We characterize zero operating value through a common optimal system of resource prices. We then construct productive networks in which every proper subset of a collection of new qualifications is economically redundant, even though acquiring the complete collection increases output. This structure translates independent, diminishing-return qualification technologies into initially increasing economic returns to learning. More generally, the smallest economically productive qualification bundles determine the leading order of the expected value of small technical improvements. Customer demand can change this order without changing the robot or its learning technology. We solve both a precommitted learning portfolio and a sequential, cost-aware acquisition problem with observed and retained successes. Adaptation can greatly lower the private investment hurdle without removing the leading-order gross-return bottleneck under independent, bounded-rate acquisitions. Correlated qualification outcomes can instead change that order, and their economic value depends on whether capabilities complement or substitute for one another. The results organize the earlier deployment, coordination, and financing models into a common framework and specify a falsifiable measurement program. They do not estimate robotics learning curves, establish an industry equilibrium, or establish publication novelty.

**Central proposition:** The economic response to technical learning depends on the structure of the production opportunities that the learning unlocks, not only on the technical learning curve itself.

## 1. Why a unified theory is needed

The prior program developed useful individual mechanisms: a deployment can generate cash and transferable experience; investment can expand an existing configuration or qualify another; hourly contracts can change the relationship between speed and receipts; shared human attention can constrain fleets; manufacturing learning need not pass through to purchaser prices; and raw pick success need not establish complete service. These mechanisms should not remain a collection of unrelated numerical reversals.

The present investigation asks a more general question:

> Which changes in capabilities alter the best economically feasible organization of production, and what does that imply for the value and allocation of learning investment?

A robot becoming able to perform another task can have no immediate operating value. The task may already be covered cheaply, downstream demand may be saturated, or another resource may remain binding. Yet the same capability can become valuable in combination with a different improvement: one robot takes over an existing task, freeing another to move elsewhere, which frees a third to serve previously unmet demand. Conversely, multiple new capabilities can compete for the same scarce machine or the same customer demand.

This is neither a claim that every deployment needs a broad generalist nor a claim that specialization wins. The question is which combination of configurations, qualifications, coordination, and customer opportunities changes the feasible production set at reasonable cost.

The analysis separates three layers:

1. **Operating possibilities:** given qualified configurations, resource availability, and customer conditions, what can be delivered and what contribution can be captured?
2. **Capability acquisition:** which qualifications are produced by adaptation, data, simulation, hardware changes, or organizational investments, at what cost and with what joint uncertainty?
3. **Investment and organization:** who funds those changes, who captures their value, and what alternatives are forgone?

The first two layers are solved in tractable forms below. The third is embedded explicitly in a dynamic research framework, with a solved single-payer investment special case. An organizational equilibrium is not inferred from an operating optimum.

## 2. Economic objects and maintained assumptions

### 2.1 The organizing unit remains the customer production system

Index a service by end market, value-chain stage, operating environment, acceptance standard, place, and time. A task is a component of a service, not a synonym for an entire market. Configuration includes the robot, policy, tooling, integration, retained human work, and relevant operating rights.

A **qualification** is permission to rely on a configuration for a specified service under stated conditions. It is not a benchmark score. Qualification can depend on technical competence, recovery, interoperability, safety, support, and the customer's acceptance procedure. Probabilities below concern whether an investment produces a qualifying configuration. They are not per-cycle field-reliability estimates or a license to relax safety requirements.

A **production recipe** is a complete way of supplying accepted service, including its complementary inputs. When several operations are required for one accepted order, either represent the full recipe or impose the appropriate intermediate-flow and completion constraints. Do not credit each constituent motion as an independently sold final output.

### 2.2 Customer economics and provider value

Let customer output have concave net contribution after its best feasible alternative and relevant retained work are accounted for. The earlier model used quadratic customer revenue and a specified two-part tariff. The present operating core allows piecewise-linear concave contribution schedules, implemented as decreasing marginal-value blocks, or fixed marginal contributions in a bounded operating window.

The weights in the operating objective can represent one provider's capturable contribution under a specified contract, or a deliberately declared joint business surplus. They are not automatically social welfare, gross customer revenue, and provider cash simultaneously. A tariff or contract assumption must justify moving between those measures. Different objectives can produce different economically productive qualification bundles.

Customer growth, market access, output prices, and competing alternatives change the value or amount of demand. The results condition on those customer states when solving the operating problem. They do not assert that demand is exogenous throughout the broader research program.

### 2.3 A fixed-qualification operating problem

Let \(Q\) be the currently qualified recipes. Let \(x_q\geq0\) denote production using recipe \(q\), \(a_q\) its resource requirements, and \(c_q\) its contribution. Let \(b\) collect available resources and relevant demand limits. Define

\[
V_Q(b)=\max_{x\geq0}\left\{\sum_{q\in Q}c_qx_q:\sum_{q\in Q}a_qx_q\leq b\right\}.
\tag{1}
\]

Resource rows can include robot-hours, particular tools, human attention, integration capacity, and demand-block limits. Linear conservation equalities can be included by the usual paired-inequality representation. The results require feasibility, bounded value, and attainment of the relevant primal and dual optima. Retaining the existing production plan remains available when a free additional qualification is introduced.

This is a transparent operating core, not a universal factory model. Nonpreemptive jobs, discrete complete orders, setup sequences, common-mode failures, and hard timing constraints can require integer or stochastic formulations. The dual theorem below is exact for the stated linear program. It must not be silently transferred to an integer formulation with a relaxation gap. The unit-assignment examples also have integral flow optima.

## 3. Resource scarcity determines whether new capability is economically active

### Result 1: A common optimal-price certificate

The dual of (1) is

\[
V_Q(b)=\min_{y\geq0}\{b^Ty:a_q^Ty\geq c_q\ \text{for every }q\in Q\}.
\tag{2}
\]

Let \(Y_Q^*(b)\) be the set of old optimal dual solutions. For a bundle \(S\) of additional recipes,

\[
V_{Q\cup S}(b)=V_Q(b)
\quad\Longleftrightarrow\quad
\exists y\in Y_Q^*(b)\ \text{such that }a_s^Ty\geq c_s\ \forall s\in S.
\tag{3}
\]

**Proof.** If such a vector exists, it is feasible for the enlarged dual at the old value. Weak duality bounds the enlarged primal by that value; retaining the old plan supplies the reverse inequality. Conversely, if the enlarged optimum equals the old one, an attained enlarged optimal dual is feasible for the old problem and has its optimal objective. It therefore belongs to the old optimal face and prices every added recipe. \(\square\)

**Interpretation.** There is no added operating value precisely when one internally consistent set of old scarcity prices can explain why every new recipe fails to beat what its inputs are already worth. A qualification can matter through the resource it releases elsewhere, not just the revenue of the task it directly performs. Zero value in this operating window does not establish zero strategic value after demand or resources change; that requires the continuation problem.

The word **common** is essential. A different old optimal price vector may certify each individual recipe as redundant while no single vector certifies the whole bundle. An arbitrary set of shadow prices returned by one solver basis is not a reliable measure of every capability's value.

### A two-machine example of the distinction

Two unit-capacity machines face two unit demands worth 2 and 1. Initially only machine 1 can serve the higher-value task; machine 0 is idle. Add qualifications \(e_0\), allowing machine 0 to serve the higher-value task, and \(e_1\), allowing machine 1 to serve the lower-value task.

| Qualified additions | Best operating contribution |
|---|---:|
| None | 2 |
| Only \(e_0\) | 2 |
| Only \(e_1\) | 2 |
| Both | 3 |

Old dual optima can be written with machine-0 price zero, low-task demand price zero, and machine-1 price plus high-task demand price equal to 2. To price \(e_0\), the high-task demand price must be at least 2. To price \(e_1\), the machine-1 price must be at least 1. Each restriction can be met separately at objective 2, but not together. The complementarity is not an imposed productivity bonus: it arises from reallocating scarce productive resources.

This is an application of linear-program duality and process-flexibility logic, not a new duality theorem. Its role is to identify the exact economic object that a capability or learning model must change.

### Capacity improvements versus qualification improvements

With fixed \(Q\), \(V_Q(b)\) is nondecreasing in ordinary available resources and concave in \(b\). To prove concavity, mix two feasible production plans: their convex combination is feasible at the corresponding mixed resource vector and delivers the mixed contribution. Qualification additions change the available columns instead of merely changing their right-hand-side capacities. Their value need not have diminishing returns.

Thus buying more of an established configuration and opening a new production recipe are different mathematical changes. Applying the same smooth return-to-capital curve to both can conceal the economics of entry.

## 4. Productive bundles can be arbitrarily larger than individual skills

### Result 2: Complementarity chains of any finite length

For any integer \(k\geq2\), construct \(k\) unit-capacity machines \(r_0,\ldots,r_{k-1}\) and \(k\) unit demands \(t_0,\ldots,t_{k-1}\). Initially, machine \(r_i\) can serve \(t_{i-1}\) for \(i=1,\ldots,k-1\); \(r_0\) is idle. Every currently served task is worth strictly more than the unserved last task, whose contribution is \(W>0\).

The candidate qualifications are \(e_i=(r_i,t_i)\). Every proper subset of these \(k\) qualifications has zero incremental operating value, while the full set increases value by \(W\).

**Proof.** If \(e_i\) is missing, tasks \(t_i,\ldots,t_{k-1}\) have at most \(k-i-1\) neighboring machines. At least one demand must remain unserved. Since all previously served demands have greater value than the final task, the original plan already achieves the highest possible value with at most \(k-1\) accepted units. All \(k\) new qualifications permit the diagonal assignment \(r_i\to t_i\), serving every task and adding exactly \(W\). \(\square\)

The inequalities on incumbent task values are strict; the result does not rely on equal-price ties. Within this unit-capacity construction, it survives an open range of value perturbations. It does rely on the stated demand limits and qualified-edge structure.

### Consequences for research and deployment selection

An improvement to a task already performed by someone else can be economically important because it starts a reassignment chain. Ranking learning projects only by their individual current contribution can miss the entire productive bundle. If each qualification costs \(\epsilon>0\), with \(k\epsilon<W\), a rule that accepts only a positive net one-step improvement stops immediately even though the complete portfolio is profitable.

That counterexample does **not** disprove approximation results for other, properly specified network-design algorithms. Process-flexibility research already studies the mixture of complementary and substitutable links and uses primal-dual methods to guide stronger heuristics. In particular, DeValve, Pekeč, and Wei's cover-modularity work is directly relevant prior art [S2].

There is no universal supermodularity result either. One idle machine and two equally valuable tasks produce value 0 with no qualification, 1 with either qualification, and still only 1 with both. The two capabilities are substitutes because they compete for the same capacity.

**Conclusion:** The economic value of learned capability is generally neither the sum of independent skill values nor a uniformly complementary function. Production topology, demand, and resource availability determine the relevant interaction.

## 5. The production system changes the economic order of technical progress

### 5.1 General qualification outcomes

Let \(E\) be a finite set of candidate qualifications. For each realized successful subset \(S\subseteq E\), solve the operating problem and define

\[
f(S)=V_{Q\cup S}(b)-V_Q(b)\geq0.
\]

We observe which qualifications succeed before choosing the final production allocation. A fixed small investment direction indexed by \(t\downarrow0\) generates independent qualification events with

\[
p_e(t)=\alpha_e t^{\beta_e}+o(t^{\beta_e}),\qquad \alpha_e>0,\ \beta_e>0.
\tag{4}
\]

This is a local mathematical expansion, not an estimated robotics scaling law. It describes acquisition of persistent qualified possibilities, not independent mistakes on successive production cycles. Directions giving zero investment to an edge should exclude that edge from the accessible candidate set.

Define the **economically productive qualification order**

\[
\kappa=\min_{S:f(S)>0}\sum_{e\in S}\beta_e.
\tag{5}
\]

If no accessible subset increases operating value, the gain is identically zero.

### Result 3: Leading economic return

Under (4) and independent qualification events,

\[
\mathbb E[f(S_t)]
=
\left(\sum_{S:f(S)>0,\,\sum_{e\in S}\beta_e=\kappa}
 f(S)\prod_{e\in S}\alpha_e\right)t^\kappa
+o(t^\kappa).
\tag{6}
\]

**Proof.** Expand the expectation over exact realized subsets:

\[
\sum_{S\subseteq E}f(S)\prod_{e\in S}p_e(t)
                         \prod_{e\notin S}[1-p_e(t)].
\]

Terms with zero gain vanish. Every remaining term has leading exponent \(\sum_{e\in S}\beta_e\), because the failure factors converge to one. The finite sum is dominated by its minimum exponent. All associated coefficients are positive, so they do not cancel. \(\square\)

For equal first-order technical acquisition probabilities, \(\beta_e=1\), the economic order is the size of the smallest productive qualification bundle. A three-link chain produces third-order expected economic gain even though every individual qualification probability improves at first order. The result extends beyond linear programs: any finite monotone attainable-value table has the same expansion. Linear production economics is what gives that table an interpretable foundation. The finite-set expansion can also apply to a correctly specified, optimized continuation payoff, provided the same monotonicity and acquisition assumptions hold. That does not identify future value from current operating data.

This is closely related to minimal-path reasoning in system reliability and to production complementarities. The potential research contribution is not the existence of a product of probabilities. It is the connection from **measured, economically valued production opportunities** to the expected returns and sequencing of capability acquisition.

### Result 3a: Demand can change the order, not just the multiplier

Take the three-machine chain with task contributions 3, 2, and 1. The original plan earns 5. Under one unit of demand for each task, all three new qualifications are needed to raise value to 6. If each qualification succeeds with probability \(p\), expected added contribution is exactly \(p^3\).

Now change only demand for the first task from one unit to two. The first new qualification alone lets the idle machine supply a second unit of that service. The incumbent plan still earns 5, and any realized subset containing the first qualification can earn 8. The expected gain is now exactly \(3p\).

The hardware, learning probabilities, candidate skills, and unit contributions did not change. A customer-growth opportunity changed the productive bundle from three qualifications to one.

This is a precise way to connect the customer-demand feedback loop to technical learning. A market with additional demand for an existing service can make a capability commercially useful earlier; a saturated incumbent market may require a longer chain that opens a new service. It does not follow that fast-growing markets always dominate: contract capture, cost, timing, alternatives, and risk still enter the investment decision.

### What the result does not establish

The order in (6) is local, holding the market state fixed. It is not a measured long-run growth exponent. Already positive qualification probabilities, common latent model improvements, qualification retention, or changing demand during training can alter it. Correlation is consequential, as Section 7 shows. The result also concerns gross incremental operating value before acquisition outlays; it does not promise that a high-order program is profitable.

## 6. Diminishing technical returns can produce an economic takeoff threshold

We now solve a particular capability-acquisition problem instead of simply assuming a favorable learning dividend.

Suppose a productive chain requires \(k\) qualifications. Effort \(u_i\geq0\), measured in normalized expenditure units, succeeds in qualifying edge \(i\) with probability

\[
p_i(u_i)=1-\exp[-a_i(z_i+u_i)],
\tag{7}
\]

where \(a_i>0\) describes technical learning effectiveness and \(z_i\geq0\) is prior effective experience. Outcomes are independent conditional on these inputs. The exponential specification is an explicit tractable assumption, not a fit to robot data. All failed effort is paid. Previously qualified production is retained.

### Optimal allocation within a fixed learning budget

Conditional on spending \(R\), maximizing the chance of closing the chain is equivalent to maximizing

\[
\sum_i\log(1-e^{-a_i(z_i+u_i)})\quad\text{subject to }\sum_i u_i\leq R.
\]

Each log term is strictly concave on its positive-probability domain. The first-order/KKT conditions give

\[
u_i^*(\lambda)=\max\left\{0,\frac{\log(1+a_i/\lambda)}{a_i}-z_i\right\},
\qquad \sum_i u_i^*(\lambda)=R.
\tag{8}
\]

The multiplier \(\lambda\) equates the proportional improvement in joint qualification probability across active investments. If an unresolved required edge has zero prior success probability, leaving it entirely unfunded leaves the full-chain success probability at zero. Strong prior experience can shift spending away from that edge toward another bottleneck.

This does not imply that the slowest individual learning curve should always receive all resources. What matters is the marginal improvement to the probability of the **whole productive bundle**, relative to its cost.

### Result 4: Economic S-shape from concave technical learning

For equal \(a_i=a\), zero prior experience, and fixed total effort, (8) gives \(u_i=R/k\). If the full productive bundle is worth \(W\), expected gross gain is

\[
L_k(R)=W(1-e^{-aR/k})^k.
\tag{9}
\]

Every individual technical probability in (7) has diminishing returns. Yet for \(k>1\),

\[
L_k''(R)=\frac{Wa^2}{k}e^{-aR/k}(1-e^{-aR/k})^{k-2}
                 (ke^{-aR/k}-1).
\tag{10}
\]

It is positive for \(0<R<(k/a)\log k\), zero at that boundary, and negative afterward. The production complementarity produces initially increasing economic returns followed by diminishing returns. The result is derived, not imposed through an S-shaped revenue function.

### Investment rather than learning for its own sake

The provider chooses \(0\leq R\leq B\) to maximize

\[
W(1-e^{-aR/k})^k-R,
\tag{11}
\]

including the no-investment alternative. \(B\) is available cash; \(W\) is the provider's incremental contribution from qualified production over the declared horizon. Fixed customer surplus capture and already available production capacity are maintained in this special case. More general alternative uses of cash add their foregone value to the cost, rather than being ignored.

For \(k>1\), let \(x_k>0\) be the unique positive solution of

\[
e^{x_k}=1+kx_k.
\tag{12}
\]

Then the unconstrained minimum reward supporting any strictly positive net gain is

\[
W_c=\frac{(k/a)x_k}{(1-e^{-x_k})^k},\qquad R_c=(k/a)x_k.
\tag{13}
\]

**Proof.** Positive net gain is possible iff \(W>\inf_{R>0}R/(1-e^{-aR/k})^k\). Substitute \(x=aR/k\) and differentiate. The stationary condition is (12). The ratio diverges at both zero and infinity for \(k>1\); strict convexity of \(e^x-1-kx\), its negative initial slope, and eventual positivity imply a unique positive minimizing root. \(\square\)

At \(W=W_c\), doing nothing and spending \(R_c>0\) tie. With sufficient liquidity, the optimal expenditure therefore jumps away from zero as demand-supported reward crosses the threshold. This is not an industry equilibrium phase transition; it is a discontinuous choice in the stated investment problem.

For a finite positive budget,

\[
W_c(B)=\frac{\bar R}{(1-e^{-a\bar R/k})^k},\qquad
\bar R=\min\{B,R_c\}.
\tag{14}
\]

The formula follows because the cost-to-success ratio falls until \(R_c\) and rises afterward. The \(k=1\) case differs: the threshold is the zero-effort limit \(1/a\), and the optimal positive effort approaches zero continuously at entry.

For \(a=1\), the conditional thresholds are:

| Required complementary qualifications | Reward threshold \(W_c\) | Entry effort \(R_c\) |
|---:|---:|---:|
| 1 | 1.0000 | 0 in the limiting entry case |
| 2 | 4.9108 | 2.5129 |
| 3 | 9.2674 | 5.7114 |
| 4 | 14.0356 | 9.3467 |
| 6 | 24.4346 | 17.5098 |

These are normalized model quantities, not dollar estimates. With three requirements and reward 10, an unconstrained optimum spends approximately 6.0511 and earns expected net gain 0.4649. A budget of 4 supports no positive-net program; a budget of 5 supports spending 5 with gain about 0.3366. Lower current operating cash can therefore prevent a promising learning portfolio, but a bigger cash balance alone does not determine its value: the reward and productive qualification structure remain necessary.

### A different technical learning curve

The qualitative mechanism is not unique to exponential qualification. With the also-concave response \(p_i(u)=au/(1+au)\), equal allocation yields \((aR/(k+aR))^k\). Its curvature changes sign at \(R=k(k-1)/(2a)\), and its positive-investment hurdle for \(k>1\) occurs at \(R_c=k(k-1)/a\), with \(W_c=k^{k+1}/[a(k-1)^{k-1}]\). These expressions follow by differentiating the aggregate success function and its cost-to-success ratio. For three requirements and \(a=1\), the reward hurdle is 20.25 rather than approximately 9.27. The local order and nonconvex investment mechanism survive; the numerical threshold is emphatically not robust enough to import into a business case without identifying the learning technology.

### A strong countermodel: observe and retain qualification successes

The batch model commits all allocations before seeing outcomes. A competent alternative works on one required qualification at a time and redirects effort after success. Suppose each qualification's required effort is an independent exponential random variable with rate \(a\). With total effort limit \(R\), completing all \(k\) requirements has probability

\[
P_{\mathrm{seq}}(R)=1-e^{-aR}\sum_{j=0}^{k-1}\frac{(aR)^j}{j!}.
\tag{15}
\]

The batch event that every requirement needs at most \(R/k\) effort implies that their total required effort is at most \(R\). Sequential retention therefore weakly improves success probability at the same maximum expenditure. At small effort, its probability is \((aR)^k/k!+o(R^k)\), compared with \((aR/k)^k+o(R^k)\) under equal precommitment. It improves the coefficient, while preserving the order \(k\) in this model.

With unlimited time and financing, always finishing all requirements has expected expenditure \(k/a\), potentially much less than the batch break-even reward. The comparison is not yet a net-value optimum: a rational firm may abandon after spending without enough progress. We now solve that stronger alternative for a homogeneous qualification chain, and establish a more general gross-return bound.

### Result 6a: Adaptive learning preserves the minimal productive order under bounded independent acquisitions

Let \(E\) be a finite collection of missing qualifications and \(f(S)\) the incremental operating value after acquiring subset \(S\). Assume \(f\) is monotone, \(f(\varnothing)=0\), and at least one subset has positive value. Define

\[
m=\min\{|S|:f(S)>0\}.
\tag{15a}
\]

Each qualification \(e\) requires an independent exponential amount of effort with known rate \(a_e\in(0,\infty)\). Success is observed and retained. At most one total unit of effort can be deployed per unit of the effort clock, but the policy may divide it or switch targets adaptively. There are no joint acquisition events, no free initially qualified requirements, and no change in customer demand during this experiment. Let \(G^*(B)\) be the greatest expected gross incremental operating value attainable with pathwise expenditure at most \(B\). Then

\[
G^*(B)=\Theta(B^m)\quad\text{as }B\downarrow0.
\tag{15b}
\]

**Upper-bound proof.** The instantaneous intensity of new qualification successes under any admissible allocation is at most \(a_{\max}=\max_e a_e\). By adding dummy events, the real acquisition counting process is dominated by a Poisson process of rate \(a_{\max}\) on the effort clock. A positive payoff requires at least \(m\) acquisitions. Since \(f(S)\leq f(E)\),

\[
G^*(B)\leq f(E)\Pr\{\operatorname{Pois}(a_{\max}B)\geq m\}
             =O(B^m).
\]

The bound applies to adaptive targeting because the intensity cap holds conditional on every history. It would not apply unchanged if a single event qualified several edges or if the total effort rate were unbounded.

**Lower-bound proof.** Choose a minimum-size productive subset \(S^*\) and work sequentially on its \(m\) requirements, stopping on completion or when expenditure reaches \(B\). For independent exponential requirements \(T_e\),

\[
\Pr\left\{\sum_{e\in S^*}T_e\leq B\right\}
 =\frac{B^m}{m!}\prod_{e\in S^*}a_e+O(B^{m+1}).
\]

This follows by integrating the joint density over the positive simplex of volume \(B^m/m!\); the exponential density is uniformly its value at zero plus \(O(B)\) on that simplex. Completion produces \(f(S^*)>0\), proving a positive lower bound of order \(B^m\). Combining the bounds proves (15b). \(\square\)

Thus adaptivity can improve the coefficient and the financing policy without reducing the minimum number of independently acquired qualifications needed for operating value. This is a **gross-value asymptotic**, not a claim that net value equals gross value minus the entire expenditure limit: the optimal policy may spend less than its limit in many realizations. The bounds also do not identify the exact optimal leading coefficient on an arbitrary graph.

### Result 6b: The cost-aware sequential chain has a recursive stopping solution

Suppose all \(k\) missing qualifications are necessary for incremental payoff \(W\), every acquisition has the same known rate \(a\) per unit of paid effort, and the firm can observe and retain successes. Cost accrues at one per unit of actual effort. The firm can stop at any time, total realized expenditure cannot exceed its available budget, and there is no calendar discount, borrowing, demand change, or payoff from incomplete chains.

Let \(J_m(b)\) be the maximum expected remaining payoff minus future expenditure when \(m\) requirements remain and remaining budget is \(b\). Then

\[
J_0(b)=W,\qquad J_m(0)=0,\qquad
J_m'(b)=\big[a(J_{m-1}(b)-J_m(b))-1\big]_+.
\tag{15c}
\]

**Derivation and verification.** While effort is active, a success arrives at rate \(a\), reducing the number of missing qualifications by one. An unsuccessful effort increment consumes budget without changing that state. First-step dynamic programming gives the active equation \(J_m'=a(J_{m-1}-J_m)-1\). Stopping is always available at value zero. The triangular system in (15c), with the solution described below, has a zero stopping region and a positive continuation region. Along any active policy, the drift of the candidate value minus accumulated cost is

\[
-1-J_m'(b)+a[J_{m-1}(b)-J_m(b)]\leq0.
\]

It is zero in the continuation region. At a stopping state the candidate equals the available zero payoff, and at completion it equals \(W\). Integrating this bounded-expenditure verification inequality shows that no policy earns more than \(J_m\); continuing in the positive region and stopping otherwise attains it. Equal rates mean allocating active effort to any unfinished qualification has the same transition rate; retaining successes prevents effort from being wasted on already completed requirements.

If \(aW\leq m\), then \(J_m(b)=0\) for every budget: even unlimited funding cannot make the remaining chain profitable. For \(aW>m\), there is a unique threshold \(t_m\), with \(t_1=0\) and, for \(m>1\),

\[
J_{m-1}(t_m)=1/a.
\]

The optimal value is zero at and below \(t_m\); above it,

\[
J_m(b)=\int_{t_m}^{b}e^{-a(b-s)}[aJ_{m-1}(s)-1]ds.
\tag{15d}
\]

The first state is \(J_1(b)=(W-1/a)(1-e^{-ab})\) when \(aW>1\). Induction establishes monotonicity, uniqueness of the threshold, and \(\lim_{b\to\infty}J_m(b)=W-m/a\). For the zero-value case, the induction bound \(J_{m-1}(b)\leq\max(0,W-(m-1)/a)\) keeps the active marginal return nonpositive. For the positive case, the preceding state's strictly increasing value eventually exceeds \(1/a\). The integral is positive after that crossing, with positive derivative, and solves the active equation. This is a recursive solution of the stated model, not an unrestricted solution to R&D budgeting.

For reproduction, set \(\tau=ab\), \(v=aW\), and \(j_m=aJ_m\). On its continuation interval the solution has the form

\[
j_m(\tau)=(v-m)+e^{-\tau}P_m(\tau),
\]

where \(P_1=-(v-1)\) and \(P_m' = P_{m-1}\); its integration constant makes \(j_m\) vanish at its threshold. The code evaluates these exponential-polynomial pieces and separately calculates completion probability and expected expenditure. An independent numerical Bellman-ODE solution checks the recursive implementation.

**A consequential counterexample to the batch investment conclusion.** Set \(k=3\), \(W=10\), \(a=1\). In the batch model, a maximum budget of 1 yields no profitable investment. The optimal sequential policy starts investing when available budget exceeds approximately **0.727164**, not the much larger batch hurdle. At a budget of 1, its completion probability is approximately 0.051009 and its expected actual expenditure is 0.415656, yielding expected net gain approximately **0.094432**. At budget 4 its expected gain is approximately 4.983610; with very large available budget it approaches 7. These numbers are synthetic consequences of the model, not expected robotics returns.

The distinction is substantive. The maximum amount one must be able to fund is not the amount paid in every realization. Successful qualifications are retained; disappointing paths can be abandoned before all funds are spent. **The large committed-expenditure hurdle is therefore not robust to a competent adaptive policy.** The positive low-budget stopping region and the gross minimal-acquisition order do survive in this setting. What does not yet follow is the optimal policy on a heterogeneous production graph with partially valuable intermediate qualifications, learning spillovers, changing customer opportunities, multiple payers, or calendar deadlines. Those are the next economic questions, not results claimed here.

## 7. Shared learning can help or hurt: the sign comes from the production system

Independent acquisition is not innocuous. A common model, dataset, or hardware redesign may improve several qualifications together. Shared latent weaknesses may also correlate them. Neither positive nor negative correlation is universally economically preferable.

### Result 5: Exact dependence decomposition for two qualifications

Write operating values as \(V_0,V_1,V_2,V_{12}\). Let marginal qualification probabilities be \(p_1,p_2\), and the probability of joint qualification be \(q\). Then

\[
\mathbb E[V]=V_0+(V_1-V_0)p_1+(V_2-V_0)p_2+\Gamma q,
\quad
\Gamma=V_{12}-V_1-V_2+V_0.
\tag{16}
\]

**Proof.** Weight the four possible qualification subsets by \(1-p_1-p_2+q\), \(p_1-q\), \(p_2-q\), and \(q\), then collect terms. Feasibility requires \(\max(0,p_1+p_2-1)\leq q\leq\min(p_1,p_2)\). \(\square\)

When \(\Gamma>0\), more joint success raises expected operating value at fixed individual learning performance. When \(\Gamma<0\), it lowers value. The same technical marginal evaluations can therefore favor different learning architectures depending on the production network.

For the two-link complementarity chain, both individual gains are zero and the joint gain is 1. With marginal qualification probabilities 0.2, expected gain is 0.04 under independence, 0.2 under perfect positive dependence, and 0 under the feasible zero-joint-success distribution. For one machine facing two substitutable unit-value tasks, the corresponding gains are 0.36, 0.2, and 0.4.

This is not a claim that a shared foundation model empirically produces beneficial correlation. It shows what must be measured: the joint qualified capability outcomes and the economic interaction \(\Gamma\). Marginal benchmark averages alone do not identify the economic comparison.

Perfectly shared qualification progress can also overturn the independent-return order in Section 5. If all \(k\) requirements qualify together with probability \(p\), the complementarity-chain gain is \(Wp\), not \(Wp^k\). An empirical test of the critical-order mechanism must therefore distinguish independently acquired skills from shared learning events. The result cannot be manufactured by splitting one capability into several labels: an exact recoding preserves the joint outcome law and economic value, whereas pretending the new labels are independent changes the technology being modeled. Operational common-mode failure during production is a separate stochastic object from persistent joint qualification after development.

### Result 7: Joint qualification programs and economically productive intermediate states

The independent edge-acquisition model and homogeneous terminal-only chain are useful benchmarks, but neither identifies a full-stack qualification event nor the value of intermediate **accepted services**. We now treat the persistent qualification state as a finite set \(S\) with optimized operating value \(f_\theta(S)\). An admissible learning program \(j\) is a distinct observable event with intensity \(\lambda_j>0\) that adds a typed subset \(A_j\) of qualifications, after which the operator can adapt and retain all successes. One unit of effort costs one cash unit and the pathwise paid-effort budget is \(b\).

The Bellman value \(H_S(b)\), including a free option to stop and retain \(f(S)\), satisfies

\[
H'_S(b)=\Big[\max_{j:S\cup A_j\ne S}
\{\lambda_j(H_{S\cup A_j}(b)-H_S(b))-1\}\Big]_+,\qquad H_S(0)=f(S).
\tag{18}
\]

This is an established finite-state jump-control equation, not a novel stochastic-control theorem. The detailed derivation, verification, counterexample, independent numerical baseline and observational protocol appear in [Joint qualification and intermediate productive states](JOINT_EVENTS_AND_PARTIAL_VALUE.md). Two useful consequences connect directly to the earlier results.

**First, the economic small-effort order counts actual acquisition events rather than arbitrary skill labels.** With bounded program success intensities and free acquisition effort, the leading gross incremental value has order \(b^m\), where \(m\) is the minimum number of admissible qualification **success events** on a path that increases \(f(S)\). This extends Result 6a to a genuine joint event. A shared successful program that validates two distinguishable capabilities simultaneously can lower \(m\), while a partially productive intermediate state can do the same even when full order acceptance still requires both qualifications. The proof uses Poisson counting-process domination for the upper bound and a sequential waiting-time simplex for the lower bound. Neither argument licenses pretending one physical qualification was two independent events.

**Second, neither targeted staged learning nor joint full-stack learning necessarily dominates.** Let targeted A and B qualification have rate \(a\) each, while one joint program acquiring both has rate \(\mu\). Suppose the optimized incremental accepted-service value of the four states is \((0,v,0,W)\) for \(\varnothing,\{A\},\{B\},\{A,B\}\), with \(W\ge v\). If \(av>\mu W>1\), \(a/2<\mu<a\), and \(v<W-1/a\), targeting A is strictly optimal at sufficiently small available budget, but the joint program is optimal at sufficiently large budget. The short-budget marginal benefits are \(av-1\) versus \(\mu W-1\); with unlimited budget, targeted sequential acquisition returns \(W-2/a\), while joint acquisition returns \(W-1/\mu\). This reversal survives an optimized adaptive response after successes and does not depend on requiring both qualifications to be worthless individually. The illustrative parameters \(a=2,\mu=6/5,v=7,W=10\) are **synthetic**; the Bellman solution chooses targeted A at \(b=.05\), joint acquisition at \(b=4\).

The source-based empirical anchor is narrow. DHL's **May 13, 2025** statement distinguishes commercially deployed Stretch unloading (introduced in North America in **2023**) from case picking as a development priority. Boston Dynamics' later published case-picking description advertises complete palletized order building and WMS integration via Orbit. Neither release identifies a site's actual accepted order, contractual payment, source-to-target qualification unit, or acquisition hazard. See the companion evidence protocol before interpreting A and B as real independently validated capabilities.

The theoretical point is not to declare robots generalist or specialized by architecture. It is to locate **which acquisition events actually create useful, retained production options**, which intermediate options already earn customer/provider value, and how finite payer liquidity changes the preferred route. Event-level success laws and economic state values are distinct empirical objects. The next challenge is date-dependent demand and the distinction between a valuable operating state that is only realized *after* research stops and one that produces cash *during* the program.

## 8. Connecting back to the full research roadmap

The framework is meant to integrate—not replace—the broader agenda.

| Research dimension | Formal location in the unified framework | What remains to be learned |
|---|---|---|
| Customer demand and value-chain economics | Demand limits, contribution blocks, customer alternatives, and state-dependent \(W\) | Joint arrival/output data, competition, customer ability to pay and actual capture |
| Embodiment and hardware redesign | New recipes/edges, resource requirements \(a_q\), and available capacity \(b\) | Real qualification cost, lead time, reliability, switching and support |
| Manufacturing and suppliers | Cost and timing of acquiring \(b\); who captures manufacturing learning | Cohort production costs, yield, component constraints, contract pass-through |
| Field data, teleoperation, simulation | Qualification acquisition probabilities, correlated outcomes, and transitions in prior experience | Transfer at a matched acceptance standard, total adaptation cost, usable rights |
| Digital intelligence and coordination | Routing within qualified edges; changes in attention, integration, and information constraints | Whether software removes a binding constraint or merely changes reports |
| Organizational boundaries | Which recipes can be assembled across actors, contracts and data rights | Gains from contracting versus ownership; no automatic integration inference |
| Heterogeneous cash deployment | Funding feasible acquisition portfolios, foregone incumbent investment, and liquidity path | Timed receipts, credible pilot contracts, restricted cash, financing eligibility |
| Topological empirics | Qualified graph, complete-service recipes, critical bundles, and joint demand | Observed versus hypothetical edges; granularity and source consistency |

The competence/coordination distinction in *Organizing Intelligence* remains important [S4]. Our additional object is the topology of qualified combinations and shared resource requirements: a scalar competence increase or coordination parameter alone need not identify whether a valuable production plan becomes feasible. No claim is made that the source paper omits all network complementarities, or that physical equipment can be replicated at the cost of copying software.

### A dynamic embedding—not an already solved equilibrium

A research state can be written as

\[
s_t=(Q_t,b_t,z_t,\theta_t,\pi_t,\{B_{a,t}\},\mathcal R_t),
\]

collecting qualifications, physical/organizational resources, experience, customer state, beliefs, payer-specific cash, and rights. Actions choose deployments, production, learning, manufacturing, hardware, coordination, experiments, and contracts. A finite-horizon value function is

\[
\mathcal V_t(s)=\max_{u\in\mathcal A(s)}
 \{\text{net distributable cash}_t(u)+\delta\mathbb E[\mathcal V_{t+1}(T(s,u,\xi))]\},
\tag{17}
\]

with terminal assets and remaining obligations specified. An alternative terminal-wealth formulation must not also count retained operating cash as already distributed dividends. Future learning value belongs in the continuation value, not in an additional arbitrary data premium.

Every legal payer retains a dated budget: opening cash plus actual collections and permitted finance must cover its own operating and investment payments. Internal transfers cancel in consolidated resource cost but can alter financeability. The operating theorems remain useful conditional on a state; they do not solve decentralization, bargaining, or competition in (17).

Productive deployments can change \(Q\) through experience, \(b\) through reinvestment, \(\theta\) through customer development or induced output, and rights through contracts. This creates the feedback the user requested: demand shapes deployment; deployment changes knowledge and cash; investments change qualified possibilities; those possibilities change customer economics and subsequent demand.

Free, optional additional capability cannot reduce optimized value when the old policies, rights, costs, and opportunities remain feasible. That statement follows by retaining the old strategy. Costly learning, lost support rights, mandatory migration, or reduced market prices are different state changes and should not be smuggled into a supposedly free technical improvement.

### Productive teleoperation and information before the next investment

The data-generating action is now a controlled production choice. A teleoperated job may supply accepted service, create training/grounding observations, and reveal whether source experience can be reused. Its current contribution and its single optimized continuation value enter (17). A measured technical gain does not by itself establish net economic value; a diagnostic can instead have decision value without immediately improving the policy. [The full continuation](data_value/TELEOPERATION_DATA_VALUE.md) derives this distinction within the same operating account, using the specified Farboodi-Koh-Xia paper and primary interactive robot-learning sources.

For two stationary capacity slots, let source collection sacrifice \(k_S\) of current contribution and target grounding sacrifice \(k_G\), each relative to a competent routine activity. Both batches are financeable at their dates, their physical effects commute, and there is no discounting within the two-slot window. Let \(F_\Theta(x,g)\) be terminal production value conditional on the transfer regime and the two acquired batches, with retained alternatives and final qualification observed before service. Source collection is uninformative before the next decision; grounding reveals \(Z\). Put
\[
B_S=-k_S+\mathbb E[F_\Theta(1,0)-F_\Theta(0,0)],\quad
B_G=-k_G+\mathbb E[F_\Theta(0,1)-F_\Theta(0,0)],
\]
and \(M(Z)=\mathbb E[F_\Theta(1,1)-F_\Theta(0,1)\mid Z]\). The exact best incremental value in this two-batch menu is
\[
\max\{0,\ B_S,\ B_G+\mathbb E[(M(Z)-k_S)_+]\}.
\tag{19}
\]
The proof exhausts all feasible plans: source alone is one option, while grounding first permits buying the source only when its posterior gain exceeds its opportunity cost. That adaptive route weakly dominates a precommitted pair, but it need not beat source alone or routine production. This is standard conditional optimization, not a claimed new information theorem.

Equation (19) allows arbitrary terminal production effects and useful partial learning. A rational noisy-transfer example makes a currently loss-making grounding job optimal because it avoids subsequent collection after an unfavorable report; a second formulation using the preceding Gaussian information model preserves the information advantage. A stronger specialist defeats that policy, and an expiring source opportunity reverses the preferred order. If routine production already supplies the same useful source batch without forgone contribution, \(k_S=0\) and optional-use monotonicity makes the acquisition-timing premium exactly zero. Those counterexamples locate the result in the actual customer/resource calendar and require a genuine incremental cost for the relevant data. A shared qualification law is valued directly rather than multiplying marginal scores. The implication for the coherent argument is that production determines both *which data exist* and *when the enterprise learns which additional data are worth acquiring*.

## 9. An empirical program that can distinguish the mechanisms

This investigation produces a measurement design, not a new empirical robot-performance estimate. The older issuer case dossiers remain useful background but do not identify the new coefficients.

### 9.1 Observe economically meaningful edges

For a fixed site and service window, record each configuration's accepted task/service eligibility, physical capacity, attention and switching requirements, and the customer's demand and feasible alternative. Separate demonstrated, qualified, deployed, supported, and billable capability. Record the unit and configuration version attached to each claim.

A production-flow diagram should identify the real alternative assignments, not just arrows suggesting that tasks are similar. On the customer side, distinguish demand for additional units of the existing service from access to a new service or value-chain position. The theory predicts those can produce different productive qualification orders.

### 9.2 Estimate interactions, not only individual learning curves

For a candidate two-capability set, compare the same production system with neither qualification, each separately, and both. The economically relevant interaction is the difference-in-differences \(\Gamma\) in (16), after reoptimizing competent operating alternatives. This is a definition of the counterfactual object, not proof that an observational difference-in-differences design is causally identified.

Separately evaluate how a shared or separate training treatment changes the joint distribution of qualified outcomes at a fixed acceptance standard. Hold out evaluation data and distinguish adaptation, validation, hardware changes, and operator learning. Repeated seeds, configurations, and target contexts may be needed to distinguish marginal success changes from dependence changes. Do not use the same trials to train and claim independent validation.

### 9.3 Use decisive negative controls

* If there is no unmet or economically valuable demand reachable by an augmented allocation, better qualification should not generate operating value through this mechanism.
* If spare capacity can already reach the target without the purported critical chain, the chain characterization is wrong or incomplete.
* If an ordinary human/fixture/software alternative supplies the missing reassignment more cheaply, it belongs in the baseline and can eliminate the proposed premium.
* If learning outcomes are strongly coupled, the independent exponent should fail; test dependence rather than relabel the discrepancy as noise.
* If indivisible accepted orders or switching delays create an LP relaxation gap, do not treat the fluid optimum as implementable output.
* If the customer can absorb more incumbent service, a previously redundant edge may become individually valuable. This is a predicted change in mechanism, not a failed technical transfer experiment.

### 9.4 Separate technological identification from commercial adoption

Observe qualification effort, total failures, customer receipts, integration and support payments, and pre-decision financing separately. A provider may decline a technologically useful portfolio because it cannot capture enough of the value or cannot fund it before receipts arrive. Conversely, a large financing round is not evidence of successful transfer or profitable order-level performance.

Sector input-output tables can locate broad supply relationships but cannot fill missing qualified-edge, service-timing, or learning-outcome records. The official numeric backbone remains a retained project requirement, not something this theory document pretends to have completed.

### 9.5 Distinguish assisted output, learned capability, and transfer diagnosis

The teleoperation continuation adds a source-grounded measurement slice and a discriminating design. Measure autonomous evaluation separately from service delivered with a human in the loop; include failures, resets and monitoring in the cost account. A controlled training-data inclusion comparison targets physical learning. A separate early-versus-late release of a transfer diagnostic, under the same initial grounding and operational safety permissions, targets whether information changes the next acquisition decision. Record joint qualification outcomes, source availability, customer expiration dates and a genuine specialist option. A report that predicts nothing about source usefulness, arrives after commitment, or cannot alter the acquisition decision cannot support this mechanism. [Evidence and design](data_value/TELEOPERATION_DATA_VALUE.md#8-empirical-connection-what-has-actually-been-observed); the proposed robotics experiment has not been run.

## 10. Closest literature and contribution discipline

**Process flexibility.** Jordan and Graves (1995) already establish the importance of appropriately connected limited flexibility and chaining [S1]. A path of reallocations is not new merely because the machines are robots.

**Network-design complementarity.** DeValve, Pekeč, and Wei (2023) develop a primal-dual account of flexibility design and cover modularity [S2]. We inspected the primary publisher abstract and author bibliography, not the full proof archive. Our elementary common-certificate argument is derived here from strong duality; we do not claim it precedes or improves their algorithms. The failure of a stop-on-nonpositive-singleton rule does not refute their stronger guarantees.

**O-ring complementarities.** Kremer (1993) models multiplicative task-quality effects and explicitly studies endogenous skill investment [S3]. The product form and complementarity-to-increasing-returns connection are established ideas. We checked the production-function definition and independence assumption on printed page 553, rather than treating the whole paper as replicated.

**Organization of intelligence.** Imas, Koh, and Legg (2026) distinguish competence from coordination and endogenize organizational composition and scale [S4]. We use that distinction and reconstruct a different fixed-service qualification/operating boundary; their equilibrium conclusions are not imported into a physical fleet.

**Optimization foundations.** Linear duality, sensitivity, and concave optimization provide the mathematical tools [S5]. The proofs in this document are self-contained applications, not new optimization theorems.

**Sequential R&D budgeting.** Dutta (1997) studies budget allocation across research stages, including the terminal-only reward case [S6]. Roberts and Weitzman develop sequential funding criteria that account for revisable decisions [S7]. We inspected primary abstract records, not their complete model proofs. Optimal budget allocation, the ability to stop, and the value of retaining development progress therefore cannot themselves be advertised as new contributions. Our recursive homogeneous example is a transparent comparator within that established family; a stronger contribution must explain the economically measured qualification network and its changes.

**Data production and interactive robot learning.** The specified *Data-Driven Automation* paper already supplies production-generated data, directed transfer and forward-looking data value. Interactive imitation-learning research already studies policy-induced state distributions and costly human intervention. The candidate synthesis here links those mechanisms to accepted production, uncertain transfer interfaces and the timing of heterogeneous acquisition decisions. Source-reading boundaries and the elementary nature of the Bayesian/optimization tools are explicit in the [teleoperation chapter](data_value/TELEOPERATION_DATA_VALUE.md#sources-and-reading-boundaries); no publication-novelty judgment follows from (19).

### Candidate contribution worth developing

The strongest candidate is a **measurement-linked theory of the economic returns to capability acquisition**: identify productive qualification bundles from a customer's real production alternatives; characterize how they transform technical learning into commercial value; and test whether changes in demand, coordination, or shared learning alter that transformation.

The candidate is not yet an established publishable contribution. The general leading-order result is elementary once the attainable-value function is given, and it is related to reliability-network arguments. Its significance would come from a convincing economic specification, a useful dynamic or organizational extension, and discriminating evidence. This is a reason to deepen the coherent argument—not to resume an endless sequence of isolated novelty disclaimers.

## 11. Adversarial verification and limits

The research kernel checks integer operating values exactly using rational arithmetic. It examines all 512 three-by-three eligibility graphs and all 19,683 assignments of their nine possible edges to old, candidate, or absent status for the critical-order comparison. These are combinatorial cases, not empirical observations.

One hundred twenty seeded graph comparisons test common-dual feasibility against independent exact allocation. Additional tests check continuous-capacity concavity, heterogeneous learning KKT conditions against a separate scalar optimizer, derivative signs and numerical derivatives, global investment optima against dense grids, correlation counterexamples, and sequential-retention alternatives. Forty-two scoped tests pass, including a different concave technical learning curve, general finite-state adaptive gross-value equations, and the optimal retained-success stopping policy checked against an independent Bellman-ODE implementation. The expected-payoff identity reconciles reward times completion probability minus actual expected expenditure, and funding remains a pathwise maximum rather than an assumed expenditure. Numerical LP checks use tolerances; symbolic proofs establish the stated general results. Neither test counts nor exhaustive small instances prove claims about all production systems.

The model deliberately excludes a full industrial equilibrium, endogenous contracting, unobserved safety constraints, estimated robot learning curves, and complete-order integer scheduling outside the identified special cases. One explicit counterexample shows a linear recipe relaxation worth 1.5 when the indivisible implementation can deliver only 1. Such gaps are a boundary to enforce, not a rounding nuisance.

No independent peer review, real robot execution, complete empirical atlas, or full historical repository CI is claimed. The scheduled research process executes only during actual supported runs. Earlier unpublished Q10 work and the inaccessible older Codex workspace have not been recovered by writing this manuscript.

## 12. Sustained next investigation

Continue this same theory block across sessions instead of inventing another numbered toy at each run. The independent adaptive gross-order bound, homogeneous-chain stopping problem, dated production/finance extensions, and endogenous-grounding continuation are retained. The immediate proof gap is now **how the intervention rule and visited-state distribution determine the information and transferable learning generated by productive teleoperation**. The current two-batch theorem solves acquisition conditional on a signal law; it does not derive that law. Determine when higher source autonomy reduces target-relevant corrective observations, and whether deliberate probes, simulation, coordination or a different embodiment repair the resulting information gap. Keep demand timing, qualified service, competent specialist alternatives and one continuation account. Do not rederive the solved signal-value example or revert to financing as the default next question.

In parallel, translate one existing workflow dossier into an explicit accepted-service allocation graph with a competent nonrobotic or mixed-system alternative. That is the minimum empirical bridge needed to test whether the critical bundles exist outside our examples. Preserve manufacturing, payer contracts, and hardware redesign as choices that can change the graph or the cost of reaching it.

At the next synthesis gate, decide whether the argument supports the first paper, supplies a major section of it, or points toward a different contribution. The November 22/29 and December 6/13/18/23/24/25 milestones remain. No date is treated as evidence of scientific completion.

## References and source-reading boundaries

[S1] William C. Jordan and Stephen C. Graves (1995), *Principles on the Benefits of Manufacturing Process Flexibility*, Management Science 41(4), 577–594. DOI: 10.1287/mnsc.41.4.577. Primary publisher abstract inspected November 17, 2026. https://pubsonline.informs.org/doi/abs/10.1287/mnsc.41.4.577

[S2] Levi DeValve, Saša Pekeč, and Yehua Wei (2023; online 2022), *Approximate Submodularity in Network Design Problems*, Operations Research 71(4), 1021–1039. DOI: 10.1287/opre.2022.2408. Primary publisher abstract and author publications page inspected November 17, 2026; complete proof archive not replicated. https://pubsonline.informs.org/doi/10.1287/opre.2022.2408 ; https://people.duke.edu/~yw118/publications.html

[S3] Michael Kremer (1993), *The O-Ring Theory of Economic Development*, Quarterly Journal of Economics 108(3), 551–575. DOI: 10.2307/2118400. Primary article, introductory mechanism and printed page 553 inspected, including screenshot; no full equilibrium replication. https://www.isid.ac.in/~tridip/Teaching/DevEco/Readings/03Expectations/02Kremer-QJE1993.pdf

[S4] Alex Imas, Andrew Koh, and Shane Legg (2026), *Organizing Intelligence*, October 29 version. Abstract and early illustrative model, including printed page 4, inspected and visually checked November 17, 2026. https://storage.googleapis.com/deepmind-media/papers/organizing-intelligence.pdf

[S5] Stephen Boyd and Lieven Vandenberghe, *Convex Optimization*, Cambridge University Press; author-hosted book resource. Author page inspected November 17, 2026. General optimization reference; no claim to have newly read the entire book. https://web.stanford.edu/~boyd/cvxbook/


[S6] Prajit K. Dutta (1997), *Optimal management of an R&D budget*, Journal of Economic Dynamics and Control 21(2–3), 575–602. DOI: 10.1016/S0165-1889(96)00945-1. Primary publisher abstract retrieved through indexed search November 17, 2026; direct full-page fetch returned 403 and was not retried. No full theorem replication. https://www.sciencedirect.com/science/article/pii/S0165188996009451

[S7] Kevin W. S. Roberts and Martin L. Weitzman, *Funding criteria for research, development, and exploration projects*, MIT Energy Laboratory report MIT-EL-79-009, April 1979; later Econometrica article (1981). MIT primary repository abstract inspected November 17, 2026; no full-paper replication in this session. https://dspace.mit.edu/entities/publication/33bd2a42-b38b-4aa3-beaa-33574292681a


---

## Result 8 — calendar production during learning changes the economic ranking

The predecessor Results 6–7 made learning effort a budget and operating value a reward available upon stopping. Actual robotic services can instead generate accepted output and **collected** provider cash while another qualification is pursued, subject to hardware/supervisor separation, customer demand and contract/receipt dates. The [full derivation](CALENDAR_FINANCE_CONTINUATION.md) now embeds the retained capability graph in a finite calendar-time jump-control model, where qualified service S earns net receipts r_t(S) while a program j has intensity lambda_j, pays effort cost c_j and adds a typed retained qualification bundle. Its standard Bellman equation is
\[
-\partial_t J_t(S)=r_t(S)+\max\{0,\max_j[\lambda_j(J_t(S\cup A_j)-J_t(S))-c_j]\},\quad J_T=0.
\]
The zero action stops *development*, not already-paid service. This is an unconstrained valuation, **not** a valid cash-feasible policy by itself.

**Proposition (finite-calendar rank reversal).** In the four-state A,B,AB model with intermediate flow v, completed flow W>v, targeted exponential rates a for A and B, genuine joint event rate mu, and running cost c, fixed A-then-B and joint policies have exact value difference
\[
V_{\rm seq}-V_{\rm joint}=\frac{av-\mu(W+c)}2T^2+O(T^3),\qquad
\lim_{T\to\infty}(V_{\rm seq}-V_{\rm joint})=v/a+(W+c)(1/\mu-2/a).
\]
If a/2<mu<a and (W+c)(2-a/mu)<v<(mu/a)(W+c) with v<W, joint acquisition beats the staged route at short positive calendars, but staged acquisition wins at long calendars. This can occur *without a funding constraint* and therefore does not contradict the earlier short-*budget* targeting/long-*budget* joint result: these are different economic environments. Under the fully adaptive stopping/switching benchmark with synthetic a=2,mu=1.2,v=4.5,W=10,c=1, the optimal initial action is **stop** for T=.02, **joint AB** for T=.5 and **target A** for T=2 (independently computed numerical policy checks, no claimed exact switch time). Long-horizon policy optimality follows from the stochastic shortest-path lost-flow recursion D(A)=(W-v+c)/a, D(B)=(W+c)/a and D(0)=min{(W+c)/mu,(W+c)/a+D(A),(W+c)/a+D(B)}; in this example D(0)=8.75 through A, versus 55/6 by the joint route.

**Financeability is a different constraint.** For deterministic dated cash flows, the minimum initial amount needed to execute a path without borrowing is the maximum cumulative **collected-receipts-adjusted** cash deficit. In a stochastic bridge example, an A success before initial cash exhaustion, followed by contemporaneous A collections at rate v>=c while B is trained, permits AB completion probability \(\int_0^{\min(T,B/c)}ae^{-as}(1-e^{-b(T-s)})ds\). A financed joint program instead has success probability \(1-e^{-\mu\min(T,(B+L)/c)}\). An advance L is liquidity/repayment obligation, not an increment to productive surplus. Actual invoice delay, service displacement, customer co-investment and supplier rights can undo the self-funding mechanism. The [source/evidence ledger](CALENDAR_EVIDENCE.md) separates DHL's operational co-development, Formic's monthly contract description, and Cardinal's proposed financing business model from measured qualification events or cash. Standard staged R&D funding, process flexibility and working-capital concepts are prior art, not newly invented theorems.

This result deepens the same core argument: economically active capabilities are those which change **accepted production and the dates when specific actors can fund their next acquisition**. The model remains synthetic and the full paper contribution is not selected. Next derive a stochastic cash-state/delayed-collection and enforceable financed-pilot extension of this precise environment; do not append a disconnected toy. [Code](calendar_model.mjs), [scoped test script](test_calendar_model.mjs), [exercise](CALENDAR_TEACHBACK.md) and [separate solutions](CALENDAR_SOLUTIONS.md).


## Result 9 — receivable maturity and learning's shared productive resource

[Full integrated theorem and proof](RECEIVABLE_LAG_THEORY.md) · [Python analytic core](core_receivables.py) · [scoped tests](test_core_receivables.py) · [evidence](RECEIVABLE_EVIDENCE.md) · [separate exercises](RECEIVABLE_TEACHBACK.md) and [solutions](RECEIVABLE_SOLUTIONS.md).

Result 8 assumed a qualified intermediate service A earned *collected* net cash immediately and continued production without interruption during B qualification. The corrected setting uses learning effort u(t), cost c u(t), B success hazard b u(t), net accepted A cash earning v[1-(1-eta)u(t)], invoice collection delay d and date-zero available cash K. The no-success cash identity is C(t)=K-c int_0^t u + v int_0^(t-d)+[1-(1-eta)u] >=0. Booked A revenue cannot fund B before collection absent separate contract or credit rights.

When A production is independent of B trials (eta=1) and B can be paused without losing retained progress, **exact cumulative qualifying effort** before horizon h is E*=min{h,K/c+min(1,v/c)(h-d)+}. A fluid learn–pause–collect–resume policy attains this bound. In a stated synthetic example, allowing pause raises lag-one two-stage completion probability from .264241 (noninterruptible) to .546572, versus .613805 without lag. The earlier continuous-investment cash-shortfall argument is therefore not a competent universal benchmark.

When B learning uses the same productive asset or scarce supervisory resource as A service, a resource-conservation proof yields long-run duty share min{1,v/[c+v(1-eta)]}. With eta=0, an unbounded sequence of learning cannot run at full effort while remaining wholly self-funded by the work it displaces. Finite up-front debt changes a transient funding need, not the asymptotic physical constraint. The same qualification graph can therefore be reachable through separate machines or coordination and unreachable at the same cost through a single shared machine.

A narrow risk-neutral revenue-pledge test distinguishes the minimum immediate finance needed for uninterrupted B (F_min) from the maximum expected AB collected cash (Pi) that a creditor contract can legally claim: F_min<=Pi is necessary and sufficient only within that specified contract class. It does not establish actual pilot lending, customer participation or provider optimality.

These propositions are applications of cash-flow conservation, first-event hazards and production allocation. Trade credit and receivable finance are well-established, with Bocola–Bornstein NBER WP31026 (2023; revised June 2026) and Amberg et al. NBER WP22286 (2016; JPE 2021) as relevant prior art. DHL's May 2025 unloading/case-picking announcement motivates measurement, but does not identify paid site receipts, production overlap or learning hazards. No novelty or calibrated claim is made. Next test net-profit/customer-demand choices and qualified specialist alternatives rather than maximizing qualification probability alone.


## Result 10 — accepted customer demand and the cost of qualifying on productive capacity

[Complete integrated theorem/proof/empirical note](DEMAND_CONTRACT_THEORY.md) · [standard-library executable core](demand_learning.py) · [scoped tests](test_demand_learning.py) · [reproducible synthetic results](DEMAND_RESULTS.json) · [teaching](DEMAND_TEACHBACK.md) and [solutions](DEMAND_SOLUTIONS.md).

Result 9's long-run self-financing fraction used an exogenously specified A cash flow. We now derive that flow from a hypothetical share of a customer's concave value for **accepted complete-service** output relative to a competent human/specialist alternative. If the robot is already capacity-constrained, reducing production while qualifying B produces g(u)=g0-Lu-hu², not necessarily an assumed linear loss. A stationary discounted Bellman problem gives an *interior* optimal learning intensity when the incremental hazard benefit exceeds the first marginal opportunity cost but not the final one. A fully independent specialist route is compared on the same postqualification service and with its own positive training/facility cost.

A structural comparative-static result separates customer demand from the technical learning rate. Holding B's incremental qualified net value fixed, greater demand for *already-qualified A work* makes shared-hardware B development progressively less valuable relative to leaving A in production. The specialist's incremental net option is unchanged in this matched experiment. This can reverse organizational choice without any change in robot capability or hazard. A contractual minimum for accepted A throughput can itself reverse the ranking; a violable SLA may induce the opposite conditional *speed* response, since an operator who chooses to pay ongoing breach penalties has an incentive to exit that state sooner. None of these synthetic benchmark thresholds is a measured robotics parameter.

Cash and optimal investment are not interchangeable. With dated accepted service collections and concave g(u), Jensen's inequality and a constructive delayed-receipt policy give an exact long-run self-funded duty share max{u<=u_max:c*u<=g(u)}, under stationary demand, divisible time sharing and retained qualifications. The formula generalizes the Result 9 constant-receipt resource-conservation ratio. An expected discounted control policy need not be cash-feasible over every path; the corresponding finite-horizon, sample-path liquidity and contractual-floor Bellman problem remains open.

DHL's 2023 commercial unloading and 2025 *future* case-picking plans, GXO/Agility's 2024 RaaS and October 2026 future-site expansion, and Formic's issuer-described productive-hours contract identify candidate organizational relationships but provide **no matched demand, overlapping training/productive work, SLA, provider collection, or causal specialist comparator panel**. Revenue management and production-pricing prior art already provides the core concavity/capacity mathematics. The candidate manuscript synthesis is the *qualified production–learning–payer* connection; standalone theorem originality is unestablished. Continue the same paper rather than proliferating new Q-numbered toys.


## Result 11 — financeable demand can overturn the monotone shared-learning premium

The preceding Result 10 establishes a *within-feasible-set* comparative static: holding incremental B demand fixed, increased demand for already accepted A work makes learning on A's productive hardware less privately valuable when it displaces A output. This does not establish monotonic actual qualification investment when stronger A demand simultaneously finances the first acquisition date. The full finite-cash derivation, exact model, source chronology and teaching are in [FINITE_CASH_DEMAND_THEORY.md](FINITE_CASH_DEMAND_THEORY.md); do not interpret this paragraph as a new standalone theory or as calibrated robotics performance.

Introduce provider liquid cash C, a dated vector of invoiced-but-uncollected accepted customer receipts P, qualified service state z, an enforceable complete-A service floor and a choice between shared and independently equipped specialist development. Only matured P can pay immediate operating and development expenses. With cash and invoice maturity separate, the Bellman state is (t,C,P,z), transitions use actual received invoices, and terminal value includes remaining fully collectible receivables at par. Under no default and no discount, terminal earned wealth telescopes to opening cash plus accepted invoices less paid costs; *timing influences the feasible learning path without fabricating incremental production surplus*.

A four-date exact synthetic benchmark takes A q in {1,2}, provider invoices R_A(q;m)=m q-q(q−1) with immediate operating expense q and a hard floor q>=1. Shared learning delivers A=1, costs 13, succeeds with probability 3/4; a real specialist alternative keeps A=2, costs 20, succeeds with probability 9/10. Both give the same qualified B service of invoice 16 and incremental cost 2 in a separate subsequent work window. After normal t=0 production, one-date collection gives 2m spendable at t=1, so shared entry requires m>=7 and specialist entry requires m>=11. Conditional expected two-service-window private premiums, if routes are feasible, are 11−m and 26/5, respectively. Although the former strictly falls with demand, actual optimized investment changes from **no B qualification at m=4**, to **shared development at m=7**, to **specialist development at m=11**. The exact Bellman solver allows adaptive retries and the actual floor, and reproduces terminal premiums 0, 4 and 26/5; with a two-date collection lag and starting cash 4, all three optimal premiums are 0. An independent exhaustive decision tree verified those exact six finite outcomes. The stronger universal claim that 'more incumbent demand always deters investment' is false. Nor is a faster receipt automatically productive value: with sufficient opening liquidity and par terminal receipts, the example's one- versus two-date receipt difference vanishes.

An explicit, enforceable advance of 12 at t=1 secured by future A invoices restores the m=7, L=2 shared option in a separate pathwise calculation: even on B failure, dated cash before t=4 repayment is 27, versus 39 on success. At fee f, project terminal gain is 4−f, not 4+12−f. The lender's principal provides *feasibility*, not free surplus, and fee, default risk and cash-flow rights determine distribution. Actual robotics site assignment rights and receivable maturities are unobserved. This is classical liquidity-sensitive investment and staged production, not claimed novel Bellman mathematics; the empirical cash-flow sensitivity critique of Kaplan–Zingales means demand changes and funding constraints must be measured separately.

This extension continues the same capability-production theorem program, not a finance-only replacement. An organization's task eligibility, safety-compatible supervision, manufacturer costs, data rights and embodiment determine the recipe and acquisition options; customer receipts and contract obligations determine who can actually reach them. Negative control: a matched well-funded warehouse receiving faster payment should not change physical service output through this model's finance channel. GXO's June 2024 commercial Digit tote handoff and October 2026 future-site announcement show organizational relations but not the joined accepted-order/qualification/invoice panel required to test this proposition. Next investigate **contingent financing and payment default with heterogeneous payer rights and demand expiry** without treating capital transfer as productive output.


## Continuing theory: qualification as an assignable but contingent cash claim

The customer-demand/finite-liquidity mechanism is not complete without distinguishing who may *pledge* the expected cash of an accepted but still unqualified service. The integrated extension in [CONTINGENT_CLAIMS_THEORY.md](CONTINGENT_CLAIMS_THEORY.md) derives a claim-specific financeability envelope with buyer prepayment, B invoice collection default, uncertain surviving order demand, a voluntarily served B operation incentive, qualified specialist development, and refunds if qualification fails. It proves an initial-funding necessary condition (and sufficiency only with enforceable transfers and pathwise solvent continuation), then tests why a single receivable-backed lender can reject a positive-profit project that a customer/lender coalition can fund. A stronger competent-specialist contract can make the specialist preferable to the apparently more financeable shared embodiment for both provider and buyer in the exact example. This is a corporate-finance/production-network synthesis, not a novel general lending theorem; the required legal and commercial rights have **not** been observed in any robotics case. The full agenda remains wider than the paper: manufacturer and customer rights, actual order completions, supervision and production topology must be measured.


## Continuing unified theory — A-buyer participation and correlated B receivables

[Full theorem, proof, counterexample and empirical discrimination](PARTICIPATION_DEPENDENCE_THEORY.md) · [executable exact model](participation_coupling.js) · [scoped tests](test_participation_coupling.js) · [machine-readable results](participation_results.json) · [source ledger](PARTICIPATION_EVIDENCE.json) · [teach-back](PARTICIPATION_TEACHBACK.md) and [separate solutions](PARTICIPATION_SOLUTIONS.md).

The previous B-receivables funding envelope omitted an economically distinct rights holder: the customer whose already-qualified A work is displaced during shared-hardware qualification. If that customer retains positive value from the marginal accepted order beyond the provider's lost margin, shared qualification requires its consent, substitute service or compensating transfer. The previously imposed A customer value of zero is a **special assumption**, not a sufficient account of production surplus. A hard two-order accepted-service obligation may bar the shared route regardless of total project profitability. This is a change in the qualified *production-and-contract* network, not an incremental cash-flow label.

The second missing object is the **joint event** connecting technical qualification, surviving customer need and actual collection. With Q independent of B demand survival S, but arbitrary dependence between potential B payment events and Q,S, two Boole–Fréchet overlap bounds give a sharp interval for pledgeable expected B receipts. A B buyer's worst participation scenario is *high* payment, whereas a nonrecourse lender's is *low* payment. For a fixed ex-ante contract that must satisfy both under unknown dependence, the robust date-1 funding envelope equals B buyer gross accepted-service value minus the upper receipt bound plus the lender's eligible fraction of the lower receipt bound. Neither marginal success rates nor provider invoiced revenue identify this envelope; average credit outcomes may be selected on qualified orders.

An exact counterexample makes the boundary constructive. The shared route's expected B receipts range from 19.6 to 22.8 in normalized units despite fixed qualification and payment marginals. When the incumbent A buyer's retained lost value is 10, shared qualification's true aggregate expected gain remains 4.35, but its up-front compensation and training gap is 22. An independence-priced, nonrefundable B pilot and lender could cover 23.94; a **uniformly participating nonrefundable** contract under the unspecified joint payment dependence can fund at most 21.2. This does **not** establish general nonfinanceability. A competent B pilot of 14, refunded if qualification fails, together with an 8-unit robust B loan, satisfies buyer, lender, provider and A customer participation in the exact model; refunded failure states remain cash-solvent. More sophisticated contingent contracts alter access to productive opportunities without adding real output.

This correction sharpens the candidate paper synthesis: economic qualification pathways depend jointly on complete-service production complementarities, the information structure of learning and demand, and the location of customer consent and pledge rights. It supplies neither a novel probability bound nor observed finance terms. The closest mathematical foundations remain classical Fréchet intersection inequalities and secured-financing/incomplete-contract theory. GXO/Agility's 2024 commercial tote-handoff and October 2026 expansion descriptions establish a relevant operating relation but do not identify A customer marginal value, joint payment–qualification events or refund/assignment terms. The next extension must challenge the constructed refund repair with **correlated A invoice default and qualification failure**, because the presently certain A collections provide its late refund liquidity.


## Continuation: endogenous transfer, target grounding and embodiment investment (November 17)

The previous [data-value continuation](data_value/DATA_VALUE_THEORY.md) connected heterogeneous source exposure to qualification probabilities and then to the optimized customer production-value table. That fixed-transfer result was only an intermediate step. The next [integrated argument and proof ledger](data_value/TRANSFER_GROUNDING_THEORY.md) makes the **transfer interface itself an investment object**: source collection, target calibration/alignment, diagnostic evaluation and embodiment design compete for resources, while the existing qualified production alternative remains available.

A stylized but structurally identified Gaussian information environment decomposes target-policy prediction uncertainty into an environment factor learned through source experience, an embodiment-specific action factor learned through target grounding, and an irreducible residual. The scalar qualification probability is the probability the resulting error lies within a specified tolerance. This is *not* a whole-order industrial service acceptance claim. Because the posterior variances are inversely related to additive information precisions, minimizing uncertainty at a fixed learning expenditure has a closed-form globally optimal source/ground allocation; changing existing source stock or physical action sensitivity changes that allocation. A single service's value multiplier changes optimal **total** spend and embodiment choice but **not** that conditional mix at fixed spend; customer-conditioned source mixtures require multiple opportunities or distinct embodiments as in the preceding chapter.

An exact derivative further distinguishes types of complementarity: even when source and grounding observations independently reduce separate posterior variances, their marginal contributions to passing a symmetric Gaussian acceptance boundary are complementary at high remaining uncertainty and substitutive at low remaining uncertainty. Neither sign requires inventing a multiplicative learning coefficient. A constructive normalized example shows that accumulating source experience can turn a redesigned body from an uneconomic option into an economic one; a full integer-budget menu still chooses old-body collection plus grounding at low stock and immediate redesign at higher stock. The common source residual also induces *correlated* qualifications across target bodies, so separate marginal success rates do not support product-probability valuation of a joint accepted service. A distinct decision-theoretic calculation shows a short diagnostic of whether source transfer works can have positive **information** value without directly increasing technical competence.

These results deliberately invoke known Gaussian inference, Bayesian experimental design, Cauchy–Schwarz allocation and standard value-of-information mathematics, not an originality claim. Farboodi–Koh–Xia already study production-generated data, directed transfer and planner data value; controlled cross-embodiment representation and pairing work already probes alignment. The candidate economic synthesis is the link between *learnable transfer interfaces*, retained physical configurations, joint qualification and a customer-specific production opportunity network. Source-to-target transfer parameters, complete-order acceptance and operating surplus are not calibrated. The Nov 22 synthesis should challenge this claim against a genuinely strong general learning/experimental-design comparator, not recast every elementary identity as a separate result. The next step is an endogenous dynamic choice between current production-derived data and targeted grounding/diagnostics with a defensible target-only specialist alternative.

[Full theory and source/assumption discussion](data_value/TRANSFER_GROUNDING_THEORY.md) · [Executable scoped model](data_value/grounding_embodiment.js) · [Computational results](data_value/grounding_results.json) · [Proof ledger](data_value/TRANSFER_PROOF_LEDGER.md) · [Exercises](data_value/TRANSFER_EXERCISES.md) and [solutions](data_value/TRANSFER_SOLUTIONS.md).


## Continuation: intervention-selected observations and the economics of correction (November 17 evening)

The productive teleoperation model previously treated an informative grounding report and persistent correction-induced update as given. The next [integrated intervention-selection chapter](data_value/INTERVENTION_SELECTION_THEORY.md) makes those observations depend on the controller's **visited-state distribution**, the operator's gating rule, a latent target error regime, and a separately specified retained qualification transition. The immediate consequence is an identification boundary: the correction fraction is the product of relevant-state exposure, gate sensitivity and would-be error propensity in a simplified supervised model. Fewer corrections need not mean fewer errors. Even with complete exposure logs, two worlds can have identical correction distributions but different rates of missed error when gate sensitivity is unmeasured; constructed rates are 3/8 versus 1/8. Independent supervised audit is needed before claiming safe autonomously qualified service.

Under exposure-independent regimes, a higher-probability correction-report experiment Blackwell-dominates a lower one by positive-event thinning, and logging exposed states dominates correction-only observation. This is standard information ordering, **not** a recommendation to maximize costly or unsafe interventions. The correction-to-qualification transition remains distinct: selected trajectories can repair today's service without creating future productive capability. Optional retained policies and freely usable information preserve optimized-value monotonicity under unchanged rights/costs, even if a newer autonomous policy generates fewer corrections.

A synthetic two-date production menu makes the decision explicit. Routine, a deliberate supervised target probe, and a competent specialist earn respectively 6, 5 and 6.3 normalized current contributions. If exposure is 1/4, 1 and 0, a correction shifts beliefs about source transfer and can raise future qualified source reuse. With a genuine target-only fallback, optimized totals are 91/8, 23/2 and 113/10; the probe wins narrowly. **Either** delaying the non-safety report until after route commitment **or** eliminating persistent training improvement switches the choice back to routine. A better target-only embodiment (future contribution 25/4) reverses the probe choice; free routine generation of the same relevant data makes special collection redundant. The analytic threshold relates current opportunity cost to future optimized production, not an intrinsic price per demonstration. These are possibility proofs, not empirical dollar values.

The next sequential proof gap remains: a first retained control update may change where the robot will visit in a second deployment, and thus which error/transfer regimes remain identifiable. The November 22 synthesis should compare the mechanism against DAgger's policy-induced distribution, ThriftyDAgger's intervention gate, IntervenGen's generated recoveries and the parent's dynamic production framework, not claim novelty in Bayes' rule, Blackwell ordering or production-derived data.

[Full chapter](data_value/INTERVENTION_SELECTION_THEORY.md) · [Executable model](data_value/intervention_selection.js) and [synthetic results](data_value/intervention_results.json) · [Proof ledger](data_value/INTERVENTION_PROOF_LEDGER.md) · [Empirical protocol](data_value/INTERVENTION_EMPIRICAL_PROTOCOL.md) · [Exercises](data_value/INTERVENTION_EXERCISES.md) and [separate solutions](data_value/INTERVENTION_SOLUTIONS.md).


## Continuing unified theory — sequentially selected state support and customer qualification

The next [sequential-support derivation](data_value/SEQUENTIAL_SUPPORT_THEORY.md) closes a one-step omission in the intervention chapter: a correction retained after the first episode changes the states the next controller is permitted to visit, so future data availability is jointly selected by past observations, embodiment access, and safety. The general Bellman transition now includes both the controller-specific second occupancy kernel and the held-out qualification kernel, with all later customer contribution kept inside the *same* optimized production f(Q;omega).

If a first corrected deployment is necessary to reach a new qualified B service, its two-step qualification probability is sum_h pi_h r_h e_h s_h, not generically a product of average correction and B success rates. In two observationally identical first-episode worlds with the same marginal future qualification rate, differing source-to-target coupling produces joint qualification probabilities 5/16 versus 3/16; the naive product is 1/4. A competent target-only specialist and the full production opportunity costs reverse the selected first acquisition: a safe probe is optimal in the positive-alignment world, whereas current productive routine is optimal in the negative-alignment world. These are exact **synthetic conditional counterexamples**, not field outcomes or claimed new general probability laws.

Without approved second-state support, first-episode logs cannot identify the B service's future qualification kernel; the measurement implication is to compare matched safe second-episode coverage and independently audited intervention quality, then connect qualification to *actual accepted customer service* and specialist/customer alternatives. Free optional policy retention preserves maximized value by feasible-set inclusion, even if newer policies produce fewer logged corrections. An independent finite-event-tree code check and new exercises/solutions accompany the full proof and [empirical design](data_value/SEQUENTIAL_SUPPORT_EMPIRICAL.md). The Nov 22 synthesis and all Christmas milestones remain open; DAgger, ThriftyDAgger, prior partial-identification results, and DDA remain central prior art.


## Continuing unified theory — safe multi-step support frontier and accepted customer bundles

The [multi-step support theory](data_value/MULTISTEP_SUPPORT_THEORY.md) tests whether ordinary production-generated experience is an economically sufficient substitute for deliberate target grounding or embodiment redesign **under the same safety, operator, cash and calendar constraints**. A finite controlled-state model retains incumbent qualified configurations and connects controller-dependent exposure, selected corrections, validated policy updates, next-state reachable support and **joint** accepted-service qualifications to the original optimized production function f(Q;omega). This is a continuation of the sequential-support mechanism, not a distinct new paper or an independent value-of-data add-on.

A resource-augmented safe-reachability certificate distinguishes *positive path support* from reliable production; a sufficient coupling result gives conditions under which routine-only production dominates every deliberate alternative for **all increasing** customer production functions. Neither criterion can be inferred from overall skill pass rates. With both recipes individually passing with probability 1/2 under two policies and every joint outcome having positive support, a controlled counterexample changes the **joint** accepted B-and-C probability from 1/16 to 7/16. Under complementary customer demand the grounding policy can earn 3 normalized net units versus routine's 1, beating a competent specialist at 2; with additive demand, routine earns 8 versus grounding's 4. This is a change in the customer production function and full joint qualification distribution, not another transfer-parameter variation.

The theory next examines an explicit zero-cut in safe policy-induced state exposure: a first routine update makes a second target state conceptually relevant but ordinary production never visits it safely before the deadline. A **two-slot adaptive policy** compares productive routine, deliberate supervised target validation, a target-only new embodiment and a competent specialist. The exact optimized contribution is piecewise linear in the additional customer bundle value Delta, with breakpoints at 3 and 20/3; at Delta=7, adaptive selection of grounding after successful first update and redesign after failure earns 23/5 versus 3 for the competent routine/specialist family. At Delta=12 it earns 319/40. If a second ordinary routine slot safely qualifies B with probability r high enough, it dominates costly grounding in the successful-update branch: r >= 3/4-(5/4)/Delta. Thus the **routine coverage/held-out qualification kernel**, not first-episode correction count, is the policy-discriminating object. Every number is conditional and synthetic. The safety feasibility of any real intervention would require external approval.

Closest prior art already includes policy-induced distributions (DAgger), safe Markov reachability/exploration, monitored interventions (ThriftyDAgger), and future production-generated data (Data-Driven Automation). The new argument is an integrated economics-and-learning synthesis, with *no scientific novelty or empirical calibration established*. The [scoped reproducible model](data_value/multistep_support.js), [result record](data_value/multistep_support_results.json), [proof ledger](data_value/MULTISTEP_SUPPORT_PROOF_LEDGER.md), [matched measurement protocol](data_value/MULTISTEP_SUPPORT_EMPIRICAL.md), [exercises](data_value/MULTISTEP_SUPPORT_EXERCISES.md) and [separate solutions](data_value/MULTISTEP_SUPPORT_SOLUTIONS.md) preserve this distinction. Next extend the same model to partially observed latent regimes and a pathwise safety/operator resource budget; no November 22, November 29 or later release gate is automatically passed.


## Continuing unified theory — latent transfer, pathwise operator capacity and jointly qualified service

The [partial-observation and pathwise-budget chapter](data_value/PARTIAL_OBSERVATION_PATHWISE_THEORY.md) strengthens the safe multi-step theory. A latent source-to-target alignment regime now determines not only whether corrected data transfer, but which *approved subsequent actions* can be executed with the actual crew and recovery reserves. The finite-horizon Bellman state includes the posterior supported regimes, controller/embodiment lineage, retained qualified bundles, and **remaining pathwise operator, cash and calendar resources**. Current accepted service and terminal optimized customer production are valued only once.

A counterexample shows why stronger diagnosis is not automatically a better deployment investment. For a customer bundle worth 8 normalized accepted-production units, ordinary production yields optimized 7; a target-independent new embodiment yields 36/5=7.2; and a competent specialist available in both slots yields 6. A fully revealing grounding probe earns 8, but a 99%-accurate probe that has already consumed one scarce operator unit cannot safely execute its regime-specific follow-on under a hard 2.1-unit budget: its optimized route value falls to 2, so **the redesigned embodiment wins**. The failure path requires total operator use 3 even though *expected* use is only 2.01. Replacing hard feasibility with an explicitly approved 2% chance cap or expanding actual capacity to 3 produces different answers; they are not interchangeable operating rules. The theoretical discontinuity at exactly perfect observation depends on exact posterior support, not a claim that a real sensor can certify perfection.

The chapter separately sharpens the identification problem for **joint** accepted B-and-C services: conditional component acceptance probabilities constrain but do not determine the bundle's contribution. Fréchet bounds imply that, with the same respective component marginals, routine production may be worth 5–7 and embodiment redesign 6.4–7.2 in a matched illustrative economic comparison. Both economic rankings are consistent with the reported marginals. This is a formal partial-identification result, not a numerical claim about a robotics fleet. It specifies the missing evidence: source/target regime proxy and observation confusion matrix, independent safe gate/exposure audit, peak recovery load, joint held-out customer acceptance and competent specialist production under the same demand window.

The work reuses **standard** Blackwell information ordering, finite POMDP/resource-budget induction and Fréchet bounds; no new scientific theorem or field calibration is asserted. The [exact scoped JavaScript source](data_value/partial_observed_budget.js) was exercised before publication in connected V8 (764 assertions, comparing event-tree enumeration against closed forms), with separate rational Python spot checks. [Proof/claim ledger](data_value/PARTIAL_OBSERVATION_PROOF_LEDGER.md), [identification design](data_value/PARTIAL_OBSERVATION_EMPIRICAL.md), [results](data_value/partial_observed_budget_results.json), [exercises](data_value/PARTIAL_OBSERVATION_EXERCISES.md) and [solutions](data_value/PARTIAL_OBSERVATION_SOLUTIONS.md) accompany it. The next gap is *robust optimal policy selection with partially identified regime and joint qualification kernels*, not another transfer-rate parameter sweep. November 22 integrated synthesis and all subsequent gates remain unpassed.


## Continuing integrated theory — robust choices under partially identified transfer and joint acceptance (18 November UTC)

[Full conditional theory/proofs](data_value/ROBUST_POLICY_IDENTIFICATION.md) · [proof/rejection ledger](data_value/ROBUST_POLICY_PROOF_LEDGER.md) · [exact JS calculation](data_value/robust_policy_identification.js) and [results](data_value/robust_policy_results.json) · [matched empirical protocol](data_value/ROBUST_POLICY_EMPIRICAL.md) · [Models A/B synthesis bridge](data_value/ROBUST_MODELS_AB_SYNTHESIS.md) · [exercises](data_value/ROBUST_POLICY_EXERCISES.md) and [separate solutions](data_value/ROBUST_POLICY_SOLUTIONS.md).

The preceding partially observed model assumed a joint accepted-service kernel. Under a set of *possible* fixed complete history laws, an economically dominant safe deployment must defeat each feasible competitor **within the same possible world**, rather than comparing independent worst and best payoff intervals. A pairwise difference certificate is sharp for the declared action menu and can be stronger than interval separation. In a synthetic complete-service example with preserved routine incumbent output 1 and full B/C customer value 8, an additional matched acceptance restriction \(q_E-q_R\le0.1\) makes R beat redesigned embodiment E by **at least 0.2** and a competent specialist by 0.6, despite overlapping individual value ranges. Such a matched restriction is explicitly hypothetical and is **not** derivable from benchmark component marginals or already observed robotics data.

A separate exact diagnostic result makes the value of a safe regime report depend on a per-regime *lower* accuracy bound and current service displaced. In a symmetric fixed-regime two-slot model, a diagnostic costing 0.1 beyond lost current productive time robustly beats the productive **randomized maximin policy** only when that lower bound exceeds \(41/60\); at a bound of .7 its guaranteed synthetic value is 6.1 versus 6. This is **not** dominance over every deterministic policy, and fails as a feasible comparison if any report branch needs an unapproved 3 units of recovery under a 2.1 hard cap. Regime-labelled confidence intervals and a separate physical support/safety audit are therefore different evidence needs. The synthetic CPU assertions verify arithmetic, not technical transfer, safety or causal validity.

This is the *same* production-envelope argument as Model A's accepted-service customer demand and Model B's current cash/known transition/expansion choice, but its acquisition kernel is now partially identified. An explicit [bridge](data_value/ROBUST_MODELS_AB_SYNTHESIS.md) preserves original Model B credit/ranking facts instead of overwriting or double-counting them. Static fixed transfer regimes should not be silently converted into a rectangular adversary able to switch after an informative report. Manski (2004), robust POMDP and robust-control rectangularity literature, Blackwell and Fréchet bounds are clear prior foundations. Originality, field robustness, the official industry quantitative backbone and the November 22 synthesis gate are **not** established.

**Persisted proof gap:** a tractable nonrectangular *adaptive* robust decision certificate when regime information, recoveries, qualifications and customer demand coevolve; independent operator-safety approval and matched end-to-end 00/10/01/11 acceptance remain missing. Next: audit the cross-Models A/B notation and production envelope for November 22, then challenge the paired acceptance bound under drift and unobserved site confounding; keep the empirical atlas, manufacturing and demand-side opportunity work active. December 25 23:59 Eastern remains the final target.


## Continuing integrated theory — transportability of the matched qualification certificate (18 November UTC)

[Conditional chapter and proofs](data_value/TRANSPORT_AND_SAFETY_IDENTIFICATION.md) · [proof and rejection ledger](data_value/TRANSPORT_PROOF_LEDGER.md) · [empirical design](data_value/TRANSPORT_EMPIRICAL_DESIGN.md) · [CPU model](data_value/transport_safety_identification.js) and [recorded outputs](data_value/transport_safety_results.json) · [learning exercises](data_value/TRANSPORT_EXERCISES.md), [separate solutions](data_value/TRANSPORT_SOLUTIONS.md) · [canonical A/B notation update](data_value/ROBUST_MODELS_AB_SYNTHESIS.md).

The earlier matched R/E complete-service acceptance restriction was explicitly hypothetical. Its economic content depends on *where and when the accepted orders occur*. For site × customer-window strata \(z\) with target demand weights \(\mu_z\), current incumbent contribution \(b_z\), real cost difference \(k_z\), incremental optimized complete-bundle contribution \(\Delta_z\), and conditional joint acceptance difference \(d_z=q_E(z)-q_R(z)\), a restricted policy comparison is \(J_\mu(R)-J_\mu(E)=\sum_z\mu_z[b_z-k_z-\Delta_zd_z]\). This is a direct specialization of the established operating \(V(Q;\omega)\) envelope, not an added data premium. Valid conditional upper differences \(d_z\le u_z\) give a demand-weighted economic lower certificate; a *pooled* study bound does not necessarily transport.

A sharp synthetic selection counterexample holds technical component marginals at .75 for routine R and .9 for redesigned E at **each** of two sites. A study mix of 90/10 yields matched joint difference .08 and R−E **+0.36**, whereas a target paid-service mix of 40/60 yields difference .23 and R−E **−0.84** at unchanged \(b=1,\Delta=8\). This overturns application of the study's earlier pooled certificate, not the earlier theorem under a genuinely valid target-matched constraint. With validated bound .1 on covered commercial orders and at most .4 on uncovered ones from the same component marginals, the strict R-over-E certificate vanishes when unsupported target share exceeds **1/12**, given the synthetic production value. Changing \(\Delta\) from 8 to 12 also reverses a fixed \(d=.1\) comparison without changing learning success.

A separate joint-support example holds unconditional good-report and high-recovery frequencies fixed while moving the rare high recovery onto the **good-report** branch selected for the terminal action. Under the hard 2.1 operator cap, the selected action then becomes unapproved/infeasible even though the marginals are unchanged. The safe-menu requirement precedes any economic lower bound. This extends the persistent-regime and recovery analysis, and makes accepted customer demand, trial enrollment/positivity and report-conditional operator support central to validation.

The companion [Models A/B synthesis](data_value/ROBUST_MODELS_AB_SYNTHESIS.md) now writes a canonical \(Q,\omega,V,J\) mapping and states the exact degenerate conditions under which Model A's positive-part customer value and deterministic Model B expansion can be recovered. These are conditional standard transport/partial-identification/robust feasibility constructions; external novelty and customer calibration are not established. The exact source blob's scoped synthetic tests and independent fraction calculations are not hardware certification, full CI or peer review. The specific next question is how policy-dependent customer composition and state visitation can be jointly bounded under a *persistent*, nonrectangular transfer regime. The November 22 review, official numeric atlas backbone and December 25 23:59 Eastern final target remain unchanged.
## Continuing integrated theory — endogenous orders and persistent transfer (18 November UTC)

The earlier site-matched transport certificate holds the target customer demand distribution fixed. That is a **conditional** limit, not the general history-dependent economics of deploying robots: routine productive exposure, a supervised target-grounding plan, and a changed embodiment can affect the next period's safely reachable state support, jointly accepted service, order mix, customer willingness to pay, and retained qualified alternatives. The general comparison must evaluate the **whole** source-to-production path once through \((Q_t,\omega_t,V,J)\), rather than weighting route-generated orders by a shared post-treatment \(\mu\).

A [full-history companion chapter](data_value/ENDOGENOUS_DEMAND_PERSISTENT_TRANSFER.md) models one latent persistent transfer/demand/recovery regime across both periods and explicitly retains qualified old policies and a specialist competitor. For two possible regimes and an **uncertain initial prior** \(p\in[\ell,u]\), fixed regime-conditional complete-path values \(w_{\pi H},w_{\pi L}\) imply a rigorous paired policy comparison:
\[
\inf_{p\in[\ell,u]}\left[p(w_{\pi H}-w_{\sigma H})+(1-p)(w_{\pi L}-w_{\sigma L})\right].
\]
The same latent world is held for both policy counterfactuals and for reports within a trajectory; no independent adversarial regime is chosen after every demand realization. This special-case endpoint calculation is conditional standard ambiguity algebra, not an asserted new result in robust MDPs. Incomplete conditional demand/qualification kernels call for conservative interval bounds and matched experiments, not automatically a known-transition Bellman equation.

A wholly **synthetic** two-period model gives safe complete-history contribution R=(14,3), G=(7,10), redesigned E=(7.5,7.5), and specialist S=(6,6) under aligned/misaligned transfer; each route has actual first-period flows, route-specific second-period customer orders and checked operator requirements. At \(p\in[.4,.6]\), pure maximin floors are 7.4, 8.2, 7.5 and 6: G is the robust pure action, but G does **not** uniformly beat R in a same-world pairwise comparison. If fractional independent deployment allocation is permitted, the mixture \(3/14\) routine and \(11/14\) grounding guarantees 8.5, attaining a simple matching upper bound at \(p=.5\); indivisibility, shared learning or tight capacity may forbid it. The example is a robustness and policy-menu demonstration, not estimated robotics adoption.

A second construction with one common uncertain transfer prior and an independently varying customer order shows an expected accepted-production value .5 under every admissible complete law; artificially splicing independent regime priors after each order gives .25. Rectangular uncertainty is therefore a **different model**, as established in robust control and recursive-priors prior work, not a measurement of physical skill. A third construction shows that arbitrarily many R-only observations cannot distinguish whether the never-deployed G/L route yields a robust floor 8.2 or 5.2: the route ranking against E reverses with an unobserved grounding/customer response. Safe matched grounding or a valid bridge restriction is required; ordinary importance weighting has no missing policy support to reweight.

The theorem/claim details and disproof boundaries are recorded in [the proof ledger](data_value/ENDOGENOUS_DEMAND_PROOF_LEDGER.md), the next practical customer-order/robot-state design in [the prospective empirical plan](data_value/ENDOGENOUS_DEMAND_EMPIRICAL_DESIGN.md), and reproducible [CPU model](data_value/endogenous_demand_persistent_transfer.js) and [saved output](data_value/endogenous_demand_persistent_transfer_results.json). Separate student [exercises](data_value/ENDOGENOUS_DEMAND_EXERCISES.md) and instructor [solutions](data_value/ENDOGENOUS_DEMAND_SOLUTIONS.md) strengthen the teaching artifact without recasting this result as a finished paper.

**Unified argument for the still-open November 22 gate:** transferable data changes capabilities only through training, embodiment, target alignment and verified safe recipe qualification; complementary production and scarce resources determine marginal accepted output; customer demand, capture and incumbent production determine economic value; deliberate versus productive acquisition changes later physical exposure *and* demand; the full adaptive policy then selects the next investment. Model A is the single-customer divisible accepted-output/capture specialization, and Model B the deterministic known-transition/cash-feasible investment specialization. Qualification joint dependence, safe operator support, incomplete transfer information, policy-dependent orders and rights are substantive limits, not additive "robot data premiums." The empirical customer panel, quantitative interindustry backbone, independent review, demonstrated general result and contribution choice remain missing. November 22 is **not** marked passed; December 25 23:59 Eastern remains the final target.


## Continuing integrated theory — coupled transfer, customer-order and recovery identification (18 November UTC)

The preceding full-history persistent-regime calculation required fully specified conditional transition laws. We now replace that assumption with a **single partially identified joint distribution of complete policy response types**, allowing latent source alignment, customer opportunities, later orders, jointly accepted services, approved physical recovery and retained fallback to move together. For a fixed feasible full-history policy \(\pi\) with type-contingent total contribution \(v_{\pi k}\), economic value is \(J_\pi(q)=\sum_k q_kv_{\pi k}\). Observable joint moments constrain a common \(q\), not separate independently selected marginal success/response probabilities for each candidate. The sharp paired comparison relative to the admitted finite response-type polytope is the LP \(\min_{q\in\mathcal Q}(v_\pi-v_\sigma)^\top q\) with a standard dual moment certificate. This is *not* automatically sharp for additional nonlinear structural-kernel invariances; that identified-set gap must be retained. A policy must also meet strict supported **pathwise** operator budgets, rather than pass an expected-recovery test.

An exact synthetic four-response-type construction holds the marginal aligned-transfer chance and the registered target-customer opportunity share both at one half, but leaves their joint mass \(t\in[0,1/2]\) unidentified. Under complete accepted-customer contributions R \(=5+8t\), G \(=8-2t\), qualified new body E \(=6\) and specialist S \(=5\), the paired R−G value spans [−3,2] despite those identical marginal facts. A valid joint audit narrowing \(t\) below or above 0.3 would discriminate the economic route; an unvalidated report or artificially factorized transfer kernel would not. The conditional four-type LP has an explicit primal/dual proof and does not turn a robot motion score into money. This is a **different partial-information example** from the earlier known-H/L ED2 numbers; those are retained.

The production enterprise's objective matters separately from the data: with genuinely independent fractional deployment opportunities, the maximin mixture uses 1/5 R and 4/5 G and guarantees 7.4. A minimax-*regret* mixture uses 2/5 R and 3/5 G, lowering guaranteed production to 6.8 but worst opportunity regret to 1.2. Remarkably, a perfectly safe oracle that reveals the **population** joint mass \(t\) (not each customer's regime) adds zero guaranteed maximin value when fleet convexification is already possible, though it adds 0.4 to the worst-case guarantee for a pure indivisible fleet decision. This is standard minimax information/convexification mathematics, not a claim that target diagnostics, individual regime information, or actual learned qualification lack value.

A potentially useful safe diagnostic must be externally validated to identify a **joint** target event. If its sensitivity \(s\) and false-positive rate \(f\) for a persistent aligned regime are stable within the pre-action demand class \(D\), then \(m=P(Z=1,D=1)=fP(D)+(s-f)P(H,D)\). This bridge can narrow the economic ranking but fails without cross-D calibration, safe target qualification evidence, recovery-tail audit, rights and complete customer-order denominators. The [full companion derivation](data_value/COUPLED_IDENTIFICATION_AND_AUDIT.md), [proof ledger](data_value/COUPLED_IDENTIFICATION_PROOF_LEDGER.md), [empirical protocol](data_value/COUPLED_IDENTIFICATION_EMPIRICAL.md), [reproducible CPU synthetic model](data_value/coupled_identification_audit.js), [saved results](data_value/coupled_identification_audit_results.json), and [separate student](data_value/COUPLED_IDENTIFICATION_EXERCISES.md) / [instructor](data_value/COUPLED_IDENTIFICATION_SOLUTIONS.md) materials document this extension.

**November 22 gate remains open.** The common \(Q,\omega,V,J\) accounting chain and Models A/B reductions are retained. Missing are a validated H/report/customer-order bridge, tested nonlinear dependence and controller interference, matched actual customer accepted-service and recovery observations, the official quantitative production backbone, independent originality/proof review, and final contribution selection. No historical CI or actual robotic training has been performed; December 25 23:59 Eastern is unchanged.


## Continuing integrated theory — diagnostic transport and nonlinear controller-pool learning (18 November)

The previous complete-history response-law LP and population audit silently left two empirical bridges: a diagnostic's sensitivity/false-positive rate must transport across actual pre-action demand strata, and fractional learning routes must be physically/economically additive. This continuation challenges both while retaining **one** \(Q_t,\omega_t,V,J\) spine. Its full [theoretical chapter](data_value/CONDITIONAL_CALIBRATION_AND_POOL_INTERFERENCE.md), [proof ledger](data_value/CONDITIONAL_CALIBRATION_POOL_PROOF_LEDGER.md), [prospective field identification protocol](data_value/CONDITIONAL_CALIBRATION_POOL_EMPIRICAL.md), [synthetic audit source](data_value/conditional_calibration_pool_audit.js), [recorded results](data_value/conditional_calibration_pool_audit_results.json), [student problems](data_value/CONDITIONAL_CALIBRATION_POOL_EXERCISES.md) and [separate solutions](data_value/CONDITIONAL_CALIBRATION_POOL_SOLUTIONS.md) document the conditional claims.

First, pooled classification quality can fail to rank data acquisition. With known pooled binary diagnostic rates 0.9/0.1, \(P(H)=P(D)=1/2\), and \(P(Z=1,D=1)=.34\), but *without* \(Z\perp D\mid H\), the synthetic source/customer coupling \(t=P(H=D=1)\) is sharply confined only to [.29,.39]. Two explicit full \(H,D,Z\) distributions share the observed pooled and demand/report margins yet give \(J_R-J_G=-.1\) and +.9. In contrast, the earlier conditionally invariant sensor would yield \(t=.3625\) and +.625. The distinction is an actual identification assumption, not a new statistic. A D-stratified safe validation or an independently randomized whole-route accepted-service comparison is necessary to narrow it.

Second, a two-slot shared-controller mechanism makes the independent R/G fleet mixing value \(J_0(x,t)=8-3x+(10x-2)t\) become \(J_\kappa=J_0-\kappa x(1-x)\) when an independently randomized mixed pair produces a measured extra accepted-service loss/gain. \(\kappa\) is twice the per-slot net effect *conditional on discordance*, not an exogenous generic "transfer coefficient." With \(\kappa\ge2.5\), the pure retained grounding route secures maximin value 7; at \(\kappa=3\) the old x=.2 hedge falls from 7.4 to 6.92. With verified complementarity \(\kappa=-3\), x=.2 instead guarantees 7.88. The pure R/G route evidence is identical under all three structures. If separate noninterfering controllers are costless, the 7.4 hedge remains available; if they require the stipulated additional .5 contribution cost, a population-level oracle can again have **.4 gross maximin value**. The sign and capacity dependence are hypotheses to test, not measured robotics effects.

The appropriate finite response-type unit under shared controller learning is the **entire independent pool**, with potential histories indexed by complete assignment vectors and report policies; per-robot independent types misidentify the cross-arm effect. Actual pathwise operator capacity, retained competent policies, rights, customer-order denominators, qualified accepted service and specialist alternatives remain explicit. No double-counted continuation data premium or benchmark-to-dollar conversion is introduced. These examples use known production response tables; real customer demand, controller interference and accepted order data are still absent. The November 22 synthesis gate and final December 25 Eastern target remain open.


## Continuing integrated theory — safely identifying controller-pool complementarity beyond pairs (18 November)

The next precise obstacle is an identification-and-deployment one, not another assumed transfer curve. [Safe pool factorial theory](data_value/SAFE_POOL_FACTORIAL_THEORY.md) uses the same full-history \(Q,\omega,V,J\) production value, whole qualified customer orders, demand-conditioned source learning, physical operator budgets, retained policy and specialist alternatives. It distinguishes *identifying an approved mixed-controller economic mean by cluster-level random assignment* from identifying a latent persistent transfer regime or transporting that mean across unrepresented target sites. A complete safe whole-pool policy assignment with known positive probability and complete post-treatment customer follow-up design-identifies its mean economic contribution without labeling H; individual robot randomization, missing order zeros, interference across clusters or unauthorized recoveries invalidate that claim.

The new three-slot Boolean factorial test makes the two-slot interference formula's limits explicit. With **synthetic** known full-service pool means \(f_0=7,f_1=7.5,f_2=7.4\), the pairwise-only extrapolated all-R production is 6.7. An unmeasured but hypothetically certified all-R mean of 6 versus 9 is compatible with every observed zero-, one- and two-R vector, yet reverses its rank relative to fixed one-R policy 7.5. The third-order economic interaction is therefore only bounded by [-0.7,2.3] if all-R contribution is separately bounded by [6,9]. This is standard Möbius inclusion–exclusion and bounded potential-outcome identification, not new learning mathematics or actual robot qualification. An independent Bernoulli x route assignment has P(all-R)=x³ and is **inadmissible for every positive x** if the all-R vector is unapproved under hard recovery limits; an exactly one-R safe saturation rule can be evaluated without that tail.

A separate target-transport decision demonstrates a constructive, resource-contingent option *despite* missing global evidence. When a prespecified 70% customer segment has a measured approved one-R contribution 7.5 against 7 fallback and the remaining 30% segment has only a [5,9] hypothetical one-R interval, global one-R has uncertain contribution [6.75,7.95] versus global G=7. But treating only the supported 70% while keeping G in the other segment gives 7.35 before segmentation costs, a strict improvement if true additional costs are below 0.35 and controller/customer spillovers are absent. This is not a sign claim about the unsupported 30%, nor permission to attempt an unapproved policy. The [proof ledger](data_value/SAFE_POOL_FACTORIAL_PROOF_LEDGER.md), [safe empirical design](data_value/SAFE_POOL_FACTORIAL_EMPIRICAL.md), [executable countermodel](data_value/safe_pool_factorial.js), [recorded outputs](data_value/safe_pool_factorial_results.json), and [separate teaching problems](data_value/SAFE_POOL_FACTORIAL_EXERCISES.md)/[solutions](data_value/SAFE_POOL_FACTORIAL_SOLUTIONS.md) expose assumptions and falsifiers. Scope remains a conditional economic synthesis: actual accepted-service panels, validated safety, official numeric production backbone and independent originality review remain absent. November 22 and December 25 dates are unchanged.


## Continuing integrated theory — independent pools fail under linked controller, operator and customer networks (18 November)

The preceding [safe whole-pool factorial result](data_value/SAFE_POOL_FACTORIAL_THEORY.md) is now stress-tested against network ties **between** nominal pools. The [full network-interference chapter](data_value/NETWORK_INTERFERENCE_THEORY.md) retains Q, omega, optimized V, complete accepted customer service, dynamic source learning, customer demand response, retained controller/specialist alternatives and common operator feasibility. It distinguishes the graph of **shared trainable weights/data rights** from the graphs of **shared recovery staff** and **customer substitution or complementary production**; these generally have different edges. A network-level potential outcome is the value of a complete history, not the sum of independent per-robot benchmark improvements. A measured individual positive learning effect can induce a negative total market response, and two separately safe controllers can produce an unsafe jointly supported recovery.

Under genuinely independent interference-closed network randomization with approved complete-vector support and complete eligible-order follow-up, the mean network contribution is design-identified by inverse probability weighting without observing a latent transfer regime. A sequential extension requires history-conditioned positivity and a common conditional transition law; uncontrolled external controller/dispatch/customer links break identification. This is established interference/off-policy mathematics (Hudgens–Halloran 2008, Aronow–Samii 2017, Leung 2022), not a new estimator. The exact identified target does **not** equal a latent-type robust policy contrast or authorize a recovery path.

A sharp conditional sensitivity result corrects the earlier 70% supported-segment selective A rollout. Given A gain 0.5 over old contribution 7, B market weight 0.3, spillover loss per B unit s and extra coordination cost c, the true network-wide policy difference is 0.35-0.3s-c. If s only lies in [-0.4,1.5], the proposed rollout's contribution lies in [6.90-c,7.47-c] rather than the no-interference 7.35-c. It cannot be certified against retained old 7 from the isolated A result. For c=0, strict improvement requires s<7/6. These bounds are sharp only in the stated unrestricted additive response class; physical controller/customer kernels may tighten them. Opposite controller-learning and customer-order mechanisms can give identical aggregate net revenue. A matched checkpoint isolation/held-out whole-service experiment plus a complete original customer order registry is needed for attribution. No benchmark-to-dollar conversion is made.

A separate exact recovery-copula counterexample holds both sites' probability of needing one human recovery at 0.1 and total expected use at 0.2. Independent recoveries put 0.01 probability on two simultaneous needs, breaking hard capacity one. Mutually exclusive recovery support permits the same two routes under this *one* peak constraint. Local certifications and average labor use therefore do not compose into a network safety certificate; full pathwise joint support, operator windows and abort/fallback choices must be verified. The conservative sum of local maxima is sufficient but may exclude physically staged safe histories. This matters directly for the model's upstream/downstream resource-price certificates and joint qualification bundles, not merely for accounting.

The [new proof ledger](data_value/NETWORK_INTERFERENCE_PROOF_LEDGER.md), [prospective identification/atlas protocol](data_value/NETWORK_INTERFERENCE_EMPIRICAL.md), [scoped dependency-free model](data_value/network_interference.js), [recorded synthetic results](data_value/network_interference_results.json), [student problems](data_value/NETWORK_INTERFERENCE_EXERCISES.md) and [separate complete solutions](data_value/NETWORK_INTERFERENCE_SOLUTIONS.md) preserve assumptions and reproduce the constructed bounds. Existing Models A/B are reductions with independent safe support, additive accepted service and stable captured demand; they are not generally portable to a connected robot/network market. A safe isolating checkpoint may restore independence if its true cost is less than the removed negative externality, but can destroy beneficial shared learning. The actual production/learning empirical panels, operator-tail certificates and numerical official macro production atlas remain missing. The November 22 gate remains an open review, not a passed acceptance criterion.



## Approximate network influence and the distinct hard-support certificate (18 November continuation)

The [bounded-interference continuation](data_value/APPROXIMATE_NETWORK_REMAINDER_THEORY.md) supplies a restricted but useful answer to the last network question: a near-neighborhood surrogate may rank complete adaptive source/grounding/embodiment policies if its **policy-reachable, persistent-regime** transition error is bounded uniformly across matched network histories. With contemporaneous contribution mismatch δ_t, total-variation transition mismatch ε_t and remaining net qualified-production contribution span M_t, a coupling gives \(|J_\theta(\pi)-\widetilde J_\theta^{(r)}(\pi)|\le\sum_t\delta_t+\sum_t\epsilon_t M_t\). Applying this *separately* to two complete policies inside the **same persistent transfer regime** yields a paired robust economic difference certificate; independent post-order uncertainty resetting is not valid. Adaptation, new customer orders, retained policies, data rights and terminal optimized V are accounted through the complete history, not an added price per trajectory. The finite causal-cone sufficient condition is restrictive: synchronous local decisions and transitions, correctly represented controller/dispatch/order edges, and no hidden global operator or checkpoint manager. The general total-variation/coupling and approximate-interference ideas are established mathematical literature, including Leung (2022) and Sävje–Aronow–Hudgens (2021), not new causal-inference estimators.

Applied to the earlier isolated-segment example (old production 7; A share .7 and own gain .5; B share .3), a *hypothetical engineering-supported* local B loss upper bound .6, omitted B loss ≤η, unmodeled A total loss ≤.02 and true additional coordination cost .03 imply complete-network paired gain at least \(.12-.3\eta\). Thus η=.25 yields a **conditional** minimum +.045, while η=.5 cannot certify an advantage. These inputs are synthetic identification conditions, **not** measured robot-market externality bounds. Another finite four-state Q×customer-demand, two-period persistent-regime model tests the full-policy coupling: exact true adaptive grounding barely exceeds retained routine in both constructed worlds, while the local-model error certificate is too loose to identify a positive sign. Numerical positive-looking transfer is therefore not a decision proof. Neither example competes automatically with the safest credible specialist; every other alternative requires its own bounded comparison.

Crucially, a **small economic influence bound never proves hard operator feasibility**. Recovery laws with identical two-site .1 marginals may differ by arbitrarily small total variation yet switch from no simultaneous event to positive support for a two-operator emergency under a peak-one budget. Policy safety is a distinct, physically certified path-support condition; a validated admission/abort mechanism changes the production and learning policy itself. [Proof ledger](data_value/APPROXIMATE_NETWORK_PROOF_LEDGER.md), [prospective network identification](data_value/APPROXIMATE_NETWORK_EMPIRICAL.md), [exact CPU check](data_value/approximate_network_remainder.js), [results](data_value/approximate_network_remainder_results.json), [student exercises](data_value/APPROXIMATE_NETWORK_EXERCISES.md) and [separate solutions](data_value/APPROXIMATE_NETWORK_SOLUTIONS.md) document this boundary. No real qualified customer panel, measured uniform residual, physical safety certificate or BEA/BLS numerical production atlas was obtained; the November 22 gate remains open.


## Continuing integrated theory — structural influence envelopes and physical admission (18 November)

The [causal influence and admission chapter](data_value/CAUSAL_INFLUENCE_AND_ADMISSION_THEORY.md) supplies an auditable **conditional form** for the previously assumed policy-uniform omitted-network error. For complete network states containing controller lineage, operator reservations, customer-order/zero-order opportunities, qualification and adaptive policy memory, suppose a joint conditional coupling gives each block i next-stage mismatch probability at most \(\sum_j C_{t,ij}1\{z_j\ne\widetilde z_j\}+b_{t,i}\) over all candidate policy histories and one persistent transfer regime. Componentwise mismatch bounds obey \(e_{t+1}\le C_t e_t+b_t\). With customer accepted-service/capture bounded-difference weights \(w_t\), **one** terminal optimized V and no extra data price, this gives a pathwise-influence economic error bound \(E\le\sum_t\delta_t+\sum_t w_t^\top\bar e_t\). Same-regime paired comparisons retain the previous error subtraction and separately require physically feasible support. These are standard coupling/influence-matrix ideas, not a proven new theorem or measured robotics relationship.

An important constructive route comparison appears when an independently verified exclusive operator reservation/abort system could make serial deployment safely admissible while checkpoint isolation decreases spillover. In a fully synthetic 70% A/30% B accepted-service comparison, an unstaged shared-controller rollout has lower bounded total contribution 7.06, a staged isolated controller 7.09675, a competent specialist assumed upper 7.08, and retained production 7. If the structural envelopes, full customer calendar, specialist upper and **independent physical reservation+fail-safe certificate** all hold, staged admission beats both specialist and retained options by at least .01675 and .09675, respectively. It is *not* established to dominate open rollout in every regime; the open route lacks an independent safety certificate. A toy semaphore does not certify robots. This is a deliberately adversarial economic choice among productive shared data, deliberately restricted learning and a specialist, not an assumed dataset return.

The same analysis identifies a stronger negative result for identification: knowing all individual controller/robot marginal next-state distributions does not bound **joint** customer bundles or shared recoveries. A fair binary U,V can be perfectly correlated under one law and perfectly anticorrelated under another while both marginals are identical. Policy-uniform C cannot be inferred from incumbent-only logs if a new embodiment broadcasts globally. Under bounded graph degree d and per-edge influence α, a one-shot remote shock β has finite-radius tail \(\beta\sum_{\ell=r+1}^T(d\alpha)^\ell\), decaying geometrically only when \(d\alpha<1\); global replay and market substitution are material failure cases. The [proof ledger](data_value/CAUSAL_INFLUENCE_PROOF_LEDGER.md), [prospective measurement design](data_value/CAUSAL_INFLUENCE_EMPIRICAL.md), [exact-source synthetic model](data_value/causal_influence_admission.js), [results](data_value/causal_influence_admission_results.json) and separate [exercises](data_value/CAUSAL_INFLUENCE_EXERCISES.md)/[solutions](data_value/CAUSAL_INFLUENCE_SOLUTIONS.md) retain the distinction. November 22 review, official BLS/BEA numerical backbone, actual customer qualification panel and safety/independent review remain **open**.


### Auditability of the network production-value certificate (18 November — conditional addition)

The preceding conditional 7.09675 staged lower versus assumed 7.08 specialist upper comparison has only 67/4000=0.01675 normalized units of **already netted** economic slack. If a *previously unbudgeted* joint controller or customer-demand transmission could change the accepted B service by at most 3, its additional policy-uniform trigger must obey \(c+3\min\{1,q_C+q_M\}<67/4000\) to retain strict same-world ranking, where c is genuinely additional isolation cost. An unknown market-demand path alone destroys the certificate even if checkpoint dissemination is structurally disabled. Under a highly demanding *proven dominating event*, iid supported cells and one-sided zero-event binomial inversion, the synthetic q threshold would require 536 independent zero-event exposures in one prespecified cell, or 783 *per cell* in four cells at simultaneous 95% confidence. **This is not** a robot safety experiment prescription, nor a uniform guarantee for unobserved persistent transfer regimes or newly reachable embodiments. Ordinary observed task-success rates do not measure the requisite joint coupling error. Structural verified no-path evidence, safe complete-pool accepted-customer-service comparisons and explicit missing-support intervals are separate evidence routes; operator-exclusive reservation and qualified pre-danger safe stop remain independently required. This sharpens the evidence burden but does not change customer value accounting or price data twice. [Conditional theory](data_value/AUDITABLE_NETWORK_CERTIFICATE_THEORY.md), [proof ledger](data_value/AUDITABLE_NETWORK_CERTIFICATE_PROOF_LEDGER.md), [evidence contract](data_value/AUDITABLE_NETWORK_CERTIFICATE_EMPIRICAL.md), [synthetic code](data_value/auditable_network_certificate.js), [results](data_value/auditable_network_certificate_results.json), [student questions](data_value/AUDITABLE_NETWORK_CERTIFICATE_EXERCISES.md) and [separate solutions](data_value/AUDITABLE_NETWORK_CERTIFICATE_SOLUTIONS.md) document scope. Actual field architecture, qualified service data, versioned replay validation, physical safety and official BLS/BEA backbone remain unavailable. November 22 synthesis still pending.

### Supported complete-policy measurements when global network coupling is unidentifiable (18 November — identification continuation)

A *positive conditional controller-network production certificate* and a *directly identified mean economic policy effect* are different evidentiary objects. The [safe-support derivation](data_value/SAFE_POLICY_SUPPORT_THEORY.md) supplies a constructive alternative to the preceding stringent **cross-world** audit trigger: independently approved whole-interference-network randomization to complete starting-controller/learning/admission policies identifies **average whole accepted-service value** on the safely eligible target stratum, even without observing the persistent latent data-transfer regime. The outcome must include endogenous future customer demand, failed/zero orders, full-service qualification, operator resource cost and nonduplicated terminal production. It cannot be a task-success proxy. This extends the existing safe-pool factorial estimator by confronting **nonrepresentative safety selection** and preserving an actually admissible retained-controller fallback.

If pre-action customer/pool strata have weights w_d, safely enrolled shares e_d, directly identified enrolled route/specialist differences delta_d and bounded unsupported whole-policy payoff range R_d, the hypothetical worldwide difference lies in [A-B,A+B], where A=sum w_d e_d delta_d and B=sum w_d(1-e_d)R_d. These are sharp *only in the unrestricted bounded potential-outcome class*; a global embodiment policy on unapproved states is **not deployable**. Two approved *selective* policies using an identical old version outside safe support instead differ by A under actual isolation and stable treatment environments. A separately justified network residual Gamma and genuinely new cost c yield only A-Gamma-c, not an automatic positive data premium. Synthetic 3/5 and 2/5 strata give A=19/100, unanchored worldwide [-41/100,79/100], specialist-anchored [-11/100,49/100], while a physically admissible isolated selective comparison may have a positive +19/100 difference before its own resource changes. These examples neither revise the earlier 7.09675/7.08 conditional network certificate nor calibrate a real fleet.

Persistent controller updates mean two-period R/G switchbacks are not interchangeable time samples: G→R can yield 22 versus R→R 20 while the post-G R episode alone scores 13 against G's 9. Customer redistribution across nominally separate robot pools can likewise generate A +1 and B -1 without any aggregate production growth. Public version-pinned [Open-RMF dispatcher documentation](https://github.com/open-rmf/rmf_demos/blob/05f5e3faad507c0d67d9343efc81093ee2e30610/README.md) demonstrates *possible* multi-fleet allocation edges but provides no evidence about the actual future target deployment, controller training or recovery safety. Full-network trial support, qualification under new embodiments, worst-transfer-regime dominance and hard physical operator admission remain separate missing tests. The [proof ledger](data_value/SAFE_POLICY_SUPPORT_PROOF_LEDGER.md), [prospective empirical contract](data_value/SAFE_POLICY_SUPPORT_EMPIRICAL.md), [exact synthetic source/results](data_value/safe_policy_support.js), [exercises](data_value/SAFE_POLICY_SUPPORT_EXERCISES.md) and [solutions](data_value/SAFE_POLICY_SUPPORT_SOLUTIONS.md) retain these distinctions. November 22 scientific review still open.


## 18 November — policy-closed networks: when technical transfer changes the measurement unit

The [policy-closed network continuation](data_value/POLICY_CLOSED_NETWORKS_AND_DATA_VALUE.md) addresses the gap after the prior [safe-support result](data_value/SAFE_POLICY_SUPPORT_THEORY.md): even if training is physically approved on an eligible subset, controller updates and market dispatch can change *which other customer production outcomes depend on that intervention*. The correct experimental assignment unit is a union of possible controller, operator, customer and dispatch influence paths **over all approved policies and safely reachable histories**, not merely the observed fallback network. Conditional structural graph closure gives interference components; independently randomized **complete approved network policies** identify a full-network *mean* qualified customer-contribution contrast, including endogenous learning and demand. In contrast, an A-only eligible effect requires an actually verified exclusion cut before SS2's selective fallback identity can be transported.

A new four-independent-network exact construction holds every eligible A customer at an accepted-service gain +2 but gives shared-grounding whole-network values (8,15,8,8) against fallback (10,10,10,10). Shared grounding then reduces mean complete contribution by 1/4; a different isolated, cost-bearing policy gives 23/2 per network and improves over fallback by 3/2. A matched 16-assignment Horvitz–Thompson enumeration identifies the negative shared complete mean, whereas eligible-only qualification cannot. The synthetic contrast tests the *economic production interface*, not claim of negative real-world transfer. When an excluded B baseline is 5, its candidate outcome is only known in [0,10], A improves 5 to 7 and incremental cost is 1/2, the sharp unrestricted whole-policy interval is [-7/2,13/2]. A **verified** controller, operator, dispatch and customer isolation cut collapses B to 5 and gives +3/2; an asserted cut does not.

This result clarifies the earlier data-menu optionality: free optional data access weakly expands qualified production choices if the old safe policies and resource environment remain selectable, but forced global retraining, access rights or market interference can remove that premise. A source-versus-grounding-versus-new-embodiment result must be measured as an actual *complete policy* (including retained frozen checkpoint and competent specialist comparators), not as an additive benchmark percentage or standalone future-data premium. With one connected market, its many robots are not many independent randomization units. The [proof ledger](data_value/POLICY_CLOSED_NETWORKS_PROOF_LEDGER.md), [prospective target evidence schema](data_value/POLICY_CLOSED_NETWORKS_EMPIRICAL.md), [exact source and results](data_value/network_policy_closure.js), and [separate exercises](data_value/POLICY_CLOSED_NETWORKS_EXERCISES.md)/[solutions](data_value/POLICY_CLOSED_NETWORKS_SOLUTIONS.md) make the assumptions falsifiable.

This reuses the established interference designs of Hudgens–Halloran (2008) and exposure-map literature, alongside existing DDA future-data and source-complementarity results, without asserting a novel causal estimator. Public versioned Open-RMF documentation illustrates possible fleet-to-fleet dispatch links, not a deployed robot network or its safety. No target-specific complete opportunity/accepted-service panel, validated architecture, independent approved network randomization, official numeric sector backbone, full repository CI or peer review is now available. The November 22 scientific review and December 25 23:59 Eastern deadline remain unchanged.


## 18 November continuation — verifiable order-loss restrictions as a bridge from connected networks to accepted production

[Full conditional argument](data_value/AUDITABLE_ORDER_LOSS_BOUNDS.md) · [proof ledger](data_value/AUDITABLE_ORDER_LOSS_PROOF_LEDGER.md) · [prospective evidence](data_value/AUDITABLE_ORDER_LOSS_EMPIRICAL.md) · [executable exact calculation](data_value/auditable_order_loss.js) and [results](data_value/auditable_order_loss_results.json) · separate [exercises](data_value/AUDITABLE_ORDER_LOSS_EXERCISES.md) and [instructor solutions](data_value/AUDITABLE_ORDER_LOSS_SOLUTIONS.md).

The policy-closed network identified in the previous section may comprise one connected market; no independent robot-level assignment then identifies complete-policy average outcomes. A structural alternative—not a replacement for randomized evidence—is to record every originally qualified, accepted complete customer-service unit under the retained policy and bound which service can disappear under each proposed **physically admissible full policy**. In a common persistent world, if original B-service contributions are additive \(b_j\geq0\), the candidate's actual A contribution gain is \(a_p\), extra real costs are \(c_p\), lost B-service fractions are \(\ell_{pj}\), genuinely independent additional net-positive B service is \(n_p\geq0\), and residual adverse demand/price/rights effects are \(e_p\geq0\), then

\[
Y_p-Y_F=a_p-c_p-\sum_{j\in B}b_j\ell_{pj}+n_p-e_p.
\]

Suppose a **verified**, horizon-wide, policy-uniform causal/operating envelope imposes \(H_p\ell_p\leq d_p,0\leq\ell_p\leq1\), together with \(a_p\geq a_L,c_p\leq c_U,e_p\leq e_U\). The pointwise lower difference is \(a_L-c_U-e_U-D_p\), where \(D_p=\max\{b^\top\ell: H_p\ell\leq d_p,0\leq\ell\leq1\}\). The established LP dual supplies a resource-like certificate for displaced **accepted customer service**. A single bound \(\sum\ell\leq k\) gives worst loss equal to the sum of the largest k baseline service margins (fractional extension for noninteger k). This is only as valid as the complete-horizon evidence behind its constraint; a dispatcher allowing one simultaneous preemption does not cap annual lost orders at one when demand or learning can cascade.

In the normalized illustrative comparison, routine-source, shared-grounding, embodiment, competent-specialist and pinned-grounding minimum gains are respectively \(0.8,0.8,0.7,0.9,1.8\) under the **separately stipulated**, safe and fully consistent exposure/cost assumptions. The embodiment has the largest enrolled A gain but a lower whole-service guarantee than the specialist. Protecting a particular high-margin baseline order tightens the shared-grounding bound only if its counterfactual protection is genuinely supported. Building a protected router is a distinct cost-bearing **policy**, not merely receiving free data. This is a conditional decision diagnostic, not a measured robotics ranking.

**The core epistemic separation:** independently evaluated target technical transfer does not identify actual \(a_p\); eligible-only A results do not establish total-network B losses; a finite horizon-wide loss cap cannot be inferred from a status-quo controller graph; a whole-network mean does not identify same-world worst-case choice; and no accepted-service economic bound certifies hard operator recovery safety. If original orders are truly additive, expected B loss needs only order-level marginal lost-service probabilities; bundled services and simultaneous recovery require joint outcomes. The November 22 integrated review must retain these separations and distinguish foundational LP/partial-identification mathematics from any possible distinctive robotics production mechanism. The official BEA/BLS numeric backbone, observed complete order registry and actual controller/dispatch/operator causal architecture remain missing; see the new [source/measurement docket](data_value/AUDITABLE_ORDER_LOSS_EMPIRICAL.md).


## 18 November: structural protection versus the cost of losing transferable learning

**Research continuation; November 22 scientific synthesis not yet accepted.** The operative question in the [protection–learning frontier chapter](data_value/PROTECTION_LEARNING_FRONTIER.md) is not simply whether a policy creates additional held-out skills or whether it can be safely isolated from existing qualified service. **Can it retain the new *jointly accepted customer-service production* that originally justified the data investment after the isolation itself changes learning opportunities, operator resources and market demand?** This extends, rather than replaces, the previous [conditional order-loss LP](data_value/AUDITABLE_ORDER_LOSS_BOUNDS.md).

Let F be the original full qualified production/contract/dispatch policy; let p(P) be a separately physically approved data/grounding/embodiment/specialist policy that genuinely protects baseline complete-service bundles P. Under structural B_P state isolation (including the customer order and price process, operator reservations and controller lineage), coupled B_P output is identical pathwise to F, by induction. This is a strong conditional causal modularity assumption, not a fact inferred from public reference architectures or a frozen checkpoint. A market substitution channel can violate it despite independent hardware. If a separate horizon-wide loss budget k is verified for the remaining B\P, the incremental captured-contribution lower certificate is

\[
L(P)=\underline a_p(P)-\overline c_p(P)-\overline e_p(P)-T_k(B\setminus P),
\]

where T_k is the sum of the k largest baseline whole-service margins, and **a_p(P) is evaluated under the new complete policy**, not copied from a shared-controller experiment. Protection changes both the maximum damage and the learning/qualification opportunity. For a fixed k the bound reduction W(P)=T_k(B)-T_k(B\setminus P) is supermodular in P (weighted uniform-matroid rank under complementation), but the true investment certificate need not be: source-to-qualification and physical resource responses can be discontinuous or countervailing. This is a property of what the analyst *can certify*, not automatically an increase in actual production.

An exact counterexample uses the earlier synthetic F=7 and B=(1.2,0.6,0.2). Shared G with accepted A gain 2.4, cost 0.4 and **assumed** one lost B order at most has lower gain 0.8. A protected B1 rule tightens worst B losses by 0.6; if it costs 0.2 and uses resources reducing qualified A contribution by 0.7, its lower gain becomes 0.5, **worse** than unprotected G's 0.8. Full eight-subset enumeration and independent rational checks are in the accompanying code/results. All quantities and the initial loss cap are synthetic assumptions.

The formerly attractive pinned G gain 1.8 assumed a_pin=2.4. Without measured matched pinned service or a valid bridge, a_pin is not identified by shared G and F data. If the pinned and shared **full A accepted-service payoff** distributions, conditional on pre-action customer demand and a persistent learning regime, are within total variation δ at fixed resources; accepted A payoff is in [0,M]; and losing r units of relevant resource reduces expected accepted contribution by no more than Kr, a conditional bridge gives a_pin≥a_shared−Mδ−Kr. At assumed pinned cost 0.6 and shared lower A gain 2.4, pinned G beats a competent specialist **upper** gain of 0.9 only when Mδ+Kr<0.9. No empirical δ,K or capacity cut has been verified. Indivisible qualification thresholds defeat generic small-r smoothness; a 0.01-unit loss can eliminate the whole qualified bundle.

This bridges the manuscript's static production-price certificates, O-ring qualification bundles, data-source choice and adaptive learning with the *network* of demand and physical resource connections. Retained F, competent S, productive source R, shared/isolated G and any separately safe E remain distinct options. No benchmark percentage is converted into customer dollars, no continuation value is double-counted, no receipt is attributed to an unaccepted skill, and no real order or safety guarantee is claimed. Interference, supermodularity of the bound and TV inequalities are established mathematics; no scientific novelty is asserted by recombination alone. Testable next proof gap: actual full-horizon B structural exclusion and the loss of A joint qualification under pinning, rather than a further numerical finance/default contract.


## 18 November continuation — separating production-data observation from controller actuation

The [shadow-learning and target-support argument](data_value/SHADOW_LEARNING_AND_TARGET_SUPPORT.md) completes a missing link in the preceding protection–learning frontier. The earlier order-loss certificate correctly charges a controller-pinned policy for forgone *A* qualification and lost accepted service. But pinning *B actuation* is not synonymous with quarantining or deleting *B source trajectories*. A third feasible architectural choice may exist: continue competent B production on its retained controller, read permitted source records into a separate offline A learner, then admit a genuinely qualified A recipe only after independent validation. A's eventual admission remains a full-network intervention and can alter B demand/recovery. This is a structural possibility, not a claim that a target system implements the split.

**Conditional separation.** Before A admission, if copied data are entirely produced under F, their capture/rights/compute/operator overhead create no causal path into B, and B's demand, pricing, dispatch, controller and safe recovery laws remain closed and unchanged, coupled B original-order paths and margins agree with F by induction. The result does not depend on whether A learns. Read-only API permissions are insufficient if resource constraints or customer offers still couple sites. At admission, the stronger policy-closed-network or horizon-wide original-order protection argument from preceding sections is still required. Extra free, optional information only weakly expands the optimizer's feasible menu; it does not guarantee technical skill, customer qualification or positive net value after costs.

**Identification obstruction.** Two latent worlds may have precisely the same F production trajectories and offline A metrics while the target A action, never tried in F, is successful in one world and not in the other. Therefore source volume and target occupancy coverage do not identify A's accepted complete-service gain. Under a declared ex-ante customer distribution μ, truly identified A complete-order mean m(x) on C, unsupported U and per-cell bounded incremental contributions [0,M(x)], the conditional additive contribution lies in [∫C m dμ,∫C m dμ+∫U M dμ]. Its simple endpoints are sharp only without additional joint feasibility constraints; physical recovery is a separate admissibility test. In a constructed 3/5-supported, 2/5-unsupported example the net candidate interval is [1/20,17/20] against a competent specialist 2/5, and the decision requires the unknown high-stratum whole-order mean to exceed 7/8. The numbers are normalized hypotheses, not data-derived robotics economics.

**Joint learning and temporal opportunity.** If two essential A qualifications have marginal successes 1/2 and 3/4, their joint success spans [1/4,1/2] without conditional independence, and production requires the *joint* event. Under two remaining dates of qualified unit service and cost 1/4, forced net return spans [1/4,3/4] (1/2 under independent events). If validation finishes after target customers disappear, forced return is −1/4; the retained F option gives zero incremental value ex ante. This is not a second data option premium: it is the endogenous continuation inside V(Q;ω). The demand window, learned controller support, source rights and safe approval jointly determine whether transferable data have economic use.

This substantially strengthens the manuscript's conceptual countermodel to “protecting existing service necessarily destroys transfer”: **data reuse and actuation sharing need not be the same scarce technology**. It also rejects the opposite overclaim that a free production log qualifies an unsupported target action. Prior-art boundaries include DDA §5 and Appendix B (future data and complementarity), offline/safe policy improvement and deficient-support partial identification. The novel scientific contribution remains unsettled. The empirical test is a permission- and controller-versioned copy-only versus pinned-grounding versus shared-update comparison measuring original B orders, *joint* held-out A customer acceptance, resource queues and source-selection rights. No robot field tests or hard safety checks have been performed.


## 18 November — observational support versus developmental transfer: one production-value argument

The linked [passive support/decision-regret chapter](data_value/PASSIVE_SUPPORT_AND_DECISION_REGRET.md) supplies an exact *information versus qualification* distinction within the existing Q, omega, V, J architecture. A rights-cleared shadow record can improve A's joint qualified technology T without identifying an otherwise unsupported target service; alternatively a safe target report can improve selection between *already approved* A and S without changing the technology. Neither improvement is an independent data dollar premium after the induced accepted production has been counted in J.

Using the same earlier supported/unsupported customer example rather than a new parameter set, A has net 1/20+(2/5)x for x in [0,2] versus a competent specialist's 2/5. The critical unsupported whole-service mean is 7/8. Two observationally equivalent F-source worlds imply minimax selection regret 63/320; arbitrarily many identical passive logs cannot distinguish them. With a *hypothetical, separately approved, fixed-menu* 1/5-error target diagnostic across the endpoint worlds, the exact minimax regret is 63/740 under the randomized response (A always for positive, A with probability 2/37 for negative), a reduction of 1323/11840 before cost and lost time. This is **decision regret**, not source-data economic price or measured customer dollars. The bound is inapplicable to unapproved target actions, changed qualification, operator competition or endogenous demand; evaluate those through full J.

A countermodel demonstrates why zero passive information does not imply zero transfer: if a separately verified optional shadow-learning transition raises A's *whole-service* contribution by at least 7/20 in both otherwise indistinguishable worlds, A becomes weakly dominant without learning theta. This is a conditional mechanism, not evidence that more F trajectories supply such improvement. Target grounding modifies observation support and possibly Q; changing embodiment alters required action/recovery/joint recipe support, potentially removing or creating unidentified edges. Existing source-to-production and resource-price identities remain in force. Prior-art boundaries include standard minimax decision theory, support-deficient off-policy evaluation and DDA's existing endogenous data value; empirical validation and novelty are open.

**Proof and reproducibility:** [ledger](data_value/PASSIVE_SUPPORT_PROOF_LEDGER.md), [exact synthetic code](data_value/passive_support_decision.js), [results](data_value/passive_support_decision_results.json), [prospective evidence](data_value/PASSIVE_SUPPORT_EMPIRICAL.md), [student exercises](data_value/PASSIVE_SUPPORT_EXERCISES.md) and [separate solutions](data_value/PASSIVE_SUPPORT_SOLUTIONS.md). The November 22 integrated argument/Models A-B scientific gate is not passed; no field trial, safety approval, whole-order demand panel, official quantitative backbone or independent novelty audit is claimed.


## Source learning changes its own target support (18 November theoretical continuation)

The new [policy-induced support chapter](data_value/POLICY_INDUCED_SUPPORT_FRONTIER.md) closes a conceptual gap between passive F data, target grounding and economic whole-service value. A learned A controller may visit different action/recovery/customer states than retained F or its previous checkpoint. For a fixed, physically approved target policy with a genuinely identified **joint whole-network** conditional kernel on a prespecified history/action support, first exit has identified probability p and no-exit total captured contribution K. With complete Y∈[L,U], the conditional envelope is E[Y]∈[K+Lp,K+Up], with sharper prefix-specific lost-order bounds only from audited actual constraints. This is standard stopped-process identification, not scientific novelty.

Illustrative independent source-copy learning that lifts accepted c service and retains identical occupancy can produce a conservative gain over competent S without identifying unsupported u; separately approved grounding can instead bound u, while full-support new embodiment can still lose to S. But a learned controller that changes its own unsupported-state probability invalidates the original source-copy comparison. This gives a concrete matched empirical priority: source-copy versus no-copy **joint** Q and complete-service effects, separately measured safe target occupancy for each checkpoint, plus pre/post-admission B orders and demand/operator closure. No target field approval, whole-order evidence or quantitative industry backbone exists. [Proof ledger](data_value/POLICY_SUPPORT_PROOF_LEDGER.md), [protocol](data_value/POLICY_SUPPORT_EMPIRICAL.md), [exact model/results](data_value/policy_support_frontier.js) and [student](data_value/POLICY_SUPPORT_EXERCISES.md)/[instructor](data_value/POLICY_SUPPORT_SOLUTIONS.md) packets accompany this section. Nov22 scientific gate remains open.

## Comparing data-trained policies under shared unsupported customer uncertainty (18 November)

[Comparative first-exit theory](data_value/COMMON_EXIT_VALUE_COMPARISON.md) sharpens the previous learned-policy support envelope **without declaring its missing physical support resolved**. Two independently approved complete policies a,b can have separately identified *own-policy* first-exit probabilities p_aj and p_bj and known qualified-service/prefix/cost terms K_a,K_b. **Only** where a versioned, full-network customer/order/recovery conditional continuation u_j(theta) is the same unknown *within a persistent world theta* do we obtain J_a-J_b=K_a-K_b+sum_j(p_aj-p_bj)u_j(theta). Under a rectangular common-residual identified set [l_j,h_j], the conditional exact contrast has width sum_j |p_aj-p_bj|(h_j-l_j), rather than sum_j(p_aj+p_bj)(h_j-l_j) from subtracting separately worst/best policy levels. This is standard partial identification/common-nuisance cancellation, not an independently novel finding.

The same earlier source/no-copy synthetic customer service witness, **now with changed learned-policy occupancy**, has K_copy=27/20,p_copy=1/2, K_no=7/5,p_no=1/4, shared u in [0,4]. The same-world difference is -1/20+u/4 in [-1/20,19/20], versus independently subtracted [-21/20,39/20]; no uniform ranking. An independently valid diagnostic that *only* establishes u in [3,4] would conditionally narrow the difference to [7/10,19/20] but is not a policy training gain. This reuses the earlier example and changes the information structure, not an arbitrary calibration sweep. It does not establish superiority to the qualified S=2 comparator or authorize physical intervention.

Critically, the common residual is far stronger than identical terminal state names or separate robot success marginals. Changed recoveries, embodiment, original B orders, dispatcher/operator competition or customer-demand feedback can make post-exit responses differ; two policies with equal p may then have unidentified contrast. Known bounded policy-specific deviations widen the paired certificate by their occupancy-weighted bounds, **only when audited over the whole service horizon**. More source data can raise K while shifting p; deliberate target grounding can restrict residual uncertainty or modify Q/p; new bodies change essential recipes and support. Evaluate each through the same V(Q;omega) and dynamic J, retaining F/S optionality and one count of costs, not an extra data premium.

The [proof ledger](data_value/COMMON_EXIT_PROOF_LEDGER.md), [prospective empirical falsifiers](data_value/COMMON_EXIT_EMPIRICAL.md), [exact executable comparison](data_value/common_exit_comparison.js), [saved results](data_value/common_exit_results.json), [student exercises](data_value/COMMON_EXIT_EXERCISES.md) and [separate instructor answers](data_value/COMMON_EXIT_SOLUTIONS.md) extend the existing teaching and reproducibility program. Ross–Gordon–Bagnell (2011) and Khan–Saveski–Ugander (2023) are prior-art boundaries for policy-induced distributions and off-policy partial identification. Actual K,p, full-network conditional equivalence, safe intervention, numeric BLS–BEA sector quantities and independent novelty remain unverified. The November 22 gate remains **open**.


## Partial post-exit policy invariance: the data-transfer comparison when controllers do not share a recovery law (18 November)

The [paired policy comparison](data_value/COMMON_EXIT_VALUE_COMPARISON.md) previously assumed identical unobserved whole-network continuation under copy and no-copy. This is rarely warranted by training history alone. We retain the same dynamic customer accepted-service objective J, source-to-joint-qualification map, original-order census, operator/recovery constraints and approved F/S alternatives, but permit policy-specific post-exit mean contribution u_ij within [l_j,h_j]. A structurally or safely matched **joint** bound |u_aj-u_bj|<=eta_j is an additional, auditable assumption, not learned from source observations.

When K_i and own-policy first-exit probabilities p_ij are identified and the residual pair sets are rectangular across labels, the sharp paired economic lower/upper bounds equal the common-residual signed-occupancy extrema, widened by sum_j min(p_aj,p_bj)*eta_j. This sharp interpolation goes from complete equality (eta=0) to independent residuals (eta=h-l). A worked [exact source model](data_value/paired_residual_sensitivity.js) reuses the prior copy/no-copy K,p and [0,4] residual, with eta=1/2 producing [-7/40,43/40], compared with common [-1/20,19/20] and fully unrestricted [-21/20,39/20]. Two otherwise observationally indistinguishable pre-exit worlds attain opposite economic rankings. Thus improving source transfer cannot by itself establish common recovery, and a diagnostic reducing the residual identified set does not create an added data-value line item.

An identical approved fallback might establish eta=0 **only** if the same full market/order/dispatch/operator/remaining-time state and action law can be guaranteed across policy versions. Existing offline policy baseline-bootstrapping research (Laroche et al., 2019, https://proceedings.mlr.press/v97/laroche19a.html) is important prior art, not evidence of such an industrial robotics architecture. The [proof ledger](data_value/PAIRED_RESIDUAL_PROOF_LEDGER.md), [audit protocol](data_value/PAIRED_RESIDUAL_EMPIRICAL.md), [student exercise packet](data_value/PAIRED_RESIDUAL_EXERCISES.md) and [separate solutions](data_value/PAIRED_RESIDUAL_SOLUTIONS.md) preserve the assumptions and falsifiers. No real paired target trial, original-order signoff, target occupancy, nontrivial eta or physical admission is verified. The November 22 scientific synthesis and BLS–BEA numeric backbone remain OPEN.


## The causal and production-valued source/grounding interaction: joint qualification, not individual skill rates (18–19 November)

The [factorial qualification/whole-service chapter](data_value/JOINT_QUALIFICATION_FACTORIAL_VALUE.md) supplies a constructive alternative to repeatedly postulating small unknown eta in the previous matched-continuation bound. Under one qualified policy-closed customer-network horizon, the intervention arms source-use x=0/1 and target grounding g=0/1 produce a **joint** qualification law pi_xg(q), a possibly changed optimized whole-service table f_xg(q) and all-in cost c_xg. Their full captured contribution is J_xg=sum_q pi_xg(q)f_xg(q)-c_xg. The second difference I=J_11-J_10-J_01+J_00 is an economic intervention interaction, **not** a constant data-transfer rate. Choosing one reference table f_00 gives an exact decomposition into (i) the **joint** qualification distribution second difference valued at baseline customer economics, (ii) the policy-specific whole-network demand/resource/order response, and (iii) interaction in rights/training/validation/deployment costs. This decomposition is algebra; its component attributions require counterfactual baseline production support and are not automatically separately identified.

A particularly discriminating counterexample makes marginal target pass rates 1/2 in **all** four arms. Independent joint outcomes under 00/10/01 and perfect positive versus negative dependence under 11 give source-grounding interaction +1 versus -1 for a jointly required customer service worth 4 normalized units; individual task success rates are identical. A second exact example shows a +1 joint-qualification interaction canceled by -1 in customer/resource response, yielding zero economic interaction. Thus adding data can create technical complements without creating incremental *enterprise production*. Shared-resource substitution or displacement of original B orders can reverse a positive A-service gain. Preserve the previous independence-based Hessian as a conditional benchmark, not a general fact about qualification.

Under genuinely independent **policy-closed whole networks**, safely approved four-arm randomized policies, and a pre-treatment customer opportunity registry, ordinary design-based factorial comparison identifies the population-average whole-service interaction **without assuming a common post-exit eta**; it is not a per-site guarantee, new estimator, or physical safety authorization. Controller learning, dispatch, operators and customer demand must not leak across randomized network units; otherwise the causal estimand is a different interference experiment. If any arm lacks physical approval, a training-only experiment identifies development outcomes, not unsupported deployment revenue; missing defined economic effects remain partially identified. Changing embodiment h changes the feasible service/qualification set and f, not merely a transfer scalar. Free optional source *availability* weakly expands a retained old-policy menu, but forced training and acquisition can destroy value.

The [proof and rejection ledger](data_value/JOINT_QUALIFICATION_FACTORIAL_PROOFS.md), [prospective customer/service protocol](data_value/JOINT_QUALIFICATION_FACTORIAL_EMPIRICAL.md), [executable exact dyadic model](data_value/joint_qualification_factorial.js), [record](data_value/joint_qualification_factorial_results.json), [exercises](data_value/JOINT_QUALIFICATION_FACTORIAL_EXERCISES.md) and [separate solutions](data_value/JOINT_QUALIFICATION_FACTORIAL_SOLUTIONS.md) accompany the result. This integrates standard production optimization, joint-outcome probabilities and factorial causal identification; no scientific novelty, empirical robotics result, approved whole-network randomization, certified eta, numerical BLS–BEA production crosswalk or final Nov22 acceptance has been established.


### Conditional adaptive qualification and endogenous investment: why static policy means do not value the staged data menu

The [adaptive source–grounding–embodiment chapter](data_value/ADAPTIVE_QUALIFICATION_MENU.md) continues the **same** qualified-production objective after the whole-network factorial result. A randomized, physically approved source-use × grounding comparison may identify static arm means and the average whole-service interaction. Yet neither those means nor individual skill rates identify the economic value of training on source data *first*, observing a jointly accepted customer qualification, and buying grounding only on failed targets. That value depends on cross-arm qualification dependence and, when learning is sequential, a further history-conditioned transition. The previous within-arm joint-qualification objection and the new **cross-policy** joint-potential-outcome objection concern different probability laws and must not be conflated.

For retained qualified fallback contribution s, alternative source-qualified contribution a and grounded contribution b, potential qualification marginals p and q and overlap t, the (approved) two-test option has gross value

    s+(a-s)p+(b-s)q-[min(a,b)-s]t.

The Fréchet bounds on t produce sharp unrestricted menu-value bounds. When a≥b and grounding is purchased *only after* source qualification failure, with no source→grounding carryover, the value is

    s+(a-s)p-c_x+max{0,(b-s)(q-t)-c_g(1-p)}.

If source training changes later grounding, the correct target object is a new history-conditional Q_(g|x) law, not the static overlap t. This distinction is an empirically meaningful reason to study production-generated source trajectories and deliberate target interventions as distinct investments. It avoids a free-floating price per trajectory or treating a benchmark percentage as customer revenue.

A complete synthetic comparison fixes s=2,a=b=4, p=q=1/2 and cost 1/5 per test. A disjoint source/grounding success coupling gives net staged value 37/10 while a perfectly concordant coupling gives 14/5, although both have the same static policy arm means; the optional choice to buy second-stage grounding reverses. An even/odd parity construction further shows that identical single and pairwise potential qualification probabilities among source, grounding and redesigned-body alternatives can yield three-test option values 29/10 versus 17/5. Both are standard mathematical counterexamples, not observed robotics or scientific originality. The [proof ledger](data_value/ADAPTIVE_MENU_PROOF_LEDGER.md), [prospective matched/sequential protocol](data_value/ADAPTIVE_MENU_EMPIRICAL.md), [exact reproducible diagnostic](data_value/adaptive_menu_copula.js) and separate [student](data_value/ADAPTIVE_MENU_EXERCISES.md)/[instructor](data_value/ADAPTIVE_MENU_SOLUTIONS.md) materials make the assumption and evidence boundary explicit.

**Integrated implication.** The candidate economics of robot data is not just the economic interaction among source features within a fixed learner or even the source–grounding factorial interaction of complete rollout policies. It also depends on whether evidence about one option reveals which *other* admissible technology is worthwhile, and whether training that option changes the later options. A valid paper claim must clearly specify the policy/experiment level of its estimand and include original customer orders, alternative qualified services, opportunity windows, resources, embodiment lead times, rights and retained policies. Conditional static source/grounding decisions, their adaptive information value, customer network spillovers and actor-specific cash constraints belong in the same model without duplicating production benefits.

Murphy (2003) dynamic treatment regimes and established joint-potential-outcome/Fréchet partial identification are closest conceptual prior art; DDA §5/Appendix B already handle data feedback and aggregation. Physical approved paired or sequential trials, signed customer/operator/dispatch lineage, BLS–BEA numerical production backbone, original novelty audit and the November 22 synthesis gate remain unverified. The final cutoff remains December 25, 2026, 23:59 America/New_York.


### 19 November UTC: Direct sequential policy value versus unknown qualification coupling

[Direct sequential-policy identification](data_value/SEQUENTIAL_POLICY_VALUE.md) refines the *same* data-to-qualified-production argument. Static source×grounding fixed policy means cannot identify cross-policy joint qualification t or after-source-failure grounding law r. But an independently approved whole **policy-closed customer network** experiment, randomizing source-failure eligible networks to buy target grounding versus retain already-qualified F/specialist S, directly identifies the *economic continuation policy effect* under pre-random history, positivity, consistency and no between-network learning/dispatcher/operator/customer interference. It includes qualified accepted A, original retained/displaced/unattempted B orders, endogenous demand/target occupancy, operator/resource exposure, testing/manufacturing rights/costs and capturable contribution once, without a separate data premium. This identifies a policy choice, not its technical transfer mechanism or an untested embodiment. Exact synthetic signs and a conservative independent-network precision certificate show why the active scientific difficulty is safely approved complete customer outcomes, not another arbitrarily assumed technical joint coupling. Public DROID/OXE technical source data is distinct from commercial field evidence. No Nov22 gate, independent novelty, safety approval or customer economic calibration.


## Source-first screening changes the economic allocation of later grounding and new embodiments (18 November Eastern continuation)

The [source-selection chapter](data_value/SELECTION_AND_SEQUENTIAL_DATA_VALUE.md) applies the established V(Q;omega) and complete network-policy J to the same issue left by direct adaptive-policy identification. A grounding effect measured among failures after source policy x0 cannot generally be transported to failures after source x1, because x1 changes which qualified whole-service opportunities remain, the information disclosed by their failure, and possibly demand and recovery. In a *restricted nested-success and invariant downstream continuation* case, the conditional effect obeys pi0 delta0=pi1 delta1+m delta_removed. If the newly resolved failures are relatively favorable to grounding, the remaining failures can rationally favor a **changed embodiment** even with no change in either downstream technical transfer map. Exact two-type complete-service example: x0 selects grounding with incremental 3/5; x1 qualifies easy services, then selects the new body for the remaining hard cases, giving 33/20 before and 27/20 after paid source expense. A separately available costless informative pre-choice diagnostic at x0 instead yields 29/20 and reverses that paid-source choice. These are synthetic countermodels—not field values, originality or hardware safety findings.

This selection mechanism is **not** a replacement for the common qualified-production and dynamic investment model: each extra accepted customer order is worth its actual optimized captured increment, and rights, compute, operator, deadline and displaced incumbent orders enter Y once. Static factorial production means, cross-controller qualification overlap, history-conditioned technical transfer and directly randomized eligible complete-policy economic value remain four different estimands. A source first-stage randomized design plus independently approved within-source whole-network continuation comparisons can in principle identify each regime's policy effect, but not an individual cross-regime principal stratum merely by conditioning on failures. The main scientific gap is genuine versioned source/controller/dispatch/operator/order evidence and an admissible source-policy comparison, not further arbitrary coefficient scenarios. November 22 synthesis and all later gates remain open.


### Source-policy estimands, non-identification of transfer coupling and support-certified investment (19 November UTC)

The [November 22 estimand reconciliation](data_value/NOV22_ESTIMANDS_SUPPORT_SYNTHESIS.md) consolidates the manuscript's source-to-qualified-production decision architecture rather than adding a fifth standalone model. Independently randomized approved source policies and conditionally randomized stage-two whole-network continuations identify each regime's **population average adaptive economic value** from prechoice histories, qualified accepted customer production and costs, even if cross-regime paired technical qualification overlap remains unobserved. But their comparison does **not** identify a monotone individual technical-learning mechanism. Two exact potential qualification populations with identical 1/4 versus 3/4 marginal success and identical dynamic economic values (5/4 and 7/4) have paired overlaps of 1/4 and zero: one has no technical regressions, the other has 1/4 regressions. This rejects interpreting a profitable source-policy comparison as evidence of uniformly positive transfer.

The [proof ledger](data_value/NOV22_ESTIMANDS_PROOF_LEDGER.md) and [prospective original-order registry](data_value/NOV22_ESTIMANDS_EMPIRICAL_REGISTRY.md) also give a conditional decision use for incomplete stage-two support: maximize approved fallback-and-training actions over valid lower/upper conditional whole-customer contribution. Under freely varying conditional response laws those bounds are sharp; shared persistent regimes or market/resource laws can tighten them and must not be rectangularized without justification. Exact synthetic source-policy contrast is [1/4,3/4] with partial approved-target support, but becomes [-3/20,7/20] after real source expense 2/5. An **unapproved** changed body cannot be counted as a missing-value feasible arm. This standard dynamic-regime/partial-identification construction illustrates why source data, target diagnostic grounding, new embodiment and retained competent fallback must be compared on a common qualified customer-order accounting basis, with no extra future-data premium. [Reproducible exact source](data_value/nov22_estimand_support.js), [saved output](data_value/nov22_estimand_support_results.json), [student exercises](data_value/NOV22_ESTIMANDS_EXERCISES.md), and [separate solutions](data_value/NOV22_ESTIMANDS_SOLUTIONS.md) accompany the result; no real customer/operator panel, physical approval, numeric BLS–BEA backbone or Nov22 scientific acceptance was obtained.


## Information value versus admitted robotic capability (19 November 2026)

Source data play two causally different roles: they can generate a **nonactuating** pre-choice signal about existing qualified customer-service options, and they can train an embodied controller that changes the joint qualification and network production frontier. A four-estimand source-policy comparison identifies the complete adaptive economic value under sequential randomization, but not the mechanism. The [controlled information/admission chapter](data_value/SIGNAL_VS_ADMISSION.md) defines `W(c,i)` as whole-network captured accepted-service value with controller admission c and report disclosure i, and derives `W11-W10-W01+W00 = (W11-W10)-(W01-W00)`. Under an invariant and optional report, Blackwell information weakly increases value at each c; **the interaction has no fixed sign**. Controller improvement can substitute for target-state information by making a route uniformly qualified/economic, or complement information by making a new approved target service worthwhile only after a sufficiently accurate customer-state report. Qualified specialists and the actual original-order network remain in V, not an added data premium.

The exact synthetic high/low customer-service construction with a qualified specialist yields interactions -7/8 and +1/2 in alternative training mechanisms and a joint paid acquisition that beats retention only with sufficiently accurate report support. This does not measure transfer, license physical deployment, or establish originality. The prospective C×I whole-network protocol requires a fixed source snapshot, separately approved controller admission, genuinely noninvasive report and immutable initial customer-order registry; without them the observed factorial is a mixed policy effect. This clarifies the November 22 theorem/assumption mapping while preserving the broader embodied/data/production/demand/finance feedback model and December 25 deadline.


## 19 November continuation — source-trained report transport and the value of target calibration

The [signal-kernel transport chapter](data_value/SIGNAL_KERNEL_TRANSPORT.md) develops the assumption the preceding information × controller result had left fixed: a source-trained controller can alter the **distribution and conditional meaning of the report itself**. Its before/after signal confusion matrix is not necessarily invariant, even if the source data improve one technical qualification. Under one fixed approved complete policy menu, original pre-source customer population p(z), and whole-network payoff y_c(a,z) inside V(Q;omega) and J, a source report K and target report K' are two distinct conditional experiments. Let R_c(z) be the span of qualified full-service contribution among currently approved continuation actions in state z. The fixed-controller optimized report values satisfy the conditional total-variation bound

\[
|W_c(K')-W_c(K)|\leq \sum_z p(z) R_c(z)\operatorname{TV}(K'(\cdot|z),K(\cdot|z)).
\]

Using the source-optimal decision rule after kernel drift incurs target regret at most twice that conditional bound. A stronger per-report *economic action-margin* inequality establishes when the source rule remains target-optimal; this requires state-level **relative qualified customer contribution**, not only statistical classification accuracy. These are conditional standard TV/decision-regret results, not physical certification or novel mathematics. If the controller changes physical qualification, operator recovery, market demand, target occupancy or support, a fixed-kernel bound is **not** a valid cross-controller causal comparison; full intervention-dependent J and previously derived support/whole-network identification remain necessary.

The exact earlier qualified specialist/G/T synthetic example exposes a consequential difference in data-investment reasoning. Source-report accuracy 9/10 selects a high-report T service, but a target accuracy of 3/5 makes blindly retaining that rule worth only 3/8, compared with retained G value 1. Optimizing the *same* physical qualified menu under the actual target kernel yields 43/40, not a negative value of optional information. The 7/10 target stale-rule regret does **not** imply a 7/10 value of buying more calibration data: with target accuracy equally likely 3/5 or 9/10, revealing accuracy before the individual report is worth only 1/10 ex ante to a planner already optimizing with the mixture kernel. This is the usual Bayesian information-value calculation applied to qualified whole-order service, not a field estimate. Under a target accuracy ambiguity interval [3/5,9/10], the fixed qualified rule (G,S) gives the full deterministic-or-randomized maximin value 43/40; this is not proof a real customer network has such uncertainty support.

This clarifies the unchanged source/target/new-body acquisition choice. Source trajectories can simultaneously help learn technical actuation and produce a decision report; **target report grounding** can repair/validate information without qualifying a new controller, while **physical target grounding** and an **altered embodiment** change the approved service/production envelope and require their own customer, recovery, manufacturing and operator tests. Market demand and resource/cash constraints remain inside J, with no added dataset price or twice-counted terminal value. A versioned nonactuating shadow-report protocol, [proof ledger](data_value/SIGNAL_KERNEL_TRANSPORT_PROOFS.md), exact [source/results](data_value/signal_kernel_transport.js), and separate [student](data_value/SIGNAL_KERNEL_TRANSPORT_EXERCISES.md)/[instructor](data_value/SIGNAL_KERNEL_TRANSPORT_SOLUTIONS.md) materials document the conditional result. A public [performative prediction](https://proceedings.mlr.press/v119/perdomo20a.html) foundation expressly warns that model-directed actions change target distributions; this work does not duplicate its equilibrium theorem. DDA future-data and complementary aggregation results remain credited. All field support, numerical BEA/BLS evidence, originality and November 22 scientific acceptance remain open.


## November 19 — incomplete target shadow-report support is an economic identification problem

The [partial target report-support chapter](data_value/REPORT_SUPPORT_IDENTIFIED_VALUE.md) extends the fixed-controller report-transport result when a *commercially defined pre-action target opportunity* has no verified report conditional row. Under explicitly rectangular unknown target rows, the sharp worst contribution for a possibly randomized qualified policy is the known-row expectation plus the unobserved-row minimum over reports; optimize over retained complete-service policies rather than importing source accuracy. If one population conditional row is subsequently independently identified, the conservative maximum can rise by at most that pre-action state's probability times its whole-service contribution span. This is an identified-set/maximin property, not expected data-purchase value or physical transfer.

The same synthetic qualified F/S/G/T customer-service table produces a robust G=1 with a known high-state 3/5 row and unknown low row **even over randomized report decisions**, because a permitted uninformative target kernel bounds every contingent policy. Exactly certifying low-state high-report probability 2/5 changes the rational choice to G/S at 43/40, a 3/40 improvement in the *guarantee* rather than a predicted cash premium. Three kernel pairs with the same pooled 60% classifier accuracy give distinct optimal service values and sometimes distinct recipes. The [proof](data_value/REPORT_SUPPORT_PROOFS.md), [source/results](data_value/report_support_value.js), [prospective original-order protocol](data_value/REPORT_SUPPORT_EMPIRICAL.md) and separate [student](data_value/REPORT_SUPPORT_EXERCISES.md)/[instructor](data_value/REPORT_SUPPORT_SOLUTIONS.md) packets preserve that distinction. Public DROID/Open X support technical route research but not customer-order labels; BLS/BEA numerical comparable-vintage crosswalk and qualified field trials remain missing. The November 22 science gate remains open; December 25 23:59 Eastern unchanged.


## Finite target-report evidence and economically allocated safe shadow audits (19 November 2026)

The [finite target-row confidence chapter](data_value/TARGET_ROW_CONFIDENCE_THEORY.md) replaces the preceding report-support proposition's idealized exact conditional probabilities with a prospectively *pre-action*, independently sampled target shadow reporter. In the same already-qualified whole-network production value V(Q;ω) and J, simultaneous fixed-n Hoeffding row intervals C create a rectangular robust lower certificate G(C)=max_π min_{K∈C}V(π,K) **over randomized report-contingent qualified-service rules**. Conditional on the true target rows belonging to C,

\[
0\le W(K_\ast)-G(C)\le \sum_z p_zR_z\,\operatorname{width}(C_z),
\]

where p_z is the original customer opportunity share and R_z is the span of *complete* qualified-service contribution (customer alternative, acceptance, displaced orders, scarce operator/dispatch resources and capture). This is a sharp fixed-rule endpoint calculation with a possibly conservative optimized-value gap, not an estimate of the value of paying for calibration or a physical-learning theorem. A qualified old controller/specialist remains selectable throughout. If the target state has zero difference among qualified alternatives, its report accuracy has zero immediate economic decision value in this *fixed* production menu.

The economic weighting gives a constructive design implication: minimizing an unclipped conservative confidence-width upper bound under a fixed permitted independent target-label budget yields n_z∝(p_zR_z/d_z)^{2/3} for per-label costs d_z, properly normalized. Rare high-displacement opportunities can therefore receive more labels than their customer-order frequency suggests. That is **not** a universal source-mixture rule: training, grounding or new embodiment can alter p, R, qualification Q, support, rights and costs. In the inherited synthetic four-service table, the G-after-high/S-after-low rule improves on retained G only when 9ℓ_H−7u_L>2. Exact saddle certificates (rather than a generally invalid pure-rule maximin shortcut) give G=1 for hypothetical 100/400 independent observations per original H/L stratum and small positive guaranteed G/S improvements for 1600/2000, under fixed-n simultaneous 95% bands. These are **invented sampling scenarios and invented production payoffs**, not empirical robot sample sizes or earnings.

The negative identification counterpart is essential: if target labels are recorded only on accepted high-report orders and the original opportunity denominator is lost, target low-state report laws 2/5 and 3/5 can generate identical selected records but different optimized *whole original-order* values 43/40 and 1. Neither more selected data nor pooled accuracy repairs that selection. The [proof ledger](data_value/TARGET_ROW_CONFIDENCE_PROOFS.md), [prospective audit registry](data_value/TARGET_ROW_CONFIDENCE_EMPIRICAL.md), [executable](data_value/target_row_confidence.js) and [results](data_value/target_row_confidence_results.json), [Nov22 Model A/B bridge](data_value/NOV22_TARGET_ROW_CONFIDENCE_MODELS_AB.md), and separate [student](data_value/TARGET_ROW_CONFIDENCE_EXERCISES.md)/[instructor](data_value/TARGET_ROW_CONFIDENCE_SOLUTIONS.md) packets state conditions and discriminating checks. No approved target reporter, original customer order sample, scientific novelty proof, numerical BEA–BLS official crosswalk, or passed November 22 gate exists. The final deadline remains December 25, 2026, at 23:59 Eastern.


## Continuation: when customer production selects the data available for target grounding

The immediately preceding finite target-report analysis assumes independently sampled *original* pre-action customer opportunities. That is stronger than recording only the reports encountered during successful productive robot deployments. Let a frozen, physically approved reporter's latent pre-action output S be h or l; its record O can be selected by customer admission, dispatch, controller recovery and dataset-retention rules. Even with the entire original customer-order count N, observing the selected high share a and selected low share b identifies the target high-report probability only in the **sharp missing-data interval [a,1−b]**, absent a validated recording mechanism. With conditional recording probabilities ρ_h,ρ_l, the restrictions a=qρ_h and b=(1−q)ρ_l expose exactly which positive-propensity audit can improve support. A fixed-n original-order sample gives simultaneous conservative confidence sets via selected-category Hoeffding indicators, while correlated or after-action records cannot inherit iid coverage.

A counterexample within our *same* qualified F/S/G/T whole-customer-service menu holds the original-order denominator and all observed selected records fixed. Target low-state worlds q_L=2/5 with recording propensity ρ_h=1 and q_L=3/5 with ρ_h=2/3 both produce selected high records with probability 2/5, no selected lows and missing records with probability 3/5. With target high-state q_H=3/5 and complete customer contribution in the established toy menu, optimized known-kernel whole-service values differ **43/40 versus 1**. Retaining qualified G achieves robust 1 across both; a known propensity of 1 would support the 43/40 report-conditioned policy. Thus preserving denominators alone does not establish target transport, nor does adding selected demonstrations necessarily resolve the economic investment choice. This is classic missing-data partial identification, **not a new statistical theorem** or robot performance evidence.

Relaxing known customer opportunity shares further yields a conservative qualified production-value certificate: demand-set total-variation diameter times the complete-service contribution range, plus the sum of worst feasible original-order shares multiplied by statewise contribution spans and report-row widths. This bounds uncertainty in *one frozen approved operating menu*; physical source-training, target grounding or a new embodiment can change the reporter itself, joint qualification, customer demand and opportunity cost. Those interventions belong to full sequential acquisition J, where optional free data preserves existing policies and any paid audit/curation/compute expense is counted once. The [full chapter](data_value/TARGET_REPORT_SELECTION_THEORY.md), [proof ledger](data_value/TARGET_REPORT_SELECTION_PROOFS.md), [prospective original-order inclusion schema](data_value/TARGET_REPORT_SELECTION_EMPIRICAL.md), [exact rational source/results](data_value/target_report_selection.py), [November 22 Models A/B bridge](data_value/NOV22_TARGET_REPORT_SELECTION_MODELS_AB.md), and separate exercise/solution texts detail the assumptions and counterexamples. No approved report system, actual customer-production panel, independent originality finding, numeric official BLS–BEA crosswalk or November 22 scientific acceptance exists. The next constructive research obligation is the **two-date choice between free/selected productive logs, paid deliberate target support and new physical qualifications**, under one common safety, demand, rights and resource budget; not another arbitrary sample-size grid. Christmas cutoff December 25, 2026, 23:59 Eastern unchanged.


### November 19: two-date production-generated data, deliberate audits, and changed qualified menus

The latest [two-date data-acquisition chapter](data_value/TWO_DATE_DATA_ACQUISITION.md) makes the observation-selection mechanism part of the **same dynamic production and investment decision**, rather than multiplying a dataset's trajectory count by an external willingness-to-pay coefficient. Date 0 allocates a real customer-service opportunity among competent productive routine, nonactuating target support or costly learning/physical qualification; date 1 optimizes accepted original-customer-order service with retained qualified controllers, changed target and embodiment alternatives and the remaining shared budget. A whole-history Bellman objective counts current contribution, rights/curation/compute/physical costs and discounted future production **once**. The old frozen target-report identification bounds remain valid only inside a physically identical sampling policy; controller-induced report selection, demand or qualification transitions require entire-policy evaluation.

An exact **uncalibrated** two-regime qualified-service construction contrasts routine production worth 1 and as many as 100 selected candidate logs with a paid independent target audit. The selected routine high-report event has probability 2/5 in both market regimes, despite latent regime-specific high-report rates 3/5 versus 2/5, because reporting propensities differ. Thus the selected logs carry no market-regime information, irrespective of volume. The optimized productive routine achieves **9/2** normalized net contribution, while a perfect paid audit, followed by regime-conditioned physical grounding or a changed embodiment, achieves **24/5**. If an equally informative report is instead a free noninterfering routine byproduct, productive routine achieves **6** and strictly dominates the audit. Under a symmetric audit accuracy α, the target investment switches from embodiment E to additional source-training X at **13/18**, then to target grounding G at **5/6**, but the audit only improves on productive routine above **19/20**. This exposes a distinction between *information changing which physical option should be developed* and *information worth acquiring after forgone customer production*; no benchmark percentage is turned directly into money.

The familiar Blackwell simulation theorem supplies a conditional productive-data dominance result when physical state, original orders, available decisions and remaining budget match. Its coupling is not established by accepted-only trajectories. Moreover, the incremental economic value of perfect information can fall when a robust embodiment is added and rise when a state-specific grounded service is added, despite monotonically expanding gross production. These are standard conditional decision/real-option constructions adapted to the common Q, original-order, resource and customer-production envelope, **not established publication novelty**. See the [proof ledger](data_value/TWO_DATE_DATA_ACQUISITION_PROOFS.md), [prospective original-order validation](data_value/TWO_DATE_DATA_ACQUISITION_EMPIRICAL.md), [Models A–B integration](data_value/NOV22_TWO_DATE_DATA_MODELS_AB.md), exact diagnostic and separate teaching packet. A real selected-report law, rights-cleared reporter, physically approved X/G/E policies, whole-network economic outcomes, official numerical BLS–BEA crosswalk and independent peer review remain absent. The November 22 synthesis gate is **open**; December 25, 2026 23:59 Eastern remains the final target.


## 19 November continuation — endogenous exposure, joint qualification, and policy-induced customer demand

The [joint-support chapter](data_value/ENDOGENOUS_EXPOSURE_JOINT_SUPPORT.md) removes a restrictive part of the preceding two-date example: future qualified physical service and **original customer demand are now jointly policy-dependent**, so the training controller can change which market opportunities exist as well as which tasks can be executed. Suppose a source-trained controller X produces two validated service components A and B, and an original customer-order opportunity D under X. Even exact marginal probabilities and all pairwise intersections of (A,B,D) identify their *complete commercially valuable triple* only in the sharp three-way probability interval
\[
\max(0,P(AB)+P(AD)-P(A),P(AB)+P(BD)-P(B),P(AD)+P(BD)-P(D))
\le P(ABD)\le
\min(P(AB),P(AD),P(BD),1-P(A)-P(B)-P(D)+P(AB)+P(AD)+P(BD)).
\]
This follows by explicitly inverting all eight nonnegative atom probabilities; it is standard Fréchet-type mathematics applied to the **demand-coupled qualified service** object, not a novelty claim. Because the entire original-order and qualification distribution depends on the trained controller, the routine policy's selected production data do not automatically identify it.

In the *synthetic* parity-world example, A, B and D each occur with probability 1/2 and every pair co-occurs with probability 1/4 under both policy-induced worlds, while the commercially qualified triple occurs with probability 0 in one world and 1/4 in the other. With date-0 incumbent production 1, terminal qualified fallback 2, source cost 2/5 and an incremental completed-service bonus 8 only for the triple, X yields **13/5 or 23/5**. An independently qualified grounding option worth **18/5** therefore beats source training in one world and loses in the other, despite identical measured individual and pairwise transfer/demand rates. The sharp source-grounding switch is t=1/8; this is not a robot benchmark threshold. The illustrative equal-prior value of knowing the whole world before acquisition is 1/2 normalized contribution units, *not* a purchased audit label's return.

This gives a concrete empirical obligation: source-modality, controller, operator, safety/recovery and **post-policy original customer orders must be linked to the same accepted complete-service unit**, including rejected and never admitted orders. Pairwise independent skill reports and routine selected trajectories do not identify joint demand alignment, and operator interference can require higher-dimensional state laws. The [proof ledger](data_value/ENDOGENOUS_EXPOSURE_PROOFS.md), [future validation protocol](data_value/ENDOGENOUS_EXPOSURE_EMPIRICAL.md), [Models A/B bridge](data_value/NOV22_ENDOGENOUS_SUPPORT_MODELS_AB.md), [verified CPU diagnostic](data_value/endogenous_exposure_joint.js), [results](data_value/endogenous_exposure_results.json), and separate [student](data_value/ENDOGENOUS_EXPOSURE_EXERCISES.md)/[instructor](data_value/ENDOGENOUS_EXPOSURE_SOLUTIONS.md) materials preserve the assumptions. **No field data, physical approval, official numeric BLS–BEA crosswalk, independent novelty review or November 22 scientific gate acceptance.** Deadline remains December 25, 2026 23:59 Eastern.


## 19 November: scarce operator resources separate source data information from embodied capacity
The earlier A/B/D triple is a *within-order* conditional qualified customer recipe. It is not enough for optimizing **multiple** original customer orders competing for one operator, recovery or dispatcher slot. Under a fixed approved policy and two qualified original orders Z_i with success p_i, cross-order coincidence r and g_1≥g_2, a precommitted slot is worth U=max(g_1p_1,g_2p_2); an *available nonactuating* joint predispatch report yields F_1=g_1p_1+g_2(p_2−r); and a separately safe second slot preserving the same law yields F_2=g_1p_1+g_2p_2. Therefore the **sum of the incremental information value and the capacity increment after information** equals min(g_1p_1,g_2p_2); its split depends on unidentified r, bounded sharply by Fréchet marginals. With unchanged original-order and per-order qualification distributions but exclusive versus synchronized across-order successes, a synthetic paid audit beats a second body in one world and loses in the other. This is decision/resource allocation mathematics, not a calibrated result or novel theorem.
The [complete theoretical chapter](data_value/JOINT_OPERATOR_INFORMATION_CAPACITY.md), [proof ledger](data_value/JOINT_OPERATOR_INFORMATION_CAPACITY_PROOFS.md), [prospective measurement contract](data_value/JOINT_OPERATOR_INFORMATION_CAPACITY_EMPIRICAL.md), [Nov22 A/B bridge](data_value/NOV22_OPERATOR_INFORMATION_MODELS_AB.md), [CPU diagnostic](data_value/joint_operator_information_capacity.js), results, and separate student/instructor materials integrate this into the existing common J and V, without double-counting continuation data value. Cross-policy source/controller/demand histories **cannot** inherit the fixed law without approval and causal evidence. No field operator architecture, independently accepted original-order panel, official numerical BEA–BLS backbone, full repository CI or originality assessment. **Nov22 scientific gate remains OPEN**, Dec25 23:59 Eastern unchanged.


## 19 November — direct whole-network policy value versus transfer mechanisms
The preceding simultaneous-order information/capacity theorem presumes a fixed qualification, original demand and operator law. Across actual X source training, G target grounding, A audit and E body investment these histories can change endogenously. The [full-history identification chapter](data_value/WHOLE_NETWORK_POLICY_IDENTIFICATION.md) now makes each **physically approved** regime an entire original-customer-order/qualification/dispatch/recovery/controller lineage over the same horizon and pre-policy network denominator. Conditional complete *network*-level random assignment identifies average full-regime captured net contribution without identifying hidden skill transfer; accepted-only service conditioning can reverse the ranking. Its exact eight-network two-date synthetic table gives X=42/8 versus G=39/8 but selected accepted-service gross means X=33/5 versus G=47/7. All 70 balanced assignments average to the full-regime economic contrast 3/8, yet realized assignment variance 8615/448 emphasizes evidentiary uncertainty; there was **no field experiment**. When two of eight approved network potential outcomes are wholly missing, even knowing the first six *paired* differences yields an envelope-only contrast interval [−25/8,31/8], no robust ranking. A feasible full-trajectory response-type LP/dual offers the alternative to randomized measurement but requires justified selection and physical transport restrictions. The [proof ledger](data_value/WHOLE_NETWORK_POLICY_PROOFS.md), [prospective network measurement contract](data_value/WHOLE_NETWORK_POLICY_EMPIRICAL.md), [Nov22 Models A/B bridge](data_value/NOV22_WHOLE_NETWORK_MODELS_AB.md), reproducible source/results and separate [exercises](data_value/WHOLE_NETWORK_POLICY_EXERCISES.md)/[solutions](data_value/WHOLE_NETWORK_POLICY_SOLUTIONS.md) integrate this **standard, conditional** result with data transfer, physical investment and customer production. No approved physical arm, actual accepted-order panel, numerical BEA–BLS crosswalk, independent novelty review or final Nov22 acceptance is claimed; theory remains primary through Dec6, Dec25 23:59 Eastern target intact.


## 19 November — pooled source data and shared operator interference: when local transfer misranks market adoption

The earlier complete-network \(J_X-J_G\) randomization result requires policy units closed to model-update, operator and customer-demand spillovers. This assumption matters **economically**, not just statistically: source-derived competence can generate additional qualified customer services but crowd the same human recovery/dispatch capacity across nominally distinct customer sites. Under a two-site fixed qualified-production example, \(q\) source-trained X sites share a single operator for incremental service \(v\), with per-X conversion cost \(k\), pooled source-production complement \(\ell\) only if both train, and a separately qualified embodiment E that supplies a second slot for cost \(K\):
\[
F_e(q)=2b+v\min\{q,1+e\}+\ell\,1\{q=2\}-kq-Ke.
\]
The cross-site data-investment interaction is \(\ell-v\) with one slot but \(\ell\) when E supplies a second. **Even positive technical pooling can be hidden by a larger operator bottleneck.** A factorial E contrast would separate the two only if E changes capacity without altering data learning, acceptance or demand. With a mixed independent X site assignment probability \(p\), the expected site-specific own-X effect differs from the entire-market all-X/all-G policy contrast by \((1-p)(v-\ell)/2\), so unbiased local randomization does not estimate universal adoption value.

In a synthetic qualified-production instance \(b=3,v=4,k=5/2,\ell=0,K=1\), G/G gross/net incumbent earns 6, targeted one-X investment earns 15/2, blanket X rollout without E earns only 5, and coordinated X+E earns 8. The local half-saturation own-X effect is **positive 1/2** per site while the all-X policy is **worse by 1/2** per site than G/G. When pooling learning raises \(\ell\) above v, the sign of the local-to-market gap reverses. This connects data-source complements/substitutes directly to scarce physical capacity and heterogeneous embodied investment, with complete customer-service contribution counted once. Free optional source data cannot be inferred harmful from a costly/forced X rollout's negative net value.

For arbitrary approved dynamic policy histories with bounded cross-site effects \(\epsilon_{ij}^a\), the mixed own-policy contrast differs from all-X versus all-G by at most the average \((1-p)\epsilon_{ij}^{X}+p\epsilon_{ij}^{G}\) across directed interference edges; in the illustrative model the bound is attained. A correct exposure-mapped randomized estimator can identify a policy contrast when target global exposures have positive probability, but high-degree source-model/operator networks can make these events rare and their estimators unstable. The [full theoretical argument](data_value/SHARED_POOL_INTERFERENCE_THEORY.md), [proof ledger](data_value/SHARED_POOL_INTERFERENCE_PROOFS.md), [future empirical protocol](data_value/SHARED_POOL_INTERFERENCE_EMPIRICAL.md), [Models A/B bridge](data_value/NOV22_SHARED_POOL_MODELS_AB.md), [source/results](data_value/shared_pool_interference.js), [student exercises](data_value/SHARED_POOL_INTERFERENCE_EXERCISES.md) and [instructor solutions](data_value/SHARED_POOL_INTERFERENCE_SOLUTIONS.md) preserve the counterexample and restrictions. No field closure, physical intervention, actual operator/customer-order panel, full repository CI, numeric BEA–BLS crosswalk or independent scientific novelty review; November 22 remains an *open* scientific gate.


## 19 November 2026 — dynamic influence and qualified production under source/model/operator/demand spillovers

The [dynamic exposure chapter](research/theory_integration_2026_11_17/data_value/DYNAMIC_EXPOSURE_PRODUCTION.md) extends the same whole-network source versus grounding/embodiment comparison beyond the static shared-operator pool. For an approved, correctly grouped finite-horizon conditional block transition law, an explicit maximal-coupling recurrence bounds the propagation of a changed source-training policy through future controller states, operator recovery, original customer demand and full accepted-service value. Plugging the resulting economically weighted per-edge bound into the prior mixed-saturation versus complete-market sensitivity inequality is **conditional on the actual joint causal graph and uniform kernel/payoff limits**; it does not identify a real robotic market contrast.

A synthetic Q/O/D path example yields a complete four-date influence bound of 521/500 versus an **invalid** 273/500 if the lagged operator→demand edge is omitted. Under a separate hypothetical D=2/5 half-saturation local contrast and two symmetric sites, the correct market T sensitivity range [-121/1000,921/1000] remains sign-inconclusive while the truncated graph falsely certifies a positive lower bound 127/1000. A joint-kernel counterexample proves that equal operator/robot marginals are insufficient for a service requiring both jointly. The companion [proof ledger](research/theory_integration_2026_11_17/data_value/DYNAMIC_EXPOSURE_PROOFS.md), [prospective original-order protocol](research/theory_integration_2026_11_17/data_value/DYNAMIC_EXPOSURE_EMPIRICAL.md), [Nov22 Models A/B bridge](research/theory_integration_2026_11_17/data_value/NOV22_DYNAMIC_EXPOSURE_MODELS_AB.md), reproducible [source](research/theory_integration_2026_11_17/data_value/dynamic_influence_production.js)/[results](research/theory_integration_2026_11_17/data_value/dynamic_influence_production_results.json), and separate [student](research/theory_integration_2026_11_17/data_value/DYNAMIC_EXPOSURE_EXERCISES.md)/[instructor](research/theory_integration_2026_11_17/data_value/DYNAMIC_EXPOSURE_SOLUTIONS.md) materials specify the same mechanism, not a detached paper. Source blob was fetched and reexecuted with 27 exact-rational assertions; four independent Python Fraction identities matched. No field-certified joint state, operator/demand graph, original-order panel, physical approval, independent originality, official quantitative BLS–BEA crosswalk or complete repository CI. Nov22 scientific gate OPEN, Dec25 23:59 Eastern fixed.
