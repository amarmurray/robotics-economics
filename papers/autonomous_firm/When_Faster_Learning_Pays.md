# When Faster Learning Pays

*The Production of Capability, Part II · RoboEcon working paper · November 25, 2026*

**A learning lead is worth the work that comes due while the firm can use it.** Two firms may end up equally capable, yet the one that learned earlier can earn a return for months. They may also spend different amounts and earn exactly the same amount if ordinary operations catch up before the first paying order. A third possibility arises when a lead is visible. A firm can profit by changing its rival’s decision to learn, even if the change reduces the total value the two firms and the buyer create.

The unit we value is a change in a *production program*. A firm assigns a real shift to a paying job, a reusable learning procedure, or extra investigation on an individual job. We compare feasible alternatives that start with the same equipment and execution models. Ordinary work can teach the firm under every alternative. A capability counts at the date it lets the firm deliver an accepted order more cheaply, using the validation capacity and permissions it actually has.

## 1. From a single deployment to a stream of orders

A robot fleet handles service calls at existing installations. A retained diagnostic procedure tells the team which test to run on a new fixture. The test itself must still be performed locally. Or consider a software firm whose digital agents resolve transaction exceptions. Experience with old cases can teach them which reconciliation to run on a new customer’s ledger. In each example we can hold initial execution quality fixed and vary how often paid source work yields the reusable procedure. A human-led team facing the same opportunities, permissions and response times can use the same technology.

Let $u$ be the chance that a single source shift yields the procedure, conditional on still searching. Ordinary work has yield $u_0$ and accelerated learning has yield $u_1$, with $0<u_0<u_1<1$. An initial engineering shift costing $F$ can install a capture protocol that raises discovery yield on subsequent source shifts. Costs are incremental present values of real resources or displaced work. Independent opportunities and retention until the last dated order give the probability of finding the procedure by exposure $t$ as $1-(1-u)^t$.

An ordinary target team qualifies the cheaper method with probability $h$. Holding the execution model and target test budget fixed, a retained procedure adds $g$ to that probability. Thus

$$p_u(t)=h+g[1-(1-u)^t],\qquad 0\le g\le 1-h.$$

For example, if the right diagnostic is one of $K$ equally likely tests, $m$ prepaid tests are available, and the procedure covers a fraction $\tau$ of authorized and compatible targets, then $h=m/K$ and $g=\tau(1-h)$ for $m\ge1$. With zero tests, $g=0$. The first paper derives this from the diagnostic choice. This extension holds the work available to learn from fixed while solving what firms do with it. Source jobs and target orders have reserved capacity, and only source feedback reveals the reusable procedure during the horizon. Each target purchase is counted once.

<!-- page -->

## 2. The value of a lead depends on when work is due

Two suppliers can perform the same accepted job. A qualified supplier saves $d$ on real cost relative to a feasible fallback. In one-shot reverse second-price procurement the sole low-cost supplier earns $d$. If both have low cost, the buyer receives $d$ through the price. Let $w_t$ denote discounted target volume times the saving per order at date $t$. Conditional on date and target type, the two firms’ qualification draws are independent in this section. With a fixed rival qualification path $p_r(t)$, upgrading from ordinary to accelerated learning is worth the following amount **before** paying $F$:

$$G_r=\sum_t w_t\,[p_{u_1}(t)-p_{u_0}(t)]\,[1-p_r(t)].$$

This compares the accelerated program with the firm’s own ordinary learning path. A higher eventual success rate on a benchmark need not imply a larger $G_r$. Orders may be due too early, too late, or where another supplier already qualifies.

**Proposition 1. A fixed future order can make faster learning valuable only at intermediate exposure.** Suppose there is one order pool at a fixed calendar deadline, with discounted savings $D$. Every target is covered, so $g=1-h>0$. Let $a=1-u_0$, $b=1-u_1$ and $c=1-u_r$ for the rival’s fixed program, with $0<c<1$. Both firms get $n$ source opportunities before the deadline. Then

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

<!-- page -->

## 3. When to spend the next engineering shift

Now let the firm choose separately on each source shift. While searching it can do ordinary work or give up $k_t$ in current net contribution to raise that shift’s discovery probability from $u_0$ to $u_1$. It observes its own discovery immediately. Once acquired, the procedure already works, and further investigation cannot improve it. Target orders are dated, the rival follows a fixed path, and the firm observes no signal that changes its forecast of that path. This is an adaptive alternative to committing the full setup cost in advance.

Let $m_t$ be the **undiscounted** incremental margin at date $t$ if the firm knows the procedure by settlement rather than remaining without it. With target value $d_t$ times volume $N_t$, $m_t=N_td_t g[1-p_r(t)]$. Write $B_t$ for the difference in optimized value, before the source shift, between already knowing and still searching. With one-period discount factor $0<\delta\le1$ and $B_{T+1}=0$, define

$$S_t=m_t+\delta B_{t+1}.$$

**Proposition 2.** Buy extra investigation when $(u_1-u_0)S_t>k_t$, skip when it is smaller, and take either action at equality. The exact recursion is

$$B_t=(1-u_0)S_t-\max\{0,(u_1-u_0)S_t-k_t\}.$$

**Proof.** Relative to an unknown firm that gets no discovery this shift, a known firm gets $S_t$. An unknown firm already earns $u_0S_t$ through ordinary operations. Accelerating adds the probability difference times $S_t$ and costs $k_t$. Both alternatives can reoptimize on every later shift. Subtract the best unknown value from the known value to get the recursion.

**Why waiting can be optimal.** Suppose only the final cohort pays, costs and yields are constant, and the rival path is given. Before the deadline $S_t=\delta B_{t+1}\le\delta(1-u_0)S_{t+1}\le S_{t+1}$. Thus, conditional on still searching, the dates on which extra investigation is strictly preferred form a suffix. Early ordinary production has time to reveal the answer. As the deadline approaches, the option to wait expires. Earlier orders can reverse the timing of investment.

For five shifts, $u_0=0.1$, $u_1=0.4$, $k=4$, $\delta=1$, and $m_5=20$, the firm buys extra investigation only on shifts three through five if still searching. Move the same margin of 20 to shift one and it buys only on shift one. In both cases it stops paying for investigation as soon as the procedure is found. This comparison gives a fleet planner a different metric from total hours logged. The planner needs the dated work a discovery could change and the remaining chances that routine service will teach it anyway.

<!-- page -->

## 4. Competition depends on overlap and on the rival’s response

A rival that accelerates on the same task and at the same time reduces the firm’s return to investing there. Index dated, separately serviceable orders by $j$. Write $\Delta p_{ij}$ and $\Delta p_{rj}$ for the gains from each firm’s fixed change in procedure. Under conditional independence, subtracting the two gross returns in Section 2 gives

$$G_{\text{ordinary rival}}-G_{\text{accelerated rival}}=\sum_j w_j\,\Delta p_{ij}\,\Delta p_{rj}.$$

If neither firm sacrifices performance on any order, the overlap is nonnegative. Equal average improvement can create very different incentives to invest. A firm that improves on other sites, embodiments or dates leaves the first firm’s marginal return intact when the gains never meet on an order. With correlated potential outcomes, replace the product of marginal gains by the expected product of the two changes in realized qualification, under a common environment where each program’s own outcomes are invariant to the other’s choice. If one firm changes its investment after observing the other, solve that response explicitly.

**A useful accounting identity.** On a given order let $Y_i,Y_r$ indicate qualification for the cheaper method. The total saving is $w\max(Y_i,Y_r)$. Firm $i$ earns $wY_i(1-Y_r)$. Their difference is exactly $wY_r$ in every outcome. After subtracting the real costs of each firm’s learning, the result for any comparison between programs is

$$\Delta W=\Delta\Pi_i+\Delta A_{-i}.$$

Here $W$ is net joint resource value, $\Pi_i$ is the firm’s net profit, and $A_{-i}$ is what the remaining supplier could save serving the work with its realized capability, less its own investment cost. For fixed rival choices and unchanged rival outcomes and costs, the firm’s unilateral incentive equals the net gain in total value. Differences in the two firms’ investments can therefore economize on duplicate effort. A rival response changes that equality by a measurable amount. $A_{-i}$ uses the rival’s capability in each compared history. A hypothetical monopoly policy would answer a different question.

**Shared resources and more than two suppliers.** Let $H(S)$ be the maximum realized operating surplus attainable with suppliers $S$, the original orders, and a feasible joint schedule. Include the buyer’s fallback, capacity limits and all binding site permissions. Under efficient procurement with Clarke pivot payments, quasilinear preferences and private costs at the bidding stage, the firm’s operating profit equals $H(S)-H(S\setminus\{i\})$. Subtract sunk investments and take expectations to obtain the same identity with $A_{-i}=E[H(S\setminus\{i\})-\sum_{r\ne i}K_r]$. Dispatch is optimized after removing $i$ for this calculation. The remaining suppliers keep their realized technology and sunk investments. This is the standard marginal-contribution property of pivot payments applied to learning. Other pricing rules require their own profit equation. Sales that themselves change later learning require a dynamic allocation and payment model before using this extension.

<!-- page -->

## 5. A firm can profit from learning early even as total value falls

Two firms get one source shift each before a single target cohort worth 100 in potential savings. They have identical technology and costs. On either shift the procedure is discovered with probability 0.2 in ordinary operations or 0.8 with extra investigation costing 10. A supplier with the procedure qualifies for the cheaper target method with certainty. A supplier without it can still qualify with probability 0.5. Target draws are conditionally independent. Both suppliers can always deliver the underlying service. Firm A acts first. Firm B observes whether A acquired the procedure before deciding how to spend its own shift. Neither controls the other’s source work. A truthful public observation of acquisition, or an equally informative certification signal, supplies the timing here.

**B’s best response.** If A has the procedure, B earns zero procurement margin with either method and does ordinary work. If A missed, A qualifies with probability 0.5. Investigating raises B’s own target readiness from 0.6 to 0.9. Its gross return is $100(0.9-0.6)(1-0.5)=15$, enough to pay 10. B investigates only after A misses. This response also maximizes joint value conditional on either observed outcome.

| Outcome with B free to respond | A works normally | A investigates | Change |
| --- | ---: | ---: | ---: |
| A’s profit | 12 | 23 | +11 |
| B’s profit | 28 | 7 | −21 |
| Buyer’s saving | 48 | 57 | +9 |
| Real saving before investigation | 96 | 99 | +3 |
| Cost of investigation, both firms | 8 | 12 | +4 |
| Net joint value | 88 | 87 | −1 |

The success of A’s first shift is a public fact about its method, even though neither firm yet knows the target job’s realized low-cost outcome. Conditional on source success A earns 40 before its own cost, because B takes the ordinary route. Conditional on a miss A earns 5, because B investigates. Buying a 0.6 increase in the probability of success is therefore worth 21 gross and 11 net. The two firms together save only 3 more in production and spend 4 more acquiring procedures. The buyer benefits, the responding supplier loses, and the additional early investigation reduces combined value by 1. The joint optimum lets A work normally and preserves B’s option to investigate after a miss.

The discrepancy has an independent check. B’s expected stand-alone savings less its own realized investment fall from $84-8=76$ to $66-2=64$. The change of $-12$ exactly reconciles A’s $+11$ with the $-1$ net change. The model needs neither exclusive data rights nor a difference in underlying learning ability to produce this effect.

The result persists on an interval. Keep B’s cost at 10 and vary A’s cost $k_A$. Extra early investigation yields $21-k_A$ privately and $9-k_A$ jointly. For $9<k_A<21$ the private decision and the joint optimum differ strictly. Equal costs of 10 put the example inside this interval. If B must commit before it can observe A’s result and its action is held fixed, the difference vanishes for a unilateral change by A.

<!-- page -->

## 6. What would distinguish these mechanisms in a fleet?

**Measure a lead.** Start with matched execution models, hardware, target permissions and validation slots. Assign independent fleets or isolated policy-sharing groups to ordinary service or enhanced evidence capture. Let both update normally. At preassigned source counts, compare qualification and accepted cost on *fresh* targets with the same test budget. Pair this with separately recorded order deadlines. A temporary lead predicts convergence where ordinary operations also learn. A lasting gap on heavily exposed tasks points to a change in eventual capability, transfer coverage or obsolescence and calls for a different transition law.

**Measure the cost of waiting.** Hold the number of source opportunities and the total booked work fixed. Where customer commitments permit, vary when a target becomes eligible to use the procedure, or exploit preassigned commissioning dates with comparable order mix. Track the incremental engineering time teams buy *while still searching*. The terminal case predicts late spending. Moving valuable work forward can move spending forward with it. If source feedback is delayed until a batch closes, the contingent stopping decision is unavailable. Such a deployment belongs in the commitment comparison.

**Measure the competitive response.** In a controlled two-supplier procurement exercise, vary whether the later supplier receives the earlier supplier’s qualification evidence before committing its review budget. Keep source rights, technical opportunity and customer value fixed. Track each firm’s review expense, the winner’s actual cost, both suppliers’ privately recorded fallback offers and the buyer’s price. Measuring only the winning price would miss the distinction in Section 5. Where markets use negotiated pricing, re-estimate how savings divide there. An observed early investment alone cannot identify strategic deterrence.

**Where this fits.** Learning from production and strategic investment have established economic precedents. Here the choice is a procedure that changes what an additional deployment teaches, and its return depends on when that change can be used and how other firms respond. *When Capabilities Become Production* provides the operating test for whether a technical gain serves actual orders. *The Production of Capability* derives a reusable diagnostic from source work. The extension here lets capable rivals learn while deadlines approach, and then lets one of them respond to the other’s realized discovery. The numbers are solved examples. Field magnitudes and the ability to observe a rival’s lead remain empirical questions.

**Research and replication.** The exact Python checks use rational arithmetic. They enumerate small operating policies, source discoveries, target outcomes, and both stages of the public-response game. The benchmark for a different capture technology is an ordinary program that also learns.

- [Founding note](The_Production_of_Capability.pdf) · [Foundation checks](replication/capability/check_foundation.py) · [Dynamic model and checks](replication/capability/learning_deadlines.py)
- [Current production paper](https://github.com/amarmurray/robotics-economics/blob/research/assistant-led-expansion-20261117/research/theory_integration_2026_11_17/data_value/WHEN_CAPABILITIES_COMPACT_DRAFT.md) · [Fleet learning and evidence supply](https://github.com/amarmurray/robotics-economics/blob/research/recursive-firm-theory/research/recursive_firm/learning_dynamics/README.md)
- [Farboodi, Koh and Xia, *Data-Driven Automation*](https://www.nber.org/papers/w35320) · [Cabral and Riordan, *The Learning Curve, Market Dominance, and Predatory Pricing*](https://ideas.repec.org/a/ecm/emetrp/v62y1994i5p1115-40.html)
- [Bulow, Geanakoplos and Klemperer, *Multimarket Oligopoly*](https://www.gsb.stanford.edu/faculty-research/working-papers/multimarket-oligopoly-strategic-substitutes-complements) · [Clarke pivot payments, Cornell lecture notes](https://sidbanerjee.orie.cornell.edu/docs/ORIE6180/files/Scribe_Notes_7.pdf)
