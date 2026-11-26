# One firm, one economic account: integrating deployment, learning and recursive improvement

*Formal integration manuscript · finite economy edition · November 2026*

## What has been integrated

A robot operator can earn from current service, retain evidence from that work, train a reusable model, alter its research procedure, build a different embodiment, acquire a diagnostic reference, contract for research, or change its internal scope. These activities compete for the same dated resources. Their returns depend on the production and investment choices they make possible later.

This paper gives those choices one economic environment. The accompanying solver optimizes the complete contingent policy of a finite firm. A second solver places two such firms in common final markets and solves a two-period competitive restriction. The terminal value of evidence, models and research procedures is zero: their private value must be earned through subsequent choices inside the model. No separate “learning premium” is inserted into revenue.

This is a solved integrated **restricted** model. It does not establish unrestricted general equilibrium, sustained recursive growth, the economics of actual LLM deployments, or an empirical calibration. The finite firm has two markets, two possible robot types, two qualified model upgrades, two procedure upgrades, one common latent transfer regime, and a short horizon. A staged [recipient-cohort restriction](SUCCESSOR_PROCEDURES.md) derives the value of many distinct target improvements from the same production recipes and solves two generations of procedure development. Its prefunding and independent-market assumptions are explicit. The general notation below explains how to enlarge the concurrent economy; notation alone is not a solution of that enlargement.

The source branches remain separately preserved. Inputs are main at `f5eaf0d549a8682923026358a02d45fe0e5de8f5`, production at `8dba84f45e18fe5896e75cd9a98539e4b87a83fb`, and recursive-firm at `af1cabb95772524db1b34dda3b2667a54c203b43`. This edition closes a common decision account; it does not relabel every earlier result as a theorem of this small numerical economy.

## 1. What the earlier models contribute

The most important integration task is to specify which quantities are outputs of the joint model. A continuation stake, a transfer probability, a market price and a funding limit cannot all be treated as determined elsewhere while claiming to have solved their interaction.

| Source mechanism | Common economic object | Restriction needed for recovery | Status in the finite implementation |
| --- | --- | --- | --- |
| Qualified production and economic emulation | Feasible accepted-service recipes and lawful contingent policies | Fix the learning state, rights and hardware; solve the operating problem | Explicit human, arm, mobile and digital recipes; old versions remain available |
| Full-stack manufacturing, models and deployment | Joint investment, production and research action | Expand the hardware/design menu and retain the source's timing and customer participation conditions | Two embodiments and paid construction are implemented; continuous design and three-vintage customer contracts remain source results |
| Learning and capital propagation | State-dependent operating margins, transition effects and investment responses | Differentiate the common solved program in a region with unchanged policy and active constraints | Finite changes are computed; the derivative identity is proved separately |
| Evidence reallocation | Production-dependent observation law and shared support capacity | Hold representation fixed; permit source effort and recipients to share a scarce input | Accepted service, case retention, training and manufacture share labor, compute and cash |
| Generalization structure | Belief over a transfer model, diagnostic experiments and qualified transfer | Restore the source graph and its joint likelihood; a scalar belief suffices only for a restricted hypothesis family | One latent binary regime, cross-domain qualification reports and imperfect/exact audits |
| Organizational recursion | Retained procedure as an input to producing its successor | Hold the executor fixed when identifying the procedure's causal contribution | Procedure 0 can produce 1; retained procedure 1 changes the chance of producing 2 |
| Economic RL and digital organization | A legal information state, joint action, externally earned payoff and learning algorithm | Match observations, costs and feasible contingent ordinary policies | An exact planning benchmark and reward accounting are supplied; no new learned policy is claimed |

The framework can nest the older Gaussian design model or the graph model by replacing the state and transition kernel. The two-domain computation does not numerically recover a graph with overlapping cycles, continuous Gaussian design, or customer bargaining. Those remain distinct, solved restrictions with explicit connections. A valid synthesis preserves that distinction.

The newest Economic RL source is particularly useful discipline. Its product-conditioned learned rule and ordinary dynamic rule fitted to the same records tie in the training family; both can fail after an unannounced transfer reversal. The inherited result supplies no intrinsic premium for the RL implementation. The present core asks which information, resources and decisions a capable implementation should use.

## 2. Common state, timing and objective

### State

Write the inherited state as

\[
s_t=(K_t,M_t,D_t,\psi_t,R_t,g_t,B_t,z_t,b_t).
\]

The coordinates have different units and meanings.

| Coordinate | Meaning | Accumulation or use |
| --- | --- | --- |
| \(K\) | Installed, qualified physical capacity by embodiment/site and diagnostic equipment | Built, installed, retained, possibly retired |
| \(M\) | Retained qualified execution models and reusable digital workflows | Trained and validated; old qualified versions are retained |
| \(D\) | Usable evidence and its provenance | Generated, acquired and retained subject to rights |
| \(\psi\) | A retained procedure for producing and qualifying later improvements | Produced using the inherited procedure and scarce research inputs |
| \(R\) | Access, retention, transfer, action and commercial rights | Separate from ownership and physical possession |
| \(g\) | Maintained internal scope and available contracting relationships | Changed at a cost and with a stated delay |
| \(B\) | Cash available before commitments | Customer collections arrive after current outlays |
| \(z\) | Observed demand and other public conditions | Exogenous shock in the current restriction |
| \(b\) | Belief over unknown features of technology | Updated from legally observed outcomes |

An installed robot and one robot-hour are different quantities. A retained model and a running inference instance are different quantities. Evidence that supports a possible update and a qualified update are also different quantities. Combining them in a single “AI capital” scalar would suppress the decisions being studied.

### Within-period order

At the start of a period, the firm observes its inherited state and chooses production, model versions, inference instances, retention, one research activity, one construction activity and next-period lab scope. It pays all current outlays from inherited cash. It then operates and conducts research. Customer receipts, research qualification outcomes and retained cases arrive at the end of the period. New equipment, models, procedures and scope are available next period. The next demand state is then observed.

Research uses inherited evidence. Cases generated during the current period cannot be used for an earlier decision in that same period. An audit and a training decision cannot be secretly sequenced within the benchmark's single research slot. Enlarging that within-period sequence would change the feasible program and must be solved explicitly.

### One resource account

For a general vector of resources \(u\),

\[
A^Y(s)y+A^L(s)\ell+A^K(s)i+A^\psi(s)e+A^R(s)r\leq \bar u(s).
\]

Here \(y\) denotes service recipes, \(\ell\) training, \(i\) hardware investment, \(e\) procedure development and \(r\) diagnostic/rights activities. Resource coefficients can depend on the inherited qualified stack. Vector resources permit engineers, operators, validators, factory hours and compute to have separate constraints. The small computation uses a shared human crew and one compute pool; it does not assert that all real human skills are interchangeable.

Let \(C(s,a)\) be the total outlay before receipts and \(\mathcal R(s,a,\omega)\) customer receipts. Then

\[
C(s,a)\leq B,\qquad
B'=B-C(s,a)+\mathcal R(s,a,\omega)-d,
\]

where \(d\) is a dividend paid after receipts. Labor, inference, provider fees, parts, retention and scope changes appear once in \(C\). Internal credits do not create external receipts.

A general finite-horizon firm solves

\[
V_h(s)=
\max_{a\in\mathcal A(s)}
\mathbb E\left[
 \max_{0\leq d\leq B-C+\mathcal R}
 \{d+\beta V_{h-1}(s'(a,\omega,d))\}
\right],
\quad
V_0(s)=B+\mathcal S(K).
\]

The computational restriction sets \(\beta=1\), has no borrowing, pays no intermediate dividends and liquidates at the terminal date. Retaining cash is weakly optimal because it can be left unused, carries no holding cost and does not create a new obligation. For every feasible history,

\[
B_T-B_0=\sum_{t<T}(\mathcal R_t-C_t).
\]

Thus maximizing terminal cash plus equipment salvage is equivalent to maximizing total external net cash plus that salvage. Initial cash is an endowment, not profit. Salvage of initially endowed equipment is reported separately from newly generated cash.

With finite menus, finite outcomes and a finite horizon, backward induction determines the optimal value and an optimal nonanticipating policy. The reachable cash and posterior states are finite even though the abstract state variables need not be globally bounded. This elementary existence argument is not a novelty claim.

## 3. The implemented economy

All numbers below are synthetic accounting units. Money is recorded in half-unit ticks for integer bookkeeping; a tick is not an estimated dollar cost. Compute units are standardized workload units, not raw tokens counted across incomparable model configurations.

### Accepted final service and demand

There are physical and digital end markets. Quantities are \(q_P,q_D\in\{0,1,2\}\). In the single-firm restriction,

\[
p_m(q_m,z)=a_m(z)-2q_m,
\]

with \((a_P,a_D)=(14,8)\) in demand state 0 and \((10,12)\) in state 1. The state persists with probability \(0.75\). The firm chooses the quantity and hence its implied price. There is no unmodeled rationing of committed output.

A qualified complete-service recipe includes necessary human recovery. Its accepted output is deterministic conditional on the chosen recipe and reserved inputs. Diagnostic incidents can still occur and yield usable cases. This convention keeps incomplete attempts out of the revenue account. It is an abstraction from actual service reliability, not a claim that real robots have deterministic output.

Let \(r_A,r_B,r_D\) be arm jobs, mobile jobs and digital-agent jobs. They obey \(r_A\leq K_A\), \(r_B\leq K_B\), \(r_A+r_B\leq q_P\), and \(r_D\leq q_D\). The firm can choose any previously qualified physical/digital model version \(v_P\leq M_P\), \(v_D\leq M_D\).

The human requirement is

\[
h_Y=
3(q_P-r_A-r_B)+2(q_D-r_D)
+r_A(2-v_P)_+
+r_B(1-v_P)_+
+r_D(1-v_D)_+.
\]

This gives an explicit human-only comparator and human recovery alongside automated execution. The mobile platform uses a different qualified recipe from the arm.

### Digital stocks and running instances

Running copies are the smallest number supporting the selected automated jobs:

\[
n=\left\lceil
\frac{r_A+r_B+r_D}{1+\mathbf1\{v_D=2\}}
\right\rceil.
\]

Compute use is

\[
c_Y=n+\kappa\frac{n(n-1)}2
+(r_A+r_B)[1+\mathbf1\{v_P=0\}]
+r_D[1+\mathbf1\{v_D=0\}],
\]

where \(\kappa=1\) in the baseline. A retained digital model can improve the service supplied by a running instance. Instances themselves consume compute, and coordination consumes additional compute. Additional idle copies are dominated under this technology; they are not treated as additional productive capital.

The baseline pools are four human units and seven compute units per period, priced at two and one ticks respectively. They are capacity constraints as well as paid inputs. Training, procedure production and construction compete with service for these same pools.

The benchmark does not equate a token with a human hour. An empirical version must declare model, hardware, context, tool use, verification and acceptance conditions before mapping inference consumption into a comparable service unit.

### Ordinary production generates selected evidence

The firm can pay to retain the first usable case family in a domain when it does not already own that family. Conditional on the selected production recipes,

\[
\Pr(\text{physical case})=
1-(1-\eta(v_P))^{r_A}
  (1-\eta(v_P)/2)^{r_B}
  0.85^{q_P-r_A-r_B},
\qquad
\eta(v)=0.75-0.25v.
\]

For digital work,

\[
\Pr(\text{digital case})=
1-(1-\eta(v_D))^{r_D}0.85^{q_D-r_D}.
\]

Both human and automated work can generate evidence. A more capable controller can reduce diagnostic incidents. The mobile recipe is more efficient in human use but less incident-rich in this assumed environment. These differences make production composition relevant to learning without assuming “more deployment means proportionately more information.”

Each domain archive is a retained bit denoting one usable family. Duplicate incidents do not multiply the stock. Repeated research attempts use that archive with fresh algorithmic and qualification randomness; they are not treated as independent new copies of the same empirical observation. Archives are nonrival after acquisition. The baseline retention fee is one tick per chosen domain; a rights mask can prohibit retention. Ownership of the lab does not automatically convey reuse rights.

### Transfer, inquiry and qualified training

A latent regime \(H\in\{0,1\}\) describes whether cross-domain transfer is strong. The initial probability is \(0.6\). A training attempt using an inherited source archive and procedure version \(m\leq\psi\) succeeds with probability

\[
\Pr(\text{qualified target increment}\mid H,m)=
\begin{cases}
(2+m)/4,&\text{own-domain training},\\
(2+m)/4,&\text{cross-domain training and }H=1,\\
1/4,&\text{cross-domain training and }H=0.
\end{cases}
\]

Success increments the target's qualified model by one, up to level two. Failure retains every older qualified model. Cross-domain qualification reports update the belief over \(H\). For example, procedure-0 cross training has ex ante success probability \(0.4\); success raises the posterior probability of \(H=1\) to \(0.75\), while failure lowers it to \(0.5\).

At the model cap, the same cross-domain diagnostic can still be run as a probe. Otherwise a free model upgrade could perversely remove an information-generating experiment. This retained-option detail matters for valid monotonicity claims.

A standalone imperfect audit has report accuracy \(0.75\). A retained reference apparatus makes that audit exact in this restricted hypothesis family. The firm can also buy an exact external audit directly. Thus owning a reference apparatus is useful only relative to the best paid alternative and the remaining horizon.

Baseline internal training uses one human unit and two compute units. Contracted training uses one internal coordination unit and a five-tick provider bundle, with no additional internal compute charge. Provider inputs are embodied in that fee. The contract gives the same stated training channel; no intrinsic ownership advantage is assumed.

### Procedure production: the recursive coordinate

If a usable archive exists and \(\psi<2\), the firm may develop a successor. Using procedure version \(m\leq\psi\), qualification succeeds with probability

\[
\rho(m,D)=\frac14+\frac m4+
\frac14\mathbf1\{D_P=D_D=1\}.
\]

Success changes \(\psi\) to \(\psi+1\); failure preserves the old procedure. Procedure 1 can therefore help produce procedure 2, which changes subsequent training yields. This is a literal second-generation transition. It is distinct from simply reusing the same executor at another site.

Internal procedure development uses one human and three compute units in the baseline. Outside procedure research costs a six-tick provider bundle plus one coordination unit. A guaranteed qualified procedure license is available at ten ticks plus coordination. Old procedures and ordinary contingent planning remain alternatives.

The recursion is economically closed because the value of a successor is

\[
\mathbb E[V_{h-1}(s'\text{ with successor})-
           V_{h-1}(s'\text{ without successor})],
\]

evaluated in the same production-and-investment program. No free-standing fleet stake \(S\) is assigned. An envelope derivative or discrete difference can later reveal how recipient scale changes that value.

The competitive comparisons also solve a stated automated-research technology with zero human coordination and positive compute/provider costs, matched to a reviewed-research economy on initial cash and archives. These comparisons do not estimate or validate that technology. The successor-procedure study retains baseline human requirements and paid verification, and enlarges the set of distinct recipient tasks instead.

### Hardware and internal scope

The firm can build an absent arm, mobile platform or diagnostic reference. Baseline parts cost six, eight and three ticks. Each requires one human unit; robots also require one compute unit. New equipment enters next period. At most one of each robot type and one reference can be owned in this finite economy.

Maintained internal lab scope costs one tick per active period. Entry costs four and operating exit costs one, with the scope change taking effect next period. The current lab determines the current internal research menu. A firm can instead cease all current activity and close its lab without a shutdown payment. This shutdown option is available to rich and poor firms alike, avoiding a spurious benefit from insolvency.

Equipment has terminal salvage of one tick for an arm, two for a mobile platform and one for a reference. These are below the corresponding construction costs including labor, so terminal construction is dominated. Terminal evidence, models and procedures have no salvage. Final-period investment and research are therefore omitted by a justified dominance restriction, rather than by an arbitrary end-of-horizon rule.

## 4. What the solution means

The policy is a mapping from every reachable public state and remaining horizon to a complete feasible action. It is not an open-loop investment schedule, a rule based only on current output, or a policy granted knowledge of the latent regime. Backward induction enumerates all retained feasible actions and all outcome branches. It collapses actions only when their complete next-state distributions are identical.

[Computed results](RESULTS.md) report endowment, cash generation, salvage, first decisions and expected operating paths separately. [Independent verification](verify.py) reconstructs the resource ledger and conditional latent-world transitions without calling the solver's transition function. It checks the resulting beliefs, terminal wealth and reward accounting.

Three interpretation rules are essential.

First, a menu containing research and integration need not select them. A short remaining horizon or expensive internal support can make present service and external contracting preferable. A null investment decision is an economic result.

Second, increasing a resource endowment need not increase every activity that uses it. Additional cash can enable a different service/scope combination and reduce optimal research. The value of the enlarged opportunity set still rises.

Third, capability improvement can alter demand served, labor, compute, evidence, scope and the future investment menu together. Reporting only a change in a model's success rate omits the economic response. Conversely, a private value increase need not imply an increase in every market's physical output.

## 5. Three different marginal objects

For a typed increment \(\Delta K_i\), specified operating policy \(\pi\), accepted final service \(Y_m\), and common external shocks, define

\[
J^\pi_{mi}(s;\Delta)=
\frac{\mathbb E[Y_m(s\oplus\Delta K_i,\pi)-Y_m(s,\pi)]}{\Delta}.
\]

This is a physical response matrix. Its columns are typed capacity increments; its rows are different accepted end-market services. The units do not become comparable merely because all services involve robots. Holding the action fixed, allowing a fixed contingent rule to respond, and fully reoptimizing are different interventions and must be named.

The private capital value is instead

\[
q^f_i(s;\Delta)=
\frac{V^f(s\oplus\Delta K_i)-V^f(s)}{\Delta}.
\]

It contains current margins, saved inputs, information, subsequent investment and the claimant's proceeds. Acquisition costs must then be compared on the same dated basis. With an endogenous price, marginal revenue and price differ. With a resource bottleneck, physical capacity can have little current product but still alter a future research opportunity.

For cash, the finite difference includes the dollar or tick itself. Under the benchmark's accounting, \(V(B+1)-V(B)-1\) is the incremental **liquidity premium**. Calling \(V(B+1)-V(B)\) a return on investing one tick would count recovered principal as a benefit.

Finally, social surplus also includes customer surplus and effects on other firms and claimants. A private demand shift or displaced rival is not automatically additional social output. The present competitive extension keeps input prices and the number of firms fixed; it is a product-market partial-equilibrium closure.

## 6. Economic RL, information and local/global reasoning

The exact solver defines the benchmark an economic learning agent should approximate. Its observation is the legally available state and belief, its action is a feasible joint allocation, and its reward is externally earned net cash with the stated terminal adjustment. Giving an agent the true latent regime would change the information problem.

A forecast of \(J^\pi\) can be an input to that policy. It should not universally be the reward. Qualifying a cheap substitute can complete more orders while reducing the marginal product of an additional robot. Paying a controller for keeping robot scarcity high could therefore penalize an economically valuable improvement.

For an arbitrary potential \(\Phi_t(s)\), a shaped reward

\[
r'_t=r_t+\beta\Phi_{t+1}(s_{t+1})-\Phi_t(s_t)
\]

preserves the policy ranking when the terminal payoff is reduced by \(\Phi_T\). The added terms telescope to an initial constant. Omitting the terminal adjustment creates an incentive to accumulate the proxy. This is an application of established potential-based reward shaping, not a new RL theorem; see Ng, Harada and Russell (1999), [author's account](https://wordpress.andrewng.org/index.php/publication/policy-invariance-under-reward-transformations-theory-and-application-to-reward-shaping/) and [original paper](https://people.eecs.berkeley.edu/~pabbeel/cs287-fa09/readings/NgHaradaRussell-shaping-ICML1999.pdf).

In a stationary discounted fixed-policy restriction, local sensitivity obeys

\[
D_\theta V_\pi=
(I-\beta P_\pi)^{-1}
[D_\theta r_\pi+\beta(D_\theta P_\pi)V_\pi].
\]

The direct operating effect and the changed transition law both matter. The inverse propagates the change through future visits. It is not a proof that a deployment feedback coefficient exceeds one: \(\beta P_\pi\) is a discounted Markov transition matrix.

Within a region where the same policy is uniquely optimal and feasible, this identity also describes the optimum locally. At a cash threshold, a discrete hardware choice, a rights boundary or a policy tie, use finite program comparisons. The exact global decomposition is

\[
V_1-V_0=
[J_1(\pi_0)-J_0(\pi_0)]
+[V_1-J_1(\pi_0)],
\]

provided the old policy \(\pi_0\) remains feasible in environment 1. The first term is the effect under the old policy; the second is the gain from reoptimization. The second is nonnegative. If the policy is no longer feasible, the comparison requires an explicitly repaired policy.

This gives a disciplined local/global connection. Physical marginal changes, resource prices and information effects are local ingredients. Changed allocation, endogenous scope, new research sequences and competing firms' responses are global parts of the solved program. A local derivative cannot be carried across those regime changes without checking them.

Detailed statements and proofs appear in [PROPOSITIONS.md](PROPOSITIONS.md).

## 7. Competition, calibration and the remaining obligations

### Competitive closure

Two firms use the same individual production, research and cash constraints. They choose first-period service and investment simultaneously. Each market clears at

\[
p_m=a_m(z)-2(q_{1m}+q_{2m}).
\]

Their qualification outcomes are independent **conditional on** the common latent regime, not independent after integrating over it. Public reports and public states support a public-state equilibrium restriction. Ownership and raw-data rights remain separate; public information about transfer is not permission to copy another firm's model.

At the terminal date, the quantity game has an exact potential. All pure equilibria are enumerated. The solver uses a disclosed continuation selection among them and then enumerates first-period best responses taking those continuations into account. The published parameter cases have pure first-period equilibria. Generic finite stochastic games need mixed strategies, and this code does not claim a general pure-equilibrium theorem. The standard finite-horizon mixed-strategy existence argument proceeds by backward induction over finite stage games; [Daskalakis and Farina's notes](https://www.mit.edu/~6.7980/stochastic_games.html) state the relevant distinction.

Evidence, beliefs and uncommercialized procedures have no value after the terminal period in this restriction, so they can be integrated out of terminal strategic choices. That compression is exact for two periods. It would be invalid in a longer competitive model, where a rival's discovery changes later inquiry and investment.

The resulting solution closes product-market response and first-period investment incentives for two periods. It does not yet combine many generations of recursive procedure improvement with strategic learning, entry, endogenous input supply and private information. Those are explicit remaining integration tasks.

### Calibration is not a single interpretability score

Three concepts must be separated.

**Observation informativeness** concerns what a deployment's lawful observations reveal about a decision-relevant latent feature. Represent it by a channel \(P(o\mid\theta,a,j)\), where \(j\) identifies the deployment/task context. Under a binary symmetric restriction a scalar accuracy can summarize the channel. In general it is a matrix or experiment, with different precision about different mechanisms.

**Predictive calibration** concerns whether stated probabilities agree with realized conditional frequencies. A model can be calibrated while uninformative: always reporting the base rate can satisfy a calibration condition. A sharp signal can also be miscalibrated when its reliability is misunderstood. The usual confidence-calibration definition is discussed by Guo et al. (2017), [original proceedings paper](https://proceedings.mlr.press/v70/guo17a.html). Conditional calibration by deployment type matters; aggregate agreement can conceal opposed errors across markets.

**Empirical calibration of this economic model** means estimating or otherwise disciplining demand, costs, capacity, transfer laws, diagnostic channels and contractual restrictions using data. None of the synthetic constants above is presented as an industrial estimate.

The relative interpretability of deployment types belongs primarily in the first object. It can affect the second and the cost of performing the third. It should not be collapsed with them. A controlled reference cell and an uncontrolled field deployment may reveal different components of failure; no universal one-dimensional ordering need exist.

### Empirical discriminator and scientific status

A useful empirical design starts with original jobs before routing. Record model and embodiment vintages, offered capacity, human recovery, actual inference, support, qualification, acceptance, receipts and lawful access. Otherwise a policy can improve its measured success rate by refusing difficult work and still degrade service to the original population.

Separate four interventions: access to source evidence; provision of a dated forecast; authority to act on it; and verification capacity. Match an ordinary human/hybrid organization on information and dated cost. Measure accepted output and resources before valuing private receipts.

For recursion, keep the executor and reference task population fixed while transferring only the research procedure. Let the recipient produce a successor and randomize passage of that successor to a third cohort while preserving access to the original procedure. Better first-cohort execution or first-generation reuse alone does not establish this second-generation effect.

The current edition establishes a common economic state/action/account, an exact finite firm solution, an independently reconstructed replay, a scoped competitive solution, and explicit analytical identities. It provides no new empirical effect estimate and no evidence that an actual LLM firm improves itself indefinitely. The [claim ledger](CLAIM_LEDGER.md) distinguishes proved statements, computed results, source inheritances and open obligations. The next cumulative extension is a competitive horizon long enough for successor procedures to affect another firm's production and research choices, without replacing the strong ordinary-policy comparator.


## Cumulative extension: joint recipient configuration

[Joint-count state aggregation and the shared-resource terminal game](JOINT_COUNTS.md) establish that a competitive continuation can be compressed by joint local types under permutation symmetry, but not by each firm's separate qualification or action counts. Two otherwise identical three-target economies with equal marginal qualification counts have unique equilibrium private cash (2,2) versus (4,4) under the same dated cash and compute constraints. The long-horizon recursion game is not yet solved. The theorem and exact terminal solver are the next building block, not an independent recipient-value coefficient.


### Concurrent joint recipient transitions

The next enlargement of the common competitive model now has an [exact public-history transition](JOINT_TRANSITION.md) and [tested generator](joint_transition.js). The local digital qualification, archive and rights coordinates and both firms' global stocks enter the same observed next state; the shared latent transfer regime is mixed only after multiplying its conditional report likelihoods. This completes the transition dependency of the joint-count result, not a backward-inducted many-generation game. The digital-only binary restriction fixes physical production and arm/mobile investment outside the menu while retaining reference construction and scope. The public information externality must be separated from private archive capture and from a physical MPK effect.


## November 26: concurrent competitive backward induction

[JOINT_GAME.md](JOINT_GAME.md) closes the exact short-horizon public-state game on the concurrent digital-recipient transition, including every legal labeled unilateral action under two continuation selections. Five initial configurations with two/three periods yield pure equilibria at all enumerated continuations. In the funded three-period one-target economy cap 2 expands the root action set but does not induce selected research. A direct second successor from an inherited first method needs development, training and service in three successive periods; acquiring both from zero needs four. Selection can change private wealth and the current scope/operating decision independently of technology. The broader competitive multi-generation premium and physical manufacturing extension are still open; neither the staged cohort value nor the planner's optional-policy theorem transfers automatically to competitive private wealth.


## November 26: pooled output and the economic scale of recursion

[POOLED_RECURSION](POOLED_RECURSION.md) closes a longer concurrent restriction with a pooled linear-demand market, local archives, fixed scope, and sufficiently prefunded shared service/research resources. A strict output-saturation theorem yields an exact competitive separation and positive cap-2 premium of 5.967401 ticks per firm at eight distinct targets over sixteen periods, beginning from procedure zero. Separate active-quantity games test the same caps without the saturation theorem. This does not establish a positive return under every coupling; the public-belief site-overlap and physical-manufacturing enlargements remain open. Initial principal is excluded and all returns arise from dated cash. Retain the strong ordinary contingent/paid equivalent comparator.

## Competitive embodied capital and the production/research substitution

Concurrent embodied competitive game: paid kits, delayed assembly, installed arm/mobile, local qualified recipes, cash, ordinary learning and successor menu in one exact dated two-market account. 32/32 matched cases; inherited-procedure manufacturing increases accepted jobs 7.5→10 and customer surplus 10.5→20 while combined terminal wealth falls 58→56 (higher-total pure selection); cheaper kits induce actual order→assembly→service and change rival research; matched cap-2 null. Positive active-rival cap-2, endogenous retention/scope, longer horizons and general mixed solver open.

[Derivation and exact dated game](EMBODIED_GAME.md). Kit procurement and assembly are separate choices; a newly installed mobile may release labor for digital service rather than increase physical jobs at a fixed frontier selection. Do not extend single-firm optional-menu monotonicity to a change in both competitors' opportunities. This restriction retains local inherited evidence and a fixed lab; it is not the full unknown-transfer game.


## Four-date funded embodied continuation

[Funded embodied game](FUNDED_EMBODIED.md) proves the conditional cash and action quotient and carries the two-market embodiment restriction from procedure zero through four dates. Four-date embodied cap-0/1/2 from zero solved under guaranteed funding and two pure selections via a cash-independent continuation quotient; all six yield wealth (160.5,159), 12.5 accepted jobs and customer surplus 22.5, with ordinary training and actual mobile-kit orders/assembly but no successor attempts. Binding-cash cap-2 diagnostic stopped at 300,001 profiles (33,480 solved states), not an equilibrium nonexistence result. Positive active-rival cap-2, larger recipient sets, rights/scope and binding finance remain open. This is a solved public-state equilibrium selection, not an unrestricted game solution.

## November 26: local recipient cohorts and exact bounded cash

A joint qualification mask with one physical and two separate digital recipient markets preserves overlap; exact cash clipping works even with binding cash under a specified quotient-based equilibrium selection. 14/18 primary cases solved; eight labeled, uncapped, distinct-cost checks agree on private wealth. Funded split vs overlapping qualifications raises combined wealth 224→228 at the same eight accepted jobs and customer surplus 12 (highest-total selection); at B=7 the comparison is 72→74, with both firms' qualified counts unchanged and active financing. Three-date inherited psi=1 cap-1/2 remains a matched null (118,118); from-zero four-date cap-0 solves, cap-1/2 reach the 1.8m profile budget, not an economic null. [Derivation, technology, exact results and falsifiers](COHORT_EMBODIED.md). Unlike the prior fully funded quotient, partial cash clipping preserves binding states and retains cost differences there. The digital level-2 shared controller is not retained in the binary local qualification restriction. No new RL training or actual calibration.

## November 26: terminal economic irrelevance and solved four-date cohort game

Four-date from-zero three-recipient embodied cap-0/1/2 now all solved under both continuation selections: wealth (166,166) or (166,164), no successor attempts in any case. Terminal projection and funded penultimate successor dominance reduce cap-2 from 6,689,725 to 3,239,595 profiles and 17,538 to 3,754 memo states; unprojected higher-budget solve matches exact selected wealth and successor counts. Five-date batch exceeded execution limit; positive active-rival second-generation return, endogenous retention/scope and longer binding finance remain open.

[Proof, exact results and falsifiers](COHORT_SCALE.md) · [Reproduction](cohort_scale.js) · [Results](cohort_scale_results.json). The projection is conditional on the selected terminal game and funding bound; binding penultimate actions remain intact. No learned-policy, empirical calibration or universal superiority claim.

## November 26: evidence rights and endogenous lab scope

Endogenous archive retention, paid outside training/data and dated lab entry/exit now enter the same three-recipient competitive technology. 24/24 primary pure-game cases and 12 projection-off comparisons solved. With an inherited procedure 2, installed mobile and costly outside research, retention rights induce one ordinary-service archive→internal physical qualification→extra accepted job: combined wealth 347→348, jobs 12→13, customer surplus 18→21. At cheap outside research or binding B=9, rights add zero selected private value. With inherited physical archives, open rather than closed initial lab scope raises wealth 349→362 and jobs 13→16; without enough useful opportunity the lab exits. This is a matched rights/scope comparison, not an endogenous second-generation acquisition result. Three-date positive cases fix hardware, while two-date cash/scope cases allow assembly.

[Derivation, exact competitive results and falsifiers](COHORT_RIGHTS.md). The terminal projection preserves inherited scope when it changes the current bill, and the funded penultimate closure result is conditional on cash-independent payoff selection. No empirical or general-equilibrium claim.

## November 26: embodied retention and strategic randomization

Endogenous kit ordering and assembly restored to the three-date rights/scope economy. All 16 matched cases solved (15 pure roots, one exact two-action mixed root with pure continuations). Installed mobile rights premium survives (+1 private tick); a paid mobile kit without installed hardware makes rights unused. With installed arm and paid mobile kit, rights displace selected assembly; under the higher-total pure continuation rule the root has no pure equilibrium across 170×170 retained profiles. Verified mixed root retains with probabilities 3/5 and 1/2, wealth (171,169.2), 12.8 jobs and surplus 22.4, versus no-right pure wealth (174,169), 12 jobs and surplus 18. Lower-total continuation gives equal private wealth (171,170) with and without rights, but rights add one job. No selected kit orders or endogenous successor acquisition in these three-date cases.

[Derivation and exact mixed certificate](MANUFACTURING_RIGHTS.md) · [Solver](manufacturing_rights.js) · [Results](manufacturing_rights_results.json). Conditional pure continuation selections, no unrestricted mixed solver or empirical calibration.


## November 26: economically usable service window and from-zero acquisition

Four investment dates with 40 or 60 independently resourced terminal service shifts: six exact prefunded public-state games from procedure zero. Both firms retain local physical evidence and acquire both paid successor licenses when permitted; ordinary contingent training, paid outside training/data, lab entry/exit and kit procurement/assembly remain feasible, subject to one shared investment slot per early date. At N=40 the cap-2 minus cap-1 combined private wealth is -0.125 despite more jobs; at N=60 it is +15.03125, positive for each firm (+7.25,+7.78125), with terminal jobs 232.5→240 and contested market shifts 112.5→120. Cap-2 acquisition via licenses, not internal development; neither hardware order nor assembly selected. The positive active-quantity from-zero cap-2 acquisition witness is conditional on the enlarged terminal service window, high outside/kit costs, prefunding and higher-total pure continuation.

[Derivation and exact results](SERVICE_WINDOW.md). Conditional fixed-profile break-even N=3896/97; not a global threshold or internal-development result.


## November 26: internally produced successor robustness

Nineteen exact service-window games separate execution qualification from internal successor success. Two-date endpoint probability premium b(q-p)-p(1-p); original internal kernel ties ordinary retry at p=b=3/4,q=1. Improved internal development (one compute slot, success (3+old)/4), costly but feasible substitutes, N=60: cap-2 internally develops both generations from zero with expected attempts 3.5, zero licenses/contracts, combined private wealth premium 23.173828125 (both gain), terminal jobs 226.875→232.5; positive under lower-total selection too. Original kernel with costly successors selects ordinary learning; improved two-compute variant buys first and develops second yet loses combined 30.25; cheap outside qualification erases original premium and reverses improved one (-0.2578125). No selected kit orders; terminal reset block, funding, slot bottleneck and local archives retained.

[Derivation and exact comparisons](INTERNAL_SUCCESSOR.md) · [Reproduction](internal_successor.js) · [Results](internal_successor_results.json).


## November 26: calendar composition and staggered service

Equal-total 63-shift calendar reallocation from (1,1,1,60) to (1,1,30,31) eliminates the +23.173828125 cap-2 premium under the higher-total continuation; both choose first-generation learning. Advancing the 29 shifts another date changes the selected investment to costly outside qualification and also yields a cap-2 null. Early digital admission and alternative selection tested; concurrent inexpensive-kit diagnostic is explicitly budget-limited if unsolved.

[Derivation and exact block-restricted comparisons](STAGGERED_WINDOW.md) · [Reproduction](staggered_window.js) · [Results](staggered_window_results.json). Fixed-program identity, not a universal threshold. No empirical estimate.

## November 26: concurrent manufacturing, retained learning and operating-cost returns

The previously budget-limited concurrent cheap-kit staggered comparison now solves both cap-1 and cap-2. At fixed 63 shifts (1,1,30,31), entry date 3, and kit price 4, enabling one research and one hardware action concurrently increases combined generated private wealth 1850→2067.625 while accepted jobs fall 248→246 and customer surplus 496→492. Both firms order and assemble a mobile robot; in the concurrent regime both also develop a first successor and train on deployment archives, saving expected 2.0625 per later service shift at unchanged later quantities/prices. No second successor selected in either regime. The six exact selected pure games include an exact replay of the accepted costly-kit late-entry comparison, full retained-menu deviations, and forward dated accounting. Exact projected transition-class caching and two-pass profile streaming remove redundant continuation evaluations; this is not an unrestricted mixed or binding-finance solution.

[Derivation and exact comparisons](CONCURRENT_WINDOW.md) · [Reproduction](concurrent_window.js) · [Results](concurrent_window_results.json). Fixed-program private break-even at nine later shifts, not a globally reoptimized threshold. The later accepted-output frontier is unchanged, yet qualified execution reduces complementary resource use. No empirical estimate.



## Globally reoptimized equilibrium regions: November 26 extension

Globally reoptimized integer threshold mapping in the accepted four-block economy: balanced later service windows give no selected learning through S=8, two asymmetric pure root equilibria at S=9, and bilateral learning at S=10. The boundary cases agree under cap-1/cap-2 and higher/lower-total pure continuation selections. At S=9 an exact symmetric mixed root uses research probability 25/32 each, checks all 92 retained actions per firm with zero regret, and passes forward dated accounting. The exclusive S=10 comparison reaches an off-path subgame without a pure equilibrium under its chosen continuations; mixed continuation remains open. A fixed-profile affine incentive-region theorem and selection counterexample are proved; the diagnostic fractional crossings are not promoted to full-game thresholds. All 56 result records (51 distinct solves) replay exactly; 33/34 primary comparisons solve and one remains explicitly open.

[The full extension](GLOBAL_EQUILIBRIUM_THRESHOLDS.md) defines regime values on an equilibrium branch, proves affine incentive regions for complete pure profiles under parameter-independent transitions and menus, and separates them from equilibrium selection and stationary stability. The numerical extension checks global firm best responses in the finite legal menus; it does not claim unrestricted general equilibrium or complete enumeration of continuation selections. The first selected learning crossing and bilateral-adoption crossing differ because a producing rival gains from temporary service withdrawal.

Make globally reoptimized equilibrium regions the organizing target. Next implement exact parameter-region incentive certificates and propagate mixed continuations at intermediate subgames, beginning with the exclusive S=10 gap. Retain ordinary contingent learning, outside research, hardware, rights, scope and dated resources. Separate equilibrium eligibility from selection, and test all off-path deviations. Then vary service timing, qualification/transfer probabilities and costs, and test within-block contingent learning against the mapped regions. Binding finance, directed archives, common latent reports and input-market closure remain cumulative extensions. Long-run stability requires a solved repeated/infinite-horizon economy and its economic transition law; solver failure, missing pure equilibria and nonlinear nonstationarity are distinct. Preserve November 27 recursive-pilot, November 29 program, December 2 theory-week, December 6 contribution and December 25 final gates.
