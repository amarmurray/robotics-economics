# Estimands, observational support and source-policy value: a November 22 synthesis test

**19 November 2026 UTC; private research, synthetic illustration, no deployment authorization.** This is an integrated continuation of *When Capabilities Become Production*, especially [source-first selection](SELECTION_AND_SEQUENTIAL_DATA_VALUE.md), [adaptive qualification](ADAPTIVE_QUALIFICATION_MENU.md), [policy-induced target support](POLICY_INDUCED_SUPPORT_FRONTIER.md), and the [Models A–B bridge](ROBUST_MODELS_AB_SYNTHESIS.md). It reconciles rather than renumbers the research questions. No external originality, accepted-service observation, or November 22 milestone is claimed.

## 1. One common economic object and four distinct questions

A **unit** is the full prospective policy-closed network of controllers, learning pools, dispatch, humans, customer orders and resources. Choose source intervention `x` at time 0: an actual specified mixture and training/control recipe, including rights, pretraining, routine field trajectories, failure/recovery histories, assisted teleoperation, deliberate target probes, simulation and synthetic inputs as separate categories. Let `H_x` be the observable **pre-second-stage** history, containing full customer-order denominators, validation, failed qualifications, feasible operator/physical support, and eligible/approved actions. Let `B_x` be realized net captured contribution before the second choice, after first-stage costs. Let `Y_x(a)` be the *remaining* net whole-network captured customer production under a fully specified, independently approved complete continuation `a`, evaluated through the same `V(Q;omega)` with all original orders, new accepted services, demand shifts and scarce resources counted exactly once. The competent qualified fallback `F` stays available; `M_x(H)` lists only **approved and feasible** continuations. If an embodiment is not yet qualified or approved it is *not* a missing-valued feasible production action.

Define `m_x(h,a)=E[Y_x(a)|H_x=h]`. The four research quantities are:

| Object | Mathematical target | Observed with what? | What it cannot answer |
| --- | --- | --- | --- |
| Static complete-policy economic arm means | `E[B_x+Y_x(a)]` for fixed complete x/a interventions | Independently approved whole-network policy randomization and full accepted-order accounting | Adaptive histories or cross-policy qualification overlap |
| Paired technical qualification overlap | `t=P(Q_0=1,Q_1=1)` on the *same* opportunity/type | Compatible matched safe technical tests or cross-world restrictions; marginal independent-arm rates alone do not identify t | Captured network production |
| Post-source technical response | `r_x(h)=P(Q_{x then G}=1|H_x=h,D_x=1,A=G)` | Versioned joint qualification and random stage-two assignment on supported, approved source-failure histories | Whether training creates profitable service, or transport to x' |
| Sequential complete economic policy value | `J_x(pi)=E[B_x+m_x(H_x,pi(H_x))]` | Sequential whole-network randomization or justified sequential ignorability, positivity, and complete outcomes on histories used | Individual counterfactual t or a new source regime without its own support |

There is no technical-success-rate-to-dollar conversion: `Q` constrains which recipes can produce accepted services, and `V` optimizes those services under the actual customer market/operating state. Neither supplier fees nor data continuation may be counted a second time on top of captured accepted production. The source-policy contrast `J_1(pi_1)-J_0(pi_0)` is the economic choice; neither `t` nor `r` is itself the estimand of that contrast.

## 2. Conditional identification without cross-world technical overlap

**Proposition (source-specific adaptive policy valuation; established dynamic-regime logic).** Fix a common pre-treatment target population, a finite pre-choice history, finite approved action menu and a policy `pi_x(h) in M_x(h)` that is fixed before evaluation. Suppose whole-network source assignment is randomized or conditionally exchangeable at baseline; continuation assignment is sequentially randomized or ignorable conditional on the *complete pre-choice* history; both stages have positive assignment probability on policy-used histories; consistency holds; and no training, dispatcher, operator, customer or information spillovers cross designated network units. Then

```
J_x(pi_x) = E[B_x] + sum_h P(H_x=h) m_x(h,pi_x(h)).
J_x^*    = E[B_x] + sum_h P(H_x=h) max_{a in M_x(h)} m_x(h,a).
```

All these quantities are identified at the population level given the above conditions and full outcome support. Proof: sequential randomization identifies each conditional mean; conditional expectation and maximization over the **actually observed pre-choice** history yield the expressions. First-stage values and downstream customer-production/resource costs are included only once. This does not identify a *unit-specific* counterfactual difference. The displayed optimal value is a population functional: an in-sample selected maximum is optimistically biased in finite samples, so its empirical policy must be prespecified or evaluated on held-out networks. This is classical dynamic-treatment-regime/g-formula mathematics, not a novel robotics causal theorem.

For `x` and `x'` each randomized with full permitted support, **their optimal expected policy values can be compared directly without t**. However `P(H_x)` and `m_x(h,a)` need not equal their x' counterparts. Randomization among x-failures alone therefore cannot transport grounding to x'-failures; it conditions on a source-induced selector. The nested-success selection identity from the preceding chapter is only a *sensitivity decomposition* requiring cross-world monotonicity and invariant downstream effects.

## 3. Counterworld: decision value is identified while transfer mechanism is not

Let `Q_0` and `Q_1` be binary first-stage **complete** accepted-A-order qualifications with randomized marginal success `P(Q_0=1)=1/4` and `P(Q_1=1)=3/4`. Each accepted qualified order has normalized incremental captured value 2, with actual production as the outcome. Among failures, a separately approved G policy would yield incremental accepted production 1 over competent fallback F on the target whole network, including all its costs. Under fully observed sequential stage-two support,

```
J_0(G-on-failure)=2(1/4)+(3/4)1=5/4
J_1(G-on-failure)=2(3/4)+(1/4)1=7/4.
```

There are two *observationally equivalent* joint technical worlds:

* **Nested:** `P(Q0,Q1)=(both:1/4, only0:0, only1:1/2, neither:1/4)`.
* **Non-nested:** `P(Q0,Q1)=(both:0, only0:1/4, only1:3/4, neither:0)`.

Both have the same marginal qualifications, the same source-conditioned failed-network histories and the same randomized complete continuation means, hence the same identified `J_1-J_0=1/2`. But the cross-world gainers' mass is 1/2 versus 3/4, and the qualification regressors' mass is 0 versus 1/4. A story in which source data monotonically resolve failures is **not** inferred by seeing an economically positive source-policy contrast. Fréchet gives `t in [0,1/4]` here; demanding nested success sets t=1/4 by *assumption*, not evidence. The two worlds can even support different recommendations about who should undergo further target grounding after a different source action. This construction is an exact response-type counterexample, not a robotics field estimate.

## 4. Partial-support valuation that can still decide an investment

A staged source experiment rarely covers every customer and controller history. Distinguish (i) a continuation which is **approved but unobserved** in a history, from (ii) an unapproved continuation which is simply **not in the deployable menu**. Never extrapolate the latter as realizable revenue.

For each approved but unobserved action `a`, suppose independently justified conditional bounds `l_x(h,a) <= m_x(h,a) <= u_x(h,a)` are available from a physical/order cap and retained-policy floor; observed actions have point conditional means. For an admissible fixed rule, summing its observed contributions and conditional bounds produces a valid interval. For the optimal history-aware rule define

```
L_x = E[B_x] + sum_h P(H_x=h) max_{a in M_x(h)} l_x(h,a)
U_x = E[B_x] + sum_h P(H_x=h) max_{a in M_x(h)} u_x(h,a)
```

with `l=u=m` on measured arms; F is always in the menu where qualified, preventing any bound from treating optional *unobserved* intervention as mandatory. Then `L_x<=J_x^*<=U_x`. The interval is **sharp only under** a rectangular unrestricted collection of compatible conditional response laws with achievable endpoints across the relevant histories. With one persistent transfer regime, shared capacities or order constraints spanning histories, this is an **outer interval** and may be tightened by a joint same-world response-type program; a rectangular adversary cannot be presented as the physical system.

For two source regimes, `J_1^*-J_0^* in [L_1-U_0,U_1-L_0]` is valid. With no cross-regime structural restrictions and independently attainable conditional endpoints it is sharp for the average contrast; signed full-market/cross-policy restrictions can make it conservative.

**Exact illustrative coverage audit (synthetic, units are captured full-service contribution):** regime x0 qualifies 1/4 of customer-network opportunities, each adding 2; on 1/2 of the population the approved failed-service continuation gain is observed to be 1; the remaining 1/4 has an approved but unobserved choice bounded by F at zero and physical/customer contribution cap 2. Hence `J0^* in [1,3/2]`. Regime x1 qualifies 3/4 at value 2 and produces supported continuation contribution 1 on its remaining 1/4; `J1^*=7/4`. The first-stage source-policy choice has robust difference `[1/4,3/4]` in favor of x1 **before** source expense. Paying an extra known 2/5 source/compute/right/curation cost changes the interval to `[-3/20,7/20]`; no robust source selection follows. These are not empirical dollars. The **sign change due to known source cost** shows how to use a support certificate to make a decision rather than calling all uncertainty an impossible data gap. Any risk cap or unsupported-state bound must be audited, not invented from benchmark percentages.

## 5. Separation, tests, and strongest objections

The within-regime measurement design is a sequential whole-network experiment, not independent randomized robots connected to one learning/dispatch/operator/customer pool. Pre-register order denominators *before* x, not only post-treatment accepted orders; record qualified F/S and original orders, all approved menus, pre-choice histories, rights, compute, collection method, versioned policies, observed training transition/target occupancy, and post-choice accepted production/expired demand and recovery resources. Stage-two randomization must be stratified by source regime and prospective supported history; it cannot manufacture physical approval. A four-arm static factorial answers a different question; matched paired Q tests answer t if safe and compatible; on-policy stage-two technical tests answer r when complete qualification is directly observed.

The two strongest contrary explanations are **selection rather than transfer** (x changes the distribution of failures, not G's technical mechanism) and **diagnostic information rather than capability** (a safe report changes action choice without physically improving qualification). A third is a **changed embodiment** with new support and manufacturing/validation delays: its learned representation and capital cost cannot be absorbed into a scalar positive source coefficient. Test the first with within-source qualification transitions plus prechoice joint support; test the second with approved non-actuating diagnostics and retained-performance controls; and test the third with a qualified changed-body arm including actual physical/organizational resources and original-order displacement. Target customer demand, captured value and policy-induced occupancy must be recorded *alongside* technical outcomes. Do not infer one from the other.

**Nearest verified prior art (bounded audit).** Murphy, *Optimal Dynamic Treatment Regimes*, JRSS B 65 (2003), 331–355, published 25 April 2003, DOI https://doi.org/10.1111/1467-9868.00389, already supplies dynamic rules, consistency and sequential ignorability. Frangakis and Rubin, *Principal Stratification in Causal Inference*, Biometrics 58 (2002), 21–29, DOI https://doi.org/10.1111/j.0006-341X.2002.00021.x, supplies the posttreatment/cross-world distinction; the publisher's online metadata is inconsistent about original online publication date, so the volume-year is the appropriate citation. DDA https://arxiv.org/abs/2606.10127 already values future data in §5 and complementary aggregation in App B. LP resource duality, process flexibility, reliability expansions, value of information and Frechet coupling are foundations, not discoveries here. The potential contribution is a physically testable and economically complete **source-to-qualified-production** interface, subject to originality review and actual evidence. No formal uniqueness claim is made.

**Synthesis verdict for Nov22 (not passed):** the four estimands are conceptually reconciled and a support-aware source investment certificate is now specified. Remaining evidence is (i) a genuinely approved, independent policy-closed whole-network intervention or signed qualified accepted-service registry; (ii) source-to-joint-Q technical measurements; (iii) original customer-order/resource and actor-capture accounting; (iv) quantitative official industry production backbone and a bounded closest-prior-art review. An audited independent technical dataset is not a measured customer contract. The November 22 scientific gate must be decided against these conditions rather than the number of derivations. Preserve November 29, December 6 and December 25 at 23:59 Eastern.
