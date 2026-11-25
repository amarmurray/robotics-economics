# The Production of Capability

*How work changes what a firm can learn, deploy and earn · Revised working paper · November 25, 2026*

A warehouse robot clears a jam. A software agent resolves an invoice discrepancy. Either service can be completed without learning how to handle a different job. Someone must choose which cases to inspect, which observations belong together, and which fresh test is worth a scarce validation slot. A firm produces a capability when that work changes the set of services it can deliver at a given cost, quality and deadline. It produces a capability for learning when earlier work changes what the next experiment can accomplish.

**A deployment leaves the firm with both experience and commitments.** A correction found at one site may teach a gripper supplier which calibration to try at another. If using the correction requires changing a shared controller, existing sites may also have to demonstrate that they can still deliver their orders. Those sites can consume the validation time needed to reach the new buyer, even when the correction offers them no direct gain. A supplier that can update the new site separately faces a different investment decision with the same robots, evidence and discovery.

### Two questions about the same hour of work

What should the firm give up today to obtain a reusable method of inquiry? The first model derives the value of an instrumented job when ordinary work also teaches, target sites still need local tests, and a rival can qualify the same orders. A better diagnostic rule makes the first test more valuable and the extra tests used for search less valuable. Competition can reward a firm for keeping a source from its rival even when it cannot learn from that source itself.

What makes the firm willing to put the discovery to work? The extension beginning on page 7 values each way of using a new method while honoring the installed fleet's commitments. It explains why better routine learning can favor a more uniform fleet while cheaper validation can favor a more varied one. It also identifies when the final customer using an old configuration can hold up upgrades elsewhere, and when a firm will take a workcell out of paid service to keep it for experiments. The final pages propose observations that would distinguish these mechanisms from slower discovery, poorer hardware or stronger demand.

In both models the comparison is the best feasible program that keeps learning through ordinary operations. The unit of value is additional accepted customer work or avoidable real cost. The firm's private return also depends on what the next-best supplier can do and who captures the saving.

<!-- page -->

## How experience produces a method

At the first date, each supplier has $B$ opportunities to do source work. At the second date, two suppliers compete for $N$ new jobs. Jobs meet a common acceptance standard. A conventional method costs $C$ per job. A qualified new method costs $C - d$, with $d$ positive. Both methods deliver the same service. This restriction makes prices and real resource savings separately observable.

### Source allocation

Each firm commits in advance which $n$ of its $B$ opportunities to instrument. Ordinary service can already produce a record that reveals a reusable rule, with probability $u_{0}$. An instrumented opportunity does so with probability $u_1>u_0$. A revealing record pairs a known context with a verified diagnostic. Other records supply no information about the rule. With independent opportunities, the chance of acquiring the rule is

$$s(n)=1-(1-u_1)^n(1-u_0)^{B-n}.$$

The proof counts the chance that every record misses. At equal output, a preauthorized recording procedure can increase $u$ by capturing informative cases that would expire during approval. If the procedures differ only in response time, the increase equals the probability of a permitted, informative case that only the faster procedure can capture in time. Either a human or an agent may hold that authority.

### Target qualification

Each fresh job has a visible marker $z$ and a local setting that must be verified. Exactly one of $K$ diagnostics certifies the setting. On compatible jobs its index is $(z+\theta_i)\bmod K$. The firm-specific offset $\theta_{i}$ is initially uniform. A revealing source record identifies it. On other jobs the correct index is independently uniform. The compatible and authorized share is $\tau$. A source record never supplies the fresh setting itself.

Each firm has prepaid capacity for $m$ distinct checks per target before expiry, with $0\le m\le K$. Without the rule its best success chance is $h = m/K$, since any $m$ distinct indices cover the same fraction. With the rule it succeeds on a compatible job whenever at least one check is available. Let $b$ equal $1-h$ when $m>0$, and zero otherwise. Qualification thus has probability

$$p_i(n)=h+\tau b s(n).$$

Target checks for the batch must be assigned before cross-site feedback arrives. The two firms’ local conventions, applicability draws, and capture events are independent across firms for a given job. Jobs within a firm may share one rule. Marginal test costs are sunk in this benchmark.

<!-- page -->

## The price of a learning opportunity

A buyer awards each target job by reverse second-price procurement. Both suppliers know their realized costs before bidding. The low-cost supplier wins and receives the other bid. If only firm $i$ qualifies, it earns $d$. If both qualify, the price falls by $d$ and neither earns a margin. With a discount factor $\beta$, define $D = \beta Nd$. Holding the rival’s qualification probability $p_{r}$ fixed, firm $i$’s expected target profit is $D p_i(1-p_r)$.

### Proposition 1 · The marginal value of instrumenting a source job

For $0\le n<B$, the largest current contribution the firm would give up to switch one more opportunity from ordinary to instrumented service, before observing any source results, is

$$w_n=D(1-p_r)\tau b(u_1-u_0)(1-u_1)^n(1-u_0)^{B-n-1}.$$

**Proof.** The switch adds a rule only if the switched case supplies incremental evidence and every other opportunity misses. Multiply that probability by the gain $\tau b$ in qualification and by the expected margin on the reachable orders. Independence supports the product. At constant or nondecreasing marginal instrumentation cost, the firm switches jobs while their marginal value exceeds cost. Ties permit either choice.

Operator effort, a digital workload displaced from a validation slot, consent fees, and delayed current service all belong in this comparison. A shared model that improves the rival’s fallback can depress the bid for field experience even while own technical transfer is unchanged. Actual costs of testing, if avoidable, also belong in the comparison.

### An investment in the process of learning

Suppose a firm can pay $F$ for a better procedure that raises the instrumented yield from $u$ to $u'$. Let $V(u)$ be the maximum over $n$ of target profit less the cost of instrumenting $n$ source jobs at that yield. The investment pays if $V(u') - V(u) > F$. Both versions can change the number of cases they inspect. A reusable procedure that earlier work discovered is one candidate investment. A purchased system or timely standing agreement is another.

**A retained method and the first validation slot are complements. Once one slot exists, the same method substitutes for the extra capacity used to search.**

This result extends to any increasing ordinary qualification curve H(m) with H(0) = 0. Let λ be the chance a usable rule identifies the right first test. The first slot gains H(1) + λ[1 − H(1)], increasing in λ if H(1) < 1. Every subsequent slot gains (1 − λ)[H(m+1) − H(m)], decreasing in λ where extra slots help. With multi-stage validation or avoidable test costs, the sign can differ.

<!-- page -->

## Why identical firms can diverge

Allow one source job per firm. Let $p_{0}$ and $p_{1}$ denote the target probabilities under ordinary and instrumented source work, and let $\Delta=p_1-p_0>0$. The firms decide simultaneously. Instrumenting costs each firm $k$ in current contribution.

### Proposition 2 · An investment equilibrium

Investment earns $G_0=D\Delta(1-p_0)$ before cost if the rival continues ordinary work, and $G_1=D\Delta(1-p_1)$ if the rival instruments. When $k$ is below $G_{1}$, each invests. Above $G_{0}$, neither does. Between them, each firm’s best response is to do the opposite of its rival. Exactly one invests in either pure equilibrium. In the symmetric mixed equilibrium each invests with probability $(G_0-k)/(D\Delta^2)$, obtained by equating the expected incremental gain to cost. At the boundaries there is indifference.

### A worked economy

Use two diagnostics, one available test, complete compatibility, and an ordinary source yield of 0.20. Active capture raises yield to 0.80. Thus $p_0=0.60$ and $p_1=0.90$. With a discounted cohort saving $D$ of 100, the same thirty-point qualification gain earns 12 against an ordinary rival and 3 against an instrumenting rival. Set $k=6$.

| Source choices | Firm 1 net | Firm 2 net | Buyer saving | Net total |
| --- | --- | --- | --- | --- |
| Both ordinary | 24 | 24 | 36 | 84 |
| Only firm 1 instruments | 30 | 6 | 54 | 90 |
| Both instrument | 3 | 3 | 81 | 87 |

All entries use conventional service at cost $C$ as the reference. The buyer saves 100 times the probability both firms qualify. Gross real cost avoided is 100 times the probability at least one qualifies. The net figures deduct each firm’s instrumentation cost once. In the symmetric mixed equilibrium each invests with probability two thirds.

### A temporary demand shock changes future supply

Give one firm a current order that raises its displacement cost above 12. Give the other spare staff so its cost is below 3. Their choices are now strict whatever the other does. After those orders expire, the firms face the same fresh work with qualification probabilities of 0.60 and 0.90. The better-paying current opportunity can leave a firm less prepared for the next market. The example derives a one-cohort difference. Its duration depends on how quickly the rival can recover the procedure.

### What would a rival pay to copy?

If a purchasable method increases the rival’s qualification probability by $\Delta$ at an all-in price $L$, it buys when $D\Delta(1-p_{\mathrm{leader}})>L$, given the leader’s current program. Cheap, transferable software can replicate a routine. Permissions, calibration and a scarce commissioning window can raise the price of an equivalent installed capability.

<!-- page -->

## Who controls the source?

Keep the same qualification technology and downstream market. Change one institution. Only the firm awarded a particular source deployment gains the additional opportunity to learn from it. Without the award the firms qualify with probabilities $p_{i}$ and $p_{r}$. The winner’s own probability rises by $\Delta_{i}$ or $\Delta_{r}$, as determined by capture and target testing. Both keep their ordinary alternatives.

### Proposition 3 · Productive use and exclusion enter the same bid

Let $W_i$ be firm $i$’s willingness to pay for exclusive access.

$$W_i=D\left[(1-p_r)\Delta_i+p_i\Delta_r\right].$$

**Proof.** If $i$ wins, its target profit is $D(p_i+\Delta_i)(1-p_r)$. If its rival wins, it is $D p_i(1-p_r-\Delta_r)$. Their difference gives the two terms. The first values new production capability. The second values preserving a margin the rival would otherwise erase. A source service fee also reflects current service costs and displaced work.

Suppose the rival cannot learn from this source. It can still value excluding the learner from it. With equal current service costs and one mandatory award, the rival outbids the learner when its independent probability of qualifying exceeds one half. It values exclusion at $D p_r\Delta_i$ while the learner values access at $D(1-p_r)\Delta_i$. Giving both the same learning rights regardless of the award erases this component of both bids.

| Rival readiness | Learner’s bid for access | Rival’s bid for exclusion |
| --- | --- | --- |
| 0 | 30 | 0 |
| 1/2 | 15 | 15 |
| 1 | 0 | 30 |

Gross bid values in the case $D=100$, $\Delta_i=0.30$ and $\Delta_r=0$. These bid schedules follow from the procurement example. Only the learner can lower production cost by obtaining this source.

### How long is the advantage worth having?

If the relative advantage is identical in each active cohort and disappears permanently once the rival catches up or the method expires, discounted rent is the sum of each cohort’s rent times the probability the lead survives to that cohort. With per-cohort rent $R$, first cohort next period, and constant conditional survival $\rho$, the sum is $\beta R/(1-\beta\rho)$. Catch-up that depends on rival investment requires solving that investment decision. A durable claim needs evidence on copying costs, access terms and the timing of decay.

<!-- page -->

## Across tasks, machines and markets

At firm scale, current capability consists of the portfolios of work achievable at each cost and deadline. An operating choice changes today’s payoff and tomorrow’s attainable portfolios. Recursion occurs when a choice changes the procedure by which later work expands those portfolios.

### A generalization that allows correlated learning

For original target opportunity $j$, let $Y_{ij}$ be one if the firm qualifies for the cost saving before the deadline. Index the firm’s complete, separately evolving programs by 0 and 1. Let $v_{j}$ be the discounted real cost saving. With the same two-supplier pricing and a rival whose outcomes are unaffected, the gross private difference is

$$\sum_j v_j E\left[(Y_{ij}^{1}-Y_{ij}^{0})(1-Y_{rj})\right].$$

Each program’s margin uses its joint outcome with the rival and allows regressions as well as gains. Multiplying average technical improvement by average rival failure requires zero covariance. Learning on a rival’s strongest tasks can yield the same benchmark gain as learning on underserved work and a different private return. If rivals respond, use the new joint outcomes under each program.

**Where to deploy.** Two source jobs of equal current value each raise qualification by 0.30 in a different market worth 50. Against rival readiness of 0.90 and 0.60, the respective future gains are 1.50 and 6.00. A rival release raising readiness in the second market to 0.95 cuts its gain to 0.75 and reverses the preferred source. Neither source’s technical yield has changed.

### Two different relationships connect tasks

Similar faults can make a pair of sites good teaching partners. Synchronized deadlines can make them poor partners for sharing an operator. The sum above requires that the wins and their savings be jointly attainable. With a shared launch team or robot, optimize a feasible schedule under each program. Adding individual opportunities can otherwise claim the same hour twice.

| Economic object | A physical deployment | A digital deployment |
| --- | --- | --- |
| Work the customer accepts | Pack a complete order by cutoff | Resolve an invoice exception by cutoff |
| Evidence to retain | Correction paired with pre-jam sensor readings | Transaction history paired with the verified resolution |
| What can travel | Which calibration test to run on a new fixture | Which reconciliation check to run in a new ledger |
| A binding complement | An operator or test cell before shift end | A qualified reviewer before release |

These are illustrations. Authority changes which actions are feasible after a signal. An integrated firm or a contractual network can supply it. Ownership raises captured value only where actual timing, permissions, incentives or costs differ.

<!-- page -->

## What a working fleet commits the firm to

In November 2024, Universal Robots told owners moving certain arms from a PolyScope 5 controller to PolyScope X that programs and settings had to be recreated and earlier plug-ins could not simply be reused. Its announcement to developers described a period of parallel support for the two platforms. The physical task could still be familiar to a gripper supplier while the implementation needed fresh work. An industry standard can change this margin too. VDA 5050 specifies the exchange of jobs and status between a fleet controller and mobile robots from different manufacturers. The documents establish feasible engineering arrangements. The economic costs, deadlines and customer commitments below are model assumptions. [Universal Robots migration guidance](https://www.universal-robots.com/articles/ur/documentation/upgrading-from-a-polyscope-5-controller-to-a-polyscope-x-controller/) · [Developer announcement](https://forum.universal-robots.com/t/polyscope-x-open-beta-announcement/36988) · [VDA interface specification](https://www.vda.de/en/news/publications/publication/vda-5050)

Two relationships matter. **Where can this experience teach?** A trace from a jam can identify which fresh test to run on a different fixture. **Whose existing work must remain qualified if that test-selection procedure goes into production?** The procedure might run inside a release that also dispatches older arms, or as a separate advisory tool on one cell. Retaining a trace, authorizing its reuse, changing a shared release, and accepting a physical installation are different rights. Competent people and digital agents face the same economic comparison when they have the same information, authority and resources.

Let $I$ be the installed obligations, each defined by an acceptance condition, a supported configuration and a date. Let $H$ be the validation hours available before the next opportunity expires. For a specific discovery, enumerate feasible release plans $a$. A plan specifies who receives the update, which configurations stay on old versions, and all tests, labor, cash and permissions required. Let $W_1(I,H)$ and $W_0(I,H)$ be the best date-one net values with and without the discovered procedure. The second value conditions on reaching this decision without the focal source discovery. Both programs can still learn locally or catch up before expiry. The conditional value of the discovery is

$$R(I,H)=W_1(I,H)-W_0(I,H).$$

The firm can shelve a discovery, so this option is nonnegative when acquiring it adds no obligation. A plan can pool tests, isolate a pilot, migrate customers, buy outside testing, or wait if the opportunity survives. A test shared by three sites occupies its resources once when its result is genuinely reusable. If the sites need independent checks, each consumes time. Holding the beneficiaries fixed, an extra obligation can lower $R$. Duplicating an already covered configuration adds no check in this case. An extra buyer that also benefits from the change can raise $R$.

<!-- page -->

## What release capacity does to the return on inquiry

Consider one prospective use. Conditional on discovery, $g$ is its incremental captured value relative to the best ordinary continuation, before extra release costs. In the first model with a fixed rival and prepaid local diagnostics, $g=Nd(1-p_r)\tau b$. Let $t$ be the additional hours to introduce the new procedure at its target. Updating a common release also requires $L$ hours to cover distinct incumbent obligations. The extra work has variable cost $w$ per hour. The hard limit $H$ and the cost of performing an hour are separate. If those hours are prepaid and would otherwise be idle, set $w=0$.

Let $R_P$ be the best value when the new use shares the existing release. It is the maximum of zero and $g-w(t+L)$ if $t+L\le H$, and zero otherwise. If the firm prepared an independent release path, it also has the option of using $t$ hours and paying $f$ to support a second version. Its value $R_V$ is the maximum of $R_P$ and $g-wt-f$ when $t\le H$. Preparing the option costs $F$ at date zero. The original version can remain available on legacy sites under the independent path. Any still-required common checks belong in $t$ or the separate plan.

Now let ordinary work discover the procedure with probability $s_0$. Investigation effort $e$ between zero and one raises it to $s_0+\gamma e$, with $0\le\gamma\le1-s_0$. Effort costs $\kappa e^2/2$ in current contribution, with $\kappa>0$. In this restriction available hours are independent of the discovery and effort. Write $r=E[R]$, and discount date one by $\beta$. Then

$$\Phi(r)=\max_{0\le e\le1}\left\{\beta(s_0+\gamma e)r-\frac{\kappa e^2}{2}\right\},\qquad e^*(r)=\min\left\{1,\frac{\beta\gamma r}{\kappa}\right\}.$$

**Proposition 4.** Preparing an independent release pays when $F<\Phi(E[R_V])-\Phi(E[R_P])$, holding ordinary service fixed. The first-order condition gives the effort above. Raising the value of a usable discovery raises the return to investigation by $\beta\gamma$ times that change per unit of effort. The firm can rationally change both its architecture and how much it investigates. If ordinary capture improves while the best possible discovery rate stays fixed, $s_0$ rises and $\gamma$ falls. Deliberate investigation can decline even as more useful discoveries arrive.

If discovery arrives at date $u$ before deadline $T$ and the crew has $h$ free hours per time unit, $H=h\max(T-u,0)$. An earlier discovery can cross the common-release threshold in one step. With uncertain arrival, use the joint distribution of discovery, remaining hours and value. Multiplying unconditional averages can misprice faster learning.

<!-- page -->

## Which capability gets investigated?

An arm supplier can improve a diagnostic embedded in the common controller, or a diagnostic that runs entirely on one fixture. A new customer bringing an unfamiliar configuration can alter the ranking of these projects before its robot does any work. This is a prediction about the *direction* of technical progress within a firm.

Suppose two research programs compete for one engineer shift. They produce incremental discovery probabilities $\Delta s_A,\Delta s_B$ over their respective ordinary programs. In this restriction the future service gains are additive in distinct windows, and choosing a source leaves the other program's ordinary yield unchanged. Write $r_A,r_B$ for their conditional release values. At equal shift costs the firm chooses $A$ when $\Delta s_A r_A>\Delta s_B r_B$. If both draws would compete for one release slot, the correct comparison instead uses the jointly optimized portfolio in each state.

**An illustrative restriction.** A shared diagnostic has gain 12, takes one target hour and requires two further hours for each distinct legacy configuration. A local diagnostic has gain 7, takes one hour and leaves the shared release unchanged. Four hours are available at unit cost. Deliberate search adds one-half to the common discovery probability or one-quarter to the local probability. The quantities are illustrative.

| Existing commitments | Value after a common discovery | Value after a local discovery | Preferred use of the shift |
| --- | --- | --- | --- |
| One legacy configuration | 9 | 6 | Common diagnostic |
| Two distinct configurations | 0 | 6 | Local diagnostic |
| Two, with an independent path costing 5 per use | 6 | 6 | Common diagnostic |

The numbers are net of release resources. In the last row, the extra search returns 3 on the common diagnostic and 1.5 on the local one. Treat the independent path as already available in that row. To price it beforehand, take $s_0=1/4$, $\gamma=3/4$, $\kappa=6$ and $\beta=1$ for the common candidate alone. At two configurations it is worth $51/16$ after reoptimizing effort, or $3/2$ if the firm keeps effort at zero. A setup cost of 2 therefore changes both decisions. This second calculation allows continuous effort on one candidate.

A sale can carry a claim on future engineering capacity. At fixed policies let $m$ include a site's direct net contribution and the change in continuation without the focal discovery. Routine source hits are already inside $s$. Its arrival changes discovery probability and conditional release value from $(s,r)$ to $(s',r')$. Its private value is

$$m+\beta\left[(s'-s)r'+s(r'-r)\right].$$

The first term inside brackets values the extra evidence. The second prices what the new commitment does to discoveries the fleet would already make. With endogenous design and inquiry, maximize both complete programs before differencing. A freely disposable additional robot can sit idle. A signed promise to support a new configuration changes the feasible release plans. Only the latter has this potential cost.

<!-- page -->

## How varied should the operating fleet be?

Teaching value and support cost need not attach to the same distinctions. A robot can encounter many objects without changing its release interface. Lin and coauthors varied the environments, objects and demonstrations used to train manipulation policies. On the tasks they studied, additional demonstrations in a fixed set of conditions yielded progressively smaller gains, while broader coverage improved generalization. That result motivates measuring exposure separately from robot-hours. It gives neither a required number of live customer environments nor a cost of supporting them. [Lin et al., manipulation experiments](https://arxiv.org/abs/2410.18647)

To see how diversity itself becomes a choice, suppose that at fixed fleet size and current service margin the firm may support $k$ distinct optional operating environments. A switch can reassign existing capacity among sites. An ordinary common source independently supplies the sought diagnostic with probability $s_0$. Each distinct environment adds an independent chance $u$, where $0<u<1$. Each also adds a separate condition to check if the discovery is released. This one-to-one relation is a restriction on the fleet design. A stable interface or an independent reference cell can break it.

Let $A$ be the gain from a usable discovery after target costs, and $c>0$ the cost of checking each extra environment. On a fixed feasible range $0\le k\le K$ with $A-cK>0$, the firm can meet the deadline. The search budget and technology are held fixed in this comparison. The probability of discovery is $s_k=1-(1-s_0)(1-u)^k$, and the conditional value of a common release is $r_k=A-ck$. Set $V_k=s_k r_k$. The value of one more distinct live environment is exactly

$$V_{k+1}-V_k=(1-s_k)u\,r_{k+1}-s_k c.$$

The first term counts cases revealed only by the additional environment. The second charges its check whenever the firm would already have discovered the procedure. As variety rises, the first term falls and the second rises weakly. Thus the smallest maximizing fleet adds environments while this increment is positive. It can stop while further environments still improve the technical discovery rate.

**Two improvements can move fleet variety in opposite directions.** Raising ordinary discovery $s_0$ reduces the incremental return to every further environment. The chosen number weakly falls. Reducing the cost per additional support condition $c$, holding $A$ and the feasible range fixed, raises those incremental returns. The chosen number weakly rises. A firm can acquire more usable knowledge from routine work and deliberately narrow its future exposure. Improving an interface can instead let it keep more kinds of work in production. If a new environment also earns different service margins, include those. If it consumes no new support, the second term vanishes for that addition.

With correlated environments, replace $(1-s_k)u$ by the probability that the added environment reveals a useful case missed by every existing source. A smaller site exposing a distinct failure can then contribute more than a high-volume site that repeats a familiar one. With complementary pieces of evidence required for discovery, increments need not diminish. Were two sites' records useful only together, pricing either site on its own would miss their joint opportunity.

A field comparison would hold the eligible order mix and machine count fixed across a change in the ordinary archive or in the cost of reusing a validation test. Record which environments the firm elects to support, the rare cases that each supplies, and the tests each requires.

<!-- page -->

## Why the last site matters

Suppose several customers use one legacy configuration. Each can migrate to a supported alternative. As long as one customer remains, the same legacy check is required whenever a common change is released. Migrating the first customer can improve its own operation. Migrating the last one can also free a validation window for an unrelated buyer. The additional benefit comes from eliminating a distinct obligation. If every site instead requires its own additive checks, that particular discontinuity disappears.

Let $B$ be the present value of the shared continuation gain from retiring this final obligation. Calculate it after both regimes choose their best investigation and release paths, including an adapter or outside support if feasible. Exclude the customers' separate migration costs. There are $n\ge2$ customers with net moving costs $c_i>0$ after direct local benefits. Suppose configuration-wide learning and release benefits change only at collective migration. If all migrate, customer $i$ receives share $\alpha_i$ of $B$. Count gains across beneficiaries once. A payment from one participant to another reallocates the gain.

**Proposition 5.** When $B>0$, retiring the configuration is jointly worthwhile if $B>\sum_i c_i$. In a simultaneous, uncoordinated decision, staying put is a strict equilibrium. A lone mover pays and leaves the common obligation in place. Full migration is also an equilibrium precisely when $\alpha_i B\ge c_i$ for every customer. With positive costs, any partial set of movers includes someone who could save money by staying. Thus a jointly valuable transition can fail even when everyone knows the technology and its costs.

A sponsor with a share $\alpha_S$ and authority to sign a binding, all-party migration agreement can offer conditional payments. If it can subsidize but cannot charge other beneficiaries, the smallest total subsidy making full participation individually rational is

$$T_{\min}=\sum_i\max(0,c_i-\alpha_i B).$$

The sponsor can cover it from its gain when $\alpha_S B\ge T_{\min}$ and the required financing is available on the migration dates. A fleet owner, a controller supplier or a buying cooperative can play this role. Ownership matters through the claims, authority and financing it conveys.

**The legacy site may also be a teacher.** If retiring it reduces useful field exposure from $s$ to $s'$ while raising release value from $r$ to $r'$, the fixed-policy gain per opportunity before discounting is $s(r'-r)-(s-s')r'$. It can have either sign. This changes the migration calculation. Removing a production obligation and disposing of the physical machine can be separate choices.

<!-- page -->

## When a robot is worth more off the line

A workcell can supply three things to the firm. It can complete paid orders. It can expose a diagnostic to physical variation that the rest of the fleet rarely encounters. And, while serving a customer under a common release, it can require the operator to keep an older configuration qualified. These services need not be bundled forever. The supplier may be able to end production at that site and retain the machine, fixture, data rights and test protocol.

Compare three feasible uses of the last legacy cell, valued at the same date. In production it provides ordinary net contribution $m_P$ and additional discovery value $\phi_P$. This value already optimizes inquiry and release, including any affordable separate version. Selling or redeploying it elsewhere gives ordinary net value $m_D$ and discovery value $\phi_D$. A dedicated test cell supplies no paid service in this comparison, costs $C_X$ to convert and operate, and gives discovery value $\phi_X$. Use the same time horizon for all three. Incremental discovery values include the benefit of useful routine experience. Avoid counting the sale proceeds as a second cost of keeping the asset.

The firm retains the machine for experimentation precisely when

$$C_X\le \phi_X-\max\{m_P+\phi_P,\ m_D+\phi_D\}.$$

The expression prices a use of capital whose direct paid output is zero. It requires a way to preserve relevant exposure without keeping the production obligation. If the old customer's behavior or final dispositions cannot be reproduced off-line, or the firm loses permission to use the records, reduce $\phi_X$ accordingly. If a simulator, retained archive or rented reference cell supplies equivalent future tests more cheaply, include that in the best alternative to ownership.

**An illustrative allocation.** Continue the four-hour example. Keeping the legacy customer yields one-half in ordinary margin and $19/16$ in optimized discovery value after buying the optional independent path. Removing the last obligation lets the common procedure earn 9 when discovered. Suppose a test cell preserves the original discovery technology. Then effort reaches one, and $\phi_X=9-3=6$. With conversion and operating cost 2, its net value is 4. Selling instead yields 1. If remaining ordinary discovery probability is $1/50$ and investigation can add at most $1/20$, its additional optimized discovery value is about 0.197. The firm chooses the test cell even though it could keep earning on customer work or sell the machine. All three choices use the same executor and prices.

The result has a direct falsification. If retaining the customer leaves exactly the same release options and produces the same useful evidence as the test cell, positive current margin and a positive conversion cost make ordinary operation preferable. Compare the independent cell, replay or simulation, and a matched live source at the same all-in budget. Score which fresh diagnostic each chooses and the accepted work on held-out sites. A physical test facility earns its place here by preserving future inquiry while freeing another group of machines to change.

<!-- page -->

## When deployment histories persist

A single missed customer can represent a timing loss. Persistent differences require a state that survives into the next opportunity. Here that state is the configuration the firm and its customers have undertaken to support. Consider two ways to operate the same installed equipment, legacy $O$ and migrated $M$. Each period brings a fresh class of diagnostic problems with an expiring buyer. A past solution cannot qualify those new jobs on its own.

Let $v_O,v_M$ be the optimized net contributions of one period in the two regimes. Each includes ordinary service, access to informative cases, development effort, and the ability to put what is discovered to work. Sunk setup costs are charged only on transition. Recurrent costs to support a version belong in its flow. Write $d=v_M-v_O$ and let $0<\delta<1$ discount these periods. After delivering its current work, the firm chooses whether to incur a one-time switching cost $C_{OM}$ or $C_{MO}$, both positive, for a change effective next period.

$$V_a=v_a+\max\left\{\delta V_a,\ -C_{ab}+\delta V_b\right\},\qquad a\ne b.$$

**Proposition 6.** With a known permanent environment, an operator on the legacy configuration migrates strictly when $d>(1-\delta)C_{OM}/\delta$. An operator on the migrated configuration returns strictly when $d<-(1-\delta)C_{MO}/\delta$. Between those thresholds each continues in its inherited regime. At a threshold the affected firm is indifferent. To see this, a firm already in the higher-flow regime has no reason to leave. The discounted flow gain from entering it next period is $\delta |d|/(1-\delta)$. Delaying a profitable switch in a stationary environment only postpones its net gain.

Two fleets with the same current demand, hardware and access to the same discovery technology can consequently keep different release arrangements. Where a configuration changes the value of discoveries it can also change their subsequent search effort. A temporary grant or large new order can leave a lasting difference if it pays for migration and the environment afterward lies inside the interval in which both stay put. For a known temporary shock, use its dated gains plus continuation value in the post-shock regime. Applying the permanent-flow threshold to a one-time order would overstate its effect.

This source of persistence has a boundary. If firms can switch freely in both directions, the interval contracts to the point of equal flows. If old evidence accumulates indefinitely or ordinary practice eventually catches up, the period values change over time. The same calculation then requires the remaining path of gains. Durable heterogeneity in the model comes from observable maintenance obligations and costly transition.

<!-- page -->

## Who gets the next deployment?

A firm can be a better discoverer and a less frequent qualified supplier. Let $s_i$ be the probability that firm $i$ discovers the relevant method and $a_i$ its probability of qualifying the new use on time conditional on discovery. For this market, assume qualification requires that method, and take these probabilities after each firm has chosen its feasible search, staffing and release arrangements. Then $q_i=s_i a_i$. With an ordinary chance of qualifying without the method, add that route in each state.

For a newcomer $E$ and incumbent $I$, the newcomer's probability of being the only qualified low-cost supplier minus the incumbent's probability of being the only one is exactly

$$\Pr(E,\neg I)-\Pr(I,\neg E)=q_E-q_I.$$

The common event cancels, even if the two firms' breakthroughs are correlated. Under the equal-cost-saving procurement rule of the first model this ranks expected gross competitive margins. The newcomer leads when $s_Ea_E>s_Ia_I$, which is compatible with $s_I>s_E$. Fixed engineering costs, the size of each firm's current business and the terms of sale determine total profit. The result gives a reason to compare an incumbent's isolated new site with its own older installations before attributing a newcomer's advantage to better AI.

The effect also reaches the marginal product of physical capital. For an added unit at a recipient, let $J_0$ and $J_1$ be its accepted work per period under the old and released methods at given complementary staffing and demand. If this unit does not itself move release probabilities, and $J_0,J_1$ are constant within their states, its expected physical marginal product is $J_0+q(J_1-J_0)$ for probability $q$ of a qualified change at the site. A supplier's decision to isolate an update, or the last buyer's decision to migrate, can raise the return to a different buyer's robot. An observed change in released code is consequential only if the recipient has work, equipment and complementary capacity that can use it.

If the next equipment payment depends on acceptance, a delayed release can also extend the time that cash is tied up. If a fixed balance $c$ remains outstanding for an additional $\Delta T$, the extra financing requirement per start is $c\Delta T$ dollar-periods. This can slow portfolio investment even when the machine's physical productivity at a qualified site is unchanged. The [cross-market model](../learning_and_capital/README.md) counts new capital when another installation becomes profitable, feasible and funded. A conditional release, a sale and a funded installation are separate observations.

Applied across the value chain, the interface supplier may earn for keeping two versions compatible, the field integrator may pay for fresh validation, and a third operator may obtain the next order. The ownership of the source data alone cannot identify the firm that captures or finances this change.

<!-- page -->

## How to test the theory

A field test should distinguish a better executor, a better method for learning, and the competitive return to either. The maintained unit is an original opportunity with a buyer, deadline, and fallback.

### 1  ·  Isolate the return to learning how to qualify

Start source teams with the same execution model, robots, and resource budget. Assign capture procedures across independent sharing groups. Allow ordinary production to continue learning. At unfamiliar target sites, independently vary access to the retained procedure and the number of fresh tests allowed. Keep the starting executor and target opportunities matched. Measure qualification and realized accepted work per dollar, including displaced jobs. Compare the revised procedure with a standing rule, same-budget replay, and a human with equivalent information and authority.

The model predicts no advantage with zero target tests, a positive advantage when scarce checks can be redirected, and equality when all relevant checks are prepaid and feasible. A gain without fresh evidence points toward a directly reusable execution policy. A gain that survives exhaustive checks points toward other channels, including speed, test costs, or execution quality.

### 2  ·  Observe who captures the saving

Record the eligible supplier set, qualification outcomes, costs, accepted volume, and the fee of the winning bid. A change in rival readiness should shift the division between supplier margin and buyer saving for a given technical gain. Compare exclusive and nonexclusive source rights at matched service quality. Independent measurement of transfer helps distinguish productive learning from a bid that protects an existing margin.

### 3  ·  Test where the lead ends

Restore the retained procedure to a random subset of comparison teams before a fresh task and re-optimize both sides. Track how quickly the best alternative learns from ordinary work, purchases a comparable procedure, or qualifies another embodiment. A persistent advantage after those inputs and capabilities have been equalized calls for a different firm-specific resource.

### Intellectual lineage

Learning by doing and learning to learn have a long history. Cohen and Levinthal make research investment build absorptive capacity. Farboodi, Koh and Xia make task-specific data a byproduct of production. Imas, Koh and Legg distinguish competence from coordination in firms. Cabral and Riordan study pricing with learning. The specific claim here links a procedure learned in production to the choice of a fresh, scarce experiment and to the margin it earns against a learning rival. Historical priority and field magnitudes remain open.

**Primary reading**   [Stiglitz (1987)](https://cepr.org/chapters/learning-learn-localized-learning-and-technological-progress)   ·   [Cohen & Levinthal (1989)](https://doi.org/10.2307/2233763)   ·   [Cabral & Riordan (1994)](https://ideas.repec.org/a/ecm/emetrp/v62y1994i5p1115-40.html)   ·   [Data-Driven Automation](https://www.nber.org/papers/w35320)   ·   [Organizing Intelligence](https://arxiv.org/abs/2611.05417)

**Related RoboEcon work**   [The Autonomous Firm](The_Autonomous_Firm.md)   ·   [Choosing the First Deployment](Choosing_the_First_Deployment.md)   ·   [Fleet learning dynamics](https://github.com/amarmurray/robotics-economics/blob/082c8b662af4a41081752f6f23e9b0d6e8ff1ac9/research/recursive_firm/learning_dynamics/README.md)   ·   [Shared-capacity result](https://github.com/amarmurray/robotics-economics/blob/e54a4eb2221249c2417acdc4218589029808f143/research/theory_integration_2026_11_17/data_value/SHARED_CAPACITY_ENVELOPE.md)

<!-- page -->

## A field test of the installed-base mechanism

Follow one new test-selection procedure across a controller supplier, a fleet integrator and buyer sites. Before results arrive, record a fixed list of eligible changes, fresh target jobs, acceptance standards, deadlines and fallback services. For each proposed change, record separately the sites whose traces could teach it, the sites that stand to gain from it, and the still-supported configurations that a common deployment would touch. Include shelving, refused launches and missed opportunities. A sample limited to shipped changes cannot distinguish poor discovery from discoveries the firm chose to leave unused.

**Cross the inquiry decision with the release decision.** Across independently supported groups, vary ordinary versus enhanced case capture and access to a prepared isolated release path versus the best available ordinary path. Hold the initial executor, service standards and resource endowments fixed. Both arms can learn, use existing alternatives and decline a release. Measure discoveries using the same held-out fresh diagnostic before commercial rollout. Then follow accepted service, real validation hours, lost orders, net outside support costs, release date and which party received the saving. A randomized or predetermined sequence of independent pilot capacity can supply variation. Assign at the scale of shared crews and software, or measure the displaced work elsewhere.

With assigned search yields $s_1,s_0$, conditional release values $r_V,r_P$, and additive arm-specific setup or search costs, the model predicts a difference between the effect of better capture with and without isolation equal to

$$\beta(s_1-s_0)(r_V-r_P).$$

This comparison requires that the release architecture leave the upstream discovery yield unchanged *at assigned effort*. If the isolated fleet generates different experiences or engineers change their search choices, the observed interaction also contains those responses. Measure them in a second design that allows reallocation. Feeding the same previously identified candidate into each path isolates the release margin. A local change touching no shared obligation is a negative comparison. A deadline slack enough for both plans removes the timing difference, while avoidable testing costs can remain.

**Test the last-customer prediction.** Compare retiring the final production user of a configuration with removing another unit from a configuration that remains supported. Measure check sets, review hours and acceptance on unrelated jobs before and after. Planned hardware retirements, temporary losses of demand and simultaneous staffing changes can shift both timing and workloads. Track those events and the informative cases that disappear. If obligations actually stay in force after the last production user moves, date the change when support expires. If each unit consumes its own independent validation time, the measured effect should be gradual.

Farrell and Saloner studied how installed bases affect compatibility choices. Henderson and Clark studied why changing the links between components challenges established firms. Here current production jointly selects future evidence and future obligations, and their interaction determines the return to inquiry. The derivations and simulations establish conditional mechanisms. Field magnitudes and their contribution to market shares remain open. [Farrell and Saloner](https://ideas.repec.org/a/aea/aecrev/v76y1986i5p940-55.html) · [Henderson and Clark](https://dash.harvard.edu/entities/publication/3affcf33-4dea-4371-ab4c-4767380018ab)

[Original model checks](replication/capability/check_foundation.py) · [Installed-base replication](replication/capability/installed_base.py) · [Learning before a rival](When_Faster_Learning_Pays.md)

[Full-stack firm extension](FULL_STACK_FIRM.md) · How manufacturing, model development and field integration jointly determine what the fleet can learn from the next machine.
