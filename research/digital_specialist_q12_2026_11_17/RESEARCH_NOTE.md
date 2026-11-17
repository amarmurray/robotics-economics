# Q12: physical optionality versus coordinated specialist robots

**Research tranche, November 17, 2026.** Compared qualified physically flexible capacity with task-dedicated capacity linked by digital routing and a scarce human-attention resource. Previous branch input bea514e7fc1c28bb56babbd26d77d5b7a9ef5d33 had an expired Q10 lease. Unpublished Q10 work was not recovered or overwritten. Q11's correlated-demand comparison is preserved as a separately validated local archive, not falsely called integrated. All numbers in this note are **synthetic normalized units**, not observed robotics returns, intervention rates, safety staffing, costs or customer prices.

## Economic environment

Two accepted customer services A and B generate incremental joint operating surplus relative to their feasible outside production:

    G(q_A,q_B) = (d_A-e_A)q_A + (d_B-e_B)q_B - b(q_A²+q_B²)/2.

The intercepts d include relevant incremental retained-work and alternative-process costs. The provider is reimbursed operating resources and captures a specified fraction rho of additional surplus through a hypothetical two-part tariff; the customer retains the rest and can refuse the robotic service. This is not a claim about actual hourly RaaS contracts or a complete welfare calculation. Customer output q responds to demand rather than equaling advertised robot cycles.

A qualified flexible platform F can allocate K=2 physical output units across both services after demand is observed, pays incremental resource cost epsilon for each accepted output, and has upfront capital/validation cost C_F. In this benchmark both services are qualified and reallocation is assumed immediate; this is optimistic for F. Dedicated specialist units S have task caps K/2 each and upfront C_S. A digital coordination investment D does not create physical capacity; it reduces human-supervision attention per accepted service from h_S to h_D for cash C_D. Each policy faces shared scarce attention H, so h_A q_A + h_B q_B <= H. Task eligibility and integration rights gate the relevant options. The provider must fund the entire C_option before production from cash B, with no assumed bridge lender. Common required human staffing is held fixed; avoiding some attention is not automatically a wage saving or permission to change safety coverage.

We maximize the concave joint service surplus under each option's linear resource/qualification constraints and compare rho times expected surplus minus upfront investment. The source code uses exact Python rational arithmetic to enumerate all interior, binding-line and vertex candidates for a compact 2D polygon, so the optimizer is exact for this specified model.

## Result 1 — demand covariance matters even against a competent digitally coordinated specialist alternative

Each demand margin takes d_L or d_H, with probability one-half marginally for each task. A synchrony parameter lambda sets HH and LL probabilities lambda/2 each and HL and LH probabilities (1-lambda)/2 each, preserving both marginal demand distributions. Suppose both policies are qualified, affordable, each dedicated task's capacity binds, and F's total capacity binds with an interior reallocation optimum. Suppose human attention is nonbinding at full K for both policies. Direct solution of F's first-order condition yields q_A = K/2+(d_A-d_B)/(2b) and q_B = K/2-(d_A-d_B)/(2b). Subtracting fixed half-capacity task outputs yields

    Expected(F minus coordinated specialists)
      = rho [ (1-lambda)(d_H-d_L)^2/(4b) - epsilon K ]
        - [ C_F - (C_S+C_D) ].

Proof: the state-specific reallocation benefit is the squared difference between demand margins divided by 4b. It occurs only when task demand differs, which has probability 1-lambda. Subtract morphology and investment costs. This is standard process flexibility / concave allocation mathematics, not a novel theorem.

Exact synthetic inputs K=2, b=2, d_L=3, d_H=5, epsilon=1/10, rho=4/5, equal capital costs C_F=C_S+C_D=43/20 yield a difference 6/25 - (2/5)lambda. F wins for lambda below 3/5 and loses above. At equality both policies yield 53/20 and the solver conservatively retains the coordinated specialist alternative. Separate marginal task demand forecasts cannot recover this ranking without their joint timing/correlation.

## Result 2 — supervisor attention can reverse the flexibility ranking under anti-correlated demand

Hold lambda=0, demand, capital outlays, qualification and physical capacity fixed. Assume F requires 1/2 human-attention unit per accepted service, S+D requires 2/5, and S without D requires 3/4. With H=1, both flexible and coordinated specialists deliver total accepted output 2 and F's optimized net provider value is 289/100 versus S+D at 53/20: F wins by 6/25. With H=4/5, F cannot deliver more than 8/5 accepted units, while S+D still delivers two. F's net provider value is 1109/500 and S+D remains 53/20, so F loses by 54/125. In a mixed (5,3) demand state, F re-solves q=(13/10,3/10) and gross incremental joint surplus 273/50; specialists deliver (1,1) at gross joint surplus 6.

These are **conditional exact counterexamples**. They show why competent digital coordination can economize on the shared human input and beat an otherwise advantageous cross-task physical platform without buying additional robots. The coefficients do not claim empirical safety-compliant staffing efficiency. Q4's finite-source Markov intervention process is an alternative specification, not a derivation of these deterministic per-unit attention coefficients.

A basic monotonicity fact follows by feasible-set inclusion: if software genuinely reduces attention required for every accepted service while holding quality, constraints and all other inputs fixed, gross operating value cannot decline. Its net private value may be negative once C_D is paid, and it cannot be chosen absent cash or integration rights. Similarly F cannot claim a second task's benefit without that task's service qualification.

## Source-backed contrast and prior art

Locus Robotics' undated How It Works page (retrieved November 17, 2026) describes LocusONE's mixed-robot/human workflows and Pick & Pass directing autonomous work toward suitable collaborative capacity. This documents organizationally routed specialist/heterogeneous productive tasks, not measured h_D, total accepted service, or contract margins: https://locusrobotics.com/platform/how-it-works/ .

Amazon's October 18, 2023 introduction of Sequoia describes a Houston deployment linking mobile robots, gantry systems, robotic arms and human stations. Its issuer-reported throughput claims are not an experiment comparing that multi-system installation with a fully certified generalist fleet: https://www.aboutamazon.com/news/operations/amazon-introduces-new-robotics-solutions .

Jordan and Graves' 1995 Management Science article already treats process flexibility under demand uncertainty. The demand covariance argument belongs to this prior-art family rather than establishing publication novelty. DOI 10.1287/mnsc.41.4.577, https://pubsonline.informs.org/doi/10.1287/mnsc.41.4.577 .

Importantly, Locus also advertises dynamically directing different robots across workflows. A real digitally orchestrated fleet may achieve some *physical* reallocation: our fixed q_A<=1 and q_B<=1 specialist restrictions are an explicit counterfactual, not a universal claim about Locus or another vendor.

## Falsification and empirical panel

Record, for the *same site and service windows*, concurrent task arrivals and accepted complete-service demand; qualified task eligibility and switching time for each robot; customer value and best feasible alternative; joint rework and service-level failures; physical capacity and retained workers; robot/human exception exposure, timestamps and required safety coverage; integrator/producer receipts, penalties, support bills, dated acquisitions and integration invoices; and legal data/coordination rights. Test a matched digital change under otherwise comparable hardware/qualification, measuring accepted output rather than robot counts or raw picks.

A decisive negative control: if human attention is not binding, reducing h cannot generate incremental accepted output through the model's attention channel. If digitally coordinated specialists can themselves freely shift qualified machines across both tasks, fixed dedicated task caps are invalid and F's modeled pooling premium may shrink or disappear. If accepted orders differ materially from pick counts, the demand intercept cannot be inferred from raw pick throughput.

## Reproduction, limits, and next work

From this folder run Python 3.10+ without external packages:

    python portfolio_attention.py --output results.json
    python -m unittest -v test_portfolio_attention

Twenty newly scoped tests passed and clean-directory results regenerated byte-identically. This covers the displayed synthetic model, not full historical repository CI, real calibration, a causal empirical effect or external peer review. Git source and test blobs have been matched to the validated local files.

Next: replace the binary qualified/unqualified task restriction with a typed overlapping eligibility graph, switching costs, same-order completion and a competent digitally routed mixed fleet; derive when organizational coordination reproduces physical flexibility and when complementary generalist hardware is justified. Integrate the result into the manuscript and workflow atlas while retaining the separately unresolved official BEA numeric production backbone and full December 25 schedule.
