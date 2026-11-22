# Endogenous original-buyer offers, shared production capacity and robotic data acquisition

**22 November 2026 — continuation of the same *When Capabilities Become Production* Models A/B; scientific gate OPEN.** This chapter follows [endogenous productive versus deliberate acquisition](ENDOGENOUS_DATA_ACQUISITION_AND_PRODUCTIVE_EXPERIMENT.md), [lawful reports](LAWFUL_REPORT_OBSERVABILITY_AND_IDENTIFICATION.md) and the [integrated Nov22 gate](NOV22_MODELS_AB_ARGUMENT_AND_GATE.md). It is a constructive *conditional synthesis* of familiar finite-capacity allocation, partial-identification and causal-interference mathematics, not a claim of novel foundational mathematics or observed robotic returns.

## Exact economic question

How does a robotics firm choose productive original-buyer work that generates data (P), deliberate target-specific collection/grounding (D), or new physical embodiment/capacity (E) when interventions alter which customer orders arrive *together*, and learned controllers compete for shared dispatch, recovery, model or organizational resources?

Let the treatment a be the **entire connected program**, not an individual selected robot episode. The history H_t records all eligible original customer offers including refused/no-order outcomes, approved physical service recipes and old retained controllers, legally usable buyer reports, provenance and rights for distinct source modalities, shared learner/model checkpoint, operator and embodiment occupancy, and net customer settlement. A safe and legal adaptive policy pi chooses production, collection, training and dispatch. The common complete economic value is

    J(a) = sup_{pi lawful under a} E_a[sum_t discount^t (cleared original-buyer receipts - operation, rescue, data, training, curation, manufacturing and other real costs)] - initial program cost(a).

The future value of data-induced learned services is already inside J, not a second data premium. No human/teleoperation input or single data modality is a master learning ontology: field trajectories, recoveries, simulated, synthetic, public/pretrained and deliberate target data induce possibly distinct and directional learner transitions. Preserving the old executable policy guarantees weak gross monotonicity for *free, optional information* only if the old entire policy, legal rights, feasibility and law of the environment remain available; compulsory data acquisition, scarce productive time or policy-induced demand do not meet that condition.

## Proposition: exact terminal original-buyer / operator-overlap identity

At one terminal original-buyer service window, two buyers A and B have legally and physically usable, predispatch-observed **eligible and qualified** order indicators Z_A,Z_B in {0,1}. These require (i) real original-buyer offer and willingness to pay under the stated contract, (ii) a safe qualified customer-specific recipe before dispatch, (iii) legal consent/report/settlement authority. They are NOT selected completed robot jobs. Let v_A,v_B be fixed nonnegative *net captured paid-service values*, including failure and payment risk appropriately, with other costs deducted. A physically scarce operator/organizational slot permits at most one service; optimized dispatch can choose the better offered lawful service; no additional future learning remains outside this terminal value.

The following holds pathwise:

    V_1(Z_A,Z_B) = v_A Z_A + v_B Z_B - min(v_A,v_B) Z_A Z_B.       (1)

Consequently, under a program-specific joint law K_a,

    J_1(a) = v_A m_A(a) + v_B m_B(a) - min(v_A,v_B) j(a),          (2)
    m_i(a) = Pr_a(Z_i=1),   j(a)=Pr_a(Z_A=Z_B=1).

No independence across qualifications, original buyers, source mixtures, shared models, rights or demand was assumed. If E actually creates *two independent, safe simultaneous service slots*, including independent recovery capacity, then V_2=v_A Z_A+v_B Z_B and the overlap penalty disappears. Merely purchasing two robot bodies with one operator does NOT meet this condition.

**Proof.** The four states 00,10,01,11 have optimum 0,v_A,v_B,max(v_A,v_B). The last equals v_A+v_B-min(v_A,v_B), proving (1); taking expectation proves (2). With two independent slots both eligible orders can run. These are standard finite-resource allocation identities; neither a trained policy's benchmark score nor a data-source marginal predicts the joint Z law.

**Conditional marginal learning value.** Suppose only B is newly qualified without changing existing A demand, rights, prices or capacity. Where B is offered but A is unavailable, newly learning B contributes v_B. Where A is already qualified and offered, incremental paid value is only max(0,v_B-v_A), not v_B. Even technically successful B transfer may be economically neutral in scarce A-priority states. When qualification *also* changes original-order arrivals or operator sharing, differentiation of (2) includes changes in both m_i(a) and j(a); it cannot be read from conditional technical trial success alone.

## Sharp per-program bounds and the selected-offer fallacy

If genuine original-buyer data establish only m_A,m_B (not their joint law), the feasible Fréchet interval is

    max(0,m_A+m_B-1) <= j <= min(m_A,m_B).

The four-cell probabilities are (1-m_A-m_B+j, m_A-j, m_B-j, j), hence both endpoints are realizable. By (2) the sharp conditional terminal paid-production range is

    [v_A m_A+v_B m_B-min(v_A,v_B) min(m_A,m_B),
     v_A m_A+v_B m_B-min(v_A,v_B) max(0,m_A+m_B-1)].             (3)

These are not physical or causal confidence bounds. A real shared learner may restrict the feasible copula. Bounds on P and D separately do not imply an exactly sharp difference bound if common latent customers, market responses or learner potential histories couple the two arms. With only **served and selected** robot successes, even m_A,m_B cannot be populated.

**Exact selected-log nonidentification.** The P robot always receives an A offer, always dispatches it with one slot, and gets a cleared receipt of 1. In world W0 no B customer offer exists. In W1 a legitimate B offer also always exists but goes unserved and unlogged. P's selected paid log is identical. A proposed D qualified menu can serve A for 2/5 or B for 2; it yields 2/5 in W0 versus 2 in W1, so the P-versus-D ranking reverses with the *same P selected paid logs*. The W0/W1 counterfactual D menu is stipulated, not observed or physically approved. The original eligible-offer registry (including rejections and when B offered) discriminates these worlds; another missing D potential-outcome support issue persists. Conditioning on treatment-affected selected jobs is not a general causal adjustment.

## A full-stack P/D/E investment reversal due solely to policy-dependent concurrent orders

Fix a fully **synthetic** two-date case with marginal eligible-and-qualified A and B order rates 1/2 under each program, legal predispatch order visibility, safe completed service conditional on offer, and no unmodeled data premium. In the first date P performs a paid productive source-data intervention earning 1/10 and consuming 1/10 in actual training/operator/curation resources (net zero); the learned menu qualifies A with paid value 1 and B with value 1/2 under one shared operator slot. D spends 1/20 on deliberate target data, retaining old A at value 2/5 and qualifying B at value 1, with one slot. E spends 1/5 on an additional genuinely independent physical/operator capacity; both original buyer services have value 4/5 and both simultaneous jobs are feasible. Original R remains optional where applicable. These are stipulated *full qualified customer payments and resource effects*, not accuracy percentages converted to money.

Let x_a=Pr_a(Z_A=Z_B=1) in [0,1/2]. Complete program contribution is

    J(P)=3/4-x_P/2,     J(D)=13/20-2*x_D/5,      J(E)=3/5.        (4)

The last expression assumes truly independent E slots, not merely two robots sharing human recovery. Two fully coherent counterworlds preserve **each buyer's marginal offered/qualified probability and conditional service value across worlds and arms**, but permit the original-customer joint order kernel to respond differently to the selected intervention:

| Structural counterworld | x_P | x_D | P total | D total | E total | Winner |
|---|---:|---:|---:|---:|---:|---|
| P separates, D synchronizes orders | 0 | 1/2 | 3/4 | 9/20 | 3/5 | P |
| P synchronizes, D separates orders | 1/2 | 0 | 1/2 | 13/20 | 3/5 | D |

At x=0 there is one A-only or B-only order with equal probability; at x=1/2 there are either both or neither with equal probability. A shared pre-intervention binary latent variable can generate the competing potential joint order responses, so these worlds are logically consistent. The causal *sign* depends on unobserved policy-specific joint demand/capacity response, not negative technical transfer. If P and E face a common x and cost/payments stay fixed, P and E tie at x=3/10; that is only a toy threshold. The learning/manufacturing/embodiment alternatives remain feasible options; this example does not claim any real customer responds in this way.

Economically this is a physical, digital and organizational complementarity: capable source-trained policies produce **saleable qualified recipes** only when original buyer orders, legal access and operator or robot slots coincide. Generalist E may buy concurrency rather than a higher benchmark score; deliberate D may improve B yet displace current paying training work; productive P may earn while learning but also induce order synchronization and consume a shared worker's scarce attention.

## General dynamic correction and where the proof stops

In the previously developed finite-horizon Bellman framework let K_a be the entire program-specific next-history law over customer orders, shared learner/model, rights, qualified recipes, physical and operator occupancy, with legally available choices. Let g_a include actual current accepted-paid receipts minus physical and data acquisition costs. Then J(a)=g_a+E_{K_a}V_a(H), where V_a is the **complete optimized continuation**, not a benchmark. For any common bounded reference function V_R on the union of supports, exact add-and-subtract algebra gives

    J(P)-J(D)=(g_P-g_D)
       + [E_{K_P}V_R-E_{K_D}V_R]
       + E_{K_P}(V_P-V_R)-E_{K_D}(V_D-V_R).                       (5)

The first bracket represents distribution/occupancy change *relative to an arbitrary reference*; the latter terms represent menu/continuation differences relative to that reference. This is not an identified mediated causal decomposition, and V_R need not be an executable physical/legal controller in all states. Transfer also changes future order formation and learning data; with successive services or prices dependent on orders, terminal (1) belongs inside the Bellman step, and arbitrary continuation complementarities may remain.

**Research obligations:** estimate or legitimately bound the joint original-buyer demand/qualification/learner/operator/rights K under physically authorized whole-network P/D/E; distinguish target alignment from demand telemetry; record no-orders and forgone orders; trace source, intervention, failure/recovery, simulation and new-embodiment data separately; verify legal predispatch observations. If no common whole-network assignment or adequate structural transport exists, leave investment ranking unidentified. This does not supply an actual official BEA/BLS interindustry coefficient; the separate published 2025 BLS sector output series is context only.

## Prior art, empirical falsification and reproducibility

This is a conditional combination of established single-resource and network revenue-management theory (Talluri and van Ryzin, *The Theory and Practice of Revenue Management*, 2004, DOI 10.1007/b139000; https://link.springer.com/book/10.1007/b139000), exposure under interference (Aronow and Samii, *Annals of Applied Statistics* 11(4), 2017, DOI 10.1214/16-AOAS1005; https://isps.yale.edu/resource/estimating-average-causal-effects-under-general-interference-with-application-to-a-social), and treatment-affected selection issues (Hernán and Robins, *Causal Inference: What If*, public 2024 text, https://www.hsph.harvard.edu/miguel-hernan/wp-content/uploads/sites/1268/2024/01/hernanrobins_WhatIf_2jan24.pdf). Public primary overview / source extracts checked 22 November 2026; the full sources were **not** replicated and no independent novelty audit was completed. DDA §5 and Appendix B already treat future data and complementary aggregation. The potential novel robotics contribution, if established, must arise from testable joint qualified-service/source-transfer/market-physical-capacity predictions and actual original-buyer evidence, not these algebraic identities.

Conditional empirical discriminators: a technical B skill gain may have zero additional paid B production where A already occupies the scarce operator; two bodies sharing one safety operator do not remove this; independently verified second operating capacity does. Original buyer offer, cancellation and refusal logs can distinguish demand displacement from poor technical transfer. A truly complete, authorized randomized connected-network P/D/E comparison can identify total original-buyer J directly under suitable independent assignment groups; selected robot-only trials cannot generally identify customer substitution, learner broadcast or whole-network effects.

[Executable exact finite model](endogenous_offer_network_exact.js) and [record](endogenous_offer_network_results.json) check the one-slot/two-slot identities across 41,184 exact integer feasible four-cell tables (123,590 assertions, counting probability consistency, both identities and the program examples). An independent Python Fraction calculation separately verified the headline two-world arithmetic, not a physical outcome or independent scientific theorem. [Prospective matched original-buyer evidence ledger](ENDOGENOUS_OFFER_NETWORK_EVIDENCE.md), [student exercises](ENDOGENOUS_OFFER_NETWORK_EXERCISES.md), [separate instructor solutions](ENDOGENOUS_OFFER_NETWORK_SOLUTIONS.md). Numerical execution does not substitute for the four-state proof.

**Next exact step:** build a simple *multi-date* lagged customer-order response with source-generated learned controller and shared operator updates, derive the whole-horizon original-buyer J difference, and state conditions for a joint K or valid sensitivity bound. Do not reopen finance-only theory; retain the full multilayer demand/production/manufacturing/rights/ownership roadmap. November22 science OPEN, theory majority through December6, final December25 2026 23:59 America/New_York unchanged.
