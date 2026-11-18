# When Capabilities Become Production
## Endogenous interventions: what a deployment reveals, repairs, and earns

**November 17, 2026, Eastern / November 18 UTC. Private theory continuation.** This chapter follows the transfer/grounding and productive-teleoperation results without launching a new isolated paper. All propositions below are conditional mathematical constructions, not empirically estimated robot-control laws or claims of scientific novelty.

### 1. The question left open by the two-batch model

The preceding chapter allowed a target episode to produce a signal about transfer and to improve future qualification. Its signal accuracy was supplied as a primitive. In operation, neither the presence nor the content of an intervention is drawn from a fixed, policy-independent data urn. The deployed controller determines which states are visited; an operator or safety gate determines which potential errors become corrections; a retained training procedure determines whether any correction changes certified production capability.

Therefore a commercial deployment can provide accepted service, physical learning and information, but a decline in recorded corrections can mean **less need for help**, **less exposure to difficult states**, or **less chance of detecting a need for help**. Those mechanisms have different technical and economic implications. We derive the joint observation and learning law and evaluate an explicit safe production-versus-targeted-probe menu with a competent target-only alternative.

### 2. Common production account and the endogenous observation law

Keep the parent state s=(D,Pi,Q,K,omega,R,B): provenance-indexed data, uncertainty about transfer and control, retained qualified recipes, available embodiments and capacities, customer demand, usable rights and cash. The action a selects an operating recipe and intervention policy subject to one shared calendar, robot/operator time, approved safety envelope, customer access and compute/curation resources.

Current provider contribution m(a;s) comes from actual accepted service less operating and human-control costs. The single Bellman term E[J(s')|s,a] captures the later customer-production consequences of changed information, control, training and embodiment options. No per-correction data bonus is added on top.

In a minimal two-regime experiment, H is either high (H) or low (L), with prior pi. The regime jointly affects prospective reuse profitability and would-be control-error propensity on a target-relevant state. Let X=1 mean the policy visits that state during the observation slot. Initially assume Pr(X=1|H,a)=Pr(X=1|L,a)=e_a, independent of H. On an exposed opportunity, E=1 is a would-be control error with probability p_H or p_L. A monitored gate detects and corrects that error with probability g_a, with no false positives, independent conditional on E,X,H. Define C=1 for a recorded correction. Then

  Pr(C=1|H=h,a) = e_a g_a p_h.                                     (I1)

The joint likelihood when visited state X is recorded is

  Pr(X=0,C=0|h,a)=1-e_a;
  Pr(X=1,C=1|h,a)=e_a g_a p_h;
  Pr(X=1,C=0|h,a)=e_a(1-g_a p_h).                                  (I2)

C=1 is impossible when X=0 in this simplified gate. These are *would-be errors*, not permission to cause uncorrected failures: e and g must be feasible under an actual supervised and safe approved operating protocol. More realistic systems can have false positives, uncertain recognition, repeated states and intervention-induced subsequent state changes; (I1)-(I2) are deliberately local.

For correction-only logging, let q_a=e_a g_a, r_h=q_a p_h, and r=pi*r_H+(1-pi)*r_L. Bayes' rule yields

  Pr(H|C=1,a) = pi*r_H/r,
  Pr(H|C=0,a) = pi*(1-r_H)/(1-r),                                  (I3)

with zero-probability events omitted. The first posterior is invariant to q_a when q_a>0 *because* exposure and gating were assumed independent of H. The second is not. When no relevant state was visited and that fact is logged, the posterior stays at pi. A bare "no correction" observation conflates no exposure with an exposed state requiring no recorded correction; it is not equivalent to a successful, tested target recovery. If e_a=0, no correction carries zero regime information.

If states visited depend on the regime, replace e_a by e_a(h) everywhere in the joint likelihood. Then even X=0 may be informative, and the positive-correction posterior generally depends on the selection policy. If the controller and gate have unobserved state-dependent decisions, the unselected/corrected sample is not representative of target production opportunities. This is a mechanism to *estimate or bound*, not a convenient missing-at-random assumption.

The retained control transition is a separate object:

  Pr(Q'=q' | Q,H,X,C,a,train,rights).                              (I4)

A recorded, owned correction can update a controller but need not produce a qualified service recipe. A no-correction trajectory can provide proprioceptive/reward information; a failed, unassisted attempt can teach without human labels; simulation and synthetic recovery data can have different observation operators and safety meanings. Equation (I1) models one *correction stream*, not all learning or data.

### 3. An informativeness result and its economic limitation

**Proposition I1 (gated observation ordering).** Suppose p_H,p_L and the prior are fixed, q=e*g is state-independent, and the only report is binary C. If 0<=q_0<=q_1<=1, the higher-q experiment Blackwell-dominates the lower-q experiment. When X is separately logged, (X,C) Blackwell-dominates C alone for a fixed action.

**Proof.** Given C from the high-q experiment, independently retain each positive report with probability q_0/q_1, converting it otherwise to C=0; keep existing zero reports. For each h the resulting positive probability is q_1 p_h*(q_0/q_1)=q_0 p_h, so it is precisely the lower-q experiment. For q_1=0 both experiments are degenerate. Deleting X from (X,C) produces C. These are signal-garbling constructions, and optimal information-dependent decisions cannot gain from a garbling when it is costless to ignore information. QED.

This is **not** a claim that maximizing interventions is socially, safely or commercially optimal. Increasing exposure can displace accepted customer work, incur monitoring fees, create physical risk or shift the state distribution. In particular I1 compares information **holding the physical learning technology fixed**; different counts of actual corrections can also alter Q' in (I4). The policy optimizer must compare both channels, costs and qualified service.

Under the maintained likelihood, E[C|a]=e_a*g_a*(pi*p_H+(1-pi)*p_L). A uniformly more competent policy with p'_h=lambda*p_h, 0<=lambda<1, and unchanged e,g reduces corrections by lambda and yields a less informative correction-only report in the Blackwell ordering. That does not establish a lower *optimized economic value*: the improved controller may already qualify without help, and a feasible optional old probing policy can still be used when its information is valuable. If e or g changes, or if a new controller visits previously inaccessible states, the correction count need not even decrease. "Higher autonomy depletes the data supply" is thus a conditional observed-sample claim, not an unconditional capital-value theorem.

### 4. A closed-form customer-conditioned intervention threshold

We now connect the likelihood to the parent's optimized production-value table, rather than assigning a price to a corrective trajectory. There are two dates, one current operating slot and one terminal qualified-service opportunity. Same rights, available operator, action-eligible learning transition, and competent alternative apply to each option. There is no discounting between these two normalized dates. The action a determines current net contribution m_a and exposure e_a; g=1. Its correction is reported before the terminal choice. A usable corrected demonstration adds d>=0 to the source-reuse route's optimized terminal customer contribution; this is a synthetic reduced form for an attained qualification, not a general assumption that correction always works. The terminal source route returns 9 in regime H and 1 in regime L, plus d if C=1. A target-only specialist/embodiment route returns T regardless of regime. Prior pi=1/2, p_H=3/4, p_L=1/4. All are normalized **customer-production** contributions from eligible complete-service recipes, not benchmark accuracies converted into currency.

For any e>0, Pr(C=1)=e/2, Pr(H|C=1)=3/4, and the conditional source payoff after C=1 is 7+d. After no correction, Pr(H|C=0)=(1-3e/4)/(2-e)<=1/2, hence the conditional source payoff is at most 5. For the commercially meaningful comparison T in [5,7+d], the optimal terminal choice is source after a correction and target-only otherwise. Therefore

  V_T(e)=T + (e/2)*(7+d-T).                                        (I5)

For e=0 the same value holds with tie-breaking in favor of the target recipe. The higher-exposure action P beats routine R exactly when

  m_R-m_P < ((e_P-e_R)/2)*(7+d-T),                                 (I6)

assuming e_P>e_R and the declared route-payoff range. On equality both tie. This is a threshold about **operating opportunity cost versus the change in optimized future production**, rather than an intrinsic value per demonstration. The marginal current cost and later customer opportunity jointly determine the data choice. If the future target-only route becomes stronger (higher T), the economically rational case for a costly probe narrows even though the technical signal distribution remains unchanged. If source rights, model update efficacy or hardware change, recompute the qualified routes and likelihood rather than reusing (I6).

**Constructive exact menu.** Routine R: m=6, e=1/4. Deliberate supervised target probe P: m=5, e=1. A competent specialist current activity S: m=6.3, e=0. Future T=5 and d=1. Each alternative can retain existing qualified routes, and the full opportunity cost is in m. Exact values are

| Current action | Correction probability | Optimized terminal contribution | Total contribution |
| --- | ---: | ---: | ---: |
| Routine R | 1/8 | 43/8 = 5.375 | 91/8 = 11.375 |
| Safe probe P | 1/2 | 13/2 = 6.5 | 23/2 = 11.5 |
| Specialist S | 0 | 5 | 113/10 = 11.3 |

The safe probe is optimal by 1/8 over routine, **despite earning less current contribution than both alternatives**. The current-profit-only comparator correctly chooses S (6.3) but earns total 11.3; the forward-looking choice is not implemented by calling current losses automatically good.

**The report and the physical update are distinct causal channels.** If the exact same physical corrections are retained but the report is not revealed before terminal route commitment, terminal source use is selected ex ante and returns 5+e*d/2. Delayed-report totals are 89/8=11.125 for R and 21/2=10.5 for P: routine wins. If the report is early but corrections produce no persistent qualified improvement (d=0), totals are 45/4=11.25 for R and 11 for P: routine also wins. These two ablations show that the chosen probe in this example needs both the information and control-update channel; neither ablation changes e or uses a fictitious fee for possessing data.

**Strong alternative counterexample.** If the target-only/modified-embodiment terminal route is T=25/4=6.25 under identical observation and source policies, totals become 399/32=12.46875 for R and 97/8=12.125 for P. Routine wins. This is a real alternative production capability, not an intentionally weak baseline.

**Free production by-product counterexample.** If commercially routine R generates the same relevant observations and persistent learning as P (e_R=1, g=1) *without sacrificing its current net contribution or violating safety*, its total is 25/2=12.5, exceeding P. Deliberate acquisition then has no incremental informational or physical benefit. If matching data can only be obtained with extra labor or capacity, it is not a free by-product and must not be assumed to erase the difference.

The example is a proof of possibility and an exactly enumerated two-stage decision, not an estimated market price or a finding that more human corrections systematically improve robots. Its regime-payoff correlation is an assumption: high future source-reuse usefulness coincides here with high propensity to request correction. Reverse the correlation, change gate behavior, or change the customer demand state and the acquisition ranking may reverse. That is the point of identifying the joint law.

### 5. Correction rates do not identify latent need or commercial learning value

The observed aggregate correction rate is e*g*\bar p. Without exposure logs and an independently evaluated gate, this product does not identify the underlying error propensity. For example, e=1/4,g=1 and e=1,g=1/4, with the same p_H=3/4,p_L=1/4, induce exactly the same correction probability under *each* regime. The first policy rarely visits the relevant state; the second visits often but rarely detects/corrects the would-be error.

Even when visits are fully logged, gate accuracy and error need remain confounded. Consider e=1 with (g,p_H,p_L)=(1/4,3/4,1/4) or (1/2,3/8,1/8). Both yield Pr(C=1|H)=3/16, Pr(C=1|L)=1/16, hence identical (X,C) distributions. But the expected rate of **unintervened would-be errors**, e*(1-g)*\bar p, is respectively 3/8 or 1/8. An observed drop in interventions alone is not a safety improvement estimate, nor a causal estimate of the persistent effect of collected corrections.

With known e>0 and known gate bounds g in [g_min,1], an observed correction fraction r implies, in this simplified no-false-positive population, r/e <= \bar p <= min(1,r/(e*g_min)), provided the bounds are jointly feasible. If g_min=0, the useful upper bound collapses to 1. Estimating training gains additionally needs a policy-level randomized inclusion or matched independent target evaluation; the accounting value additionally needs accepted service, all-attempt cost, demand, competent fallback and qualification history. Inverse propensity reweighting cannot recover a target state that no policy in the permitted design visits (positivity failure).

### 6. Integrated controller and learning program

The exact general continuation remains

  J_t(s)=max_{a feasible}{m_t(a;s)+beta*E[J_{t+1}(s')|s,a]}.          (I7)

The transition includes both Pr(Z|H,a) induced by visitation and gating and Pr(Q'|Z,a,train) induced by retained training, validation and hardware compatibility. A data-rights restriction may make a useful correction unavailable for training while leaving today's service feasible. Different modalities—unsupervised field trajectories, failures and recoveries, teleoperation, simulated rollouts, synthetic data and public pretrained representations—enter through distinct observations and qualification transitions; no modality defines every other modality's value.

A higher-quality new policy, body or source may dominate an old one in safety and contribution, but optional feasible old data and retained safe policies preserve weak monotonicity of the *optimized* attainable value under unchanged costs, rights, constraints and demand. Forced retraining or retirement of a safe policy is not optional expansion. The standalone source/grounding precision model remains useful for a conditional target, while (I1)-(I4) show why its source precision increment must itself be learned from selected state-action observations.

The production network can invalidate a one-route threshold. When multiple complementary qualifications are needed for a single accepted order, replace each fixed 9, 1 and T by the common optimized f(A;omega) and integrate over the **joint** qualification outcomes. If a scarce robot-hour constraint causes the probe to displace an order, that forgone customer contribution belongs in m; if a targeted probe opens a new embodiment and changes actual task access, that enters the future feasible production set. Do not add either consequence twice.

### 7. Empirical discrimination and closest prior work

A controlled technical panel would record state opportunity and exposure X, gating attempt and correctness, corrective content and provenance, unassisted/assisted attempt outcomes, retraining inclusion and held-out qualification, then marry those records to *matched* complete accepted-service recipes and customer demand/payments. A suitable treatment varies safe, preapproved coverage and correction logging; a separate experiment holds acquired physical data constant while changing the timing of a non-safety report before an optional acquisition decision. An independent supervised evaluator can audit missed would-be errors without permitting unsafe unmonitored operation. Cross-target/embodiment transfer should use held-out bodies/sites, qualification bundles and competent target-only and modified-embodiment alternatives. Aggregated interventions per success or benchmark percentage alone do not establish (I4) or an economic value. A fuller pre-registered set of contrasts is in the accompanying empirical protocol.

**Prior-art boundary.** Ross, Gordon and Bagnell (2011), *A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning*, https://proceedings.mlr.press/v15/ross11a.html, already explain policy-induced observation distributions in imitation learning. Hoque et al. (2022), *ThriftyDAgger*, https://proceedings.mlr.press/v164/hoque22a.html, explicitly design intervention gating around novelty/risk and a human budget. Hoque et al. (2024), *IntervenGen*, https://arxiv.org/abs/2405.01472, generate diverse recovery data from fewer collected interventions. Farboodi, Koh and Xia, *Data-Driven Automation*, https://arxiv.org/abs/2606.10127, already assign future value to production-derived data and discuss complementary aggregation. We reconstruct a **customer-qualified production and intervention-selection comparison**, not new DAgger, Blackwell ordering, Bayes' rule or an original learning algorithm. Online source check dated November 17, 2026 Eastern: PMLR abstracts/metadata and IntervenGen arXiv abstract/introduction; not new implementation of those papers or full proof replication.

### 8. Boundary and exact next theoretical question

The current identification result is deliberately strong as a negative result: even a perfectly observed correction count across all visits cannot distinguish a sensitive gate monitoring a less erroneous policy from a weak gate monitoring a more erroneous one without additional audit instrumentation. The current positive result is conditional: informative deliberate exposure can beat current profitable service *if* the intervention creates persistent qualified improvement and changes a future production choice, after opportunity cost and competent alternatives.

Next extend (I1)-(I4) to **two sequential deployments whose first correction changes second-period visitation, gate selection and training suitability**. An adaptive controller can choose to route around difficult states, selectively solicit help or redesign an end effector; those choices change both the *support* of the training sample and the source-to-grounding identification problem. The proof gap is an ordering or sharp counterexample when the action that produces today's accepted service itself endogenizes tomorrow's observation support, and when missed errors are partially observed. Use a shared safety/production budget, a retained safe policy and qualified-order performance, not a new arbitrary value-of-data coefficient. The Nov 22 synthesis, Nov 29 evidence backbone, Dec 6 contribution choice and Dec 25 final edition remain open.

### Reproducibility and limits

The accompanying standard-library JavaScript model implements (I1)-(I6), correction-only and exposure-logged posteriors, early/delayed route choice, and countermodels. The generated JSON contains all synthetic totals. The same exact source was executed with 46 scoped assertions in the connected JavaScript runtime; rational cases were separately checked with Python fractions. This is numerical checking plus written mathematical proofs, not independent peer review, full repository CI, calibrated robot training or accepted customer experimentation. 