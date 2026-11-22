# Lawful signal timing and the recursive data option: choosing before the learner-network regime is known

**22 November 2026. Same integrated argument, When Capabilities Become Production.** A conditional mathematical extension to the shared-network uncertainty chapter, not an independent claim of empirical discovery. November 22 Models A/B scientific acceptance remains **OPEN**. The units below are entirely hypothetical, complete normalized net accepted-and-cleared original-buyer production, not measured robotics economics, dollar conversion from benchmarks, or a sector forecast.

## The question left by the common-network envelope

The preceding [coupled-network argument](COUPLED_NETWORK_ECONOMIC_ENVELOPE.md) correctly joined the learner checkpoint, original buyer demand, worker recovery, and embodiment response through one exogenous whole-cluster regime Z and its common prevalence theta. Yet its pointwise optimized P-minus-E advantage assumed each program selected the correct policy *knowing* theta. That is not an executable investment rule. We now endogenize the decision to learn an **authorized predecision signal** of a realized connected-network regime, and its timing relative to an irreversible new embodiment or data-program selection. This is a direct continuation of the source-data, target-grounding and new-embodiment investment problem: a report can change how pre-existing source capability is deployed without adding any technical skill, and its value can vanish once the irreversible physical capital choice has passed.

The central distinction is **knowledge of a factor prevalence theta versus observation of a realized network factor Z**. A report Y about the current cluster's Z is not an oracle giving theta. If theta is learned across repeated clusters, the producer also has a belief or partial-identification set about theta, updated through legally observed history. A history-derived posterior belongs in the policy state; it cannot be smuggled into the precommitment choice.

## 1. Complete production environment and lawful information

Program a belongs to {R,P,D,SG,E,other feasible composites}: retained qualified controller; productive original-customer field-data acquisition; deliberate target intervention including teleoperation; source learning plus target grounding/alignment; new physical embodiment/capacity; and feasible combinations subject to cash, machine, manufacture, site access, and recovery budgets. Field trajectories (including failures/recoveries), teleop, simulation, synthetic, and public/pretrained sources remain **distinct state-transition channels** with different provenance and data-use permissions. Source data are not an automatic monotone increase in qualification or paid receipts. An optional source or report can always be ignored only when the old controller and the old policy truly remain lawful, physically feasible, and supported.

Fix a finite legal policy menu Pi_a of complete adaptive within-program rules and an exogenous factor Z in {0,1} drawn once per whole connected interference cluster. The conditional whole-program net value v_(a,pi,z) includes paid accepted safe service, refund, outside-option displacement, missed original buyer offers, recovery and operator opportunity, data/compute/rights costs, and any purchase/manufacture/curation expenses **once**. Learning-generated qualified future services, cross-site transfer and customer demand feedback are already inside v; never add an external future-data premium on top.

A signal Y available **before** a contemplated program commitment must be documented as timely, contractually usable, and physically attainable. Suppose it has program-invariant exogenous conditional likelihood L(y|z) and acquisition cost c, with no other effects on offers, service, learner, licensing, or recovery. These are strong assumptions. They permit the ordinary observation-only information calculation below; if obtaining the signal changes the network transition law, it must instead be an explicit active experiment with its own paid-service and learned-state kernel.

For a stipulated Bayesian predictive factor probability p=Pr(Z=1), write w(z,y)=Pr(Z=z)L(y|z). With a report purchased before the irreversible program choice,

    W_early(p,L) = sum_y max_(a,pi in Pi_a) sum_z w(z,y) v_(a,pi,z).

If the program and its fixed capex are committed before the signal, but a lawful controller can be chosen within that program upon receipt,

    W_late(p,L) = max_a sum_y max_(pi in Pi_a) sum_z w(z,y) v_(a,pi,z).

With no such signal,

    W_none(p) = max_(a,pi) sum_z Pr(Z=z) v_(a,pi,z).

The net signal-option values are W_early-W_none-c and W_late-W_none-c, provided the same fixed c is paid once. If one may reject the acquisition option, the realized optimized net gain is the **positive part**, not the possibly negative forced-purchase value. Data source rights and safe deployment can shrink the feasible Pi_a and observation sigma-field; illegal or unavailable labels cannot be given invented likelihoods.

### Proposition 1: report timing, optimal-action overlap, and exact cost threshold

For finite legal programs, conditional responses and exogenous report kernel as specified,

    W_early >= W_late >= W_none.

The first difference, W_early-W_late, is exactly the economic option destroyed by choosing the program before seeing Y. It is zero if and only if (with positive-probability report atoms and attained maxima) at least one common program a is conditionally optimal for **every** such report atom, allowing within-program policy pi to vary with y. The first and second inequalities are weak: even a highly informative report can have zero economic value when it cannot change any lawful optimized service decision. A gross signal gain G has a positive **costly** acquisition value precisely if c<G, with equality giving indifference.

**Proof.** Let B_a(y)=max_(pi in Pi_a)sum_z w(z,y)v_(a,pi,z). Then W_early=sum_y max_a B_a(y) and W_late=max_a sum_y B_a(y). The maximum and finite sum yield their stated order. If equality holds, an a maximizing the latter sum must attain the per-atom maxima for every y of positive mass, since the nonnegative summand gaps total zero; the converse follows directly. A policy that ignores Y recovers an identical fixed pi under the same program, proving W_late>=W_none. Subtract the identical c once to obtain the cost statement. QED.

This is an application of standard expected-value-of-information and Blackwell-comparison principles, not a universal new economics theorem. The *production-specific* obligation is to ground v in original-buyer accepted-and-paid qualified outputs, one connected network and lawful contingent policies, not in a model task-score delta.

### Proposition 2: uncertain factor prevalence is a different implementability problem

Suppose theta itself is not identified, but lies in a justified set Theta. One legally implementable report-contingent policy f maps each observed y to an allowed program and its legal continuation. The **precommitment maximin** problem is

    sup_(lawful f, possibly randomized) inf_(theta in Theta) E_theta[v_(f(Y),Z)] - c * 1{report purchased}.

Do not replace this with inf_theta W_early(theta): that expression lets the optimizer select a different rule *after nature reveals theta* and is generally optimistic. Nor may nature choose theta separately at each site or after each history when the model posits a single common cluster factor. A Bayesian expected return instead specifies a prior on theta or predictive p; its answer need not coincide with maximin. When signal acquisition changes the future learner/operator/customer transition, the lawful full-history Bellman objective—not the exogenous L information formula—must be optimized.

**Proof and limitation.** For any fixed report rule f and fixed conditional factor tables, E_theta[v_f] is affine in theta. Therefore, when Theta is a closed interval, the worst theta for that fixed f occurs at an endpoint. Taking sup_f is a finite zero-sum decision problem (linear programming after allowing randomized policies). In general sup_f inf_theta does not commute with inf_theta sup_f, and information that is valuable under an interior Bayesian forecast may be worthless to the worst-case guarantee. If experiment assignment changes the distribution of Z, any common-theta pairing must be rejustified; if it changes conditional v through physical training, Proposition 1 does not apply as a free exogenous report. QED.

## 2. Exact paid-production counterexample: one signal, two commitment times

We reuse the prior connected-network numerical construction but change E's independent-capacity row to the previously documented alternative, so **a single common Z remains shared across programs**. These are complete hypothetical net contribution rows after each program's one-time costs, with no extra data premium:

| Legal full-program option | Z=0 | Z=1 |
|---|---:|---:|
| P: retained R, decline pilot | 2 | 4 |
| P: original-buyer productive pilot, later new qualified customer service | 3/2 | 5 |
| E: retained R after embodiment investment | 19/10 | 39/10 |
| E: deploy genuinely independent embodied service capacity | 11/5 | 9/2 |

A lawful preassignment signal Y in {0,1} matches the common realized Z with accuracy q in [1/2,1], the same conditional likelihood in either potential program. The predictive probability p=1/2 is stipulated, **not learned or physically measured**. Without a signal, E capacity yields 67/20=3.35 and beats P's best 13/4=3.25.

At q=3/4, the two equally frequent reports give posterior Pr(Z=1|Y=0)=1/4 and Pr(Z=1|Y=1)=3/4. If Y=0 *before* purchase, E capacity contributes 111/40=2.775; if Y=1, P's productive source pilot contributes 33/8=4.125. The implementable ex-ante policy **buy E if low; pursue productive source learning if high** has

    W_early = (1/2)(111/40 + 33/8) = 69/20 = 3.45.

If capital investment is **locked before** Y arrives, a P commitment can adapt its controller and realize 53/16=3.3125; an E commitment yields 67/20=3.35 and is better. Thus

    W_none = W_late = 67/20,     W_early-W_late = 1/10.

An early, licensed, non-disruptive signal strictly helps iff its full single acquisition cost c < 1/10 normalized production units. It does not help merely by furnishing a better task benchmark. If the same report arrives after E manufacturing commitment, this q=3/4 signal cannot undo the prior capacity decision, so its **program-choice value is zero**. Retained R stays available under P. No controller is forced to ingest training data.

The result is not an arbitrary grid switch. The row geometry gives the **exact accuracy frontiers for every q in [1/2,1]**:

    W_early(q) = max{67/20, 3+(3/5)q},
    W_late(q)  = max{67/20, 11/4+(3/4)q}.

The first source-versus-capacity switch requires q>7/12; with investment already locked, a within-P controller choice can exceed the E commitment only for q>4/5. At q=1, W_early=18/5 while W_late=7/2. The conditional differences are not generic robotics thresholds: they depend on the fully paid original-customer response rows and reported factor likelihood.

**An informative zero-value counterresult.** Hold q=3/4, but suppose the operator knows only that common theta is in [1/4,3/4], and must maximize the **absolute worst-case** whole-program return. At theta=1/4, even the high report has posterior Z=1 of 1/2, too low for a P pilot to beat E capacity. Therefore W_early(1/4)=111/40. No admissible report policy can guarantee more across Theta, since nature can choose 1/4; ignoring the report and using E capacity guarantees 111/40 for all theta in this interval (the E conditional value rises with theta). Thus the **sharp maximin free-report gain is zero**, even though under the separate Bayesian p=1/2 objective the same signal has gross value 1/10. A mandatory c>0 experiment strictly lowers the maximin guarantee; a free optional signal cannot.

The contrast is a decision-criterion difference, not a contradiction. To label a report useful, specify (i) what it reveals (realized Z versus unknown theta), (ii) when it is legal to observe, (iii) whether the decision is fixed program, full report-contingent program or adaptive multi-date learning, (iv) whether the criterion is Bayesian, minimax absolute reward, minimax regret, or a risk-limited policy, and (v) whether the signal itself consumes manufacturing/robot/operator/customer opportunities.

## 3. Active source/data acquisition and physical recursion

For a report that is *generated by an action*, replace exogenous L with the joint action-conditional law of the entire next state and report:

    V_t(h) = max_(u in legal A_t(h)) E[ r_t(h,u) + beta V_(t+1)(h,u,Y,D,H_next) | h,u ].

Here u can be a paid original-customer deployment generating successes, failures and recovery traces; deliberate safe teleoperation; a simulator/synthetic/public-pretrained source or curation job; licensed target-specific grounding; a new body/manufacturing or access purchase; a physical queue/worker allocation; or an option to keep R. The learner and embodiment capability, legal retention, new eligible recipes, worker recovery availability, later buyer orders, and competitive/customer response all enter H_next jointly. Information from Y can select future policies, **but productive or deliberate acquisition simultaneously changes qualified recipes and costs**. The simple report value is no longer an additive second term.

Three distinct empirical hypotheses now become testable instead of implicit: (H1) the same source-trained capability earns additional paid service only after a timely licensed target report, with no new qualification change; (H2) target grounding changes joint held-out qualification after identical source data while report quality is fixed; (H3) E changes **simultaneous feasible accepted-and-paid physical capacity**, including shared recovery bottlenecks, rather than merely adding an alternative benchmark controller. Each is separately falsifiable using original buyer offers, safe completed service and cleared payment, plus a matched learner/operator/rights graph. A technical improvement without customer orders or capacity is not itself economic value.

## 4. Identification, falsification and broader value-chain consequences

A real estimate requires a predeclared *connected interference cluster* and signal before assignment; valid predecision reporting rights and latency; independent approved assignment or defensible conditional identification of P, D, SG, E and R; original buyer offer/no-offer/unserved service, qualification, delivery, refund and cleared payment; shared model-checkpoint/teleop/recovery timestamps; embodied hardware/manufacture independence; and source-level modality/provenance/permission logs. Cluster-level spillover invalidates sitewise independent potential outcomes. Positivity must cover the **report-contingent policies** whose paid returns we compare, not only the R controller logged in the past. If conditional returns, L or network factor stability lack support, the thresholds must remain bounds or hypotheses, never empirical policy recommendations.

Direct discriminants: (1) intentionally withhold or lawfully delay the report on matched clusters to distinguish true before-commitment switching from retrospective conditioning; (2) independently vary early report availability and E manufacturing commitment while retaining the same buyer universe and safety rules; (3) compare paid accepted service and unserved buyer offers, not episode success alone; (4) audit whether learner broadcast and rescue queue cross assignment clusters; (5) test whether a supposed Z is indeed preassignment invariant rather than a post-treatment success category; (6) measure acquisition cost inclusive of the next-best scarce production and operator use. No such robotic intervention or customer-cleared panel is available here.

For the wider robotics-economics agenda, information changes the allocation **across layers**: a digital learner checkpoint may unlock physical capacity across customer service nodes, whereas a manufactured embodiment adds independent service throughput only if supervision/recovery and market demand permit it. Actual input-output networks, task-to-end-market demand, manufacturing lead times, rights, financing and ownership affect the feasible v table, rather than being replaced by this two-type example. The prior BLS sector output is legitimate macro context only, not an observed interindustry input-output matrix or robotics addressable market.

## Bounded closest prior art and scientific status

- David Blackwell, [Comparison of Experiments](https://digicoll.lib.berkeley.edu/record/112749) (Berkeley Symposium, 1951) and [Equivalent Comparisons of Experiments](https://doi.org/10.1214/aoms/1177729032) (Annals of Mathematical Statistics 24(2), 1953). Information monotonicity and experiment comparisons are old results.
- Maryam Farboodi, Andrew Koh and Anchi Xia, [Data-Driven Automation](https://www.nber.org/papers/w35320) (NBER Working Paper 35320, June 2026; arXiv:2606.10127), already models future data value, endogenous production-generated data and task spillovers. Its section 5 and Appendix B are conceptual foundations, not claimed novelties.
- This chapter's exact finite-menu commitment inequality and two-type tabulation are **conditional applications of known decision theory**, offered as a candidate production-economics synthesis. An original publishable contribution would need well-supported, cross-site customer-paid and transfer/qualification observations, independent prior-art review, and a mechanism not already encompassed by standard information-acquisition/real-option/robust-control models.

**November22 scientific gate OPEN.** No approved P/D/SG/E original-buyer paid experiments, verified legal signal channels, identified common learner/market/operator factor, independently proven scientific novelty or numerical official BEA/BLS interindustry coefficient. [Evidence protocol](LAWFUL_SIGNAL_TIMING_EVIDENCE.md), [exact executable](lawful_signal_timing_exact.js), [recorded results](lawful_signal_timing_results.json), [Fraction audit](report_timing_fraction_audit.py), [exercises](LAWFUL_SIGNAL_TIMING_EXERCISES.md) and [separate solutions](LAWFUL_SIGNAL_TIMING_SOLUTIONS.md) accompany this integration. The next action is to remove the observation-only exogeneity assumption in a **joint active sensing-plus-production** Bellman comparison, with genuine customer/no-offer, qualified source-to-grounding and shared-worker support, or preserve unidentified signs. Theory remains the majority workstream through December 6; original December 25, 2026 23:59 Eastern target is unchanged.
