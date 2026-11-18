# Policy-dependent demand and persistent transfer — discriminating empirical design

**Prospective research protocol, November 18, 2026. No external trials, customer data or physical robot access.** Complements [TRANSPORT_EMPIRICAL_DESIGN.md](TRANSPORT_EMPIRICAL_DESIGN.md), and tests the theory in [ENDOGENOUS_DEMAND_PERSISTENT_TRANSFER.md](ENDOGENOUS_DEMAND_PERSISTENT_TRANSFER.md). Do not interpret synthetic 14/3/7/10 examples as empirical projections or assign actions that violate site safety policies.

## Causal unit and decisions

The unit must be an initially **eligible commercial customer opportunity**, not a logged robot trajectory or an order observed only after the first action. Register site, available accepted recipe, order-window and demand before route choice, rights to learning material, body/controller lineage and available recovery/operator capacity. Record baseline \(\omega_0\) and safe feasible action set for R (routine productive acquisition), G (deliberate grounding), E (new body), and S (qualified retained specialist).

Assign or infer first action \(A_0\) without conditioning on post-action orders. Follow the same initially eligible population over an announced time horizon, including users who **do not order again**, cancel, are denied safety clearance or switch to specialists. Register customer demand \(D_1(A_0)\) as a *potential outcome of the deployment*, not a fixed population covariate. A common \(\mu\) can reweight baseline opportunity strata; it must not be used as if policy-dependent follow-on order counts were exogenous.

Report both the *policy-specific demand denominator* (new whole-service customer opportunities, accepted price/capture/conditions, within-window composition) and *policy-specific whole-service accepted production* (joint 00,10,01,11 outcomes where applicable, plus retained work and actually paid fallback), linked by independent keys. An autonomous pick/human correction, even if technically successful, is neither an order nor full qualification.

## Longitudinal source-to-production chain

| Time | Required observation | Identification purpose |
| --- | --- | --- |
| Before A0 | Eligible customer opportunity; baseline demand, contracted capture/price, whole-service criterion, specialist/old recipe, site resources and rights | Treatment allocation, feasible alternatives and target commercial weighting |
| First deployment | R/G/E/S version, initial accepted customer contribution, opportunity/acquisition/manufacturing resource cost, assigned safe envelope | Avoid treating production as free when it displaces opportunity or treating a learning expense as an independent data premium |
| Learning/diagnosis | Distinguish field attempts and corrections, failures and recoveries, deliberately assigned teleoperation, simulation, synthetic and public/pretrained inputs; retained update lineage and data rights | Estimate conditional source-to-target transfer without conflating modality with market value |
| Before second action | Independent eligible state-exposure audit, correction gate and missed-error events, reports, support for target states, peak recovery requirement and abort/fallback approval | Identify **pathwise feasible** continuations, including rare positive-support tails |
| Second demand window | All assigned units' new orders including zeros, prices/capture and customer outside alternatives; separately record body/operator availability | Identify policy-induced customer demand and lost reorders, not only successful demand |
| Second accepted production | B/C joint acceptance, whole-service contract fulfillment, resource occupancy, specialist fallback, disallowed/nonattempted states and costs | Recover \(V(Q;\omega)\) and comparable \(J(\pi;m)\) once per period |
| Long-run follow-up | Retained policy and new embodied capabilities, customer referrals/repeat orders, learning interference, continued eligibility | Test the complete history mechanism rather than a one-shot benchmark |

## Identification and decision-relevant contrasts

An initial cluster-randomized R/G/E/S trial across **independent learning pools** with frozen versioning can estimate total intention-to-treat differences in follow-on accepted contribution and customer demand, assuming valid assignment, retention, consistency and full follow-up. But if action G is *never allowed* at rare site/θ state, the potential response is unsupported and **not point identified**. Observational longitudinal adjustment additionally requires sequential exchangeability given measured pre-action histories, positive probabilities of all relevant safe action assignments, and correctly tracked controller interference; without these, state partial-order/capacity bounds and their assumptions explicitly. Safe diagnostics do not justify forcing rare unsafe actions.

Separate quantities that have different causal meanings: (i) initial site-specific route assignment probabilities; (ii) controller-induced **visited state support**; (iii) technical qualification under frozen held-out evaluations; (iv) downstream orders and per-order capture; (v) approved operator/recovery feasibility and (vi) retained qualified service. Model A offers an accepted divisible-service customer-demand envelope; discrete complementary B/C recipes use the full optimized production program. Do not regress an observed post-treatment customer order count into a pre-treatment propensity score and claim transport.

A useful factorial specification compares source mixture \(\times\) target grounding \(\times\) embodiment with matched target-specific technical validation and whole accepted-service measurement, then follows actual route-assigned customer demand. Field trajectories, failures/recoveries, purposeful teleoperation, simulation, synthetic and public/pretrained data are independently coded inputs, not a single "human data volume." Data rights and compute/curation expenses remain real constraints. For source data offered free as an **option**, retain the no-training/old-controller arm, or the design would confuse harmful forced transfer with the value of extra optional information.

## Which results would discriminate the theory?

- **Endogenous demand:** after matched baseline orders, does assignment to routine deployment, grounding or a new body change *later* eligible customer-order mix/value and not just trained success? A static \(\mu\)-weighted formula should mispredict when policy-dependent follow-on demand is material.
- **Support substitution:** does reliable routine exposure give the same authorized target-state support and jointly qualified service as supervised grounding **per common calendar/operator resource**, rather than only fewer correction requests? Is the rare target state missing due to lack of demand, a controller avoidance policy, gate censoring or an actual physical safety constraint?
- **Persistent transfer:** do reports across site/order branches constrain a *common* latent cross-embodiment transfer regime? A customer order that is independent of regime should not license independent priors conditional on each order without evidence of regime heterogeneity.
- **G countermodel:** under previously unsupported G/L safe trials or a validated bridge to simulation, is commercial value closer to the illustrative W+ or W−? R-only sample expansion cannot answer this, and joint accepted-customer service—not scalar benchmark transfer—is the primary outcome.
- **Competent alternatives:** compare S and retention of previously qualified releases, as well as E and free routine data, before claiming a benefit of deliberate acquisition.

## Minimal data table / estimand

Each row: \((\mathrm{pool},\mathrm{site},t,\mathrm{baseline\ opportunity},A_0,\mathrm{source\ type},\mathrm{body},\mathrm{controller\ lineage},\mathrm{eligible\ support},\mathrm{report},\mathrm{recovery\ peak},\mathrm{approved\ fallback},\mathrm{future\ order\ including\ zero},\mathrm{capture},\mathrm{joint\ acceptance},\mathrm{accepted\ output},\mathrm{resource\ spend},\mathrm{rights})\). An aggregation into route-by-regime tables requires credible regime identification or an explicit identified set; do not infer a latent H/L label directly from whether a robot was successful.

The target estimands are \(J_\mathrm{target}(\pi)-J_\mathrm{target}(\sigma)\) for total feasible **dynamic** policies, and the bounds on this difference over the same admitted set of common complete laws. When all conditional kernels are measured and p remains an interval, ED3 gives exact prior endpoints; with incomplete regimes, order-response or joint acceptance information, report a conservative outer interval and named falsifier. Robust maximin comparisons and robust *pairwise* dominance are separate objects.

## Current evidence gap and next field decision

No authorized field intervention, customer data panel, paid-source access or robot safety validation was performed. The program has **synthetic identified examples and prospective identification requirements**, not customer-level observation. The official numeric BEA/BLS production backbone remains missing; a vendor performance post is not a substitute for official interindustry relationships or real economic capture.

The smallest scientifically useful future contrast is a pre-registered same-initial-opportunity R/G/E/S customer-follow-up study with independent frozen-controller learning pools, accurate zero-order denominators and permitted safe target-state diagnostics. Choose the safe first diagnostic by whether it can alter a complete-policy **paired economic bound**, after its foregone accepted production and resource use, not by information entropy alone. No real trials or external contacts are authorized here.
