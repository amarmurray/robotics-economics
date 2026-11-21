# Calibration-gated source information and the same X/G/E/R original-customer decision

**20 November 2026, Eastern.** This extends *When Capabilities Become Production* and the preceding [three-source lineage construction](SOURCE_LINEAGE_HIGHER_ORDER_TRANSFER_AND_ECONOMIC_DECISION.md) without changing the paper's question. Its distinction is substantive: a source-trained signal can discriminate a customer regime yet fail to create a qualified, paid service. The previous synthetic signal example assumed a correct selection immediately produced a fully approved and accepted customer contribution. We explicitly isolate that assumption rather than transporting higher signal accuracy into actual robotic earnings. Results are conditional applications of standard probability and optimized decision theory, not independently demonstrated scientific novelty.

## One production objective, three separate empirical stages

Let X mean additional licensed source acquisition and admission (with a separate distinction between *new* collection and fixed-archive inclusion), G mean target grounding or reweighting, E mean a changed embodiment and R the already-qualified retained complete-service policy. Source trajectories from production, failures/recoveries, teleoperation, simulation, synthetic rollouts and public/pretrained representations are distinct mechanisms. An episode identifier is not an independent learning family; an accepted update is not a learned qualification; a correct held-out target signal is not an accepted *paid* customer service. A changed embodiment expands or changes the signed recipe menu; it is not just a new data modality.

Condition on one stipulated original buyer, a bounded common unit of accepted service, a separately physically authorized R earning 2 normalized contribution units whenever a new service cannot be offered, and a signed approved selected service contributing 12 when successfully fulfilled, accepted and paid. The complete X or G program costs 1/4; E has independently stipulated net contribution 10. No observed robot, deal, receipt or benchmark-to-dollar mapping supports these numbers.

For intervention a in {X,G}, let D_a indicate that its signal selects the nominally correct specialist for original-customer regime theta. Let A_a indicate **jointly qualified, physically allowed, complete, accepted and paid** service by that chosen specialist (including robot-controller, operator and buyer acceptance). Write p_a=Pr(D_a=1), r_a^+=Pr(A_a=1|D_a=1), r_a^-=Pr(A_a=1|D_a=0). Full customer/network policy must be the same arm throughout. By partitioning the paid-service event on D_a, the optimized value of this *fixed selected-policy with retained R* is exactly:

\[
J_a=\frac74+10[p_a r_a^++(1-p_a)r_a^-].\tag{1}
\]

Proof: expected captured service is 2+10Pr(A_a=1), and 1/4 acquisition cost is deducted exactly once. Equation (1) requires a feasible R after failure; failure cannot silently strand the operator or consume a nonrefundable customer obligation. The conditional r parameters incorporate physically qualified complete recipes and original customer receipts, not merely motion success. The generalized network analog replaces 10r^+ and 10r^- with **conditional optimized incremental captured original-service contributions**, accounting for scarce robot/operator/access resources, retained alternatives, customer demand, rights, displacement and discounted continuation once. No positivity of data's technical transfer is presumed.

## Qualifying robots can eliminate the economic price of better source information

The preceding source-lineage model proved that with marginal target-error 1/4 and pairwise wrong 1/16, the unidentified triple wrong mass t in [0,1/16] gives optimal three-signal selector accuracy p_X=13/16+2t. Grounding yields p_G=7/8. Those are **inference probabilities only**. Suppose additionally that for both interventions a correctly selected whole service qualifies and earns incremental contribution with the common probability r, while an incorrectly selected service cannot do so: r_X^+=r_G^+=r and r_X^-=r_G^-=0. Under exactly these transport and qualification assumptions,

\[
J_X(t,r)=7/4+10r(13/16+2t),\quad J_G(r)=7/4+35r/4,\quad J_E=10.
\]

Thus X−G = 10r(2t−1/16). For r>0, t=1/32 remains their pairwise threshold, but the entire incremental economic benefit contracts with qualification/acceptance reliability; at r=0, higher signal accuracy has zero value. These are conditional customer contribution units, not general wages or revenue per demonstration.

**Proposition (embodiment-gated perfect source-audit value).** Suppose t is equally likely to be 0 or 1/16, and can be learned perfectly before the firm irreversibly chooses one of X, G or E. The audit is initially free and does not itself change r, signed policies, demand or costs. The gross incremental value of its information, defined as the difference in **optimized program production values**, is exactly

\[
\mathcal V(r)=
\begin{cases}
0,&0\le r\le22/25,\\
(75r-66)/16,&22/25<r<33/35,\\
5r/16,&33/35\le r\le1.
\end{cases}\tag{2}
\]

Proof: Source endpoint accuracies are 13/16 and 15/16, so X's unconditional average equals G's 7/8 accuracy. Low-t X is dominated by G; high-t X dominates G. Ex ante the best fixed plan is max(G,E). Following an audit the low-t optimal plan is max(G,E) and the high-t plan is max(X_high,E). The value is therefore [max(X_high,E)−max(G,E)]/2. X_high crosses E=10 at r=22/25 and G crosses E at r=33/35; substituting yields (2), continuous at the breakpoints. This is one objective and already includes X/G program costs: adding a second future-data premium would double-count.

At r=4/5, even high-t X is 37/4 and G is 35/4, both below the independently signed E=10. A perfect higher-order source-lineage audit therefore has **zero investment value** despite being technically informative. At r=9/10, G=77/8<10 but high-t X=163/16>10: an audit can switch the high-t state from E to X and has stipulated value 3/32. At r=1 it recovers the earlier 5/16 perfect-audit value. These two thresholds arise only from this one hypothetical original buyer/qualified-embodiment value table.

## Counterworld and partial-identification proof

A source-accuracy ranking is not a robot-production ranking. Hold the entire observed three-signal error distribution at t=1/16 (X accuracy 15/16, G accuracy 7/8). World I supposes both correct-selected policies always qualify and are paid: X=89/8, G=21/2, E=10; X wins. World II supposes X's correct-selected complete-service reliability is only 1/2 while G's is 1, and both wrong-selected increments are zero: X=103/16, G=21/2 and E=10; G wins. Source prediction observations are identical across these worlds. The worlds would, correctly, be distinguished by original-customer joint qualification and acceptance experiments. This is a counterexample against transporting diagnostic accuracy without calibration, not proof that higher-order data cannot improve learned controllers.

Suppose eligible matched trials bound each arm's r_a^+ in [ℓ_a^+,u_a^+] and r_a^- in [ℓ_a^-,u_a^-], with known p_a. Under **rectangular feasibility** of conditional Bernoulli laws, the sharp bounds are

\[
\underline J_a=7/4+10[p_a\ell_a^++(1-p_a)\ell_a^-],\quad
\overline J_a=7/4+10[p_a u_a^++(1-p_a)u_a^-].
\tag{3}
\]

Proof: (1) is increasing in each conditional success rate, and any stated endpoint pair can be implemented by an admissible Bernoulli completion. A separately rectangular X and G model makes lower-X minus upper-G and upper-X minus lower-G sharp bounds on their difference. If shared controller weights, customers or treatment potential outcomes constrain both arms jointly, the separate endpoints need not be simultaneously attainable: use the actual joint identified set instead. For an uncertain p interval, optimize the affine (3) over its endpoint p values according to the sign of ℓ^+−ℓ^- or u^+−u^-. With r wholly unknown, even an exactly audited p admits J_a anywhere between 7/4 and 47/4 under the stated model. Paid service outcomes—not accuracy alone—shrink this range.

A prospective matched **shadow-to-original-customer** validation can additionally bound drift. If the complete accepted-service outcome law for a fixed signed arm in actual deployment is within total variation ε_a of its properly matched shadow law, with payoff range exactly 10, then |J_a^customer−J_a^shadow|≤10ε_a. A shadow X−G margin exceeding 10(ε_X+ε_G) gives a robust positive ranking under common fixed costs and policies. This is the standard bounded-function TV inequality. An illustrative, **not observed**, ε_X=1/20 widens high-t r=9/10 X from 163/16 to [155/16,171/16], crossing E=10. Without independently justified ε or actual acceptance data, no numeric production ranking is certified.

## Constructive empirical identification and wider network fit

**Model A:** version-locked source lineage and rights, proposal/admission budget (fixed B versus fixed accepted K), modality, genuinely independent failure-recovery coverage, matched source–target truth and complete learned joint physical qualification. Archive inclusion and costly new data collection are separate treatment arms; optional original controller can be retained, but forced retraining or cost may reduce net value. No human-data master ontology.

**Model B:** separately approved signed customer/robot/operator network, all original offered/refused orders, true buyer acceptance, paid/refunded complete service, fallbacks, operator congestion, displacement and capture. Track r^+, r^- and E's feasibility on independent whole learner/customer units; do not condition solely on successful X deployments. Shared updating weights and pooled operators require closed-cluster or exposure-aware assignments. Policy-level causal effects may be identified with supported whole-network interventions even when the source mechanism remains uncertain. Data source attribution and precommitment audit information are different estimands.

Prior foundations are the law of total probability, Blackwell/EVSI, partial identification, bounded TV and resource-price-certified optimized production. *Data-Driven Automation* section 5 already values future data and production effects, Appendix B discusses aggregate complementarities. We claim only a conditional integrative implication, not novel mathematics. The [prospective evidence protocol](QUALIFICATION_GATE_EVIDENCE_PROTOCOL.md), [CPU exact executable](qualification_gate_value.js), [record](qualification_gate_value_results.json), [student](QUALIFICATION_GATE_EXERCISES.md) and [solutions](QUALIFICATION_GATE_SOLUTIONS.md) complement the previous three-signal proof. **No** learner, robot, physical approval, original customer paid receipt, direct BEA numeric IO relationship, full repository CI or independently reviewed novelty is demonstrated. November 22 scientific Model A/B gate remains **OPEN**, with theory majority through December 6 and final deadline December 25, 2026 23:59 Eastern.