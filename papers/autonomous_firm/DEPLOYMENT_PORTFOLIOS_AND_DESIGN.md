# Archived source edition — Paper 2 consolidation

This is preserved supporting text, not an independently evolving paper. The sole active manuscript is [The Autonomous and Full-Stack Firm](The_Production_of_Capability.md). [Source-to-section routing](../../research/portfolio/CANON.md#paper-2-one-manuscript-five-results) sends financing/disclosure to Paper 1 and organizational recursion, scaling and dynamic boundaries to Paper 3. Existing proofs, links, scripts, counterexamples and empirical limitations remain valid only within their original scope. Old packaging dates are provenance, not deadlines.

---

# Deployment portfolios and the next robot

*The Production of Capability — a further extension of the full stack firm · November 25, 2026*

**A deployment can be valuable because it makes another deployment's experience interpretable.** That relationship changes the set of sites worth operating, the hardware worth building, and the scale at which the firm wants to deploy its next design. The next fleet is an outcome of learning, so its size cannot always be held fixed when valuing the experience that produces it.

The [previous extension](FULL_STACK_FIRM.md) showed how a mechanical improvement can suppress useful failure records and make instrumentation more valuable. This extension studies a different obstacle. A record can be captured perfectly and still fail to distinguish the causes that matter for the next design. The firm may need a contrast between operating conditions, rather than more observations of the same condition.

The companion full stack manuscript now also solves finite successive tooling choices, manufacturing yield and customer participation. This extension preserves that work and isolates how complementary sources change what can be inferred and the scale of the next cohort.

The main results are conditional propositions about one firm. They solve a production-site portfolio, a subsequent hardware design and manufacturing quantity, and a further choice to build hardware that makes the next inquiry cheaper. They do not establish a market equilibrium, an empirical scaling law, or a general advantage to vertical integration.

## 1. The economic starting point

Consider a manufacturer that also trains its controllers, integrates its machines, and operates them for customers. It can change the next hardware batch, the procedure for inspecting field records, and which work is attempted at each site. It earns value when those choices produce accepted customer service or avoid real costs.

Three premises motivate the extension.

**Production creates selected observations.** An operating cell reveals what happened under a particular hardware configuration, policy and workload. Knowing that an error occurred does not necessarily reveal whether the cause was the mechanism, its calibration, or the environment.

**The firm can sometimes choose a useful contrast.** A reference operation may isolate a shared calibration effect that is mixed with the task requirement in ordinary production. That reference might come from another deployment, a factory bench, a retained cell, or a permitted intervention at the original site. The economic choice is over feasible experiments; a larger customer count is only one way to obtain them.

**The recipients of a discovery are partly endogenous.** After seeing what the source operations reveal, the manufacturer can choose a different design and a different number of machines. Learning can improve an already attractive design, make a marginal opportunity worth entering, or prevent an unattractive batch from being built.

These premises connect to the two papers motivating the research. In the baseline of *Data-Driven Automation*, task output accumulates data and a nonnegative spillover kernel maps source stocks into effective task data. The question here is how the chosen operating arrangement changes what a record identifies. *Organizing Intelligence* separates productive competence from coordination and studies how supplied capabilities organize into firms. The present question is how one firm invests to produce the capabilities and information on which later organization depends. These are extensions in modeling scope, not objections to those papers. [1, 2]

Actions with both productive and informational consequences are established in dual control. Likewise, simulations of evolving robot morphologies show that embodiment can affect the learning of later controllers, including when those controllers start from scratch. Neither finding establishes the industrial or ownership effects derived below. [3, 4]

Within this project, [reference coverage](https://github.com/amarmurray/robotics-economics/blob/49811393f67ffb17720371a615ea99705d5ccbc9/research/recursive_firm/reference_coverage/README.md) already established that selected archives can fail to identify a production convention. [Partition discovery](https://github.com/amarmurray/robotics-economics/blob/49811393f67ffb17720371a615ea99705d5ccbc9/research/recursive_firm/partition_discovery/README.md) studied learning which cases share a correction. The new step here is to derive the complementarity of chosen evidence sources and carry that complementarity into an endogenous manufacturing decision.

## 2. A production problem with two unresolved causes

Let $\theta$ be a parameter relevant to the next hardware design. Let $\nu$ be a shared nuisance parameter affecting the interpretation of operating records. Before the focal experiments,

$$
\theta\sim N(\mu_0,S),\qquad
\nu\sim N(\nu_0,T),\qquad \theta\perp\nu,
\qquad S,T>0.
$$

Here $S$ and $T$ are variances. The prior includes what the firm has already learned through ordinary work. The comparison does not make the ordinary firm forget its existing evidence.

Two feasible source configurations produce

$$
y_A=\nu+\varepsilon_A,\qquad
y_B=\theta+\nu+\varepsilon_B,
$$

where measurement errors are independent, have zero means, and have variances $r_A,r_B>0$.

For an applied interpretation, suppose the next design must accommodate a task-specific load, while an uncertain calibration parameter affects the readings used to infer that load. Production configuration $B$ mixes the two. A reference operation at $A$ isolates the calibration parameter. This is a local, stylized measurement model. It requires a reason that the same nuisance affects both records; arbitrary sites do not satisfy it.

The firm first chooses a source portfolio $E\subseteq\{A,B\}$. Its current net cost includes hardware, integration, measurement, permissions, support and the value of ordinary service displaced. After the records arrive, the firm chooses its next design and manufacturing quantity. Both sources and all subsequent designs satisfy the maintained service requirements. Failure to meet those requirements is not a free learning technology.

### The state must preserve relationships between unknowns

Let $s_E$ denote the posterior variance of $\theta$. Gaussian conditioning gives

$$
s_\varnothing=s_A=S,
$$

$$
s_B=S-\frac{S^2}{S+T+r_B}.
$$

Observing $A$ first leaves nuisance uncertainty

$$
T_A=\frac{Tr_A}{T+r_A}.
$$

Therefore,

$$
s_{AB}=S-\frac{S^2}{S+T_A+r_B}
<s_B<S.
$$

The order of acquiring the two measurements does not change this final posterior. After $B$, the posterior covariance between $\theta$ and $\nu$ is

$$
\operatorname{Cov}(\theta,\nu\mid y_B)
=-\frac{ST}{S+T+r_B}.
$$

This covariance explains the mechanism. If the firm subsequently learns that more of the observed discrepancy came from calibration, it revises how much came from the task requirement.

A scalar record of current task performance is not generally a sufficient state for this subsequent decision. The firm needs the relevant joint posterior, or records and a valid likelihood from which it can recover it. Retaining raw files is not itself necessary if a sufficient statistic preserves the required relationships. Retaining files without an interpretable measurement model is not sufficient either.

## 3. Proposition: individually weak sources can be jointly valuable

Begin with a fixed recipient exposure $W>0$. The firm's future design $x$ incurs expected loss

$$
W E[(x-\theta)^2\mid D].
$$

The optimal design is the posterior mean, $x^*=E[\theta\mid D]$, and its remaining expected loss is $Ws_E$. Define gross information value relative to the existing prior as $L_E=W(S-s_E)$.

It follows that

$$
L_A=0,\qquad
L_B=\frac{WS^2}{S+T+r_B},
$$

while

$$
L_{AB}=\frac{WS^2}{S+T_A+r_B}.
$$

Hence

$$
\boxed{
L(A\mid B)
=
\frac{WS^2(T-T_A)}
{(S+T_A+r_B)(S+T+r_B)}
>0=L(A\mid\varnothing).
}
$$

**Proof.** The posterior mean minimizes quadratic loss. Substituting the posterior variances and subtracting gives the displayed expression. Since a finite-precision observation of $\nu$ reduces its variance, $T_A<T$, and every denominator is positive.

The information sources are complements for this decision. A site supplying no standalone improvement to the target design can belong in the optimal portfolio because it explains a different site's evidence. Ranking each deployment by its standalone data contribution would miss that portfolio.

The claim is about this decision and these signals. It does not say that $A$ lacks value for every purpose, or that all additional environments are complements. Correlated priors, redundant measurements and different payoffs can change the result.

### Faster accumulation can increase the value of a different source

Suppose $B$ is observed $n$ times with independent measurement errors but the same $\theta$ and $\nu$. Its mean reading has noise variance $r_B/n$. Replacing $r_B$ by this quantity gives

$$
s_{B,n}=S-\frac{S^2}{S+T+r_B/n}.
$$

Thus

$$
\lim_{n\to\infty}s_{B,n}=\frac{ST}{S+T}>0.
$$

The repetition identifies $\theta+\nu$ increasingly well. It does not identify the decomposition.

In the fixed-exposure benchmark, more precise $B$ observations also increase the marginal value of $A$. Writing $r$ for the remaining noise of the average $B$ observation,

$$
\frac{\partial L(A\mid B)}{\partial r}
=
-L(A\mid B)
\left[
\frac{1}{S+T_A+r}+\frac{1}{S+T+r}
\right]<0.
$$

This supplies a precise alternative to the earlier result in which better routine discovery favored fewer environments. When sources supply independent chances of finding the same rule, one can substitute for another. When one source separates causes mixed by another, improving the latter can make the former more valuable. “Faster learning” has to identify which part of the learning technology improved.

For a fixed cost of obtaining $A$, a firm can therefore initially concentrate on $B$ and later add $A$ as the accumulated $B$ evidence makes the contrast worth buying. That is a comparative static holding the recipient exposure and costs fixed. Aging recipients, shorter remaining deadlines or changing demand can reverse the chronological prediction.

The information floor also has a sharp boundary. If each $B$ observation redraws an independent nuisance with a known mean, averaging removes nuisance uncertainty. If the firm can vary $B$'s known loading on $\nu$, it may generate the necessary contrast without another site. A cheap factory test may dominate a new deployment.

## 4. The next design and fleet are choices

A fixed $W$ makes the recipient fleet an external input. To endogenize it, let one unit of the next vintage produce operating surplus

$$
m+a\theta-\kappa(x-\theta)^2.
$$

The constant $m$ is captured service value net of ordinary linear costs, including the relevant per-unit manufacturing expense. The coefficient $a$ lets the same unknown influence the attractiveness of the opportunity. The mismatch term prices avoidable rework, adjustment or another real cost of choosing the wrong design. It is a cost specification, not a formula for physical throughput.

Let expanding the cohort to $N\geq0$ units incur an additional cost $\gamma N^2/2$, with $\gamma>0$ and $\kappa>0$. This represents a specified increasing marginal manufacturing or integration cost. An appropriate declining marginal demand value can produce the same reduced form. We do not count both explanations as separate costs. Capacity is continuous here; integer units require finite differences.

After evidence $D$, suppose $\theta\mid D\sim N(\mu_D,s)$. Expected profit is

$$
\Pi(N,x\mid D)
=
N\left[m+a\mu_D-\kappa\{(x-\mu_D)^2+s\}\right]
-\frac{\gamma}{2}N^2.
$$

Both design and quantity are chosen after the observations and before the new batch is committed.

### Proposition: evidence changes design, scale and entry

For positive production, the optimal design is

$$
\boxed{x^*(D)=\mu_D.}
$$

The optimal manufacturing quantity and continuation value are

$$
\boxed{
N^*(D)=\frac{[m+a\mu_D-\kappa s]_+}{\gamma},
\qquad
V(D)=\frac{[m+a\mu_D-\kappa s]_+^2}{2\gamma}.
}
$$

Here $[z]_+=\max(z,0)$.

**Proof.** Conditional expected squared mismatch equals $(x-\mu_D)^2+s$, minimized at $x=\mu_D$. The remaining objective is a strictly concave quadratic in $N$; its nonnegative maximizer gives the two expressions. If $N=0$, the unused design is immaterial.

There are two effects. A more accurate design reduces expected mismatch costs. The content of the evidence also changes the chosen quantity: favorable evidence can justify a larger batch, while unfavorable evidence can stop a batch. Information is valued against a competent manufacturer that already chooses its best design and quantity from its prior.

### An exact ex ante value

For a predetermined Gaussian experiment portfolio, posterior variance $s$ is nonrandom and

$$
\mu_D\sim N(\mu_0,S-s).
$$

Define

$$
M(s)=m+a\mu_0-\kappa s,\qquad
\omega(s)=|a|\sqrt{S-s},\qquad z(s)=M(s)/\omega(s).
$$

Let $\Phi$ and $\phi$ be the standard normal distribution and density. Integrating the positive part of the optimized profit gives

$$
\boxed{
H(s)
=
\frac{
\{M(s)^2+\omega(s)^2\}\Phi(z(s))
+M(s)\omega(s)\phi(z(s))
}{2\gamma}.
}
$$

For $\omega(s)=0$, the expression is understood as $[M(s)]_+^2/(2\gamma)$. The corresponding expected quantity and entry probability, when $\omega>0$, are

$$
E[N^*]=\frac{M\Phi(z)+\omega\phi(z)}{\gamma},
\qquad
\Pr(N^*>0)=\Phi(z).
$$

These moments apply before a fixed portfolio's outcomes are seen. If the firm selects further measurements in response to early signals, the selection must be integrated explicitly; the unconditional formula cannot simply be applied to the selected sample.

## 5. What determines the marginal value of learning?

Differentiating the preceding continuation value yields

$$
\boxed{
-H'(s)
=
\kappa E[N^*]
+
\frac{a^2}{2\gamma}\Pr(N^*>0).
}
$$

**Proof.** Write optimized value as $Z_+^2/(2\gamma)$ for a normal variable $Z$ of mean $M$ and variance $\omega^2$. Its expected derivative with respect to $M$ is $E[N^*]$. Its derivative with respect to $\omega^2$ is $\Pr(Z>0)/(2\gamma)$. Since $dM/ds=-\kappa$ and $d\omega^2/ds=-a^2$, the result follows. The formula holds in the interior with positive dispersion; at degenerate boundaries use one-sided limits.

The first term values reducing mismatch on the units the firm ends up manufacturing. The second values adapting entry and scale to what the evidence reveals. It is not exclusively an entry term: it also covers resizing opportunities that remain profitable.

This is a concrete replacement for multiplying a learning gain by an externally fixed fleet. The exposure that makes precision valuable is partly created by the same precision. For a finite variance reduction, integrate the marginal expression over the interval; adding a separate data premium to $H$ would double-count its effect on production value.

For the next investment, the marginal expected net surplus conditional on the chosen design is

$$
m+a\mu_D-\kappa s-\gamma N.
$$

At an unconstrained interior optimum it is zero. An improvement can initially raise this margin, induce a larger batch, and leave the margin on the final chosen unit back at zero. This is an investment condition in value units. It is not a claim that physical $MPK_r$ equals zero.

The existing definition of physical $MPK_r$ remains the vector of additional accepted services from a specified commissioned robot, holding other stocks and the order book fixed while reoptimizing dispatch. Knowledge can change that vector when it changes physical feasibility. The present mismatch-cost model can instead increase investment value by reducing costs without changing accepted physical output. The two outcomes must be measured separately.

## 6. Joint source entry with endogenous manufacturing

Let $\beta$ discount the manufacturing continuation to the source decision date, and let $d_A,d_B$ be the sources' current net costs relative to the maintained ordinary-production alternative. Define

$$
G_B=\beta[H(s_B)-H(S)],
\qquad
G_{AB}=\beta[H(s_{AB})-H(S)].
$$

The four feasible portfolio values, relative to neither new source, are

| Source portfolio | Incremental optimized value |
| --- | --- |
| Neither | $0$ |
| $A$ | $-d_A$ |
| $B$ | $G_B-d_B$ |
| Both | $G_{AB}-d_A-d_B$ |

### Proposition: the portfolio can pay when neither site pays alone

For $d_A,d_B\geq0$, both sources are optimal, allowing ties, exactly when

$$
\boxed{
d_A+d_B\leq G_{AB},
\qquad
d_A\leq G_{AB}-G_B.
}
$$

**Proof.** The first inequality compares both sources with neither. The second compares both with $B$. Since $A$ alone has nonpositive value, those comparisons also dominate $A$. Necessity follows from the same comparisons.

Because $H$ falls with residual variance, the extra contrast can produce a strictly positive gap $G_{AB}-G_B$. Costs can then satisfy $d_A>0$, $d_B>G_B$ and $d_A+d_B<G_{AB}$. Neither source is attractive alone, but the pair is.

If source costs are negative because current service earns sufficient contribution, retain the additional comparison $d_B\leq G_{AB}$. If source obligations create shared costs, replace $d_A+d_B$ with the actual portfolio cost. If cash, engineering or customer permissions rule out a portfolio, remove it from the feasible menu. Positive expected value does not establish dated funding feasibility.

The mechanism is complementary evidence plus contingent manufacturing. It does not require subsidizing every atypical customer. The exact comparison can favor a test cell, a purchased calibration or a modified operating policy over either new deployment.

### A conditional competitive implication

In this uncapped expansion model, reducing posterior variance weakly increases expected manufacturing quantity. Also $H_m(s)=E[N^*(s)]$. Thus

$$
\frac{\partial}{\partial m}
\{H(s_{AB})-H(s_B)\}
=
E[N^*(s_{AB})]-E[N^*(s_B)]\geq0.
$$

A reduction in captured unit margin can weaken the firm's incentive to acquire the complementary source, even with the same observation technology. This is a partial-equilibrium comparison in a stipulated margin. Competition, customer pricing and industry-wide quantities are not solved here.

## 7. Two generations of hardware design

The model can now price a machine that helps the firm learn what to manufacture next.

Suppose the current source hardware has two designs, $h_0$ and $h_1$, with the same accepted service. Design $h_1$ costs an extra $F$, inclusive of relevant operating burdens, and makes the $A$ contrast available at cost $c_{\mathrm{on}}$. Under $h_0$, an equivalent external experiment remains available at cost $c_{\mathrm{ext}}\geq c_{\mathrm{on}}$. Both alternatives receive the ordinary $B$ record and may decline to purchase $A$.

After observing $B$, let $b_B$ be the complete conditional belief. Define the remaining gross value of obtaining $A$ by

$$
g(b_B)
=
E[V(b_{AB})\mid b_B]-V(b_B)\geq0.
$$

The value includes reoptimization of the *next* design $x$ and manufacturing quantity $N$. Nonnegativity follows because the manufacturer could retain the decision it would have made without $A$.

If purchasing $A$ can respond to $B$, the incremental value of building $h_1$ is exactly

$$
\boxed{
\Delta_h
=
\beta E_B\left[
[g(b_B)-c_{\mathrm{on}}]_+
-
[g(b_B)-c_{\mathrm{ext}}]_+
\right]-F.
}
$$

The manufacturer chooses the more informative source hardware when $\Delta_h>0$. With no future design decision, its incremental value is $-F$. The additional hardware is therefore justified entirely by what it enables the firm to learn for the next generation.

The expectation matters. Replacing each adaptive option by an option on its average gain need not preserve the difference between the two hardware designs. If acquisition must be precommitted before $B$ arrives, the restricted comparison instead uses

$$
\beta\left[
[G-c_{\mathrm{on}}]_+
-
[G-c_{\mathrm{ext}}]_+
\right]-F,
\qquad
G=H(s_{AB})-H(s_B).
$$

### The competent alternative bounds the result

For $c_{\mathrm{ext}}\geq c_{\mathrm{on}}$,

$$
\Delta_h\leq\beta(c_{\mathrm{ext}}-c_{\mathrm{on}})-F.
$$

**Proof.** For every nonnegative $g$, the difference between the two positive parts is between zero and $c_{\mathrm{ext}}-c_{\mathrm{on}}$. Take expectations and subtract $F$.

If the external experiment has the same all-in cost, timing and permissions, the hardware advantage disappears. A factory-owned test cell may itself be the best alternative. Full stack control permits joint optimization; ownership alone does not establish superiority.

This is a solved, bounded cycle: current hardware changes the economics of acquiring evidence, that evidence changes the subsequent hardware design, and the subsequent design's contingent production scale determines the value of the original hardware choice. Persistent recursive growth would additionally require renewed questions, new tasks, changing designs or shocks. A stable finite set of already identified parameters does not supply an endless learning dividend.

## 8. Why higher value need not mean more robots

In the particular uncapped Gaussian model,

$$
\frac{dE[N^*]}{ds}
=
-\frac{1}{\gamma}
\left[
\kappa\Phi(z)+\frac{a^2}{2\omega}\phi(z)
\right]\leq0,
\qquad \omega>0.
$$

More information raises expected manufacturing in that specification. It is not a general law of automation.

With a hard demand or capacity cap $\bar N$, favorable evidence cannot increase output indefinitely. Unfavorable evidence can still lead the firm to forgo a batch. The value of a better decision can then rise while expected deployment falls.

The replication contains an exact finite-state counterexample with the same quadratic mismatch and expansion costs. Before learning, the firm fills the cap. Once informed, it builds only in the favorable state. Its expected optimized value increases while expected machines decline. This example is a boundary check, not an industry forecast.

The implications for existing vintages also differ. Information about the next mechanical design does not automatically improve irreversibly built machines. An installed cohort benefits only through a feasible change such as calibration, a software adjustment, retrofit or redeployment, with its costs and qualification requirements included. If none is possible, the benefit belongs to future builds.

Similarly, shortening the time to the same usable evidence can increase its discounted value and let it arrive before a tooling commitment. It generates additional manufacturing only when the revised investment is both desirable and feasible. Faster information, faster collection of cash and a higher physical marginal product are separate changes.

## 9. What must be observed to test the mechanism?

The key empirical object is the **interaction between sources at a fixed downstream decision**, followed by the endogenous response of the manufacturer.

A useful design would hold the initial model, comparable source-work budgets, interpretation method and target evaluation protocol fixed, and compare four evidence sets: ordinary prior only, $A$, $B$ and $A+B$. Acquisition costs and the best available factory or purchased experiment belong in all comparisons. Where updates are shared, assign the experiment at the level of that sharing.

| Prediction | Necessary observation | Strong competing explanation |
| --- | --- | --- |
| $A$ makes $B$ useful | A positive interaction in held-out design loss or accepted target service | $A$ merely adds more examples of the target task |
| Repeating $B$ does not resolve the cause | A persistent ambiguity under the same exposure and measurement law | The apparent floor is inadequate optimization or too few observations |
| The contrast changes manufacturing | Revised design, batch size or entry after the signal | A concurrent demand, credit or supplier change |
| Current hardware is chosen for later inquiry | A costed hardware choice with a return through later evidence and design | An unmeasured direct reliability or service benefit |
| An archive becomes interpretable | Sufficient old records improve after the new contrast, with stable mappings | The new method trains entirely from new records |
| Value rises while capital falls | Better net decisions and lower expected deployments under a binding cap | Lower demand alone caused both |

These observations need not all be collected before theoretical progress. They distinguish the model's claims from plausible alternatives and specify the additional records needed before estimating its magnitude.

### What can invalidate the exact result?

If the nuisance at $A$ is unrelated to the nuisance at $B$, $A$ cannot supply the required contrast. For correlated Gaussian nuisances, the reduction in the variance relevant to $B$ is proportional to the square of their covariance; it vanishes at zero covariance.

If the nuisance is independently redrawn with known mean, repeated $B$ observations can remove it. If operating choices change unknown measurement loadings or selection, that uncertainty must enter the likelihood. Our known linear mapping does not establish causal identification from arbitrary observational records.

If every relevant future action is already irrevocably fixed, extra information may have no decision value. If hardware changes the nuisance or destroys the mapping to old data, prior records can become less useful. If a sufficient contrast is already present in ordinary data, its extra acquisition value must be priced relative to that existing source.

## 10. The broader object for the recursive firm

A generalized observation system is

$$
y_i=X_i(h,\pi)\vartheta+\varepsilon_i,
$$

where hardware $h$, operating or diagnostic policy $\pi$, and the chosen production portfolio determine the available measurement directions. Repetition increases precision along existing directions. A different configuration can add a direction needed for a profitable decision.

Under a nonsingular Gaussian prior and a known linear model, arbitrarily precise observations identify a target $\ell^\top\vartheta$ exactly when that target lies in the row span of the attainable observation matrix. The firm need not identify every physical parameter. It needs the distinctions that change feasible production choices.

For a recurrent model, retain:

- the joint belief over economically relevant unknowns, including covariances;
- the hardware vintages, existing obligations and feasible adjustments;
- the experiments the hardware, policies and rights make available;
- manufacturing, integration and dated financial constraints;
- the demand and captured margins governing the continuation decision.

The conditional value of a proposed experiment is the change in the best feasible continuation, net of its full cost. A fixed “data value per robot-hour” generally cannot represent it. Nor can a fixed source weight represent the zero-standalone, positive-joint value in the strictly increasing fixed-exposure benchmark without adding an interaction or a richer learning state.

The next unsolved step is **co-evolution of the experiment menu and the production design over repeated vintages**: allow redesign to change the measurement directions themselves, allow calibration relationships to drift, and solve whether the firm retains a reference configuration, redesigns it, or buys outside evidence. Demand and dated commissioning capacity must constrain each generation. This extends the solved cycle rather than assuming that every additional deployment reinforces it.

## Proof status, replication and sources

The posterior formulas, source complementarity, repetition floor, fixed-exposure comparative static, contingent design/quantity solution, variance shadow value, portfolio inequalities and two-generation option comparison are conditional analytical results. Their mathematical building blocks are standard Gaussian conditioning, Bayesian decision theory and investment optimization. No generic novelty claim is made for those tools. The particular conjunction provides a further worked mechanism in this research program.

The [replication script](replication/capability/diagnostic_portfolios.py) checks posterior formulas against joint covariance conditioning, normal moments against direct numerical integration, the shadow value against numerical differentiation, and source-entry inequalities against all four portfolio values. It also checks adaptive acquisition after the first signal, an equivalent external experiment, irrelevant uncertainty, independent nuisance variation and the capped-demand counterexample. Its [recorded results](replication/capability/diagnostic_portfolios_results.json) use synthetic inputs and do not calibrate a robot, firm or industry.

Run from the repository root with Python 3, NumPy and SciPy:

~~~bash
python3 papers/autonomous_firm/replication/capability/diagnostic_portfolios.py
~~~

**Source and scope notes**

1. Maryam Farboodi, Andrew Koh and Anchi Xia, *Data-Driven Automation*, June 2, 2026, §2 and §2.1. [Author-hosted paper](https://static1.squarespace.com/static/5efca972e541380b32c1ca30/t/6a20374d02f50639ed704dce/1780496209650/DDA_June26.pdf). Used for the task-data and spillover primitives, not a calibrated mapping from robot hours to usable information.
2. Alex Imas, Andrew Koh and Shane Legg, *Organizing Intelligence*, October 29, 2026, §3.1. [Official paper](https://storage.googleapis.com/deepmind-media/papers/organizing-intelligence.pdf). Used for the separation of competence and coordination and the organizational allocation question; our manufacturing dynamics are additional assumptions.
3. Edgar D. Klenske and Philipp Hennig, *Dual Control for Approximate Bayesian Reinforcement Learning*, JMLR 17(127), 2016. [Journal page](https://www.jmlr.org/papers/v17/15-162.html). Establishes the prior-art connection for actions that affect both control and learning.
4. Agrim Gupta, Silvio Savarese, Surya Ganguli and Li Fei-Fei, *Embodied intelligence via learning and evolution*, Nature Communications 12, 5721, 2021, results on downstream learning. [Published paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC8494941/). Simulation evidence that morphology can affect learning, not a test of our site-entry or investment propositions.

Input accepted revision: [b784b262d7503a8baae573d4ff49efcaba48193c](https://github.com/amarmurray/robotics-economics/commit/b784b262d7503a8baae573d4ff49efcaba48193c). Independent research-branch antecedents were read at [49811393f67ffb17720371a615ea99705d5ccbc9](https://github.com/amarmurray/robotics-economics/commit/49811393f67ffb17720371a615ea99705d5ccbc9). Before publication this extension was reconciled with the finite-vintage and customer-demand work at [734a08d0f64e5b9e209d0a290b99bad15692161d](https://github.com/amarmurray/robotics-economics/commit/734a08d0f64e5b9e209d0a290b99bad15692161d). That manuscript, its PDF, its replication and its result register are preserved.
