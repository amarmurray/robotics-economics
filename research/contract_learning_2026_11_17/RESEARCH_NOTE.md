# Q3 — Billing units, customer demand and the economics of reusable experience

**17 November 2026; source revision 7a2e974d85c0d4ee259c34af2679f8bf4925dfcc.** Exact synthetic microeconomic results and checked primary commercial descriptions. Not measured learning economics, an observed contract experiment, a calibrated forecast, or a selected novel paper claim.

## Research question

Does the deployment choice change when *customer output*, *billable hours*, *target-useful experience* and *cash available for another configuration* are derived from the same contract rather than inserted as independent proxies? This bridges the prior posted-hour RaaS receipts model, the constructive fleet-expansion model, and qualification theory. We explicitly distinguish a given pricing institution from the customer's full feasible alternative.

## Customer and provider

A source customer earns gross revenue R(q)=a q-b q²/2 from accepted output. The best conventional service has marginal cost w and optimized profit G0. A robot with accepted speed s (units per active hour), availability T, resource cost c per active hour and fee u per accepted unit can deliver at most sT output. Here u=h/s under a fixed fee h per *productive hour*, or u=p under an output fee p. The customer chooses one *complete* service (robot or conventional), not a mix. Its robot choice solves q=min(sT,max(0,(a-u)/b)), and it adopts iff its resulting profit is at least G0 (ties favor the robot by convention). The provider refuses strictly negative source operating margin.

With robotic adoption: active hours H=q/s; provider receipts u q, operating resources cH, **net collected provider profit m=u q-cH**. Customer profit plus provider profit equals gross revenue R(q)-cH, so payments are not duplicated as resources. This is not a welfare calculation and assumes no intraperiod cash gap, target-financing advance or unobserved customer labor savings.

The next-date provider budget is B0+m. It chooses **one**: retain cash; pay 8 for incumbent A expansion with incremental provider operating profit 52/5; or pay target B unit cost 3 plus qualification F(e)=max(2,11-tau e). B provider operating profit is derived from a separate customer demand curve R_B(q)=24q-q², supported cost 2q, outside profit 2, qualified capacity 1, and a stipulated 4/5 provider capture share: P_B=76/5. Here e is either accepted source output q or productive source hours H, and source-to-target rights gate its availability. No additional option premium is assigned to experience. If neither profitable investment can be financed, retain cash. These are finite, mutually exclusive investments, not a full portfolio equilibrium.

## Conditional derivations

On a positive adopted interior with slack robot capacity, fixed h>c implies q=(a-h/s)/b and m=(h-c)(a-h/s)/(bs). Therefore

    dm/ds=(h-c)(2h-a*s)/(b*s³).

Above s>2h/a, customer output increases while billable hours and provider profit fall. With per-*hour* useful experience e=H and qualification floor slack, one-target funding slack is D=B0-3-11+(h-c+tau)H; it also declines in this region. For per-*accepted-unit* experience e=q, funding slack instead has derivative [(h-c)(2h-a*s)+tau*h*s]/(b*s³), so additional transferable task exposure can counteract lower billing hours.

For a fixed output price p, q=(a-p)/b is independent of s when capacity is slack. If B is financed and strictly beats A and the qualification floor is slack, per-hour experience makes total source-plus-B value

    p*q + P_B - 3 - 11 + (tau-c)*q/s.

Consequently, with two supported source speeds, higher speed improves value **iff c>tau**, holding customer demand, contract rights, target value and other conditions fixed. If tau>c, the greater qualification savings from useful source-hours dominate saved resource cost, so lower speed yields higher combined value. With per-*output* experience e=q, faster speed instead improves operating margin without changing qualification cost. These are conditional model properties, not an empirical claim that slowing a real robot is optimal or that experience must scale with time.

## Exact normalized demonstration (not dollar estimates)

Source has a=6,b=1,w=3,T=3,c=1. It can operate a given slow configuration s=2 or fast configuration s=4. Both are treated as distinct feasible source opportunities with equal initial fixed costs (not a claim that a faster policy cannot retain the old speed). B0=4 and, initially, e=q, tau=1. The same target and investment menu follows both.

| Contract/configuration | q | H | m | F(e) | B investment feasible? | Next action | Total m + investment gain |
|---|---:|---:|---:|---:|---|---|---:|
| Fixed hourly h=4, slow | 4 | 2 | 6 | 7 | Yes, budget=10/cost=10 | Qualify B | 56/5=11.2 |
| Fixed hourly h=4, fast | 5 | 5/4 | 15/4 | 6 | No, budget=31/4/cost=9 | Retain | 15/4=3.75 |
| Fixed output p=2, slow | 4 | 2 | 6 | 7 | Yes | Qualify B | 56/5=11.2 |
| Fixed output p=2, fast | 4 | 1 | 7 | 7 | Yes | Qualify B | 61/5=12.2 |

The **source ranking reverses** between a posted hourly rate and a matched posted output rate because customer quantity, cash and qualification finance respond together. With ample B0 both hourly paths can qualify, but slow still wins this particular comparison: its extra source margin exceeds fast's target-qualification saving. Stronger capability does not force worse outcomes when the old speed remains optionally usable.

A second falsification holds the output fee at p=2 but sets e=H, tau=2 and B0=5. Both paths fund and choose B; slow's qualification is 7 and combined value 56/5, fast's qualification is 9 and value 51/5. The preferred source reverses *again*. The specified useful-learning unit drives the result. With rights withheld or tau=0, both output-priced paths instead choose incumbent expansion; with a weaker target demand intercept (a_B=16), the transfer-enabled target also loses to incumbent A. No benefit is assigned to raw data with zero usable transition.

## Primary empirical contrast (source reported only)

Formic's **30 August 2023** 3D Machine case describes a FANUC M-10iD tending Mori Seiki and Haas CNC equipment, with manual raw-magazine loading retained. The provider describes a one-year productive-hour fee with performance guarantees and maintenance/remote monitoring. Formic reports ~2,000 production hours in first-half 2023 and +25% capacity, but not exact invoice rates, accepted-output gains, target transferable learning, profitability, financing terms or a quasi-experiment with altered speed. [S1]

A separate Formic trial landing page advertises a *three-month monthly-fee palletizer* ($4,750/month with unlimited usage) alongside its general productive-hour RaaS language. The page date is not established and the trial is **not** the 3D Machine contract. [S2] Mitsubishi HC Capital America separately describes financing services that bundle equipment, software, supplies and service into customer monthly payments, but no specific executed pledgeability or qualification advance is established. [S3]

These show **commercial contract heterogeneity** and a named workflow, *not* estimates of our synthetic parameters. An identification-ready study would join (i) same service/acceptance standard, baseline and customer demand; (ii) measured accepted units, active/idle hours, performance guarantees; (iii) verified invoices, rates, collection dates, service/maintenance cash; and (iv) source data rights and matched target adaptation/qualification effort. Capacity increases are not automatically changes in paid hours or sold output.

## Validation and continuation

From this module directory run:

    python contract_core.py
    python -m unittest -v test_contract_core

**12 compact scoped tests passed locally**, verifying fraction-exact source allocations, participation, choices, target demand ablations, rights, funding, terminal cash, budget monotonicity and old-policy option dominance. A more detailed local version of the model separately passed 20 scoped tests, but only the compact checked module is committed here; historical repository CI was not run. The math is conditional and should be challenged against contingent pricing, minimum service and mixed-fleet operations.

**Next substantive question:** Does a realistic service guarantee or hybrid minimum payment reduce the divergence between private receipts and useful source experience, especially when a shared human supervisor limits effective productive hours? Connect that extension to a second observed workflow end-market, rather than another disconnected finance toy.

**Primary-source references (read 17 November 2026):** [S1] Formic (2023-08-30), https://formic.co/resources/customer-stories/3d-machine-finds-new-competitive-edge-with-automation-partner-formic ; [S2] Formic trial page, undated, https://land.formic.co/3-month-trial ; [S3] Mitsubishi HC Capital America, undated release extract, https://www.mhccna.com/en-us/about-us/press-release/mitsubishi-hc-capital-america-grows-its-financing-automation-service .
