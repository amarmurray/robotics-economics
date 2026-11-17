# From a deployment to an expanding production portfolio

**Research takeover checkpoint · November 17, 2026**

Input accepted research revision: `ef2ef5809eda042903041bac252a52da932da024`.
Status: exact synthetic benchmark and conditional analytical results; not calibrated findings, an established original contribution, or a completed paper.

## 1. Research decision

Keep the prior theoretical reconstructions and financing counterexamples, but make the next constructive model explain a choice among uses of capital: deepen an existing deployment, qualify another configuration, lower the acquisition cost of new units through tooling, or retain cash. Tie the learning value to the destination market's economics, rather than append a strategic-value bonus to data.

This checkpoint develops that decision and an initial source-observation slice. The unpublished/local checkpoint 12 has not been recovered. No claim is made that it was inspected, that the old runtime was stopped in this session, or that these results incorporate it. Work is additive to the accepted revision and does not replace historical files.

## 2. Demand, pricing, and production

Reuse `research/theory/deployment_investment.md` rather than introduce conflicting accounting. In market j, customer revenue is R_j(q)=a_j q-b_j q^2/2, total marginal service/retained-work cost is c_j, and qualified capacity is K_j. Customer monopoly output and a fixed outside option are maintained assumptions, not industry equilibrium.

Let d_j=a_j-c_j. The maximum joint operating profit is:

    q_j(K)=min(K,max(0,d_j/b_j))
    G_j(K)=d_j*q_j(K)-b_j*q_j(K)^2/2
    S_j(K)=max(0,G_j(K)-Pi0_j).

Pi0_j is the customer's profit under its best feasible alternative. Under the inherited two-part tariff the provider receives reimbursed service resources plus fixed fee rho_j*S_j, and net operating profit P_j(K)=rho_j*S_j(K). The customer retains Pi0_j+(1-rho_j)*S_j. When S=0, it uses the outside option. Collections and resource reimbursements are contemporaneous; customer liquidity, procurement delays, competitor responses and intraperiod working capital are not modeled here. These assumptions are limitations, not evidence that those constraints never matter.

The tariff is not fixed-price hourly RaaS. The earlier hourly-receipts note remains a separate contractual comparison. Prices/capture shares here are specified institutions, not a bargaining equilibrium. Operating business surplus is not social welfare.

## 3. Sequence and actual choices

At t=0, choose one of two funded source deployments. Each delivers one unit of current service. Its current customer demand and the same tariff determine collected provider profit M_s. Its source-to-target relationship determines target-useful experience e_s. Equal recorded output need not generate equal target-useful experience.

At t=1, available cash is B=B0+M_s. There is one installed A unit; configuration B is not yet qualified. Choose integer new units n_A,n_B and optional tooling m in {0,1}. Each unit provides one accepted-service capacity unit over the modeled window. No claim is made that these are literal robot-hour measurements.

    F(e)=max(F_min,F_0-tau*e)
    k_A(m)=k_A-m*delta_A
    k_B(m)=k_B-m*delta_B
    I=m*T+k_A(m)*n_A+k_B(m)*n_B+1{n_B>0}*F(e).

Require I<=B. F includes the assumed development/qualification expenditure to enter the second configuration. Its learning response is hypothetical and deterministic; it is not inferred from benchmark performance. Tooling reduces costs only for newly acquired units, not historical fleet spending. This is one explicitly chosen manufacturing investment, not an empirically estimated learning curve or free scale economy.

At t=2, output responds to the resulting capacities. All modeled service obligations end; newly acquired equipment has specified salvage s, zero in the base example and 25% of its acquisition outlay in a sensitivity. Tooling/qualification have zero terminal recovery. Existing assets' unchanged terminal value cancels in comparisons. These finite-horizon assumptions are explicit; an infinite-lived fleet is not valued by dropping its continuation obligations.

Relative to retaining the installed fleet, optimize:

    gain = P_A(1+n_A)-P_A(1)+P_B(n_B)-I+salvage.

The source decision maximizes M_s+max(gain). The initial B0 and unchanged installed-fleet operating profit are omitted constants, not lost cash. Every dollar retained remains in terminal cash; no additional option premium is added. The solver enumerates the complete finite feasible set implied by the budget and positive new-unit costs. This is a finite single-provider optimization, not a decentralized equilibrium.

## 4. An exact entry condition with the alternative use of cash

Suppress tooling and let salvage be linear per new unit. Define H(B) as the maximum incremental value from A-only investment with cash B. For y>=1 new B units, let I_B(y,e)=F(e)+k_B*y, and J_B(y,e)=P_B(y)-I_B(y,e)+s_B*y.

The best value of entering B is:

    max_y [ J_B(y,e)+H(B-I_B(y,e)) ],
    where I_B(y,e)<=B.

Entry strictly dominates staying with A iff some feasible y satisfies:

    J_B(y,e) > H(B)-H(B-I_B(y,e)).

Proof: fix y, subtract its required cash and optimize the remaining A investments. Compare that sum with H(B), then maximize over feasible y. Equality is indifference, not a mandatory entry prediction.

The right-hand side prices the best A investments displaced by entry. A positive standalone B project need not justify entry. This is standard capital-allocation reasoning expressed in the deployment model, not a novelty claim. The useful research target is measuring the destination market and transfer relationships that move this boundary.

A demand-side no-entry bound follows with zero salvage. Define maximum possible B operating profit:

    Pbar_B=rho_B*max(0,max(0,d_B)^2/(2*b_B)-Pi0_B).

If Pbar_B<=F(e)+k_B, no B investment can strictly beat A-only investment: every y>=1 costs at least F(e)+k_B, P_B(y)<=Pbar_B, and H(B-I)<=H(B). Transfer cannot create an attractive market solely by supplying more data; the maximum capturable destination surplus matters.

## 5. Exact constructive example

All quantities below are normalized synthetic units, not prices, robot counts or estimated returns. All fractions are calculated exactly in the attached implementation.

Existing A: a=18,b=2,c=2,Pi0=10,rho=4/5,initial capacity=1. Its baseline provider profit is 4. New B in the base comparison: a=20,b=2,c=2,Pi0=2,rho=4/5. Unit acquisition costs are k_A=6,k_B=3; F0=8,F_min=2,tau=6. Initial extra cash B0=4. Base tooling is disabled and salvage is zero.

The cash-rich source has a=13,b=2,c=2,Pi0=0,rho=4/5,K=1, so q0=1 and M=8. Its target-useful experience is zero. The transfer-rich source has a=21/2 and otherwise the same current service parameters, so q0=1 and M=6. Its target-useful experience is one. This directional difference is stipulated, not measured.

| Source | Collected cash M | Cash for investment | B qualification cost | Optimal new A/B units | Investment | Value added, M+gain |
|---|---:|---:|---:|---|---:|---:|
| Cash-rich | 8 | 12 | 8 | 2 / 0 | 12 | 76/5 = 15.2 |
| Transfer-rich | 6 | 10 | 2 | 0 / 2 | 8 | 22 |

The second choice earns less now, but makes expansion into a commercially valuable destination cheaper. It retains two units of cash instead of spending the entire budget. No arbitrary premium is paid for its data. Both current and future customer output are optimized under the stated tariff.

Mechanism tests are decisive:

| Change | Selected source | Interpretation |
|---|---|---|
| Base | Transfer-rich | Qualified expansion recovers the sacrifice in current cash. |
| No cross-source cost reduction, tau=0 | Cash-rich | More labels or experience alone confer no payoff. |
| Weaker B demand, a_B=12 | Cash-rich | The same experience is less valuable when destination economics are weak. |
| No second configuration allowed | Cash-rich | Existing-fleet scaling alone does not justify this source sacrifice. |
| Tooling option T=2, savings 2 on A and 1 on B | Transfer-rich | It selects tooling plus three B units; value added 152/5=30.4. |
| 25% new-equipment salvage | Transfer-rich | Result survives this explicit terminal-value alternative. |
| Initial cash 100 | Transfer-rich | Result is not solely an inability to pay; real development-cost savings still matter. |

This example establishes a conditional comparison, not a universal rule to sacrifice near-term profit for learning. Stronger technical evidence, customer economics and credible alternative contracts must determine any practical conclusion.

## 6. More capital can deepen rather than broaden production

Keep A unchanged, reduce B's revenue intercept to a_B=12, set experience to one (qualification cost 2), and disable tooling and salvage. Optimize new investment for three different budgets:

| Available cash | New A units | New B units | Gain versus retaining installed A |
|---|---:|---:|---:|
| 5 | 0 | 1 | 3/5 |
| 6 | 1 | 0 | 22/5 |
| 11 | 1 | 1 | 5 |

At budget 5, an additional A unit is unaffordable and a small B expansion is worthwhile. At 6, A expansion becomes feasible and dominates B. At 11, both are selected. The objective value increases throughout, but entry into B is not monotone in cash. These are alternative investment decisions from the same initial state, not a claim that a firm abandons an already-built B fleet when cash arrives.

Proof is by complete enumeration of the finite investment sets, with exact rational payoffs. This is a counterexample to a monotone-breadth claim, not a novel general theorem: indivisibility and competing uses of capital already supply the underlying mechanism. It motivates distinguishing greater deployment depth from wider task/market coverage in the empirical atlas.

## 7. Source-observation slice: what can and cannot be joined

The accompanying `evidence.json` preserves four primary source readings and six typed relationships. It is an initial evidence slice, not the completed sector/workflow atlas.

- Open X-Embodiment's project page reports pooled robotic experience and positive cross-platform transfer in evaluated policies. This supports investigating transfer; it does not measure our qualification-cost slope, industrial acceptance or customer returns. [S1]
- Re-Mix studies training-data mixture choices and downstream policy performance. This motivates distinguishing useful data composition from raw volume; no result here is converted into an adaptation-cost or revenue coefficient. [S2]
- Mitsubishi HC Capital America's Formic release describes a commercial partnership and a managed automation service including design, equipment, deployment and support. That is issuer-reported organizational evidence, not verified project-level cash flows or learning effects. [S3]
- Jeon's capacity-expansion paper is directly relevant prior art on investment timing/size, learning and time-to-build. This checkpoint reads the abstract and introductory framing, not a full proof replication. Its existence cautions against claiming that sequential learning-dependent capacity choice is itself new. [S4]

These are separate observations. There is no evidence here that Formic uses RT-X or Re-Mix, that a laboratory transfer result reduced a Formic qualification bill, or that an announced financing agreement funded a particular model update. Those connecting relationships remain unknown, not zero.

## 8. Verification and limits

Run with Python 3.10 or later; no external package is required:

    python expansion.py --output results.json
    python -m unittest -v test_expansion

Eighteen scoped tests passed in this session. They cover the exact example and ablations, source cash derivation, customer participation/saturation, budget and free-learning value monotonicity, manufacturing-option dominance, the analytical entry decomposition, cash/terminal-asset reconciliation, no upfront use of salvage, input validation and deterministic result regeneration. These are newly run checks for this module only. Historical repository tests and independent peer review are not claimed.

The model does not yet endogenize the knowledge-production function, qualification uncertainty or time, a continuous embodiment design space, a full manufacturing learning curve, competing firms' responses, a network of legal payers, customer liquidity, nonexclusive task capacity, or a recursively evolving general production network. The two-part tariff and perfect foresight need alternatives. The nonmonotone-entry example relies on indivisible investments. Neither example establishes a causal empirical estimate or publishable novelty.

The next theory step is to replace the stipulated experience-to-cost transition with a small capability/qualification model and a measured source-target comparison, while retaining customer demand and the investment menu. The next empirical step is a focused capability–workflow–customer map with explicit unknown costs and alternative production methods. Do not reopen an unlimited prior-art search before producing that joint theoretical/empirical contrast.

## Sources

[S1] Open X-Embodiment Collaboration, project page, abstract/model overview; retrieved November 17, 2026. https://robotics-transformer-x.github.io/

[S2] Hejna et al., Re-Mix: Optimizing Data Mixtures for Large Scale Imitation Learning, arXiv:2408.14037; abstract and introduction read November 17, 2026, not a full replication. https://arxiv.org/abs/2408.14037

[S3] Mitsubishi HC Capital America, Mitsubishi HC Capital America Signs Agreement with Leading Robots-As-a-Service Provider; release page read November 17, 2026. The page does not expose a publication date in the retrieved text; do not treat retrieval as announcement date. https://www.mhccna.com/en-us/about-us/press-release/mitsubishi-hc-capital-america-signs-agreement-leading-robots-service

[S4] Haejun Jeon, Time-to-build and capacity expansion, Annals of Operations Research 328, 1461–1494 (2023), DOI 10.1007/s10479-023-05413-3; abstract/introduction read November 17, 2026. https://link.springer.com/article/10.1007/s10479-023-05413-3
