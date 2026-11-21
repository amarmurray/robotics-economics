# Source-mixture support, higher-order paid-production interactions, and pooling transport

**21 November 2026 — continuation of When Capabilities Become Production, Nov22 Models A/B (scientific gate OPEN).** This develops the precise problem left by the isolation-versus-pooling bridge: can experiments with individual and paired source types transport to a whole pooled source mixture when learning, robot qualification, original-buyer demand and shared capacity are jointly optimized? The mathematical answer is conditional; no source-type scaling law is asserted.

## 1. Economic unit and interventions

Compare complete, physically and legally *eligible* whole-network investment programs a=SG (licensed heterogeneous source acquisition plus target grounding) and a=E (a changed robotic embodiment and its compatible policies). Other supported choices R, S and G, retained old or specialist controllers, deliberate versus production-generated learning data, manufacturing and digital coordination remain in the broader investment menu. The source *availability* coalition A is a subset of H={F,T,M}: F denotes field production episodes including failures/recovery, T licensed teleoperation episodes, and M simulation/synthetic episodes. Public/pretrained input remains an additional separately licensed source in the full model; three groups here are a tractable illustrative partition, not an ontology or claim of human-data supremacy. Split or recombine groups only if version and rights information permits.

At **one fixed original eligible buyer market N**, including never-accepted orders, define J_a(A) as expected optimized, qualified, buyer-accepted, finally paid production contribution over a predeclared horizon, after opportunity cost of displaced services, operator/robot/manufacturing/data rights, compute, curation, capital and grounding costs counted **once**. State policies must be approved and old fallback actually physically feasible. Buyer orders, delivery and prices can respond to a and A; only the original eligible market and exogenous assignment regime are held comparable. Future learning and production-generated data are already inside dynamic J, never another data premium.

For a costless optional source set expansion with unchanged exogenous demand, rights and technology, nested admissible policies imply gross optimized W_a(B)>=W_a(A) whenever A is a subset of B. This need not hold for *net* J if licensing/retraining is costly, or when adding sources forces a checkpoint, changes customer environments or removes an old policy. Negative transfer under one training recipe does not refute the nesting claim.

## 2. Exact coalition decomposition and its empirical content

For every source subset T, define the economic coalition dividend

    theta_a(T) = sum_{U subset T} (-1)^(|T|-|U|) J_a(U).

Inclusion-exclusion gives the exact identity

    J_a(H) = sum_{T subset H} theta_a(T).

For the economic SG-E contrast D(A)=J_SG(A)-J_E(A), dividends commute with subtraction. The *paired-source extrapolation* using only coalitions of size at most two is

    D_2(H) = D(FT)+D(FM)+D(TM)-D(F)-D(T)-D(M)+D(empty).

The exact unmeasured remainder is the third-order **economic** difference

    D(H)-D_2(H) = theta_SG(FTM)-theta_E(FTM).

More generally, with n sources and all supported coalitions up to k, D(H) is the sum of observed order-at-most-k dividends plus the order-above-k remainder. If externally defensible, simultaneous high-order restrictions |theta_D(T)| <= eta_T yield the valid outer interval [D_k-sum eta_T, D_k+sum eta_T]. Coupled costs, physical feasible sets or buyer demand can tighten it. For n=3, a directly supported interval for the signed third difference is exact without triangle relaxation. The interval is a *decision certificate* only if it excludes zero. It is not an empirical confidence interval: every input mean and restriction would separately need adequate observation and joint statistical coverage.

**Proof.** Substitute the definition and swap subset sums. A particular J_a(U) appears in sum_{T:U subset T subset H} (-1)^(|T|-|U|), which is (1-1)^(|H|-|U|): zero except U=H. The remainder and triangle bounds follow by subtraction. This is standard Möbius inversion/Harsanyi-dividend mathematics, not a novel theorem.

Crucially, measuring every individual and pairwise *technical* transfer does not identify these economic differences. Program-specific optimized J incorporates *joint task qualification*, buyer acceptance, shared operator slots, adaptive choice, data rights and payment settlement. All lower-coalition J values must refer to the same target market and allowed intervention architecture. Results from one-source **islands of size m** are not automatically J_a^N(F) at target-market size N; the preceding pooling bridge's scale and graph-cut remainder still applies.

## 3. Two sharp observationally indistinguishable pooled-choice counterworlds

Use hypothetical *normalized paid contribution* units, with no incremental source acquisition cost and old policies retained. For each program, the fixed target N outcomes for the empty coalition, any singleton and any pair are 2, 2.1 and 2.5, respectively. These seven values are the same for SG and E in both worlds. All observed one-source, pairwise, joint qualification, operator and paid-service responses can be compatible with those economic means.

Only the fully combined source mixture differs:

| World | J_SG(FTM) | J_E(FTM) | SG minus E | third dividend SG | third dividend E |
|---|---:|---:|---:|---:|---:|
| SG-compatible pooled training | 3.5 | 2.7 | +0.8 | +0.3 | -0.5 |
| E-compatible pooled training | 2.7 | 3.5 | -0.8 | -0.5 | +0.3 |

The lower-coalition Möbius extrapolation predicts 3.2 for **each** program, hence zero comparison. In both worlds every extra optional source only weakly increases each program's contribution; both satisfy a stipulated 3.5 physical buyer-paid capacity ceiling. Thus optionality, matching all singleton/pair outcomes and even nonnegative own-program transfer cannot determine which investment wins when three compatible types are jointly available.

Under only the lower-coalition observations, optionality and a defended ceiling 3.5, each full-program contribution lies in [2.5,3.5], and the **rectangular outer** SG-E interval is [-1,+1]. With a separately defended full-program lower bound 2.7 (not inferred from those observations), it sharpens to [-0.8,+0.8], whose endpoints the two worlds attain. The narrow bound is *conditional*, not an identified real fleet interval. The exact executable enumerates 121 monotone completions on a tenth-unit grid; integer enumeration checks the algebra but is not the proof.

## 4. When pairwise evidence *can* transport, and why it often cannot

**Separable bounded-source-neighborhood sufficient condition.** Suppose at the same N target market:

    J_a(A) = sum_{i=1}^N f_(a,i)(A intersect H_i) - C_a(A),

where every original buyer's entire reoptimized service, demand, operator resources and learning exposure are closed within H_i, each |H_i|<=k, and the aggregate rights/compute/manufacturing cost C_a is itself k-additive as a source-coalition set function. Then theta_a(T)=0 for every |T|>k. Hence the paired-source extrapolation is *exact* for k=2, including the SG-E comparison.

**Proof.** For any higher-order T and each f_i, select a source t in T outside H_i. Its inclusion-exclusion terms cancel pairwise between U and U union {t}; the k-additive C term likewise has no higher-order dividend. Linearity establishes zero. Reoptimization *inside* each closed f_i is allowed. The substantive assumptions are buyer/learner/operator closure, unchanged contexts and no unaccounted global network constraints—not independence of all task qualifications.

The condition is restrictive. A shared foundation-model checkpoint, a single recovery operator pool, cross-market order substitution, common manufacturing bottleneck, or source-conditioned embodied controller can create a three-way **economic** interaction even if engineering reports only pairwise data effects.

**Two direct falsifiers of technical-order truncation.** Let the robot's latent qualification score be exactly additive, q(A)=|A|, with a safe paid service paying 8 only when score reaches 3. Then J(A)=8*1{|A|=3}, and its third-order economic dividend is +8 despite *zero* third-order term in q. The qualification/paid-service threshold created the complement. Conversely J(A)=min{|A|,2}, representing saturating accepted paid capacity, has third-order dividend -1 despite additive technical inputs and monotone gross production. With changes in original demand, the sign and extent can change again. A stable engineering transfer functional form does not certify a low-order **paid** value functional form. These are familiar threshold and resource-rationing mechanisms.

One can use source-coalition structure for a **bounded** remainder without asserting exact zero only if its *global high-order economic finite differences* can be bounded over relevant licensed regimes. A local benchmark interaction, a shadow price at one production basis, or one missing-edge derivative is not that bound. Uniform upper restrictions must cover all downstream trained descendants, reoptimized customer orders, displacement and settlements, just as in the pooling edge-cut chapter. Avoid multiplying hypothetical local skill effects by wages.

## 5. Buyer-market composition is a separate transport equation

Even if all coalition effects are correctly characterized on experimental islands, target-market composition may change the investment ranking. Under the **additional falsifiable** assumption of stable class-conditional complete buyer-paid effects mu_(a,c,e), physically closed exposure classes e and no cross-class operator/learning constraints, the target paid contrast is

    Delta_target = sum_(c,e) n_target(c,e) [mu_SG(c,e)-mu_E(c,e)] - Delta_cost.

Target exposure weights n_target must be observed over *original eligible orders*, not accepted-only survivors. For identical per-class SG-E paid differences (3,0,-3), hypothetical island class weights (1/3,1/3,1/3) imply a tie; target original-buyer weights (1/2,1/3,1/6) imply SG advantage +1. These are normalized buyer-class economic contributions, not robot benchmarks.

If target classes/exposures have no counterpart in the lawful experiment, transport is unidentified unless the missing-class paid outcomes have externally justified bounds. With bounded missing-class contributions [L,U] and unsupported original-buyer mass u, the missing *average contribution* adds an interval of width u(U-L) for **each** program (their contrast requires a joint bound). A common global model or cross-class dispatch breaks the additive class equation entirely; then the valid estimand is the whole-network J and one must return to the full exposure design or defend a complete network sensitivity bound.

## 6. Evidence decision and roadmap connection

For the immediate choice **SG versus E at the planned full pooled market**, an authorized, adequately replicated **whole-program, all-source** comparison with original-buyer paid contribution is sufficient to identify the program-average decision effect under valid network-cluster assignment. It does **not** require all seven lower source coalitions or latent cross-world coupling. Those factorial comparisons matter for mechanism identification, transfer to *untested* source mixtures, and deciding whether to acquire more source data, change grounding, or create a new embodiment. Conversely, if safety/rights block full-mixture SG or E, no number of single/pair demonstrations identifies the unrestricted third-order paid-production remainder.

A useful empirical program would pre-register F/T/M provenance, rights, source volumes and checkpoints; signed complete robot/grounding/embodiment policies and permitted old fallbacks; original buyer/order demand and prices including noncustomers; joint complete-service qualification; recovery/teleop/opportunity costs; actual delivered accepted service and final paid/refunded settlement; all data-to-checkpoint-to-buyer links through the full horizon. Observe matched *source mixture availability* and *actual training recipe adoption* separately. Include changed downstream model embodiments, production-generated new data, customer mix and manufacturing/coordination spillovers. Randomize only genuinely closed entire networks with verified legal and physical support, not correlated trajectories as nominal replicas.

**Research interpretation.** We now have a precise hierarchy: (i) direct same-market full pooled program outcomes when supported, (ii) reweighting under validated local customer-exposure stability, (iii) low-order source-coalition reconstruction under validated **economic** locality, (iv) partial identification with audited full-economic tail bounds, and (v) no sign conclusion if neither full-arm support nor credible closure/bounds exists. The first paper can state this hierarchy as a candidate integrated production argument; the broader work retains multilayer production/value chains, directional heterogeneous learning, demand/coordination/manufacturing and rights/ownership.

**Closest foundations, not originality claims.** Möbius decomposition and cooperative-game dividends trace to Harsanyi, *International Economic Review* 1963, doi:10.2307/2525487; source interference/transport to Hudgens & Halloran (2008), Aronow & Samii (2017), and recent network exposure-misspecification research (Schröder et al. 2026, arXiv:2602.03459). Gao et al. (2024, arXiv:2403.05110) study robotic compositional generalization, while Hejna et al. (2024, arXiv:2408.14037) study data-mixture optimization in robot imitation learning. These do not establish original-buyer paid economics. *Data-Driven Automation* (arXiv:2606.10127) already explicitly values future data in §5 and discusses complementarity in Appendix B. The contribution here is a **candidate applied economic synthesis and falsifiable identification hierarchy**, not an independently established new mathematical result.

[Prospective evidence design](SOURCE_COALITION_TAIL_EVIDENCE.md), [synthetic exact JS](SOURCE_COALITION_TAIL_EXACT.js), [record](SOURCE_COALITION_TAIL_RESULTS.json), [independent rational checker](source_coalition_tail_independent.py), separate [exercises](SOURCE_COALITION_TAIL_EXERCISES.md) and [solutions](SOURCE_COALITION_TAIL_SOLUTIONS.md) accompany this extension. **Scientific Nov22 gate remains OPEN**: no signed target-size full-mixture programs, source-to-joint qualification field data, original-buyer payment cohort, network influence audit, BEA/BLS numeric interindustry crosswalk, full repository CI or independent novelty review. Theory majority to December 6; final December 25, 2026, 23:59 Eastern unchanged.
