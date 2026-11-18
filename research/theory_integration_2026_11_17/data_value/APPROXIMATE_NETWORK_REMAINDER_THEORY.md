# When Capabilities Become Production — approximate network influence, production value, and hard support

**18 November 2026 | private theoretical continuation; not a measured robotics effect or certified safety plan.** This develops the *same* [network-interference question](NETWORK_INTERFERENCE_THEORY.md): when may a partial controller/operator/customer network map support a complete source-data, target-grounding, embodiment or retained-policy economic decision? The full state remains qualified controller/embodiment/old-policy set Q, observed and prospective orders ω, optimized accepted-service production V(Q;ω), persistent transfer regime θ and complete-policy payoff Jθ(π), with terminal V counted once. An extra "value of data" payment is not added.

## A practical distinction: near-separable value is not near-separable safety

A radius-r neighborhood in the **union** of checkpoint-sharing, human dispatch and customer-demand edges might approximate *economic* spillovers, while failing to exclude an arbitrarily rare joint recovery path. We therefore need **two separate certificates**: (A) a defensible bound on missing economic influence for the **entire adaptive policy**, and (B) a hard feasible-support or independently justified risk-and-abort certificate for the actual proposed policy. A small statistical error in mean service does not prove (B).

Each candidate π is a complete nonanticipatory history-to-action rule choosing routine deployment, deliberate grounding, redesigned embodiment, isolated versus shared checkpoint training, old-version retention or specialist capacity with the same rights, scarce operator time and customer order horizon. It determines visited field states, failure/recovery records, future qualification and orders. A local surrogate may approximate π's payoff but is *not* automatically a physically feasible deployment policy. θ is held **fixed through a complete history**. No rectangular adversary may pick a fresh θ after seeing customer orders.

## Result 1. A same-regime whole-policy value-error and ranking certificate

Take a finite horizon t=0,...,T-1 and an arbitrary persistent θ in identified set Θ. Let Kθ,t be the *true complete controlled-network history transition*, and \(\widetilde K_{\theta,t}^{(r)}\) an r-neighborhood surrogate. They may be history-dependent and non-Markovian in a reduced state; use the **complete** history, including zero customer orders, unassisted qualification, retained checkpoints and all operator conflicts. The policy π is the *same* measurable rule under both systems, conditional on its own realized history and common randomization.

For every matched prefix h_t and action a supported under the two models, suppose \(d_{\rm TV}(K_{\theta,t}(\cdot\mid h_t,a),\widetilde K_{\theta,t}^{(r)}(\cdot\mid h_t,a))\le\epsilon_{\theta,t}^{(r)}(\pi)\). This uniform, support-aware bound is **an assumption to justify**, not an estimate inferred from a handful of unrelated sites. Suppose the two models' contemporaneous accepted-service net contributions at a matched prefix differ by at most δθ,t; their time-t contribution range has span at most R_t, and terminal optimized production V (once) has range span R_T. Define \(M_t=\sum_{u=t+1}^{T}R_u\), with R_T the terminal span. Then:

\[
|J_\theta(\pi)-\widetilde J_\theta^{(r)}(\pi)|
\le E_\theta^{(r)}(\pi)
:=\sum_{t=0}^{T-1}\delta_{\theta,t}
+\sum_{t=0}^{T-1}\epsilon_{\theta,t}^{(r)}(\pi)M_t. \tag{A1}
\]

If t's service payoff is determined *after* its transition rather than at the matched prefix, its range must also enter M_t. Matching the timing matters. The bound is conservative, often far from sharp, and requires bounded customer/physical contribution. It incorporates learning-generated new qualifications, demand response and positive/negative training transfer through the complete transition kernel; no additive source-return functional form is assumed.

For any two potentially admissible complete policies π and π0, with the **same θ in each counterfactual**, a strict economic ranking holds across Θ if

\[
\inf_{\theta\in\Theta}
\{\widetilde J_\theta^{(r)}(\pi)-\widetilde J_\theta^{(r)}(\pi_0)
-E_\theta^{(r)}(\pi)-E_\theta^{(r)}(\pi_0)\}>0. \tag{A2}
\]

This is not the incorrect difference between two independently minimized worst-case outcomes; it compares **paired worlds**. A1–A2 follow by coupling and the triangle inequality; the complete proof and scope are in [APPROXIMATE_NETWORK_PROOF_LEDGER.md](APPROXIMATE_NETWORK_PROOF_LEDGER.md). They are standard bounded-kernel and robust-value reasoning, not asserted original mathematical principles.

**Why this is not just a sign threshold:** a local exposure map is economically useful only when its residual bound controls **every history the intervention itself makes possible**. A learned new embodiment can create distant checkpoint interactions and new customer orders; a bound calibrated only on the incumbent policy cannot be applied to the new complete policy. Strongest case: under synchronous one-hop transition dependencies, local policy decisions and no unmodeled global dispatch or checkpoint broadcast, induction gives a finite causal cone of radius T for T transitions; a neighborhood covering the cone is *exact* for focal outcomes. This is a sufficient locality structure, not a default property of cloud-updated robots or globally pooled operators. See the proof ledger.

## Result 2. Apply the bound to the previously corrected selective-rollout claim

Retain the earlier synthetic baseline 7, eligible A customer weight 0.7 with own approved gain 0.5, B weight 0.3, and true B per-customer loss s after A rollout. Assume the properly matched local analysis puts s_local ≤0.6; a **separately justified** omitted-network remainder gives s−s_local≤η, true own-A omitted total contribution can be as low as −0.02, and *incremental* network coordination cost is 0.03. Stable pre-action weights and genuinely nonoverlapping costs are maintained. Thus

\[
\Delta_{\rm full}\ge .7(.5)-.3(.6+\eta)-.02-.03
=.12-.3\eta. \tag{A3}
\]

At η=0.25, the conditional lower contribution gain is **0.045** and lower total is **7.045**; at η=0.4 the lower advantage vanishes; at η=0.5 the lower difference is −0.03. The bound applies only when the true A own gain, demand strata and source/target order denominator are covered. The η values are synthetic sensitivity inputs, **not observed tail measurements or a proposed physical safety authorization**. This sharp affine envelope is a restricted special case of A2, retaining the old controller and specialist as live competitors. Under additional qualification, order or safety restrictions the endpoints may cease to be sharp. If weights themselves respond to deployment outside the registered target population, use A1 on the complete demand transition instead of A3.

## Result 3. Exact finite adaptive test: a valid bound can be inconclusive

The [scoped finite-state diagnostic](approximate_network_remainder.js) has qualification Q∈{0,1}, customer opportunity D∈{0,1}, routine R and grounding G, and two *persistent* regime types, good/bad. Current accepted contribution is \(0.5QD-0.15\,1\{G\}\), terminal qualified order production \(2QD\). Grounding probability and customer demand transitions depend on Q, D, action and θ. The local approximation perturbs the qualification transition down by .02 and demand up by .015 under the same θ; actual one-step total variation is bounded by **0.0259** on this enumerated finite menu.

For two decisions and final qualification, contemporary payoff span ≤.65 and terminal span ≤2. Thus the verified A1 envelope for each policy is \(0.0259(2.65+2)=0.120435\); the paired A2 allowance is 0.24087. The complete true example has adaptive grounding exceed retained routine by only **0.01157888** in good and **0.00730944** in bad. The local model also ranks adaptive above retained, but its robust lower certificate is **−0.22638524**: positive estimated mean gain is **not robustly identified from this coarse bound**. The exact full toy model is known, so its two actual rankings can be computed; the negative bound reflects what can be asserted when only the restricted approximate information is available. It does not prove adaptive grounding is harmful or that collecting free optional data reduces optimal value.

The importance of data content is endogenous: a routine intervention may improve the controller but change which failures/teleop corrections it ever sees; a grounding or embodiment move may make distant source data relevant only if its updated transition and qualification kernel supports accepted whole-service production. Field failures, recovery, teleoperation, simulation, synthetic labels and public pretrained representations require separate kernels, rights and comparable matching. No percentage from a benchmark enters the revenue function directly.

## Result 4. Arbitrarily small statistical interference can invalidate hard recovery feasibility

Two sites each require one operator with probability .1. The verified-disjoint *hypothetical* law has \((P_{00},P_{10},P_{01},P_{11})=(.8,.1,.1,0)\). For any \(0<\eta\le.1\), another law \((.8+\eta,.1-\eta,.1-\eta,\eta)\) has **identical individual failure marginals** and expected operator load but total variation distance \(2\eta\) from the first. It has a supported simultaneous recovery path using **two** operators and breaks hard capacity B=1. For η=.001, the laws differ by only .002 in total variation, and the probability of seeing no simultaneous recovery in 1,000 independent episodes remains approximately .3677. The independence illustration is not a field confidence statement. **There is no positive finite-TV radius that by itself certifies a hard support constraint.**

One feasible way forward, *conditional on independent safety review*, is a preauthorized admission cap/serial staging/abort **before** an unsafe support path is reachable. Such a rule changes production, reporting, qualification, the reachable history and usually expected revenue, so it must be evaluated as a **different complete policy**, not by applying the old A2 gain after removing adverse outcomes by fiat. A chance-constraint design is possible only with an explicitly chosen tail tolerance and validated emergency response; it cannot be substituted for a hard-cap premise.

## Falsifiable observations, alternative assumptions and nearest prior results

A defensive field design needs the union controller/operator/order graph, fixed pre-action eligible-customer denominators including *zero* orders, matched whole accepted-service trials on old, shared and isolated controllers, retained fallback, real sequential action propensities and **joint timed** operator resource support. To justify ε, bound omitted edges by observed/engineered checkpoint isolation, trace dispatch coverage and negative-control far-site outcomes **under the target policies and their possible new states**, with honest treatment of unsupported regimes. Aggregated rollout value alone cannot separate data learning from customer demand diversion or shared human queues. [Prospective measurement protocol](APPROXIMATE_NETWORK_EMPIRICAL.md) specifies discrimination and failure criteria; no such field panel is claimed here.

**Prior-art boundary (verified source metadata/abstracts 18 Nov 2026):** Leung (2022), *Causal Inference Under Approximate Neighborhood Interference*, *Econometrica* 90:267–293, DOI [10.3982/ECTA17841](https://doi.org/10.3982/ECTA17841), already develops approximate, nonzero distant exposure effects and statistical inference. Sävje, Aronow & Hudgens (2021), *Average Treatment Effects in the Presence of Unknown Interference*, *Annals of Statistics* 49:673–701, DOI [10.1214/20-AOS1973](https://doi.org/10.1214/20-AOS1973), already derives estimator behavior with limited unknown interference. The coupling value inequality, causal cone and rare-tail hard-cap counterexample are ordinary probability/control arguments. The *candidate* research synthesis is their physical–economic combination with joint customer qualification, endogenous learning/source choice, alternative embodiments and a nonfungible operator support condition. **Scientific novelty and empirical calibration have not been independently established.**

**Next intellectual gap:** derive a practicable, defensible **policy-uniform** omitted-influence envelope from measured controller lineage, customer-demand connections and operator scheduling without extrapolating beyond observed safe support. Compare that envelope with a fully specified safe admission policy and a capable specialist, not with a deliberately weak baseline. Keep November 22 Models A/B review open and December 25, 23:59 Eastern deadline unchanged.
