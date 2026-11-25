# How firms learn what to test

*Recursive Firm Theory · RoboEcon working paper · November 25, 2026*

A robotic milking station records a cow that enters. A farmhand also knows something about a cow that never arrived. Deciding which animals need to be brought in is part of the work. It changes the use of the station, the labor the farm needs, and which animals leave machine records. Researchers studying a commercial dairy could distinguish animals that appeared on a fetch list and were fetched, animals listed but left alone, and animals never listed. A file of completed milkings alone would collapse these histories. [McCalmon et al., commercial dairy study](https://plf.tennessee.edu/wp-content/uploads/sites/229/2024/01/Impact-of-parity-and-days-in-milk-on-fetch-cow-status-in-automated-milking-systems.pdf)

Now consider two operators installing identical equipment at a new site. Both have learned to run the equipment more efficiently. One has also learned which local observation to obtain before changing the operating rule. Its advantage can survive a change of machine even if nothing it learned tells it what action to take at the new site. The new site still has to be tested. What the operator brings with it is a way of spending the first hour.

**A recursive firm can use the work it performs to change how it learns from subsequent work.** Its present operating method determines what it can do. Its method of inquiry determines what the next technician-hour, validation slot or batch of demonstrations can teach it. The two can improve at different rates. Either can deteriorate. The economic question is when it pays to produce and retain the second capacity, how it travels between firms, and how it changes the value of the next machine.

*Data-Driven Automation* starts from a feature of machine learning with implications for economics. Training draws on task-specific data, production creates more of those data, and the data can improve production on other tasks. *Organizing Intelligence* asks which attributes of people and copyable machines change output at a given firm size and which change the return to organizing more agents together. Both make a choice about what must be explained before choosing a parameterization. Our starting choice is to treat the **method by which a firm turns work into evidence** as a possible product of the firm. Whether it actually produces one is an empirical question. [Farboodi, Koh and Xia](https://www.nber.org/papers/w35320) · [Imas, Koh and Legg](https://arxiv.org/abs/2611.05417)

The argument yields a restriction. If one affordable diagnostic is economically best on every job, learning how to choose among diagnostics has no value on that margin. And if different sites already know which checks suit them, a single fleet-wide default can make ordinary specialization look like an organizational discovery. These claims tell us where to look for recursion and when to favor a simpler explanation.

The companion paper asks where to deploy once sites can both generate evidence and earn on its use. It derives when a larger recipient fleet raises the standalone value of two investigative sites while reducing the premium for combining them. [What the next deployment teaches the fleet](deployment_portfolio/README.md)

<!-- page -->

## The economic premises

**Work is delivered at a place, under a standard and by a deadline.** A pick, a meter reading or a database write is a technical outcome. Its economic product depends on the order it helps finish, the labor it releases, the fallback it displaces and the stage that constrains delivery. Capital here supplies services specific to an embodiment, such as an hour of arm time at a workcell. An hour of mobile transport, model inference or qualified human review can be a complement. *When Capabilities Become Production* studies this conversion. Recursive Firm Theory asks how doing that work changes the next conversion. [Companion production and deployment analysis](https://github.com/amarmurray/robotics-economics/blob/e9ba30fcafbe216606e33636bdd91cbf418e1582/papers/How_Deployment_Changes_Robot_Productivity.md)

**Operations select their own evidence.** An attempted grasp reveals one outcome. A parcel routed to a person, an untried grasp and a repeat view of the same failure each carry different information. A digital agent can prevent an exception from reaching the reviewer who would have labeled it. A sensor trace, a retained human correction and a verified result on a new customer order occupy different places in the learning process. Source correlation, rights, delay and the next feasible action determine how much an additional record is worth.

**An execution skill and an inquiry procedure can travel separately.** Write $q$ for the current executor and $m$ for the rule that allocates a finite budget among candidate observations, tests or demonstrations. A procedure can reside in a trained agent, a technician's practice or a routine that several sites use. It becomes a firm-level asset to the extent that the organization can retain and exercise it when people, jobs or machines change. A capable operator can acquire an improved procedure from a supplier. To attribute the improvement to the firm's own production, we need a source history and a credible comparison with how it would otherwise have learned.

A minimal sequence makes these premises operational. The firm chooses a deployment and a route for offered work. That decision and the current executor generate a selected history of attempts, rejections and records. Under its budget and rights, the firm chooses what to inspect. It can use the result to change an action, update $q$, revise $m$, or wait. The next deployment generates a different history. Revising the rule can cost operator time, delay a release or disrupt current jobs. No step guarantees a gain.

There are familiar rivals. Learning by doing can improve execution at a fixed inquiry rule. Research investment can increase the capacity to absorb knowledge. Active learning can make a fixed program extremely good at choosing labels. Our narrower claim concerns **a persistent change in the productivity of a subsequent inquiry, attributable to how earlier production was organized**. Any human team or automated program that already conditions well on the available evidence belongs in the counterfactual. [Arrow, learning by doing](https://doi.org/10.2307/2295952) · [Cohen and Levinthal, R&D and absorptive capacity](https://doi.org/10.2307/2233763) · [Settles, active learning](https://minds.wisc.edu/items/37538f44-36ae-413e-8967-e6c831e17a8e)

<!-- page -->

## When is learning which test to run valuable?

An arriving job has observable context $z$ and a local condition $\theta$ that must be learned. The firm can buy one experiment $e$ from a common finite menu. A no-test alternative can be included. Its result $x$ arrives in time for a feasible action $a$, such as releasing a machine, continuing manually or sending a technician. For one claimant, let $\pi_z(a,\theta)$ denote the contribution of that decision and $c_z(e)$ the incremental cost of obtaining the result. Under a specified joint distribution and common downstream decision rule, the net value of choosing the experiment is

$$
W_z(e)=\mathbb E_{x\mid z,e}\!\left[\max_{a\in A_z(e)}
  \mathbb E[\pi_z(a,\theta)\mid z,e,x]\right]-c_z(e).
$$

Delay can remove an action from $A_z(e)$. A cheap fallback can shrink the gain from diagnosing the fault. Keep the executor, menu, budget and the information available **after** the observation fixed. Compare the best test chosen for each context with the best test the firm commits to across all contexts. Their difference is

$$
R=\mathbb E_z\max_e W_z(e)-\max_e\mathbb E_z W_z(e).
$$

**Proposition.** The opportunity $R$ is nonnegative. It is zero exactly when some single test is optimal almost surely. For two tests $A,B$, put $d_z=W_z(A)-W_z(B)$ and $x_+=\max(x,0)$. Then

$$
R=\min\{\mathbb E[(d_z)_+],\,\mathbb E[(-d_z)_+]\}.
$$

*Proof.* Subtract the value of a best fixed test inside the expectation. Every difference is nonnegative. Its mean vanishes exactly when the chosen fixed test also maximizes value on almost every job. For two tests, write the flexible payoff as $W_z(B)+(d_z)_+$ and the fixed payoff as $\mathbb E W_z(B)+(\mathbb E d_z)_+$. Their difference gives the identity. The two-test expression applies when the two are the relevant alternatives. An additional competitive fallback belongs in the general maximum.

**The side with less total value at stake sets the ceiling.** Suppose the best test differs between two types of jobs. Let $N_A d_A$ and $N_B d_B$ be the total positive stakes favoring each test over a period. With separate test slots per job and comparable units of account, the value of choosing correctly on both types is the smaller of those totals, relative to the best common test. Once type A already determines the default, twice as many A jobs can mean more orders and twice as many logs while leaving the *total* opportunity to improve test selection unchanged. One rare fault can instead dominate the choice if a wrong release is costly enough.

This is a standard decision-theoretic value of conditioning. It provides a ceiling relative to the fixed comparator. A firm must still discover a rule that approaches it, and ordinary operation may already capture most of it. The distinction between the ceiling and what production causally adds is essential. [Blackwell, comparison of experiments](https://doi.org/10.1214/aoms/1177729032)

<!-- page -->

## Where the organization enters

A plant often knows which line, shift and machine generated a case. Let $g$ contain the distinctions the incumbent team already uses and let $z$ refine $g$. Define $B(g)=\mathbb E_g[\max_e\mathbb E(W_z(e)\mid g)]$, $B(z)=\mathbb E_z\max_e W_z(e)$, and $B_0$ as the best common default. Then

$$
B(z)-B_0=[B(g)-B_0]+[B(z)-B(g)].
$$

Both terms are nonnegative because a finer rule can reproduce a coarser one. The first is the value of **existing specialization** if the incumbent implements its group optima. The second is the most a finer selector could still add above that baseline. If every depot has its own stable best check and knows it, pooling the depots can produce a large apparent opportunity even when the second term is zero. If the incumbent falls short of its group optima, measure that shortfall separately. A better manual or a centrally distributed lookup table might close it.

The causal return to the method is different again. Let $m_1$ be the procedure retained from an enhanced source program and $m_0$ the procedure retained from ordinary service. Give both the same fresh jobs and information. The per-job gain is $\mathbb E[W_z(m_1(z))-W_z(m_0(z))]$, averaging over source histories and any randomized test choices. It can be negative after a controller or embodiment changes. To value revision today, sum gains over reachable jobs after the release lag, discount them, and subtract the cost of producing and maintaining the rule. Let both alternatives continue learning. A full decision model treats the two future procedures as separate paths. A mandate revised on every release can lose when the relevant faults change faster than the firm can validate an update. If the recipient never gets a usable action before the next change, accumulated records have no in-window payoff from this diagnostic.

A local team may see the context before a distant model supplier does. Delegation matters when it changes which test or action can happen before the deadline. A supplier and an operator with timely shared evidence, decision rights and identical costs can implement the same policy under separate ownership. Their willingness to fund the test can still differ. The operator may save a shift of recovery labor while a supplier paid per service call loses revenue. Price each party's claim, and remove internal transfers before aggregating the value chain.

The decomposition assumes each target has its own slot or an already allotted budget. A shared validation team changes the action to a *joint assignment* across sites. Apply the same comparison to feasible assignments and to whole-order contribution. Two locally valuable tests may then displace one another. With decentralized authority, local proposals can respond faster to a fault while competitors for the same review slot bear some of the cost. That trade-off can be tested against an equally informed central dispatcher and a standing rule for sharing capacity.

<!-- page -->

## From a learned procedure to the marginal product of capital

Choosing a diagnostic is the smallest version of a broader allocation problem. A digital agent can choose which demonstrations to buy, a training team can allocate a fixed corpus across competing objectives, and a fleet can choose which embodiments share a representation. The slower organizational decision is how much authority and budget each of those choices receives. A learning objective can give more weight to a failure on the critical path to delivery. Its performance can then be scored against later accepted work and real resource use even if the training loss goes down under both objectives.

Here is a restriction that applies across those designs. Write $V_0(K)$ for the discounted contribution of a fleet with capital vector $K$ under its best feasible incumbent learning arrangement. Ordinary operation continues to teach under that arrangement. Let $V_1(K)$ give the comparable contribution with access to a revised arrangement, measured before the one-time adoption cost $F$. Both valuations charge the labor, compute and validation delays they actually incur. Put $D(K)=V_1(K)-V_0(K)$. If the organization can retain the incumbent, its attainable value is $V^*(K)=V_0(K)+[D(K)-F]_+$. For a finite block $h_i$ of embodied capital, the change in its investment value attributable to the option to revise is exactly

$$
\Delta_i V^*(K)-\Delta_i V_0(K)
=[D(K+h_i)-F]_+-[D(K)-F]_+ .
$$

This follows by subtracting fleet value at the two capital stocks. **A better learning organization changes the value of the next robot only insofar as that robot changes what the revision opportunity is worth.** A highly valuable routine that works equally well with either capital stock can raise firm value yet leave this marginal investment unchanged. Conversely, a small retrofit can bring enough eligible jobs within reach before a deadline to make a previously uneconomic procedure worth installing. A hardware fix that removes the diagnostic problem can move the investment value in the opposite direction. A long release lag shortens the sequence of jobs for which the revision can pay. These are directions to measure, conditional on the fallback, demand and the firm's claims. The value difference above is a discounted contribution. The marginal physical product is measured in additional accepted units per unit of robot service.

This suggests three comparisons across types of firms. For an operator without retention rights, vary access to independently audited cases at the recipient. For a model supplier with a fixed corpus, hold that corpus and compute fixed and vary who learns the training weights. For a full-stack operator, compare an upstream retrofit with a shared controller change while charging the same downstream validation time. A federation with matched information and release rights provides a comparison for an ownership explanation. In each case track who can actually revise a rule, the independent jobs reached before it expires, and how the next preferred installation moves. This is how firm typologies can become inputs to a broader theory of heterogeneous automation. [Mixed-fleet allocation](../stack/README.md) · [Economic value of a learning lead](https://github.com/amarmurray/robotics-economics/blob/e9ba30fcafbe216606e33636bdd91cbf418e1582/papers/autonomous_firm/When_Faster_Learning_Pays.md)

<!-- page -->


## What changes across end markets?

**Parcel induction.** In Amazon's Robin workcells a fixed arm transfers a parcel to a mobile unit. A learned score ranks candidate picks for further checks. The system observes the result of the pick it actually attempts. A proposed test of recursion would give a new workcell a choice between inspecting tooling and obtaining a new observation of the parcel, with the grasp policy held fixed. Did a procedure learned on other lines change which investigation the technician performed first, and did more original parcels clear dispatch cutoff per combined arm and recovery hour? Tool maintenance, easier parcels and more recovery labor are credible alternative explanations. [Li et al., physical fleet study](https://roboticsproceedings.org/rss19/p023.pdf)

**Dairy production.** A commercial study followed 528 cows served by eight automatic milking stations and linked farm records to fetch-list decisions. The farm supplies stockperson time and access to the animals. An equipment supplier can observe station events, depending on access. A proposed diagnostic comparison is checking station congestion versus inspecting the pattern of overdue visits. The original roster, including animals that never appear at the machine, makes a different sampling policy testable. Measure milk accepted by the processor and labor used in fetching and supervision alongside station visits. A change in barn layout, available labor or herd composition can alter all three without improving the farm's inquiry procedure. [McCalmon et al.](https://plf.tennessee.edu/wp-content/uploads/sites/229/2024/01/Impact-of-parity-and-days-in-milk-on-fetch-cow-status-in-automated-milking-systems.pdf) · [Wisconsin Extension on voluntary visits](https://dairy.extension.wisc.edu/articles/encouraging-voluntary-visits-in-automatic-milking-systems/)

**Digital service.** In a field study of customer-support workers, access to an AI assistant improved issues resolved per hour on average, with different effects across workers. A separate autonomous service can choose to inspect an account event, request a missing document, or escalate an exception. A corresponding research design would hold the executor and access to tools fixed, copy only the procedure selecting that check into a new queue, and count resolved issues, reopened tickets and reviewer minutes. Worker skill, better software and a shift toward easier tickets can each mimic a learning advantage. The field study documents assisted human work. The autonomous-service comparison is a proposed test. [Brynjolfsson, Li and Raymond](https://doi.org/10.1093/qje/qjae044)

These cases lead to a multivariate marginal product. For robot service at stage $i$ and end-market output $Y_j$, estimate $J_{ji}=\Delta_i Y_j/\Delta K_i$ at a specified feasible production allocation. Also measure the change in real cost and the firm's discounted value when later learning and investment can adjust. A diagnostic may make a machine productive at another site, free a shared reviewer for a third site, or reduce upstream demand for a supplier's input. The production links carry material and work. Learning links carry evidence, conditional on compatibility, permission and timing. They need not run in the same direction. The current network experiment supplies a worked example with simulated firms. [Capital returns across the value chain](../network_mpk/README.md)

<!-- page -->

## What our earlier benchmark examples can establish

The previous network study illustrated task dependence using two digital models and two robot tasks. We returned to the complete published tables to ask a harder question. **How much apparent specialization can a firm obtain simply by selecting among existing execution policies?** These data measure task scores. They supply a control for the recursive explanation.

In the original τ-bench results, with equal weight on retail and airline, choosing the better of GPT-4 Turbo and Claude 3 Opus per domain adds 1.15 percentage points over the better fixed member of that pair. Across all 12 reported configurations, the same model, GPT-4o, leads both domains. Domain-specific selection adds zero at the reported scores. The pairwise ranking reversal remains arithmetically correct. Its implication for allocation depends on the alternatives available and their costs. The benchmark provides scores against a simulated user and a database criterion. [Yao et al., Table 2](https://arxiv.org/html/2406.12045v1)

We repeated the comparison for all four policies, all 17 WidowX tasks and all 12 Google-robot tasks in the OpenVLA evaluation. The source provides physical trials, including partial-credit scoring on some WidowX tasks. The categories are the authors' task families on WidowX and in- versus out-of-distribution on the Google robot. The held-out comparison removes one entire task, selects a policy from the other tasks in its category, and scores it on the omitted task. Its comparator chooses one policy from all other tasks at that embodiment.

| Published robot suite | Best fixed score | Best per-task score in hindsight | Gain from using category on a held-out task |
|---|---:|---:|---:|
| WidowX, 17 tasks | 70.59 | 74.12 | −1.62 pp |
| Google robot, 12 tasks | 85.00 | 90.00 | −3.33 pp |

A reader given all outcomes can find gains from reassigning policies. The tested category rule *lost* to the fixed comparator on unseen tasks in both suites. Each cell has only ten or five trials. Sampling noise, heterogeneous tasks within a category and weak predictors can all explain the result. It neither estimates the value of a new diagnostic nor implies that a better selector is impossible. The published tests report no customer settlements, matched operating costs or randomized source histories. [Kim et al., Tables 4 and 5](https://arxiv.org/html/2406.09246v1) · [Calculations and full results](results.json)

This changes how we read the rest of the branch. The paired fleet experiment demonstrates how improving routing can remove another robot's training cases. The validation and settlement studies show how information, timing and priced audits could change the next release. The network study shows how those changes can revalue capital across sites. Together they generate mechanisms and discriminating tests. Demonstrating that a deployed firm produced a transferable inquiry procedure still requires observing the procedure on a fresh local decision. [Fleet-learning study](../learning_dynamics/README.md) · [Transfer validation](../transfer_validation/README.md) · [Settlement attribution](../settlement_learning/README.md)

<!-- page -->

## The test the theory should face

**At the source, vary how work becomes evidence.** Assign comparable fleets or independent groups of sites to ordinary operation or a program that sets aside a priced reference sample covering both robot-handled work and work routed to people. Both groups keep learning from normal operations. Record all eligible opportunities, including refusals, and the time, labor and compute displaced. Assign treatment at the level at which procedures are shared. Record which tests each team learned to request. Retain a version that another crew can use without copying its execution model or handing it the answer to the target problem.

**At the target, put the inherited procedure in a position to fail.** Use new sites and fresh local conditions. Keep model weights, test budget, deadlines, permissions, signals available before choosing a test, and downstream decision rules alike. Compare the procedures produced by the two source programs. Within each arm, either allow the procedure to select the test or externally assign a common feasible test using the established site-specific rule. Pre-specify the strongest ordinary comparator, including an experienced operator, existing routing software, and a rule fitted on independent historical sites. Price their time equally. Use held-out customers or task families and repeat after a regime change. An independent, authorized reference sample gives a check on the cases that never entered review.

Let $Y$ be accepted target work or real operating contribution per original opportunity, net of target testing costs. Compare the source-program difference with free test choice to the same difference with common assigned tests. Record which check ran, whether its result changed a deployment or maintenance decision, and how much time remained. An improvement under free choice that disappears with assigned tests supports the inquiry-choice channel if teams differ only in the procedure selecting the test. A gain under assigned tests calls for examining improved execution, direct information about the target, or capability in interpreting a given signal. An interaction between these channels requires a further crossed comparison. Better qualification with no additional paid work can still save resources. Count those savings and charge source-program costs once.

**The next open question is which firm sustains the reference sample after a successful release makes failures rare.** A farm can see missing visits a vendor never records. A recovery contractor can see work a digital router removed from the robot's queue. Let each choose how much to audit before pooling evidence, then compare with a jointly funded sample at the same total resources and rights. A persistent advantage for the shared arrangement must survive a comparison to the best existing site rules. If ordinary teams choose the same tests, reach the same decisions and use the same resources on fresh sites, the recursive channel has added no measured value there. That is a result the theory must be able to accommodate.

**Reproduction.** From this directory run **python -m unittest -v** and **python evidence.py** with Python 3. The two CSVs transcribe the published tables. Scores are equally weighted by task within each embodiment or by digital domain. Models tied on training scores share selection probability equally. Selecting the fixed model on one robot suite also selects OpenVLA for the other. These are comparisons of published cells. The task-conditional upper envelope uses observed cells in sample and is subject to winner selection. Compute prices, restrictions on model access and operating outcomes could change a firm's ranking. [Robot cells](robot_scores.csv) · [Digital cells](agent_scores.csv) · [Reanalysis](evidence.py)

