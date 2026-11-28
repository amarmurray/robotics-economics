# Recursive Firm Theory

**Canonical Paper 3. Gate A: closed for the explicitly restricted claims P3.1–P3.5 and A.COST in this revision. Gate B: pending an independent hostile referee. Gate C: pending.** [Closure and claim record](GATE_A_RECORD.json) · [Proof appendix](PROOFS.md) · [Source disposition](SOURCE_DISPOSITION.md) · [Lane 4 / Gate B / Gate C handoffs](LANE3_HANDOFF.md). Input main: `a03659f79395ce9b7d9c06235e660a0d5e704f76`. No frozen solver or oracle was invoked. Gate A does not establish novelty, empirical identification or a solved general equilibrium.

## 1. Scope and common controlled state

The economic object is a firm, or a coordinated value-chain coalition, using its current means of production to change the procedure by which it selects, produces and deploys future means of production. Write the state as $(x_t,m_t)$: $x_t$ contains embodied fleets, digital execution policies, human and compute capacity, beliefs, lawful data rights, dated working capital, receivables and obligations; $m_t$ is the retained inquiry/production procedure. A recursive action changes the feasible technology of subsequent inquiry, not merely the name of the optimizing controller.

This is a scope claim about economically implemented recursion, not a theorem that an individual agent cannot improve itself. An agent-level model is sufficient when its objective, budget, evidence access, evaluator, deployment interface and appropriation rules are supplied and fixed. The software/sandbox limit identifies the agent's authorized environment with the whole relevant productive unit. Physical access, customer acceptance, validation slots, dated cash and multiparty rights then impose no additional binding choice. STOP and AIDE² are technical antecedents, not evidence that these economic conditions hold in all deployments; ENPIRE supplies a physical example of improvement inside a supplied interface. [Verified positioning and reading boundaries](LANE3_HANDOFF.md#b-gate-b-referee-brief-for-an-independent-author).

### State, actions, observation and payoff

Let

$$x_t=(K_t,q_t,\mu_t,D_t,R_t,H_t,B_t,\mathbf{AR}_t,\mathcal O_t,g_t,\chi_t).$$

Here $K$ is usable physical capital; $q$ the execution policy; $\mu$ the joint belief over unresolved causes; $D$ retained evidence; $R$ lawful use/control rights; $H$ dated resource capacities; $B$ spendable cash by payer; $\mathbf{AR}$ collectible receipts indexed by due date; $\mathcal O$ customer/deployment obligations; $g$ the organizational arrangement; and $\chi$ the operating/research phase. The procedure $m$ specifies which experiments can be designed, interpreted and transmitted, and their resource, timing and observation laws. It is not a scalar intelligence score.

A history-adapted action $a_t\in\mathcal A(x_t,m_t)$ can operate, inspect, investigate, design, qualify, commission, finance, change rights, change organization or wait. The feasible set includes competent human/fixed-machine alternatives, retained old procedures and equivalent external tests whenever the stated institution supplies them. Resource use and every dated cash prefix must be feasible. In particular,

$$B_{t+1}=B_t+\operatorname{collections}_t-\operatorname{cash\ outlays}_t+\operatorname{net\ financing}_t,$$

with receivables entering collections only on actual collection. Borrowing is not operating revenue; financing claims enter the claimant's payoff and terminal net assets consistently. A controlled kernel determines observations and transitions:

$$\Pr(dx',dm',do\mid x,m,a)=\mathcal K(dx',dm',do\mid x,m,a).$$

A proposed successor uses an explicit operator $\mathcal U(m,a,o)$, so that $m'=\mathcal U(m,a,o)$ on qualification and the old $m$ remains available otherwise. Ordinary operation can change $q$, $D$ and beliefs. A stronger recursion claim requires evidence that experience changes $m$, or the technology for producing its successor, after matching those ordinary changes.

For fixed market primitives and rival policies, the risk-neutral claimant solves

$$V_i(x,m)=\sup_{\pi\in\Pi_i(x,m)}E^\pi\!\left[\sum_{t\ge0}\beta^t r_{i,t}\right],\qquad0<\beta<1,$$

with bounded rewards, or the corresponding finite-horizon objective and declared terminal value. The reward is the specified claimant's economic flow, with internal transfers cancelling on consolidation and each service/cost counted once. Capital, physical output, information and finance have different units. P3.1–P3.5 are transparent restrictions of this model; they are not a jointly closed economy.

### Three common lemmas and one notation

A free, ignorable menu expansion weakly raises optimized value **holding rival behavior and market primitives fixed**. Two organizations have equal values if two-way mappings preserve every relevant contingent program's timing, resources, rights, observation/outcome laws and claimant payoff. Two latent states remain observationally equivalent under adaptive policies when every admissible ordinary action has the same observable conditional kernel. The short proofs appear in [A.0](PROOFS.md#a0-common-lemmas).

Use $m$ only for the retained procedure in Paper 3; validated evidence is $z$. Physical robot marginal product is $MPK_r$; a forecast of it is $\widehat{MPK}_{r,t}$. $B$ is cash, never an hours budget or benefit. $e_{\rm rec}$ is successor qualification yield, $\varepsilon_i$ reducible execution error, $\lambda_{\rm ev}$ evidence arrival probability, and $\lambda^{\rm meas}_e$ measurement reliability. The exact shared-notation deltas and collisions with Papers 1–2 are in [the Lane 4 handoff](LANE3_HANDOFF.md#a-notation-delta-for-lane-4).

## 2. P3.1 — Successor-procedure production and Economic RL

### P3.1a: current success and production of a successor are distinct

A mutually exclusive research program $j$ costs $k_j$ and solves the current defect with probability $p_j$, yielding current contribution $G_0$. Conditional on success, it can pay $c_j$ to qualify a successor with probability $e_j=e_{{rec},j}$ (the program-specific successor yield), whose incrementally captured next-period stake is $S$. Failure has zero incremental payoff in this normalization. The stake and qualification choice have no omitted program-specific information, and financing, rights and validation capacity permit the chosen branch. Then

$$W_j=p_jG_0-k_j+p_j[\beta e_jS-c_j]_+.$$

If the two programs have common $k,c$, $G_0>c$, $p_1>p_0$, $p_1e_1<p_0e_0$, and $\beta e_jS>c$ for both, program 0 is strictly preferred exactly when

$$S>\frac{(p_1-p_0)(G_0-c)}{\beta(p_0e_0-p_1e_1)}.$$

At equality the programs tie; outside the active regions retain the positive parts. This ranks stipulated successor-production technologies. It does not prove that the firm invented them, that an RL implementation beats an information-matched planner, or that improvement accelerates indefinitely. [Proof A.1](PROOFS.md#a1-successor-production-and-economic-rl).

### P3.1b: three layers require three different comparisons

| Layer | Changed object | Held fixed / required discriminator |
| --- | --- | --- |
| Execution | $q\to q'$ | Same task, resources, evaluator and procedure; accepted service and costs measured |
| Inquiry procedure | $m\to m'$ | Fresh site, matched executor $q$, information access, rights, tests and resources; actual next-test choices recorded |
| Successor production | $m'\to m''$ | A third independent cohort receiving the incremental second-cohort procedure, separately from the first inherited procedure and executor |

Let $Z\in\{0,1\}$ be randomized source-history/procedure assignment to cohort 2. After cohort 2 finishes under the same announced transmission probability, randomize $T\in\{0,1\}$, passage of its incremental procedure to cohort 3. For a prespecified third-cohort economic or inquiry-performance outcome $Y_3$, the factorial contrast is

$$\mathcal D_3=\{E[Y_3\mid Z=1,T=1]-E[Y_3\mid Z=1,T=0]\}
-\{E[Y_3\mid Z=0,T=1]-E[Y_3\mid Z=0,T=0]\}.$$

Random assignment, interference control and consistent carrier definitions identify this interaction. Interpreting it as successor-procedure production additionally requires excluding transmitted answers, extra raw target information, resources and executor changes. Include all originally assigned cases, including failures and zero-successor cases. Randomizing announced rights **before** cohort 2 instead estimates the incentive to produce a transferable successor; that is a different estimand. A three-cohort design is a discriminator, not by itself a novelty claim or an existing field estimate.

### P3.1c: $MPK_r$ is a valid forecast, not a universal reward

For accepted service $Y^{acc}(K,H_{sub})=\min(D_{job},K+H_{sub})$, at $K+H_{sub}=D_{job}-1$ a cheap substitute raises accepted service by one and reduces the physical marginal product of the next robot from one to zero. Maximizing $MPK_r$ as a reward would penalize that beneficial substitution. A dated forecast remains useful when it changes the ranking of economic actions. For binary action-value difference $\Delta_a$, current information $\mathcal I$ and timely signal $Z$, its gross decision value is

$$E[(E[\Delta_a\mid\mathcal I,Z])_+\mid\mathcal I]-(E[\Delta_a\mid\mathcal I])_+\ge0.$$

Charge forecast acquisition, transmission, validation and delayed service separately. Technical success cannot be added as a second bonus to cash already reflecting that success. The historical information-matched ordinary-planner tie remains a counter-boundary, not an omitted unfavorable result. [Source disposition](SOURCE_DISPOSITION.md).

## 3. P3.2 — Two distinct evidence brakes

### P3.2a: passive failure starvation

Assume a conditional example-time law $\varepsilon_i(n)=a_i(n+b_i)^{-\alpha_i}$, with $a_i,b_i,\alpha_i>0$, $n(0)=0$, stable operating exposure $v_i>0$ and useful-record intensity $\kappa_i\varepsilon_i(n)^{\gamma_i}$, $\kappa_i>0$, $\gamma_i\ge0$. Records must be informative, admissible and effectively distinct; processing is slack. If interpreted as a probability rather than an intensity, restrict the parameters to its valid probability domain. Integrating the fluid law yields

$$(n+b_i)^{1+\alpha_i\gamma_i}
=b_i^{1+\alpha_i\gamma_i}+(1+\alpha_i\gamma_i)v_i\kappa_i a_i^{\gamma_i}t,$$

$$\varepsilon_i(t)\asymp t^{-\alpha_i/(1+\alpha_i\gamma_i)}.$$

The assumed record-time exponent and the derived deployment-time exponent are different objects. A persistent positive rate of **informative, independent** audits restores asymptotically linear record growth under the same stability/processing conditions. A target receiving a positive fixed multiple of this donor's records inherits its record-growth slowdown. Finite sums of substitutable streams and minima of complementary record requirements obey different exponent rules. None is a generic law for arbitrary skills. [Proof and exact boundaries A.2](PROOFS.md#a2-evidence-time-and-allocation).

### P3.2b: active allocation and source expansion

Let source reliability be $p\in(0,1)$ and chosen workload $u\ge0$. A job uses $h(p)=h_0+h_1(1-p)$ shared hours, $h_0>0,h_1\ge0$. Remaining hours are $H^{free}=H-h(p)u\ge0$; eligible incident-review hours are $I^{elig}=r(1-p)u$, $r\ge0$. Choose incident review $i\le I^{elig}$, independent reference work $a$ and other service $y$, with $i+a+y\le H^{free}$. Validated recipient evidence is $z=g_I i+g_R a$, with $g_I>g_R>0$. Other-service value $U(y)$ and optimized recipient continuation $W(z)$ are increasing and twice continuously differentiable, with strictly negative second derivatives in the interior.

If incident review is exhaustive and both reference work and other service are positive,

$$y+z/g_R=\mathcal H=H^{free}+(g_I/g_R-1)I^{elig},$$

$$\frac{dz^*}{d\mathcal H}=\frac{g_RU''}{U''+g_R^2W''}>0,
\qquad \mathcal H'=(H^{free})'+(g_I/g_R-1)(I^{elig})'.$$

This is the former $E'=B'+(g/e-1)I'$ in typed notation: its old $B$ meant **hours**, not dated cash. At fixed workload the sign is that of $h_1-(g_I/g_R-1)r$.

Let $k(p)=h_0+[h_1-(g_I/g_R-1)r](1-p)$ and $\mathcal H=H-k(p)u$. With source contribution $(v_sp-c_s)u-\kappa_u u^2/2$, $\kappa_u>0$, and optimized $V(\mathcal H)$, a feasible interior satisfies

$$v_sp-c_s-\kappa_u u=kV',\qquad
\frac{du^*}{dp}=\frac{v_s-k'V'+kk'uV''}{\kappa_u-k^2V''},\qquad
\frac{d\mathcal H^*}{dp}=-k'u-k\frac{du^*}{dp}.$$

For $k>0$, expansion of profitable source work can absorb more resources than improved reliability releases. This is **active hour crowding**, distinct from passive suppression of informative failures. The complete feasible frontier and corner cases are in A.2. Prices, yields and recipient stakes changing with $p$ add derivative terms; this restriction does not sign them.

## 4. P3.3 — Four identification failures and their discriminators

### P3.3a: structural reliability and measurement noise

For a binary relation on edge $e=(i,j)$, let latent vertex signs be $Z_i$, stable structural noise $U_e$, and measurement noise $\eta_e$. Write

$$M_e=Z_iZ_jU_e,\quad Y_e=M_e\eta_e,
\quad E[U_e]=\tau_e^{str},\quad E[\eta_e]=\lambda_e^{meas}.$$

With independent sign-valued structural and measurement error families, both independent of the latent signs, one reading per pair depends on the product $\tau_e^{str}\lambda_e^{meas}$. Distinct decompositions with identical products have the same observation law, including adaptive selection of new pairs. More such readings need not identify the decomposition.

Two independently refreshed measurements of the **same stable** $M_e$ satisfy $E[Y_{e1}Y_{e2}]=(\lambda_e^{meas})^2$. With a sign normalization this identifies measurement reliability, **not automatically structural reliability**. Recovering $\tau_e^{str}$ still needs anchors or identifiable graph/parameter restrictions. With latent uniform vertex signs on a forest, structural reliability can remain unidentified even after noise is learned. [Proof A.3](PROOFS.md#a3-identification-and-audit-location).

### P3.3b: audit location and an unknown joint law

Let $U$ denote a new correction, $T$ a favorable recipient-transfer regime, $p_U=\Pr(U)$, $p_T=\Pr(T)$ and $j=\Pr(U\cap T)$. A release earns $G_A$ on $U\cap T$, loses $G_A$ on $U\cap T^c$, and has zero benefit when redundant; commissioning costs $c_A\ge0$, with $G_A>0$. Perfect source and recipient audits reveal $U$ and $T$, respectively, including $T$ for a redundant candidate. Before audit fees their optimized release values are

$$V_0=[G_A(2j-p_U)-c_A]_+,\quad
V_S=[G_A(2j-p_U)-p_Uc_A]_+,\quad
V_R=[G_Aj-p_Tc_A]_+.$$

Under independence, $0<p_U<1$, $c_A>0$, and $(1+p_U)/2<p_T<1$, the source and recipient options activate at $c_A/(2p_T-1)$ and $c_A/p_U$. Once both are active, the recipient option overtakes at

$$G_A^*=\frac{c_A(p_T-p_U)}{p_U(1-p_T)}.$$

Audit purchase must also cover its own price and displaced service. Without independence, $j$ lies in $[\max(0,p_U+p_T-1),\min(p_U,p_T)]$. Sharp bounds on $V_R-V_S$ follow by checking the endpoints and the feasible kinks $j=p_Tc_A/G_A$ and $j=p_U(1+c_A/G_A)/2$. Marginal dashboards alone can leave the audit ranking unidentified.

### P3.3c–d: selection and aggregate settlement

Unknown admission and retention propensities can make two different source populations produce identical retained signs, admitted-but-unlabeled counts and rejection totals after every ordinary action. The common observation-equivalence lemma then defeats adaptive archive growth until a new observation breaks the equivalence. Known propensities, independent roster sampling or additional settlement fields can do so.

Likewise, equal-margin aggregate settlement for two conditionally independent Bernoulli lanes has generating function $(1-p_1+p_1z)(1-p_2+p_2z)$, unchanged by permuting lane success probabilities. Under symmetric actions, priors and transitions, arbitrarily many totals need not locate the fault. Tagged outcomes, unequal known margins or asymmetric releases can break that symmetry. These are distinct failures; each has its own maintained filtration and discriminator in A.3.

Repetitive partition-discovery, transfer-validation, adapter-repair and network-world sweeps are historical witnesses only. No 48–72-shift or 96-world result carries a main-text proposition. Their negative results and original scripts remain preserved at immutable sources. P2 owns deployment-portfolio/design theory; its Gaussian nuisance result is not duplicated here.

## 5. P3.4 — Dynamic boundaries and portability

### P3.4a: integrate to produce a portable interface, then delegate

An unresolved interface is one stationary state: failed attempts bring no new informative drift, calendar change or financing change. Under arrangement $g\in\{I,P\}$ and effort $a$, net flow is $\pi_g(a)$ and the chance of producing a persistent portable specification is $r_g(a)$. Mature flows satisfy $v_P>v_I\ge0$, so costless idling cannot improve on the displayed mature values. Integration costs $C_{in}\ge0$ and delegation $C_{out}\ge0$; financing permits the selected switch. With $0<\beta<1$,

$$W_P=\frac{v_P}{1-\beta},\qquad
W_I=\max\left\{\frac{v_I}{1-\beta},W_P-C_{out}\right\},$$

$$Q_g=\max_a\frac{\pi_g(a)+\beta r_g(a)W_g}{1-\beta[1-r_g(a)]}.$$

Assume the maximum is attained, for example by a finite effort menu. The stationary switching equations have values

$$U_P=\max\{Q_P,Q_I-C_{in}\},\qquad
U_I=\max\{Q_I,Q_P-C_{out}\}.$$

Thus $Q_I-C_{in}>Q_P$ selects integration while unresolved, and $(v_P-v_I)/(1-\beta)>C_{out}$ selects delegation after portability. Both inequalities can hold. A.4 proves the switching lemma, including why postponing a switch while continuing in the stationary unresolved arrangement cannot improve these values. Costless pure idling, if feasible, is included as a zero-flow, zero-transition effort option. A reserved external slot, joint lab, informative failure, debt constraint or changing opportunity adds a genuine alternative/state; the two-arrangement boundary is then insufficient. The [pinned boundary source](https://github.com/amarmurray/robotics-economics/blob/af1cabb95772524db1b34dda3b2667a54c203b43/research/recursive_firm/boundaries/README.md) supplies a constructed joint-lab alternative that overturns the restricted ownership ranking.

### P3.4b: the fixed-pair speed premium can peak in the interior

For one captured payoff $G_S>0$, internal and partner qualification lags $0<d_I<d_P$, survival probability $\rho$ per period and $\zeta=\beta\rho$, the gross internal-speed premium is

$$G_S(\zeta^{d_I}-\zeta^{d_P}),\qquad
\zeta^*=(d_I/d_P)^{1/(d_P-d_I)}.$$

The peak matters only if $\zeta^*\in(0,\beta)$. Middle-region integration additionally needs fixed overhead below the peak and above both attainable endpoint premiums. Discounting can leave a positive speed premium even at $\rho=1$. Immediate internal action, faster specialists, repeated payoffs or an optimized menu of partners change the shape. This proves neither universal integration under rapid change nor a single hump for the optimized firm boundary. [Proof A.4](PROOFS.md#a4-portable-interfaces-and-boundaries).

## 6. P3.5 — Dormancy versus activation in a funded regenerative firm

### Restricted technology and all five brakes

P3.1 supplies the successor-producing operator and the distinction from executor-only improvement. P3.2 supplies useful-evidence arrival and the value of shared hours. P3.3 determines whether those inputs and transfer benefits are identified: with unresolved joint laws, the threshold is a conditional or bounded region, not a fitted scalar. P3.4 supplies the organizational and portability alternatives that can change costs, timing and capture. The theorem below conditions on a declared institution; its dormancy certificate must also defeat every admitted organizational escape. Paper 1 owns the underlying payer-incidence and cash-time foundations.

A retained procedure $m_n$ can construct and qualify $m_{n+1}$ using the **same** direct cash cost $c>0$ and conditional technical yield $e_{rec}\in(0,1]$ at every generation. Conditional success creates a fresh cohort's incremental value $G>0$; assume $e_{rec}G>c$, so the sandbox technology has strictly positive standalone return. $G$ excludes the value of all future successor procedures; those are counted through later actions. This holds a successor-producing capability fixed to isolate economic activation; it does not itself demonstrate an accelerating or improving improver. Establishing that stronger claim still requires P3.1's matched third-cohort discriminator.

At an inquiry initiation date the firm spends $c$ and commits $h>0$ shared hours whose present opportunity cost is $h v_{op}\ge0$. The proposed procedure requires a **prospectively tagged** qualifying record from subsequent/current operating opportunities; freely banked equivalent evidence would change the model. With residual-error index $f\in(0,1]$ and starvation elasticity $\gamma\ge0$, set $\lambda_{ev}=f^\gamma$. This is the stipulated probability of a useful, transferable record per normalized operating opportunity; it is not automatically the raw failure rate. For $\gamma>0$, eliminating the unresolved cases eliminates that evidence stream.

The first record arrives at $T\sim Geom_0(\lambda_{ev})$, meaning $\Pr(T=k)=\lambda_{ev}(1-\lambda_{ev})^k$. Conditional technical qualification succeeds with probability $e_{rec}$, independently of the arrival delay and commercial hazard. An independent opportunity-specific imitation/obsolescence hazard $\delta_{obs}\in[0,1)$ operates **before acceptance**. The firm captures share $\theta\in(0,1]$ of $G$. Once accepted, its enforceable receivable settles after $d\ge0$ periods: obsolescence does not erase an already-earned debt. With $a=\beta(1-\delta_{obs})$ and $C=c+h v_{op}$,

$$R_{rec}(\lambda)=\theta e_{rec}G\,\beta^d\frac{\lambda}{1-a+a\lambda},
\qquad \Delta_{rec}=R_{rec}-C.\tag{P35.1}$$

Dated cash is a separate constraint. Let $L_t(d)$ be the maximum cash deficit of the actual committed operating outlays minus enforceable collections during the bridge. The maintained robust admission rule is

$$B_t\ge c+L_t(d).\tag{P35.2}$$

For a fresh, empty receivables pipeline, constant operating outlay rate $w$ and receipts starting after $d$, with positive net operating cash rate $s$ thereafter, $L_0=wd$. A mature, continuously operating pipeline can have $L_t=0$. Never charge the same $wd$ bridge again every generation. The exact cash-prefix proof is in A.5.

### Theorem P3.5: a dynamic regime separator

Maintain known primitives, linear monetary payoff, nonanticipating policies, at most one initiation per period, retained predecessor procedures and the specified ordinary/external menu. Ordinary learning and its feasible alternatives are included in the baseline used to define $G$ and $v_{op}$; the constant-stake closed form assumes their incremental comparison does not drift during the waiting time except through the stated hazard. Incremental payoff is additive across cohorts, all ordinary-operation effects are already included in the optimized comparator or the cohort stake, and later controls cannot improve a prepaid cohort’s receipt law except through explicitly priced actions. An extra route or omitted non-inquiry benefit requires a new comparison; A.5 states this decomposition precisely.

1. **Closed-form economic threshold.** Put $H_G=\theta e_{rec}G\beta^d$. Strict activation gain is possible exactly when

   $$H_G>C\quad\text{and}\quad
   \lambda_{ev}>\lambda_*:=\frac{C(1-a)}{H_G-aC}.\tag{P35.3}$$

   Equivalently, $\theta>C(1-a+a f^\gamma)/(e_{rec}G\beta^d f^\gamma)$. Cash feasibility still requires (P35.2). Equality gives a tie, not uniquely positive or zero research.

2. **Optimal dormancy trap.** On a forward-invariant set of states where **every reachable admitted inquiry has $\Delta_{rec}<0$**, an ordinary policy making no successor attempts is globally optimal: the discounted attempt count $N^*=0$. Cash can grow indefinitely within this set. The proof compares complete adaptive continuations, not only the first action. If margins are weakly nonpositive, zero research is optimal but may not be unique. A current negative margin alone is insufficient if it can buy access to a positive later regime.

3. **Self-funding recursive basin.** Suppose fresh cohort opportunities renew with the same positive margin, useful evidence renews with $\lambda_{ev}>0$, the ordinary operating core provides a guaranteed surplus $s>0$, all starts meet the cash-prefix constraint, and the paid predecessor survives failed attempts. Starting with enough cash to establish the operating bridge ($B_0\ge wd$ in the fresh case), operation can fund the first inquiry after a finite wait. A policy that waits for settlement, reserves $M=\lceil c/s\rceil\ge1$ operating/refill periods, and repeats sustains infinitely many attempts and qualified successors almost surely without outside finance. After warmup it has finite-mean cycle length

   $$E[L_{cycle}]=(1-\lambda_{ev})/\lambda_{ev}+d+M,$$

   and positive incremental discounted value. Technical success and commercially surviving qualification are distinguished in A.5; the applicable successor probability is strictly positive. Any optimal continuation cannot choose **permanent** dormancy in a recurrent state from which such a profitable funded attempt remains available. This establishes a feasible self-funding basin and excludes optimal permanent stopping there; it does not assert the refill policy is the uniquely optimal timing rule.

A source cash surplus finances losses on failed inquiries. Expected project profitability alone does not give pathwise solvency. Below the minimum operating bridge, with no collectible receivables, credit or other income and an indivisible operating core, a liquidity trap is possible even when (P35.3) holds. Between funding the operating core and funding an inquiry lies a **temporary financing/waiting region**; $I_t^{rec}=0$ there does not mean $N^*=0$.

### Why this is a dynamic result

For initiation times $\sigma_k$, the expected incremental value of completed protocols with zero ordinary-action residual is

$$J(\pi)=E\sum_k\beta^{\sigma_k}\Delta_{rec}(x_{\sigma_k},m_{\sigma_k}).\tag{P35.4}$$

A nonpositive ordinary-action residual makes the right side an upper bound. Voluntary abandonment without further refunds can only lower the corresponding individual receipt bound. The tower property and bounded discounted sums prove the dormancy statement on **all deviation-reachable states**. The cash-prefix invariant and operating-refill construction then prove actual continuation through failed projects. These are the steps missing from a static hurdle-rate comparison. A.5 gives the proof and its exit-action boundary.

### Cash-rich dormancy and a non-monotone profitability response

Let a parameter $z_{op}$ raise actual operating cash and inherited cash, but also raise $v_{op}(z_{op})$ or suppress residual-error opportunities $f(z_{op})$. Holding $c,e_{rec},G,\theta,\beta,d,\delta_{obs}$ fixed,

$$\Delta'_{rec}(z_{op})=
\frac{H_G(1-a)}{(1-a+a\lambda)^2}\,\lambda'(z_{op})-h v'_{op}(z_{op}).\tag{P35.5}$$

Thus $B'(z_{op})>0$ and $s'(z_{op})>0$ can relax financing while $v'_{op}>0$ or $\gamma>0,f'<0$ moves the firm into the optimal dormancy trap. If the same profitability change also raises the recipient stake $G$ or capture share, add those terms; no unconditional sign is claimed.

An exact **constructed arithmetic witness**, not a deployment estimate, holds $\beta=9/10$, $\delta_{obs}=1/10$, $d=2$, $\theta=3/4$, $e_{rec}=1/2$, $G=40$, $c=2$, $h=w=1$, $f=1/2$, $\gamma=1$. Then $R_{rec}=1215/119$, the inquiry start buffer is $c+wd=4$, and the direct technical surplus is $18$. Along $B(z_{op})=s(z_{op})=v_{op}(z_{op})=z_{op}$, $z_{op}=1$ cannot fund the minimum operating bridge, $z_{op}=5$ permits profitable funded recursion, and $z_{op}=10$ is cash-rich but strictly dormant. The technology is identical. At $z_{op}=3$ the firm can fund ordinary operation and later activate; initial inactivity is a financing wait.

### Failure-only learning can end its own recursive sequence

Fresh opportunity renewal is substantive. Without it, suppose each successful successor reduces the same residual-error index by $\eta\in(0,1)$, so $\lambda_n=f_0^\gamma\eta^{\gamma n}$, with $\gamma>0$, while $G,C$ and other parameters stay fixed. Here $f_n$ measures remaining informative cases: no admitted operation, rollback or retained old procedure can replenish them; deliberately recreated known errors supply no useful tagged evidence, and reproducing an already available procedure cannot earn the same incremental $G$ again. If $H_G>C$ and $\lambda_0>\lambda_*$, the first generation with no strict inquiry gain is

$$n_{stop}=\left\lceil\frac{\log(\lambda_*/\lambda_0)}{\gamma\log\eta}\right\rceil.\tag{P35.6}$$

Beyond it, all successors have weakly smaller margins, so the tail is an invariant dormancy region. Strictly negative states uniquely favor zero research; exact equality can tie. Initial profitable recursion therefore need not sustain itself. Bounded stakes and vanishing failure-only evidence eventually force this tail. New informative cohorts, independent references or growing incremental stakes can avert it only if the resulting margins and cash feasibility remain positive; a reference stream alone does not preserve a vanishing payoff.

### Sandbox and strategic boundaries

With $\theta\to1$, $\gamma\to0$ (hence $\lambda_{ev}\to1$), $v_{op}\to0$, $d\to0$, nonbinding cash and $\delta_{obs}\to0$, (P35.3) reduces in one line to **$e_{rec}G>c$**. That is the supplied-interface/software condition. It requires no separate firm-boundary theory to evaluate the given technical revision.

All threshold derivatives hold rival policies and the market/rights menu fixed. Endogenous entry, withdrawal, procurement responses, capture shares or hazards can change $G,\theta,v_{op},s$ and the transition law. A.COST's rival-withdrawal counterexample remains: a common surcharge can raise one firm's equilibrium profit when its rival exits. Neither that profit response nor the new activation boundary is signed by the fixed-rival theorem. No equilibrium phase diagram is claimed.

### Relation to the funded embodied null

The archived [FUNDED_EMBODIED result](https://github.com/amarmurray/robotics-economics/blob/a03659f79395ce9b7d9c06235e660a0d5e704f76/papers/integrated_firm/FUNDED_EMBODIED.md) reports cash 120, procedure caps 0/1/2 and zero selected successor attempts. Its funding bound makes the legal menus cash-independent within the stated finite game and selector; it does not make a successor valuable. P3.5 explains analytically **how funded operations can rationally remain dormant**. It does not identify which new threshold parameters generated that archived four-date equilibrium, equate its finite horizon with the renewal model, or recompute its result. Such a numerical attribution remains null. No frozen script was run.

## Appendix A.COST — Common charges and complete contingent policies

Against fixed rivals, take a finite common game tree with perfect recall, identical feasible policies/chance laws over a cost interval, and risk-neutral additive monetary payoff. Let $n_{it}\ge0$ be the designated attempt count. The surcharge enters payoff only as $-c\,d_t^{obj}n_{it}$, with objective-consistent nonnegative weights $d_t^{obj}$; every other payoff component is independent of $c$. Then

$$V_i^\sigma(c)=A_\sigma-cN_\sigma,\qquad
N_\sigma=E_\sigma\sum_t d_t^{obj} n_{it}.$$

Use $d_t^{obj}=\beta^t$ for discounted cash flows and $1$ for undiscounted terminal wealth without cash carry. The complete-policy best response is the finite maximum of these affine values: continuous, nonincreasing, convex and piecewise affine. At costs $c_1<c_2$, adding the two optimality inequalities proves $N^*(c_1)\ge N^*(c_2)$, with counts for any chosen optimizers. Research at an individual date need not decline.

A fixed complete policy's optimality region is the intersection of all inequalities $A_\sigma-A_\tau-c(N_\sigma-N_\tau)\ge0$. For a fixed behavioral profile in a finite perfect-monitoring game, the equilibrium region intersects the analogous one-shot inequalities at **every history**, including off-path histories. Backward induction proves subgame perfection. Fixed-probability supported actions can remain indifferent on an open interval only if their continuation intercepts and weighted counts coincide. Changing probabilities are not fixed mixing. Private information requires beliefs and a specified equilibrium concept.

P3.5 extends the reasoning with a stopped-sum dormancy certificate and cash-feasible continuation, not by applying convexity through changing finance menus. Regular fixed supports of two-player matrix continuation games remain rational functions when their payoff entries are rational and the indifference systems nonsingular, regardless of support size. More players, degeneracy or different primitives require additional branch analysis. [Full proof and strategic counterexample A.6](PROOFS.md#a6-common-cost-and-strategic-boundaries).

## 7. What is ready for independent review

The common state, five restricted propositions, proof dependencies, empirical nulls and every inherited source disposition are fixed in this revision. The broader RSI introduction has not been stylistically expanded. Historical numerical worlds carry no main-text proof. The main claims are conditional mechanisms, not estimates, a universal recursive advantage, or a closed repeated competitive economy.

Gate B must test whether these mechanisms add a defensible contribution beyond dynamic capabilities, absorptive capacity, learning-to-learn, experimentation/active learning and the technical RSI literature. In particular, the physical-RSI survey already discusses resource payback and controlled successive-improver tests. Gate A closure is not a novelty verdict. The [separate-author referee brief](LANE3_HANDOFF.md#b-gate-b-referee-brief-for-an-independent-author) specifies those attacks and the functional-form, funding, renewal and agent-sufficiency boundaries.

The [Robin operational packet](operational_anchor_robin.json) maps only public disclosures to $x,m$ and the three layers. It does not establish successor-procedure lift. Lane 4's Symbotic–Walmart packet remains unchanged as the contractual/rights/payment anchor with its 16 unidentified parameters. Gate C remains pending. All new numbers above are exact constructed arithmetic checks; the [verification script](verify_p35_dormancy.py) contains no finite-game solver or multi-shift simulation.
