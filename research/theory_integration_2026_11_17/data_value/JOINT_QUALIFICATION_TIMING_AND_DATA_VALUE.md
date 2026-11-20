# Joint source qualification, commitment timing and the economic value of data diversity

**20 November 2026 — same `When Capabilities Become Production` / November 22 Models A–B scientific acceptance question.** This continues [source-generated embodiment options](ADAPTIVE_EMBODIMENT_DATA_OPTION_VALUE.md), rather than creating another unrelated question. The central problem is whether training on distinct sources produces *a menu of usable qualified policies*, whether a target-grounding report arrives before the hardware decision, and whether original customers will actually buy the resulting service. Mathematical values below are explicitly synthetic normalized **captured contribution** for complete customer–robot–operator production policies. No robot, customer, certification or scientific originality has been established.

## Which technical moments make source data economically useful?

Fix a source/acquisition architecture, lawful original-customer offer, customer regime θ in {A,B} with probabilities 1/2 each, and signal Y in {A,B} with symmetric accuracy α in [1/2,1]. An independently admitted incumbent R delivers contribution 2 in either regime. A qualified specialist E_A or E_B delivers 4 in its matching original-market regime and 0 otherwise; the operator may decline that specialist and run R **only if the complete fallback is separately physically approved**. Net resource, price, service and rights terms are held fixed at this stage. The report must be available before permitted dispatch where used.

Let Q_A,Q_B be the *joint development qualifications* resulting from the source-data training programme on the SAME controlled version of models, embodiments, operator/recovery plan and original customer tasks. Define p_A=P(Q_A=1), p_B=P(Q_B=1), q=P(Q_A=Q_B=1). These are development-program probabilities, not per-movement accuracy or additive data-transfer coefficients. Assume first that (Q_A,Q_B) is independent of (θ,Y), is observed before hardware/dispatch decisions, and that target-report quality is unchanged by the source programme. This excludes endogenous customer-regime selection and changes in the source-conditioned observation kernel—both treated below.

The entire feasible law for a binary qualification pair is:

| outcomes (Q_A,Q_B) | probability |
|---|---:|
| (0,0) | 1-p_A-p_B+q |
| (1,0) | p_A-q |
| (0,1) | p_B-q |
| (1,1) | q |

Consequently the **sharp Fréchet qualification interval** is L=max(0,p_A+p_B-1) ≤ q ≤ U=min(p_A,p_B). Every q in that interval defines a nonnegative four-cell probability law. No independence assumption q=p_A p_B is warranted by separately reported benchmark passes.

## Conditional proposition: identical qualified marginals can have opposite value implications

Let b=2α-1. Compare THREE explicitly different, independently admissible complete deployment architectures, *not* three labels for a single robot:

**F — genuinely flexible specialist choice.** After the report, both qualified specialist embodiments or equivalent safely switchable configurations can be selected, and R remains genuinely available. If neither qualifies, value is 2; if exactly one qualifies, value is 1+2α; if both qualify, value is 4α. Therefore

    W_F = 2 + b(p_A+p_B).

**L — irreversible single-body selection before report, with certified R fallback after report.** One qualified specialist can be installed before the report, and the qualified incumbent may be selected after observing the report; there is no post-report specialist interchange. The value is 2 if neither qualifies and 1+2α if at least one qualifies:

    W_L = 2 + b(p_A+p_B-q).

**B — original buyer's joint certification bundle.** The full original customer service is *contractually and physically admissible only if both distinct qualifications are present*; if both are present the operator may select the report-matching specialist and obtain 4α, otherwise independently admitted R earns 2:

    W_B = 2 + (4α-2)q = 2+2bq.

The calculations require physical approval and the same original qualified, accepted and paid production environment for each architecture. They are not universal engineering predictions: a single body incapable of switching must not be credited with F, while a buyer who accepts either specialty cannot be modeled as B.

**Proof.** Conditional on Y=A, expected qualified E_A contribution is 4α and E_B contribution is 4(1-α), and R is 2. For α≥1/2 the matching specialist weakly dominates R, while the mismatched specialist does not. Under F, the four qualification patterns therefore produce conditional optimized values (2,1+2α,1+2α,4α). Under L, both qualifications cannot be installed after the report: both-qualified yields the same 1+2α as a single specialist; the optimal precommitment is symmetric A or B. Under B, the complete original service requires both qualifications, making only the (1,1) state eligible for 4α. Weight each value by its corresponding four-cell probability and simplify to the three identities. QED.

**Key comparative implications.** Holding both technical marginals fixed, increased joint qualification probability q:

- has **exactly zero** effect on flexible F in this stipulated disjoint-regime model (qualification effects add economically, though data acquisition need not);
- **reduces** locked L's value at slope -b (correlated qualifications duplicate pre-committed coverage);
- **increases** joint-certificate B's value at slope 2b (the customer needs the pair).

Thus the same technical source synergy can appear as economic redundancy, neutrality or complementarity, solely because policy timing and buyer qualification requirements differ. These are applications of elementary four-cell / Fréchet algebra, not a claim to a new general theorem.

### A distinct option-value identity

The exact gross option value of a physically verified post-report flexible body relative to pre-lock L is

    W_F-W_L = bq.

The ability to reconfigure is useful precisely in the development histories where BOTH specialists qualify, provided the report is informative. If once-counted incremental flexibility cost is c_F in the same normalized production units, then F strictly dominates L only when bq>c_F for the same original-customer horizon, embodied resource use and qualified production. With q only bounded, sufficient robust dominance requires bL>c_F, robust rejection requires bU<c_F, and otherwise the choice is unidentified. No further data premium is added to the dynamic J; these contributions are already in its optimized next-period value.

For p_A=p_B=3/5 and α=3/4, q may lie anywhere in [1/5,3/5]. F always yields 13/5, while L ranges from 5/2 (q=1/5) down to 23/10 (q=3/5). B rises from 11/5 to 13/5. Thus gross flexibility ranges from 1/10 to 3/10. At c_F=1/5 the F-versus-L preference **reverses** across observationally identical qualification marginals. Imposing independent Q would set q=9/25 and predict gross flexibility 9/50, net -1/50; neither independence nor this cost is measured. Every figure is an *internally consistent hypothetical contribution*, not inferred dollars or a robot success improvement.

## Where independence from the customer regime fails

The above “marginals plus q” result requires the development qualification vector to be exogenous to the original customer regime/report. This is particularly doubtful when production-generated data are selected by the existing deployment policy, when failures and recoveries are sampled disproportionately, or when a customer regime persists across training and deployment. The general correct finite object is

    W = sum_(Q,Y) P(Q,Y) max_(a in A(Q)) E[u(a,θ) | Q,Y],

where A(Q) is the independently admitted complete policy set. It cannot generally be reduced to a marginal qualification copula and one unconditional report accuracy.

**Sharp counterworld.** Let θ be equally likely A/B, Y reveal θ perfectly, and exactly one source-generated specialist qualify in each training/customer cohort. In World 1, only E_A qualifies in regime A and only E_B in regime B. In World 2, the qualifications are reversed by regime. Both worlds have p_A=p_B=1/2, q=0, exactly the same unconditional report accuracy and original customer regime frequencies. Yet safely flexible optimized gross service is 4 in World 1 and 2 in World 2 (R is retained). Therefore even *observing the full unconditional qualification joint law* does not identify the economic value of directional transfer if the source-development process and customer regime are endogenously matched. The worlds are distinguishable by a paired, regime-conditioned original-target development and buyer/robot observation, not by another marginal score. This is a counterexample, not measured negative transfer.

If a free optional data source merely enlarges the lawful menu without changing the incumbent option or cost, maximized V cannot fall. But costly training, a changed customer offer, endogenous collection, or forced controller replacement may lower its realized net production. None of the counterworlds claims that free optional information destroys value under an unchanged feasible set.

## Implications for the original X/G/E/R production and data-acquisition problem

X may change p_A, p_B, **and q**, not just a fixed positive additive T coefficient. G can improve target-report accuracy α, target alignment or physical observation/recovery; these are different causal interventions. E changes F versus L feasibility through hardware lead time, lawful body interchange, operator scheduling, supply chain and certification; B changes the complete service required by the original buyer. For fixed exogenous demand, a source-induced small change has marginal value b(d p_A+d p_B) under F but b(d p_A+d p_B-dq) under L, while under B it is 2b dq. The derivative is not a global one when new embodiment labels or approvals appear discretely.

The right comparison is the Bellman J of complete policies (current accepted production plus subsequent production, information, manufacturing and learning transitions minus real costs), with the **same** original buyer offer, qualified operator resources and customer capture denominator. Production-generated field/failure/recovery data, teleoperation, simulation, synthetic data and public/pretrained sources are separate interventions with distinct selection, rights, compute/curation and matched qualification kernels. They cannot be merged into a universal “number of demonstrations”. New evidence must measure complete multi-qualification outcomes and demand-conditioned report/action compatibility. Changing only q by manipulating a mixture may change the ranking only if the specified original-customer architecture makes q payoff-relevant; this is an empirical hypothesis, not an optimization recipe.

**Model A:** V remains the optimized original-customer complete-service production function with shared operator, acceptance, price, payment and outside-option constraints. F/L/B are tiny conditional examples of how qualification bundle structure alters the feasible recipe incidence matrix. In multilayer production, use the actual joint network; resource duals provide conditional upper certificates, not automatic realized cash.

**Model B:** Source X, target G, and embodiment E select both qualification law and post-information action/commitment possibilities. Joint event qualification may be learned and paid for; no independent “data shadow asset” is added to already optimized continuation value. Deliberate target audits may be valuable when they change the chosen acquisition or deployment action; routine production data may miss the low-support regimes where source/target alignment determines eligibility.

## Empirical discrimination, prior art, and unresolved proof gap

[Prospective original-customer design](JOINT_QUALIFICATION_TIMING_VALIDATION.md) specifies paired seed/model/embodiment qualification, report timing, signed physical fallback, complete original procurement and receipts, lawful full-cluster assignment, source lineage, and measurement of P(Q_A,Q_B|θ,Y,H), not just p_A,p_B. No such panel or approved live experiment was accessed. The next proof gap is economic valuation with **partially observed source–demand dependence** and explicit safe policy support, not another arbitrary q grid or a claim to passing the November 22 gate. If no admissible real policy data exist, bounds—not a forced empirical ranking—are the honest result.

Closest foundations: Fréchet bounds for binary dependence and reliability-style qualification events; classical Blackwell experiment comparison and reversible versus irreversible real options; DDA's future endogenous production-data valuation and complementary aggregation (https://arxiv.org/abs/2606.10127); ReMix heterogeneous imitation mixtures (https://proceedings.mlr.press/v270/hejna25a.html); and **DataMIL**'s task-performance-aware curation of robot training data (https://arxiv.org/abs/2505.09603, 2025). These papers do not supply original buyer-payment or physically approved complete customer-network observations for this numerical model. BEA (https://www.bea.gov/itable/input-output) and the official BLS input-output matrix (https://www.bls.gov/emp/data/input-output-matrix.htm, page last modified August 27 2026) identify quantitative production-network routes; the downloadable BLS ZIP was attempted but unavailable to this execution, so **no numerical interindustry edge** has been extracted here.

An exact `node joint_qualification_timing.js` program records finite integer checks across qualification joint laws and the displayed fractions; independent Python `fractions.Fraction` enumeration was executed separately on a matched model. Neither constitutes a proof of empirical transfer or scientific originality. November 22 acceptance and subsequent gates remain OPEN; theory remains the majority workstream through December 6; final target **December 25, 2026, 23:59 Eastern** remains unchanged.
