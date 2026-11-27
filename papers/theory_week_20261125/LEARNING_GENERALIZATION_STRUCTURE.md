> **Historical synthesis / scoped proof appendix.** The dated theory-week program and its solver queues are retired. Analytical results are owned by [Paper 3](../../research/recursive_firm/README.md) under the [canon map](../../research/portfolio/CANON.md); other claims follow that map. The preserved text, dates, scripts, nulls and saved results below are provenance, not a calendar deadline, live lease or authority to expand the frozen solver.

# Learning where generalization works

## Deployment choice, experiments and the production of transferable capability

November 25, 2026, America/Chicago. Conditional theory and synthetic verification; no estimated industrial parameters. Main input: `e27351d38593b2b489fa6f49a752fe5433a1fa6a`. Production input: `bb8d87b86d6a679e55de777c59f6e5d82e4ecb3b`. Recursive-firm input: `ec919bd95c52521051414b5f99315854b9700879`. Source branches are read-only antecedents. The existing theory-week and Christmas clocks remain unchanged.

**Question.** Which deployments and investigations should a robotics firm choose when it is uncertain not only about individual tasks, but about the relationships that make learning travel between tasks?

**Answer within the restrictions developed here.** Allocate to decision-relevant combinations of productive work, connections between contexts, and tests of the proposed common representation. Connections and tests can be complements. A sequential test can screen a costly expansion, but a noisy test or a short deadline can make direct target learning preferable. No portfolio of one-off comparisons can, by itself, distinguish certain measurement failures from failures of the transfer relationship. The firm may therefore need to invest in the measurement procedure before expanding its deployment footprint.

This is the next step beyond the production branch's [relative-interpretability model](https://github.com/amarmurray/robotics-economics/blob/bb8d87b86d6a679e55de777c59f6e5d82e4ecb3b/research/theory_integration_2026_11_17/data_value/RELATIVE_INTERPRETABILITY_AND_DIAGNOSTIC_SUPPLY.md) and [reach/coherence model](https://github.com/amarmurray/robotics-economics/blob/bb8d87b86d6a679e55de777c59f6e5d82e4ecb3b/research/theory_integration_2026_11_17/data_value/RELATION_STRUCTURE_AND_TRANSFER_GRAPH.md). Those studies already learn the relation and test composability. The additions here are an endogenous choice and ordering of bridges, audits and a priced direct alternative; an explicit failure of diminishing returns; noisy graph likelihoods; and a nonidentification result that changes which experiments should be available. [Code](generalization_allocation.py) and [results](generalization_allocation_results.json) accompany the derivations.

## 1. What the firm is learning

Index a context by task family, embodiment and vintage, environment, operating policy, customer interface and date. An industry label alone does not identify a learning domain. Two manufacturing sites may have incompatible observation conventions; manufacturing and inspection work may share a well-defined sensing or manipulation relationship.

There are at least five distinct objects:

| Object | Economic question | Example of an investment |
| --- | --- | --- |
| Source skill or task state | What did the source experience establish? | More useful operation, demonstrations or task-specific training |
| Relative interpretation | How does that evidence map to a specified target? | Matched source/target comparisons, an embodiment interface or a grounded representation |
| Structure of relations | Which mappings compose, and over what class? | A held-out consistency check, an intervention across interfaces, or testing an alternative partition |
| Observation technology | Is an apparent disagreement caused by measurement, or by a real limit of transfer? | Independent instrumentation, repeated measurements, retained reference equipment |
| Qualified production menu | Which candidate improvements can actually be used, on which dated orders? | Validation, integration, manufacturing, support, rights and finance |

Thus relative interpretability is a useful name for the second object, with uncertainty about the third and fourth. It is not generally one scalar attached to a robot. The economic state is a joint posterior over task states, relationships and observation mechanisms, attached to a dated feasible production menu. Literal physical calibration is one mechanism inside that state. Statistical confidence calibration, internal neural-network interpretability and cross-deployment transportability are distinct questions.

Learning a shared bias across related tasks has a long technical history: Baxter's [A Model of Inductive Bias Learning](https://arxiv.org/abs/1106.0245), published in JAIR in 2000, explicitly studies choosing a hypothesis space using multiple related tasks. No novelty in the idea of learning to generalize is claimed. Our question concerns the economic allocation of bodies, work, experiments and control rights that produces useful evidence about that structure.

## 2. The common dynamic allocation problem

Let `s` contain the installed hardware vintages, model and research resources, retained experiment procedures, customer obligations, qualified recipes, dated input capacity, cash and enforceable rights. Let `b` be the joint posterior about the latent technical state. A choice `u` can produce ordinary service, acquire outside evidence, make a matched comparison, test a representation, improve measurement, revise hardware or change a contract. Its feasible set is determined by resources, timing and rights. Outcomes include both paid production and whatever observations can actually be retained.

With a common period length, the risk-neutral private value is

\[
V_t(s,b)=\max_{u\in\mathcal A_t(s,b)}
\mathbb E_b\!\left[\pi_t(s,u,\omega)+\beta V_{t+1}\{F_t(s,u,Y),\mathcal B(b,u,Y)\}\right].
\]

Here `pi` counts cash contribution and resource costs once; `F` carries commitments, qualification and resources forward; and `B` is the Bayesian update under the chosen observation technology. A production choice can alter both `F` and the law of `Y`. An inquiry investment can change which experiments the next state permits. Future work is valued through the continuation program, not by adding an arbitrary price per trajectory.

The baseline can respond to history, learn from normal operations, retain old releases, buy a direct target experiment, and decline a project. Every alternative has the same ordinary observations unless its actual activity changes them. If a natural production event will supply an equivalent report early enough, there is no incremental reason to buy a duplicate. The broad dual-control connection—actions affect production and information—is established prior art; see Klenske and Hennig, [Dual Control for Approximate Bayesian Reinforcement Learning](https://www.jmlr.org/papers/v17/15-162.html).

This Bellman equation defines the complete comparison, rather than solving every industrial case. The following restrictions solve a consequential component exactly.

## 3. Reach and evidence about a common representation

Retain the source branch's binary benchmark. A latent hypothesis `H=1`, with current probability `p`, says a shared representation is valid within a prespecified class. Independent uniform vertex labels `Z_i` generate exact pair relations `M_ij=Z_i Z_j`. Under `H=0`, each pair has an independent uniform relation. The latter are pair-local facts, not globally consistent vertex labels. Initially observed exact relations form a consistent graph.

For a graph with `m` observed edges, `n` vertices including isolates, `c` connected components and independent cycle count `r=m-n+c`, a consistent pattern has posterior

\[
\Pr(H=1\mid G,M_G)=\frac{p_0 2^r}{1-p_0+p_0 2^r}.
\]

An inconsistent exact cycle rules out this particular shared hypothesis. A forest gives reach conditional on the hypothesis but no evidence for it. This follows by counting the `2^c` consistent label assignments under `H=1`, versus `2^{-m}` likelihood of each observed pattern under `H=0`. These are properties of the stated priors, not universal properties of transfer datasets.

A **bridge** joins previously disconnected components. It makes new path-based predictions possible, while supplying no evidence about `H`. A **cycle audit** measures an additional edge within an already connected component and checks it against the existing path. For one unused exact chord, agreement has probability

\[
z=\frac{1+p}{2},\qquad p_+=\frac{p}{z},\qquad p_-=0.
\]

The posterior mean remains `p`: `z p_+ +(1-z)p_-=p`. Counting only the confirming branch would manufacture a spurious learning gain.

An audit can update predictions in a different, disconnected component if both components share the same hypothesized representation. A bridge changes connectivity locally; an audit tests a common hypothesis. This nonlocal information effect requires the common-class assumption. It gives no warrant to generalize from one physical regime to every end market.

Pairwise synchronization is established mathematics. Singer's [Angular Synchronization by Eigenvectors and Semidefinite Programming](https://arxiv.org/abs/0905.3174) studies recovering relations from noisy pairwise measurements. The economic use of different graph roles, not synchronization itself, is the object of this note.

## 4. Deriving an economically weighted connection

For a fresh target decision, source information has symmetric reliability `a` and an available independent direct target report has reliability `d`, where reliability means twice correctness minus one. Given an unmeasured relation predicted by an exact path, transfer has reliability `a p`. The optimal binary decision with equal losses and those two symmetric reports is correct with probability

\[
Q(a,p,d)=\frac{1+\max\{a p,d\}}{2}.
\]

When the reports disagree, the more reliable one determines the decision; agreement yields the same choice. The source and direct report errors are conditionally independent under the restriction. Fresh task decisions do not pool other tasks' reports before their dated local decisions. General joint inference belongs in the full posterior program.

This `Q` is not a safety score or authorization to deploy. For the solved economic restriction, each candidate subsequently undergoes a separately available, fully informative verification stage, and a known conventional fallback serves a rejected candidate. A correct candidate yields a stipulated discounted contribution `w_j` relative to fallback. This idealized verification law connects the decision to a payoff. Real verification, joint feasibility and failure costs require their own measured law.

Suppose a candidate bridge connects components and makes a set `T_e` of previously unmeasured source/target pairs reachable. Exclude the actually measured bridge pair from `T_e`; its relation is directly learned even if `H=0`. Assume the selected chord and bridge have no separate current customer payoff, all target resources are separable and available, and there is no cross-recipient inference before action. The bridge's gross incremental operating value is

\[
R_e(p)=\frac12\sum_{j\in T_e}w_j[a_jp-d_j]_+,
\qquad [x]_+=\max\{x,0\}.
\tag{1}
\]

This is derived relative to using the direct reports. It is not an assigned graph-centrality score. A bridge between large components can be worthless if direct target knowledge dominates, margins are small, deadlines have passed, or required rights are absent. A small connection can be valuable when it reaches a consequential decision near its threshold.

For endogenous recipient investment, use the actual terminal value. For example, one optional project with upfront cost `k_j` has

\[
v_j(p)=\left[w_jQ(a_j,p,d_j)-k_j\right]_+.
\]

If the direct route is insufficient to cover `k_j`, adoption through transfer requires `p>(2k_j/w_j-1)/a_j`, when that threshold lies in the feasible interval. Replacing (1) by the sum of differences of these optimized values incorporates entry; shared slots require a joint maximization. Nonlinear adoption thresholds sharpen the distinction between technical reach and economically exercised reach.

## 5. Proposition: a bridge and an audit can have increasing returns

Consider one target reachable only after buying bridge `B`. An audit `C` lies inside a preexisting component and has no direct payoff for that target. An ordinary direct report of reliability `d` is available. Let `0<p<1`, `a>0`, and assume

\[
a p<d<\frac{a p}{z},\qquad z=(1+p)/2.
\tag{2}
\]

**Proposition 1.** Gross incremental values satisfy

\[
F(\varnothing)=F(\{B\})=F(\{C\})=0,
\qquad F(\{B,C\})=\frac{w}{2}(a p-zd)>0.
\tag{3}
\]

**Proof.** Without the bridge, the target relation remains unobserved between disconnected components; an audit alone does not change that. With the bridge alone, the ordinary direct report dominates by the first inequality in (2). With both, a confirming audit makes transfer preferable; a contradiction leaves the direct route available. The expected improvement is `z w(a p/z-d)/2`, which is the expression in (3). The second inequality makes it positive.

Consequently `F` is not submodular: the marginal gain from the audit is larger after the bridge than before it. An objective has diminishing returns only if adding an item to a larger collection cannot increase its incremental value. This example directly violates that condition. An adaptive greedy rule based only on the next experiment's immediate terminal improvement can stop at zero even when a profitable pair exists. Adding a small positive standalone alternative makes such a rule select the alternative; scaling `w` makes its ratio to the best pair arbitrarily small while preserving (2). This is a failure of that myopic rule, not of every approximation method or every deployment ranking.

The broader literature already establishes useful greedy guarantees under appropriate conditions. Golovin and Krause's [Adaptive Submodularity](https://arxiv.org/abs/1003.3967) supplies such a condition. Its guarantees cannot be imported merely because an objective is called learning or information. Our result identifies a concrete economic source of failure: reach and evidence about composability are complementary inputs.

This also refines the earlier [source-portfolio complementarity](../autonomous_firm/DEPLOYMENT_PORTFOLIOS_AND_DESIGN.md). There, a known measurement law made two sources jointly informative. Here, one investment extends reach while another investigates the law used to interpret that reach. The ordinary direct route creates a genuine decision threshold rather than disappearing from the comparison.

## 6. Proposition: test first and buy reach conditionally

Let the bridge cost `b>=0`, the audit cost `c>=0`, and let `R(p)` denote (1) or another nonnegative bridge value with `R(0)=0`. Assume the audit is already feasible before the bridge, its report law is unchanged by the bridge, opportunities survive either order, and the bridge's sign does not change the magnitude of the symmetric payoff. There are no separately binding delays, cash dates or service obligations in this restriction.

**Proposition 2.** The optimal value among these two investments, relative to the ordinary route, is

\[
U(p)=\max\left\{0,\ R(p)-b,\ -c+z[R(p/z)-b]_+\right\}.
\tag{4}
\]

**Proof.** The first two choices are stopping and acquiring the bridge alone. After an audit, a contradiction makes the bridge worthless; after confirmation the firm buys it exactly when its value exceeds cost. The last term is the resulting contingent program. Buying the bridge first cannot improve this menu: its only later useful decision is whether to buy the same audit, whose law is unchanged; the audit-first program can reproduce the informative branch while declining the bridge when it does not pay. The bridge-first alternative is `-b+max{R(p),-c+zR(p/z)}`, which is weakly bounded by (4).

If the bridge is bought after confirmation, audit-first saves

\[
(1-z)b
\tag{5}
\]

relative to buying both unconditionally. This is a financing and investment-selection benefit, not an extra physical-productivity multiplier. After an imperfect test, replace the last term of (4) by the expectation of `[R(p_Y)-b]_+` over all outcomes; negative evidence need not imply `p_Y=0`.

Order dominance has a clear boundary. If the entire confirming branch's net increment `R(p/z)-b` is delayed one period with discount factor `delta`, the staged-minus-simultaneous value, under the same two-branch purchase rule, becomes

\[
(1-z)b-z(1-\delta)\{R(p/z)-b\}.
\tag{6}
\]

The second term can overturn the saving. Expiring orders, a factory reservation or a customer who supplies the audit only after installation can also require a different order. The correct unit is a dated contingent program.

### Exact witness with an external alternative

Four contexts have exact initial edges `0--1` and `1--2`, while context `3` is isolated. The target uses relation `0--3`. The audit measures `0--2`; the bridge measures `2--3`. Set `p=.4`, `a=.8`, `d=.4`, `w=100`, `b=.8` and `c=.5`. Units are synthetic discounted contributions. Neither investment helps alone. Agreement occurs with probability `.7`, yielding posterior `4/7`. The pair's gross gain is `2`; buying both unconditionally nets `.7`. Audit-first, with optional bridge acquisition, nets `.94`.

Now offer an outside experiment that directly reveals the actual target relation `0--3`, without relying on composability, for `19.5`. That raises the terminal contribution by `20`, so its net value is `.5`. The experiment remains available to the adaptive comparator after either audit result. With two inquiry slots, full enumeration gives:

| First choice, with optimal continuation | Net increment above the ordinary route |
| --- | ---: |
| Audit; buy the bridge on agreement and direct evidence on contradiction | 1.09 |
| Bridge; optimally choose the next investigation | 0.70 |
| External direct target experiment | 0.50 |
| Stop | 0.00 |

The new strategy exceeds the best direct alternative by `.59`. With only one inquiry slot, the direct experiment wins. There is no assumed inability of the baseline to adapt: the enumerator optimizes every permitted history using the full latent-state posterior.

## 7. Noisy tests: graph shape is not enough

Perfect comparisons were useful for identifying the mechanism. They are too strong for interpreting real failures. Suppose each observed edge is

\[
Y_e=M_e\varepsilon_e,\qquad \mathbb E[\varepsilon_e]=\lambda_e\in[0,1],
\]

with independent known measurement errors, one reading per distinct edge, and the original exact shared-representation hypothesis. Under `H=0`, all observed edges remain independent uniform signs. Under `H=1`, the likelihood ratio against that alternative is

\[
L_G(y)=\sum_{F\subseteq E:\ \deg_F(v)\ \mathrm{even}\ \forall v}
\prod_{e\in F}\lambda_e y_e.
\tag{7}
\]

**Proposition 3.** Equation (7) is the exact likelihood ratio, and the posterior is

\[
p_y=\frac{pL_G(y)}{1-p+pL_G(y)}.
\tag{8}
\]

**Proof.** Conditional on labels, the likelihood is `2^{-m} product_e(1+lambda_e y_e Z_i Z_j)`. Expand the product and average over independent uniform labels. A term survives exactly when every vertex label occurs an even number of times. Divide by `2^{-m}`, the likelihood under `H=0`, to obtain (7), then use Bayes' rule. This is a standard finite graphical-model expansion, used here to price experiments.

A forest still has `L=1`; its only even-degree edge subset is empty. For a single cycle, `L=1+rho product_e y_e`, where `rho=product_e lambda_e`. Long paths with imperfect readings can therefore produce weak tests even though their exact cycle count is one. With overlapping cycles, multiplying independent cycle Bayes factors is generally wrong. For a complete four-vertex graph, all positive readings and every `lambda=.5`, the correct likelihood ratio is `1.6875`; multiplying the factors for three fundamental triangles gives `1.423828125`.

For a noisy chord compared with an exact existing path, let its reliability be `lambda`. Then

\[
z_\pm=\frac{1\pm p\lambda}{2},\qquad
p_\pm=\frac{p(1\pm\lambda)}{1\pm p\lambda}.
\tag{9}
\]

A negative result no longer proves the common representation false unless `lambda=1`. If the existing path is also noisy, the chord can simultaneously improve the inferred vertex relations and the belief about `H`; use (7) and the full posterior, not only a scalar update.

In the preceding numerical witness, reduce only audit reliability to `.8`. Audit-first is worth `.342`, below the direct alternative's `.5`. The best first action changes to direct target learning. The exact indifference reliability is `315/374`, approximately `.842246`, in the active branch of this example. More observed connections alone do not determine the research allocation: measurement reliability, direct substitutes, costs and decisions jointly determine it.

## 8. Proposition: more one-off comparisons may not identify the problem

Now allow approximate structure even within the proposed class. In this section both structural and measurement reliability are unknown; this relaxes the preceding known-noise restriction:

\[
M_e=Z_iZ_j U_e,\quad \mathbb E[U_e]=\tau_e,
\qquad Y_e=M_e\varepsilon_e,\quad \mathbb E[\varepsilon_e]=\lambda_e.
\]

The `U_e` are stable pair-specific deviations from the shared representation. The `epsilon` are independent measurement errors. They are independent of labels and of each other. For clarity, first hold `H=1`; uncertainty about `H` adds another layer, not identification by itself.

**Proposition 4.** With only one observation per pair, the observed joint law depends on `tau_e` and `lambda_e` only through the products `tau_e lambda_e`. Different structural and measurement qualities can therefore produce identical data on every chosen graph while implying different predictions for an unobserved true target relation.

**Proof.** Conditional on labels, `U_e epsilon_e` is a sign with mean `tau_e lambda_e`, independent across edges. Substitute this product for `lambda_e` in the edge likelihood and in (7). In contrast, for a new edge whose local deviation is unobserved, `E[M_ij|Y]=tau_ij E[Z_iZ_j|Y]`. The latter retains the separate target structural reliability. A policy that adaptively chooses previously unmeasured pairs cannot distinguish observationally equivalent parameterizations: induction on the history gives identical conditional observation distributions, hence identical distributions of subsequent choices and reports.

For a homogeneous class, compare `(tau,lambda)=(1,.5)` with `(.5,1)`. Every one-reading-per-edge dataset has the same law. Following two positive path observations, the label correlation is `.25` in both cases. But the unobserved true target relation has mean `.25` in the first world and `.125` in the second. One world needs better measurement; the other has a real limit on generalization. Those are different hardware, research and deployment problems.

There is an available discriminator under additional assumptions. Repeat an observation of the *same stable pair relation* with independently refreshed measurement errors. Then `Y_e1 Y_e2=epsilon_e1 epsilon_e2`, so its expectation is `lambda_e^2`; the structural deviation cancels. Replication or an independently characterized reference can help separate the mechanisms. Repeats are not additional independent graph chords. Common sensor errors, changing relations, or unknown dependence can defeat this discriminator and require additional interventions. Neither the identifiability argument nor its repair establishes an empirical parameter for any robot.

This supplies an economic reason to retain a reference configuration, calibration equipment or an external measurement partner even when another production deployment promises more immediate revenue. The investment changes what can be learned about the transfer technology. Without it, collecting more novel task pairs can preserve the same unresolved ambiguity.

## 9. Connections to the firm and the wider economy

### Hardware, model breadth and minimum viable scope

Hardware affects more than current accepted throughput. It can change source observability `a`, measurement reliability `lambda`, the feasible matched comparisons, and the persistence of relations after a vintage change. A model or research method can change the candidate representation class, its approximate structural fit `tau`, and the cost of reusing it. Deployment choices determine which edges and ordinary outcomes appear. All of these changes must be costed and separately qualified.

The recursive branch's [degrees of full stack](https://github.com/amarmurray/robotics-economics/blob/ec919bd95c52521051414b5f99315854b9700879/research/recursive_firm/stack_profile/README.md) already distinguishes hardware, model, deployment and finance coordinates, and defines minimum viability as a feasible frontier. The present result adds structure to its evidence requirement. A viable learning route may require complementary observations and enough dated inquiry capacity for their sequence. A count of sites or a weighted average of ownership shares cannot establish that route. One site that supports repeated reference comparisons can be more useful than many sites that share the same unidentifiable observation law.

The standard production fleet can rationally be narrow while the evidence portfolio is varied. Scale manufacturing can use one embodiment; a small reference fleet or partner can investigate different sensing regimes. The opposite can also occur if diverse operating embodiments are themselves necessary to identify the relevant relationships. No unconditional diversity or standardization premium follows.

### Integration, rights and equivalent outside experiments

Rights enter the feasible information structure: can source and target records be matched, can the final outcome be observed, can a report cross customer boundaries, and can a resulting method be exercised on the recipient? Possession of files does not settle these questions. A relationship learned in one contract may be unusable under another.

There is a useful equivalence result. If a partner arrangement can reproduce every relevant internal experiment's joint report law, timing, downstream control rights and feasible actions at the same all-in cost, the optimal values coincide. Map each internal contingent program to its external counterpart and vice versa. Mere ownership adds no value in that comparison. A specific integration premium requires a difference in those feasible programs: cost, latency, enforceability, access, production effects or available experiments. A cheaper timely equivalent external route can erase it.

This connects to the recursive branch's [integrate-then-delegate result](https://github.com/amarmurray/robotics-economics/blob/ec919bd95c52521051414b5f99315854b9700879/research/recursive_firm/boundaries/README.md). Internal inquiry may help discover a portable interface; after that, outside provision may become the best option. Starting position matters because installed equipment, staff, interfaces and transition costs differ. There is no general prediction that all successful firms converge to internal hardware-model-deployment ownership.

### Multivariate MPK_r and investment timing

Keep current physical production, expected information value and private capital returns separate. For a qualified target recipe, the restricted production function

\[
y_j=\min\{A_j K_j,\ H_j,\ D_j\}
\]

has physical robot marginal product `A_j` only when the robot stage binds, and zero when another fixed complement binds, away from ties. A structural audit changes beliefs; it does not physically increase `A_j`. A resulting trained and qualified recipe may increase `A_j`, unlock another task, reduce required support, or convince the firm not to invest. The corresponding installation choice follows the full payoff and constraints.

The financial value of a reference machine can largely arise at other machines or dates. That makes a vector of current and future effects necessary, but does not justify adding its information value to current physical output. The earlier source-portfolio and transfer-graph studies already give examples where information raises private value while source purchases or recipient starts fall. Equation (4) shows the selection mechanism directly: costly reach is exercised only in favorable states.

Equations (5) and (6) connect inquiry to capital velocity. Screening can preserve cash that would otherwise fund an unproductive bridge; sequential inquiry can also delay commissioning and collection. Faster information changes velocity only when it changes a binding commitment, qualification or cash date. It need not increase the eventual number of deployed machines.

### Shared resources and the direction of diffusion

[Evidence reallocation](EVIDENCE_REALLOCATION.md) showed how improved source execution can expand ordinary workload and crowd out a recipient's evidence. The present complementary case intensifies the problem: losing one required bridge, reference reading or audit can remove the return to the other investment. Additivity in effective evidence is not generally available.

Let the induced deployment response be a local derivative, where it exists,

\[
J_{ji,t}=\frac{\partial\mathbb E[K^*_{j,t+1}]}{\partial K_{i,t}}.
\]

This object depends on current graph coverage, structural beliefs, measured reliability, ordinary substitutes, demand, rights and resource constraints. At discrete policy switches, use finite program differences instead. A technically helpful source can reduce another market's investment by taking a shared commissioning window or funding allocation. Conversely a previously irrelevant context can become valuable after an audit makes a connection worth buying. A fixed nonnegative spillover matrix cannot describe all these regimes.

In [Data-Driven Automation](https://static1.squarespace.com/static/5efca972e541380b32c1ca30/t/6a20374d02f50639ed704dce/1780496209650/DDA_June26.pdf), Farboodi, Koh and Xia model heterogeneous task data generated by economic activity and affecting automation elsewhere. Our connection is to endogenize the evidence behind usable cross-task relations and the allocation that exercises them. We have not solved a replacement equilibrium growth model. A finite static graph eventually exhausts its unknown relationships; sustained growth would need new opportunities, drift, new embodiments or an evolving experiment technology. Repeatedly counting the same inferred path cannot establish a perpetual feedback dividend.

### Competition, external benefits and commercial structure

The weights `w_j` in a private problem are captured contributions after the relevant customer and supplier responses. They need not equal real resource savings. A shared audit can help other firms without giving its sponsor a claim on their gains. Under separable recipient resources and a committed common report, let `G_f` be firm `f`'s optimized incremental value after its own conditional bridge costs. A single sponsor may decline when `G_f<c<sum_g G_g`. This is a conditional underprovision comparison; it is not a claim about a unique voluntary-contribution equilibrium.

With rival procurement, overlapping validation or entry, private `G_f` must be recomputed in the resulting game. A common report can change joint success patterns and displacement as well as marginal correctness. The source branch already solves restricted examples of this distinction and competing equivalent diagnostic suppliers. Lower supplier prices can make an experiment privately attractive without directing it toward the largest social learning benefit.

Commercial form determines who benefits from learning. A system seller, model licensor, hourly service provider and operator paid per accepted job can face the same physical relation but different returns to reducing work or expanding transfer. Manufacturing capability, commissioned capacity, customer access, rights and cash therefore remain separate economic coordinates.

### Recursive organization and the strong comparator

A sufficiently expressive prewritten contingent policy with the same experiments, resources and information can implement all of (4), including the direct external option. Calling the optimizer recursive does not make its value larger. Learning the posterior about a fixed model is ordinary adaptive learning.

The separate organizational investment is in an experiment or decision procedure: retaining a repeatable reference, inventing an economical matched comparison, identifying a useful partition of tasks, or making a qualified procedure portable. Test its value by charging development and validation, carrying it to fresh work, and asking whether it improves the feasible observation/decision menu relative to a competent existing procedure and purchasable alternatives. If both organizations can make precisely the same procedure investments, an unrestricted contingent-policy benchmark again replicates the result. The economic distinction resides in resources and technologies, not in the adjective recursive.

[Organizing Intelligence](https://storage.googleapis.com/deepmind-media/papers/organizing-intelligence.pdf), by Imas, Koh and Legg, distinguishes multidimensional competence from coordination and studies how agents sort into competing organizations. The connection here is that joint interpretation and inquiry can alter the future competence and feasible task portfolio of an organization. This note does not establish a new coordination scaling law or infer firm size from a learning graph alone.

## 10. Cross-market implications and a discriminating design

These are proposed mechanisms to investigate, not claims that these markets empirically have the stated transfer structure.

| Environment | Candidate relation or shared hypothesis | Useful discriminating comparison | Binding economic link to observe |
| --- | --- | --- | --- |
| Repetitive material handling | Whether a grasp or perception correction transports across objects, fixtures and grippers | A matched bridge plus a held-out cross-gripper consistency test; direct local retraining as an alternative | Changeover, accepted throughput, support and customer order density |
| Manufacturing with complementary stages | Whether coordinate, tolerance or process relationships compose across tools and stages | A closed chain of measurements with independent metrology and repeated readings | Joint line acceptance, tooling commitment and release windows |
| Inspection and maintenance | Whether a signal anomaly has comparable meaning across sensors, assets and operating regimes | Cross-sensor reference, repeated readings and later independently verified outcomes | Sparse failures, delayed ground truth, liability allocation and decision deadlines |
| Digital exception handling | Whether a common representation preserves the meaning of records and actions across systems | Schema-matched cases, alternative resolution procedures and a held-out workflow | Access rights, labels, exception queues, compute and actual settlement |

A prospective study should prespecify the hypothesized class and keep an independent target panel. Compare ordinary operation, a bridge, a coherence audit, their combination, and an independently priced direct target route. Add repeated measurements of the same stable pairs, or independently characterized reference equipment, to distinguish measurement noise from local structural deviations. Track all outcomes, including contradictions, rejected releases, customer refusals and canceled expansions. Do not select only successful transfers.

First measure posterior predictions on unmeasured pairs and task performance on fresh cases. Then separately measure complete qualification, actual allocation, accepted production, dated resource use, cash commitments and retained successor evidence. Randomize or otherwise identify order when estimating the staging effect. The model is rejected in a particular application if the proposed audit changes neither held-out transfer predictions nor a feasible decision, if the bridge reaches no useful target, or if a cheaper equivalent ordinary/direct route accounts for the gain. Identical apparent edge accuracy with different repeat behavior is evidence against collapsing measurement and structure into one coefficient.

## 11. What is established and what remains

Established under explicit restrictions: an economic bridge value; complementarity between reach and a test of composability; exact optimal staging with an adaptive outside route; a noisy graph likelihood that handles overlapping cycles; and observational equivalence between measurement and structural error with a conditional repair. These join earlier capital, full-stack and evidence-allocation results. They do not establish commercial magnitudes, universal transfer, a new statistical learning theorem, or a complete market equilibrium.

The replication uses exact rational arithmetic. It compares the graph expansion with direct enumeration for all 729 four-vertex observed graph/sign patterns with heterogeneous noise, checks all 729 perfect-observation patterns against cycle counting, solves the full finite latent-state experiment tree with the external alternative, and independently enumerates the structural/measurement equivalence. These calculations support the stated formulas and examples; the proofs supply the general claims.

**Next theoretical question.** Jointly choose the representation class or partition, the measurement technology and the next deployment when relations drift across hardware vintages. The sharp dependence to solve is whether a retained reference or paid external standard makes the *next* round of graph discovery more informative per scarce research hour, while recipient adoption feeds back into available source work and rival sponsorship. Preserve direct experiments, ordinary learning, dated capacity and the option to delegate. This extends the experiment technology itself rather than merely adding another task to a fixed graph.
