# Finite paid-program inference when source learning joins formerly separate fleets

**21 November 2026 | continuation of the same *When Capabilities Become Production* Models A/B argument.** Scientific gate **OPEN**. This chapter extends [finite-sample complete-buyer measurement](FINITE_SAMPLE_PAID_PROGRAM_THEORY.md), [the existing network-interference theory](NETWORK_INTERFERENCE_THEORY.md) and [shared-pool production](SHARED_POOL_INTERFERENCE_THEORY.md). It does **not** rebrand standard interference estimators as new mathematics. The question is whether a mixed source/grounding (SG) versus new embodiment (E) study can identify a **full-market paid-production** contrast when a robot learner, operator recovery pool or original buyer contract joins experimental sites. All numerical examples below are deliberately synthetic, not robot/customer evidence.

## 1. Economic and learning environment: the actual intervention boundary

Pre-register a finite set of original eligible customer/order accounting units `i=1,...,N`, including customers who never buy. Let `z_j=1` mean one **physically approved complete SG learner/controller/operator program** assigned to eligible experimental unit `j`, and `z_j=0` mean a separately **physically approved complete E program**, with old R and specialist fallback still feasible where authorized. Outcomes must include the entire predeclared horizon of accepted original-buyer service, refund or settlement, displaced outside orders, operator/robot capacity, and program-specific continuation from licensed production-generated data *once*. The data sources — field success, failure/recovery, teleoperation, simulation, synthetic, public/pretrained — retain separate lineage, rights, compute/curation and causal support. SG is not merely 'more teleoperation'; E changes physical recipe feasibility and may also alter training data.

Define a **fixed accounting allocation** `Y_i(z)`: total captured paid-service contribution assigned to original order/parent `i` under complete network policy vector `z`, after correctly accounting for displaced service and refunds. Sum across `i` must equal the actual signed whole-network contribution (before any separately specified deterministic program costs). If the optimizer reallocates a shared operator or robot across customers, this affects `Y_i` at *both* customers. This partition is for measurement, not an assertion that economic production is separable. Original buyer demand and accepted price may respond to the intervention. The target is the finite-population, **all-market** contrast

```text
Delta = (1/N) sum_i [Y_i(1,...,1) - Y_i(0,...,0)] - (K_SG-K_E)/N .
```

Here `K` is any program-specific *total* cost not already included in `Y`; do not subtract twice. If `Y` includes economically relevant future learning and its paid production, there is no separate premium for the learned dataset. No claim of real customer support or deployed hardware is made.

Define a **pre-treatment full-horizon exposure set** `H_i` (containing `i`) sufficient if, for all admissible physically signed assignments `z,z'` that agree on every index in `H_i`, `Y_i(z)=Y_i(z')`. The closure must include not only current physical proximity but *all directed ancestor influences throughout the full horizon*: source/replay and updated shared model checkpoints, operator queues, procurement parents, robot/embodiment manufacturing and site access, shared customer substitution and replenishment, future licensed service-generated data, safety/recovery and payment settlement. Unobserved network links are a scientific assumption failure, **not** small errors by default.

The prior independent-network fixed-n Hoeffding result is a special case with individually closed, independently sampled networks. Here assignment can be randomized across linked units inside **one** fixed market, so we explicitly target all-SG versus all-E, not the direct effect at a mixed exposure rate.

## 2. Exact exposure-based full-program estimator

**Proposition (design-unbiased total program contrast; standard exposure Horvitz–Thompson construction).** Suppose complete assignments are randomized independently, `P(Z_j=1)=p` with `0<p<1`. The full-horizon exposure sets `H_i` are valid and fixed *before* treatment, both complete programs are lawful and physically feasible for every relevant assignment, observed buyer allocations are consistent and complete, and all outcomes are well defined. Define `I_i^1=1{Z_j=1 for all j in H_i}`, `I_i^0=1{Z_j=0 for all j in H_i}`, and `pi_i^1=p^{|H_i|}`, `pi_i^0=(1-p)^{|H_i|}`. Then

```text
mu_hat_a = (1/N) sum_i I_i^a Y_i(Z)/pi_i^a ,  a in {0,1}
Delta_hat = mu_hat_1 - mu_hat_0 - (K_SG-K_E)/N
E_Z Delta_hat = Delta.
```

**Proof.** On `I_i^a=1`, exposure sufficiency gives `Y_i(Z)=Y_i(a 1_N)`. The indicator has expectation `pi_i^a`, so each inverse-weighted term has expectation exactly the desired full-policy original-buyer contribution; sum and subtract deterministic costs. No assumption of independent realized customer outcomes, constant demand, additive technical transfer or cross-world qualification independence is used. What is crucial is the *stronger* full-horizon exposure mapping. QED.

If `Y_i` can be negative, choose predeclared `L_i` and `U_i` that bound both arm outcomes, estimate `Y_i-L_i` by inverse exposure weights and add the known `L_i` outside the HT sum. The value remains unbiased; the range width `B_i=U_i-L_i` governs variance. This retains continuous contract prices, refunds and verified outside-service opportunity rather than forcing paid service into Bernoulli probabilities. If there is no credible bound on extreme refunds, downstream liabilities or continuation, no finite range-based certificate follows.

## 3. Exact randomization variance and the interference penalty

For transparent variance algebra, suppose normalized shifted full-program paid contributions `y_i^a=Y_i(a1_N)-L_i` lie in `[0,B]`; the constant lower shifts and deterministic `K` do not change the variance. With `o_ij=|H_i intersect H_j|`, the exact *design* covariance identities are

```text
Var(mu_hat_a) =
  N^-2 sum_{i,j} y_i^a y_j^a [p_a^(-o_ij)-1] ,
   p_1=p, p_0=1-p.

Cov(mu_hat_1,mu_hat_0) =
  - N^-2 sum_{i,j: o_ij>0} y_i^1 y_j^0 .

Var(Delta_hat) = Var(mu_hat_1)+Var(mu_hat_0)
                 -2 Cov(mu_hat_1,mu_hat_0).
```

**Proof.** For equal-arm full-neighborhood indicators, the joint exposure probability is `p_a^{|H_i union H_j|}`; dividing by the two marginal exposure probabilities gives `p_a^{-|H_i intersect H_j|}`. For opposite-arm indicators, an overlapping neighborhood cannot be both all-1 and all-0, so the product is zero and the covariance is minus the product of means; disjoint neighborhoods' exposures are independent. Multiplication by fixed full-policy contributions and summation yields the formulas. QED.

Let `d=max_i |H_i|` and `M=max_i #{j:H_i intersect H_j is nonempty}`. Then, by `0<=y_i^a<=B`,

```text
Var(Delta_hat) <= (B^2 M/N) [p^(-d)+(1-p)^(-d)].
```

This follows by counting at most `NM` overlapping ordered pairs, bounding equal-arm positive covariance by `B²(p_a^{-d}-1)` and opposite-arm absolute covariance by `B²`. Thus Chebyshev gives the **valid but potentially vacuous**, fixed-design certificate

```text
P_Z( |Delta_hat-Delta| >=
 B sqrt(M [p^(-d)+(1-p)^(-d)] /(N alpha)) ) <= alpha .
```

A positive paid-production ranking is certified only if the observed `Delta_hat` exceeds this radius (with deterministic cost differences and any justified transport/error allowances applied). This is a finite-population design result: it need not rely on iid robot attempts or buyer prices. It is often *much worse* than a whole-closed-network randomized design. No sequential peeking or ex post graph surgery is allowed.

## 4. Synthetic exact counterworlds and negative findings

A predeclared four-original-buyer **path** has `H_1={1,2}`, `H_2={1,2,3}`, `H_3={2,3,4}`, `H_4={3,4}`; `p=1/2`. Under full SG the individual normalized paid contributions are `(8,12,18,16)/20`; under full E they are `(10,6,15,13)/20`. These are *synthetic per-buyer payoff cells*, not robot success rates or dollar returns. Mixed assignments may have any paid outcomes consistent with the stated local exposure assumption; the HT estimator only uses homogeneous neighborhoods.

Exhaustive, integer-exact enumeration of all 16 assignments gives `mu_SG=27/40`, `mu_E=11/20`, `Delta=1/8`, `Var(mu_hat_SG)=2127/1600`, `Var(mu_hat_E)=129/160`, `Cov=-33/100`, `Var(Delta_hat)=4473/1600`. The simple `B=1,d=3,M=4` variance upper bound is **16**, too large to certify this small positive SG advantage. The negative cross-arm covariance matters: do not treat both arm estimators from the *same* mixed assignment as independent. The independent Python `Fraction` check and exact JS reproducer corroborate the algebra, not the assumptions.

**Global shared learner counterworld.** If a single reused/updated learner, supervisor/dispatch arbitrator or buyer allocation couples every original market unit to every assignment, then `H_i={1,...,N}`. Bernoulli 50:50 assignment has probability only `2^{1-N}` of producing **either** homogeneous full-program exposure. For N=20, that is `1/524288` per random assignment, so 524,288 independent *full assignment vectors* is the geometric mean to see either once, **not** a usable precision or experimental power calculation. Two physically possible worlds can agree on *every mixed assignment's* customer payoffs but assign opposite complete-network advantages to SG and E. Until a homogeneous vector is observed, mixed-outcome evidence cannot distinguish these worlds under arbitrary whole-network interference. Adding more independently logged robot attempts does not restore missing full-market support.

**One omitted edge.** With two units, suppose unit 1 earns one accepted paid-service unit under SG *only when both assignments are SG*, and the second accounting unit earns zero; true all-SG average is `1/2`. Mistakenly declaring the first unit's exposure set to be only itself gives an own-assignment inverse-weighted **expected** market average of `1/4`. This is not mere variance inflation: a missing shared learner/operator or buyer edge changes the estimand and produces bias.

**Data availability versus knowledge of deployment value.** Adding free, legally accessible source information to an optimization menu while retaining old safe controllers and budgets cannot reduce the maximum *gross feasible* production value: the old feasible policy remains selectable. But using a **forced shared update** may (a) have costs or negative transfer and (b) expand `H_i` through network-wide data and model reuse. An investor could therefore gain a real production option while making its *market-wide treatment comparison* exponentially less supported under naive mixed randomization. There is no contradiction: economic option monotonicity and statistical exposure probability are different objects. Whether pooling also improves future qualification is a matched learning experiment question, not assumed by this inference theorem.

## 5. What survives at the November 22 Models A/B gate

The contribution is a **conditional integration**, not a purported new inverse-probability estimator. Model A's whole-network qualified service optimization determines actual paid `Y_i` and physically feasible dispatch; Model B's endogenous source/grounding/E learning and production-generated data determine both the future paid values *and the causal exposure closure*. One must *not* build the influence graph from postassignment data-reuse behavior alone and then claim fixed design unbiasedness. Explicitly version and freeze learner lineage, training update admission, E manufacturing/site feasibility, operator recovery and buyer/settlement parentage when declaring the allowable graphs. If shared weights are updated from production during the outcome horizon, closure must include everyone who can influence that update. Multiple independent, wholly isolated learner/operator/customer networks can still be used as the previous [finite sample independent-cluster design](FINITE_SAMPLE_PAID_PROGRAM_THEORY.md); they are not conjured by treating individual robot trajectories as independent.

The actual **discriminating evidence** is not another benchmark score: it is signed legal physical support for both complete arms, the original offered-buyer registry, a trace of shared weights/data rights and update/dispatch edges, accepted and finally settled services and displaced alternatives at contract-level prices (including zero buyers), and a justified pre-treatment exposure map. If either E is not physically approved or the true graph is near-complete, report economic program ranking as unidentified or exceptionally imprecise; choose an ethically lawful whole-network design rather than extrapolating mixed site evidence. Heterogeneous hardware, demand mixtures, compute/curation and ownership/control rights remain in `Y,K,H`, not in arbitrary new 'data premiums'.

**Closest prior art (verified public records):** Aronow & Samii, [Estimating Average Causal Effects Under General Interference](https://doi.org/10.1214/16-AOAS1005), *Annals of Applied Statistics* 11 (2017), develop exposure probabilities and inverse-weighted inference; Ugander, Karrer, Backstrom & Kleinberg, [Graph Cluster Randomization](https://arxiv.org/abs/1305.6979) (2013), address exponential degree-related variance and graph clustering; Sävje, Aronow & Hudgens, [Average Treatment Effects in the Presence of Unknown Interference](https://doi.org/10.1214/20-AOS1973), *Annals of Statistics* 49 (2021), address limited unknown interference with different estimands. The earlier internal [network interference](NETWORK_INTERFERENCE_THEORY.md) and [approximate network remainder](APPROXIMATE_NETWORK_REMAINDER.md) already cover nearby issues; this chapter specifies the **full paid-service, original-buyer, source-learning horizon** version and exposes the finite-sample comparison cost. DDA [§5 and Appendix B](https://arxiv.org/abs/2606.10127) already discuss valuable production-generated data and complementary accumulation. Neither this adaptation nor the synthetic computations establish independent scientific novelty.

**Evidence status:** No approved cross-arm SG/E deployment, customer registry/receipts, learner/procurement exposure closure, numerical official BEA/BLS transaction network, full repository CI or external novelty evaluation. [Prospective protocol](WHOLE_PROGRAM_EXPOSURE_EVIDENCE.md), [exact JS source](whole_program_exposure_exact.js), [record](whole_program_exposure_results.json), [independent Python checker](whole_program_exposure_independent.py), [student problems](WHOLE_PROGRAM_EXPOSURE_EXERCISES.md) and [instructor solutions](WHOLE_PROGRAM_EXPOSURE_SOLUTIONS.md) accompany the argument. November 22 scientific acceptance is **OPEN**; November 29, December 6, December 13/18/23/24 and final December 25, 2026, 23:59 America/New_York are unchanged.
