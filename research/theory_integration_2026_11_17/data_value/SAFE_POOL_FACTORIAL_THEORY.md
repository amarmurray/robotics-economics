# When Capabilities Become Production — safe controller-pool assignments, identification, and higher-order data complementarity

**18 November 2026 | private continuation, not publication.** This is the next argument after [conditional diagnostic calibration and pool interference](CONDITIONAL_CALIBRATION_AND_POOL_INTERFERENCE.md), not a new independently valued data model. Results are finite conditional propositions and **synthetic normalized captured accepted-service contribution**, not trained-robot evidence, field calibration, or novel statistical theory. Related [proof](SAFE_POOL_FACTORIAL_PROOF_LEDGER.md), [prospective empirical design](SAFE_POOL_FACTORIAL_EMPIRICAL.md), [reproducible countermodel](safe_pool_factorial.js), and [results](safe_pool_factorial_results.json).

## The precise unresolved question

The preceding two-slot example specified a mixed-pair controller interaction and showed that pooled diagnostic accuracy and pure-route economic payoffs do not reveal it. **Can we identify a demand-conditioned economically useful mixed learning action without observing the latent transfer regime, and which statements fail when the controller pool grows or part of its assignment support cannot be safely evaluated?**

Preserve one accounting map. \(Q_t\) records embodiment, controller version lineage, retained qualified policies, source rights, complete jointly accepted service recipes and safe operator resources. \(\omega_t\) records *actual* customer opportunities (including zero subsequent orders), contract capture, prices, specialist alternatives and scarce organizational/physical inputs. \(V(Q;\omega)\) optimizes feasible qualified accepted customer service. A complete-history controller-pool policy has captured value \(Y(a)=\sum_t r_t^{\rm accepted}-\sum_t c_t+V_T(Q_T;\omega_T)\), provided the terminal production horizon is **not** already included among the \(r_t\). Data enter only by changing learned \(Q\), information and feasible next decisions; no additional continuation-value premium is appended. Financial or rights limitations can restrict the assignment menu but are not the default mechanism.

Let D be a *pre-assignment* site/customer-demand stratum, and let \(a\in\{G,R\}^n\) specify which of n eligible learning slots in an **independent shared-controller pool** receive routine production data R versus deliberate target grounding G. The policy also specifies a frozen starting controller, intervention gate, retained fallback, technical validation, calendar and admissible physical recovery plan. Define the whole-pool conditional contribution \(\mu_d(a)=\mathbb E[Y(a)\mid D=d]\). A genuine new embodiment E or competent specialist S is another complete feasible policy, not an implicit free improvement in \(R\).

### Proposition 1 — directly identified expected economic interaction, without labeling latent transfer

Suppose the actual independent controller-pool or interference-neighborhood clusters are randomly assigned to **complete approved assignment vectors** with known strictly positive probability \(p_d(a)\) for every vector being compared, conditional on pre-action D and a common eligibility registry. All eligible customers are followed, including zero orders and recoveries; outcome/cost capture definitions and baseline policy rights are held fixed. Clusters do not contaminate each other's controller learning or customer opportunities.

Then the stratum-specific **mean full-policy** \(\mu_d(a)\) is design-identified, even if latent source-to-target alignment H is never safely observed. A finite-population Horvitz–Thompson estimator is
\[
\widehat\mu_d(a)=\frac{1}{N_d}\sum_{i:D_i=d}\frac{\mathbf1\{A_i=a\}Y_i}{p_{i,d}(a)}.
\tag{SP1}
\]
Randomization makes its expectation equal the average pool potential outcome \(N_d^{-1}\sum_iY_i(a)\). Customer demand *after* treatment is part of \(Y_i(a)\), not a group on which we condition. A full mixed-pool contrast such as \(\mu_d(RG)-[\mu_d(RR)+\mu_d(GG)]/2\) therefore identifies the extra **accepted customer production net of real resources** of a mixed controller in that demand stratum, under the experiment's joint policy and budget definition. It need not identify which latent data representation or modality caused the effect.

This identifies **population mean route rankings in randomized, safely eligible strata**, not individual counterfactual pairs, a parameter-invariant H report, a same-\(\theta\) robust guarantee, demand transport to unrepresented sites, or qualified behavior after an untested new embodiment. If separately randomized learning pools share a production customer, cloud controller checkpoint or scarce recovery operator, the actual cluster must be enlarged. If a branch has positive possible operator load beyond the cap and lacks certified pre-attempt abort, that assignment is not eligible for randomization, regardless of its attractive modeled mean.

### Proposition 2 — the two-slot interaction is not a scale law

For three slots write \(\mu_d(T)\) for the full-history conditional mean when the slots indexed by subset \(T\subseteq\{1,2,3\}\) are R and the rest G. The exact Boolean-lattice expansion is
\[
\mu_d(T)=\sum_{S\subseteq T}\beta_{S,d},\quad
\beta_{S,d}=\sum_{U\subseteq S}(-1)^{|S|-|U|}\mu_d(U).
\tag{SP2}
\]
Singletons measure changes relative to all-G with the *other two slots held at G*. Pairs measure nonadditive gains/losses conditional on that third G slot. The triple term is
\[
\beta_{123,d}=\mu_d(RRR)-\mu_d(RRG)-\mu_d(RGR)-\mu_d(GRR)
+\mu_d(RGG)+\mu_d(GRG)+\mu_d(GGR)-\mu_d(GGG).
\tag{SP3}
\]
It represents **whatever three-way complementarity or interference remains after every lower-order contrast**: new jointly qualified recipes, shared parameter interference, operator coordination, or customer-demand response. SP2 is inclusion–exclusion, not a claim of a newly discovered learning law.

Even perfect measurements of all seven assignments with at most two R slots leave \(\beta_{123,d}\) unidentified without a restriction or a safely supported eighth assignment. In the finite class with an independently justified bound \(\ell_d\le\mu_d(RRR)\le u_d\), the resulting sharp interval is \([\ell_d-c_d,u_d-c_d]\) where \(c_d\) is the value of RRR extrapolated using only lower-order coefficients. **Sharp** means relative to this unconstrained bounded-mean response class; actual shared hardware and transition kernels can impose additional restrictions, so this is at most an outer region for richer physical models.

A concrete three-slot conditional counterexample holds \(\mu(GGG)=7\), all three one-R assignments at 7.5, and all three two-R assignments at 7.4. These are complete per-pool accepted-service contributions with identical starting checkpoints and customers, not task benchmark scores. The pairwise-only predicted triple is 6.7. Two worlds have identical observed seven assignments but \(\mu(RRR)=6\) and 9. Accordingly \(\beta_{123}=-0.7\) or +2.3. If the RRR action is physically certified in both worlds, the best known one-R route yields 7.5: RRR loses in one world and wins in the other. The threshold \(\beta_{123}>0.8\) is exactly when RRR exceeds the 7.5 competitor. Neither a positive two-body transfer benchmark nor a two-slot mixed-controller regression identifies this three-slot decision.

### Proposition 3 — data collection randomization and production assignment are different decisions

With independent Bernoulli R assignment of probability x per slot, exchangeable three-slot mean values \(f_0=7,f_1=7.5,f_2=7.4,f_3=z\) imply
\[
F(x,z)=7(1-x)^3+3(7.5)x(1-x)^2+3(7.4)x^2(1-x)+zx^3
=7+1.5x-1.8x^2+(z-6.7)x^3.\tag{SP4}
\]
If an approved action has \(z\in[6,9]\), the lower-world Bernoulli optimum is \(x^*=(\sqrt{71}-6)/7\approx0.34659\), guaranteeing \(F(x^*,6)\approx7.27452\). Yet **a fixed saturation design that assigns exactly one R per pool** (with symmetric randomly selected physical slot) produces 7.5 with the same three learning slots and no RRR support. Bernoulli exploration is useful for identifying multiple potential exposure cells; it is *not automatically* the profit-maximizing production allocation. If RRR is not safety-approved, every \(x>0\) Bernoulli rule is **inadmissible**, as it places positive probability \(x^3\) on that trajectory. Its calculated value cannot rescue it. The exactly-one-R design remains a feasible candidate only after **its own** pathwise certification.

This fixed-composition superiority is not universal: known heterogeneous customers, regime-conditional learning, binding embodied materials, adaptive signal discovery or cross-pool interference can make randomization/hedging valuable. The constructed mean table only isolates the invalid inference from an i.i.d. route-mix parameter to a deployment policy. The prior two-slot interference functional form should not be extrapolated to n=3 by fiat.

### Proposition 4 — selective rollout can be robustly productive when global transfer is not ranked

Let **pre-action** high-coverage customer segment A have target share \(w_A=0.7\) and independently approved, observed mixed-one-R contribution 7.5, with all-G comparator 7. Segment B has share 0.3 and known all-G contribution 7, but its *approved yet unassigned* mixed-one-R conditional mean is only bounded by 5 and 9. Assume a common per-pool accounting unit and no cross-segment demand spillover. These are hypothetical bounds, not source-calibrated estimates.

All-G target production is 7. Applying the mixed learning policy everywhere gives \(0.7(7.5)+0.3\mu_B(RGG)\in[6.75,7.95]\); relative to all-G, its paired target difference is \([-0.25,+0.95]\). The sign is unidentifiable because the trial did not cover B, even though A's randomized route effect is exactly known. But the **selective** eligible policy using mixed learning only in A and the retained G fallback in B gives \(0.7(7.5)+0.3(7)=7.35\). It dominates all-G on this constructed target by 0.35, provided differentiated coordination/rights/validation cost is below 0.35 and no between-stratum interference exists.

This policy's guarantee does **not** infer technical transfer in B. If the mixed B policy is *unapproved* rather than merely unobserved, global mixing must be deleted from the feasible menu, but the selective A/G route may still be evaluated. If segmentation itself changes later customer demand across strata or pools share controller weights, the simple weighted sum fails and a complete coupled history must replace it. These transport bounds are sharp only under the stipulated interval and independently attainable stratum means.

## Consequences for source value, embodiment, and end-market economics

A reported improvement in pretrained, simulation, teleoperated, field or recovery data can have an effect on a *component* controller skill while adding zero accepted complete service under the customer's bundle requirements, or it can interact with the third concurrent deployment to open an entire service recipe. SP3 is an exact contrast in **economic outcomes**, not evidence that training on a given modality is intrinsically complementary. To interpret it as *learning* rather than cross-customer demand externality, hold the commercial opportunity and route-specific price/capture schedule in a controlled secondary experiment, then measure qualification on held-out whole tasks; contrast this with the total-policy economic effect, which should include genuine demand response.

A genuinely new embodiment changes which vector assignments and controller-lineage rollouts exist; it cannot be inserted by adding a constant coefficient to the RRR polynomial. Scarce operators and physical capacity constrain feasible vectors before the cost/return table is optimized. A kept, approved old controller provides a baseline option if resources and rights make it available. **Free optional data** cannot lower optimized feasible value under a policy menu containing the opt-out; conflicting mandatory shared training and costly storage/curation can.

This bridge remains useful for the wider enterprise theory: which combinations of equipment, human supervision, digital-controller pooling and qualified customer orders are complementary in a multipayer production network; which source information unlocks *new recipes* versus merely better old tasks; and which end markets have enough demand to pay for the actual validated new bundles. Nothing here establishes the BLS/BEA numerical industrial topology, a deployment cost elasticity or a source's market price.

## Empirical discrimination, prior art, and open proof gap

The smallest credible test is **whole-pool randomized saturation within already approved controller/safety strata**, pre-action customer segmentation, a complete order/zero denominator, frozen lineage, independent recovery support validation and explicit measured isolated-controller cost. Compare all-G, one-R, two-R and, *only if certified*, all-R assignments on the same n-slot pool, as well as a competent specialist, old-policy/no-retrain and a different embodiment when equivalently feasible. Add a held-out skill/qualification experiment to distinguish true controller learning from a commercial order effect. If RRR is unsafe or lacks rights, record the positivity gap and deploy the best approved policy; do not extrapolate an imaginary three-way coefficient to authorize it.

**Closest existing foundations:** Hudgens and Halloran (2008), [JASA 103:832–842](https://pmc.ncbi.nlm.nih.gov/articles/PMC2600548/), explicitly treats within-group interference and two-stage randomization. Aronow and Samii (2017), [*Annals of Applied Statistics* 11:1912–1947](https://isps.yale.edu/resource/estimating-average-causal-effects-under-general-interference-with-application-to-a-social), covers assignment-dependent exposure mappings and randomization-based effects under general interference. Inclusion–exclusion/Boolean factorial expansions, Horvitz–Thompson weighting, partial-identification bounds and process complementarities are established mathematics. DDA §5 already endogenizes data and production; its Appendix B already addresses data complementarities. The candidate contribution remains a disciplined **customer-qualified, safety-feasible data-to-production** connection, not the assertion that interference or higher-order interactions were newly discovered.

**Exact continuation:** establish which safe n-slot production/exposure vectors and controlled held-out customer acceptance records can support an informative partial-identification bound under an evolving **shared controller network**, where controller lineage, market demand and operator capacity create interference across pools. At the November 22 review, reconcile these finite mean results with the *same-world*, persistent-transfer robust complete-history result: randomized policy means identify an average treatment contrast, **not** the unit-level joint potential-response distribution or its regime-conditional minimum. Do not promote the scientific gate from these synthetic checks. December 25, 2026 23:59 Eastern remains the final research deadline.
