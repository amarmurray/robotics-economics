#!/usr/bin/env python3
"""Build the decision supplement from reviewed sources and common source arithmetic."""
from pathlib import Path
import sys
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from model.research_calculations import research_summary


def build():
    result = research_summary()
    fs, tac = result['field_support'], result['tac_costs']
    distribution = fs['calculations']['FSD-CALC-04']
    retrieval = fs['calculations']['FSD-CALC-05']
    text = f'''# What the continuation evidence changes

Early campaign continuation, edition 0.2. The original 168-hour campaign remains in progress. This short supplement advances the [integrated report](REPORT.md); it does not replace its broader market map or claim a calibrated investment case. Four targeted investigations have independent source reviews. Their main contribution is to identify what must be measured or contracted before a deployment can support an economic conclusion.

The numerical source reconstruction below comes from `model/research_calculations.py`, using the saved hospital metrics and benchmark task rows. It is separate from synthetic deployment scenarios. Run `python3 scripts/build_continuation.py` to regenerate this document. No field-study or benchmark coefficient is copied into the scenario engine.

## Hospital logistics: faster transport is not a staffing result

The [hospital investigation](research/field_support_denominators.md) adds two primary studies to the six-cell program. One reports transport-phase comparisons; the other exposes the staffing around a nominally autonomous mission and an unresolved internal count discrepancy.

| Published phase comparison | Difference of group means | Relative difference from manual mean |
| --- | ---: | ---: |
| Qilu distribution | {distribution['value']:.2f} seconds lower | {100 * distribution['relative_value']:.2f}% lower |
| Qilu retrieval | {retrieval['value']:.2f} seconds lower | {100 * retrieval['relative_value']:.2f}% lower |

These means concern different transport phases and cannot simply be summed into saved paid person-time. The source's FTE and ROI claims remain author-reported because the complete calculation methods were not recovered. In Guro's medication-delivery trial, a trained safety operator accompanied the robot while staff performed loading and unloading. The paper's literal no-intervention success definition must be interpreted alongside that retained work, not used to erase it.

Guro's stated completed/eligible counts imply {fs['guro_count_implied_success_percent']:.2f}%, while the paper reports {fs['guro_reported_success_percent']:.2f}% overall success. The audit preserves both, selects neither for calibration, and retains the older ChristianaCare intervention-category discrepancy. A reconciled mission ledger would improve the evidence; silently repairing either source would not.

**Deployment implication:** define the purchased service around accepted deliveries and deadlines, then price all handling, observation, exceptions, maintenance and software/infrastructure work over the same cohort. A reduction in one travel phase can create useful capacity without removing a shift or an employee. Nonurgent transport remains a narrower proposition than nursing-work substitution.

## Utility inspection: cover the whole required visit

The [non-Spot operator follow-up](research/quadruped_operator_followup.md) adds TenneT's operator-coauthored offshore ANYmal study and a later, separate onshore pilot. The offshore work assessed 385 instruments and reported materially different coverage across rooms. The room counts are missing, so no pooled inspectability fraction is calculated. Hidden instruments, closed doors, fire rules and energized-area restrictions remained constraints after locomotion worked.

The later presentation includes a planning card selecting robot-suitable inspection points. Its financial and result fields are blank. That is evidence of the selection rule and evaluation intent, not a completed inspection count or verified cost saving. Mission-count descriptions in separate reports also have different or unspecified meanings. Later routine retention or abandonment remains unestablished.

**Customer and provider implication:** compare the entire due-inspection inventory and residual human route. Automating selected measurements can improve monitoring without eliminating a mandatory human visit. A service contractor should price review, excluded points, exceptions and maintenance decisions, and should not promise a labor saving from a supplier mission count alone. This shifts the commercial question toward complete visit substitution or valuable additional monitoring, with those outcomes accounted separately.

## Digital coordination: pay for failures and distinguish acceptance from completion

The [coordination reproducibility audit](research/coordination_reproducibility.md) reconstructs the archived TheAgentCompany run and traces pinned Open-RMF interfaces. Its benchmark arithmetic separates source populations:

| Archived source boundary | Reconstructed result |
| --- | ---: |
| Evaluated task rows | {tac['row_count']} |
| Perfect completions under the source checkpoint criterion | {tac['perfect_count']} |
| All displayed agent API-cost estimates | ${tac['all_displayed_cost_usd']:.2f} |
| Cost in non-perfect task rows | ${tac['nonperfect_displayed_cost_usd']:.2f} |
| Full-suite displayed cost / perfect completions | ${tac['suite_cost_per_perfect_usd']:.2f} |

The last ratio is not a business service price: tasks differ in value, non-perfect tasks can earn partial credit, and environment models, infrastructure, earlier omitted attempts and human work are incompletely priced. It is also not directly comparable with Astranomy's successful-episode-only mean. Failed-episode costs are required before constructing a full-attempt cost per success from that source.

The TAC run's declared model, OpenHands version and cherry-picked patch are more specific than a generic model name. A candidate configuration contains a budget field, yet archived repriced costs exceed it; the exact executed configuration and effective enforcement remain unresolved. Astranomy's public task-source pin also does not pin its inaccessible policy harness or prove a real-time physical service.

Open-RMF's source code provides a concrete integration boundary: accepting a dispatch request is not the same as assigning it or completing the physical task. A timeout does not prove that a request had no effect, and cancellation acceptance does not prove that a robot has stopped or a business transaction has been reversed. The inspected component pins are not certified as one compatible deployment.

**Architecture implication:** require persistent business/task identity, allowed-action checks, authoritative robot feedback and reconciliation of partial effects before claiming an LLM closes the enterprise-to-robot loop. First compare with a deterministic scheduler/interface. The evidence supports these integration questions; it does not establish an LLM productivity uplift.

## Learning inputs: optimize validated capability, not cheap trajectories

The [learning-data investigation](research/learning_data_economics.md) separates Cobalt's conditional cloud-cost saving from operator and whole-program costs. It preserves Cobalt's small physical-policy experiment separately from its simulation dataset. DexWild's faster human-worn collection remains a different embodiment from robot demonstrations; its target policies still require robot grounding, and its data-size and sampling-mixture results contain task-level nonmonotonic comparisons.

**R&D implication:** a collection investment needs attempted and retained data, all person-hours, processing, training, physical validation and rights, followed by held-out target performance at matched quality. Cheaper cloud computation or faster capture can improve one stage without shortening the full engineering critical path. No universal learning exponent, full-cost ratio or commercial data-factory ROI is inferred.

## Financing and the next executable step

The [treasury extension proposal](model/treasury_extension_design.md) sets out how to replace exogenous funding envelopes with dated cash, obligations, financing and shared entrant deployment. The [independent design challenge](reviews/treasury_design_review.md) tests reservation settlement and event-phase timing. The shared monthly enterprise implementation now joins physical cohorts, commercial contracts, assigned demand, paid human capacity and cash. Annual digital paths and intelligence architectures still require explicit unit/cohort/cost bridges; scheduled debt/default/recovery and acquisition transitions remain unfinished. The [active decision campaign](DEPLOYMENT_ENTRY_CAMPAIGN.md) pursues those mechanisms without treating synthetic assumptions as observed terms.

The immediate next question is whether one chosen service can combine accepted output, complete support, a sufficiently durable customer contract and actual cash survival. The new evidence narrows how to test that proposition. It does not justify bypassing it with an attractive benchmark, a large fleet announcement or a synthetic terminal-stock result.

Independent reviews: [hospital](reviews/field_support_review.md), [quadruped](reviews/quadruped_followup_review.md), [coordination](reviews/coordination_review.md), and [learning data](reviews/learning_data_review.md). See the [acceptance audit](ACCEPTANCE_AUDIT.md) and [roadmap](RESEARCH_ROADMAP.md) for remaining requirements and bounded next actions.
'''
    (ROOT / 'CONTINUATION_FINDINGS.md').write_text(text)
    print('Wrote CONTINUATION_FINDINGS.md:', len(text.split()), 'words')


if __name__ == '__main__':
    build()
