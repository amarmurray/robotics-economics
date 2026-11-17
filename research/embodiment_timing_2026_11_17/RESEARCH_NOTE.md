# Hardware redesign versus software adaptation under expiring customer demand

**Research tranche, November 17, 2026.** Based on assistant branch `bee49a9d66bf09f5bee50692f7cb44c17147e029`. All prices, probabilities, periods, equipment capacities, qualification functions and cash values are **synthetic normalized assumptions**. Nothing here is a measured robotics return, reliability certificate or selected novel contribution.

## Economic problem and architecture

The prior qualification model makes adaptation cost depend on the profile of service-relevant weaknesses. This tranche adds an investment alternative: (i) expand the incumbent service, (ii) qualify an existing embodiment for a second customer market through software adaptation, (iii) redesign and then qualify a different embodiment for that market, or (iv) retain capital. A changed embodiment may reduce an irreducible failure component or increase qualified capacity, but imposes development time. The target market's customer demand continues evolving while hardware is unavailable.

This is a **post-source-deployment** investment decision. Source deployment has generated a given cash budget and candidate profiles; the upstream choice is not solved again. A t=0 capital commitment must be paid with existing cash. Contracts, learning response and qualification times are known in this deterministic benchmark. The three investments are mutually exclusive, one new physical unit per project. Existing installed capacity and its base receipts cancel. The comparison does not model fully simultaneous portfolio expansion or competitive industry equilibrium.

Customer operating revenue is `R_j(q,t)=a_j(t)q-b_j q²/2`; full resource cost is `c_j q`; the best feasible alternative gives profit `Pi0_j`. Under the *inherited*, explicitly assumed, two-part resource reimbursement plus surplus-sharing contract, the customer chooses quantity subject to supported capacity `K`. Provider operating receipts are `P_j(K,t)=rho_j max(0,G_j(K,t)-Pi0_j)`, where `G_j` is maximum gross operating profit at that capacity. Nonpositive surplus triggers the outside option. In B, `a_B(t)=a_B(1)-gamma(t-1)`: exogenous time variation in final-demand conditions, but quantity and provider receipts respond endogenously. This does **not** yet solve demand feedback from economy-wide robot adoption.

Project j spends `I_j` upfront, makes `K_j` supported capacity available only after lag `l_j`, and may recover acquisition salvage `s_j` at the end of period T. Incremental value relative to retained cash is

`V_j = -I_j + sum_(t=l_j+1)^T beta^(t-1)*P_j(K_j,t) + beta^(T-1)*s_j.`

For incumbent expansion use the **increment** `P_A(K_A+1,t)-P_A(K_A,t)`, not its full gross receipts again. Choose the maximum nonnegative value among projects satisfying `I_j<=B_0`. Salvage affects terminal value but **never** upfront feasibility. This is provider accounting, not social welfare. Project lags are deterministic, not fitted duration distributions.

## Qualification links hardware to an economically meaningful service

The software option retains the old two-component configuration, unit capacity 1 and no development lag. The redesigned option alters the hard component's failure floor from .012 to 0 and raises its adaptation response rate from 1 to 2; it supplies capacity 3 after two development windows. All components use the **same epsilon=.02 conservative whole-service failure bound**, the same independently stipulated 2-unit verification cost, and the previously checked `qualification.py` cost-minimization solution. The synthetic old and redesigned qualification bills, rounded *up* to .01 cash unit, are **19.91 and 9.56**. One new unit costs 3 in either path; redesign additionally incurs 8 in fixed engineering expenditure. Thus `I_software=22.91` and `I_redesign=20.56`. This intentionally favorable redesigned cost case is *not* a claim that hardware upgrades are usually cheaper; the effect of additional lag and weakening customer economics is what is being isolated.

The prior model supplies a second, sharper distinction: if irreducible failure floors sum to at least epsilon while reducible failures remain, software adaptation cannot meet this particular conservative union-bound rule with finite effort. Redesign that reduces the floors may reopen modeled eligibility, subject separately to financing and demand. The rule is sufficient rather than necessary, so failure to satisfy it does **not** prove physical service is impossible.

## Conditional threshold—analytical result, not general novelty

Assume beta=1, zero salvage, the same B operating cost, capture share and outside option across configurations. Suppose each customer chooses the project's full capacity in every active period and B's incremental surplus is strictly positive. Then

`P_B(K,t)=rho_B[(a_B(1)-c_B)K-b_B K²/2-Pi0_B-gamma(t-1)K].`

Write `D(gamma)=V_redesign(gamma)-V_software(gamma)`. Subtraction gives

`D(gamma)=D(0)-rho_B*gamma*[K_R sum_(t=l_R+1)^T (t-1)-K_L sum_(t=l_L+1)^T (t-1)].`

When the bracket is positive the redesign advantage falls linearly with demand erosion, so its candidate pairwise crossing is the zero of this expression. **The capacity-binding and participation inequalities must be independently checked at that crossing**. Outside that region, the expression becomes piecewise and a crossing may disappear. Better design is not guaranteed to lose more from delays in other settings: its capacity, timing and customer economics jointly determine exposure.

For four service windows, `K_R=3`, `l_R=2`, `K_L=1`, `l_L=0` and `rho=.8`, the bracket is `3*(2+3)-1*(0+1+2+3)=9`. Hence the slope is `-36/5=-7.2`. The checked synthetic intercept is `D(0)=31.15`, giving **`gamma*=623/144≈4.3264` customer-revenue-intercept units per window**. Exact-rational code confirms capacity-binding and positive-surplus operation at this candidate. Pairwise indifference is not automatically the enterprise's preferred investment if incumbent expansion yields greater value.

## Exact synthetic choice, including incumbent capital opportunity cost

Established market A: `a=12,b=2,c=2,Pi0=7,rho=.8`, one installed unit and one-unit optional expansion for 6. Four-window incumbent incremental value is `82/5=16.40`. New B: `a_B(1)=25,b=2,c=2,Pi0=2,rho=.8`. Upfront budget is 30. No salvage or discounting in this table.

| Demand erosion gamma | Incumbent expansion | Software adaptation | Hardware redesign | Optimal option |
|---|---:|---:|---:|---|
| 0 | 16.40 | 41.09 | 72.24 | Redesign |
| 3 | 16.40 | 26.69 | 36.24 | Redesign |
| 5 | 16.40 | 17.09 | 12.24 | Software |
| 6 | 16.40 | 12.29 | 0.44 | Incumbent |

A single technical technology and investment menu therefore selects **redesign → quicker adaptation → incumbent deepening** as the assumed destination market's future demand falls. The 3x capacity is *accepted output per redesigned unit*, not three units of purchased hardware. The benchmark does not imply that an actual end market erodes at any of these rates.

Ablations: redesign lag equal to the four-window horizon eliminates its operating receipts; a redesign fixed fee of 25 becomes unaffordable; 22 cash units fund redesign but not software; a positive salvage share affects value but does not finance upfront investment; optional retention floors chosen incremental value at zero. These alternatives and the threshold are in `delayed_embodiment.py`. **Eighteen new scoped tests passed**, including the exact threshold, demand-slope comparison, prior qualification interface, budget monotonicity, customer demand response, accounting, lag, salvage and honest invalid-input cases. An additional **17 previous qualification tests and 18 original expansion tests were rerun successfully**. They are module tests, not historical repository CI or independent review.

## Empirical comparison and novelty boundary

**Hardware primary source:** Shaw, Agarwal and Pathak, *LEAP Hand: Low-Cost, Efficient, and Anthropomorphic Hand for Robot Learning*; first posted September 12, 2023. https://arxiv.org/abs/2309.06440 . The authors report a hand with changed kinematics and real manipulation demonstrations, assembled in roughly four hours from about $2,000 of research components; they also discuss simulation-to-real transfer. Abstract/introduction checked November 17, 2026. Those are **author-reported research-system observations**, not a commercial robot qualification cycle, complete-service reliability result, service output conversion factor or cost-to-qualified-capacity estimate.

**Closest timing prior art:** Jeon, *Time-to-build and capacity expansion*, *Annals of Operations Research* 328 (2023), published June 22, 2023. https://link.springer.com/article/10.1007/s10479-023-05413-3 . The published model already derives investment timing and capacity choices with uncertain time-to-build and learning-by-doing. The publisher's abstract and introduction were read November 17, 2026; this checkpoint does **not** replicate its full model. A delay-induced ranking reversal is not in itself a new economic result.

**Needed discriminating evidence:** compare two hardware configurations on the *same* customer-defined accepted service and target environment distribution, measuring adaptation/verification inputs, failed attempts, actual accepted output per physical unit, calendar time from design decision to qualified delivery, remaining human/supervisory support, alternative production costs, customer demand/contract receipts, and who finances each expenditure. Repeat across several target workflows. This distinguishes lower adaptation cost from higher output rate and from a shorter economic window. A research device's assembly hours cannot be substituted for industrial qualification or demand/finance evidence. The paired `evidence.json` records what is author-reported and what is still hypothetical.

This is a **conditional constructive economic model**, not an established publishable novelty claim. Existing optimal capacity, reliability allocation and real-options results limit the novelty of the threshold. A stronger contribution must demonstrate a property specific to joined capability–qualification–customer–payment networks, with a credible empirical denominator or new formal restrictions. The next tranche should develop the **observed** sector input–output backbone and a matched task/workflow contrast rather than add another unconstrained toy parameter sweep. Later theory should endogenize information-producing deployments, customer demand response and contract financing together.

Reproduce from this directory (Python 3.10+, standard library): `python delayed_embodiment.py` and `python -m unittest -v test_delayed_embodiment`. Generated results are exact fractions for cash and values; the existing convex qualification solver uses floating arithmetic, and its costs are explicitly rounded upward to hundredths. This checkpoint introduces no hardware purchase, model training, private data access or external publication.
