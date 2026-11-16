# Faster service, hourly receipts, and an explicitly bounded financing result

A synthetic contract diagnostic motivated by the [public assignment-finance statements](raas_assignment_evidence.md). Neither hourly-rate rigidity nor an advance fraction is identified by those sources. This is a tractable explanation and adversarial test, not a calibrated prediction or a selected original contribution.

## Service and contract environment

An existing qualified robotic service supplies accepted output q to a customer with revenue a*q-b*q^2/2. This is the same quadratic customer-revenue convention as Model A (inverse output demand a-b*q/2), with nonrobot marginal costs absorbed into a. Customer rivals' responses are held fixed. Its feasible incumbent has constant unit cost w and no capacity constraint. Customer output is chosen, not imposed. The provider has robot speed s in accepted units/hour, at most T hours, and resource cost c per robot hour. Hardware costs are sunk for this comparison; all remaining service/terminal obligations are included in the specified cost, with no terminal salvage.

Under a committed hourly rate h, the robot's unit fee is h/s. In the domain h/s<=w and robot capacity is slack, the customer adopts and chooses

q(s)=(a-h/s)/b, H(s)=q(s)/s, R(s)=h*H(s).

At exact equality with the incumbent, the stated convention selects robotic service; rejecting a tie changes that boundary only. When h/s>w, the customer uses the incumbent and robotic receipts are zero. Mixing with incumbent production would need to be solved if robot capacity binds; the numerical domain below keeps capacity slack throughout the adopted region. The result is not asserted for a congested site.

Here q increases with s, but H and R need not. In the adopted positive-output interior,

R'(s)=h*(2h-a*s)/(b*s^3).

Receipts fall once s>2h/a, even as customer output rises. More generally d log R/d log s equals the output elasticity with respect to speed minus one at a fixed hourly rate. The provider's service profit is (h-c)*H, so it falls in the same region when h>c. This is a contract-incidence result; it is not evidence that technical progress reduces total surplus.

## An advance finances a different prerequisite

At date zero the provider has cash B and can qualify an additional, separate project for K. That project pays known operating profit V at date one, net of all its operating/terminal obligations. Existing source-service receipts arrive at date one. A stipulated lender can advance up to lambda*R against those receipts, with zero interest, also requiring enough remaining source receipts to cover its operating costs. Thus the implemented advance limit is min(lambda*R,R-c*H). The loan is repaid from the source receipts. The new project's prospective receipts are **not pledgeable before qualification in this scenario**; allowing them is an important alternative, not silently forbidden by legal separation.

An advance L changes current cash to B+L-K, but lifetime terminal cash is B+source profit-K+V because repayment subtracts L later. Do not add the advance to project value. Qualification is chosen only if funded and V>=K; ties are retained as investment in the code. The contract terms and predictability are scenario assumptions, not an underwriting model or a Holmström–Tirole calibration.

When operating reserves do not bind, B<K and D=K-B>0, funding requires

D*b*s^2-lambda*h*a*s+lambda*h^2<=0.

Subject to participation and capacity, this defines a speed interval between the quadratic roots if the discriminant is nonnegative. The upper root comes from the decline in billable hours. If B>=K this financing restriction disappears. If V<K, repairing it need not change the investment decision. These are conditional feasibility/choice statements, not a universal adverse-learning theorem.

## Exact comparison and competent alternatives

Set a=6, b=1, w=3, T=3, c=1, B=0, K=4, V=10 and lambda=1/2. Compare speed two with speed four. All inputs use normalized units. T=3 exceeds the maximum required hours 9/4 under the fixed-hourly adopted schedule, so the capacity exclusion does not hide a binding bottleneck.

| Contract and speed | Customer output | Hours | Receipts | Source provider profit | Customer profit | Advance limit | Invest? | Terminal provider cash |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: |
| Fixed hourly h=4, s=2 | 4 | 2 | 8 | 6 | 8 | 4 | Yes | 12 |
| Fixed hourly h=4, s=4 | 5 | 5/4 | 5 | 15/4 | 25/2 | 5/2 | No | 15/4 |
| Fixed output p=2, s=2 | 4 | 2 | 8 | 6 | 8 | 4 | Yes | 12 |
| Fixed output p=2, s=4 | 4 | 1 | 8 | 7 | 8 | 4 | Yes | 13 |
| Repriced output p=3, s=2 | 3 | 3/2 | 9 | 15/2 | 9/2 | 9/2 | Yes | 27/2 |
| Repriced output p=3, s=4 | 3 | 3/4 | 9 | 33/4 | 9/2 | 9/2 | Yes | 57/4 |

For fixed hourly billing the funding quadratic has roots one and two. Customer adoption requires s>=4/3. Thus in the stated capacity domain funding is available exactly for s in [4/3,2], with the participation tie convention above. Faster service beyond two improves customer output/profit but reduces these particular pledgeable source receipts below the qualification requirement.

At the source service alone, customer plus provider surplus rises from 14 to 65/4 under the hourly speed gain; it is the provider's capture that falls. This is not a welfare ranking of the two-project allocations, since new-project customer surplus is unspecified.

The output contract p=2 matches the hourly contract's old-speed unit fee and quantity. It keeps receipts constant while the provider saves operating hours. The repricing comparator is also competent: with customer participation p<=w, provider profit (p-c/s)*(a-p)/b is strictly concave, so the optimal output price is min(w,(a+c/s)/2) in this positive-margin domain. Both speeds give the participation ceiling p=3. An adjustable hourly rate h(s)=p*s reproduces the same allocation. These are different pricing rights, not an assertion that an existing fixed-rate contract can be renegotiated at will.

## Counterexamples that constrain the claim

**Retain the old policy.** If experience merely makes speed four available and the old qualified speed-two policy remains feasible at unchanged terms, the provider can keep the old policy and value 12. Availability of the new policy does not lower optimized value. It may instead cause the provider to decline a privately unattractive update. If new learning is also reusable on a different configuration, do not force it to change the existing contract's operating policy.

**Change the contract.** Fixed output pricing or permitted repricing removes the declining-receipt channel in this example. A proposed paper must explain why rates or billable units remain committed, not compare a frozen hourly contract with an omniscient repricing policy as though they had the same contractual rights.

**Change funding access.** With B=4 both speeds fund the extra project. If the new project can itself pledge sufficient future receipts, the source-receipt shortfall can also be repaired. The public evidence does not identify pre-qualification pledgeability. The source margin can still decline under fixed hourly billing, but that is distinct from a financing bottleneck.

**Change demand.** At speeds below 2h/a, the demand response raises hours and receipts; more generally a sufficiently elastic output response can reverse the sign. Demand saturation strengthens the falling-hours channel. The model does not infer which region any actual customer occupies.

The surviving result is narrow: billing units and demand determine the cash-flow consequences of a specified productivity change, and these can matter for a restricted receipt-backed advance. The unrestricted claim that more learning reduces optimal enterprise value fails. Whether contract commitment and pre-qualification credit restrictions jointly yield a distinctive first-paper result remains open.

Replication: `python -m model.raas_receipts`; `python -m unittest tests.test_raas_receipts`. The kernel reuses the existing exact-fraction serializer but keeps this posted-unit-price customer problem separate from Model A's surplus-sharing tariff. Their quadratic revenue and resource accounting agree; their pricing institutions differ explicitly.
