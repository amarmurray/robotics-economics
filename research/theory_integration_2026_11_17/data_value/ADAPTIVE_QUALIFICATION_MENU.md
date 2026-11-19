# Economic value of the adaptive source–grounding–embodiment menu

**18 November 2026 Eastern / 19 November UTC.** Continuation of *When Capabilities Become Production* and the [joint-qualification factorial argument](JOINT_QUALIFICATION_FACTORIAL_VALUE.md). This is conditional classical decision/Fréchet mathematics integrated with whole-network qualified customer production, not evidence of field effects or independent scientific novelty.

## Where the previous factorial result stops

Randomizing complete, independently physically approved policy-closed networks can identify each static arm mean J_z and its source-use × grounding interaction I=J_11-J_10-J_01+J_00. That does **not** identify how to acquire source data first, then decide whether to ground the target *after a failed qualification*, or how to select among several separately qualified embodied policies. Three different objects must be kept separate:

1. The mean whole-network customer contribution under each fixed complete policy: static factorial randomization identifies it under policy closure, positivity and no between-network interference.
2. The **cross-policy** joint potential qualification law of several alternatives on the *same customer network*: independent arm randomization does not identify it.
3. The **sequential** qualification/demand/recovery law after training, validation and observed failure: source learning can change grounding response, so this need not equal the static cross-policy law.

Field trajectories, failure/recovery data, productive teleoperation, deliberate grounding, simulation, synthetic and pretrained inputs retain separate costs, permissions and transition laws; none is a universal transfer scalar.

## Whole-production economy, not a score-to-dollar shortcut

Fix a pre-treatment customer opportunity population and demand stratum d, horizon, original B orders, resource/operator/dispatcher exposure, physical approvals and captured whole-network contribution. The feasible policy menu includes retaining qualified F or competent S. Let its *complete* contribution be s. A particular source-trained policy x earns a>s when independently fully qualified; a target-grounding policy g earns b>s when independently fully qualified; otherwise choose approved fallback s. All s,a,b include optimized customer demand, B displacement, accepted A service, recovery and scarce-resource response. We do **not** add any continuation data premium beyond the value already accounted in this complete horizon. Testing, rights, training and validation costs c_x,c_g are charged once. These special-case constants require stable demand, independently approved service, and a noninterfering qualification inspection before customer rollout; they are **not known for actual robots**.

Let binary potential whole-recipe qualification indicators Q_x,Q_g have marginal probabilities p,q and cross-policy overlap t=P(Q_x=1,Q_g=1). Nonnegative cell probabilities imply the sharp Fréchet interval

    max(0,p+q-1) <= t <= min(p,q).

### Exact proposition: option-value bounds

If both independently admissible controllers are qualified/tested upfront, and the buyer may select the better approved one, expected gross value is

    V_both(t) = s + (a-s)p + (b-s)q - (min(a,b)-s)t.

Subtract c_x+c_g for net value. Proof: the four cross-policy masses are P00=1-p-q+t, P10=p-t, P01=q-t, P11=t; their payoffs are s,a,b,max(a,b). Since V_both decreases with t when both alternatives outperform fallback, its exact identified range over unrestricted joint couplings is obtained at the Fréchet endpoints. For a> s, b> s, uncertainty about redundancy can dominate uncertainty about individual technical success. This **menu** substitution is different from complementarity within one jointly trained 11 controller; the source/grounding factorial interaction I does not recover t.

If x is tested first and g is bought only after x fails, with a>=b and *no learning carryover*, the optimal ex ante staged value is

    V_stage(t) = s+(a-s)p-c_x
                 +max(0, (b-s)(q-t)-c_g(1-p)).

The ground-on-failure criterion, for p<1, is

    P(Q_g=1|Q_x=0)=(q-t)/(1-p) > c_g/(b-s).

This is a **demand- and cost-conditioned whole-service** criterion, not a benchmark-pass threshold. If p=1 there is no failed branch. If b>a, testing g even after x succeeds may be optimal, so the displayed one-branch formula is incomplete and that branch must be added. If the source experiment alters subsequent grounding, the correct continuation statistic is r=P(Q_{g after x}=1 | Q_x=0, observed history), not (q-t)/(1-p). The sequential path x→g is a separate policy with its own controller, target support, B-order losses, operator budget, customer clock and right to train; an arm-level factorial does **not** identify r.

### Exact two-world counterexample with identical static arms

Let s=2, a=b=4, p=q=1/2 and c_x=c_g=1/5 in hypothetical normalized **complete customer contribution**, not dollars or robot scores. Any static four-arm experiment can have the same means in the following worlds (including independently fixed J_11); only cross-arm potential qualification dependence changes:

| Cross-arm coupling | t | Source test alone | Both tests upfront | Source, then grounding only after failure |
|---|---:|---:|---:|---:|
| Disjoint successes | 0 | 14/5 | 18/5 | 37/10 |
| Independent successes | 1/4 | 14/5 | 31/10 | 16/5 |
| Identical successes | 1/2 | 14/5 | 13/5 | 14/5 |

With disjoint qualifications, second-stage grounding is valuable; with identical qualifications it is not purchased. The ex ante *optimal acquisition strategy* reverses although static marginals, each arm's outcome and factorial interaction are unchanged. This is a counterexample to identifying staged acquisition value from factorial source-grounding effect alone.

### New embodiment expands the unknown joint object

For three mutually exclusive but independently approved qualification alternatives (source-trained x, target-grounded g, redesigned embodiment h) with each success marginal 1/2 and every pairwise co-success 1/4, let outcomes be equiprobable:

    Even-parity: 000,011,101,110
    Odd-parity:  001,010,100,111

Their single and pairwise laws are identical. But the probability **at least one** approved version qualifies is 3/4 versus 1. With fallback 2, qualified-version whole-network contribution 4, three test costs 1/5 each, the upfront three-option values are 29/10 versus 17/5. Thus *even all pairwise* potential qualification statistics can fail to identify the value of a menu of source, grounding and embodiment investments. It is not an observed industrial correlation or a claim about a simultaneous triple-skill service.

## Restore dynamic customer production

In the full model, the object is a history-dependent policy value J(pi,theta) with joint qualification, endogenous state visitation, possible learning-created embodiments, customer demand and original order displacement. The Bellman decision after first-stage observation O_x is: retain qualified fallback, operate x if approved/qualified, or, if still permissible and beneficial, pay for a newly qualified **sequential** grounding or embodiment path, then optimize whole accepted customer production over the remaining clock. Histories that lack physical approval or operator capacity **exclude** that action; they are not assigned imaginary deployment earnings. Read-only production-data copying can leave B controller/actuation retained if its *entire network* really is causally isolated; optional old policies remain.

Demand d determines s_d,a_d,b_d and the value width from unidentified overlap:

    (min(a_d,b_d)-s_d) *
      [min(p_d,q_d)-max(0,p_d+q_d-1)].

This width can be zero with saturated demand or economically equivalent service, even if technical coupling is widely unidentified. Per-network values cannot simply be summed across customer/operator networks without verified isolation and shared-resource accounting. A resource-price LP certificate is only exact under its documented convexity/divisibility; integer service bundles or common controllers can cause gaps. Rights and manufacturing lead-time restrict available policy paths, not create an independent premium.

## What an empirical study must actually measure

Static approved whole-network factorial randomization identifies fixed arm means. A separate, verified **paired** technical qualification comparison may reveal cross-arm Q_x,Q_g (and Q_h), but only if controller instances are separately trained, comparisons remain valid within the same pre-treatment customer strata and there is no interference. That does not by itself identify accepted commercial service or establish deployment approval. A prospective *sequentially* approved randomized second-stage acquisition among x-failure histories can estimate r and corresponding complete whole-service value, conditional on history support/consistency, no cross-unit interference and measured original orders. If none is possible, retain sharp response-set bounds, the qualified old/specialist comparator and explicit impossibility of inference. Do not infer dynamic learning from static qualification correlations.

**Falsifiers:** source training alters g's conditional recovery law; paired target qualification fails to transport to physical service; test time expires target demand; original B orders or operator availability change; a specialist dominates; a free routine production-data byproduct renders paid acquisition redundant; h manufacturing or rights make it unavailable. No actual target fleet architecture, approved intervention, matched field panel, BLS–BEA numeric crosswalk or originality audit was obtained.

**Closest prior art (checked 19 November UTC):** S. Murphy, *Optimal Dynamic Treatment Regimes*, JRSS B (2003), https://doi.org/10.1111/1467-9868.00389 (history-conditioned sequential treatment). *Partial identification of the distribution of treatment effects with an application to KIPP*, *Quantitative Economics* (2020), https://doi.org/10.3982/QE1273 (unobserved joint potential outcomes and Fréchet bounds). DDA, Farboodi/Koh/Xia, https://arxiv.org/abs/2606.10127, §5 and Appendix B, already study production-generated data value and aggregation complementarity. These established tools are combined as a **candidate robotics-economic synthesis**, not asserted scientific novelty.
