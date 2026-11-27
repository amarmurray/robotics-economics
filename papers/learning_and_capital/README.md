# Deploying to Learn, Learning to Deploy

**Canonical Paper 1.** Gate A: in progress. Gate B: pending independent hostile-referee pass. Gate C: pending. This manuscript consolidates the two-proposition core, signed coordination–grounding result and production/learning/financing foundations. [Canon and source map](../../research/portfolio/CANON.md) governs ownership. Existing exact scripts and source proofs are retained; no new solver was run for this consolidation.

## 1. The deployment decision

A robot can complete a job for one party, create experience useful at a second site, and leave a third party responsible for paying to qualify that next deployment. A firm choosing its first job must therefore consider where useful learning arrives and which actor can act on it. A second distinction arises when qualification changes what a rival can infer before pricing.

The paper has two principal propositions. **Where the saving lands** concerns payer-specific prerequisites and implementable contracts. **Who sees qualification** concerns the information and competitive institution through which a technical improvement changes captured value. The liquidity reversal is a corollary of the first. Customer-verifiable evidence and rival-visible evidence are different objects.

The competent counterfactual can learn, retain its existing controller and use human fallback. Ordinary funding, incentive and information arguments are prior art. The contribution question is whether the specified physical qualification, lawful data use and timing restrictions produce a portable additional implication. Novelty remains subject to Gate B.

## 2. Common service, learning and cash primitives

Accepted service has a stated task, configuration, deadline and acceptance criterion. Physical marginal product measures an increment in that service under a stated resource comparison. Its monetary value depends on demand, the contract, complementary costs and who receives the cash. Qualification probability, lawful transfer and realized service are distinct.

The three source foundations below retain their original local notation. They are now sections of this paper, not a parallel Learning and Capital monograph. [Shared notation](../../research/portfolio/CANON.md#one-shared-notation-table) governs new text; complete legacy-symbol reconciliation remains part of Gate A.

### Foundation 1. The marginal product of a particular robot

A deployment type specifies an embodiment, task stage, end market, controlling firm and operating window. Two firms can work in the same industry and occupy different positions in the three networks. A digital agent may dispatch jobs or review evidence from many physical sites. The robots, the available technical labor and permission to install a release remain site-specific.

Let $Y_m$ be original service accepted in end market $m$ at a given quality and deadline. Let $K_i$ be installed units of embodiment and site type $i$. At a stated service mix or fixed set of weights for selecting among feasible orders, define the column of marginal physical products

$$J_{mi}=\frac{Y_m^*(K+\Delta K_i e_i)-Y_m^*(K)}{\Delta K_i}.$$

Each coordinate has units of accepted service per added machine over the window. Operating or support hours can be perturbed separately. Other endowments, initial knowledge and original demand are fixed in this comparison, while dispatch can adapt. If several schedules tie, specify a dispatch rule or report a range. More capital can redirect work away from one market while increasing total value. For different final services, aggregation requires weights and counts each final service once.

The **operating value** of an additional machine includes savings in scarce human time, maintenance or shutdowns even when final volume is fixed. Its **investment value** is the difference in discounted private contribution between the best feasible programs with and without buying it, net of acquisition once. Both programs can use ordinary experience. Market prices, data rights, capital costs and spillovers to others separate this value from the physical marginal product.

A simple restriction gives the sign of the immediate effect. A final job needs one machine stage and one support stage. With demand $D$, installed robot capacity $K$, support hours $H$, and stage rates $a,b$, output is $\min(D,aK,bH)$. Improving execution can raise existing throughput and exhaust demand so that another machine adds zero units. Improving human exception handling can instead release a binding support constraint and make the next machine productive. Identical gains on a robot benchmark need not move the same coordinate of $J$.

What makes this about programmable production? The site at which a machine works determines both its immediate product and the experience available to change $a$, $b$, or a different firm's technology. Amazon's Robin study documents a fleet that ranked candidate grasps using results from attempted picks, across differing workcells and tooling. That establishes a physical route from operations into a policy update. How much transferable knowledge or additional capital a particular shift caused is a separate empirical quantity. [Li et al., *Demonstrating Large-Scale Package Manipulation*](https://roboticsproceedings.org/rss19/p023.pdf)

<!-- page -->

### Foundation 2. Data generation, collection and the firm's choice

A source site $i$ encounters $A_i$ attempts per period. They include recoveries and failed jobs. The operating policy selects the cases attempted. Let $q_{0i}$ be the useful records per attempt obtained in ordinary work, after accounting for novelty at the margin. Investigation intensity $z_i$ between zero and one adds $q_{1i}z_i$ records per attempt in this restriction. These rates are conditional on the current corpus and operating policy. A million nearly identical records can carry little additional evidence.

Let $t_{ji}$ be the marginal validated change in method $j$ per useful source record, inclusive of compatibility and permissions for that use. It can differ across embodiments. One retained record can benefit several recipients. A second copy at the same recipient confers value only through its incremental effect. The firm's discounted captured value per unit of that change is $\beta^{\ell_{ji}}\lambda_{fj}$ when usable after lag $\ell_{ji}$. Use joint expectations if event quality, permission and the opportunity to use a result are related.

Suppose incremental collection costs per attempt are $\omega_i z_i+\kappa_i z_i^2/2$, with $\kappa_i>0$. The linear term includes displaced productive work. With locally constant marginal values, yields and transfer, an interior choice equates marginal cost with the sum of marginal *captured* returns. Including corners gives

$$z_i^*=\mathrm{clip}_{[0,1]}\left(\frac{q_{1i}\sum_j\beta^{\ell_{ji}}\lambda_{fj}t_{ji}-\omega_i}{\kappa_i}\right).$$

This is why data richness has several dimensions. A site can generate unusual cases yet collect little when the operator cannot use the results and no beneficiary pays. A model supplier may attach greater value to a correction than the host that pays for human review. A license, a contingent payment or common ownership can change collection. Equal feasible rights, timing and financial claims yield equal incentives in this restriction.

Full-stack ownership is one way to connect operating, learning and financing decisions. A digital agent that can schedule machines may still depend on a customer to approve cross-site training or an owner to release cash. Autonomy concerns which of those decisions an agent can actually revise. The typology follows from control over these links and the resources they use. Different products, sites and contracts within one firm can have different degrees of recursion.

There is also feedback *against* learning. With incident-only collection, useful records per period equal attempts times the failure probability times the conditional usable yield per failure. If failures become rarer faster than attempts and conditional yield rise, the evidence stream contracts while successful production can expand. Deliberate sampling of normal work offers an alternative and consumes resources. Rights expiration or a change in embodiment can further reduce the useful life of the stock.

Write $L_{ji}$ for the net marginal additions to validated method $j$ per extra period of an active deployment of type $i$. In the simple source above this is incremental attempts times useful yield times validated transfer. In a constrained fleet it includes displaced attempts and review elsewhere. A recursive firm can invest to change $L$, the release lag, or the collection policy itself. A better executor changes present performance. A better rule for experimentation changes what the next unit of field access can discover. [Study of endogenous incident supply](https://github.com/amarmurray/robotics-economics/blob/6951d24824287b11056e62e3e5221f818086ef5c/research/recursive_firm/learning_dynamics/README.md)

<!-- page -->

### Foundation 3. Capital velocity and the decision to install

Operating turnover is qualified work per installed machine-period. Commissioning velocity is installations per crew-period. Both can rise while the cash available for the next purchase stays tied up. We use **financial capital velocity** for how often a unit of revolving funds can be committed, recovered and recommitted. If each installation ties up $c_j$ dollars for $T_j$ periods, each start occupies $c_jT_j$ dollar-periods. With financing base $W_j$, a balanced pipeline can start at most $W_j/(c_jT_j)$ installations per period. The turnover of identical fully occupied dollars is $1/T_j$. For staged collections use $m_j=\int b_j(s)\,ds$, the area under the outstanding recoverable cash balance of one project. Advance payments and interim releases change this area. Count permanent asset cost in the investment calculation. [Little's flow and occupancy relation](https://doi.org/10.1287/opre.9.3.383)

Let $\nu_j$ fresh eligible candidate sites arrive per period with heterogeneous one-time integration costs distributed as $F_j$. Each requires one standardized installation. Write $v_j$ for the private value of its incremental services given the deployed capital of other firms and validated method stock $h$, less the machine price and before the site-specific integration cost. For example, with a constant incremental operating margin $\pi_j(h)$, a commissioning lag $d_j$, a discount factor $\beta<1$, and per-period retirement probability $\delta_j$ after commissioning,

$$v_j(h)=\frac{\beta^{d_j}\pi_j(h)}{1-\beta(1-\delta_j)}-P_j.$$

This valuation includes the operating alternatives in Section 1. A move in market prices, the volume that qualifies or the division of savings can change private margin. In the solved restriction the private operating path used by the candidate is stationary after commissioning. With forward-looking price or policy changes use the expected discounted path instead.

Available starts are the minimum of profitable applicants, financeable starts and a physical installation ceiling $S_j$.

$$I_j(K,h,W)=\min\{\nu_j F_j(v_j(K,h)),\ W_j/m_j(h),\ S_j(K,h)\}.$$

The expression assumes applicants draw on equal cash-time within type and capacity can be assigned among eligible applicants. It applies to balanced pipelines, or to cohorts contracting for a cash-time budget. A transient rollout with dated receivables requires the outstanding balances by vintage.

A faster payment to a deployer may also tie up the customer’s funds sooner. For a small reallocation of revolving cash and comparable machines, the effect on total starts is the cash moved times the difference in starts per additional dollar at the two firms. It can be negative when the customer was the more constrained adopter. An acceleration of collections for one firm does not establish faster capital turnover for the entire chain.

When profitability binds, the response to a method improvement is proportional to the density of sites *at their investment threshold*, $\nu_j F'_j(v_j)\partial_h v_j$. When cash binds it is $-I_j\partial_h\log m_j$ at fixed $W_j$. When available machines or commissioning crews bind, it is $\partial_h S_j$. At ties compare both feasible regimes. Thus a higher physical marginal product can coexist with flat installation, and faster release of working capital can expand deployment with identical execution capability. Symbotic reports that customer advances and work performed before invoicing both occur. Its disclosure supports distinguishing these clocks. Identifying a binding financing constraint requires further evidence. [Symbotic, contract balances](https://www.sec.gov/Archives/edgar/data/1837240/000183724026000009/sym-20251227.htm)

<!-- page -->


The cash-time bound W_j/m_j requires m_j>0. Define b_j(s) as nonnegative recoverable cash actually tied up by that claimant. A fully prepaid or otherwise zero-occupancy type has no cap from this particular finance constraint; interpret its bound as infinite, not division by zero. Customer prepayments require separate customer accounting, not negative supplier occupancy credited as extra starts.

## 3. P1.1 — Where the saving lands

### Financing feasibility and deployment reversal

For initial deployment j, let k_a^j be payer a's remaining prerequisite bill, b_a^j its available cash before commitment, and t the capacity of enforceable payment links. In the divisible, costless payment benchmark, the follow-on can be funded exactly when every payer subset U satisfies
$$
k^j(U)\le b^j(U)+t(\mathrm{incoming}\ U).
$$
Necessity follows by adding resources available to the subset; sufficiency is the standard funding-flow/min-cut argument. The theorem's indivisible physical follow-on and its financing arrangement must not be conflated.

Let pi_j^0 be the current combined net return, chi_j^fund the indicator that all funding cuts hold, and g_j the participants' combined incremental follow-on return over their feasible fallback. After counting prerequisite costs once, and requiring feasible participation and implementation, this restricted additive combined-surplus benchmark ranks deployments by
$$
\pi_j^0+\chi_j^{\mathrm{fund}}\max(0,g_j).
$$
If H earns more now and only L funds the target, L is preferred precisely when g_L exceeds pi_H^0−pi_L^0. This is not a newly solved individual-firm equilibrium policy. Equal aggregate technical savings can put the two deployments on opposite sides of a payer-specific funding cut. Pooling or a feasible equivalent contract can remove that difference.

These statements are conditional financing arithmetic, not an intrinsic superiority of integration or a new max-flow theorem. Full proof and comparisons remain in [qualification_finance.md](../../research/theory/qualification_finance.md) and [learning_funding_alignment.md](../../research/theory/learning_funding_alignment.md).

### Financing a test versus inducing the test

Consider an operator that alone controls target validation and can fill the same shipment with human fallback. Let k_O be its avoidable validation cost, v_O its private gain, and d the expected enforceable transfer difference between validating and using fallback. Once the action is funded, strict validation requires
$$
v_O+d>k_O.
$$
An unconditional advance enters the cash of both actions equally. If all admissible settlement records have the same distribution under validation and fallback, d=0 for a contract written on those records. Increasing the advance can fund validation without changing its incentive.

A saving s on operator commissioning can cross the incentive threshold when
$$
k_O-s<v_O<k_O,
$$
while the same total saving on supplier adaptation does not. An auditable target test can permit a conditional bonus and remove the wedge, provided the test distinguishes the actions, verification is feasible and both parties participate.

The source's synthetic example uses supplier/operator cash (5,1), initial bills (2,2), one unit of saving and private gains (4,1.5). Operator-side saving induces validation. Supplier-side saving plus a one-unit advance funds but does not induce it. Adding a 0.75 pass bonus makes validation strictly preferred and leaves the supplier positive surplus. These are synthetic units, not estimates from the automotive replay.

The claim fails where the operator already gains enough to validate, settlement can distinguish the actions without the proposed audit, a supplier can directly procure the target test, or another feasible contract implements it. The complete assumptions, proof and counterexamples are in [qualification_observability.md §1](../../research/theory/qualification_observability.md).

## 4. P1.2 — Who sees qualification

A customer may verify target performance without disclosing it to competitors. Distinguish actual qualification, the procedure chosen, admissible payment records and the rival's pre-bid information.

### Public bid pricing

In the preserved two-price example, quotes are 4 or 2, demand is 7−2 times own quote plus the rival quote, and firm 1's capacity increases from four to eight. Its low quote is feasible only after qualification. Failure supports high quotes and a payoff of 12; public success induces the rival's low quote and a payoff of 10. Holding the rival's high quote fixed would instead give 14.

Thus, among equal-cost attempts, a higher qualification probability changes the first firm's payoff by −2 times the probability increase under this public-capacity institution. Abstention remains a separate feasible action; the comparison does not establish that an optimally chosen initial research program becomes harmful.

### Private qualification and disclosed procedures

If the actual outcome and procedure choice are private and there is no additional signal, a unilateral change of procedure does not change the rival's information. At the common rival belief, realized qualification improves the firm's payoff against either quote.

If the procedure is credibly disclosed before bids, the rival can react to its success probability even if the realized outcome stays private. In the source example, the rival changes its quote at p=1/2; moving from p=1/4 to p=3/4 reduces the first firm's ex-ante payoff from 12.5 to 8.5. The equality case and mixed rival response remain explicit boundaries.

### Quantity benchmark and institutional scope

With the same demand/cost/capacity numbers and continuous quantity competition, the source's unique solution raises the first firm's profit by 6/25 after qualification. In the archived funded embodied quantity calibration, both published selectors produce gains or ties and no strict loss across matched probability increases.

These are boundaries, not a universal quantity-monotonicity theorem. The later reservation/suffix institution admits off-path, selection-dependent conditional losses while leaving the relevant selected initial outcomes unchanged; it is preserved in the frozen verification archive. No new expansion is authorized.

The exact payoff table, private-information timing, quantity derivation and existing checker are retained in [qualification_observability.md §§2–3](../../research/theory/qualification_observability.md). The checker is subject to the [targeted oracle rule](../../research/portfolio/ORACLE_REQUESTS.md) before another invocation.

## 5. P1.X1 — Signed coordination and grounding

This extension imports Result 2 from the pinned production-theory source. Consider two dates, one final authorized service of contribution v≥0, no other competing orders, stable demand and additive costs. H is authorization, L timely baseline qualification, T incremental qualification from grounding G, S incremental routine qualification created by coordination C, and W_0≤W_1 usable capacity before/after C. These indicators have a joint distribution and are lawfully observable at dispatch. Qualification composes by OR; set R*=H(1−L)T.

The four-program interaction is
$$
I=J_{CG}-J_C-J_G+J_P
=v\,E[R^*(W_1-W_0)(1-S)]-v\,E[R^*W_0S].
$$
Subtract the grounding benefit without coordination from that with coordination and rearrange. Newly usable capacity creates complementarity; routine learning can make grounding redundant. Capacity release alone weakly complements G, whereas a pure routine-readiness improvement weakly substitutes under these restrictions.

General demand, shared orders, cost interactions or additional training interactions require the complete program comparison. The ordinary coordination comparator itself learns; freezing it would change the question.

Source and proof appendix: [WHEN_CAPABILITIES_COMPACT_DRAFT, Result 2](https://github.com/amarmurray/robotics-economics/blob/8dba84f45e18fe5896e75cd9a98539e4b87a83fb/research/theory_integration_2026_11_17/data_value/WHEN_CAPABILITIES_COMPACT_DRAFT.md) and [COORDINATION_ROUTINE_MODEL_AB](https://github.com/amarmurray/robotics-economics/blob/8dba84f45e18fe5896e75cd9a98539e4b87a83fb/research/theory_integration_2026_11_17/data_value/COORDINATION_ROUTINE_MODEL_AB.md). Its later portfolio/design material belongs to Paper 2; procedure recursion belongs to Paper 3.

## 6. Operational mapping and explicit nulls

The saved automotive comparison delivers the same 12 kits by the same modeled deadlines under human service and a prepared fixed cell. The customer outlays are 572 and 908 synthetic dollars, respectively. The 336 difference is conditional accounting within the declared replay window. The actual industrial source motivates a competent fixed alternative; it does not supply those numerical inputs.

Retain the job-level match, station versus upstream preparation, due bills, avoidable commitments and incomplete comparisons. Actual integration/qualification costs, supplier margins, support/maintenance costs, reuse permissions, target learning probability and financing terms remain unidentified. The deficit is not an observed advance or incentive-payment requirement. [Workcell bounds](../../research/workcell_cash_decision.md) · [Replay contract](../../model/WORKCELL_COMPARISON.md).

Public anchors remain distinct: Amazon Robin informs a technical learning/operating relation; National Grid Sandy Pond informs site qualification and permission; Symbotic records inform commercial acceptance, rights and accounting categories. They are not one joined causal panel.

The first Lane 4 packet uses the October 29, 2026 Symbotic–Walmart agreement and FY2026 filing to map acceptance, payment, data use and information separately. Its [structured record](../../research/portfolio/empirical_target_symbotic.json) retains missing project-level variables as null. This is preparation for Gate C; A and B remain open.

## 7. Claim boundaries, reproduction and next editorial test

P1.1 must survive pooling, competent contracts, human fallback and the distinction between liquidity and incentives. P1.2 must retain the exact offer/observability institution and the non-reversal comparisons. P1.X1 must retain the joint law and the evolving ordinary-learning comparator. Each empirical extension must state which of those premises is actually observed.

The [existing referee report](../../reviews/integrated_firm_referee.md) is an antecedent objection ledger, not the independent paper-specific Gate B pass. Next complete common notation, proof dependencies and every cross-paper route; then commission the adversarial pass.

Existing replication.py is retained without modification. The [canon register](../../research/portfolio/CANON.md#reproduction-ownership-and-completeness) maps the workcell and coordination scripts. No new computation was performed for this consolidation.

The earlier full Learning and Capital text, its first-generation network illustration and proofs remain preserved at the [input main revision](https://github.com/amarmurray/robotics-economics/blob/f3a6d0f8146c773ca7906f395f5eb52ec6fac910/papers/learning_and_capital/README.md). Its §§4–7 provide a fixed-primitive network appendix; endogenous procedure/multigeneration material in §8 is routed to Paper 3. This immutable source is a historical supporting edition, not a fourth active paper.
