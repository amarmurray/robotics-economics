# Joint qualification and the location of deployable cash

Theory checkpoint 2. This minimal Model C extension adds a complementary service bundle and separate payer balances to the [two-period benchmark](deployment_investment.md). It does not yet endogenize which embodiment is designed, estimate learning, or solve organizational equilibrium. All numerical inputs are synthetic normalized units.

## State, timing and objective

At t=0 choose one initial deployment j. After its complete obligations, it yields a vector of collected cash b(j) across legally separate parties. Its cash-generating service has already been supplied; b is a reduced-form contract outcome, not a claim about specific companies. Initial setup is funded equally for all policies. Both deployment paths use the same information and engineering opportunity.

At the investment date, one future service requires **all** prerequisites in a bundle. Prerequisite i costs k_i, payable by its assigned party before future service. Paying only some prerequisites gives no service in the finite horizon; paid costs remain sunk. No resale, surviving support obligation or outside cash is omitted from the example's defined boundary: all are assumed zero. A richer horizon must model them explicitly.

Parties may transfer cash along authorized directed edges before paying obligations, with capacity t_ab for transfer a→b. These are contractually permitted payments, not automatic transfers between any entities sharing a parent. Transfers are instantaneous within this date, divisible, costless and do not consume a real resource. There is no borrowing against future receipts. Interparty compensation is specified in the example, rather than inferred from aggregate value. Lead times or legal restrictions would require a time-expanded or differently constrained formulation.

If the complete bundle is funded and qualified, the customer chooses output using the existing service benchmark. A specified contract allocates the resulting captured operating surplus across parties. The cooperative policy maximizes the parties' **combined net cash**, with individual balances and explicit terminal payoffs reported. This is a coordinated decision, not a decentralized equilibrium or a welfare optimum. The example's chosen plans are also individually no worse than the indicated no-investment alternatives; a general bargaining/participation result is not claimed.

## Funding-cut proposition

For a **fixed complete bundle**, let b_a≥0 be available cash at payer a and k_a≥0 its mandatory obligations. Transfers on edge a→b lie between zero and t_ab. The bundle can be funded iff, for every subset U of payers,

`sum_(a in U) k_a <= sum_(a in U) b_a + sum_(a not in U, b in U) t_ab`.  (FC)

The all-payer set checks aggregate affordability; smaller sets detect cash trapped on the wrong side of a payment boundary. Missing payment permission is a zero-capacity edge **in the specified scenario**, not evidence that a real contractual link is absent. Observationally unknown edges remain unknown.

**Proof.** Necessity follows by summing payer balance inequalities over U: internal transfers cancel, external incoming funds cannot exceed edge capacities, and outgoing transfers only reduce funds available to U. For sufficiency, construct a flow network with source→payer capacities b_a, payer→payer capacities t_ab, and payer→sink capacities k_a. Saturating all sink edges funds the complete bundle. For a cut whose payer nodes on the sink side are U, cut capacity is `b(U)+t(incoming U)+k(U_complement)`. Every cut is at least total obligations iff (FC) holds. The standard max-flow/min-cut theorem then gives a flow saturating every obligation. Unused source cash is retained. No investment is divided or partially counted as complete; only cash is divisible. ∎

**Attribution and limit.** This is a direct economic application of the standard max-flow/min-cut theorem, not a new theorem in network mathematics. The proof above states the reduction completely. The sufficient condition depends on the absence of transfer costs, timing frictions, collateral constraints or separate transaction-level permissions beyond the modeled edges. Selecting which service bundles to fund is a different optimization problem.

**Two-payer corollary.** With only edge 1→2 of capacity tau, qualification costs (k1,k2), and balances (b1,b2), feasibility requires and is implied by:

`b1>=k1`, `b1+b2>=k1+k2`, and `tau>=max(0,k2-b2)`.

Proof: these are the three nonempty subset inequalities. When satisfied, transfer exactly `max(0,k2-b2)`; payer 1 can cover its obligation after that transfer. Transfer volume above the minimum is unnecessary for feasibility and cancels in combined terminal cash.

## Exact reversal with fixed engineering and aggregate cash advantage

Let prerequisite 1 be a qualified configuration adaptation paid by a technology provider, and prerequisite 2 be commissioning paid by an operator. Both cost 2. The labels are illustrative; no field case has supplied these costs. Initial deployment H generates cash `(5,1)`, total 6; deployment L generates `(2,2)`, total 4. Both leave the same physical/capability state and future demand. The only differences are cash amount and location.

Future inverse demand is `p(q)=10-q`, with marginal service cost 2 and qualified capacity 2. Using Model A (`a=10,b=2,c=2,K=2,Pi0=0`), optimal q=2, revenue=16, service resource cost=4 and joint operating surplus=12. The RaaS contract captures 5/6 of this surplus, or 10. The operator receives customer payment 14, pays resource cost 4 and transfers a contractual 5 to the technology provider, leaving 5 each; the customer keeps 2. This **future service payment** is distinct from the restricted **pre-service funding edge** tau. Receiving a future fee does not fund today's prerequisite without permitted credit or prepayment.

| Pre-service payment capacity | H best plan and terminal balances | L best plan and terminal balances | Optimal initial deployment |
| --- | --- | --- | --- |
| tau=0 | No investment: (5,1), total 6 | Fund both: (5,5), total 10 | L |
| tau<1 | Cannot fund full bundle; no investment, total 6 | Fund both, total 10 | L |
| tau>=1 | Transfer 1, fund both: (7,5), total 12 | Fund both: (5,5), total 10 | H |

H has **more total cash** in every case. With tau<1 it fails the singleton cut U={operator}: obligation 2 exceeds operator cash 1 plus incoming capacity tau. L meets all cuts. At tau=1, H funds the same engineering bundle, retains `(2,0)` after investment and earns `(5,5)` from service. This is an exact threshold, not numerical noise. Paying only the provider's prerequisite under H would spend 2 with no future service and is strictly dominated by no investment.

The t=0 one-unit funding transfer is assumed to be an allowed contribution under the parties' joint project agreement, not a loan needing another repayment. Payer 1's terminal 7 exceeds its no-project 5; payer 2's 5 exceeds its no-project 1. Under L, both parties earn 5 versus 2 without investment. These checks establish individual gains against those stated disagreement plans; they do not identify the equilibrium negotiated fee split. The external qualification/commissioning suppliers receive total 4; their margins and resource composition are outside this business-cash boundary, so the combined return is not a social-welfare estimate.

## What survives and what fails

**Result.** A higher aggregate-cash deployment can be dynamically inferior solely because cash is held by the wrong payer for a complementary prerequisite. The appropriate feasibility check is a family of payment-network cuts, not just total cash or an engineering-reach graph. This extends the scalar liquidity diagnostic but is still standard finance/flow logic, not a settled paper contribution.

**Contract counterexample to an ownership claim.** A costless, enforceable separate-firm funding agreement with tau≥1 reproduces pooled-cash feasibility here. Therefore the example does **not** show that common ownership is required. Conversely common ownership without permission or ability to transfer does not establish feasibility. Integration could matter through authority, enforcement, taxes or transaction costs, but those mechanisms require modeling/evidence.

**Demand boundary.** If qualified service earns captured continuation value V, L with the bundle yields `4-4+V=V`, while unfunded H yields 6. Thus at tau<1 L is preferred only when V>6 (and individually agreed allocations are implementable). Demand saturation, a strong incumbent alternative or a lower capture share can remove the reversal. The example uses V=10, which is derived from the customer quantity choice, not an extra strategic premium.

**No completion, no benefit.** Failed qualification sets V=0 but retains paid costs. Removing either prerequisite from the engineering requirement changes the problem and may remove the singleton funding bottleneck. Learning is held fixed here to isolate payment placement; this is not evidence that learning is economically irrelevant.

## Joint demand and payment boundary

Keep the same costs, cash vectors, capture and service capacity, but vary the customer revenue intercept a≥0 and pre-service transfer capacity tau≥0. Since b=2, c=2 and K=2, captured continuation profit is

`V(a)=(5/6)*max_(0<=q<=2) [(a-2)q-q^2]`.

For a≥6, both the original threshold comparisons occur in the capacity-binding region, and `V(a)=(5/3)*(a-4)`. Solving V=4 gives **a=32/5**; solving V=6 gives **a=38/5**. For a<6 the exact concave optimum gives V≤10/3, so it cannot introduce another investment region. Thus the global policy partition on a≥0 is:

| Demand intercept | tau<1 | tau≥1 |
| --- | --- | --- |
| a<32/5 | H, no investment | H, no investment |
| 32/5<a<38/5 | H, no investment | H, complete bundle |
| a>38/5 | L, complete bundle | H, complete bundle |

At a=32/5 and tau≥1 H is indifferent between investing and retaining cash. At a=38/5 and tau<1 H without investment ties L with investment. The funding equality tau=1 is feasible. These tie sets must not be hidden by numerical rounding.

This partitions two effects often conflated: financing permission can change the investment decision while preserving the initial deployment (middle demand region), or change the initial deployment itself (high demand region). In the low demand region it changes neither. Demand here is the customer's own output market; the robot service demand is derived from its quantity choice.

The [diagnostic phase figure](../../model/results/qualification_finance_phase.svg) plots this analytical partition, not empirical estimates. The accompanying test checks exact candidate choices across a finite rational grid; the plot script rejects a stale input artifact. The diagram is a conditional result, not a forecast or a novelty claim.

**Topology versus state.** Changing tau on an existing permitted edge changes a financial capacity. Moving from a prohibited edge to a permitted one changes the contractual topology. Neither operation creates a new capability or a new customer in this example. Do not label it full endogenous reorganization of production.

## Empirical implication and next challenge

For a proposed complete service, record mandatory prerequisites, responsible payers, payable dates, dated free cash/committed finance, allowed prepayments/transfers, and the qualifying output/contract. A missing payment link is unidentified, not necessarily zero. If a denied feasibility claim relies on a cut, specify the exact obligations and incoming sources on that cut; an aggregate funding announcement cannot close it. Production and learning edges alone cannot identify the financing threshold.

Next distinguish this reduction from prior work on financial networks, internal capital markets and complementary investment. Then connect **directional deployment experience** to which qualification costs/rights exist, rather than simply relabeling fixed cash vectors. Retain the [capability-paper audit](capability_accumulation.md): a physical all-required bundle is different from that paper's market-relevance hyperedge and does not automatically imply its organizational bounds.

Replication: `python -m model.qualification_finance` writes the exact diagnostic artifact; `python -m unittest tests.test_qualification_finance` checks feasibility against explicit integer-flow enumeration on small networks and the synthetic decision/contract accounts. This is a small analytic extension, not a new general enterprise simulator.
