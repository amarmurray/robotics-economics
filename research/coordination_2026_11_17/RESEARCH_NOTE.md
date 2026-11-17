# Q4 — Human attention as a productive bottleneck: fleet expansion versus digital coordination

**Executed November 17, 2026; accepted input `668de875796edd1a50f6b90667c1124f682d859b`.** Model, proof, synthetic counterexamples, primary-source comparison and measurable falsification design. The numbers below are normalized hypothetical values, **not measured intervention rates, fleet economics, safety performance, or a calibrated industry forecast**. No first-paper novelty or full equilibrium claim is made.

## Research decision

A central question arising from *Organizing Intelligence* is whether improved coordination changes the optimal scale of productive capital rather than merely the competence of each unit. In a physical fleet this requires an actual constraint: robots may be qualified to operate but periodically require scarce human attention, intervention, diagnosis or recovery. Buying another robot changes the arrival rate of those requests; improving digital coordination changes their frequency or resolution; buying more human supervision changes response capacity. The value of each action must then pass through the **customer's demand for accepted output** rather than through installed-fleet count.

The research contribution attempted in this tranche is a concrete analytical and numerical separation of (a) **technical complementarity** between hardware and coordination, from (b) **financial complementarity** after declining customer marginal value and capture are included. The interaction changes sign with demand even though the technical interaction does not. This is a conditional constructive model, not evidence that generic queuing-network complementarity is new economic theory.

## Environment and exact stationary capacity

A fleet has `N` qualified, otherwise identical physical units. When active, each requests a blocking intervention with Poisson hazard `lambda` per active unit-time; the robot remains inactive until resolved. There are `c` parallel supervisors with exponential service rate `mu` per supervisor. An inactive robot cannot generate another request. Assume independent hazards and services, no priority or safety-compelled preemption, work always available, and stationary rates over a long-enough observation window. Field repair, charging, scheduled maintenance, and nonblocking software diagnostics are **not** silently folded into this particular hazard.

Let `k in {0,...,N}` be the number of interrupted robots. The birth and death rates in the finite-source Markov repair process are

    b_k=(N-k)*lambda,   d_k=min(k,c)*mu.

Detailed balance gives the exact stationary weights

    w_0=1, w_k=w_(k-1)*(N-k+1)*lambda/[min(k,c)*mu],
    pi_k=w_k/(sum_j w_j).

With `r` accepted-output units per active robot-time, the **expected productive capacity** is

    K(N,lambda,mu,c)=r*[N-sum_k k*pi_k].

Stationary flow conservation gives

    lambda * E[N-k] = mu*E[min(k,c)] <= c*mu,
    hence K <= r*c*mu/lambda for lambda>0.

For fixed positive lambda, fixed c and mu, the probability that all supervisors are busy approaches one as N grows; thus the expected number of active robots approaches `c*mu/lambda` and marginal extra hardware eventually adds arbitrarily little output. This is an elementary **finite-source queue repairman ceiling**, not a new theorem. It is not an industry-wide limit: more supervisors, better autonomy, different exceptions and site/task arrangements change it. In the limiting case lambda=0, K=r*N.

The interruption queue is a **specific mechanism** for coordination, not a rebranding of all fleet orchestration. Other mechanisms include task assignment, ERP/warehouse integration, charging slots, narrow aisles, shared tools, safety interlocks, network reliability and customer demand. Those warrant separate constraints or networks when they change a decision.

### Customer economics and investment menu

Keep the earlier program's customer monopoly benchmark and complete-service alternative. For a customer with gross revenue `a*q - b*q²/2`, full noninvestment operating resource cost `v*q`, outside operating profit `Pi0` and output capacity K, let

    q*(K)=min(K,max(0,(a-v)/b))
    G(K)=(a-v)*q*(K)-b*q*(K)^2/2.

If G(K) <= Pi0 the customer uses its alternative. Otherwise the provider earns `P(K)=rho*(G(K)-Pi0)` under the established two-part surplus-sharing fee, and the customer retains `Pi0+(1-rho)*(G(K)-Pi0)`. The provider is assumed reimbursed for current service resources, so `P` is net operating profit **before** separately modeled investment costs. The policy is assumed enforceable with contemporaneous collections; this is not a posted hourly RaaS tariff or bargaining solution. The customer bears no unmodeled forced adoption. Gross business profit is not social welfare.

The provider has cash budget B and may choose (each binary): hardware `H` adding one N at price I_H, a digital intervention-reduction investment `D` changing lambda to `theta*lambda` (0<theta<=1) for cost I_D, or another human supervisor `S` changing c to c+1 at a fully paid period cost I_S. Combinations are feasible only if their **sum** of cash requirements fits B. Supervisor incremental wage/support is prepaid or reserved for the modeled window; no employee disappears when a robot is down. All costs and benefits are for a single matched period; zero salvage is explicit. A baseline existing supervisor is included in `v` or sunk common resources, not counted again as an incremental outlay.

For action x, optimize `P(K_x)-P(K_0)-I_x` over funded actions, including doing nothing. A digital change in intervention hazard is an assumption about automation/reliability and must not be inferred from an observed reduction in human interactions without observing accepted output and safety.

## Conditional choice comparisons

For all four configurations (baseline, H, D, H+D) that **remain adopted and capacity-binding**, let `d=a-v` and define `delta_X=K_X-K_0`. Then

    Delta P_X = rho * [(d-b*K_0)*delta_X-b*delta_X^2/2]

for investment X that changes capacity. With no fee differences except explicit I_X, digital beats additional hardware exactly when

    rho*[G(K_D)-G(K_H)] > I_D-I_H,

subject to both being fundable, the baseline/adoption regime and any alternative such as S or H+D. One cannot infer the ranking from `delta_X` alone when prices, constraints or demand vary.

### Physical complementarity can coexist with economic substitution

Define cross-interaction capacity

    C_K = K_HD-K_D-K_H+K_0.

If C_K>0, the marginal productive contribution of hardware is *larger* after digital intervention reduction—technical complementarity in this model at that parameter point. Yet the provider's **economic** cross-interaction, with additive cash costs cancelling, equals

    C_P = rho * [ d*C_K - (b/2)*(K_HD²-K_D²-K_H²+K_0²) ].

Assuming positive rho and C_K, its sign changes at

    d*=(b/2)*(K_HD²-K_D²-K_H²+K_0²)/C_K,

provided *all four* states satisfy adopted, capacity-binding demand. Below that threshold the actions can be productive complements but **private-value substitutes**; above it they can be complements in both senses. The sign result is an algebraic comparison, not a general theorem that C_K is always positive. Outside options, partial adoption, nonlinear costs, shared supervisor wages and nonbinding demand can break the formula. The threshold is not a calibrated boundary or a policy target.

An exact rational example with N=3, lambda=1/2, mu=1, c=1, theta=1/2, r=1 produces

    K0=30/19; KH=38/21; KD=156/71; KHD=284/103;
    C_K=961508/2917887 > 0; d*=4243593611144/701392923399 (~6.0502).

With b=2, rho=4/5 and no outside-option binding, `d=23/4=5.75` meets all capacity-binding conditions and yields `C_P≈-0.07915`. At d=8, the exact same technologies and interventions yield `C_P≈+0.51399`. Thus **the topology of physical complementarities does not determine the topology of profitable joint investments**. The customer-demand layer can reverse it.

## Synthetic decision comparison under equal capital needs

For N=4, one supervisor, mu=1, r=1, digital halves lambda, and a customer with a=18,b=2,v=2,Pi0=5,rho=4/5, set I_H=3,I_D=3,I_S=5 and B=6. Cost units are arbitrary and the chosen event rates are not empirical.

| Case | Initial expected productive capacity | Best funded action | Net incremental provider value |
|---|---:|---|---:|
| Relatively rare interruptions, lambda=1/10 | about 3.533 | Add one hardware unit | about +2.364 |
| Frequent interruptions, lambda=1/2 | about 1.810 | Digital improvement **plus** hardware | about +6.254 |
| Frequent interruptions but B=3 | about 1.810 | Digital improvement alone | about +5.669 |
| Low customer demand (a=5, otherwise as above) | about 1.810 | Retain cash | 0 |
| Provider capture rho=1/10 | about 1.810 | Retain cash | 0 |

The combined high-interruption action illustrates that coordination and hardware need not be mutually exclusive investment types: it can be optimal to buy the software improvement *and* an additional unit. Separately, even a large physical improvement is not valuable if customer output cannot be sold, the customer rejects the service, or the provider cannot capture adequate surplus.

The extra-human-supervisor option is explicitly evaluated, not treated as costless digital coordination. In the high-interruption synthetic regime it produces positive value but loses to the stronger digital/hardware combination under the specified costs and cash. If the digital intervention reduction is unavailable, adding a supervisor can become optimal. This is not evidence that a real robot operator should eliminate supervisors.

## Source-grounded contrasting workflows (what is observed)

The accompanying `evidence.json` separates reported workflow roles from unknown intensity and costs.

**Serve Robotics—sidewalk delivery.** Its Form 10-K for fiscal 2025 (filed 2026-03-12, SEC-hosted) describes fleets monitored through video/mobile connectivity by remote human supervisors who intervene when navigation needs assistance; physical incidents sometimes require local field dispatch. Merchant staff load a package; customers retrieve it at delivery. The same filing describes multiple simultaneous deliveries being overseeable by one supervisor as an operational motivation for autonomy. This establishes a **shared-attention workflow** and retained roles, not a measured Poisson hazard, supervisor service rate, expected stationarity, intervention cost, safety SLA or revenue per active hour. [S1]

**Agility Robotics—Digit industrial operations.** Agility's public FAQ, read 2026-11-17 and not reliably dated, describes autonomous operation inside predefined production workflows, fleet cloud integration with WMS/MES through Arc, provider-side monitoring, diagnostics and maintenance, while teleoperation is described only for setup mapping or offsite R&D. This is a **different role for human attention**, not a measured analogue to Serve's remote sidewalk interventions. Digit's safe-workcell requirements also bound the production topology. [S2]

**Hoque et al.—ThriftyDAgger.** The peer-reviewed 2022 CoRL/PMLR paper gives a specific mechanism for human intervention-budget gating, and reports a controlled three-robot user study (10 participants) with improved performance and lower supervisor burden relative to a study comparator. The study is about interactive imitation learning and selected tasks; it cannot calibrate delivery exceptions, industrial uptime or our chosen lambda and theta. [S3]

These are distinct empirical settings, not three independent estimates of one universal supervisor-to-robot ratio. In particular, remote navigation assistance, offsite data collection, maintenance repair, workflow dispatch and safety supervision must not be collapsed into the same server.

## Empirical design: what would identify the economic coordination threshold?

For each supported configuration–workflow–site–time cohort, the desired panel records:

1. **Exposure:** on-task qualified robot-time by unit and software version, task accepted and task arrivals, intervention opportunities and incident categories; distinguish active from waiting, paused, charging, maintenance and offsite training.
2. **Supervisor load:** dispatch timestamp, assignment, human engagement, resolution timestamp, simultaneous competing requests, retries, offsite versus field response, paid supervisor hours, required standby/coverage and safety minima.
3. **Accepted customer service:** accepted output and quality, complete workflow throughput, downstream capacity and market demand, retained human work, alternative provider/process, contract pricing and billed versus productive hours.
4. **Investment and rights:** software update cost and timing, new units and qualification dates, supervision and support cost, permitted data access/transfer, reimbursement/financing and which legal entity pays and collects.

One can estimate arrival intensity conditional on active exposure, time-to-resolution, queue waiting conditional on concurrent load, and the actual effect of coordination changes on accepted output. Tests should match safety/service standards and control for changes in tasks, site geography, fleet assignment, dispatch policies, software versions and customer demand. An update event is not randomly assigned; regression of reported uptime on deployment size alone cannot identify congestion or digital improvement. If arrivals are correlated, breakdowns are physical rather than remote, priority rules bind or requests do not block productive operation, the present finite-source Markov model can fail outright. Those failure modes are research findings worth measuring.

**Useful negative controls:** an automated exception that never reduces output should not count as blocking λ; an offsite teleop demonstration should not count as a customer-operations supervisor recovery; a raw remote-assistance count cannot proxy accepted throughput without exposure and duration. Payer-specific support costs must be reconciled with service fees and avoided customer work; no duplicated labor savings or phantom wages.

## Relationship to the paper and ongoing research

This result operationalizes the competence/coordination distinction from *Organizing Intelligence* without reproducing its unconstrained digital-firm size model. It joins the preceding manuscript's billing-unit and learning-exposure work to an explicit **shared productive-resource constraint**. It also produces a falsifiable empirical design: the sign and location of hardware-versus-coordination ranking changes require measured intervention exposure, duration, output value and costs—not fleet count or benchmark accuracy.

The result is an informative structural example; the finite-source queue and cross-difference algebra are standard ingredients. Prior research on machine repairman queues, finite-source polling/repair models and real production networks is relevant, and the first-paper novelty decision remains open.

**Next bounded tranche:** join demand and coordination under different contract payment units and a measured-style workflow panel, or advance manufacturing/capital Q5 with a small precise result while independently developing the missing BEA industry backbone. Do not begin another unbounded literature search or build a new dashboard from this checkpoint.

## Replication

Python standard library only. From this directory:

```sh
python -m unittest -v test_coordination
python coordination.py --output results.json
```

`results.json` is deterministic and stores exact rational numbers as well as readable decimals. 25 scoped tests passed, including finite-source detailed balance, conservation, budget/option monotonicity, conditional cross-effect signs and exact choices. Code/results are synthetic; the historical repository suite and an independent external replication were **not** run. The code assumes an otherwise identical robot fleet, stationary blocking exceptions, exponential services, full-information investment and quadratic customer demand. It does not simulate safety-critical operation.

### Primary sources (read November 17, 2026)

- **[S1]** Serve Robotics, fiscal 2025 Form 10-K, SEC HTML, filed March 12, 2026. *Robot Operations* and *Level 4 Autonomy*. https://www.sec.gov/Archives/edgar/data/1832483/000183248326000010/patr-20251231.htm
- **[S2]** Agility Robotics, public FAQ: *Who handles day-to-day operations?*, *Is Digit autonomous or driven by a human?*, *How do commercial humanoids work with WMS/MES?*, *Digit's workcell*. No page publication date established. https://www.agilityrobotics.com/faq
- **[S3]** Ryan Hoque et al., *ThriftyDAgger: Budget-Aware Novelty and Risk Gating for Interactive Imitation Learning*, Proceedings of CoRL/PMLR 164 (2022), pp. 598–608, abstract and publisher citation examined. https://proceedings.mlr.press/v164/hoque22a.html
