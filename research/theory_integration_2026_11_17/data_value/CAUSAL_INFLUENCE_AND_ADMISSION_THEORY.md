# When Capabilities Become Production — causal influence envelopes and safe admission

**18 November 2026 | continuation of approximate network interference, not a calibrated result or safety approval.** This answers the *same* research question left by [APPROXIMATE_NETWORK_REMAINDER_THEORY.md](APPROXIMATE_NETWORK_REMAINDER_THEORY.md): how could controller lineage, customer-demand topology and shared dispatch yield a **policy-uniform** economic residual bound, and can a physically admissible staged route beat a competent specialist? No additional data premium is added to customer production.

## 1. Economic objects and the incomplete network

The production state at decision time t includes retained qualified recipes Q_t, controller and embodiment versions, source observations and their rights, observed customer orders and the *original* eligible zero-order registry, operator reservations and recovery/abort status, and the complete action/observation memory needed by a nonanticipatory policy. An investment strategy π specifies routine field production, deliberate target grounding, controller isolation, a new embodiment, a specialist or retention of old qualified policies at **all** its possible histories. A latent transfer regime θ is persistent over the whole history and belongs to Θ. True captured accepted-service contribution, including interim production and one terminal optimized production value V(Q_T;ω_T), is J_θ(π). A local controller/operator/demand network surrogate yields tilde-J_θ(π); its approximation must never create physical permission.

Partition the complete dynamic state into n blocks: sites, controller lineages, operator dispatch/reservation resources, customer demand links and, when feedback is nonlocal, **policy decision/memory nodes**. Distinguish controller update (C), operator (O), market/order (M) and input/coordination (P) edges; this is a multiplex causal graph, not merely geographic proximity. A shared worldwide checkpoint or a central operator dispatcher is a real global node, not an ignorable low-correlation residual. An action can endogenously add edges or reach a new embodiment; then its applicable matrix must cover that support or the bound is invalid.

For a predeclared set of complete policies Π and every θ, assume that true and truncated transitions admit a **joint sequential coupling**, with initial matching states and for each jointly reachable matched pair (z, z~),

\[
 \Pr(X_{t+1,i}\ne\widetilde X_{t+1,i}\mid z,\widetilde z,\pi,\theta)
 \le \sum_j C_{t,ij}{\bf1}\{z_j\ne\widetilde z_j\}+b_{t,i}. \tag{C1}
\]

The arrays C_t≥0 and b_t≥0 are componentwise upper envelopes over *all* supported histories, θ and policies in Π, not fitted average effect coefficients. A differing adaptive action is represented in the decision node and its outgoing edges, not assumed away. A common exogenous shock may require a joint coupling construction; **marginal site TV estimates alone do not establish C1**. Conditional factorized site kernels with an explicit shared-innovation state and Dobrushin-style single-coordinate conditional bounds are one sufficient construction. No independence of eventual customer qualifications is needed.

Let e_{t,i} be the coupled mismatch probability, e_0=0. If the difference in each actual versus surrogate captured contribution at t, including its selected action, is bounded by δ_t plus the weighted mismatched components \(\sum_i w_{t,i}{\bf1}\{X_{t,i}\ne\widetilde X_{t,i}\}\), with the same at terminal T and **one** V_T, then

\[
 e_{t+1}\le C_t e_t+b_t,\qquad
 |J_\theta(\pi)-\widetilde J_\theta(\pi)|
 \le E(\pi):=\sum_{t=0}^{T}\delta_t+
 \sum_{t=0}^{T} w_t^\top\bar e_t,\quad
 \bar e_{t}=\sum_{s=0}^{t-1}C_{t-1}\cdots C_{s+1}b_s. \tag{C2}
\]

At t=T, δ_T covers only the terminal V mismatch. Set δ_T=0 where V is the same state-based function in both models. The empty matrix product equals identity; the e bound may be clipped coordinatewise at 1. Component ranges w must be derived from **accepted service and captured value** (possibly bounded from the qualified production LP/resource-price certificate), not from benchmark success percentages. This is a bounded-differences/Dobrushin-style path-sum bound, not a new general probability theorem. Importantly, it handles opposite-signed technical transfer or market substitution because it bounds absolute differences.

For two separately **admissible** complete policies π and π0, there is strict same-world economic dominance if

\[
 \inf_{\theta\in\Theta}
 \{\widetilde J_\theta(\pi)-\widetilde J_\theta(\pi_0)
 -E_\theta(\pi)-E_\theta(\pi_0)\}>0. \tag{C3}
\]

If Π-uniform envelopes are used, the corresponding E may be common. Identifying an actual θ-conditioned minimum needs defensible conditional bounds; pooled differences alone do not supply it. C1–C3 refine the earlier whole-history TV bound A1–A2 by charging only economically relevant **reachable graph paths**. They are not automatic improvements: C1 is substantially more structural and may fail even when A1 holds.

### When a partial graph is useful

Suppose an omitted intervention reaches a focal service only through paths of length at least r+1, there are at most d^ℓ such relevant length-ℓ paths, each path transmits no more than α^ℓ in its product of conditional influence weights, and each remote source shock has a certified upper size β at the start. For a maximum T-step propagation, the unobserved focal mismatch is bounded by

\[
 \beta\sum_{\ell=r+1}^{T}(d\alpha)^\ell
 \le \frac{\beta(d\alpha)^{r+1}}{1-d\alpha}
 \quad\text{if }d\alpha<1. \tag{C4}
\]

This geometric display is valid only for the specified one-shot remote-source topology (or after appropriately summing distinct shock times); do not use it in place of C2 with ongoing shocks. If dα≥1, finite-horizon sums still exist but no uniform decaying-radius certificate follows. A high-fanout cloud update, unknown demand substitution or new robot embodiment can defeat C4. Engineering isolation with zero training/replay permissions can set a particular causal weight to exactly zero; observationally nonsignificant distant correlations cannot.

## 2. Exact synthetic route and a credible comparator

Consider a three-node A-site → shared controller X → B-customer propagation skeleton with omitted direct mismatch shock at X and one subsequent X→B influence. It is **not** a measured robot market. With e_{1,X}=b_X and C_{B,X}=c, we obtain e_{2,B}≤c b_X. B represents 30% of the original customer opportunity registry, with an assumed 10-unit maximal per-customer contribution swing, so the full economic weight is \(w_{B}=0.3(10)=3\).

The older connected-network partial rollout had retained value 7, a 70% supported A group and a 30% exposed B group. The following numbers are all explicit **conditional sensitivity assumptions** and already include only nonoverlapping costs:

| Complete route | A gain per A opportunity | local B loss upper per B opportunity | own-A residual loss | incremental coordination cost | \(b_X,c\) | additional remote B loss bound | lower full J |
|---|---:|---:|---:|---:|---|---:|---:|
| Unstaged shared routine rollout | .50 | .60 | .02 | .030 | .050, .40 | \(3(.050)(.40)=.060\) | **7.06000** |
| Serial admission, isolated/controlled updating | .44 | .45 | .02 | .045 | .015, .25 | \(3(.015)(.25)=.01125\) | **7.09675** |
| Retained qualified old controller | — | — | — | — | no intervention | — | **7.00000** |
| Competent specialist alternative | — | — | — | — | separately qualified | — | **7.08000 assumed upper** |

For the first route, \(\Delta_{\rm open}\ge .7(.50)-.3(.60)-.02-.03-.06=.060\). For serial admission, \(\Delta_{\rm serial}\ge .7(.44)-.3(.45)-.02-.045-.01125=.09675\). If the competent specialist's *true same-regime* production is at most 7.08 on that same calendar/resources and serial admission is independently safety-certified, the latter strictly beats the specialist by at least **0.01675** and the retained controller by **0.09675** normalized units. The un-staged strategy **cannot** be ranked above the specialist on this lower-bound evidence (and may violate hard safety). It may still have greater actual economic value in some regimes; a lower bound is not its exact value. This construction shows a potential choice between shared productive data and a safer, narrower admitted data stream rather than selecting data volume on its own.

Causal weights \(b_X,c\), local B bound, A benefits, specialist upper, customer weights and the qualified-service payoff range are **not empirically calibrated**. This table does **not** certify any true field investment or say the serial option dominates the unstaged option in every possible world. Counterfactual A benefit, new controller qualification, lost orders under admission, and independent specialist opportunity cost must be measured under complete policies; changing admission changes future learning and demand.

## 3. Hard operator admission as an independent physical premise

An operator budget B=1 cannot be certified from C2 or C4. Consider a **candidate** serialized policy that requires every recovery consumer (including retained versions, remote sites, manually initiated operations and shared infrastructure) to obtain an exclusive reservation *before* initiating a trajectory that could need human recovery. When a reservation is unavailable, a **verified non-operator-dependent safe stop or refusal to start** must precede the dangerous trajectory; releases are recorded and a recovery token cannot be duplicated. If those engineering premises really hold for every supported history, induction on token transitions establishes active recovery demand at most one. No independent site recovery probabilities, average headcount, or 1,000 collision-free trials establish those premises.

Critically, the reservation is more than a scheduling spreadsheet: once recovery is needed without a token, a queue **does not** make two simultaneous emergencies safe. The presumed safe stop itself must be qualified for the actual embodiment/site. This contract is a formal sufficient condition, **not** a real safety signoff. It can reduce accepted customer throughput, create zero orders, select different field data, change what is teleoperated and alter qualification rates. That is why the serial route's lower A gain and higher cost are not gratuitous; all induced outcomes belong in its own J rather than crediting it with unstaged productivity.

## 4. Empirical discriminators, stronger alternatives and failure cases

The C1 weights can be justified most credibly by verified controller lineage/access permissions, sandboxed checkpoint builds, scheduler topology, customer-order and input-network registry, and *safe matched policy perturbations over the reachable target state space*. Define a conditional single-node sensitivity as a supremum over two otherwise matched histories differing in one upstream controller/dispatch/customer component, then bound the downstream next-state law. Unmeasured history cells must remain unknown, not set to zero. Whole-service customer acceptance including zero orders, cross-site operator peak events, and frozen-demand qualification trials measure economic w and physical support separately.

An observation of small average far-site effects is compatible with a rare, high-consequence regime and cannot upper-bound C1 uniformly; partial observational positivity or uncontrolled shared checkpoints destroys it. When C1's bound is wide, the honest decision is to retain the specialist/old controller or seek safe isolation and a more informative matched design. A cheap standalone specialist could dominate every route; a free qualifying routine-data byproduct could eliminate the need for deliberate target grounding; controller mixing could be complementary rather than destructive. These remain live countermodels.

**Closest prior art, not a novelty claim:** influence matrices, disagreement propagation, path expansions and finite-horizon value bounds are standard coupling/control arguments; Leung (2022), *Econometrica* 90:267–293, DOI https://doi.org/10.3982/ECTA17841, already studies approximate neighborhood interference. DDA arXiv:2606.10127 already models forward data value and complementarity. The candidate *synthesis* is to connect these restrictions to economic customer qualification, policy-induced usable data, embodiments and physical dispatch admission inside one production alternative set. Neither a new general estimator nor field-validated robotics effect is claimed.

**Precise next unresolved question:** construct a practically auditable conditional influence envelope with unknown customer demand responses and shared-controller reuse, then ask which safe, independently approved experiment most reduces the sign ambiguity against a specialist. The November 22 synthesis gate and December 25, 2026, 23:59 America/New_York target remain unchanged.
