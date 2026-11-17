# When Capabilities Become Production
## Qualification networks, learning complementarities, and investment thresholds

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

## 10. Closest literature and contribution discipline

**Process flexibility.** Jordan and Graves (1995) already establish the importance of appropriately connected limited flexibility and chaining [S1]. A path of reallocations is not new merely because the machines are robots.

**Network-design complementarity.** DeValve, Pekeč, and Wei (2023) develop a primal-dual account of flexibility design and cover modularity [S2]. We inspected the primary publisher abstract and author bibliography, not the full proof archive. Our elementary common-certificate argument is derived here from strong duality; we do not claim it precedes or improves their algorithms. The failure of a stop-on-nonpositive-singleton rule does not refute their stronger guarantees.

**O-ring complementarities.** Kremer (1993) models multiplicative task-quality effects and explicitly studies endogenous skill investment [S3]. The product form and complementarity-to-increasing-returns connection are established ideas. We checked the production-function definition and independence assumption on printed page 553, rather than treating the whole paper as replicated.

**Organization of intelligence.** Imas, Koh, and Legg (2026) distinguish competence from coordination and endogenize organizational composition and scale [S4]. We use that distinction and reconstruct a different fixed-service qualification/operating boundary; their equilibrium conclusions are not imported into a physical fleet.

**Optimization foundations.** Linear duality, sensitivity, and concave optimization provide the mathematical tools [S5]. The proofs in this document are self-contained applications, not new optimization theorems.

**Sequential R&D budgeting.** Dutta (1997) studies budget allocation across research stages, including the terminal-only reward case [S6]. Roberts and Weitzman develop sequential funding criteria that account for revisable decisions [S7]. We inspected primary abstract records, not their complete model proofs. Optimal budget allocation, the ability to stop, and the value of retaining development progress therefore cannot themselves be advertised as new contributions. Our recursive homogeneous example is a transparent comparator within that established family; a stronger contribution must explain the economically measured qualification network and its changes.

### Candidate contribution worth developing

The strongest candidate is a **measurement-linked theory of the economic returns to capability acquisition**: identify productive qualification bundles from a customer's real production alternatives; characterize how they transform technical learning into commercial value; and test whether changes in demand, coordination, or shared learning alter that transformation.

The candidate is not yet an established publishable contribution. The general leading-order result is elementary once the attainable-value function is given, and it is related to reliability-network arguments. Its significance would come from a convincing economic specification, a useful dynamic or organizational extension, and discriminating evidence. This is a reason to deepen the coherent argument—not to resume an endless sequence of isolated novelty disclaimers.

## 11. Adversarial verification and limits

The research kernel checks integer operating values exactly using rational arithmetic. It examines all 512 three-by-three eligibility graphs and all 19,683 assignments of their nine possible edges to old, candidate, or absent status for the critical-order comparison. These are combinatorial cases, not empirical observations.

One hundred twenty seeded graph comparisons test common-dual feasibility against independent exact allocation. Additional tests check continuous-capacity concavity, heterogeneous learning KKT conditions against a separate scalar optimizer, derivative signs and numerical derivatives, global investment optima against dense grids, correlation counterexamples, and sequential-retention alternatives. Forty-two scoped tests pass, including a different concave technical learning curve, general finite-state adaptive gross-value equations, and the optimal retained-success stopping policy checked against an independent Bellman-ODE implementation. The expected-payoff identity reconciles reward times completion probability minus actual expected expenditure, and funding remains a pathwise maximum rather than an assumed expenditure. Numerical LP checks use tolerances; symbolic proofs establish the stated general results. Neither test counts nor exhaustive small instances prove claims about all production systems.

The model deliberately excludes a full industrial equilibrium, endogenous contracting, unobserved safety constraints, estimated robot learning curves, and complete-order integer scheduling outside the identified special cases. One explicit counterexample shows a linear recipe relaxation worth 1.5 when the indivisible implementation can deliver only 1. Such gaps are a boundary to enforce, not a rounding nuisance.

No independent peer review, real robot execution, complete empirical atlas, or full historical repository CI is claimed. The scheduled research process executes only during actual supported runs. Earlier unpublished Q10 work and the inaccessible older Codex workspace have not been recovered by writing this manuscript.

## 12. Sustained next investigation

Continue this same theory block across sessions instead of inventing another numbered toy at each run. The independent adaptive gross-order bound and homogeneous-chain stopping problem are now solved in stated scope. Joint acquisition events and partially valuable intermediate qualifications now have a verified finite-state extension (Result 7). The next substantive question is how **date-dependent customer opportunities, interim paid production, and multiple payers** change that learning portfolio without counting future value twice. Start with a general state-transition formulation that nests the current proofs, then identify the smallest extension that changes their economic implication. Do not rederive the solved homogeneous chain or build an all-purpose simulator.

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
