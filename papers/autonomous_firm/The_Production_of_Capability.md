# The Autonomous and Full-Stack Firm

**Canonical Paper 2.** Gate A: in progress; Gate B: pending independent hostile-referee pass; Gate C: pending. This file consolidates the six earlier autonomous-firm manuscripts around five analytical results. The [canon register](../../research/portfolio/CANON.md) specifies every source's owner and archival status. The five other manuscripts are preserved historical editions. No new simulation or solver was run for this consolidation.

## 1. One allocation problem across dates and vintages

A robotic firm allocates current paid work, diagnostic opportunities, shared validation hours and future hardware commitments. Its best first deployment can depend on when other jobs need the same resources, which old configurations it must continue to support, and what a later customer's records can lawfully teach. These are connected choices within one firm. The paper's five results identify separate reasons a site-level learning score can rank deployments incorrectly.

The common state contains the dated order book and accepted-service criteria; installed machines and legacy obligations; the joint posterior over production and diagnostic uncertainties; retained procedures and authorized records; engineering, training and release capacity; feasible contract rights; and dated payer-specific cash. A feasible policy specifies what the firm does after each observed result. It may retain an old policy, use human or fixed-machine service, shelve a discovery, buy an equivalent outside experiment, or wait when deadlines permit.

Current contribution, a report's usefulness and the ability to act on it must be distinguished. Information has economic value through a changed feasible decision. A source can have no standalone value and still improve another source's interpretation. A better design can reduce the need to manufacture a particular machine while raising optimized value.

The five results use explicit restrictions of this common problem. They are not asserted to hold simultaneously in an already solved general equilibrium. Paper 1 owns payer incidence, qualification disclosure and product-market bidding. Paper 3 owns production of successor decision procedures, endogenous deployment-time scaling and dynamic firm boundaries. This paper cites those interfaces rather than recreating their arguments.

## 2. State, units and scope

Use accepted service, physical robot marginal product, firm value and spendable cash as different quantities, following the [shared notation table](../../research/portfolio/CANON.md#one-shared-notation-table). Track shipments, manufacturing starts, conforming hardware, installed units, successfully commissioned usable machines and accepted service separately. Commissioned machines enter usable capital; a start or shipment need not. Data possession does not establish training permission or compatibility. A shared test consumes its resources once only if its result really covers the named configurations.

Each result states its own information structure and fixed comparisons. Local legacy symbols are retained explicitly: I is a useful-trace indicator in P2.1; I is the installed-obligation set in P2.3; B in P2.3 is the present value of a release benefit, not dated cash B_(a,t); S,T and s in P2.5 are variances. Beta or delta discounts the stated continuation. Complete notation reconciliation remains a Gate A obligation.

## 3. P2.1 — Timing covariance and the unit sold



### When the timing of scarcity changes the answer

*Allocation  /  A derived implication*

Two firms can have identical demand, robots, error rates, teleoperator costs and available compute, yet rationally collect different data.

An operator can handle a paying job today or sample a fault at site A. Sampling gives up k in contribution. With probability one half it yields a usable trace (I = 1). Tomorrow, validating that trace delivers target contribution v by the deadline. It consumes a slot otherwise earning X on another job. Without a trace the other job runs. The authorized scheduler observes I and X before committing the slot. All amounts are in present-value units.

Gain from sampling = E[I × max(v − X, 0)] − k

Suppose k = 7, v = 24, and the alternative job earns either 2 or 18 with equal probability. The slot is always worth using when there is a trace. The two schedules differ solely in which state coincides with a usable trace.

| Timing of useful traces | Alternative displaced when I = 1 | Gain from sampling | Allocate operator to |
| --- | --- | --- | --- |
| All arrive in quiet windows | 2 | ½(24 − 2) − 7 = +4 | Sampling |
| Timing is independent | 10 on average | ½(24 − 10) − 7 = 0 | Either use |
| All arrive in busy windows | 18 | ½(24 − 18) − 7 = −4 | Paying job |

#### Why a site-level score misses the reversal

In this range the gain is Pr(I = 1) × (v − E[X]) − Cov(I, X) − k. A score built from average transfer yield, average compute utilization and target value gives zero in all three rows. The omitted covariance gives the entire ranking here. With higher congestion the option to decline validation also matters. The positive-part formula continues to hold when the covariance shortcut fails.

An operating prediction follows. Retiming an unrelated batch job, without adding compute or improving the model, can make a previously rejected demonstration worth collecting. The prediction requires a shared, deadline-bound slot. If traces can wait costlessly until spare capacity arrives, the relevant alternative is whatever that later slot would displace. The immediate congestion effect can disappear.

#### A test at the level of the firm

Randomize and announce eligible batch-job schedules before sampling decisions, holding total capacity and booked work fixed. Record the trace yield with occasional assigned sampling shifts, including windows the controller would normally skip. Then observe its discretionary sampling choices, accepted target work and displaced jobs. This tests a change in the allocation ranking and the firm-wide contribution it predicts. Samples gathered only on chosen shifts would confound the decision with the evidence used to evaluate it.


### Fixed hourly RaaS can penalize a speed improvement

Let r be the contracted price per robot-hour, q accepted units per billable hour, c(q) supplier cost per hour and epsilon the constant elasticity of demand for accepted service. With slack capacity, full pass-through of r/q into the service price and a nonbinding billing minimum,

$$H(q)=D(r/q)/q\;\propto\;q^{\varepsilon-1}.$$

For a g-fold speed improvement, holding the hourly price fixed,

$$\frac{\Pi_1}{\Pi_0}=\frac{r-c_1}{r-c_0}\,g^{\varepsilon-1}.$$

Demand for accepted output can increase while billed hours decrease. Whether the supplier gains depends on the margin improvement as well as elasticity. Development cost must then be deducted. Binding capacity, minimum billing, renewal, redeployment into another queue, incomplete pass-through and a per-accepted-unit contract change the comparison. For an intermediate service, the relevant demand response must account for its share in the customer's final cost and actual pass-through; an end-product elasticity cannot be inserted unchanged.

Tutor Intelligence's [posted pricing](https://tutorintelligence.com/pricing) is a contract-form anchor: the historical source edition records hourly palletizing and per-pick alternatives, with minimums and implementation/deposit terms. The archived posted terms are not a signed customer contract, realized utilization, labor substitution estimate or supplier margin. Verify the current terms before using a new numerical case. No wage-to-hourly-price comparison alone establishes profitability at matched accepted service.

**Boundary.** P2.1 combines two reasons the timing and denominator of a service contract matter. The covariance result concerns the joint timing of evidence and opportunity cost. The hourly result concerns how accepted throughput changes the billed unit. Neither proves an industry-wide equilibrium effect.

## 4. P2.2 — A fixed deadline can produce an intermediate learning peak



### 1. What a shift can teach

At an Amazon Robin workcell, a robot faces several possible grasps. Testing every candidate for reachability and collisions would take too long. The team trained a model on outcomes of actual picks to rank the candidates it would check first. Trying a grasp reveals whether it worked. The untried alternatives leave no physical outcome on that attempt. Some failures also reflected suction-cup wear, a factor absent from the model’s inputs. These features give the firm a meaningful choice over what to attempt, what to record, and whether to spend the next engineering hour on learning or on maintenance. [Li et al., §§ IV–VI](https://roboticsproceedings.org/rss19/p023.pdf)

The field study shows that experience from production can improve a grasp-ranking policy. Our model asks a further question. Can experience yield a procedure for choosing which *fresh test* to run on an unfamiliar installation? A transferable diagnostic can make a technician’s hour more productive while the new fixture still requires local validation. We allow ordinary service and deliberate investigation to teach the procedure at different rates. That difference is an assumption whose size a matched comparison could measure. It can pay to accelerate discovery only on work that falls within a usable lead, given a fixed rival. A rival that observes a qualification may also revise its own investigation.

Let $u$ be the chance that a single source shift yields the procedure, conditional on still searching. Ordinary work has yield $u_0$ and accelerated learning has yield $u_1$, with $0<u_0<u_1<1$. An initial engineering shift costing $F$ can install a capture protocol that raises discovery yield on subsequent source shifts. Costs are incremental present values of real resources or displaced work. Independent opportunities and retention until the last dated order give the probability of finding the procedure by exposure $t$ as $1-(1-u)^t$.

An ordinary target team qualifies the cheaper method with probability $h$. Holding the execution model and target test budget fixed, a retained procedure adds $g$ to that probability. Thus

$$p_u(t)=h+g[1-(1-u)^t],\qquad 0\le g\le 1-h.$$

For example, if the right diagnostic is one of $K$ equally likely tests, $m$ prepaid tests are available, and the procedure covers a fraction $\tau$ of authorized and compatible targets, then $h=m/K$ and $g=\tau(1-h)$ for $m\ge1$. With zero tests, $g=0$. The [preserved foundation](https://github.com/amarmurray/robotics-economics/blob/f3a6d0f8146c773ca7906f395f5eb52ec6fac910/papers/autonomous_firm/The_Production_of_Capability.md#how-experience-produces-a-method) derives this from the diagnostic choice. This extension holds the work available to learn from fixed while solving what firms do with it. Source jobs and target orders have reserved capacity, and only source feedback reveals the reusable procedure during the horizon. Each target purchase is counted once.

### 2. The value of a lead depends on when work is due

Two suppliers can perform the same accepted job. A qualified supplier saves $d$ on real cost relative to a feasible fallback. In one-shot reverse second-price procurement the sole low-cost supplier earns $d$. If both have low cost, the buyer receives $d$ through the price. Let $w_t$ denote discounted target volume times the saving per order at date $t$. Conditional on date and target type, the two firms’ qualification draws are independent in this section. With a fixed rival qualification path $p_r(t)$, upgrading from ordinary to accelerated learning is worth the following amount **before** paying $F$:

$$G_r=\sum_t w_t\,[p_{u_1}(t)-p_{u_0}(t)]\,[1-p_r(t)].$$

This compares the accelerated program with the firm’s own ordinary learning path. A higher eventual success rate on a benchmark need not imply a larger $G_r$. Orders may be due too early, too late, or where another supplier already qualifies.

**P2.2a. A fixed future order can make faster learning valuable only at intermediate exposure.** Suppose there is one order pool at a fixed calendar deadline, with discounted savings $D$. Every target is covered, so $g=1-h>0$. Let $a=1-u_0$, $b=1-u_1$ and $c=1-u_r$ for the rival’s fixed program, with $0<c<1$. Both firms get $n$ source opportunities before the deadline. Then

$$G_r(n)=Dg^2[(ac)^n-(bc)^n].$$

It starts at zero, becomes positive, then returns toward zero. It has one peak, allowing a tie at adjacent integers. To see this, put $x=ac$ and $z=bc$. The change from $n$ to $n+1$ is positive precisely when $(z/x)^n>(1-x)/(1-z)$. The left side falls strictly from one to zero. Consequently the exposures at which the upgrade covers a fixed positive cost form a single interval, possibly empty. The simple peak proof uses full coverage. The decaying difference between own ordinary and accelerated learning survives partial coverage in this model.

| Shifts before the deadline | Value against an ordinary rival | Value against an accelerated rival |
| ---: | ---: | ---: |
| 1 | 6.75 | 4.50 |
| 2 | 9.11 | 4.05 |
| 3 | 9.35 | 2.77 |
| 4 | 8.64 | 1.71 |
| 5 | 7.57 | 1.00 |
| 8 | 4.45 | 0.17 |

Illustrative values use $D=100$, $h=g=0.5$, $u_0=0.1$, $u_1=0.4$. At a setup cost of 8 the firm invests at two through four exposures against an ordinary rival. Now hold target demand, resources and five total source shifts fixed. Move the target deadline from after shift five to after shift three. The decision flips from passing at 7.57 to investing at 9.35, in undiscounted units. This isolates timing from customer volume.

If another paying cohort is *added* after each shift, the gain through date $N$ is a sum of nonnegative dated gains. It rises with $N$ whenever another cohort falls inside the lead, even though the gain on the last cohort declines. This comparison expands demand. It answers a different commercial question from retiming the same order.

### 3. When to spend the next engineering shift

Now let the firm choose separately on each source shift. While searching it can do ordinary work or give up $k_t$ in current net contribution to raise that shift’s discovery probability from $u_0$ to $u_1$. It observes its own discovery immediately. Once acquired, the procedure already works, and further investigation cannot improve it. Target orders are dated, the rival follows a fixed path, and the firm observes no signal that changes its forecast of that path. This is an adaptive alternative to committing the full setup cost in advance.

Let $m_t$ be the **undiscounted** incremental margin at date $t$ if the firm knows the procedure by settlement rather than remaining without it. With target value $d_t$ times volume $N_t$, $m_t=N_td_t g[1-p_r(t)]$. Write $B_t$ for the difference in optimized value, before the source shift, between already knowing and still searching. With one-period discount factor $0<\delta\le1$ and $B_{T+1}=0$, define

$$S_t=m_t+\delta B_{t+1}.$$

**P2.2b.** Buy extra investigation when $(u_1-u_0)S_t>k_t$, skip when it is smaller, and take either action at equality. The exact recursion is

$$B_t=(1-u_0)S_t-\max\{0,(u_1-u_0)S_t-k_t\}.$$

**Proof.** Relative to an unknown firm that gets no discovery this shift, a known firm gets $S_t$. An unknown firm already earns $u_0S_t$ through ordinary operations. Accelerating adds the probability difference times $S_t$ and costs $k_t$. Both alternatives can reoptimize on every later shift. Subtract the best unknown value from the known value to get the recursion.

**Why waiting can be optimal.** Suppose only the final cohort pays, costs and yields are constant, and the rival path is given. Before the deadline $S_t=\delta B_{t+1}\le\delta(1-u_0)S_{t+1}\le S_{t+1}$. Thus, conditional on still searching, the dates on which extra investigation is strictly preferred form a suffix. Early ordinary production has time to reveal the answer. As the deadline approaches, the option to wait expires. Earlier orders can reverse the timing of investment.

For five shifts, $u_0=0.1$, $u_1=0.4$, $k=4$, $\delta=1$, and $m_5=20$, the firm buys extra investigation only on shifts three through five if still searching. Move the same margin of 20 to shift one and it buys only on shift one. In both cases it stops paying for investigation as soon as the procedure is found. This comparison gives a fleet planner a different metric from total hours logged. The planner needs the dated work a discovery could change and the remaining chances that routine service will teach it anyway.


## 5. P2.3 — Installed obligations and the last legacy customer

A discovered procedure must pass through a feasible release arrangement. Separate interfaces, adapters, outside testing and a retained old version belong in the comparison. The following result isolates a configuration-level obligation rather than assuming every customer adds an identical cost.

### What a working fleet commits the firm to

In November 2024, Universal Robots told owners moving certain arms from a PolyScope 5 controller to PolyScope X that programs and settings had to be recreated and earlier plug-ins could not simply be reused. Its announcement to developers described a period of parallel support for the two platforms. The physical task could still be familiar to a gripper supplier while the implementation needed fresh work. An industry standard can change this margin too. VDA 5050 specifies the exchange of jobs and status between a fleet controller and mobile robots from different manufacturers. The documents establish feasible engineering arrangements. The economic costs, deadlines and customer commitments below are model assumptions. [Universal Robots migration guidance](https://www.universal-robots.com/articles/ur/documentation/upgrading-from-a-polyscope-5-controller-to-a-polyscope-x-controller/) · [Developer announcement](https://forum.universal-robots.com/t/polyscope-x-open-beta-announcement/36988) · [VDA interface specification](https://www.vda.de/en/news/publications/publication/vda-5050)

Two relationships matter. **Where can this experience teach?** A trace from a jam can identify which fresh test to run on a different fixture. **Whose existing work must remain qualified if that test-selection procedure goes into production?** The procedure might run inside a release that also dispatches older arms, or as a separate advisory tool on one cell. Retaining a trace, authorizing its reuse, changing a shared release, and accepting a physical installation are different rights. Competent people and digital agents face the same economic comparison when they have the same information, authority and resources.

Let $I$ be the installed obligations, each defined by an acceptance condition, a supported configuration and a date. Let $H$ be the validation hours available before the next opportunity expires. For a specific discovery, enumerate feasible release plans $a$. A plan specifies who receives the update, which configurations stay on old versions, and all tests, labor, cash and permissions required. Let $W_1(I,H)$ and $W_0(I,H)$ be the best date-one net values with and without the discovered procedure. The second value conditions on reaching this decision without the focal source discovery. Both programs can still learn locally or catch up before expiry. The conditional value of the discovery is

$$R(I,H)=W_1(I,H)-W_0(I,H).$$

The firm can shelve a discovery, so this option is nonnegative when acquiring it adds no obligation. A plan can pool tests, isolate a pilot, migrate customers, buy outside testing, or wait if the opportunity survives. A test shared by three sites occupies its resources once when its result is genuinely reusable. If the sites need independent checks, each consumes time. Holding the beneficiaries fixed, an extra obligation can lower $R$. Duplicating an already covered configuration adds no check in this case. An extra buyer that also benefits from the change can raise $R$.

### Why the last site matters

Suppose several customers use one legacy configuration. Each can migrate to a supported alternative. As long as one customer remains, the same legacy check is required whenever a common change is released. Migrating the first customer can improve its own operation. Migrating the last one can also free a validation window for an unrelated buyer. The additional benefit comes from eliminating a distinct obligation. If every site instead requires its own additive checks, that particular discontinuity disappears.

Let $B$ be the present value of the shared continuation gain from retiring this final obligation. Calculate it after both regimes choose their best investigation and release paths, including an adapter or outside support if feasible. Exclude the customers' separate migration costs. There are $n\ge2$ customers with net moving costs $c_i>0$ after direct local benefits. Suppose configuration-wide learning and release benefits change only at collective migration. If all migrate, customer $i$ receives share $\alpha_i$ of $B$. Count gains across beneficiaries once. A payment from one participant to another reallocates the gain.

**P2.3.** When $B>0$, retiring the configuration is jointly worthwhile if $B>\sum_i c_i$. In a simultaneous, uncoordinated decision, staying put is a strict equilibrium. A lone mover pays and leaves the common obligation in place. Full migration is also an equilibrium precisely when $\alpha_i B\ge c_i$ for every customer. With positive costs, any partial set of movers includes someone who could save money by staying. Thus a jointly valuable transition can fail even when everyone knows the technology and its costs.

The customer shares $\alpha_i$ and sponsor share $\alpha_S$ are nonnegative, nonoverlapping claims on the same benefit $B$, with $\sum_i\alpha_i+\alpha_S\le1$. If the sponsor is also a customer, count its claim and migration cost once. A sponsor with share $\alpha_S$ and authority to sign a binding, all-party migration agreement can offer conditional payments. If it can subsidize but cannot charge other beneficiaries, the smallest total subsidy making full participation individually rational is

$$T_{\min}=\sum_i\max(0,c_i-\alpha_i B).$$

The sponsor can cover it from its gain when $\alpha_S B\ge T_{\min}$ and the required financing is available on the migration dates. A fleet owner, a controller supplier or a buying cooperative can play this role. Ownership matters through the claims, authority and financing it conveys.

**The legacy site may also be a teacher.** Let $s,s'$ be the probabilities of a useful discovery per opportunity before and after retirement, and $r,r'$ the respective conditional values of a usable discovery. If retirement lowers $s$ to $s'$ while raising $r$ to $r'$,  the fixed-policy gain per opportunity before discounting is $s(r'-r)-(s-s')r'$. It can have either sign. This changes the migration calculation. Removing a production obligation and disposing of the physical machine can be separate choices.


## 6. P2.4 — Future rights can change the first deployment

The installed base has two roles: it supplies current obligations and can receive improvements discovered by a later vintage. Backward induction must value future rights before choosing the first site. The exact example below is synthetic and uses fixed prices, funded builds and a restricted information technology. It establishes a strict mechanism within those assumptions; it does not estimate the magnitude in a commercial fleet.

### Three vintages with paid customer work

A legacy robot has one operating shift. The firm chooses a routine or unusual site. It must then commit design 1, standard or specialized. Commissioning reveals the first bottleneck regardless of whether a diagnosis arrived early. Design 1 fills one order window, then operates a separate shift that can produce evidence for design 2. Design 2 is the final build. One unit per build is already commercially justified and funded. This restriction isolates the composition of new machines. Optional manufacturing starts are treated separately in the historical source appendix and in P2.5 below.

Each generation has an independent mechanical or control bottleneck, equally likely. A routine site's conclusive report is timely with probability $1/4$, an unusual site's with probability $3/4$. Without a report the firm retains its prior. The standard machine earns 4 units of contribution on routine work. A specialized machine can do the same work, costs 4 extra to build, and can qualify for a higher-paying order in the mechanical state. That order earns 10 in the first generation and 14 in the second, before the extra build cost. The firm chooses the best qualified buyer. All values are illustrative, after common costs, in one numeraire with $\beta=1$.

| Field decision | Routine customer | Unusual customer |
| --- | --- | --- |
| Contribution from the legacy robot's shift | 2 | $11/8$ |
| Contribution from design 1's later field shift | 2 | $1/2$ |
| Access to that later shift | Always | Requires the first specialized design and successful mechanical-state qualification |
| Chance of a reusable model candidate in the later shift | $1/4$ from the common source | $3/4$ with permission and $1/4$ from the common source alone |

A retained model candidate in the later shift can be trained for 1. It lets a separate surviving old workcell accept two additional orders at contribution 2 each. The old unit has the spare time and rights to serve those orders. Training therefore earns 3 net when the candidate exists. The model does not affect qualification for the new unit's higher-paying order in this restriction. Local disclosure of the bottleneck for hardware diagnosis remains available in both permission regimes. The permission change governs reuse of the future trace for fleet training. The candidate is independent of the bottleneck and the timing of its diagnosis. The first field shift has no differential trainable-candidate return. Common training or production can be added to both first-site alternatives.

### A future customer's data rights change the first deployment

Start with the final factory decision. Gross advantages are $a_M=14-4=10$ and $a_C=0$, with switching cost 4. The firm ordinarily specializes. A timely control-state diagnosis avoids spending 4. Thus the expected value of a conclusive final-factory diagnosis is $I_2=(1/2)4=2$. At the later unusual site the extra probability of timely diagnosis earns $(3/4-1/4)2=1$. With reuse permission, the extra probability of a trainable candidate adds $(3/4-1/4)3=3/2$. The sacrifice in current site margin is $3/2$. Access to this customer is worth 1 after the firm chooses its best site. Without reuse, the extra return to training disappears and the firm chooses the routine site even when the unusual one is accessible.

At the first factory, the specialized design's mechanical-state advantage is $10-4=6$ for the first service window. If its successful qualification opens the valuable subsequent shift, that advantage becomes 7. In the control state the advantage stays zero. With cost 4 the firm would ordinarily build the standard version in either permission regime. The value of an early diagnosis is 1 with future reuse denied and $3/2$ with future reuse permitted. The first unusual site's reporting advantage of $1/2$ is therefore worth $1/2$ or $3/4$. The initial service margin forgone is $5/8$. The optimal first site changes strictly.

| Outcome from the initial decision | Future reuse denied | Future reuse permitted |
| --- | --- | --- |
| First deployment | Routine | Unusual |
| Expected optimized net contribution | $29/2$ | $59/4$ |
| Probability of a specialized first build | $1/8$ | $3/8$ |
| Probability of a specialized second build | $7/8$ | $25/32$ |
| Expected additional accepted orders on the old workcell | $1/2$ | $7/8$ |

The first build specializes more often because evidence can authorize entry to a customer whose traces now have a future use. The second specializes less often because better evidence sometimes cancels a poor hardware change. The surviving old workcell gains more accepted work through its own model update. Both new units still get built. Those three outcomes are compatible inside one firm at the same prices and order book.

The first-site reversal holds for every forgone margin strictly between $1/2$ and $3/4$. If future traces add no genuinely new training information, or the future customer is equally reachable with the standard first design, the permission premium on that earlier hardware decision disappears. The [replication](replication/capability/full_stack_vintages.py) checks the recursion against 2,048 contingent site and hardware plans per permission regime, with training and dispatch optimized in each state.

### Why better hardware can increase the demand for sensing

The site-choice result conditions on how evidence is produced. The firm can also change that technology in the factory. Consider one source workcell and a horizon with $N$ other compatible uses. A mechanical fix eliminates a fraction $h$ of the otherwise informative failures on the source cell. Let $p_f$ be the initial probability of a useful failure and $q_c$ the probability of capturing a usable record conditional on that failure. For a single source opportunity, yield falls from $p_f q_c$ to $(1-h)p_f q_c$. Suppose the downstream demand for the learned correction survives the source redesign. A usable record creates expected incremental saving $b$ per reachable target after local costs and ordinary learning.

Let $G$ be the discounted direct net gain from improving source reliability, including design, installation and displaced work. Under failure-based recording, the value of redesign is $G-\beta h p_f q_cNb$. A sensor costing $C$ can recover a fraction $\lambda$ of the *useful records lost to the fix* by measuring force precursors on otherwise successful picks. If the sensor has no other use on the original machine, the optimized gain from the option to redesign is

$$\left[G-\beta h p_f q_cNb+[\beta\lambda h p_f q_cNb-C]_+\right]_+.$$

The inner expression is the best payoff conditional on redesign; the outer positive part preserves the original machine. This follows from choosing among the original machine, redesign alone, and redesign with instrumentation. The sensor changes which hardware is manufactured when redesign alone loses but redesign with the sensor earns a positive gain. Here measurement and mechanical reliability are complements, although mechanical reliability reduces the supply of failure data. An instrument already useful on the standard machine must be priced on both alternatives.

Replace $Nb$ by $\sum_j N_j b_j$ for different tasks, remaining service lives and compatible vintages. A sensor on the new batch can pay because its records improve old machines that will never receive it. Imminent retirement of that installed base can change the new bill of materials. If the same mechanical fix removes the need for the learned correction everywhere, the downstream value must be recomputed. The relative return to operating a reference cell, retaining an archive or simulating rare events depends on whether it supplies equally useful diagnoses on fresh physical jobs.

A recovered trace can supply a trainable policy and can change the information available for the next hardware choice. These are separate margins only after conditioning on what the trained policy itself reveals; assigning both an independent premium can double-count information.


## 7. P2.5 — Complementary diagnostics carried into manufacturing scale

A diagnostic portfolio must preserve the joint law of what its observations mean. The next result endogenizes the recipient fleet instead of treating data value as a fixed premium per deployment.

### 2. A production problem with two unresolved causes

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

where measurement errors are mutually independent Gaussian variables, independent of $(\theta,\nu)$, with zero means and variances $r_A,r_B>0$. Gaussianity is required for the conditioning and ex ante formulas below; moments alone are insufficient.

For an applied interpretation, suppose the next design must accommodate a task-specific load, while an uncertain calibration parameter affects the readings used to infer that load. Production configuration $B$ mixes the two. A reference operation at $A$ isolates the calibration parameter. This is a local, stylized measurement model. It requires a reason that the same nuisance affects both records; arbitrary sites do not satisfy it.

The firm first chooses a source portfolio $E\subseteq\{A,B\}$. Its current net cost includes hardware, integration, measurement, permissions, support and the value of ordinary service displaced. After the records arrive, the firm chooses its next design and manufacturing quantity. Both sources and all subsequent designs satisfy the maintained service requirements. Failure to meet those requirements is not a free learning technology.

#### The state must preserve relationships between unknowns

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

### 3. Proposition: individually weak sources can be jointly valuable

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

#### Faster accumulation can increase the value of a different source

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

This contrasts with independent chances of finding the same rule: for a fixed prize and common success probability u, discovery probability 1-(1-u)^n has diminishing increments across n opportunities. One source can then substitute for another. When one source separates causes mixed by another, improving the latter can make the former more valuable. “Faster learning” has to identify which part of the learning technology improved.

For a fixed cost of obtaining $A$, a firm can therefore initially concentrate on $B$ and later add $A$ as the accumulated $B$ evidence makes the contrast worth buying. That is a comparative static holding the recipient exposure and costs fixed. Aging recipients, shorter remaining deadlines or changing demand can reverse the chronological prediction.

The information floor also has a sharp boundary. If each $B$ observation redraws an independent nuisance with a known mean, averaging removes nuisance uncertainty. If the firm can vary $B$'s known loading on $\nu$, it may generate the necessary contrast without another site. A cheap factory test may dominate a new deployment.

### 4. The next design and fleet are choices

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

#### Proposition: evidence changes design, scale and entry

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

#### An exact ex ante value

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

### 5. What determines the marginal value of learning?

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

### 6. Joint source entry with endogenous manufacturing

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

#### Proposition: the portfolio can pay when neither site pays alone

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

#### A conditional competitive implication

In this uncapped expansion model, reducing posterior variance weakly increases expected manufacturing quantity. Also $H_m(s)=E[N^*(s)]$. Thus

$$
\frac{\partial}{\partial m}
\{H(s_{AB})-H(s_B)\}
=
E[N^*(s_{AB})]-E[N^*(s_B)]\geq0.
$$

A reduction in captured unit margin can weaken the firm's incentive to acquire the complementary source, even with the same observation technology. This is a partial-equilibrium comparison in a stipulated margin. Competition, customer pricing and industry-wide quantities are not solved here.


## 8. Boundaries, empirical discrimination and proof ownership

The five mechanisms are distinct. A deadline peak requires retiming a fixed cohort, while adding future cohorts changes total demand. A timing covariance requires a genuinely shared dated slot. A last-site discontinuity requires a shared configuration obligation, while additive site checks behave differently. The three-vintage reversal requires incremental lawful reuse and design-dependent access to the future site. The nuisance contrast requires a shared persistent confounder, not arbitrary environmental variety.

In P2.5's uncapped Gaussian expansion model, information can increase expected manufacturing. With a hard cap, indivisible batches, deadline constraints or changes in recipients, more information can instead cancel bad starts and reduce expected units. Its decision value remains nonnegative only when the firm can ignore costless evidence and retains the original menu. Purchasing an experiment or reserving cash/resources can change the feasible alternatives; compare net investment value over the complete cash-feasible programs. A cash constraint by itself does not destroy the value of free, ignorable information when the menu is unchanged. The historical portfolio appendix keeps the capped and two-generation cases; they are not silently extrapolated from the uncapped formula.

Operational anchors establish particular premises: Tutor identifies a posted contract unit; Universal Robots identifies an actual migration/interface issue; a commercial data agreement can identify a permission structure. None identifies every model parameter. The first cross-paper [Lane 4 record](../../research/portfolio/empirical_target_symbotic.json) preserves actual implementation times, costs, transfer probabilities and joint signal laws as null. A later Paper 2 case must map a release or vintage decision specifically before Gate C can pass.

### Proof and replication map

| Claim | Preserved source / script | Qualification |
| --- | --- | --- |
| P2.1 timing | Choosing_the_First_Deployment.md; replication/deployment/allocation_and_bids.py, check_allocation | Procurement functions in the same file belong to P1 |
| P2.1 hourly service | The_Autonomous_Firm.md; replication/labor_checks.py | Conditional price/demand arithmetic; no causal deployment estimate |
| P2 supporting allocation appendix | The_Autonomous_Firm.md; replication/physics_checks.py | Correlated rescue-fault allocation, not the hourly-price check |
| P2.2 | When_Faster_Learning_Pays.md; replication/capability/learning_deadlines.py | Fixed-rival timing proof; rival-response extensions are P1 interfaces |
| P2.3 | [Original manuscript](https://github.com/amarmurray/robotics-economics/blob/f3a6d0f8146c773ca7906f395f5eb52ec6fac910/papers/autonomous_firm/The_Production_of_Capability.md); replication/capability/installed_base.py | Shared-release, migration and reference-cell restrictions |
| P2.4 | FULL_STACK_FIRM.md; replication/capability/full_stack_vintages.py | Exact synthetic contingent-plan comparison in the saved implementation |
| P2.5 | DEPLOYMENT_PORTFOLIOS_AND_DESIGN.md; replication/capability/diagnostic_portfolios.py | Analytic Gaussian formulas and numerical checks with stated tolerances |

The earlier complete manuscripts are preserved at input main [f3a6d0f8146c773ca7906f395f5eb52ec6fac910](https://github.com/amarmurray/robotics-economics/tree/f3a6d0f8146c773ca7906f395f5eb52ec6fac910/papers/autonomous_firm). The five noncanonical files now carry archive banners. The old replication/run.py does not invoke every capability script and cannot certify this whole paper. Code and saved output bytes have not been changed or rerun for this consolidation. A new finite solver invocation requires a named proposition and preregistered falsification question under AGENTS.md.

Gate A still requires complete notation/proof-link reconciliation, a claim-level comparison with the closest prior art and disposition of all source qualifications. Gate B then requires an independent hostile referee. The historical general referee report and this editorial integration do not satisfy that pass. Allocator self-revision, deployment-time scaling and dynamic make-versus-buy arguments are routed to [Paper 3](../../research/recursive_firm/README.md); general cash incidence and disclosure competition are routed to [Paper 1](../learning_and_capital/README.md).

