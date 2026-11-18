# When Capabilities Become Production
## Multi-step safe coverage: when can production-generated data replace grounding or embodiment redesign?

**Private working continuation | 18 November 2026 UTC.** An extension of the same integrated qualified-production model, not a new paper, observed effect, or claim of theorem novelty. Synthetic contributions are normalized production units, not dollar-per-correction estimates.

### 1. The exact comparison

The earlier sequential-support chapter derived a two-episode selected qualification event. It did not establish whether repeated *ordinary accepted production* eventually reaches the same states and joint customer qualifications as supervised target grounding or an altered embodiment. The question is not whether a robot can collect more trajectories; it is whether its **safe, chosen policy** can visit and validate the states needed for an economically valuable *complete service* before the relevant customer window closes.

Fix a horizon T, discount beta, demand state omega and existing qualified configurations Q_0, including a competent incumbent A. The finite controlled state is x_t=(q_t,e_t,Q_t,b_t,s_t,z_t), with retained controller lineage q, embodiment e, **jointly** held-out accepted recipe set Q, remaining cash/operator and calendar resources b, safety eligibility s, and permissible training/rights history z. With unknown transfer regime H, include the posterior pi_t(H) and its observation history (finite histories suffice for the statements below). A safely approved action a has current **net accepted production** m_t(x,a;omega), a resource vector k_t, and a kernel P_t(dx',dy|x,a,H) for next control, visited-state exposure, intervention, usable correction and held-out qualification. The transition explicitly records observing nothing because a state was **not visited**. Actions include R (routine production and its optional byproducts), G (target-specific supervised grounding), E (new/modified embodiment and its validation), S (competent specialist) and retaining prior policies. These labels are not assumed to have ordered quality, safety, information, or cost.

The same customer-production function f(Q_T;omega_T) used in the parent theory is optimized **once** at terminal time over feasible accepted-service recipes, customer demand, site permissions, body capacity, human attention and coordination. An adapted controller is not automatically a qualified recipe. All acquired-data rights, compute, curation, embodied validation, cash and lost accepted service belong in m, k, P and terminal constraints. No additional data premium is added to f.

The value of a policy family F is

    V_F(x0) = sup_{pi in F, safely feasible} E_pi[
              sum_{t=0}^{T-1} beta^t m_t(x_t,a_t;omega_t)
              + beta^T f(Q_T;omega_T)].                                 (M1)

The routine family F_R may adapt its *routine* exposure after observing its own reports and may retain earlier controllers. The unrestricted family F_all additionally permits G, E and S within the **same budgets**. If S is a permitted outside option, it must also be available to the routine benchmark: never compare a fully optimized research route against a deliberately incompetent incumbent. Trivially F_R is a subset of F_all when all options are optional, so V_all >= V_R; this trivial inequality says nothing about whether the costly extra actions are worth taking.

### 2. Positive safe reachability is not equal economic production

Define the policy-union T-step safe support of a qualification bundle B by

    Reach_F(B,T,x0) = 1 iff there exists pi in F with
                         Pr_pi(B subset Q_T | x0) > 0.                    (M2)

Here B denotes an entire customer-accepted bundle (potentially robot, grasp, recovery, human coverage, tool, warranty and access), not a benchmark skill. In a finite, fully observed state space, construct a time-expanded graph of **safely feasible** action/observation transitions with positive probability, augmenting nodes with remaining budgets and jointly retained Q. Do not include a marginally safe action that violates an almost-sure safety or operator-budget constraint on some possible continuation.

**Proposition M1 (reachability certificate).** Reach_F(B,T,x0)=1 if and only if this resource-augmented graph contains a positive-probability, safely feasible path of at most T decisions from x0 to a node with B subset Q. Proof: a positive-probability policy terminal event is a finite union of trajectory cylinders, so at least one path has positive probability. Conversely choose the prescribed actions on a positive path and safely feasible fallback actions at all other histories; their joint cylinder probability is the product of positive conditional factors. If no safe fallback exists, the path is not in the graph. This is standard finite-horizon Markov reachability, not a novel graph theorem.

For an unknown fixed H, a positive mixture probability need only hold for *one* prior-supported H. Robust feasibility in every H is different and must be stated separately. Positive support may have arbitrarily tiny probability and is **not** a customer reliability certification. A B node reached after a customer deadline is economically irrelevant to that window. A body that changes safe contacts/tool access can add an edge absent under every existing controller; additional training examples on the old body need not do so.

**Proposition M2 (sufficient routine-production dominance).** Fix *any* permitted G/E/S contingent policy D. Suppose there exists a safe routine policy R satisfying the same or tighter resource limits and a coupling of their **total net accepted-service flows** M_R,M_D and terminal Q_R,Q_D such that M_R >= M_D and Q_R contains Q_D almost surely, with the same terminal omega. Then for every nondecreasing optimized production function f, E[M_R+beta^T f(Q_R)] >= E[M_D+beta^T f(Q_D)]. If this coupling exists for each D in F_all, V_R=V_all. Proof: apply pathwise monotonicity and integrate, then optimize. This strong sufficient condition is *not necessary* for one fixed customer f. It requires no additive transfer coefficients and applies to bundles, but cannot be inferred from equal marginal task pass rates. A more specific F_all can still dominate by better present production without being more informative.

A tempting weaker inference fails: equal reachable support of every Q and equal marginal qualification of each new skill do **not** imply equal production value. In a two-new-recipe example, let the four mutually exclusive held-out outcomes be 00, 10, 01, 11 for B,C. Under R their probabilities are (1/16,7/16,7/16,1/16); under G they are (7/16,1/16,1/16,7/16). Every outcome has *positive support* under both, and each recipe's marginal qualification chance is 1/2 under either. A complete customer workflow requiring **both** has f(11)-f(00)=16 and zero incremental value for singletons, so expected terminal gain is 1 under R and 7 under G. If G displaces 4 units of current net accepted production, its net gain 3 still exceeds routine gain 1; a competent specialist of value 2 is beaten by G but not R. If f is instead additive with 8 for each singleton, both paths yield expected terminal 8, so G's four-unit displacement makes R preferable. The difference is the **joint qualification law and customer complementarity**, not support or marginal ML scores. These full-support distributions are constructive technical kernels, not estimated robotics correlations.

### 3. Endogenous learning changes the very supply of the next data

For a transparent special case, let j=0,...,K be retained **validated progress** stages toward a new target bundle, and an approved action a in stage j either stays at j or advances to j+1. Conditional on H and the currently chosen policy, define

    p_j^a(H) = Pr(relevant safe exposure | H,j,a)
               * Pr(eligible detected correction | exposure,H,j,a)
               * Pr(retained update passes its target validation
                     | exposure,eligible correction,H,j,a).              (M3)

These factors are *sequential conditional probabilities*, not assumed independent. The final factor encompasses licensed use, compute/curation, training and the matched held-out qualification check; a recovery can improve current service without passing it. The product may vanish because the policy avoids the state, the detector misses it, rights forbid reuse, or the proposed transfer does not qualify. Different sources (routine field, failures/recoveries, teleoperation, simulation, synthetic and public/pretrained) have different kernels; none is privileged. After progress, the next p_{j+1} changes endogenously because q, exposure and the safe action set changed.

**Proposition M3 (staged-coverage boundary).** If the only route to K requires K distinct validated advances and exactly K decision slots remain, a fixed safely feasible action sequence has terminal progress probability equal to the product of its conditional stage-success probabilities along the all-success history. The event has positive probability if and only if every required conditional factor is positive. If some necessary p_j^R=0 for *every* safely available routine action at that progress/history, routine-only policy support for K is zero for any horizon within which all alternate routes also remain absent. No positive amount of additional data drawn from those exact zero-exposure routine kernels unlocks that particular state. Grounding or embodiment may change the action graph and create support. Proof: the only possible K-success trajectory advances on every remaining slot; apply chain rule. At a zero cut, induct over further routine steps. This is a finite safe-policy **support** statement, not a claim that any machine-learning method has fundamentally zero generalization.

With T>K, failed advances can be retried, and the relevant probabilities follow a finite dynamic recursion, not a simple product. With p_j(H) regime-dependent, integrating the **within-H path product** over H is required; multiplying mixture-average p_j is generally wrong because the posterior is selected by prior corrections. No global ordering survives arbitrary policy-induced changes to visitation, recovery and training.

A limited constructive ordering does survive: if two policies operate on the *same* upward-only progress chain, face the *same* starting state and slots, and one has p_j^a >= p_j^b for each j at every history (with no loss of other qualification, no change in rights, and matching safety feasibility), shared uniforms give a coupling j_T^a >= j_T^b. This is the standard monotone chain coupling, not a value ordering when a sacrifices current service or burns operator time. The condition must be verified on reached states, not asserted because the new controller has a higher benchmark average.

### 4. Exact adaptive comparison with an incumbent, a specialist and a new body

The following two-slot example tests **policy menus/information structure**, not a parameter tweak to the previous correction experiment. One supervised or physical modification is permitted by a common **operator budget of one** and cash cap two; every route uses the same two calendar slots, retains qualified A, and has approved safe fallbacks. beta=1 and terminal B denotes a **jointly accepted customer-service bundle**; terminal incremental f(B)=Delta>=0. One routine accepted A slot earns 1.

Slot 1 must serve a prerequisite customer operation R; it earns 1, and with probability 1/2 produces a validated retained update j=1. The report is available before slot 2. If no update, j remains zero. In slot 2, the same feasible menu is assessed in the *actual reached state*:
- R earns 1. At j=1, its safe exposure to the next required target state is **zero**, so repeated routine production cannot reach j=2 by the deadline; at j=0 it may only achieve j=1, too late for bundle B. This is an explicit zero-support hypothesis, not a claim about field fleets.
- G, only after the validated j=1 update, uses the one operator unit, displaces A service, incurs 1/4 of net compute/curation cost, and reaches/validates complete B with probability 3/4. Its slot-2 *expected contribution* is (3/4)Delta-1/4.
- E is a safe alternative embodied target-only route available after slot-1 site access even if j=0. It uses one operator unit, displaces A service, costs two cash units and reaches/validates B with probability 3/5. Its expected slot-2 contribution is (3/5)Delta-2.
- S is an actually qualified specialist using the same last physical/organizational slot and at most the common human budget; it contributes 2 of net accepted service. It is available under **both** routine and enlarged menus. It is not an unqualified straw baseline.

This is an exclusive last-slot choice: no route receives B and specialist output simultaneously. G and E terminal gains already include the entire realized learning benefit, so there is no data-premium term. The exact optimal value is

    V_all(Delta) = 1 + (1/2) max{1,2,(3/4)Delta-1/4,(3/5)Delta-2}
                    + (1/2) max{1,2,(3/5)Delta-2}
                 = 1 + (1/2) max{2,(3/4)Delta-1/4}
                     + (1/2) max{2,(3/5)Delta-2}.                     (M4)

E is always dominated by G *after* an informative first retained update because G both costs less and has higher target completion chance; E can still matter *after failure*, where G is not safely accessible. In the success branch G beats the specialist iff Delta>3; in the failure branch E beats the specialist iff Delta>20/3. Consequently:

    0 <= Delta <= 3:      V=3
    3 < Delta <= 20/3:    V=15/8 + (3/8)Delta
    Delta > 20/3:        V=-1/8 + (27/40)Delta.                         (M5)

At Delta=7, V_all=23/5=4.6, selecting G on first success and E on first failure, against 3 for the best *routine-or-specialist* second choice and 16/5=3.2 without G. Without E, the adaptive value is 9/2=4.5. The latter is an additional 1/10 option value from redesign on the failure branch, **not** 0.6 multiplied by a generic data wage. At Delta=12, V_all=319/40=7.975; the same contingent mixture remains optimal. At Delta=0, the specialist earns 3 total including the first A slot, and no learning action is bought. A free relevant byproduct can reverse these comparisons.

**Proof of (M4)-(M5).** Apply the last-slot Bellman maximum after each observed first-update history, with no ability to spend the one operator unit twice; average each branch with probability 1/2, add first A output 1. At j=1, (3/4)Delta-1/4 strictly exceeds (3/5)Delta-2 for Delta>=0, while the specialist dominates routine 1. At j=0, G is infeasible. Solving the two remaining crossings against specialist 2 gives Delta=3 and Delta=20/3. Expand the two piecewise linear terms. QED. Exact fractions make the comparison reproducible; they are illustrative and uncalibrated.

The strong zero-exposure hypothesis is also **directly challengeable**. If routine slot-2 access after the first update instead qualifies B with probability r while preserving its 1 accepted-service unit, the success-branch routine option is 1+r Delta, and it weakly dominates G when

    r >= 3/4 - (5/4)/Delta,     Delta>0.                              (M6)

At r>=3/4, routine dominates G at every nonnegative Delta; the extra acquisition is never optimal in that branch if rights/other feasibility are unchanged. This is the *economically meaningful observational task*: estimate approved second-stage coverage, validation and retained qualification under the **routine controller actually selected**, not infer that access from first-stage correction frequency. A targeted intervention has no unconditional advantage.

### 5. General latent alignment, retention and the missing empirical joint law

For a finite unknown H, the recursion conditions on each observed report y:

    pi_{t+1}(h) = pi_t(h)L_t(y|h,x,a) /
                  sum_g pi_t(g)L_t(y|g,x,a),                          (M7)
    V_t(x,pi) = max_{a safe} {m_t(x,a)+beta sum_y Pr(y|x,pi,a)
                                            V_{t+1}(x',pi_y)}.          (M8)

The kernel L must log **eligible exposure even when no correction is recorded**, independent safety gate audit and the retained controller update. The terminal cost and f are still the original qualification/accepted-service problem. Replacing the posterior mixture by a mean correction count loses covariance between progress, next-state support and joint acceptance. An apparent increase in first-stage autonomy can lower logged interventions and the *supply of a particular byproduct* without lowering enterprise value when old policies and acquisition methods remain safely and legally optional. A forced controller swap or loss of access is different.

Neither M1 nor M2 says that data acquisition on the best routine policy always substitutes for a target experiment. The actual condition is a verified safe-reachability/policy-dominance relation **for the specific customer bundle and deadline**. Endogenous demand, fleet coordination, manufacturing capacities, skills and capital access enter through m,k,P,f and can change the result, but cannot be substituted by a benchmark-to-dollar coefficient.

### 6. Close prior art, falsifiers and research bridge

These are **standard conditional controlled-Markov, coupling and probability constructions**. Ross, Gordon and Bagnell (2011), [DAgger](https://proceedings.mlr.press/v15/ross11a.html), already establishes the importance of policy-induced state distributions (PMLR abstract/metadata checked 18 Nov 2026 UTC). Moldovan and Abbeel (2012), [Safe Exploration in MDPs](https://arxiv.org/abs/1205.4810), and Turchetta, Berkenkamp and Krause (2016), [Safe Exploration in Finite MDPs with Gaussian Processes](https://arxiv.org/abs/1606.04753), treat constrained safe reachability; their safety guarantees are **not** inherited by this illustrative toy model (arXiv abstracts/metadata checked 18 Nov 2026 UTC). ThriftyDAgger, [Hoque et al. (2022)](https://proceedings.mlr.press/v164/hoque22a.html), treats supervised human intervention budgets; earlier chapter records the source boundary. Farboodi, Koh and Xia's [Data-Driven Automation](https://arxiv.org/abs/2606.10127) already values production-generated data and complementarities; this work does not re-label those ideas as new. Parent LP duality/resource prices, multilinear bundle interactions, optional retained policies and dynamic production learning are inherited. No prior-art search establishes a new publishable theorem.

Concrete disconfirmation: (i) an approved routine policy reaches the nominally missing second state, making p_1^R>0 and defeating the asserted zero cut; (ii) safety or operator constraints make G/E infeasible in the same customer deployment; (iii) the claimed joint recipe fails independent held-out validation, setting its Delta to zero; (iv) customer demand is already served, or a competent S dominates; (v) routine can get comparable qualifying data for lower opportunity cost; (vi) empirical customer bundle outcomes are additive rather than complementary. Log exposure, gate/false-negative audit, controller lineage, operator minutes, all-attempt accepted production, customer demand, final joint qualification and relevant rights before making a policy claim. These are *measurement targets*, not measurements.

**Exact next proof/identification gap.** Extend (M8) to **regime-dependent, partially observed** progression and customer qualification under a binding *pathwise* operator/safety budget, and distinguish policies that expand reachable support from those that merely shift its probability. The empirical gating experiment should jointly estimate second-exposure/correction eligibility and complete accepted-service qualification, not only marginal task success. Preserve the November 22 integrated argument/Models A-B synthesis and November 29 official quantitative backbone obligation. No dated gate is passed by writing this theorem.
