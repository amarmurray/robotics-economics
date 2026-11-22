# Lawful predispatch observability and the economic value of source-trained production

**22 November 2026 — continuation of *When Capabilities Become Production*, November 22 Models A/B scientific gate OPEN.** This is a constructive step after [the action-cover theorem](DECISION_SUFFICIENT_REPORT_COVER.md) and [adaptive Bellman-occupancy theorem](POLICY_OCCUPANCY_DECISION_SUFFICIENCY.md), **not** a separate Q-number, novel general information theorem, field estimate or robotics policy authorization.

## Question and environment

A source-trained robot can qualify multiple recipes yet lack the information needed to dispatch the right recipe to a paying customer. Target grounding can mean **(i) physical training that changes ability**, **(ii) a timely report that changes dispatch information**, or both. New embodiment E alters the lawful menu and throughput. What is the highest customer-accepted-and-paid production value of a report that the producer is *actually authorized to observe and use before dispatch*, not a hindsight oracle?

At a single fixed production-decision epoch of investment program k∈{R,S,G,SG,E}, let H be the finite set of **available-information histories** of an original eligible customer cohort, p_h>0 the stated cohort weights, M_k(h) its certified lawful feasible actions, and q_k(h,a) the complete conditional Bellman accepted-and-finally-settled net paid-production return of action a. q includes downstream learned production and opportunity cost in the same original program; it must not also receive a “future data premium.” Historical learner versions, retained R, operator occupancy, buyer offer/no-order, price and rights are among h, only to the extent legitimately available to an agent. Neither a latent private buyer need nor a counterfactual unavailable checkpoint is automatically in H.

An exogenous, predispatch, signed-and-timely **usable observation** z:H→Z induces atomic blocks B_z={h:z(h)=z}. “Usable” requires the actual observation channel, inference timestamp, physical availability, consent for this purpose, legal permission for the deciding agent to receive/use it, and no material perturbation of q or p caused by acquiring it. The acquisition/legal architecture is *part of the definition*, not a statistical afterthought. The lawful report φ may postprocess z but cannot separate two histories in the same observation block. For an action to be used in a pooled cell C its physical/rights identity must be the same and a∈∩_{h∈C}M(h). If this intersection is empty, that pooling is infeasible, not zero-return.

The unrestricted full-information economic benchmark is W*=Σ_h p_h max_{a∈M(h)}q_h(a). Define Q_B(a)=Σ_{h∈B}p_h q_h(a) and M_B=∩_{h∈B}M(h) for each observation block B. A postprocessed observation with ≤L symbols has value

W_L(z)= max_{φ measurable w.r.t. z, |range φ|≤L} Σ_{C∈φ} max_{a∈∩_{h∈C}M(h)} Σ_{h∈C}p_h q_h(a).

The maximum of an empty feasible set is “infeasible,” never silently imputed as a payment zero.

## Proposition 1: lawfully observable report frontier and an irreducible information deficit

Assume finite H and A, fixed p,q,M, costless exogenous z and unrestricted *postprocessing* of its usable symbols. Then:

**(a) No alphabet budget:** If every M_B is nonempty, W(z)=Σ_{B∈B_z}max_{a∈M_B}Q_B(a). If any M_B is empty, a universally lawful z-measurable dispatch rule does not exist until the observation is refined, the action menus legitimately expanded, or the domain is restricted.

**(b) Finite label budget:** Exactly
W_L(z)=max_{D⊆A, 1≤|D|≤L, D∩M_B≠∅ ∀B} Σ_{B∈B_z}max_{a∈D∩M_B}Q_B(a).
There is no need to enumerate all arbitrary history-level reports. This differs from the preceding unrestricted action-cover equation: the economically usable units are **observation blocks**, not individual histories, and their Q is pooled before the maximization.

**(c) Lossless observation:** W(z)=W* iff every positive-mass observation block has an identical lawful Bellman-optimal action in ∩_{h∈B}A*(h), A*(h)=argmax_{a∈M(h)}q_h(a). When this holds, the least number of report labels is the set-cover number of the **block-level joint optimal-action intersections**, not merely a pairwise-conflict graph on histories. If even one block lacks such a common optimum, no increase in the final report alphabet alone recovers W*.

**Proof.** Every z-measurable action is constant on each atom, so optimization separates by atomic blocks, proving (a), with common-menu feasibility explicit. Every L-label report uses at most L actual action identities; its sum is bounded by the best choice from those identities on each atomic block. Conversely, choose at most L lawful action identities and map each atom to the action maximizing Q_B within that set, using the action as its report symbol; this implements the right side, proving (b). For (c), subtract each cell's paid contribution from the fully informed maximum: each p_h[max_{a∈M(h)}q_h(a)-q_h(a_C)] is nonnegative and p_h>0, so aggregate loss is zero iff a common maximizer is selected at every contained h. Applying the same action cover to atomic blocks gives the minimum lossless alphabet. QED.

**Structural consequence.** The preceding perfect-observation action-cover number κ_unrestricted is a *lower bound* on required labels, not an achievable implementation target. The lossless problem can be impossible under fixed licensed telemetry even with arbitrarily many report labels. A sensor's technical information content and its legally usable economic decision capacity are separate, falsifiable objects.

## Proposition 2: admissible signal refinement, value and its sharp scope

If z' is legally usable, exogenous, costless and deterministically refines z (every z' atom lies inside a z atom), and all prior lawful policies can ignore z', then W(z')≥W(z). More generally, a lawful Blackwell garbling of z' to z preserves the old policy. **Proof:** every z-measurable action rule is also z'-measurable, so the feasible policy set is nested. This is a standard Blackwell-type option argument, not a claim about novel sensor theory.

The increment W(z')−W(z) is a **gross optimized paid-production information value**, conditional on actual lawful menus and complete paid Q. If extra sensing, curation, license, training, lost service time, delay, privacy remediation or compute costs C are required, the *net* intervention is W(z')−C versus W(z), with no guaranteed sign. Likewise an imposed training recipe may lower realized performance despite freely optional raw source availability being weakly valuable. A physically informative but contractually unusable z' is **not** a refinement of the controller's feasible information set. When acquisition changes customer demand, learning, failure/recovery or tomorrow's actions, use the earlier full dynamic J and Bellman occupancy, rather than the fixed-stage formula.

## Counterexample: a two-symbol oracle is unimplementable under lawful telemetry

Take three equally likely original-buyer predispatch contexts h1,h2,h3 with qualified **SG** specialists a,b and a retained legal fallback R worth 1/2 in each context. The complete paid action returns for a,b are (1,0), (0,1), (1,0). For this example the old fallback never exceeds the specialists in the relevant pooled choices. The unrestricted two-symbol report sends h1,h3→a and h2→b, earning **W*=1**.

A legally usable existing report z distinguishes {h1,h2} from {h3}, *not* h1 from h2. Its best fully licensed postprocessing earns (1+1)/3=**2/3**: the first block chooses either specialist, the second chooses a. A one- or twenty-symbol report applied only to z cannot recover the absent distinction. A separately licensed, timely target field z' distinguishing h2 from {h1,h3} permits W(z')=1 with two labels. This is an economic **target-information** improvement, not physical grounding or a model-accuracy change.

Now assume a different, separately signed new embodiment E has identical paid return **3/4** in all three original contexts, under the same exogenous market and with upfront embodiment cost already included in that number. With only z, SG−E=2/3−3/4=**−1/12**; with z' and a once-counted additional reporting/licensing cost 1/8, SG−E=1−1/8−3/4=**+1/8**. The old R action is retained. Under these *stipulated synthetic* q values, the raw report-value gain is 1/3, its net gain 5/24, and the investment ranking reverses. No benchmark was mapped into dollars, and no field estimate or real license was obtained. All units are normalized complete original-buyer paid contributions.

This construction distinguishes a minimally sized *oracle partition* from an implementable **information architecture**. It also distinguishes “licensing a target signal” from “training on more source data,” and the ability of an embodiment to avoid the same observation problem by delivering a generalist response.

## Proposition 3: supported Q uncertainty and a minimax legal-report criterion

Without original-buyer conditional paid-Q evidence, a policy cannot choose actions using the unknown true response table as if it had been observed. Let Θ be an explicitly supported joint set of possible (p_θ,q_θ,M_θ) regimes, with common certified legal menus M_B for every regime and z blocks fixed. A **regime-agnostic, possibly randomized** report policy assigns probabilities π_Ba over actions in M_B. Its worst-case regret against the full-information benchmark for each regime is

R(π,θ)=Σ_h p_{θ,h}max_{a∈M_θ(h)}q_{θ,h}(a)−Σ_BΣ_{h∈B}p_{θ,h}Σ_a π_Ba q_{θ,h}(a).

For finite Θ, min_π max_θ R(π,θ) is a linear program: minimize r subject to r≥R(π,θ) for every θ, π_Ba≥0, Σ_aπ_Ba=1 and π_Ba=0 for unsupported actions. More generally Θ must be constrained **jointly** by shared learner, operator, original-buyer offers/payments and rights; independently guessed intervals need not correspond to any feasible shared-fleet counterfactual.

There are **two different sufficiency tests**. If an omniscient analyst may choose a different policy after being told θ, zero reporting regret for each θ requires ∀θ∀B:∩_{h∈B}A^*_θ(h)≠∅. A *single deployable policy not told θ* has zero worst-case regret only if ∀B:∩_{θ∈Θ,h∈B}A^*_θ(h)≠∅ (for all positive-mass states). The latter can fail despite the former holding. A toy single-block, two-regime table with opposite uniquely optimal actions gives deterministic minimax regret 1, mixed minimax regret 1/2, and zero if a licensed exogenous predecision signal reveals the realized regime. This is a prior-art robust decision/LP construction, not proof of how uncertainty is distributed in deployed robot models.

## Integration with Model A, Model B and the full program

**Model A:** For fixed signed customer demand, qualified menus and one-step paid-Q, estimate or bound the observation atoms from actual learner version, order/offer, operator, report rights and timeliness. Use Proposition 1 to distinguish *disallowed separations* from expensive but implementable separations. This does not impute missing paid-Q from robot benchmark scores.

**Model B:** For production-generated field success/failure/recovery, teleoperation, licensed simulation/synthetic/public-pretrained sources, target-specific grounding and embodiments, the report and data action may change the subsequent full-history kernel and future action menus. The controller must use lawful observations available **when it acts**. Compute each SG/E program's own full J and policy-occupancy regret. Apply the fixed-stage theorem only to an embedded *exogenous* observation transition with a common underlying market. Never append a second continuation premium.

**Economic boundaries:** Separate acquisition of extra source trajectories; licensing/aligning an already useful target signal; deliberately acquiring target labels through teleoperation; and deploying a different physical body. Distinct rights to record, train, pool, transfer, reveal and dispatch can give different z even with identical bytes. Joint bundle demand and a scarce operator slot can create higher-order interactions; hidden buyer type is not evidence that an unpermitted sensor can reveal it.

## Empirically discriminating obligations

Before any practical policy recommendation: (i) produce signed legal and physical action-menu snapshots at the original-buyer *offer* denominator, including no-orders and failed/refunded services; (ii) timestamp precisely when source checkpoint, buyer order, report signal and dispatch decision become available; (iii) document rights **to use** each report by the actual controller, not just to collect it; (iv) measure joint, arm-matched conditional whole-horizon accepted/settled paid Q under R/S/G/SG/E and fallback, or defend a joint Q identified set; (v) validate learner and robot/operator interference and capacity; (vi) determine whether report acquisition changes demand, qualification, legal state or producer occupancy and switch to the dynamic model if so; (vii) audit prospective information refinements against permitted actual signal kernels and paid outcomes.

[Prospective evidence graph](LAWFUL_REPORT_OBSERVABILITY_EVIDENCE.md), [executable exhaustive enumeration](lawful_signal_partition_model.js), [record](lawful_signal_partition_results.json), [independent Fraction audit](lawful_signal_fraction_independent.py), [student exercises](LAWFUL_REPORT_OBSERVABILITY_EXERCISES.md), [separate solutions](LAWFUL_REPORT_OBSERVABILITY_SOLUTIONS.md). No physical intervention or customer private data is proposed as already authorized.

## Closest prior art and boundary of contribution

Blackwell's comparison of experiments (1951/1953) already establishes the garbling/information-order logic. A primary-source retrospective/general-space proof is Khan, Yu & Zhang (2025), DOI https://doi.org/10.1016/j.econlet.2024.112146; Goel & DeGroot (1979), DOI https://doi.org/10.1214/aos/1176344790, study comparison of experiments. Dynamic/decentralized information structures are established, with Charalambous, Guvercin & Djouadi (2026), https://arxiv.org/abs/2605.27645, another related direction, not a new robotics result here. The preceding repository action-cover, dynamic-policy occupancy, O-ring and resource-price results are prior foundations. *Data-Driven Automation* §5 and Appendix B already account for future training data and source complementarity; no rediscovery claimed. The candidate **research synthesis** is a physically/legal original-buyer, whole-paid-production implementability and source-to-qualified-recipe comparison. Empirical validation and independent novelty assessment remain absent.

**November 22 acceptance:** synthetic Models A/B and the constrained signal theorem are mathematically articulated but scientifically OPEN. No signed legal/physical SG/E action panel, real customer-paid Q, shared-learner transition bounds, matched source/target report rights, numerical official BEA/BLS interindustry requirements coefficients, full-repository CI or independent review. Theory majority through December 6; unchanged final December 25, 2026, 23:59 America/New_York.
