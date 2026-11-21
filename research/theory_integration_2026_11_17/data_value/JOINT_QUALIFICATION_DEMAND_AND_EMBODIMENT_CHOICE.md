# Joint qualifications, demand, and the source–grounding–embodiment choice

**21 November 2026 | Continuation of *When Capabilities Become Production* (November 22 Models A/B). Conditional derivations, no measured robotic returns or independent novelty claim.**

## The next economic question, not a new toy research agenda

The previous chapters establish that training-source signal exposure, episode independence, joint error law, target-grounding information and report-conditioned paid outside opportunities are distinct. They end at the same missing bridge: **does technical improvement change the *jointly qualified, accepted, original-buyer production recipes* enough to justify buying new source episodes, grounding an existing archive, or manufacturing a new embodiment?** Repeated variation of the fixed-learner outside-slot shadow price cannot answer this. Its empirical identifying restriction remains unproven. This chapter retains that result conditionally and moves to the whole-program comparison that the November 17 agenda calls for.

Let \(s\in\{0,1\}\) denote inclusion or acquisition of a genuinely specified source-data intervention (hold the origin, archival lineage, admission budget and rights explicit); \(g\in\{0,1\}\) denote target **training** grounding/reweighting (not a free predecision observation report); and \(e\in\{0,1\}\) denote investment in a new robotic embodiment and its operator, manufacturing and service recipe. They are factorial *program definitions*, not source-data origins. Existing field trajectories, failure/recovery episodes, teleoperation, simulation, synthetic trajectories and public/pretrained inputs are separate source families whose proposed/accepted updates and independent lineage must be recorded. Old models \(R\), older signed dispatch rules and no-action remain available when physically and contractually feasible.

For a fixed original customer offer cohort \(d\), capacity/rights envelope \(N\), signed controller version and deadline, a whole-learner training intervention \((s,g)\) induces binary **joint service qualification** \(Q=(Q_A,Q_B)\). Qualification means the *complete* legal robot/operator/service recipe can attempt and safely satisfy the target, including recovery, acceptance and billing conditions; it is not a per-frame accuracy score or a benchmark percentage. Write
\[
p_A^{sg}=\Pr(Q_A=1\mid sg,d,N),\qquad
p_B^{sg}=\Pr(Q_B=1\mid sg,d,N),\qquad
h^{sg}=\Pr(Q_A=Q_B=1\mid sg,d,N).
\]
Probabilities are taken over declared training seeds, target environments and/or eligible offered service units, holding their sampling interpretation fixed. A joint distribution is meaningful only when both recipe qualifications have been measured on the **same** target unit or learner/cluster with a predeclared rule. A/B must not be computed from independent benchmark tables.

Define \(F_{e,d,N}(Q)\) as the *optimized* original-buyer and competing-buyer accepted/paid contribution, with actual robot/operator capacity, fallback, deadlines and refunds, over all **signed physically feasible** dispatch recipes available after certification. It is already net of displaced orders and operating costs (but not the separately declared capital/program outlays below). An attainable outside paid order \(\lambda_y\) enters the optimization only if that competing order is eligible, signed, and truly feasible. It is never inferred from a sector LP's dual variable. Let \(f_{ij}=F(i,j)\); set
\[
r=f_{00},\quad a=f_{10}-f_{00},\quad b=f_{01}-f_{00},\quad
\kappa=f_{11}-f_{10}-f_{01}+f_{00}.
\]
Then, exactly,
\[
V_{sg}(e,d,N)=\mathbb E F(Q)=r+a p_A^{sg}+b p_B^{sg}+\kappa h^{sg}.\tag{1}
\]
This is the binary Möbius/multilinear identity, not a novel functional form. Where qualification merely adds optional service policies to a common network, \(a,b\ge0\) and \(f_{11}\ge\max(f_{10},f_{01})\), but **\(\kappa\) has no fixed sign**. Two simultaneously valuable recipes may be complementary (a buyer buys a qualified end-to-end bundle) or substitutes (one operator slot can serve only one of them). The policy menu, contribution coefficients and target demand are to be reoptimized when embodiment or market demand changes.

### Proposition: interaction and its exact partial-identification envelope

For fixed \(e,d,N\) and the same post-certification value table \(F\), write \(\Delta_{sg} x=x^{11}-x^{10}-x^{01}+x^{00}\). Then
\[
\boxed{\ \Delta_{sg}V=a\,\Delta_{sg}p_A+b\,\Delta_{sg}p_B+\kappa\,\Delta_{sg}h.\ }\tag{2}
\]
The last term is a **joint-qualification transfer interaction**; a finding that source or grounding separately improves each task's marginal qualification probability does not identify its sign. When only the eight marginal probabilities are measured, every arm's joint success probability independently satisfies the sharp Fréchet interval
\[
L_{sg}=\max(0,p_A^{sg}+p_B^{sg}-1)\le h^{sg}\le
U_{sg}=\min(p_A^{sg},p_B^{sg}).\tag{3}
\]
Let \(M=a\Delta p_A+b\Delta p_B\). If \(\kappa\ge0\) and there are **no further** restrictions linking cross-arm joint laws, the sharp interval is
\[
M+\kappa(L_{11}-U_{10}-U_{01}+L_{00})
\ \le\ \Delta V\ \le\
M+\kappa(U_{11}-L_{10}-L_{01}+U_{00}).\tag{4}
\]
For \(\kappa<0\) interchange the two endpoints of the parenthesized bounds before multiplying. Proof: (1) applied to the four potential-program joint laws gives (2). Nonnegativity of the four binary cells \(h,p_A-h,p_B-h,1-p_A-p_B+h\) is necessary and sufficient for (3). Expression (2) is linear in each \(h\), so opposing Fréchet endpoints attain both extremes. Even if potential outcomes are defined on one superpopulation, independent coupling of arm-specific qualification vectors constructs a joint potential-outcome law attaining these endpoints in the absence of added restrictions. **A common training seed, mandated old-policy retention, shared infrastructure, selection or monotonicity can make that product coupling infeasible and tighten the set.** Use that actual joint identified set, not (4), when supportable. This is a sharp *conditional* partial-identification theorem, not a robotics empirical estimate.

If \(\kappa=0\), all joint information vanishes from (1) at that demand/capacity configuration: audited marginal qualifications are economically sufficient for this fixed table. If \(\kappa\ne0\), even perfect marginal calibration can leave the investment ordering undecidable. The same source episode can therefore have high value in a complementary end market and little or negative *incremental program value* in a substitutive one, without its technical transfer changing.

### Two counterworlds: same marginal technical progress, opposite economic investments

Consider a **hypothetical** target customer with optional old policy, two qualified services A and B, unit contribution \(f_{00}=0,f_{10}=f_{01}=2,f_{11}=12\). Thus \(a=b=2,\kappa=8\). Imagine a bundled original-buyer order is accepted and paid only when *both* full service recipes pass certification; this is not a benchmark-to-dollar conversion. All four training programs have identical observed marginal qualification rates across the two possible worlds:

| Whole-learner intervention | \(p_A=p_B\) | \(h\): both worlds except SG |
|---|---:|---:|
| R (retained old learner) | 2/5 | 1/5 |
| S (new source episodes) | 1/2 | 1/4 |
| G (target grounding of existing source archive) | 1/2 | 1/4 |
| SG (both interventions) | 3/5 | **1/2** or **1/5** |

Both SG joint values satisfy (3): \(h\in[1/5,3/5]\). All marginal technical effects are nonnegative and their cross difference is zero. Yet by (1), gross qualified service production is \(16/5,4,4,32/5\) in the **high joint-support** world and \(16/5,4,4,4\) in the **low joint-support** world, ordered R,S,G,SG. Consequently \(\Delta V=8/5\) versus \(-4/5\) respectively. The low SG forced recipe does **not** imply free optional source access reduces optimized firm value: its gross service value of 4 merely ties the S-only old checkpoint, which the joint program can retain. Its additional grounding cost can still make SG a poor *investment*.

Let S and G each cost 1/2 in the same abstract contribution units. E manufacturing plus qualified integration costs 1 and grants access to a separately qualified, signed service recipe worth **5** gross on this customer cohort, while retaining the original recipes. For a given \((s,g)\), E's feasible gross production is \(\max(V_{sg},5)\); all capital/program costs are subtracted once. Enumerating all eight feasible S/G/E investments gives:

| Program | High joint world: net | Low joint world: net |
|---|---:|---:|
| R | 16/5 | 16/5 |
| S or G | 7/2 | 7/2 |
| SG | **27/5** | 3 |
| E only | 4 | **4** |
| SE or GE | 7/2 | 7/2 |
| SGE | 22/5 | 3 |

Hence **SG is optimal only in the high joint-support world; E is optimal in the low world**, although all four marginal source/grounding qualification experiments report identical successes. E is an optional **embodiment recipe expansion**, not a purported training-data productivity coefficient. No actual robot is guaranteed to qualify for 5; that stipulation is part of the counterexample. Indeed gross SG is \(12/5+8h^{11}\), net SG \(7/5+8h^{11}\), whereas E-only net is 4; holding all other stipulated programs unchanged,
\[
\boxed{\ SG\text{ outranks E }\iff h^{11}>13/40.\ }\tag{5}
\]
The sharp technical Fréchet range \([1/5,3/5]\) crosses this *economic decision boundary*. A customer-specific **joint** held-out qualification study, paired with signed accepted-paid production terms, is decision-relevant precisely because marginal gains cannot settle (5). When the actual E alternative is weaker, rights/costs differ, or original demand and outside orders change, rederive the boundary rather than transfer 13/40 as a universal number.

**Demand and resource countertest.** Change *only* the customer/network to one shared operator slot, so a jointly qualified A+B system can serve one of the two equally valuable orders. Now \(f_{11}=2\) rather than 12, \(\kappa=-2\), and (2) gives SG cross effects \(-2/5\) in the high-\(h\) world and \(+1/5\) in the low-\(h\) world. The physical source-to-qualification laws are *unchanged*. Complementary data and task qualification are not the same as complementary customer revenues. For demand distributions \(D\), integrate \(F_{e,d,N}\) over the actual predecision offered-order distribution only if intervention \(s,g,e\) does not change that distribution; otherwise identify and solve the endogenous demand response as part of the complete policy.

### Full dynamic value, free options and future production data

Equation (1) is a one-cohort diagnostic inside the larger dynamic program, not an extra data premium. A minimal full program is
\[
J(z)=\max_{i\in\mathcal I(z)}\left\{-K_i+\mathbb E\left[C_i(z,\xi)+\beta J(z'_i)\right]\right\},\tag{6}
\]
where \(z\) includes model/embodiment capability, training archive rights and cluster lineage, buyer offers, operator availability, data generated by actual service, manufacturing, demand and future opportunities. S obtains distinct additional episodes, G-train changes alignment/admitted mix using an existing archive, G-observe produces an actionable fixed-learner report, and E changes the feasible production technology and potentially the future *data-generating state distribution*. Production-generated recovery data enters \(z'_i\) only once via continuation. If one evaluates a production policy with \(J\), **do not add** a Blackwell report value or a standalone "data dividend" again.

**Optional-data theorem.** If giving a learner additional *free, optional and rights-cleared* source data weakly enlarges the feasible set of trained checkpoints and the original old-policy/dispatch menu is retained, with no new curation, inference, time, compliance, storage or resource cost and unchanged demand, maximizing \(J\) over that nested set cannot lower value. A particular forced mixture **can** show negative transfer, and buying technically available data can be uneconomic. Distinguish these. A new physical embodiment need not enlarge the feasible set without cost: it may displace a production line, operator or site, and a new source data collector may alter future task exposure; do not assume the nested-set theorem across those constraints.

This conditional analysis exposes three mechanisms: **learning** changes the joint distribution of qualification; **production** assigns a demand- and resource-conditioned value to those joint states; **investment** selects the source–grounding–embodiment package net of one accounting of cost and future opportunity. The empirical discriminant is the full trajectory, not a single benchmark percentage.

## Evidence and closest foundations

The companion [matched whole-learner/original-order protocol](JOINT_QUALIFICATION_CHOICE_EVIDENCE.md) maps S, G-train, G-observe and E to separate causal interventions and data rights; distinguishes new independent source episodes from relabels/resamples; and specifies which matched buyer orders, jointly qualified policies, actual acceptance, refunds and competing-service receipts identify (5) in a lawful real deployment. No customer or physical study has been authorized or performed. The [exact integer executable](joint_qualification_choice.js), [record](joint_qualification_choice_results.json) and independent [Python Fraction checker](joint_qualification_choice_independent.py) reproduce these *synthetic* counterworlds. Separate [student exercises](JOINT_QUALIFICATION_CHOICE_EXERCISES.md) and [solutions](JOINT_QUALIFICATION_CHOICE_SOLUTIONS.md) cover identification and design.

**Prior art and non-novel components.** Binary joint-distribution Fréchet–Hoeffding bounds, multilinear expectation identities, Topkis-style complementarity, Blackwell information comparisons and finite decision selection are established mathematics. [A standard fixed-marginal analysis](https://link.springer.com/article/10.1186/2195-5832-1-14) and [Topkis, *Supermodularity and Complementarity* (1998)](https://www.jstor.org/stable/j.ctt7s83q) supply context (retrieved 21 November 2026). Farboodi–Koh–Xia, [*Data-Driven Automation* (arXiv:2606.10127)](https://arxiv.org/abs/2606.10127), already gives a dynamic role to production-generated data (including its §5) and treats complementary aggregation (including Appendix B). The conditional combination here is a candidate **robotics production identification architecture**, not a claim of a new general mathematical theorem, actual original buyer revenue or independently established scientific novelty.

## November 22 synthesis gate, still open

**Model A**: service qualification is a joint random vector, and value is the optimized signed original-buyer robot/operator production table, with demand-conditioned complementarity/substitution and outside-service opportunities established independently of a shadow price. **Model B**: entire source/grounding/embodiment programs alter the qualification law, future field-data exposure, physical recipe menu and dynamic opportunities. Within-model G-observe value is the earlier report-coarsening/Jensen calculation only when the learner and legal action support are unchanged; it cannot be added to B's total \(J\).

Formal claims now isolate a decisive estimand and an exact synthetic choice threshold. **Scientific acceptance still fails** for lack of real causal whole-learner joint qualification, complete customer order/paid opportunity policy support, attributable source lineage and a verified numerical official BEA/BLS transaction link. Neither reported student proof nor deterministic unit tests replace those. Theory remains majority workstream through December 6. The final 25 December 2026, 23:59 America/New_York deadline and the full manuscript, atlas, code, appendix and teaching roadmap are unchanged.
