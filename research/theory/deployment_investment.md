# Deployment cash, customer demand, and the next capacity investment

Theory phase checkpoint 1. All numerical values here are **synthetic normalized units**, not calibrated dollars, hours, robot counts, or forecasts. The result is a diagnostic for a potential paper, not a novelty claim. The closest generic prior mechanism is constrained dynamic investment: invest when attainable continuation gains exceed cost. The open research contribution concerns how production, transfer, and payment relationships jointly determine those attainable gains.

## Model A: service and the customer's outside option

One customer sells accepted output q into inverse demand `p(q)=a-b*q/2`, with a>0 and b>0. Thus revenue is `R(q)=a*q-b*q^2/2`. This is customer monopoly output choice with rival responses held fixed, not an equilibrium of competing robotics firms. Parameter a is the revenue intercept; b is the magnitude of the revenue curvature, twice the inverse-demand slope. Quantity responds to service cost and available capacity.

Let c be the full marginal resource cost of accepted service, including retained work and support, and K the qualified capacity within a single service window. Gross operating profit available to the customer/provider pair is

`G(a,c,K)=max_(0<=q<=K) [(a-c)q-b*q^2/2]`.

Define `d=a-c`, `q*=min(K,max(0,d/b))`; then `G=d*q*-b*q*^2/2`. The customer's best feasible alternative earns Pi0 over the same window, including its own costs and constraints. Incremental joint operating surplus is `S=max(0,G-Pi0)`, with the customer retaining its alternative when G<Pi0. Pi0 cannot be replaced by the wage associated with one robotic task. G and S are business operating surplus, **not total welfare**; consumer surplus is excluded.

A two-part service tariff reimburses marginal service cost c*q and charges fixed fee `T=rho*S`, for `0<=rho<=1`. With participation and sufficient liquidity, the customer chooses q* and retains `Pi0+(1-rho)S`; the provider receives net operating profit rho*S. Total fee is c*q+T; c*q is not provider profit. The tariff is a transparent implementable allocation assumption, not a bargaining solution. When the customer's own retained work is paid directly, subtract that component from the provider reimbursement and preserve it in total c; the consolidated quantity decision is unchanged.

We assume contemporaneous customer collections/cost reimbursement so no intraperiod working-capital deficit arises. Relaxing this or imposing a customer budget may invalidate the tariff. Hourly RaaS with fixed hourly prices is not equivalent: faster service can reduce billed hours at fixed output. Output-based, hourly, and minimum-commitment contracts belong in a later comparison if they change the result.

## Model B: two deployment paths and a binary expansion

At t=0 the provider must choose one of two feasible deployments i in {H,L}. Both are available with the same initial resources and information. Their complete initial services generate net collected cash m_i after all period-zero obligations. Setup working capital is assumed already funded equally. This reduced-form m_i must ultimately be derived from matched contracts/service accounts; it is not an empirical estimate. A no-new-deployment alternative with no gains can be added and is dominated in the numerical example.

The deployment generates a known state `(a_i,c_i,K)`: customer access changes a_i, and eligible, validated directional learning changes c_i. Learning about uncertainty is absent; these are deterministic technology transitions assumed known at choice time. Raw data volume earns no separate payoff. The right to use data is a gate on the cost transition, not an additional asset premium.

After collecting m_i, choose x in {0,1}: pay I at t=0 to increase next-window supported capacity from K to K+Delta. This can represent a delivered, qualified configuration expansion; it is not yet endogenous embodiment design or manufacturing learning. A failed or late qualification makes effective Delta=0 while still charging I. Existing assets have no resale value in this two-window abstraction, and all support obligations end with the modeled service. A longer-lived fleet requires explicit salvage and outstanding obligations, not silent truncation.

Initial provider liquidity is B. A permitted, riskless bridge lender may supply f up to Fbar. At unit discount factor and zero interest, lender cash is -f at t=0 and +f at t=1. Investment is feasible only if `B+m_i+f>=I` and terminal repayment is feasible. The provider's terminal cash is `B+m_i+f-I*x+rho*S_i(K+Delta*x)-f`. Loan principal cancels from lifetime value, **not** from the date-zero cash constraint. No lender is assumed available unless that policy scenario permits one. All comparison policies face the same credit limit.

At zero interest and discounting, value net of initial B is

`W_i=m_i+rho*S_i(K)+max(0,rho*[S_i(K+Delta)-S_i(K)]-I)`,

where the max includes investment only when funded and repayable. More generally put beta on continuation profits, but then explicitly price loan timing; the numerical result uses beta=1. Retaining liquidity is x=0. The optimum chooses the highest feasible W_i. This is a finite single-provider decision problem, not decentralized industry competition.

## Conditional investment threshold and switching result

For Pi0=0 and `d_i>=b*(K+Delta)`, both capacity levels bind. Direct subtraction gives

`Delta S_i = Delta*(d_i-b*K)-b*Delta^2/2`.

Therefore investment is privately worthwhile precisely when

`d_i >= b*K+b*Delta/2+I/(rho*Delta)`

for rho>0, Delta>0, **and** financing/repayment is feasible. Equality gives indifference. This is necessary and sufficient only inside the stated binding-capacity regime. Outside it, use exact q*; if K already serves unconstrained demand, expansion has zero value. For Pi0>0, participation can introduce a threshold and the positive-part formula must be retained.

Proof: maximize a strictly concave quadratic over a compact interval; substitute its constrained optimizer at both K values; subtract; multiply by rho and compare with I. Feasibility is a separate restriction. The calculation does not establish that any particular capacity investment meets these assumptions.

Let `A_i=rho*S_i(K)` and `E_i` be the feasible nonnegative net expansion gain. L overturns the current-cash ranking m_H>m_L iff

`A_L-A_H+E_L-E_H > m_H-m_L`.

This identity is the exact comparison, not the proposed original contribution. The binding-regime threshold shows how demand and capturable surplus enter it. A larger learning improvement or access intercept raises the investment return only until demand is saturated. A fixed fee capture share can leave a socially or jointly worthwhile capacity expansion privately unattractive.

## Exact synthetic reversal with payer-specific finance

Set b=2, K=1, Delta=1, I=3, rho=4/5, B=0, Pi0=0, beta=1. H generates m_H=8 and state `(a_H,c_H)=(8,4)`. L generates m_L=2 and `(a_L,c_L)=(12,2)`. Relative to H, L supplies a four-unit access increment and a two-unit validated cost reduction. These increments are assumptions, not causal estimates. Integer units here refer to service capacity, not digital copies or physical headcount.

| Path | Current cash | G at K=1 | G at K=2 | Net expansion gain | Best value without credit | Best value with Fbar=1 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| H | 8 | 3 | 4 | -11/5 | 52/5 = 10.4 | 52/5 = 10.4 |
| L | 2 | 9 | 16 | 13/5 | 46/5 = 9.2 | 59/5 = 11.8 |

Without credit, L cannot pay I=3 even though its continuation gain exceeds cost; H is optimal. With the same one-unit credit access available to both paths, L borrows one, invests three, earns provider continuation profit 64/5, and repays one; terminal net cash is 59/5. H declines expansion. The lender earns zero in this deterministic illustration. Liquidity moves the optimal first deployment although the engineering and demand transitions are unchanged.

At L's expanded quantity q=2, final-output revenue is 20, service resource cost is 4, operating surplus is 16, provider fixed fee/profit is 64/5, total service payment is 84/5, and customer profit is 16/5. The lender's principal is not another operating resource cost or another benefit. Investment expenditure I is paid separately at t=0 and treated as real acquisition cost; the recipient's internal production/margin is outside this deliberately narrow business-accounting boundary. No social-welfare estimate is inferred from the provider's value.

## Challenges that change the result

1. **No validated learning/transfer:** set c_L=4 while retaining its access. L's best funded value becomes 43/5=8.6; H wins. Rights failure has this effect only because rights gate this specific transfer in the model.
2. **No access improvement:** set a_L=8, retaining c_L=2. Expansion is unprofitable and L's value is 6; H wins.
3. **Demand saturation:** if d<=b*K, additional capacity has no operating value even with cheap finance. Centrality or data richness alone cannot rescue it.
4. **Misaligned collection:** if the m_i cash is held by a customer affiliate without an enforceable provider transfer, it cannot fund provider I. Consolidating that balance would falsely make L feasible. Organizational ownership by itself is not a permission to transfer funds.
5. **Complementarity:** if entry requires both qualification and physical delivery, neither isolated investment may open any output. The additive capacity formula is then wrong; Model C needs a joint eligibility constraint.

The current result survives exact enumeration, but depends on observed-at-choice deterministic transitions, fixed capture, timing, and a very simple demand specification. It does not yet beat generic constrained-investment theory as a research contribution. A useful next test is whether **the same measured production adjacency but different learning and payment edges** yields distinguishable sequencing predictions after credible outside options and contract costs are held fixed.

## Replication and evidence bridge

Run `python -m model.theory_deployment` to regenerate `model/results/theory_deployment.json`; run `python -m unittest tests.test_theory_deployment`. The small kernel is an analytical toy distinct from the existing enterprise execution models. It neither replaces their accounting nor imports their synthetic parameters as evidence. Historical results are preserved.

The empirical contrast in [the phase charter](../../THEORY_PHASE.md) asks whether transfer/qualification and payer funding can be observed independently. The [source reconstruction](organizing_intelligence.md) supplies the physical-replication boundary; it does not supply the cost or demand increments in this example.
