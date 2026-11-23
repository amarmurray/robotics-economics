# Reachable-state, buyer-value-weighted data transfer with no grounding history

**22 November 2026 (Eastern).** Continuation of *When Capabilities Become Production*, not a new disconnected estimand. November 22 scientific acceptance remains **OPEN**. This is a **conditional mathematical construction**, not observed robotics profit or established novelty.

## The precise unresolved problem

The preceding [component-kernel proof](COMPONENT_KERNEL_IDENTIFICATION_AND_ECONOMIC_TRANSFER.md) separated cross-*distribution* sensitivity from cross-*unit* counterfactual disagreement. Uniform Q/D/J kernel total variation neither identifies the G transition when licensed target grounding has never been assigned nor bounds the actual same-customer P-versus-G potential-outcome mismatch. Can the original buyer's economic values, a *shared* worker's physical queue and genuine pre-action evidence still yield an implementable P/G/E investment certificate, without pretending a G sample exists?

The answer has two parts: (i) physical conservation provides a sharp **upper opportunity envelope** but no positive G success floor without a G-specific qualification-and-demand restriction; (ii) defensible G-specific marginal mechanism bounds can combine with the *one physically conserved queue* to produce a sharp, **value-weighted** interval and an ex-ante regret policy. The resulting bounds are conditional, not inferred from P histories.

## 1. Original-buyer production and conservation

At program commitment, choose P (production-generated source learning), G (licensed target grounding from already available data), E (genuinely new, independently staffed embodiment capacity), or retain lawful old service R. Program commitment is before the next queue state is revealed; no hindsight choice among programs is allowed. The initial worker backlog L0 in {0,1} is inherited from a common pre-intervention network; its law p_l is identified *only if* the pre-action registry is representative and intervention-independent. In period 0 a single worker processes at most one unit of recovery work. G may create J^G in {0,1} additional recovery jobs; there is no extra G-specific worker. Hence

    L1^G = max{0, L0 + J^G - 1}.

A date-1 original buyer provides **captured** contribution v_l >= 0 only when the program's target bundle is qualified and approved (Q^G=1), a *genuine customer* orders and settlement is verified (D^G=1), the required data-use/contract rights hold, and the shared worker is available (L1^G=0). The rights gate is part of whether G is legally admissible; a forbidden G is removed from the policy menu, not assigned a fictitious missing mean. This example assumes verified settlement whenever Q^G D^G=1, with actual empirical validation still missing. Write A^G=Q^G D^G, not a benchmark accuracy. For lawful G the gross incremental contribution is

    B_G = sum_l p_l v_l Pr(A^G=1, L1^G=0 | L0=l);

and net V_G=B_G-C_G, with any training/curation/license/deployment cost C_G deducted **once**. No independent "future data premium" is added: future services belong inside the complete production-value function. P's present paid learning, its downstream improvements and forgone worker capacity likewise enter P's full V_P; E has its own real manufacturing, power, staffing and operating constraints, not the G worker's capacity for free.

The model is a deliberately minimal terminal section of the earlier dynamic network, not a claim that all real worker queues are one-slot or that G necessarily creates failures. Q, D and J may depend jointly on unobserved customer, latent task and learner shocks; Q and D are **not independent**.

## 2. Sharp reachable-state theorem

Assume a nonnegative service value v_l; pre-action p_l invariant across programs; a work-conserving, program-invariant period-0 worker with one unit of service; no additional period-0 jobs except J^G; one future G target offer; and a fixed lawful original-buyer service recipe. In backlog-free stratum l=0, J^G <=1 clears by date 1, so the G service probability is q0=Pr(A^G=1|L0=0).

In backlog-one stratum l=1, worker availability at date 1 occurs **iff J^G=0**. Put q1=Pr(A^G=1|L0=1) and j1=Pr(J^G=1|L0=1). For any jointly feasible law,

    max(0,q1-j1) <= s1=Pr(A^G=1,J^G=0|L0=1)
                    <= min(q1,1-j1).                              (1)

Consequently B_G = p0 v0 q0 + p1 v1 s1. If external, intervention-credible restrictions give q_l in [a_l,b_l] and j1 in [c_1,d_1], and every combination of the stated marginal intervals is allowed, the **sharp** conditional bounds are

    p0 v0 a0 + p1 v1 max(0,a1-d_1) - C_G <= V_G
    V_G <= p0 v0 b0 + p1 v1 min(b1,1-c_1) - C_G.            (2)

**Proof.** The one-worker queue equation gives L1=0 identically for l=0, and L1=J for l=1. For two events A and {J=0}, their intersection is bounded by max(0,Pr(A)+Pr(J=0)-1) and min(Pr(A),Pr(J=0)), producing (1). Every endpoint is attained by the four nonnegative atoms (A,J=0), (A,J=1), (not A,J=0), (not A,J=1), with masses (s,q-s,1-j-s,j-q+s). Independent pre-action strata can be combined into one complete law, and nonnegative v_l selects the interval endpoints in (2). This endpoint sharpness **fails without modification** if there are cross-stratum, longitudinal, technical, cost or correlated potential-outcome restrictions: (2) is then only an outer certificate and one must optimize over the actual common-law feasible polytope, not independently select period endpoints. Q and D can be split inside A without assuming independent qualifications.

**No-free-identification corollary.** P-only buyer and queue logs, the shared worker law, and G's action-support zero provide *no* lower q_l for untried G. Allow q0=q1=0 and G generates no jobs: G produces no future paid service despite a free worker. Allow q0=q1=1 and J^G=0: every worker-cleared opportunity can be taken. Both can coexist with exactly the same complete P histories on one common potential-history probability space, provided G is lawful and no extra action-specific restriction exists. Therefore the physical-only bound is gross V_G in [0,p0 v0+p1 v1], minus admissible program cost, and cannot alone establish profitable G transfer. If G necessarily generates jobs, has known restrictions on service, or induces extra workers, replace the assumptions and recompute; do not silently use (2). This is a counterexample, **not** a claim that G necessarily has zero or unit real success.

**Engineering sufficiency, not observational identification.** If a genuinely defended G-specific lower bound on *joint* accepted-and-paid QD and upper bound on G incident probability exist, the lower bound in (2) can exceed the best lawful P/E value even without historical G assignment. But P performance, P-only operator logs, fixed pretrained scores or a logical maximum on job sizes do not certify a G **probability** bound. A G-specific sensor/hazard argument or a prospectively authorized externally valid test must support it.

## 3. One common-law counterexample, not independent program oracles

Synthetic, normalized, not measured: Pr(L0=0)=Pr(L0=1)=1/2, (v0,v1)=(2,4), C_G=0, Pr(Q^G D^G=1|l)=3/4 in each stratum, and Pr(J^G=1|l=1)=1/2. At l=1 two feasible G conditional worlds share all these margins but allocate the paid-versus-job atoms as follows:

| Atom conditional on L0=1 | Low service world | High service world |
|---|---:|---:|
| QD=1,J=0 | 1/4 | 1/2 |
| QD=1,J=1 | 1/2 | 1/4 |
| QD=0,J=0 | 1/4 | 0 |
| QD=0,J=1 | 0 | 1/4 |

Within each QD=0 cell divide mass evenly between (Q=1,D=0) and (Q=0,D=1). Then both worlds have Q and D marginals 7/8, *joint* QD=3/4 and J marginal 1/2. In l=0 hold the same (Q,D,J) distribution in both worlds; J cannot block the next service there. Thus the difference is in the job/qualified-demand **alignment**, not a changed technical pass rate, demand rate or job frequency. Complete observed P original-buyer, learner and worker histories can be made identical in both worlds by defining their P potential outcomes identically and varying only unassigned G responses. There is one law over all potential histories per world, not independently cherry-picked program success histories. Consistency holds for the realized P-only regime, and E has physically independent verified resources *by synthetic stipulation*.

The G contribution is V_G=3/4+2s1, hence the sharp interval [5/4,7/4]. Stipulate complete **net** V_P=3/2 and independent V_E=13/8, both program costs already counted. Then E wins the low-G world, and G wins the high-G world, with the same P observable evidence. This is an **economic** reversal despite matched G technical and buyer margins. An oracle with knowledge of the unassigned joint G law cannot be substituted for a precommitment policy.

**Robust decision.** More generally if p<=e and G lies in [L,U] with L<e<U, a precommitment lottery assigning G with probability x and E otherwise has worst-case regret

    max{x(e-L), (1-x)(U-e)}.

The minimax-regret fraction is x=(U-e)/(U-L), attaining (U-e)(e-L)/(U-L). With [L,U]=[5/4,7/4] and e=13/8, x=1/4 and worst regret=3/32; P is dominated by E *in this constructed menu*. Maximin expected net contribution instead chooses E, since its known 13/8 exceeds G's 5/4 lower bound. Regret and maximin answer different questions.

**What strong outside support would change:** with q0>=3/4, q1>=3/4 and a *separately defended* G-specific j1<=1/4, (2) forces V_G>=7/4, exceeding E's 13/8 in this case. This is not a result of observing the P worker or extrapolating a benchmark: without defensible G-specific q and j limits the condition has no empirical authority.

**Value and timing of an audit.** Under an explicitly stipulated 50/50 prior over the two synthetic G worlds, a *lawfully available before-commitment perfect report* of their true G response yields ex-ante value (13/8+7/4)/2=27/16 versus the no-report optimum 13/8, so gross report value is 1/16 before audit cost. A P-only report with the same distribution in both worlds has exactly zero Bayesian value for discriminating them. An identical perfect G report arriving *after* irrevocable program commitment also has zero investment-switching value (but may affect lawful dispatch if a future action remains). No claim is made that a perfect G report exists under zero G support.

## 4. Full-horizon network certificate and limits

For finite connected deployments let z denote a *single* legally feasible potential-history scenario encoding original buyer offers, learner checkpoints, data rights, acceptance/payment gates, recovery queue trajectories, alternative independent embodiment capacity, and reports actually observed by the decision date. Let mu_z>=0 sum to one. P-only selected histories constrain A mu=b after explicitly modeling selection; engineering/rights/work-conservation claims constrain C mu<=d. No G assignment means no hidden G-response moment may be inserted into A mu=b.

Every lawful **nonanticipative** contingent policy pi has its full production contribution R_pi(z) as a known function of an assumed scenario (including any continuation and all costs once). Define the common-law uncertainty set U={mu>=0: 1'mu=1, A mu=b, C mu<=d}. For a policy mixture x chosen before any revealed signals, guaranteed contribution is

    min_(mu in U) sum_pi x_pi sum_z mu_z R_pi(z);

the implementable maximin choice maximizes this over x. Under a finite U polytope, minima of each fixed x occur at its vertices; the maximin problem is a finite LP with one guarantee inequality for each vertex. For minimax regret use inequalities against **every** lawful oracle policy pi' and every vertex of U. A robust Bellman recursion that independently changes the G kernel at each date can be invalid here: a single physical recovery path and endogenous original buyer history couple periods and programs. The correct common-history LP preserves those links. A rectangular relaxation can furnish an outer conservative bound, but its selected worst histories need not come from one actual shared network law.

**Proof of LP reduction:** for fixed x, expected reward is affine in mu, so it achieves its minimum over a nonempty compact finite-dimensional polytope at a vertex. Max over the policy simplex x subject to each vertex inequality is linear. Regret relative to the best hindsight lawful policy is max over pi' of an affine function in mu and therefore also attains its max at a vertex. This is standard finite robust optimization; we do not claim polynomial scale for arbitrary networks or independent theorem novelty.

For a longer exogenous one-worker service schedule and no G-induced faster staffing, the no-new-job path is a pathwise **upper occupancy** envelope: adding nonnegative incidents never clears an inherited backlog sooner. The economic upper bound weights only reachable original-buyer paid opportunities, rather than uniformly pricing missed technical benchmarks. The envelope is **not** an automatically sharp multiday bound when serving orders generates additional tasks, receipts change demand, G changes staffing or distinct dates share the same customer budget. In those cases the whole law and policies must be modeled; per-period product bounds cannot simply be summed as though jointly attainable.

## 5. Prior work, falsification and empirical discrimination

The event-intersection bounds are classical Fréchet/Boole probability inequalities, not a newly discovered robotics scaling law. Missing unassigned-arm response is the standard causal-overlap / partial-identification problem. Finite robust dynamic control, especially rectangularity conditions, is established by Iyengar (2005, DOI 10.1287/moor.1040.0129), Nilim and El Ghaoui (2005, DOI 10.1287/opre.1050.0216); Goyal and Grand-Clément (2022 online, 2023 volume, DOI 10.1287/moor.2022.1259) explicitly examine dependence across transition sets. Farboodi, Koh and Xia, *Data-Driven Automation* (2026 NBER WP 35320), already models future data and complementary aggregation; neither is claimed original here.

What could falsify the *applied* economic certificate? A G program that changes pre-action backlog or worker capacity invalidates the assumed common L0 or exogenous shift. A target buyer who never pays on technically qualified service invalidates treating Q as revenue. A grounding action that can create multiple unresolved jobs invalidates J<=1. A target-data license that disallows the relevant use removes G from the legal menu. Different customer valuation conditional on queues requires audited v_l, not a static "robot productivity" multiplier. Multiple customers competing for the same service window require a full buyer-choice/queue allocation model, not independent order Bernoullis.

The [unpopulated original-buyer/worker and legal evidence protocol](REACHABLE_PAID_SERVICE_EVIDENCE.md), [exact finite checker](reachable_paid_service_exact.js), [record](reachable_paid_service_results.json), [replication](REACHABLE_PAID_SERVICE_REPLICATION.md), and separate [exercises](REACHABLE_PAID_SERVICE_EXERCISES.md) / [solutions](REACHABLE_PAID_SERVICE_SOLUTIONS.md) accompany the argument.

**Next exact proof gap, not a new question:** derive a tight three-date correlated-buyer/worker/learner bound using a common original customer budget and action-specific G job-service envelope. Determine which subset of allowed P-side history, engineering-certified invariants and a *lawful prospective* G mechanism probe could actually shrink the optimal policy regret, with reporter selection modeled explicitly. If no lawful G support exists, retain the nonidentified G policy ranking. Maintain the full manufacturing/embodiment, network diffusion and official quantitative production-backbone agenda. Nov29 and later gates remain open; theoretical majority through Dec6; **Dec25 2026, 23:59 America/New_York** target remains.
