# Paper 3 — named proof appendix

This appendix proves the restricted claims in the [single canonical manuscript](README.md). It is not a separate paper. Input main: `a03659f79395ce9b7d9c06235e660a0d5e704f76`; recursive-source branch: `af1cabb95772524db1b34dda3b2667a54c203b43`. No finite-game solver, oracle, NumPy world or historical simulation was run. Analytical proof is distinguished from the small exact arithmetic check in A.5.

## A.0 Common lemmas

**Setting.** A policy is adapted to the declared observation history and obeys every physical, rights and dated cash constraint. The objective is expected additive claimant payoff. For the infinite-horizon statements assume $0<\beta<1$, uniformly bounded one-period rewards and well-defined measurable policies; the finite restrictions below have finite menus or an explicitly attained optimum. Rivals and prices are fixed unless stated otherwise.

**L0.1 — Optional-menu inclusion.** If an added procedure is free, may be ignored, preserves every original contingent program and changes no rival response, obligation or transition when ignored, the new optimum is weakly larger. Every old policy remains feasible with the same value, so the supremum over the larger set cannot be smaller. This is a decision-value result; public disclosure can change a rival's policy and invalidate its premise.

**L0.2 — Implementation equivalence.** Suppose each internal policy has an external implementation preserving the joint law of observations and accepted service, timing, resource use, lawful rights and claimant cash flows, and conversely. The two sets of attainable payoff distributions coincide, hence their suprema coincide. One-way implementation gives only a weak value ordering. Matching a final accuracy score alone is not implementation equivalence.

**L0.3 — Adaptive observation equivalence.** Let two candidate latent economies have the same initial observable law and the same conditional observable kernel after every history/action in a declared action class. Couple the policy's randomization. Equal observable histories induce identical action distributions; the equal next-observation kernels then give equal histories one step longer. Induction proves equality for every finite history. Infinite histories inherit equality on cylinder events. No policy restricted to that class identifies the two economies. A new diagnostic can defeat the premise by changing its observation law. All observed cash, rejection totals and settlement tags must be included in the filtration.

**Competent comparator.** A procedure is economically new only if it changes a feasible technology, information law, resource/timing cost or implementable contingent program. Identical fully informed optimization over identical laws cannot generate an organizational premium merely from assigning different controller names. Costs of acquiring or transmitting information are separate from the gross value of using information once available.

## A.1 Successor production and Economic RL

### A.1.1 The successor-value proposition

At date 0 choose one feasible program $j$. Its real/opportunity cost is $k_j$. With probability $p_j$ the current defect is resolved and incremental contribution $G_0$ is earned; failure pays zero under the normalization and offers no successor opportunity. After success choose whether to spend $c_j$. This additional spend yields a qualified successor with probability $e_j$ and next-date incremental claimant value $S$. The yield is conditional on current success and the extra expenditure. No unmodeled information changes this expenditure decision, and cash, rights and validation resources permit it.

Backward induction gives the success-branch continuation $\max\{0,\beta e_jS-c_j\}$, and therefore

$$W_j=p_jG_0-k_j+p_j[\beta e_jS-c_j]_+.$$

With common $k,c$ and both continuation investments strictly active,

$$W_1-W_0=(p_1-p_0)(G_0-c)+\beta S(p_1e_1-p_0e_0).$$

If $G_0>c$, $p_1>p_0$ and $p_1e_1<p_0e_0$, the coefficient on $S$ is negative. Dividing its zero by the strictly positive $\beta(p_0e_0-p_1e_1)$ gives the threshold in P3.1. The region also requires $S>c/(\beta e_j)$ for each positive $e_j$; outside it use the option values. At zero yields or indifference the separate branch must be evaluated directly.

For heterogeneous success outcomes, condition on the observed outcome and take the positive part before averaging. Replacing $E[X_+]$ by $[E X]_+$ generally changes the result. A fee or returned datum contributes to $S$ only to the extent that it changes value beyond the comparator; do not count the same recipient service twice.

### A.1.2 Three-layer estimand

Fix a carrier protocol specifying what counts as executor $q$, inquiry procedure $m$, raw records, answers, rights and resources. Randomize $Z$ at cohort 2 and transmission $T$ after cohort 2 has generated its incremental artifact. Maintain a common announced transmission chance while the artifact is produced. Let $Y_3(z,t)$ be the potential outcome on independently sampled cohort 3 under source assignment $z$ and transmission $t$.

Randomization and interference control imply $E[Y_3\mid Z=z,T=t]=E[Y_3(z,t)]$. Subtract the two transmission effects to identify

$$E[Y_3(1,1)-Y_3(1,0)-Y_3(0,1)+Y_3(0,0)].$$

That is an interaction of assigned history and artifact passage. Calling the artifact a better successor inquiry procedure requires the exclusion restrictions in the main text, a matched executor, and measuring its effect on choosing/producing the next improvement. The experiment does not establish which abstract label uniquely names the mechanism. Preannounced transfer rights change production incentives and identify a different treatment. Failed inquiries and absent artifacts remain in their original assigned cells.

### A.1.3 Physical MPK and the forecast's value

Let $Y^{acc}=\min(D_{job},K+H_{sub})$. At $K+H_{sub}=D_{job}-1$, an added robot increases accepted work by one. Increasing the qualified substitute $H_{sub}$ by one also adds one accepted job, but makes the next robot's physical marginal product zero. If that substitute costs less than the job's value, it improves economic contribution while decreasing $MPK_r$. Thus no universal increasing reward transform of $MPK_r$ implements the claimant's objective across this menu.

For two actions with conditional value difference $\Delta_a$, optimize before and after a signal. With costless discretion to ignore it, the resulting gross value is

$$E[(E[\Delta_a\mid\mathcal I,Z])_+\mid\mathcal I]-(E[\Delta_a\mid\mathcal I])_+.$$

Conditional Jensen proves nonnegativity. Strict positivity requires the posterior action-value difference to put positive probability on both strictly positive and strictly negative values, subject to integrability. An accurate forecast that never changes the preferred action can have zero decision value. This standard value-of-information result is not a claim that an RL system learns the correct value model.

The original Economic RL module retains its negative comparisons and information-matched ordinary-planner tie. Its correlated-proposal and delegation calculations are explicitly historical analytical support in SOURCE_DISPOSITION, not additional unproved main-text claims.

## A.2 Evidence time and allocation

### A.2.1 Deployment-time exponent

The maintained fluid law is

$$\dot n=v_i\kappa_i a_i^{\gamma_i}(n+b_i)^{-\alpha_i\gamma_i}.$$

Multiply by $(n+b_i)^{\alpha_i\gamma_i}$, integrate from $n(0)=0$, and solve. This gives the identity and exponent in P3.2a. The asymptotic comparison is in calendar/operating-opportunity time; it is not an estimated learning curve. With initial $n_0\ne0$, replace the initial $b_i^{1+\alpha_i\gamma_i}$ by $(n_0+b_i)^{1+\alpha_i\gamma_i}$.

If an additional independent admitted stream supplies useful records at constant rate $a_0>0$ and the total intake is bounded above by a finite constant, then $a_0t\le n(t)\le Ct+O(1)$. Thus $n(t)\asymp t$ and the original record-time exponent is restored. Raw audit counts with no information, duplicated labels or binding processing do not satisfy these bounds.

For a recipient with $z=\tau n$, $\tau>0$, and its own error exponent $\alpha_j$, the time exponent is $\alpha_j/(1+\alpha_i\gamma_i)$. For finitely many streams $n_i(t)\asymp t^{\nu_i}$ and fixed positive weights, their sum has exponent $\max_i\nu_i$, while their minimum has exponent $\min_i\nu_i$. Bound each by constant multiples of its dominant/slowest power. The minimum concerns complementary record requirements as specified; arbitrary skills with different transformations need another proof.

### A.2.2 Shared-hour frontier and interior derivative

At fixed source state, usable hours are $H^{free}\ge0$ and incident capacity $I^{elig}\ge0$. A unit of incident review yields $g_I$ evidence and a unit of reference work yields $g_R$, with $g_I>g_R>0$. The minimum hours needed for $z$ are

$$t(z)=\begin{cases}
z/g_I,&0\le z\le g_I I^{elig},\\
I^{elig}+(z-g_I I^{elig})/g_R,&z>g_I I^{elig}.
\end{cases}$$

Impose $t(z)\le H^{free}$, so the actual domain ends at $z_{max}=g_I\min(H^{free},I^{elig})+g_R[H^{free}-I^{elig}]_+$. If the incident pool exceeds total hours, the second segment is infeasible. This increasing convex frontier allows corners to be solved by the concave objective $U(H^{free}-t(z))+W(z)$, with $U,W$ increasing and concave.

In the mixed interior, incident review is exhaustive: replacing reference time by an unused eligible incident hour raises evidence without more hours. Hence

$$y+z/g_R=\mathcal H=H^{free}+(g_I/g_R-1)I^{elig},\quad U'(y)=g_RW'(z).$$

Differentiate the constraint and FOC, assuming $U'',W''<0$:

$$dz/d\mathcal H=g_RU''/(U''+g_R^2W'')>0.$$

At fixed workload $u$, $(H^{free})'=h_1u$ and $(I^{elig})'=-ru$, proving the sign condition. Corners use the frontier and one-sided comparisons; this derivative is not global.

For endogenous workload impose $u\le K_s$, $pu\le D_s$ and $h(p)u\le H$, all with the declared nonnegative source demand and capacity. Let $\kappa_u>0$ be the curvature of source contribution, so its value is $(v_sp-c_s)u-\kappa_u u^2/2$. In the relevant mixed interior, $\mathcal H=H-k(p)u$, $V'>0,V''<0$. The FOC is

$$v_sp-c_s-\kappa_u u-kV'=0.$$

Differentiating and substituting $\mathcal H'=-k'u-ku'$ yields

$$(\kappa_u-k^2V'')u'=v_s-k'V'+kk'uV''.$$

The denominator is strictly positive. With $k>0$, a sufficiently large expansion $u'$ can turn a positive fixed-workload resource release into negative effective resources. Heterogeneous recipient evidence, moving yields, demand prices, private capture or additional source options change this reduced objective and its derivative.

The separate average-reward review-cadence proposition from the branch remains a named historical analytical result in SOURCE_DISPOSITION. Its finite/infinite audit rule is not silently substituted for this paper's discounted dormancy theorem.

## A.3 Identification and audit location

### A.3.1 Structural/measurement product and stable repeats

Let $U_e,\eta_e\in\{-1,1\}$ have means $\tau_e^{str},\lambda_e^{meas}$. The structural family and measurement family are mutually independent, independent across edges, and each independent of all latent vertex signs $Z$; the same latent-vertex prior is used in both decompositions. Conditional on vertex signs,

$$\Pr(Y_e=y\mid Z_i,Z_j)=\{1+yZ_iZ_j\tau_e^{str}\lambda_e^{meas}\}/2.$$

Thus the one-reading likelihood, and its mixture over latent vertices, depends on the structural/measurement parameters only through their products. Distinct decompositions sharing every product are observationally equivalent. With independent new-edge errors and the specified latent prior, the equality of conditional likelihoods carries through Bayesian updating and adaptive new-pair choice by L0.3. The claim concerns this declared observation experiment, not every conceivable test.

For stable $M_e$ and independent refreshed errors with common mean $\lambda_e^{meas}$,

$$E[Y_{e1}Y_{e2}]=E[M_e^2\eta_{e1}\eta_{e2}]=(\lambda_e^{meas})^2.$$

A nonnegative sign convention recovers $\lambda_e^{meas}$, but a nonzero value and identification of the product are still needed to divide out $\tau_e^{str}$. Known vertex relations are one sufficient anchor. Cycles may supply informative products, but their identification requires the specified graph/parameter restrictions. On a forest with independent uniform vertex signs, all edge sign-products are jointly uniform; multiplying them by any independent structural noises preserves that uniform law. Repeats can reveal measurement noise while structural reliability remains unidentified. Correlated errors or changing $M_e$ invalidate the square identity.

### A.3.2 Exact audit tree and sharp bounds

For $G_A>0$ and $c_A\ge0$, a release costs $c_A$ whether the correction is novel or redundant. Its benefit is $+G_A$ on $U\cap T$, $-G_A$ on $U\cap T^c$, and zero on $U^c$. Without an audit expected net benefit is $G_A(2j-p_U)-c_A$, with the option to decline.

After a source audit, decline on $U^c$. On $U$, the probability-weighted benefit is $G_A(2j-p_U)$ and commissioning is incurred with weight $p_U$. Optimizing this branch gives $V_S$. After a recipient audit, decline on $T^c$. On $T$, novelty occurs with conditional probability $j/p_T$, giving probability-weighted benefit $G_Aj$ and cost $p_Tc_A$. This gives $V_R$. Zero-probability branches are handled without dividing; the positive-part formulas remain valid. The recipient audit must reveal $T$ even for a redundant candidate.

With $j=p_Up_T$, source value first becomes positive at $G_A=c_A/(2p_T-1)$ and recipient value at $c_A/p_U$. The maintained inequality $p_T>(1+p_U)/2$ puts source activation first. When both are active,

$$V_R-V_S=p_U(1-p_T)G_A-(p_T-p_U)c_A.$$

Its positive slope gives the stated crossing. These are release-option values before buying either audit. Different audit prices, availability and opportunity costs can reverse the purchase ranking.

For arbitrary marginals, the four joint masses are $j,p_U-j,p_T-j,1-p_U-p_T+j$. Their nonnegativity is exactly the Fréchet interval. The value difference is continuous piecewise affine in $j$, with kinks at the stated zeros of the two positive parts. A piecewise-affine function on a compact interval attains its extrema at endpoints or kinks; every permitted $j$ defines an admissible joint law, so the bounds are sharp.

### A.3.3 Selected admission and retention

Each period draws a fresh roster case independently conditional on a fixed hidden convention; the only observations are the retained signs and admission categories described here. Take two latent conventions with different original-roster probabilities $p_\ell(y)$ for latent convention $\ell\in\{0,1\}$ for diagnostic sign $y$. For each permitted route $a$, choose admission masses $b_y(a,\ell)$ and retained masses $w_y(a)$ satisfying $0<w_y(a)<b_y(a,\ell)<p_\ell(y)$ and with total admission $\sum_yb_y(a,\ell)$ the same in both conventions. Admit sign $y$ with probability $b_y/p_\ell(y)$ and retain an admitted sign with probability $w_y/b_y$.

The unconditional retained signed mass is $w_y(a)$ in both worlds. Total admitted-but-unlabeled mass is $\sum_yb_y-\sum_yw_y$, and unadmitted mass is $1-\sum_yb_y$; both also match. If hidden signs of unlabeled/rejected cases are not otherwise observed, L0.3 implies that any adaptively chosen sequence of these routes yields the same observable law. For example, the construction is feasible with original sign probabilities $3/4$ versus $1/4$ and sufficiently small common positive admission/retention masses.

This is an existence result for unknown selection under the stated filtration. Known propensities, meaningful rejection reasons, labeled settlements or an independently sampled original roster can change the likelihood and defeat it. The funding-share discussion attached to the historical source is routed to Paper 1; it is not an extra Paper 3 financing proposition.

### A.3.4 Aggregate-settlement permutation

With one order in each of two lanes, conditionally independent Bernoulli outcomes given their probabilities, and equal known margins, aggregate success count has probability-generating function

$$(1-p_1+p_1z)(1-p_2+p_2z).$$

Swapping $p_1,p_2$ leaves all coefficients unchanged. If ordinary releases, priors and hidden transitions preserve the same symmetry, the aggregate-history likelihood cannot distinguish the two fault locations, by L0.3. A release that makes success high-high in one hidden state and low-low in the other changes the count likelihood. Tagged results or unequal known margins can also reveal the lane. Approximate planner experiments are not a proof of an unrestricted optimum; only the exact likelihood symmetry is retained as a main claim.

## A.4 Portable interfaces and boundaries

### A.4.1 The stationary switching lemma

There is one unresolved state under each incumbent arrangement, with the same primitive laws on every return after failure. Portability is persistent. Mature flows satisfy $v_P>v_I\ge0$ and switching costs are as in P3.4. No financing or calendar restriction changes feasibility, and an effort maximizer exists. If pure costless idling is feasible, include its zero-flow, zero-transition action in both effort menus; the proposition does not silently exclude an available outside option. Let

$$\mathcal B_g(u)=\max_a\{\pi_g(a)+\beta r_g(a)W_g+\beta[1-r_g(a)]u\}.$$

This operator is a contraction with modulus at most $\beta$. Its fixed point is the stay-until-portability value $Q_g$, and rearrangement of its optimal fixed-point inequality gives the ratio formula in the main text. For $u\ge Q_g$, $\mathcal B_g(u)\le u$; at $Q_g$ equality holds.

Allow one arrangement choice before operation at each date. Repeated instantaneous switches have no payoff and are discarded. The full two-arrangement discounted Bellman operator is

$$\mathcal T_P(U)=\max\{\mathcal B_P(U_P),-C_{in}+\mathcal B_I(U_I)\},$$

$$\mathcal T_I(U)=\max\{\mathcal B_I(U_I),-C_{out}+\mathcal B_P(U_P)\}.$$

It is a contraction in the sup norm, so its bounded fixed point is unique. Set

$$\widehat U_P=\max(Q_P,Q_I-C_{in}),\quad
\widehat U_I=\max(Q_I,Q_P-C_{out}).$$

If $\widehat U_P=Q_P$, its stay value is exactly $Q_P$, while its switch value is at most $-C_{in}+\widehat U_I\le Q_P$. If instead $\widehat U_P=Q_I-C_{in}>Q_P$, nonnegative switch costs imply $\widehat U_I=Q_I$; its switch value equals $\widehat U_P$, and its stay value is no larger. The same argument applies to $I$. Thus $\widehat U$ is the unique Bellman value. This proof avoids relying on a noncontractive instantaneous-switch equation when both switch costs are zero.

Integration then delegation follows from the two strict inequalities in P3.4. This is global over the stated two-arrangement effort/switching menu. A joint lab or reserved outside resource can supply an additional continuation and defeat it, as the pinned source example does. Informative failures, changing demand, rights or financing require additional state variables. Waiting can then have value; it is not ruled out by the stationary lemma.

### A.4.2 Speed and the attainable domain

Differentiate $P(\zeta)=G_S(\zeta^{d_I}-\zeta^{d_P})$ for $0<\zeta\le\beta$. Its derivative changes sign where $\zeta^{d_P-d_I}=d_I/d_P$, proving a unique interior maximum on $(0,1)$ and the stated $\zeta^*$. If $\beta\le\zeta^*$, the accessible premium is increasing. At maximal persistence $\rho=1$ it equals $G_S(\beta^{d_I}-\beta^{d_P})$, positive when $\beta<1$. A strictly middle integration interval requires an overhead between both attainable endpoint premiums and the interior maximum. Maxima across changing arrangements or multiple payoff dates need not be single-peaked.

## A.5 Dormancy, cash invariance and sustained recursion

### A.5.1 Exact experiment and comparator

P3.5 fixes the technical operator, direct attempt outlay $c$, conditional yield $e_{rec}$, and incremental one-cohort stake $G$. A paid proposed procedure needs prospective, experiment-specific evidence. The first eligible record has geometric delay $T\ge0$ with parameter $\lambda=f^\gamma$. All probability statements are conditional on the currently known state; arrival, technical success and the opportunity-specific hazard are independent there. Technical qualification is distinct from commercial survival. The old procedure is retained after failure.

The ordinary cash-generating core remains viable when the focal research opportunity expires. Source operation can continue while the inquiry uses a specified shared engineering/review slot; the slot's next-best contribution $h v_{op}$ is not assumed equal to the entire core cash surplus $s$. Compute the cash bridge after that slot is reassigned. In the simple constant-core example, source outlay/receipts are unaffected by that reassignment; in another application lost mandatory receipts must enter the bridge.

$G$ is measured relative to competent ordinary learning and the stipulated outside alternatives. The closed form assumes this **incremental** stake and evidence law are stationary during a project's waiting time, apart from the hazard. The hypothesis does not assert that ordinary firms cannot learn. If ordinary catch-up makes the incremental stake depend on $T$, replace $G$ by $G(T)$ and recompute the expectation. All benefits, including any terminal or resale value, must be included once. No hidden value of producing future procedures is inserted in $G$; future cohort payoffs enter through subsequent actions.

Conditional on arrival at $T=k$, technical qualification earns the cohort receipt with probability $e_{rec}(1-\delta_{obs})^k$. Acceptance creates an enforceable debt, settled at $k+d$. Therefore

$$R=\theta e_{rec}G\beta^d\sum_{k\ge0}\lambda[(1-\lambda)\beta(1-\delta_{obs})]^k
=H_G\frac{\lambda}{1-a+a\lambda}.$$

Because $0<\beta<1$, the series converges. Only payment discounting, not a second commercial-survival factor, operates after acceptance. An unenforceable or still-contingent receivable would require a different kernel.

The unconditional probability of a commercially surviving successful qualification is

$$p^{qual}_{commercial}=e_{rec}\frac{\lambda}{\delta_{obs}+(1-\delta_{obs})\lambda}>0.$$

If technical qualification can be retained even after the focal commercial opportunity expires, its technical success probability remains $e_{rec}$. Otherwise use $p^{qual}_{commercial}$ for advancement. Either is positive under the maintained domains; the main existence result uses the relevant one, never confuses it with the conditional yield.

### A.5.2 Threshold algebra and domains

For $0<\lambda\le1$, $R$ is increasing in $\lambda$ and is at most $H_G$. Hence strict gain requires $H_G>C=c+h v_{op}$. Under that condition $H_G-aC>0$ and

$$\Delta=\frac{(H_G-aC)\lambda-C(1-a)}{1-a+a\lambda}
=\frac{(H_G-aC)(\lambda-\lambda_*)}{1-a+a\lambda},$$

$$\lambda_*=\frac{C(1-a)}{H_G-aC}\in(0,1).$$

This proves P35.3. If $H_G=C$, only $\lambda=1$ can tie; if $H_G<C$, all arrivals yield strictly negative margin. Do not divide by $H_G-aC$ without checking its sign. For $0<f<1$ and fixed other parameters, the active region also satisfies $\gamma<\log(\lambda_*)/\log f$. At $f=1$, starvation elasticity does not alter arrival probability. Literal probabilities/intensities must be calibrated to the operating opportunity unit; $\lambda=f^\gamma$ is a reduced-form assumption, not an identity equating logs with raw failures.

### A.5.3 Stopped-sum verification of optimal dormancy

Assume the optimized ordinary comparator includes every admitted non-inquiry alternative. Relative to it, total incremental claimant payoff is the sum of the dated cohort receipts minus their initiation costs, plus an ordinary-action residual that is zero or nonpositive. Any effect of a successor on ordinary production, terminal assets or rights must be included once in its priced cohort payoff or in subsequent declared actions. A later control cannot improve a prepaid cohort’s receipt law beyond its initiation-state expectation; abandonment may only reduce that bound. There are no omitted subsidies, saved future costs, refunds, or cross-cohort externalities. This additive, noninterfering cohort restriction is what makes the stopped-sum comparison a statement about total value.

Let $\sigma_k$ be the history-adapted initiation time of inquiry $k$. Each initiation has immediate economic cost $C_k$; its own nonnegative receipt is delayed and may be zero. At most one initiation occurs per period, all cohort stakes/costs are bounded, and $\beta<1$. Thus discounted receipts and costs are absolutely integrable, allowing the tower property and exchange of expectation and sum.

For policies completing each declared protocol with zero ordinary residual,

$$J(\pi)=E\sum_k\beta^{\sigma_k}\{E[\text{own discounted cohort receipt}\mid\mathcal F_{\sigma_k}]-C_k\}
=E\sum_k\beta^{\sigma_k}\Delta(\mathsf{s}_k).$$

Here $\mathsf{s}_k=(x_{\sigma_k},m_{\sigma_k})$ and future successor receipts are not inside the current stake. The policy may adapt the next initiation to success, cash, rights or past waits; the law at the next initiation is evaluated in that new state. Abandonment can reduce a prepaid project's receipt bound. With no refund or saved incremental future cost, it cannot turn a nonpositive upper bound into a positive one. Any extra action changing those premises must be included explicitly.

Suppose $\mathcal D$ is forward invariant under **all** feasible transitions from its states, including inquiries and exit/rights/reference/organizational actions in the maintained menu, and every reachable inquiry margin is nonpositive. Ordinary operation attains incremental value zero, while the displayed expression/bound gives $J(\pi)\le0$ for every complete adaptive policy. This proves optimal dormancy. If every initiated inquiry has strictly negative conditional margin, any policy with a finite initiation on a positive-probability event has strictly negative value. Its optimal discounted research count is zero. At equality nonzero inquiry may tie.

The same logic can be written as a Bellman verification: the ordinary-program value is a supersolution for every admitted recursive action and is attained by an ordinary action. Bounded discounted dynamic programming then yields the ordinary value. **A first-action test only along the ordinary realized path is insufficient.** For example, a negative first experiment may open a high-value new market. The trap theorem requires ruling out that exit, or including and defeating it. P3.5's stationary renewal case and its monotone failure-starvation tail provide explicit ways to do so; no unrestricted full-economy trap is claimed.

### A.5.4 Dated financing and the bridge

For an admitted operating plan after research has received its shared resources, let $O_t(u)$ be mandatory cumulative cash outlays and $A_t(u)$ certain cumulative collections through $t+u$, excluding the uncertain successor receipt. Define

$$L_t=\sup_{u\ge0}[O_t(u)-A_t(u)]_+.$$

This is a requirement on **spendable cash**, not a valuation of receivables as cash. When the baseline cash prefixes are deterministic and $c$ is the only extra upfront outlay, $B_t\ge c+L_t$ is necessary and sufficient for the zero-successor-receipt operating plan to be feasible. Necessity for every actual project policy additionally requires that a zero-receipt path be admissible; otherwise the rule may be conservative. More generally it is a conservative robust admission rule; state-contingent borrowing or guaranteed minimum successor payments can change it.

For the initially empty continuous-flow operating pipeline, outlays are $w$ per unit time; gross receipts from completed operation are $w+s$ and are collected after lag $d$. With no successor receipts,

$$B(t)=\begin{cases}
B_0-c-wt,&0\le t\le d,\\
B_0-c-wd+s(t-d),&t\ge d.
\end{cases}$$

The minimum is at $d$, proving the exact fresh requirement $B_0\ge c+wd$. With ordinary operation alone set $c=0$. If $wd\le B_0<c+wd$, the core can start; after warming the pipeline it reaches cash $c$ no later than

$$t_{fund}=d+(c+wd-B_0)/s.$$

That bound is sufficient, not a claim that earlier inquiry during warmup can never be optimal. If $B_0\ge c+wd$, immediate inquiry is feasible. Once the pipeline matures, current net receipts are $s$ and its remaining bridge is zero. During initial warmup $L_t=w(d-t)_+$ for this unchanged operating plan. The lag is not charged repeatedly as a fresh expense or reserve.

If $B_0<wd$ with no receivables, credit or alternative income, the specified **indivisible** operating plan is infeasible. Divisible operation, prepayments, a smaller cell or an outside employer can defeat that liquidity trap and must be admitted when feasible. The $wd$ value is peak working capital in money units, not money-times-time occupancy or a second operating cost in $C$.

### A.5.5 A constructive recurrent self-funding set

After operating warmup let $X$ be cash beyond the current mandatory bridge. Assume a guaranteed free operating surplus $s>0$, net of all costs and replenished required working capital, continues independently of whether a focal inquiry succeeds or its commercial opportunity survives. This operating core can continue while a shared engineering slot forgoes another contribution valued at $h v_{op}$; $s$ and $v_{op}$ are different accounts. If diverting the slot reduces mandatory collections, that loss must also enter the actual cash-prefix plan used to compute $L_t$ and the guaranteed surplus. Define $M=\lceil c/s\rceil\ge1$. Start only at $X\ge c$, complete the declared protocol, wait through settlement, then operate/refill for $M$ periods before starting again. A qualified predecessor is retained; a failure permits retry. Fresh normalized opportunity/evidence laws and positive incremental stakes recur after each completed round.

Ignoring any additional operating surplus during the research/waiting interval gives the conservative cash inequality at successive starts

$$X_{n+1}\ge X_n-c+sM+Y_n\ge X_n,$$

where $Y_n\ge0$ is the actually settled cohort receipt. No loan is secured against its expectation. Within each round the bridge condition prevents a shortfall. This is a pathwise invariant funding rule even for an arbitrarily long succession of zero-receipt attempts.

The deliberately conservative cycle length is $L=T+d+M$. It is at least one period and has finite mean $(1-\lambda)/\lambda+d+M$. Under independent regenerated cycles, the renewal strong law gives

$$N_{attempt}(t)/t\to1/E[L]>0\quad\text{almost surely}.$$

Applying the renewal-reward law to qualified-success marks gives technical successor rate $e_{rec}/E[L]$, or commercial-qualified rate $p^{qual}_{commercial}/E[L]$ if that is required to advance. Because the relevant probability is positive, infinitely many retained successor procedures are produced almost surely. This does not imply accelerating improvement or a stationary distribution over unbounded procedure indices.

For this particular policy, after resetting excess cash by a permissible dividend if a common buffer is desired (a distribution of already counted resources, not another project reward),

$$q_\beta=E[\beta^L]=\beta^{d+M}\frac{\lambda}{1-\beta+\beta\lambda}<1,$$

$$V_{regen}=\Delta+q_\beta V_{regen}=\frac{\Delta}{1-q_\beta}>0.$$

The renewal value requires that a next round remain available after both success and failure and that normalized payoffs/laws reset; failed attempts retry the retained predecessor. Technical advancement is counted separately from round count. If cohort obsolescence ends the whole enterprise or removes the next opportunity, this renewal equation is invalid.

Existence of this policy proves a feasible self-funding basin and that permanent abandonment is suboptimal whenever a finite operating/refill path still leads to a positive-margin attempt. It does **not** prove this schedule optimizes cadence or that every optimum has the displayed rate. A stronger pathwise optimal-policy statement requires its own timing Bellman problem. No such claim is used to close Gate A.

The finance distinction is essential. Without operating refill, insurance or another certain receipt, finite cash can be exhausted by a sufficiently long failure streak with positive probability even when expected project NPV is positive. Here operations fund the firm, and inquiry creates positive expected incremental value. A failed individual inquiry need not pay for itself.

### A.5.6 Cash-rich dormancy and ordinal extensions

At fixed $H_G,a$, differentiation gives

$$\frac{\partial R}{\partial\lambda}=\frac{H_G(1-a)}{(1-a+a\lambda)^2}>0.$$

For $\lambda(z_{op})=f(z_{op})^\gamma$ and $C(z_{op})=c+h v_{op}(z_{op})$, this proves P35.5. A parameter can increase the core's settled cash surplus and inherited liquidity while raising the opportunity cost of inquiry or suppressing eligible unresolved cases. The funding surface and the economic margin then move in opposite directions.

For the exact main-text witness, $a=81/100$, $H_G=243/20$ and $\lambda=1/2$, so

$$R=(243/20)(1/2)/(119/200)=1215/119.$$

At $v_{op}=5$, $C=7$ and the gain is $382/119>0$; at $v_{op}=10$, $C=12$ and the gain is $-213/119<0$. Both have positive technical sandbox surplus $e_{rec}G-c=18$. Along $B=s=v_{op}=z_{op}$, the fresh operating bridge is 2 and the inquiry requirement is 4. Values $z_{op}=1,5,10$ give liquidity trap, feasible positive recursion and cash-rich economic dormancy, respectively. These are constructed exact units. The case $z_{op}=3$ is an operating/refill state, not permanent economic dormancy.

The signs do not depend on the power law or geometric distribution alone. For any finite evidence-delay distribution and a known preacceptance survival function $S_{obs}(T)$,

$$R=\theta e_{rec}G\,\beta^d E[\beta^T S_{obs}(T)].$$

If improved operation makes the evidence delay first-order stochastically longer, and $\beta^tS_{obs}(t)$ is nonincreasing, expected receipt weakly falls. If it also raises shared-hour opportunity cost, the margin weakly falls. Strict signs require strict stochastic/order changes on payoff-relevant support. This ordinal statement preserves the economic comparison, though the closed-form $\lambda_*$ depends on the geometric restriction. Nonlinear cost menus, endogenous prices or unknown hazards can remove a scalar threshold; the all-action Bellman/invariance condition is the portable dormancy criterion.

### A.5.7 No-renewal stopping bound and its limits

If successes move $f_n=f_0\eta^n$, $0<\eta<1$, $\gamma>0$, then $\lambda_n=f_0^\gamma\eta^{\gamma n}\downarrow0$. For constant $G,C$ with $H_G>C$, monotonicity of $R$ gives the first weakly nonpositive margin when $\lambda_n\le\lambda_*$. Taking logs yields P35.6, with zero if the initial state is already at/below the boundary. Every later reachable generation remains below it if the menu has no evidence-renewal, rights, scale or technology escape. In this restriction $f_n$ is an irreversibly unresolved/informative-case stock: no admissible operation, rollback or retained old procedure raises the useful-record arrival probability. Known or deliberately recreated errors are not new useful evidence; reproducing an already available procedure cannot earn the same incremental stake again. If rollback can restore informative arrivals, it is an exit from the claimed tail and must be evaluated; monotonicity along one deployment path then does not certify an all-policy trap. This verifies the trap on deviation-reachable successor states, not just the ordinary path.

For bounded stakes $G_n\le\bar G$, replace $H_G$ with $\bar H_G=\theta e_{rec}\bar G\beta^d$ to obtain a sufficient tail bound. If $\bar H_G\le C$, no strict gain is possible anywhere. If it is larger, the corresponding $\bar\lambda_*$ yields a finite invariant tail. When $\beta=1$ and $\delta_{obs}=0$ simultaneously, longer but finite waits without any waiting cost need not change the sign; this paper uses $\beta<1$.

Maintaining positive margins despite $\lambda_n\to0$ requires

$$G_n>\frac{C}{\theta e_{rec}\beta^d}\left(\frac{1-a}{\lambda_n}+a\right).$$

Thus incremental stakes must grow at least at inverse-arrival order in this restriction, before paying to create that scale. A genuine reference stream can prevent arrival from vanishing, but cannot by itself stop incremental stakes from disappearing. The theorem is a finite-depth bound, not a universal perpetual-RSI claim.

### A.5.8 Sandbox, funded null and verification status

At $\theta=1$, $\gamma=0$, $\lambda=1$, $v_{op}=0$, $d=0$, nonbinding cash and $\delta_{obs}=0$, the margin is $e_{rec}G-c$. This is a supplied-interface technical condition. The economic model becomes necessary when access, shared resources, finance, rights, capture or rival behavior are choices rather than fixed inputs.

The stored FUNDED_EMBODIED comparison is a different four-date game with known-local archives, specified successor menus and equilibrium selection. Its cash-120 condition removes liquidity from the stated legal menus; it does not remove opportunity cost, timing or strategic tradeoffs. The old selected zero attempts are a matched synthetic null. P3.5 supplies a logically exact **mechanism for funded dormancy**, not a parameter fit, a re-solve or a claim that failure-starvation generated that null. The mapping's unmeasured $\theta,\gamma,v_{op},d,\delta_{obs},G$ coefficients remain null.

`verify_p35_dormancy.py` checks selected rational identities, a geometric prefix with exact tail, the cash-rich sign change, cash-prefix consistency and the sandbox limit. It is under 150 physical lines, imports `fractions.Fraction` for all numerical arithmetic, and performs no policy enumeration, multi-shift simulation or solver call. Its execution receipt is in GATE_A_RECORD. It is an arithmetic check; A.5.1–A.5.7 are the proofs.

## A.6 Common cost and strategic boundaries

Against fixed rival behavior on corresponding histories, take a finite common game tree with perfect recall and the same feasible policies and chance laws throughout a surcharge interval $\mathcal C$. The objective is risk-neutral expected additive monetary payoff. If $n_t\ge0$ counts the designated attempts, the surcharge contributes exactly $-c\,d_t^{obj}n_t$; every other payoff component is held independent of $c$. A fixed complete policy induces one history distribution, so linearity of expectation yields

$$V^\sigma(c)=A_\sigma-cN_\sigma,\qquad N_\sigma=E\sum_t d_t^{obj}n_t\ge0.$$

$A_\sigma$ is an algebraic intercept if zero is outside the feasible interval. Finite perfect-recall expected-payoff decision problems admit a pure optimal response; maximizing over the finite pure contingent-policy set gives the nonincreasing convex piecewise-affine envelope. Optimality at $c_1<c_2$ yields

$$A_1-c_1N_1\ge A_2-c_1N_2,\qquad A_2-c_2N_2\ge A_1-c_2N_1,$$

so $(c_2-c_1)(N_1-N_2)\ge0$. This is about total objective-weighted attempts, not each current action.

A policy's optimal region intersects all $A_\sigma-A_\tau-c(N_\sigma-N_\tau)\ge0$. Pairwise equality supplies an actual boundary only if no third policy dominates. A vector of additive charges gives half-spaces on a common feasible tree. Cash thresholds changing the tree invalidate a global extension across those boundaries.

For a fixed complete behavioral profile under perfect monitoring, let $A_i(h),N_i(h)$ be conditional intercept/count under the profile, and $A_i(h,a),N_i(h,a)$ force one current action, average over rivals' simultaneous actions and return to the profile. All-history one-shot inequalities

$$A_i(h)-A_i(h,a)-c[N_i(h)-N_i(h,a)]\ge0$$

are sufficient for subgame perfection by backward induction, including off-path histories. Two supported actions must tie; fixed probabilities over an open cost interval require equal intercepts and equal conditional counts. Equal immediate attempt counts alone are insufficient. Private information requires an information-set/belief analysis.

**Regular two-player mixed-support branches.** At a continuation matrix game with rational payoff entries, fix each player’s positive support. Normalization and supported-action indifference form augmented linear systems for the opponent’s probabilities and each player’s value: for example, $A_{S_1,S_2}y=v_1\mathbf 1$ and $\mathbf 1^\top y=1$, with the analogous system for $x,v_2$. On a square nonsingular regular system, Cramer’s rule gives rational probabilities and values. The branch is valid only where its determinants are nonzero, probabilities satisfy normalization/positivity, and all inactive-action deviation inequalities hold. Inequalities must retain denominator signs. Finite backward induction preserves rationality when transition probabilities, payoffs and the remaining operations are rational. Rectangular/degenerate supports, singular systems and more-player multilinear indifference equations require a separate analysis; rationality is not asserted for them.

**Preserved strategic counterexample.** Each firm chooses entry/research $E$, paying common charge $c$, or outside option $O$:

| | Firm 2 E | Firm 2 O |
| --- | --- | --- |
| Firm 1 E | $(5-c,1-c)$ | $(10-c,0)$ |
| Firm 1 O | $(0,3-c)$ | $(0,0)$ |

For $0<c<1$, firm 1 strictly prefers E and firm 2's best response is E. For $1<c<3$, firm 1 still strictly prefers E and firm 2 chooses O. These unique equilibria give firm 1 the branches $5-c$ and $10-c$. Its equilibrium profit can jump upward as the common charge rises. No uniqueness is claimed at $c=1$. The numbers are an analytical counterexample in constructed units, not a new synthetic simulation.

P3.5's partial derivatives hold these rival responses and the market/rights menu fixed. Endogenous withdrawal, entry or disclosure may change capture, gross stakes, cash surplus, opportunity cost or arrival/survival law. Fixed-policy convexity and the dormancy surface do not sign that equilibrium response. The globally reoptimized correspondence remains uncomputed; no frozen oracle is invoked to fill it.
