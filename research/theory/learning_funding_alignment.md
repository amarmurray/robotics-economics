# Which learning reduces the binding qualification bill?

Theory checkpoint 3. This adds directional experience to the [fixed-bundle funding model](qualification_finance.md). It holds customer demand, physical output requirements and initial cash fixed to isolate the destination of a learning gain. Inputs are synthetic; the result is a conditional reduction of an existing flow problem, not an established original contribution.

## A tractable experience-to-cost transition

A deployment produces effective experience e and net cash b after all its collection/operating costs. Source configuration j induces nonnegative, payer-specific cost-reduction loadings ell_a(j). The cost of payer a's prerequisite becomes

`k_a(e,j)=k_a(0)-ell_a(j)*e`, for `0<=e<=Ebar`,

with `k_a(0)>=ell_a(j)*Ebar`. Thus costs never become negative in the admitted domain. This is a local linear approximation, not a universal learning curve. Effective experience means a qualified, rights-permitted cost reduction in this scenario; raw episode counts do not automatically become e. Zero loading can mean no permitted/validated transfer in a scenario; an empirically unknown loading must remain unknown. Negative transfer, unvalidated candidates, new eligibility and acquisition of information require different state transitions.

No independent “data value” is added. Learning changes an actual future obligation. Both deployments in the comparison have identical cash after all first-period costs; if obtaining one kind of experience costs more or displaces profitable service, that difference must change b before comparing policies.

## Exact threshold from all relevant funding cuts

For payer subset U define its initial deficit

`D_U=k(U)-b(U)-t(incoming U)`

and source-specific loading `L_U(j)=sum_(a in U) ell_a(j)`. Applying the fixed-bundle proposition at e gives `D_U<=e*L_U(j)` for every U.

If an initially deficient cut (`D_U>0`) has `L_U(j)=0`, this source cannot make the bundle financeable within the model, no matter how much experience in the admitted range it supplies. Otherwise the smallest sufficient experience is

`e*(j)=max(0, max_(U: L_U(j)>0) D_U/L_U(j))`,

provided it is at most Ebar. If it exceeds Ebar, no feasible threshold exists **within the specified linear domain**; no conclusion is drawn about a different technology beyond that domain. Proof: each cut inequality is necessary and sufficient by the funding-cut proposition, and the nonnegative loadings make their intersection an interval with that lower endpoint. Initially nondeficient zero-loading cuts impose no additional restriction. ∎

This formula is a transparent corollary, not a novel network theorem. It shows why a source's total learning gain or outgoing-edge count cannot identify its financing value: every still-deficient payer subset must be relieved. The bottleneck cut can change as transfer permissions or cash change. It is not always a singleton or the largest initial deficit, since loadings differ across cuts.

## Equal total improvement, different deployment value

Use cash b=(5,1), initial prerequisites k=(2,2), and no pre-service payment permission. Qualified future service earns combined provider/operator profit V=10, derived from the responsive customer contract in checkpoint 2. Two parties must still complete both prerequisites. Compare deployments producing one effective unit of experience and the **same total cost reduction of one**:

| Source | Cost-reduction loadings | Costs after e=1 | Full bundle funded? | Best combined terminal cash |
| --- | --- | --- | --- | ---: |
| Provider-focused | (1,0) | (1,2) | No: operator still lacks 1 | 6, retaining cash |
| Operator-focused | (0,1) | (2,1) | Yes | 13 = 6−3+10 |
| Broad | (1/2,1/2) | (3/2,3/2) | No: operator still lacks 1/2 | 6, retaining cash |

Provider-focused experience cannot repair the operator cut. Operator-focused experience needs e*=1. Broad experience needs e*=2, within a domain extending to two; at e=1 it is insufficient despite touching both prerequisites. The broad source is not worse technologically in every sense—it improves two obligations—but its gain is split across a binding and a nonbinding financing constraint. These are alternative source transitions, not three new empirical observations.

If a pre-service transfer of up to one is permitted, all three e=1 transitions fund the bundle, have the same total cost three, and yield combined terminal cash 13. The directional advantage disappears with transferable cash, holding engineering and learning reductions fixed. This distinguishes an interaction between transfer **of learning** and transfer **of funds** from a claim that targeted learning is universally better.

Individual implementation remains explicit. With equal future operating-profit shares five each, the operator-focused plan without an early transfer ends at balances (8,5), versus no-investment (5,1). With transfer permission, the provider-focused plan uses a one-unit contribution and ends at (8,5); the broad plan transfers half and also ends at (8,5). These plans satisfy the stated individual comparison, not arbitrary bargaining equilibria. The fixed cost reductions must be accepted before they reduce the funding requirement; an expectation of cheaper future validation is not current cash.

## Demand and identification boundaries

At e=1, complete investment costs three. With the no-investment alternative worth six, implementing the funded source is worthwhile only if V>3. If demand or the customer alternative makes V<=3, the observed financing advantage need not change action. At V=3 the decision ties. Unfunded sources cannot realize V even when it is large. There is no social-welfare conclusion from provider/operator cash alone.

To distinguish this mechanism empirically, measure the **same accepted target service** under matched source-experience treatments and separate actual engineering, commissioning, retained-support and validation obligations by responsible payer. Identify dates and reuse permissions, not just overall R&D spending or dataset size. A reduction in a model benchmark loss is insufficient to establish ell. Simultaneous hardware upgrades, customer preparation, easier sites and the selection of already-financeable targets are confounders. Separate cost reductions from supplier price transfers if making a resource-efficiency claim.

The source audit now makes the prior-art burden explicit: [Stein](internal_capital_markets.md) already studies reallocation under scarce finance, [Farboodi–Koh–Xia](data_driven_automation.md) already supplies directional spillovers, and [Chen–Elliott–Koh](capability_accumulation.md) already supplies capability combinations. The potentially useful research question is the empirically disciplined interaction; the combination alone is not proof of novelty.

Replication: `python -m model.learning_funding_alignment`; `python -m unittest tests.test_learning_funding_alignment`. The kernel reuses funding cuts from checkpoint 2 and exports exact fractions. No earlier model/result is changed.
