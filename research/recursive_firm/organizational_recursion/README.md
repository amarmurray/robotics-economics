# From recursive self-improvement to the recursive firm

*Recursive Firm Theory · Independent RoboEcon research · November 2026*

An AI researcher can ask whether an agent can improve the procedure that will conduct its next experiment. A robotic firm faces a further choice. It can put the next engineer-hour into that agent, instrument a gripper, send a teleoperator to an unfamiliar site, or finish a customer's order. Which choice it makes determines what evidence, equipment, money and methods will be available to the *next* engineer-hour. **A recursive firm uses its present means of production to change how it will select, produce and deploy its future means of production.** The economic question is when a firm can do that, what doing it displaces, and where the subsequent gains accrue.

## What carries over from RSI?

The recursive self-improvement question predates language models. Good asked what happens when designing machines becomes one of the activities a machine can perform. Modern LLM research makes the distinction between an executor and an improver experimentally accessible. In STOP, a program that calls a language model rewrites the program used to improve other programs. The authors kept the underlying model fixed. In AIDE², accepted changes to an AI research agent become part of the agent used in subsequent research rounds. The authors report gains on held-out technical benchmarks. These are examples of an improvement procedure acting on its own successors. [Good](https://vtechworks.lib.vt.edu/bitstream/handle/10919/89424/TechReport05-3.pdf) · [STOP](https://www.microsoft.com/en-us/research/publication/self-taught-optimizer-stop-recursively-self-improving-code-generation/) · [AIDE²](https://arxiv.org/abs/2609.26457)

For economic production, the natural unit is the organization that can commit scarce resources, retain what was learned and exercise the next decision. It can replace its LLM and preserve a fruitful way of assigning field experiments. It can keep exactly the same LLM and lose that ability when a customer withdraws permission to link interventions to outcomes. Two firms with identical model weights can consequently choose different hardware, serve different markets and learn at different rates. **RFT generalizes the unit of analysis for economic outcomes.** Model or agent RSI is one process inside that theory when the organization allocates resources to it. An AI experiment can still be explained at the agent level when the resource, authority and market environment are fixed.

The firm is an empirical candidate for the “self.” Identify which entity can redirect a resource, which procedure survives a change of people or models, and who can fund its next use. The same LLM can be a tool in one enterprise and, with authority over spending, experiments and release, operate much of another. A firm can direct a loop through a supplier. A supplier can also refuse the decisive revision while a customer alone holds the final outcome. If no individual firm can exercise the complete decision, model the firms and their shared dependency. Knowledge can expand across the economy even when little of its value or evidence returns to its originator.

This builds on learning by doing and on dynamic capabilities, which already give firms a role in developing and reconfiguring productive competence. *Data-Driven Automation* makes task data an endogenous product of activity with spillovers elsewhere. *Organizing Intelligence* distinguishes competence from coordination in a firm composed of heterogeneous agents. Our proposed addition is a priced and testable link from **selected production experience to the procedure governing a later investment in capability**. Calling a successful firm recursive does not identify that link. [Arrow](https://doi.org/10.2307/2295952) · [Teece, Pisano and Shuen](https://ideas.repec.org/a/bla/stratm/v18y1997i7p509-533.html) · [Farboodi, Koh and Xia](https://arxiv.org/abs/2606.10127) · [Imas, Koh and Legg](https://arxiv.org/abs/2611.05417)

## The economic object

Let $x_t$ contain the firm's people, digital agents, model versions, robotic capital by embodiment and vintage, data capital (retained observations, provenance and permitted uses), support commitments, cash and partner options. Let $m_t$ be a reproducible procedure for choosing what to investigate, train, build or qualify. A procedure can reside in an agent, a shared operating practice or an interface between teams. The firm chooses an allocation $u_t$ before all outcomes are known. Its deployment generates accepted work $y_t$, dated cash and a selected history $e_t$. Digital dispatch affects which cases reach an arm, a mobile carrier or human recovery. Retention and audit capacity affect which of those cases can teach anything.

The law of motion is the joint distribution of $(y_t,\mathrm{cash}_t,e_t,x_{t+1},m_{t+1})$ given $(x_t,m_t,u_t)$ and the outside environment. The current procedure $m_t$ helps choose the work and experiments that can produce a successor $m_{t+1}$. That successor changes which attainable investment the organization actually chooses on fresh work. The firm can deliberately change its instrumentation, research allocation or boundary to change this transition. Costs enter when resources are committed. Solvency is checked against dated cash. Private value counts only the claims the firm can exercise. Original orders and real costs determine the corresponding production account.

A firm can also revise the *internal objective* it gives the agents allocating training time. Paying attention to failures per robot-hour can be sensible until an easier admission rule keeps difficult jobs out of the denominator. A team able to trace original orders through recovery can then give greater weight to costly unfinished work. The customer still determines acceptance. A revision earns its cost only if the discounted improvement in decisions before the objective goes stale exceeds the investigation, validation and transition expense, including the value of a release slot used elsewhere. In digital services a release queue and tool permissions can play these roles. In physical services the firm must also qualify an embodiment to perform the resulting work.

Three comparisons keep the object measurable.

| Claim | What changes across comparable histories? | What would establish it? |
|---|---|---|
| Execution improved | A trained model, agent or physical procedure on a fixed task | Performance on held-out jobs, followed separately to acceptance, human fallback and payment |
| Production created an organizational capability | The rule for choosing the next investigation, at matched executor, rights, budget and outside menu | A retained rule changes which costly test is bought and improves net outcomes at a fresh site relative to ordinary local teams |
| The capacity to improve itself changed | What an investigation under that rule leaves for the next generation of investigators | An incremental successor produced in the second cohort changes a third cohort's decisions after crediting direct reuse of the original rule |

A prewritten adaptive policy can account for impressive behavior. Give the incumbent its existing conditional policies, outside tools and ordinary learning. If it can purchase the same signal and implement the same mapping at the same dated cost, that part of the proposed organizational premium is zero. Conversely, producing a transferable diagnostic can have value even if that diagnostic is eventually encoded in simple software. What matters is how the firm obtained it and the choices it makes feasible.

## A better improver for which generation?

A firm can favor a research procedure because it resolves more current problems. Whether it also improves the production of *future* procedures depends on what its successful investigations leave behind. This is a distinction between the productivity of inquiry and the productivity of producing better inquiry.

Consider two feasible research programs, broad and focused. Program $i$ resolves the current defect with probability $p_i$, earning incremental contribution $B$ on success, and costs $k_i$. After resolving a case the firm can spend $c_i$ to qualify a successor procedure. Conditional on that expenditure it obtains a reusable method with probability $e_i$. Its value to the claimant on the next independent opportunity is $S$, discounted one period by $\beta$. Each program can decline the extra expenditure after success. Net value today is

$$
W_i=p_i B-k_i+p_i[\beta e_i S-c_i]_+,\qquad [z]_+=\max(z,0).
$$

The conditional probabilities correspond to different observations. $p_i$ is estimated on all assigned investigations. $e_i$ concerns *new* procedures that qualify on an independent target after an initially successful investigation. A narrow rule may repeatedly solve a familiar defect without distinguishing hypotheses about other defects. A broader rule can sacrifice current resolution probability to obtain a more discriminating matched case. The converse is also possible. These probabilities have to be measured on the programs' chosen work, including failures and the eligibility of follow-on evidence. The restriction holds the target stake fixed across programs. With heterogeneous cases, evaluate the expected qualified stake conditional on the particular success, take the best expenditure decision at that information set, and then average over all assigned cases.

Suppose costs $k$ and $c$ are equal and both programs would qualify their successes. For a focused program 1 and broad program 0,

$$
W_1-W_0=(p_1-p_0)(B-c)+\beta S(p_1e_1-p_0e_0).
$$

**A procedure can increase the success rate of the next investigation and reduce the expected production of a successor.** If $B>c$, $p_1>p_0$ and $p_1e_1<p_0e_0$, the preferred program switches to the broader one when

$$
S>\frac{(p_1-p_0)(B-c)}{\beta(p_0e_0-p_1e_1)}
$$

within the region where both qualification investments pay. Else use the positive parts. This predicts *use* of a program. Access to a costless additional program can always be left idle. Nor does repeated profitable use of a single procedure establish accelerating improvement.

### How the next market feeds back into the present firm

The continuation stake $S$ can be built from the recipient's choice. A site with net value $v$ from adopting the ordinary system can instead wait for zero. A qualified new method raises adoption value by $g$ before a posted use fee $\ell$. It is used if $v+g-\ell>\max(0,v)$. An already viable site may use it with no additional machine. A site with $v<0$ that crosses zero can induce a new installation, conditional on financing and capacity. The source's stake includes its captured fees, net margin on genuinely additional equipment, and the incremental value of evidence returned by the new installation. Charge qualification and access costs once. Cash recovered on an asset is distinct from operating surplus.

In the exact illustration a site that would already operate has $(v,g,\ell)=(3,4,2)$. A second site has $(-2,7,3)$. Both use a qualified method, and only the second buys an additional machine. The source earns five in fees and three in additional equipment margin. If the second site's records stay local, $S=8$. If it can return an otherwise unavailable diagnostic worth 16 to the source with probability one half, $S=16$. Recipient service terms and physical technology are held fixed across these two permissions. The return diagnostic's value excludes adoption and fees already counted.

Set $B=8$, $k=2$, $c=1$ and $\beta=0.95$. The focused program has $(p,e)=(0.8,0.25)$ and the broad program $(0.5,0.8)$. The switch occurs at $S\approx11.05$. With local-only records the focused program leads by 0.58. With the return right the broad program leads by 0.94. Current resolution probability falls from 0.8 to 0.5, while expected induced machines per original research opportunity rise from 0.2 to 0.4. These expectations include the possibility that no method qualifies. In the second regime, scoring the research team solely on today's resolution rate would favor the lower-value choice.

The figures are constructed and prices are fixed. If the records duplicate an existing source, arrive after the next decision, or require more review than they are worth, the return right can leave the ranking unchanged. If a new installation displaces another market's orders or a rival's engineers, carry those signed changes through the production network. The physical marginal product of the machine still requires comparing accepted services with and without the extra machine at a stated labor and capital endowment. [Network marginal products](../network_mpk/README.md) · [Learning and capital across firms](https://github.com/amarmurray/robotics-economics/blob/e27351d38593b2b489fa6f49a752fe5433a1fa6a/papers/learning_and_capital/README.md)

## Can a firm delegate and still inherit what its fleet learns?

The [stack-profile model](../stack_profile/README.md) allowed an OEM, model lab or integrator to reacquire a missing layer between service windows. Relax that timing assumption. After a vintage changes, a representative reference panel can shorten detection time by $u$. A reserved revision slot can shorten implementation and qualification by $v$. For a serial response initially taking $T$ days, let $s=T-t$ be the lead required to save work due on day $t$. On a common job roster, the interaction between the panel and the reservation is positive on work with $\max(u,v)<s\le u+v$ and negative on work with $0<s\le\min(u,v)$. On all other work it is zero. This follows by evaluating the four feasible schedules. Weight the histories by the claimant's incremental contribution over the strongest ordinary fallback.

Now let a matched early case also teach the firm how to choose between two tests on fresh equipment. Its source observation identifies the correct diagnostic convention with accuracy $r\ge1/2$. Across releases the convention flips symmetrically with probability $(1-\kappa)/2$ per release. A uniform initial convention, equal conditional test payoffs and independent source error yield a signed forecast. After $d$ releases the chance that blindly following the source sign points to the right target test is $(1+(2r-1)\kappa^d)/2$. A team that knows the transfer law can invert a systematically reversed signal. An unexpected reversal can instead leave it confidently buying the wrong test. Hardware, execution model and the ordinary local team are held fixed.

For a target test costing $k$ and incremental captured payoff $B_f$ on a correct choice, the ordinary program can decline, buy a test at half chance of success, or use a local specialist with success probability $p_L$ for extra charge $k_L$. Let $U_0=\max(0,B_f/2-k,p_L B_f-k-k_L)$. The gross value of inheriting the rule, under a correctly anticipated law, is

$$
G_d=\left[\frac{B_f}{2}(1+(2r-1)|\kappa|^d)-k-U_0\right]_+ .
$$

One scarce slot can be allocated to one of these target routines. The source sign alone specifies no physical repair at the new site. A fresh diagnostic is needed. If raw source evidence already lets the ordinary specialist make the same choice at the same cost, $G_d=0$.

For a transparent clock, ordinary requalification takes six days. The panel saves two and the reservation saves three. Either alone saves an order due on day four, worth $m$. Only both together save an order due on day two, worth $b$, and make its matched diagnostic available, with retention probability $q$. The two rights have additive costs. Their *total* interaction on current and subsequent work is therefore

$$
I_d=b-m+\beta^d qG_d .
$$

The direct operating interaction can be negative while the total is positive. Delay erodes the inherited method through both discounting and convention drift. A useful right at the source can accordingly lose its private value even as the same physical workload persists. Positive interaction and optimal purchase of both rights have different thresholds. Compare net value with all four programs.

| Constructed scenario | Operating interaction | Total interaction | Best feasible arrangement under the planning assumptions |
|---|---:|---:|---|
| One release to validation | −4 | +0.47 | Panel and reservation |
| Two releases | −4 | −0.86 | Panel and reservation |
| Five releases | −4 | −3.17 | Panel only |
| Recipient keeps all diagnostic records | −4 | −4.00 | Panel only |
| Source captures a quarter of the target payoff | −4 | −3.30 | Panel only |
| Local specialist matches the inherited procedure at the same price | −4 | −4.00 | Panel only |
| Unanticipated reversal after one release | −4 | −11.20 realized | Both chosen in advance. Panel alone earns more under the realized convention and frozen decision rules. |

The baseline uses $m=5,b=1$, respective rights costs two and three, $q=0.8$, $r=0.9$, $\kappa=0.8$, $\beta=0.95$, $B_f=24$, $k=4$, $p_L=0.7$, $k_L=3$. The return right is incremental on top of ordinary learning. The reversal scores the original policy without giving it foreknowledge. If the reversal is anticipated and inversion is feasible, the one-release premium returns. If tooling adds two days to every schedule, the combined rights can save the day-four order but miss the matched case altogether. Observing that both rights rescued an order then supplies no evidence of procedure inheritance.

This exercise prices the ability to detect a change and requalify work under stated restrictions. A partner supplying the same dates, matched cases and revision authority at the same cost can reproduce the result. Learning the source convention is a modest form of organizational memory. The calculation imposes the learning algorithm and the drift law. A finding that a firm invented a better *algorithm for learning* requires the additional intergenerational test below.

## Evidence and the next discriminating test

Digital and physical studies already establish parts of the mechanism. AIDE² Appendix C crosses the starting and improved research-agent code with three underlying language models on two held-out benchmarks. The reported improvements transferred across models. On MLE-Bench the strongest model's two agent scores were within one standard error. This comparison gives the proposed transfer design a technical precedent and illustrates why the incumbent matters. [AIDE², Appendix C and Figure 9](https://arxiv.org/abs/2609.26457)

Physical Intelligence's RECAP used demonstrations, on-policy robot experience and teleoperated corrections. The authors report more than doubled task throughput on diverse laundry folding and espresso when adding on-robot data relative to the reported offline comparison. These were physical robot evaluations. The organizational account requires observing who chose the evidence and training allocation, how it changed the next investigation, and where cash became available for another installation. [RECAP, results and comparison](https://www.pi.website/download/pistar06.pdf)

**A three-cohort transfer test.** Independently assign source production histories. At a fresh recipient, cross passage of an improved model or agent with passage of the organization's procedure for choosing its next costly investigation. Preserve the same rights, ordinary staff, baseline upgrades, available tests and priced resources. Permit an ordinary team to learn from the same raw records in a separate arm. Record whether the inherited procedure changes the actual test, subsequent accepted work, human recovery or net cost with the executor fixed. If assigning both teams the same tests removes the advantage, test selection is a plausible channel. A gain under common tests points to another mechanism.

At a **third** independent cohort, let both recipients retain whatever first-generation method they were assigned, and randomize whether they may pass on the *incremental* procedure produced in the second cohort. Compare the effect of passing it on across the two original histories. Charge the cost of producing and validating successors. Preserve the independently assigned reference roster and measure linked dates. This interaction distinguishes the value of producing a successor from merely reusing the first improvement on another customer. A residual difference needs checks for direct answers embedded in the carried material, better hardware, extra budget, intake selection and ordinary local specialization. For ambiguous carrier boundaries, specify in advance which model weights, agent code, organizational memory and decision rights each arm receives.

The timing of that permission identifies two different margins. Draw the transfer assignment after the second cohort finishes, under a common announced chance of passage, to measure what the successor transmits given common incentives to produce it. Randomize announced permission before that cohort starts to measure how the prospect of reuse changes what investigators choose to produce. Include every originally assigned case, including failed investigations, abandoned installations and cohorts that produce no transferable procedure. Otherwise a change in who survives to validation can masquerade as an improvement in the firm's capacity to learn.

### Where the broader roadmap stands

| Economic question | What has been established | What still discriminates between explanations |
|---|---|---|
| What is the recursive object? | A common state and transition, distinct carriers of improvements, and a successor-value restriction. | Matched model-only, procedure-only and joint transfer. Demonstrate reuse, then successor production on a third cohort. |
| What creates useful evidence? | [Exposure and fleet learning](../learning_dynamics/README.md) and [shared-hour reallocation](https://github.com/amarmurray/robotics-economics/blob/e27351d38593b2b489fa6f49a752fe5433a1fa6a/papers/theory_week_20261125/EVIDENCE_REALLOCATION.md) give signed conditions. Published robot curves discipline breadth claims. | Measure original jobs before routing and the opportunity cost of review. Better execution can reduce recipient evidence. |
| Which organization can act in time? | [Stack minima](../stack_profile/README.md) cover eight ownership origins. The dated re-entry result here prices detection, action and survival of the inherited method. | Vary a retained reference panel and a reserved slot independently. Include well-equipped partners and precommitted late audits. Earlier [standing coverage](../reference_coverage/README.md) sometimes favored the fixed schedule. |
| Where do capital and subsequent learning go? | [Network MPK](../network_mpk/README.md) separates accepted physical services and captured returns. Here a recipient's entry and return rights change the originating firm's choice of research. | Track original orders, displaced labor, new machine service and who actually finances it. Rival capacity, prices, multiple vintages and a joint distribution of measured firm returns remain open. |

The next pilot comparison is whether a carried procedure beats the best ordinary team **after matching its information**, and whether a later recipient panel detects a changed sign before the rule is used. Report the strongest conflicting results at the November 27 seven-session checkpoint. The theory-week integration runs through December 2. The analytical results and synthetic panels are available now. A field estimate of firm-level recursive improvement remains outstanding.

**Reproduction.** Run **python3 reentry.py** in this directory. The script enumerates the timing and convention histories, checks the program rankings, and evaluates four conditions on 64 independently seeded synthetic panels of 600 cohorts each. The resulting sampling variation is conditional on the specified laws. [Code](reentry.py) · [Exact results and synthetic panels](results.json)
