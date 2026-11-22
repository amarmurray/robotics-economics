# Selected original-buyer histories and decision-sufficient economic data

**22 November 2026 — integrated *When Capabilities Become Production*, Models A/B.** This is a conditional theoretical extension of [the globally coupled multi-job model](GLOBALLY_COUPLED_MULTI_JOB_PRODUCTION.md), not real robotics evidence, a benchmark-to-dollar conversion, or an independently established mathematical discovery. All numerical receipts/costs are synthetic normalized *net qualified and accepted original-buyer production* units. The November 22 scientific acceptance gate remains **OPEN**.

## Question: which missing observations actually determine the data-versus-embodiment decision?

The preceding model correctly showed that even all pairwise incident/demand distributions fail to identify the joint multi-job economic opportunity. But the real field problem is harder: pilot policy assignment is selected and original buyer orders are often only visible when the robot can serve. This chapter asks whether **the decision** can be identified without observing every technical or market state, and derives observation-aware, rather than fully stipulated, economic bounds.

Preserve the complete physically coherent toy: P's t2 action T is qualified and receives the same current accepted net as safe R. T broadcasts a lawful target learner, creates two separate unit recovery jobs J and H at the end of t2, and t3 can discharge only one. A qualified site-2 original buyer X=1 is offered at t3 when J=H=0; dispatching it produces increment 1/2 and **creates** another worker job K=1. At t4 a distinct original buyer Y can earn net increment 1 only if the worker is physically available. Queue dynamics are B3=J+H and B4=max(0,B3-1)+K. R is optional and has a separately stipulated expected incremental value of 5/16 net of P's 1/8 purchase; G (lawful reused-data grounding) and E (extra robot plus independent operator) have complete incremental values 3/8 and 13/32. All branches retain the baseline safe production of 6. Do not treat post-dispatch settlement as information known before t2/t3 action.

For any **one** potential law under do(T), write

\[
p_{00}=\Pr(J=H=0),\quad q_0=\Pr(J=H=0,Y=1),\quad
q_1=\Pr(J+H=1,Y=1).
\]

**Proposition 1 — economic observation quotient.** For the full lawful T program, the three nonanticipative policy values, relative to 6, are exactly
\[
 V_R=5/16,\quad
 V_{\mathrm{wait}}=-1/8+q_0+q_1,\quad
 V_{\mathrm{serve}}=-1/8+\tfrac12 p_{00}+q_1,
\quad
J_P=6+\max\{V_R,V_{\mathrm{wait}},V_{\mathrm{serve}}\}.
\]
This is not a claim that (p00,q0,q1) is a sufficient Markov state for an arbitrary multi-date robot fleet. It is **only a payoff-sufficient statistical quotient for this full, fixed lawful policy menu**. The proof is exhaustive queue accounting: if two jobs enter at t2, one remains at t4; if exactly one enters, it clears before t4 and no K is admitted; if none enters, the site-2 controller either generates K and receives 1/2 now or waits and preserves the t4 original-buyer opportunity. Each payoff is counted exactly once. The retained R choice competes with both and keeps optional source-data availability from being miscalled negative transfer. \(\square\)

An implication more useful than recovering every marginal is that a truthful predispatch eligible-original-buyer registry could target these **two** Y/queue event groups and worker-zero probability. Full Y outcomes when J=H=1 do not enter any of these three payoffs. This statement fails if those histories affect future learning, buyer demand, rights, service costs, or a longer policy menu.

## Selection/censoring theorem: the common structural-law identified set

Let \(\omega\) be a complete feasible potential-history table containing action-specific learner/qualification, original buyer offers **and no-offers**, physical queue jobs, rights, and service/settlement outcomes. Let \(\mu\) be one distribution on these tables, used across P/G/E and all periods (not a separate favorable law for each arm). A registered action-selection and reporting process yields an observable distribution \(m=M\mu\), where M records chosen treatment/exposure, queue state, reporting mask S, and Y only where it is legally observed. If S can depend on unrecorded Y, include S jointly in \(\omega\); **do not** assume missing at random. Physical and licensing constraints form a closed nonempty support polytope
\[
\Gamma(m)=\{\mu\ge0:\mathbf1^\top\mu=1,\ M\mu=m,\ C\mu=c,\ D\mu\le d\}.
\]
For a fixed lawful policy i, \(v_i^\top\mu\) is complete original-buyer net production. Its sharp bounds are LPs over **this single set**. If \(\Gamma\) has a strictly positive relative-interior law on its admissible atoms and has only equality restrictions on that affine support, a fixed-policy payoff is point identified iff \(v_i\) lies in the row span of the augmented observation/constraint matrix restricted to that support. Proof: \(v_i^\top\mu\) is invariant along every feasible null-space direction precisely when \(v_i\) annihilates that null space. With active inequalities/boundary supports, test invariance directly by LP; unrestricted row-span assertions may then be too strong. This is standard linear identification/partial identification, not a new theorem.

An *investment decision* can be identified without identifying each value: use the same \(\Gamma(m)\) and the preceding [finite-policy envelope construction](GLOBALLY_COUPLED_MULTI_JOB_PRODUCTION.md) to bound \(\max_i v_i^P\cdot\mu-\max_j v_j^E\cdot\mu\). A uniformly strictly positive lower bound proves P dominates E among these lawful models; a strictly negative upper bound proves E dominates. An interval crossing zero leaves the choice unidentified. **Do not** substitute a logged policy's performance for every lawful counterfactual policy; do not use independently chosen row-wise worst cases as though one common network could realize all of them.

## Exact selected-history counterworld: logged success can hide opposite investments

Impose the preceding deliberately favorable **external** structural restriction that J,H,Y each have fair Bernoulli marginals and **all** their pairwise 2×2 tables are uniform. This does not follow from the selected records below. As previously proved, their entire compatible distribution is the parity family
\[
\Pr_\theta(j,h,y)=\begin{cases}\theta/4,&j+h+y\ \mathrm{even},\\
(1-\theta)/4,&j+h+y\ \mathrm{odd},\end{cases}\quad 0\le\theta\le1.
\]
Consequently \(p_{00}=1/4,\ q_0=(1-\theta)/4,\ q_1=\theta/2\). The wait policy never exceeds the best of R and serve, giving \(J_P=6+\max\{5/16,\theta/2\}\).

Now suppose all T-connected episodes register J and H, but Y is logged only in queue-one strata (J,H)=(0,1),(1,0), under a possibly **outcome-dependent** recording process S. In *each* such jh stratum the **unconditional** observable mass is: logged original Y=1 equal to 1/32, logged Y=0 equal to 1/32, and **missing** Y equal to 3/16; the total stratum mass remains 1/4. At jh=00 or 11 no Y is logged; the complete jh=00/11 mass is still registered. The selected log's apparent Y-positive rate is 1/2 in either queue-one stratum, independently of the truth.

**Proposition 2 — exact identified set given the stated parity restriction and recorded mask.** The observed data permit precisely
\[
\theta\in[1/8,7/8],\quad q_1\in[1/16,7/16],\quad
J_P-6\in[5/16,7/16],\quad J_P-J_E\in[-3/32,+1/32].
\]
For proof, each queue-one atom has true positive mass \(\theta/4\) and negative mass \((1-\theta)/4\). Observed positives and negatives must each exceed 1/32, giving \(1/8\le\theta\le7/8\). Conversely, for *any* theta in this interval, allocate logged mass 1/32 to each Y status and hide the remainder \(\theta/4-1/32\) positive and \((1-\theta)/4-1/32\) negative; their sum equals the stipulated missing 3/16. On queue-zero and queue-two histories hide all Y. This constructs a physically coherent full law with **identical complete observable selected-history distributions** at every theta in the interval, proving sharpness. The program expressions then give the asserted value interval. At theta=1/8, E > G > P; at theta=7/8, P > E > G. No benchmark skill or worker-use average changed. \(\square\)

The observed selected success rate 1/2 would falsely produce point identification if treated as representative of the censored original market. The extra third-order Y/incident event is not priced correctly by observing just successful invoices or by the untested assertion that recording is ignorable. Even granting *all pairwise outcome distributions externally*, a large decision-relevant interval remains.

## What would actually close the gap?

A **prospectively authorized and lawful original buyer offer/no-offer registry** can record buyer-eligible Y whether or not service is possible and regardless of eventual receipt, with timestamps, lost demand, safe Q, report timing, worker jobs, and rights. Under the parity family, directly identifying \(q_1=\Pr(J+H=1,Y=1\mid\mathrm{do}(T))\) suffices for P's full policy maximum because the other event moments are pinned down. In the unrestricted law, \(p_{00},q_0,q_1\) and the complete **R/G/E** potential-policy receipts are needed; future menu additions invalidate this narrow quotient.

If the T action is assigned with positive known preaction propensity \(e(H)\), future Y recording has strictly positive known \(\rho(H,J,H',T)\) and is conditionally independent of the unobserved Y given logged pre-recording history, and the *entire connected cluster* satisfies sequential exchangeability/consistency under its assigned intervention, then the usual appropriately timed inverse-propensity-weighted complete-case moments identify the intervention-specific indicators (for adaptive policies, use the legal sequential product and all required history overlap). Here H' denotes the second job, not the preaction history. This is a strong, testable-by-design selection protocol plus untestable conditional exchangeability, not a result from recording a nominal propensity. When S depends on Y beyond that history, \(\rho\) computed only from observed cells is insufficient and the interval above must remain; a randomized audit or explicit selection-sensitivity assumption is necessary. No data-use right or assignment support can be manufactured by statistical weighting.

Data-generation interventions still alter qualification, demand, recovery queues and learner broadcasts; measurement of Y does not convert a **causal** P/G/E comparison into an observational one. Keep typed field, failures, teleoperation, simulation, synthetic and public/pretrained provenance separate. Physical cluster interference, accepted original customer service, independent E resources, compute/curation costs, and contractual rights are dimensions of \(\omega\), not removable accounting footnotes.

**Replication:** [exact Fraction source and recorded result](selected_history_bounds.py) / [results](selected_history_bounds_results.json), independent [integer-tick Node audit](selected_history_independent.js), [prospective evidence and feasibility](SELECTED_HISTORY_IDENTIFICATION_EVIDENCE.md), and separate [exercises](SELECTED_HISTORY_EXERCISES.md)/[solutions](SELECTED_HISTORY_SOLUTIONS.md). The executed rational-grid checks are verification of the stated *synthetic algebra*, **not** proof of physical robotics or novelty. Closest prior foundations: Horowitz–Manski, [randomized experiments with missing outcomes (2000)](https://doi.org/10.1080/01621459.2000.10473902); Robins–Rotnitzky–Zhao, [missing-at-random IPW (1994)](https://doi.org/10.1080/01621459.1994.10476818); Farboodi–Koh–Xia, [*Data-Driven Automation* (2026), especially §5 and Appendix B](https://arxiv.org/abs/2606.10127); and the previously cited robust MDP/causal-interference literature. The candidate contribution is a robotics-specific **integration** of decision-relevant censoring, joint learning, paid original customer demand and a physically conserved queue, not a newly invented missing-data or data-option theory.

**Open scientific obligations, unchanged deadlines:** No signed P/G/D/E connected-cluster interventions, actual original buyer/no-offer and cleared payment panel, validated outcome-dependent selection process, causal learner-to-customer-demand transition, signed cross-site rights, genuine separate E worker resource, or official quantitative BEA/BLS interindustry coefficients. November 22 Models A/B gate remains **OPEN**; the next proof question is longitudinal policy-dependent censoring and action overlap for simultaneously changing learner, buyer and incident histories, not another arbitrary parity parameter sweep. Theory majority through December 6; November 29/December 6/13/18/23/24 milestones and December 25, 2026, 23:59 America/New_York final target preserved.