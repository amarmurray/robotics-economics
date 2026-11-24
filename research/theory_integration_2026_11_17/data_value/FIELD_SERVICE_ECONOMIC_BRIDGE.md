# Original assigned service and the missing economic contrast
24 November 2026. Empirical bridge for [policy-closed data value](POLICY_CLOSED_DATA_VALUE.md), not a separate candidate contribution.

## Measured source composition: Robin

Li et al., Demonstrating Large-Scale Package Manipulation via Learned Metrics of Pick Success, arXiv:2305.10272v2 (27 June 2023), https://arxiv.org/html/2305.10272 (displayed v2, consulted 24 Nov 2026), IV-A and VI-B–D, tables I–III. Named internal stage: package singulation from conveyor to mobile sorting carrier. At fixed corpus size 394,872, 41,388 examples were replaced by observations from a broader pick-location distribution. Failures were intentionally oversampled; class balance is not field frequency. Table I compares centered versus broader training: centered evaluation AUC .755 versus .758, wider-location evaluation .802 versus .848. This supports the importance of data composition and target support, not an economic effect or a pure volume experiment.

Table II has a source consistency issue: baseline reports 89,162 total, 84,718 success, 4,444 failures (reconciles); learned experiment reports 90,127 total, 87,700 success, 3,427 failures (sum exceeds total by 1,000). The reported 96.20% agrees with the total and failure count, not the success count. Conditional on total/failures, the success fraction is 96.1976% versus baseline 95.0158%; do not repair the original counts or use exact learned success count in further estimation. Table III is a separate six-method fleet ranking comparison, not a controlled data-only intervention; e.g. TopoZ-Center 92.28%, LPR-Center 93.73% reported. No paid service, duration, complete order or downstream costs identified. Author/operator evidence, not independently reproduced. Data variation and deployed ranking are distinct comparisons.

## Original assignment denominator: Vulcan Pick

Park et al., Vulcan Pick: A Robotic System for Picking Targeted Objects from Fabric Pods (2025), https://www.amazon.science/publications/vulcan-pick-a-robotic-system-for-picking-targeted-objects-from-fabric-pods ; https://cdn.amazon.science/21/35/994901c74feaa276d363c2eb818e/vulcan-pick-a-robotic-system-for-picking-targeted-objects-from-fabric-pods.pdf ; pp.12–13 Tables I–II, sections I, VIII–IX. Parsed PDF text inspected 24 Nov; page screenshot failed due to source size. Counts cross-checked by conservation. January–March 2025 station-assigned item requests (not all originally eligible warehouse requests and not necessarily unique customer orders). Live configuration changed during deployment. No claim of independent reproduction.

|Stage|Count|
|---|---:|
|Assigned|6561|
|System failure|41|
|Band planning rejection|24|
|Band execution failure|93|
|Pick planning rejection|1246|
|Extraction attempts|5157|
|Successful extractions|4690|
|Unsuccessful extractions|467|

6561=41+24+93+1246+5157; 5157=4690+467. Attempt-conditional success 90.94%, assigned-request extraction success 71.48%. 1270 planning rejections (19.36% of assignments), 1404 never attempted. Manual routing means final fulfillment can succeed even if robotic extraction fails. Conditional on all other request paths fixed, a hypothetical intervention repairing only failed extractions adds at most 467/6561 = 7.12 percentage points; repairing only planning rejections adds at most 1270/6561 = 19.36 points, if all those requests subsequently succeed. Neither is an estimated training effect or safety authorization. The second may be limited by extra execution/congestion. A controller changing initial routing has different support; no general cap claimed.

Table II reports 4447 successes without online adaptation and 4690 with it on 5157 attempts. No evidence this is an independently randomized parallel comparison. The descriptive difference is 243/5157 per attempt or 243/6561 per assigned request (3.70 points) if membership is fixed. Online visual feedback changes within-episode control; this is NOT a data-only training intervention.

## Sharp conditional stage-to-accepted-route contrast

On n original units suppose two fixed programs have paired stage success S0,S1, counts a,b, and a *common* invariant downstream admissibility/acceptance event H with count h. Direct qualified route Yg=Sg H. Excludes alternative manual completion, program-induced H, resource displacement and continuation; these restrictions are NOT verified by either paper. j=count(S0=S1=1) is in [max(0,a+b-n),min(a,b)]. Put u=b-j (gain-only), v=a-j (loss-only). The exact interval for sum(Y1-Y0) at fixed j is

    [max(0,h-(n-u))-min(h,v), min(h,u)-max(0,h-(n-v))].

Proof: assign h ones of H to gain cells first, zero cells second, loss cells last to maximize; reverse to minimize. Remaining labels fit by construction. As j falls, u,v rise, so both extrema weakly expand. Thus unknown overlap has sharp endpoints at j=max(0,a+b-n). All counts integer; every endpoint attained. Without common H, direct-route difference bounded only by [-a,b] from Yg<=Sg. Neither bound describes total fulfilled orders with alternate routes.

Illustration treating Vulcan Table II counts as hypothetical paired marginals: n=5157,a=4447,b=4690, so j in [3980,4447], gains [243,710], losses [0,467]. If h=467 (not observed), allocating H to gain-only or loss-only at j=3980 gives +467 or -467 despite positive net technical change. If H=1 everywhere, difference is +243. If casewise monotonicity is independently established, gain lies between zero and 243 absent further H information; retaining executable old controller is not itself casewise monotonicity. Actual paired potential results are not identified by the paper. This is standard finite partial identification applied to the measured stage counts, not a field economic estimate.

If invariant incremental net contribution w>=0 per direct accepted unit and known incremental cost c, with no other effects, multiply the count endpoints by w then subtract c. No public w or c has been obtained; do not convert benchmark percentages to dollars. For real internal operations compare complete net operating contribution, avoided manual work valued with actual dated opportunity cost, quality and delivery effects, distinct future qualified service, and training/curation cost once only. A free routine-data emulator can make deliberate grounding redundant, and another body can change resource use and qualification; neither is ranked by these public numbers.

## Actual evidence requirement

Robin anchors source-composition measurement, Vulcan anchors the denominator/route bottleneck. They are separate services, not pooled arms. Pre-register fixed P/X/G/E programs on full eligible request catchments, including pre-routing exclusions, legal source lineage/readiness, certified qualification, deadlines, dated shared worker/body occupation, manual recovery outcomes and accepted final service, actual receipts or internal cost displacement, distinct successor orders and full program costs. Actual independent E staffing must be verified. Cluster by learner, buyer and shared operator interference, not isolated picks. Whole-program randomized arm means (if lawful) identify those means, not arbitrary adaptive policies or cross-world coupling. No field access, experiment or outreach. The first-paper economic contrast remains open; next obtain a direct whole-program contribution contrast or independently supported bounds. See [historical BEA numerical slice](HISTORICAL_BEA_USE_EDGE.md) separately; it is not a robot revenue estimate.
