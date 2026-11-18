# When Capabilities Become Production — order-level economic loss certificates for data investments

**18 November 2026 | private, conditional theory continuation.** This is the same source → joint qualification → optimized accepted customer production → dynamic demand argument, not a new stand-alone economic model. Its exact question follows [policy-closed networks](POLICY_CLOSED_NETWORKS_AND_DATA_VALUE.md): **if source data, grounding, a new embodiment or a specialist changes the market's complete controller/dispatch/operator policy, what economic decision can be defended from an immutable original-order registry when no independent connected-network replication is available?**

## 1. The evidence gap in the preceding network theorem

The policy-closed union graph may have just **one** connected customer market. Its complete-policy randomization theorem then cannot generate independent market replicates by assigning robots individually; learning may permanently change the controller and orders may be rerouted. But we can sometimes bound the *economic harm* of a candidate through constraints on what existing qualified accepted customer service it can destroy, without pretending to identify every counterfactual policy outcome.

Fix a genuinely physically admissible complete-horizon policy menu \(\mathcal P_{\rm safe}\) with frozen retained policy \(F\), productive source acquisition \(R\), target grounding \(G\), embodiment \(E\) where approved, competent specialist \(S\), and optional pinned/isolated variants. A policy includes training recipe, checkpoint lineage, embodiment, qualification, dispatch, operator/recovery reservation, customer opportunity horizon, rights, costs and fallback. Let \(Y(p,\theta)\) be its **one** optimized captured contribution from accepted complete service over the same original customer census, customer demand process and time horizon, under one persistent world \(\theta\). The data's future effects already enter this \(Y\); there is no extra data premium.

Partition original-window accepted qualified service units under \(F\) into enrolled A and potentially affected B. The units in B may be complete order-service bundles rather than isolated skills. Let \(b_j\geq0\) be the captured *net incremental contribution* for baseline B service \(j\), after declaring all service variable costs and competition for capacity. It is not an industry wage or an arbitrary assigned price per trajectory. This decomposition is legitimate only when order-level contributions are accounting-additive under the actual complete policy and costs/resources are not counted elsewhere. If two recipes are jointly required to satisfy an indivisible order, **that order is one unit**; qualification marginals cannot be substituted for its value.

For a candidate \(p\), write the actual **same-world** complete difference as

\[
Y(p,\theta)-Y(F,\theta)
=a_p(\theta)-c_p(\theta)
-\sum_{j\in B}b_j\ell_{pj}(\theta)+n_p(\theta)-e_p(\theta). \tag{1}
\]

Here \(a_p\) is accepted A-service contribution gain *under p's full-network environment* (not a transferred technical benchmark); \(c_p\) is all additional real compute, curation, training, embodiment, coordination, validation and operating cost not already embedded in \(a_p,b_j\); \(\ell_{pj}\in[0,1]\) is fractional loss of baseline B's contribution (binary for one indivisible service); \(n_p\geq0\) captures independently net-positive new B service when it can genuinely be declined without damaging retained service; and \(e_p\geq0\) is any additional negative repricing/churn/rights/market effect not represented by losses. **(1) is an accounting assumption, not a free theorem about arbitrary production LPs.** If customers, prices or demand change in ways that invalidate it, an explicit bound on \(e_p\) or a larger unit/census is required. A customer opportunity with zero actual orders remains in the denominator.

## 2. Structural service-loss polytope and dual certificate

Suppose separately verified system evidence supplies the **policy-uniform** restrictions

\[
\ell_p\in\mathcal L_p:=\{\ell:0\leq\ell\leq{\bf1},\ H_p\ell\leq d_p\},\quad
a_p\geq\underline a_p,\ c_p\leq\overline c_p,\ e_p\leq\overline e_p. \tag{2}
\]

The inequalities must hold for every safely reachable history and every maintained persistent regime; a low empirical mean, a silent message log or a one-operator *expected* utilization number is not a hard cut. Define \(D_p=\max_{\ell\in\mathcal L_p}b^\top\ell\). For nonnegative \(b\), feasible bounded nonempty \(\mathcal L_p\), the following **conditional service-retention certificate** follows:

\[
\boxed{\inf_\theta[Y(p,\theta)-Y(F,\theta)]
\geq\underline a_p-\overline c_p-\overline e_p-D_p.} \tag{3}
\]

By finite LP duality, the worst plausible displaced-service contribution also equals

\[
D_p=\min_{\lambda,\mu\geq0}
\{d_p^\top\lambda+{\bf1}^\top\mu:
H_p^\top\lambda+\mu\geq b\}. \tag{4}
\]

The dual's nonnegative prices certify the largest damage permissible by *audited* edge/dispatch/contract restrictions. They are not prices of source data, and the LP duality is established mathematics. If all that is verified is \(\sum_j\ell_j\leq k\), \(0\leq k\leq m\), then by the exchange/rearrangement inequality

\[
D_p=\sum_{j=1}^{\lfloor k\rfloor} b_{(j)}
+(k-\lfloor k\rfloor)b_{(\lfloor k\rfloor+1)},\quad
b_{(1)}\geq\cdots\geq b_{(m)}\geq0,\quad b_{(m+1)}:=0. \tag{5}
\]

For binary loss and integer k, the extremum is exact if any subset of at most k baseline services can disappear consistently with the other assumptions. For non-integer k the fractional formula is an LP relaxation, not a physical claim of divisible customers. Under only the stated constraints and independently attainable \(a,c,e\) endpoints, (3) is **sharp in that abstract model**. In a particular robot system, coupling restrictions can make it conservative, or an unverifiable loss-cap assumption can invalidate it completely.

**Important: volume is not a market causal estimate.** A configured dispatch queue allowing one preemption per *slot* need not bound lost future orders to one: persistent learning, customer churn, wait-time demand, rebidding and recovery cascades can multiply losses. A defensible horizon-level \(H,d\) must include those paths or their explicitly bounded contribution, and a separate *physical* safe-admission proof must cover concurrent recoveries. This economic LP cannot certify robot safety.

## 3. An actual route choice requires whole-policy support

All numbers below are **synthetic normalized captured contribution**. Baseline A contribution is 5 and B has three separately accepted complete orders of net contribution \(b=(1.2,0.6,0.2)\), so \(Y(F)=7\). Assume for illustration that each candidate's listed A increment survives its *own* complete environment, no unbounded new demand harms B, loss restrictions are independently physically substantiated and the comparison policies are separately certified safe.

| Complete policy | Incremental accepted A contribution \(a\) | Additional cost \(c\) | Max lost B orders (audited assumption) | Worst B loss | Conditional net gain lower bound |
|:--|--:|--:|--:|--:|--:|
| \(R\): productive routine/source acquisition | 1.1 | 0.3 | 0 | 0 | 0.8 |
| \(G\): shared target grounding | 2.4 | 0.4 | 1 | 1.2 | 0.8 |
| \(E\): new embodiment | 3.5 | 1.0 | 2 | 1.8 | 0.7 |
| \(S\): competent specialist | 1.0 | 0.1 | 0 | 0 | 0.9 |
| \(G^{\mathrm{pin}}\): pinned/isolated grounding | 2.4 | 0.6 | 0 | 0 | 1.8 |

In this **stipulated feasible menu**, \(G^{\mathrm{pin}}\) has the largest robust lower contribution gain (1.8); absent that branch, \(S\) is the maximin choice (0.9), even though \(E\) has the largest technical-side A gain (3.5). The interval for shared G is [0.8,2.0] if n=e=0 and all lost margins are nonnegative; consequently G *might* beat S but a one-order loss cap alone cannot certify it. A conditional *genuine* cut protecting the high-margin 1.2 B order changes the worst G loss to 0.6 and raises the lower certificate to 1.4; this is a sharper **evidence bound**, not new physical production. If making that cut real costs 0.2 and leaves the A response unchanged, it is a **different policy** with lower guarantee 1.2—not a free improvement.

The table is not an observed robot economic ranking. In particular, requiring \(a_{G^{\rm pin}}=a_G\) despite the isolation of training/dispatch is a hypothesis that must be tested with matched qualification and customer-demand outcomes. The pinned branch beats the stipulated S guarantee only when its actual A increment exceeds 1.5 at the stated 0.6 cost and no loss. A new embodiment is not assumed safe merely because its potential A contribution is high.

## 4. Partial identification can be useful without pretending to close the graph

Three information levels must stay separate:

1. **Incomplete empirical support:** if only eligible A has been observed under G, neither the actual B losses nor a conditional hard cap follow; the unrestricted B bound from the previous chapter remains. Do not set \(k=1\) by convention.
2. **Engineering-constrained support:** if signed, versioned rules plus safe reachable-state analysis establish \(H,d\) and stable baseline service margins, (3) provides a conditional whole-policy lower bound even for one connected market. It need not point-identify the treatment effect. A claimed controller cut that ignores demand competition or shared operator capacity is not enough.
3. **Complete experimental support:** independent policy-closed market clusters with genuine approved network-policy assignment can directly identify a mean whole-policy contrast, as in the preceding chapter; that mean alone still does not certify worst-regime performance or hard recovery safety.

**Additive mean exception.** When economic outcomes truly decompose into fixed order-level margins, \(\mathbb E[\sum b_j\ell_j]=\sum b_j\mathbb E[\ell_j]\); the *expected* loss does not need the joint distribution of which orders are lost. This is a constructive reduction in empirical requirements. But complementarily qualified complete-service bundles must be aggregated before applying it; controller-pool learning, maximum simultaneous operator recovery, nonadditive overtime costs and demand response may require the **joint** law. Prior work already develops reliability-style joint qualification and interference; this observation does not erase it.

**Against the competent alternatives.** A lower bound for p versus retained F can rank p above a known complete-policy q gain only if \(\underline\Delta_p>\Delta_q\), or above a separately valid q upper bound if \(\underline\Delta_p>\overline\Delta_q\). Comparing two independent lower bounds is logically insufficient. Stronger paired comparisons may use valid same-world common constraints on \((\ell_p,\ell_q,a_p,a_q)\), but cannot assume a causal cross-world cut solely from baseline logs. The maximin criterion differs from expected-value and minimax-regret investment.

## 5. Data-source mechanism, empirical falsifiers and prior art

Source stock and acquisition \(x\), target grounding \(g\), embodiment \(h\), training selection, and field/recovery/teleoperation/simulation/synthetic/public inputs determine qualified controller states jointly. Neither the budgeted loss polytope nor its dual determines \(a_p\); that requires measured *held-out joint qualification* under each candidate and complete accepted customer service. A source that improves a task score but fails to alter accepted recipes has \(a_p=0\) in the actual customer accounting; no fictitious wage conversion is allowed. Optional free data preserves the old feasible policy and weakly enlarges the optimized menu **only** when the old implementation, customer world, resources and rights remain available. Mandatory sharing may break that premise.

The sharpest empirical falsifier is a connected target market where the proposed loss cap fails under an approved deployment history: original order IDs disappear outside the supposed affected set, accepted B contribution is repriced without the residual bound, or an isolated checkpoint still changes demand via shared dispatch. Conversely, a verified immutable contract/order router that excludes policy-sensitive B channels could make the conservative decision bound meaningful **without requiring unapproved robot experiments**.

The nearest mathematical foundations are LP primal–dual bounds and rearrangement (not novel), Manski-style partial identification of missing outcomes ([Manski 2005](https://doi.org/10.1016/j.ijar.2004.10.006)), and assignment-based causal analysis with interference ([Aronow–Samii 2017](https://doi.org/10.1214/16-AOAS1005)). DDA §5 already endogenizes production and future data; Appendix B already considers data complementarity. What might be useful in this project is the **operational bridge** from policy-specific joint qualification through defensible service-loss constraints to a decision against a competent specialist, not a claim of new optimization mathematics or empirical proof.

**Next exact task:** audit any *actual* authorized versioned controller, dispatch, operator and customer-order lineage; test whether any nontrivial horizon-wide service-loss cap can be defended and whether target grounding/embodiment changes the assumed A gain under isolation. If not, retain unrestricted support bounds and strengthen the November 22 first-paper assumptions, not another arbitrary numerical loss budget.