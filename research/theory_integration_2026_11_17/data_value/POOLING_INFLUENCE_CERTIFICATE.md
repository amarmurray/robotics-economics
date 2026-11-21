# A uniform whole-horizon learner-influence certificate for pooled economic source transfer

**21 November 2026; same *When Capabilities Become Production* and November 22 Models A/B synthesis. Scientific gate OPEN.** This continues [source-coalition tail theory](SOURCE_COALITION_TAIL_THEORY.md) and [isolation versus pooling](POOLING_BRIDGE_THEORY.md). The precise question is what *defensible* restriction on an omitted cross-source link is sufficient to transport original-customer **paid production** from supported one- and two-source SG/E programs to the untested all-source pooled program. No robot field calibration or novel mathematical theorem is claimed.

## Environment and the missing economic tail

Fix the same initial eligible original-buyer cohort and horizon H, including never accepted, failed, refunded, unserved and paid orders. Investment program a is SG (licensed heterogeneous source learning + target grounding) or E (new embodiment with its own feasible controller and manufacturing/deployment pathway). Both retain any actually permissible legacy/specialist fallback. Let the source availability coalition A be a subset of {F,T,M}, where F=field production, failure and recovery episodes; T=licensed teleoperation; M=simulation and synthetic data. Public/pretrained data, deliberate data collection and production-generated future data retain distinct provenance, rights and state transitions. Coalitions index *availability*, not compelled mixing or forced checkpoint replacement.

J_a(A) is expected optimized **full-horizon, qualified, original-buyer accepted and finally settled** production contribution in a specified target fleet/operator/customer network, with rights, compute, curation, operator time, displaced outside production, deployment/manufacturing and acquisition costs counted once. It includes new capabilities learned from production episodes and downstream demand/price responses; no second future data premium is added. Technical accuracy has no direct dollar multiplier. If free optional licensed information only expands feasible policies without altering other conditions, gross value is nested; net J need not be nested if extra source costs or forced updates arise.

For any source-coalition value function f, its three-way Möbius dividend is

    theta_f(FTM) = f(FTM)-f(FT)-f(FM)-f(TM)+f(F)+f(T)+f(M)-f(empty).

Let D(A)=J_SG(A)-J_E(A). With every size-at-most-two target-market program mean genuinely supported, define

    D_2 = D(FT)+D(FM)+D(TM)-D(F)-D(T)-D(M)+D(empty).

Then D(FTM)=D_2+theta_D(FTM), exactly. A pairwise *technical* interaction bound says nothing by itself about theta_D. A benchmark trained on isolated m-site networks also does not supply the fixed-target-market inputs D(A), as shown in the pooling bridge.

## Structural reference and coupling theorem

For each program a and coalition A, construct a **counterfactual, fully specified target-market reference** M0(a,A) that disconnects only predeclared nonlocal source/learner/operator/buyer influences while otherwise keeping the same initial buyer market, rights, resource accounts, signed policy menu and full-horizon stochastic reward definition. M1(a,A) is the actual target pooled regime. Both are histories of original orders, task-level and **joint** complete-service qualification, model/checkpoint lineage, robot actions, human recovery, prices, buyer acceptance, refunds, cleared settlement and future acquired data; these variables must remain in the state. Let V0_a(A), V1_a(A)=J_a(A) be their optimized expected contributions.

**Uniform trajectory-influence lemma.** Suppose both systems admit exactly the same nonanticipating physically legal policy class Pi_a(A) and initial state law. At each decision date t=1,...,h, conditional on any **common reachable history and action** for which both models are defined, the total-variation distance between complete next-event kernels (including reward, demand, qualification and payments) is at most delta_(a,A,t), uniformly across policies. Assume a common measurable realized full-horizon contribution is in [L_a(A),U_a(A)], of width R_a(A), under both systems. Then

    |J_a(A)-V0_a(A)| <= b_a(A)
       := R_a(A) [1 - product_t (1-delta_(a,A,t))].

The same bound applies to a fixed policy; optimization cannot invalidate it **because the menus agree**.

**Proof.** Run maximal couplings of the two complete next-event kernels while their histories match; use identical policy randomization. Conditional probability of agreement at step t is at least 1-delta_t, so agreement through the horizon is at least product_t(1-delta_t). When all events agree, the full realized objective agrees, including all downstream productive data and settlement. On mismatch, the payoff difference is bounded by R. Consequently every common policy's expected objectives differ by at most b. The elementary inequality |sup_pi f(pi)-sup_pi g(pi)| <= sup_pi |f(pi)-g(pi)| proves the optimized claim. This is a standard coupling/simulation-lemma argument, not new learning-economics mathematics.

**What the lemma does NOT say.** A shared operator bottleneck cannot be deleted if doing so changes the feasible action set. A new E arm need not have the same policies as SG; common-menu coupling is required only *within each a*, between M1 and its appropriate M0. If missing nonlocal links alter licensing rights, permitted actions, feasible manufacturing, customer contract terms or the reward map in ways not encoded and uniformly bounded in the kernels, b is invalid. Conditional TV estimated at a single baseline checkpoint, empty-source context or common frequent history is not a uniform all-coalition, all-history bound. A local LP shadow price, benchmark loss or marginal qualification score is not delta.

**Economic three-source tail theorem.** Assume **in addition** that each reference economic production function V0_a(A) is 2-additive across the three source types at the *same target market*, i.e., theta_(V0_a)(FTM)=0. Then

    |D(FTM)-D_2|
       <= sum_{A subset {F,T,M}} [b_SG(A)+b_E(A)].     (1)

If b_a(A)<=B_a for every coalition, a simple bound is 8(B_SG+B_E). Hence the target all-source SG/E paid-production difference lies in the interval centered on D_2 with that radius. A sufficient strict SG decision certificate is D_2 greater than the radius; a sufficient strict E certificate is D_2 less than minus the radius. The certificate is conditional and can be conservative because the true joint feasible model may couple errors across coalitions.

**Proof.** Substitute J_a=V0_a+e_a into the alternating three-way dividend. The V0 third difference vanishes, leaving eight alternating e_a(A) terms for each a. The coupling lemma bounds their absolute values by b_a(A); triangle inequality proves (1). No source marginal independence, fixed demand, linear production function or nonbinding robot capacity is assumed *inside the reference*, only its justified low-order economic structure.

**Stronger activation-local corollary.** If the architecture ensures **actual equivalence M1=M0 for every coalition containing at most two source types**, not merely that a few measured outcomes coincide, then b_a(A)=0 for |A|<=2 and

    |D(FTM)-D_2| <= b_SG(FTM)+b_E(FTM).              (2)

This is a stronger falsifiable statement: no cross-source learner/dispatcher/contract influence can activate until all three sources are simultaneously present, and the unobserved triple effect has a valid full-horizon conditional influence bound. Observing no difference in lower-coalition average paid outcomes does *not* prove this physical closure. If, instead, a direct all-source whole-network arm is authorized, valid original-buyer randomized means can identify the program-average D(FTM) without any of these low-order assumptions.

## Exact counterexample, sharpness and economically meaningful synthetic certificate

Use a **single eligible original-customer service** that pays 1 unit if accepted and finally settled, 0 otherwise. Thus each program's value is a Bernoulli paid-service probability; no benchmark percentage is converted to customer dollars. Let m=|A|. In the *two-local reference* define V0_SG(A)=(550+120m)/1000 and V0_E(A)=(150+120m)/1000. They are linear in source count, within [0,1], and have zero three-way dividends. Define s(A)=(-1)^(3-m), and actual pooled expected paid outcomes

    J_SG(A)=V0_SG(A)+s(A)/100,
    J_E(A)=V0_E(A)-s(A)/100.

A single Bernoulli event per program/coalition realizes these models. The program-specific Bernoulli next-event kernel is at TV distance exactly 1/100 from its reference, uniformly across all eight coalitions, and the whole-horizon reward width is 1. Every value function is **monotone** under added free optional information (the smallest one-source incremental change is still 0.10). The *observed* lower-coalition signed paid contrast gives D_2=13/50=0.26. The true full mixture gives D(FTM)=21/50=0.42, with third-order contrast 4/25=0.16. This attains the generic radius 8(0.01+0.01)=0.16 *exactly*, even under monotone source values, so one cannot generally replace 8 by a smaller universal coefficient without strengthening assumptions. The conditional evidence bound is [0.10,0.42], strictly favoring SG in the hypothetical model. Its economic sign, unlike the earlier counterworlds, is recoverable **only because a valid uniform whole-system delta restriction has been stipulated**.

If both pooled and localized regimes coincide for all lower coalitions and differ only at FTM by +0.01 for SG and -0.01 for E, then D_2=0.40 and D(FTM)=0.42. The stronger radius (2) is 0.02, giving [0.38,0.42]; the upper endpoint is attainable. Conversely, a model with exact equality on all seven lower coalitions but a triple-only paid effect of +0.10 makes every empty-context and pairwise benchmark check pass while invalidating any claimed *global* delta below 0.10. If one uses time-step deltas 0.01 and 0.02, the **conditional** whole-horizon mismatch probability is 1-(0.99)(0.98)=0.0298; this number is neither observed robot error nor an estimated paid outcome.

## Empirical discrimination and full roadmap

A scientifically usable certificate requires a physically allowed program/coalition comparison and an audit of *complete full-horizon kernel support*. Record all source/checkpoint ancestor links, target grounding and embodiment signatures, failed and successful attempted services, original eligible buyer orders including zeros/refunds, material/production coordination and operator displacement, and settlement. Enumerate uncommon safety/recovery and cross-market price/contract histories, not only frequent training sequences. Identify which conditional kernels can in fact be compared under licensed source access, physically approved controllers and independent learner/operator/buyer networks; no unauthorized experiments are implied. A defended high-probability **simultaneous** statistical statement about all required conditional probabilities could be propagated through (1), with its coverage and unsupported contexts stated, but no such data or confidence certificate exists.

The constructive scientific fork is explicit: (i) legally supported target-scale SG/E all-source original-paid arms; (ii) auditable genuinely 2-local target-market economic reference plus uniform downstream kernel influence restrictions; or (iii) honest partial identification without SG/E ranking. Test source locality jointly with market-class transport and full-network exposure. Do not erase manufacturer capacity, fleet coordination, end-market demand, digital agents, ownership/rights, cash constraints or new embodiment feasibility from the broader work. This certificate is intended as a **conditional layer**, not a claim that recursive robotics firms inherently satisfy small total-variation errors.

**Closest prior art.** The coupling is standard controlled-process comparison, related to Iyengar, *Robust Dynamic Programming* (2005), DOI [10.1287/moor.1040.0129](https://doi.org/10.1287/moor.1040.0129), and Nilim & El Ghaoui (2005), DOI [10.1287/opre.1050.0216](https://doi.org/10.1287/opre.1050.0216). Exposure support and network interference connect to Aronow & Samii (2017), DOI [10.1214/16-AOAS1005](https://doi.org/10.1214/16-AOAS1005). Möbius inclusion-exclusion and Harsanyi dividends are established. *Data-Driven Automation*, arXiv:2606.10127, already treats future data's effect on production and complementary aggregation. The application to recursively optimized **qualified, accepted and paid original-customer production** is a candidate synthesis, not independently established novelty.

[Evidence protocol](POOLING_INFLUENCE_EVIDENCE.md), [exact synthetic source](pooling_influence_certificate.js), [record](pooling_influence_certificate_results.json), [independent Python audit](pooling_influence_independent.py), and separate [exercises](POOLING_INFLUENCE_EXERCISES.md)/[solutions](POOLING_INFLUENCE_SOLUTIONS.md).

**Acceptance:** November 22 scientific gate OPEN. No signed physical SG/E comparison, customer-paid cohort, measured learner kernel influence, justified 2-local reference at target fleet scale, actual total reward bounds, official numeric BEA/BLS I-O edge, full repository CI or independent novelty review. Theory priority through December 6. Final delivery date December 25, 2026, 23:59 America/New_York, unchanged.
