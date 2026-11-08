# Support commitments can constrain expansion before cash runs out

Edition 0.25, continuation from accepted edition 0.24 at `01e1ceab09ef5b083a94e1ab618a6b013dba371b`. The [support/expansion policy](../model/SUPPORT_EXPANSION.md) adds sixteen synthetic worlds to the existing monthly physical and Treasury execution. It tests **DE-CF10** without changing old engine coefficients or importing a source announcement as calibrated capacity.

A funded manufacturing order can consume cash needed to support installed robots before the new unit is useful. Conversely, refusing to order until all future resources exist today can unnecessarily delay service. The correct comparison preserves the announced plan, what actually arrives, all actor cash and every failed unit or service period. No one policy is declared universally superior.

## Current capacity and announced capacity imply different commitments

The fixed market requires 8,000 cleaning zones across eight months. Two opening robots and retained paid human capacity initially deliver less than the monthly requirement. One additional robot is requested; repeated candidate dates are opportunities to meet that finite request, not additional demand. The reference support budget grows from 25 to 60 hours in month four. Dates are zero based.

| Synthetic policy/resource world | Start month | New commissioning month | Accepted zones, eight months | Opening-cohort supported robot-months |
|---|---:|---|---:|---:|
| Funded only, actual increase occurs | 0 | 4 | 7,401.90 | 16 |
| Announced capacity plus cash reserve, increase occurs | 2 | 4 | 7,401.90 | 16 |
| Current capacity plus cash reserve, increase occurs | 4 | 6 | 7,125.43 | 16 |
| Announced increase fails to arrive | 2 | Not commissioned | 6,894.10 | 16 |
| Ample support from the beginning | 0 | 2 | 7,678.38 | 16 |

The announced policy orders early enough for the available support window, using the stated manufacturing and commissioning leads. Funded-only ordering creates earlier WIP/transit but the same accepted service and included resource cash in this particular comparison. No unpriced carrying-cost advantage is invented. Current-capacity caution loses **276.48** accepted zones relative to the announced policy. A longer manufacturing lead moves the necessary order earlier while retaining the same month-four commissioning outcome.

When the promised allocation fails, the funded unit remains in transit awaiting commissioning. The pre-change decisions and all earlier physical/cash states match the successful-announcement world. The model does not consult the future failure when approving the earlier order. Even the ample-support case does not satisfy the complete 8,000-zone service target because the opening capacity and initial ramp remain. Supported robot-months and complete customer service are different measures.

## A cash reserve protects existing service but does not finance every next step

With $40,000 opening provider cash, three-month service-fee collections and ample physical support hours, funded-only admission starts the new unit immediately. It loses two opening-cohort support months and delivers **6,149.33** zones; the new unit remains uncommissioned at the end. The two-month recurring-support reserve blocks the expansion and preserves all sixteen opening support months, delivering **6,894.10** zones. The protected **744.76** zones are actual future service, not backfilled misses. Both retain the fixed human staffing commitments and the same customer workload.

The exact initial admission boundary is **$42,730.32** provider cash. One cent less rejects the first order and shifts admission to month five. Yet crossing the threshold does not guarantee the expected month-two commissioning: the exact-boundary unit cannot pay commissioning until month five. Its two-month reserve covers a named recurring-support budget, not every future bill. The one-cent-below unit commissions in month seven. Their accepted service differs, but this is not proof that the reserve is optimal or sufficient for a real company.

A separate funded $5,000 provider loan restores one new commissioning in month three, preserves opening support and delivers **7,540.14** zones. It is fully repaid in month seven, leaving only **$32.91** provider cash at close and substantial uncollected service fees. Loan principal is not sales or extra consolidated resources. The model demonstrates dated funding and repayment, not a financing offer, safety margin or investor return.

## Cash and planned hours cannot replace qualified resources or a paying operator

A deliberately rejected first manufactured unit retains its full $36,000 manufacture cost and components. A later individually identified replacement restores the reference service; two funded starts produce one commissioned new robot. The growth request is still one. Acceptance is observed when the existing physical loop reaches its ready date; the earlier admission policy does not exploit the supplied future acceptance flag.

With only seven opening qualified components, maintenance and starts compete for the same finite stock. The case delivers **2,797.90** zones and only five opening-cohort supported robot-months. Neither a monetary reserve nor an announced engineering allocation manufactures a component. A later actual support reduction similarly lowers service even after successful commissioning. Frozen-cohort replay tests preserve each known configuration's support/software cost instead of repricing all installed units as the current release.

When the operator has no cash, an ample provider balance does not pay the operator's committed staff and site obligations. Delivered service is zero; the two legal accounts do not pool cash automatically. With zero growth requested, monthly candidate dates fund no starts and create no inventory. These cases reject two misleading shortcuts: treating aggregate capital as freely transferable, and treating a planned pipeline as qualified supported capacity.

## Decision consequences across the research program

A robotics provider should qualify the entire path from funded start to sustained customer service. A manufacturer margin, backlog, financing announcement or a purchased module is insufficient. The [commercial disclosure audit](commercial_disclosure_boundaries.md) supplies real-world questions about generation, support and actor cash; its prices and aggregate financials do not calibrate these synthetic reserve results. The [renewal work](competitive_renewals.md) separately tests customer retention and operating collections. Neither combines into an unobserved product ROI.

For the hospital pack, a new fleet cannot take support from urgent installed workflows without explicit fallback and accepted clinical service. For utility inspection, support priority must preserve required coverage, reviewer capacity and residual visits. For automotive, expansion requires components, qualified configuration, changeover/integration and continuous supported takt. Transfer these commitment and continuity questions, not the cleaning zones, per-unit hours, prices or thresholds. All three empirical recommendations remain provisional.

Substantial H remains connected through cohort-specific software obligations, human capacity, conventional planning and explicit forecasts. The simple policies use current state and an announced calendar; no LLM advantage, model-score transfer or data premium is assumed. The prior [learning/qualification worlds](learning_execution.md) preserve finite engineering and failed candidate work. This extension adds the distinct manufacture/installed-support/funding sequence, with shared identities and one Treasury.

Proceed to target measurement when contractual service, actor cash, component supply, qualification, support and contingency resources can be reconciled on one dated plan. Wait where a support increase or collection is merely announced. Reject a claim of fully financed deployment when it substitutes a recurring-support reserve for commissioning, debt and remaining obligations. These are research gates, not authorization for purchases or commercial commitments.

The bounded counterfactual catalog now spans fourteen named challenge families and 144 worlds. The result does not close empirical full-cost requirements, real rights, asset recovery, optimal fleet investment or cross-market transfer. The same active campaign continues toward **2026-11-14T20:12:27Z**. Next challenge the provisional recommendations against measured accepted service and complete retained work; add sources only when they can change a decision gate, and retain explicit unknowns where they cannot.
