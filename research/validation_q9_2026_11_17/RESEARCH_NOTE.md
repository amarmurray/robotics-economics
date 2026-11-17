# Q9 — When is evidence worth more than another robot?

**November 17, 2026.** Source revision: `18e092cf07f4e4376a7ae3de7bee3b30aba28b1d`. Status: exact synthetic Bayesian value-of-sample-information analysis, not an empirical calibration or established novel theorem.

## Question and economic unit

Q8 established that a successful case movement is not a completed paid warehouse order. The joint completion rate of required pick, pallet and WMS-acceptance events can differ sharply despite identical marginal competence. A deployer uncertain about **complete target service** might fund a held-out qualification experiment rather than immediately expand an accepted unloading workflow.

This checkpoint values **learning whether a fixed configuration meets acceptance**, distinct from Q7's investing to improve capability, manufacturing, data rights and demand. The alternative to testing is not zero: it is a profitable incumbent capacity investment.

## Exact decision model

At time 0 the firm has cash B. A target policy has stable hidden state θ in {H,L}, with prior p for H and complete-service success probabilities g_H>g_L. Across target orders, conditional on θ, n held-out outcomes are iid Bernoulli(g_θ). Within each order component failures may be correlated. The illustrative g_H=19/20 and g_L=17/20 are both compatible with three component marginal successes of 19/20 under different dependence patterns from Q8. No such prior or cross-order stationarity has been estimated.

The firm can pay for n **nonbillable** complete-order trials, costing C(n)=f+n*c_test if n>0, or zero if n=0. These trials are pure information, not additional training, policy adaptation, billable production or contractual rights. For s successes:

    L_θ(s) = binom(n,s)*g_θ^s*(1-g_θ)^(n-s)
    p_s = p*L_H(s)/[p*L_H(s)+(1-p)*L_L(s)].

After paying C(n), remaining cash funds at most one next action: retain cash (incremental net 0), acquire incumbent unloading capacity for I_A and incremental gross receipts H_A (net J=H_A-I_A), or qualify a new case-picking service for I_B. Future customer demand, rework and outside production are treated as in Q8:

    G(A;g)=[(a+h)g-(c_a+h)]*A - b*g²*A²/2, 0<=A<=K
    V_θ = ρ*max(0,max_A G(A;g_θ)-Π0) - I_B.

Here ρ is provider surplus capture, Π0 the customer's best feasible outside operating profit; c_a is cost per attempted service, not experiment cost. The inherited fluid approximation applies demand revenue to expected accepted output; it is not E[R(random total)]. Retained terminal cash cancels in net-value comparisons. Loan finance, salvage and simultaneous fleet investments are not assumed. All outcomes are valued with common discount factor one.

Let w_H(s)=p*L_H(s), w_L(s)=(1-p)*L_L(s), P_s=w_H+w_L. For each s, choose the best *feasible* action after spending C(n). A requires B-C(n)>=I_A; B-entry requires B-C(n)>=I_B. Then

    W(n)=sum_s max feasible{0, J*P_s, V_H*w_H(s)+V_L*w_L(s)} - C(n).

The finite optimal experiment maximizes W(n) over permitted n. When both investments are feasible and V_H>J>V_L, target entry requires

    p_s > (J-V_L)/(V_H-V_L).

Equivalently posterior odds must exceed the threshold odds. With costless information and unchanged actions, EVSI is nonnegative by the retain-original-policy argument and bounded by EVPI. **Paid information need not be valuable:** sample spending can make the target itself unaffordable, even when free perfect information would improve a decision. Arbitrarily preventing customer/financier transfers would overstate that effect; this is a specified cash policy, not proof that integrated ownership is necessary.

## Exact synthetic comparison

Use Q8's complete-order operating function a=10, b=2, c_a=1, h=2, K=4, Π0=16, ρ=1, fixed new-service investment I_B=2. For g_H=.95, target payoff V_H=29/25=1.16; for g_L=.85, V_L=-19/25=-.76. Both use capacity K=4 at the optimum. The incumbent alternative requires I_A=1, generates gross future incremental provider profit H_A=13/10, and gives J=3/10=.30. Prior p=.5 makes untested target expected value .20, so without testing the deployer expands the incumbent. Set B=2.10 and C(n)=.01*n.

The posterior high-state threshold is 53/96, and with equal prior odds the required likelihood ratio is 53/43. The likelihood ratio after s successes in n trials is (19/17)^s*(1/3)^(n-s). A single successful whole order is insufficient to reverse the choice. **For n=8 only eight full-order successes induce target entry**; any failure retains the incumbent.

Exact rational enumeration across n=0,...,40 yields n*=8. Gross post-evidence investment value is 112857806639/256000000000 ≈ .440850807. Trial expense is .08; resulting net W(8)=92377806639/256000000000 ≈ .360850807, compared with W(0)=.30. Thus **incremental net evidence value ≈ .06085**, not the gross EVSI ≈ .14085. EVPI in the base example is .43. Full fraction-valued computations, all signal branches and alternative scenarios regenerate via the attached Python model.

| Cash B | Best n | Net provider value | Mechanism |
|---|---:|---:|---|
| 2.00 | 0 | .300000 | Any positive trial cost removes ability to pay I_B=2 after testing. |
| 2.05 | 5 | .347562 | Five trials preserve B-C(n)>=2. |
| 2.10 | 8 | .360851 | Eight trials maximize net value with the selected costs. |

Increasing destination demand intercept to 12 makes the new service preferable in both regimes and removes the value of testing. Reducing capture ρ to 1/2 makes both regimes less valuable than incumbent expansion, also removing the test incentive. Thus outcome uncertainty is insufficient: **information has economic value near a consequential, financeable decision margin**. These are synthetic conditional examples, not robotics-industry sample-size recommendations.

## Empirical bridge and prior art

Primary source [S1], the RoboCasa 1.0.1 benchmarking documentation, specifies randomly sampled evaluation scenarios with **binary full-task success** across 50 rollouts and a held-out target scene/object split. It supplies a useful experimental measurement *format*; kitchen simulation outcomes do not identify paid warehouse order completion, corrective labor, contracts or cash.

Primary source [S2], the DROID project, describes 76,000 demonstration trajectories across heterogeneous physical settings and released policy-training materials. Curated successful demonstrations are not an unbiased denominator of accepted target customer orders. Its first arXiv posting was March 19, 2024; subsequent project updates should not be conflated with that initial version.

Nanda and Rhodes-Kropf (2016) [S3] analyze staged experimentation and its financing. Bayesian information valuation and costly financing of experiments are prior art. No novelty claim is made from rederiving those mechanisms with robotic terminology.

The minimum discriminating field panel records: (site/date, fixed robot-policy version, held-out complete-order identifier, required SKU/steps, joint successes/failures, manual recovery, WMS acceptance, data exposure/reuse rights, experimental labor/cost and delay, incumbent expansion alternative, customer final-output economics, contract rights, upfront financing, invoices and receipts). Rejecting failed opportunities and unpurchased pilots from the denominator biases apparent success. Do not add the same trial both to policy-training and independent-validation outcomes without accounting for the dependence.

None of [S1]–[S3] provides a matched warehouse order-level acceptance, qualification expenditure, provider receipt and financing sequence. Q8's observed DHL unloading and proposed case-picking expansion cannot calibrate the example. The BEA production backbone remains a separate uncompleted empirical milestone.

## Replication and next test

From this directory: `python value_of_evidence.py` then `python -m unittest -v test_value_of_evidence`. **25 new scoped tests passed** on November 17, 2026: exact payoff/threshold arithmetic, posterior signal decisions, binomial normalization, cash and opportunity cost, gross EVSI and EVPI bounds, high-demand/low-capture alternatives, parameter scans, deterministic regeneration. Full historical CI and independent review were not run. The stored git blobs for code and tests were checked against the locally tested files.

**Next theory:** add validation delay with changing destination demand, and a competent paid pilot/finance alternative; separate pure information acquisition from policy improvement and don't credit both for one episode. **Next empirical task:** find a real service-completion and payer panel, or explicitly delimit why public evidence does not identify it. The first-paper contribution remains unselected.

Sources inspected November 17, 2026:

[S1] RoboCasa official 1.0.1 benchmarking documentation (page undated): https://robocasa.ai/docs/build/html/benchmarking/benchmarking_overview.html

[S2] DROID project and original paper: https://droid-dataset.github.io/ ; https://arxiv.org/abs/2403.12945

[S3] Ramana Nanda and Matthew Rhodes-Kropf, *Financing Entrepreneurial Experimentation*, *Innovation Policy and the Economy*, March 1, 2016: https://www.journals.uchicago.edu/doi/10.1086/684983
