#!/usr/bin/env python3
"""Build a decision chapter from the exact inspected simulation export."""
import json
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from model.inspection_uncertainty import source_hashes

def money(n):
    return f'${n / 100:,.2f}'

def build():
    d=json.loads((ROOT/'model/results/inspection_uncertainty.json').read_text())
    if d['source_sha256']!=source_hashes():
        raise ValueError('Regenerate the uncertainty export before building its report')
    out=['''# Evidence that changes the inspection decision

Edition 0.54 · 11 November 2026 · same November 14 campaign deadline.

**A joined service-and-paid-work packet changes the decision; isolated favorable facts can leave it unresolved.** We extend the utility pack because it already has a common-service execution and separate payer ledger. The hospital and automotive cases keep their own minimum-evidence requirements; none of the numbers below transfers to them.

The new [reproducible sensitivity model](../model/INSPECTION_UNCERTAINTY.md) uses the existing human, fixed-sensor and mobile-sensor policies. It evaluates 96 explicit possibilities, 288 policy executions and all 63 nonempty evidence-field subsets. These are sensitivity evaluations, not 96 empirical deployments or independent new challenge worlds. All prior 271 bounded worlds remain unchanged. No source price, productivity claim, repair probability or employment total calibrates this experiment. The [inputs and provenance](../model/inspection_uncertainty_inputs.json), [complete results](../model/results/inspection_uncertainty.json) and [interactive local explorer](../dashboard/inspection_uncertainty.html) are reviewable.

## What the public evidence adds

The [new municipal audit](quadruped_operator_followup.md#software-renewals-and-contract-discretion-edition-054) adds QOF-E32–E35: a separate software authorization and proposed recurring charge in Augusta, and reported project progress/renewal discretion followed by another authorization in Mount Dora. These refine U2/U3/U6 record requirements. They do not supply an executed current contract, paid invoice, complete accepted-service cohort or payroll change. Historical source statements and their evidential stages remain separate from simulated outcomes.

The subsequent [configured-offer audit](quadruped_operator_followup.md#configured-offer-and-continuing-obligations-edition-055), QOF-E36–E38, identifies additional authorization history and concrete warranty/cost exclusions. This strengthens the U2/U6 packet specification without changing a simulation input, interpreting an executed contract or claiming an actual payment.

The edition 0.53 [twenty-row matrix](deployment_evidence_sequence.md) is preserved as a dated acceptance specification. Its package hashes still refer to that historical input. New source mappings supplement it; no row is marked empirically complete. A target's U1–U3 record must identify due measurements, qualification, timing, applicable rights and acceptance; U5/U6 then establish paid commitments and the complete payer boundary. U4 is additionally required for downstream maintenance benefits.

## Quantified decision uncertainty

Six finite axes are assumptions: retained or avoidable paid visits; presence/absence of a separate field duty; complete fixed qualification or one missing measurement; complete mobile readings, one failed review or capture after cutoff; review capacity 23/24 person-minutes; service deadline 100/180 minutes. These bracket structural and exact fixture thresholds, not estimated confidence intervals. Every candidate in a state faces the same due service. No probabilities are assigned.

The rule chooses the policy with the smallest worst cash regret among those feasible across all compatible possibilities. Regret is the difference from the best feasible option if that state's facts were already known. A hard service failure is excluded, not priced as a cheap failure. The human comparator remains funded and complete throughout this specific domain.

| Perfect evidence known before choosing | Worst customer regret left | Worst consolidated regret left |
| --- | ---: | ---: |
''']
    packets=[('No fields (also any single field or pair)',[]),('Physical duty + fixed qualification + review capacity',['field_duty','fixed_fit','review_capacity']),('Also mobile quality/timeliness',['field_duty','fixed_fit','mobile_fit','review_capacity']),('Also paid staffing contract',['staffing','field_duty','fixed_fit','mobile_fit','review_capacity'])]
    for label,keys in packets:
        values=[]
        for o in d['decisions'].values():
            values.append(o['before_evidence']['worst_regret_cents'] if not keys else next(x['worst_remaining_regret_cents'] for x in o['evidence_partitions'] if set(x['revealed_axes'])==set(keys)))
        out.append(f'| {label} | {money(values[0])} | {money(values[1])} |\n')
    out.append('''
This demonstrates complementarity: cheaper equipment or a faster capture alone does not resolve the whole service/cash choice. It does **not** imply that single records have no value. A resolved branch can change feasibility, narrow the scope or reject a claim even when another branch retains the same worst regret. Nor is zero regret in this finite model zero real-world uncertainty. The five-field packet leaves the deadline unresolved because its branch decisions avoid the late-fallback dependence; real operators must still specify a deadline.

Without resolving fields, only the human policy is feasible across this entire domain. Fixed sensing fails complete service in 42 possibilities and mobile sensing in 44; these counts are not failure probabilities. Even assuming deadline 180 everywhere makes all three feasible but does not change the customer minimax choice: the fixed policy's worst cash regret is $1,060 versus $940 for human. Resolving fixed qualification and review as well changes the customer minimax choice to fixed with $340 worst regret. The answer depends on the declared domain and policy set.

With avoidable visit payment, no field duty, complete fixed qualification and sufficient review established, fixed sensing has zero regret across the remaining declared possibilities. If only the mobile service is established complete under the same staffing/duty/review conditions, mobile is the robust choice while fixed fit is unresolved, with $220 customer regret if fixed later proves qualified. Thus the next qualified alternative is economically relevant even after the robot works.

## Full cost and the next bill

In the complete, avoidable-visit, no-field-duty illustration, the four-window payer ledger is:

| Policy | Customer cash | Provider external resources | Provider net cash change | Consolidated external resources |
| --- | ---: | ---: | ---: | ---: |
''')
    good=next(s for s in d['states'] if s['state']==dict(staffing='per_visit',field_duty=False,fixed_fit='complete',mobile_fit='complete',review_capacity=24,deadline_minute=180))
    for p,v in good['policies'].items():
        c=v['cash'];out.append('| '+p+' | '+' | '.join(money(c[k]) for k in ('customer_outlay_cents','provider_resource_cash_cents','provider_cash_change_cents','consolidated_resource_cash_cents'))+' |\n')
    out.append('''
Compared with human, the fixed policy leaves $940 customer and $1,016 consolidated room for *incremental omitted net costs*; mobile leaves $720 and $882. Compared with qualified fixed sensing, mobile instead needs $220 customer or $134 consolidated incremental net benefit/cost reduction. Fees cancel inside the two-party perimeter; the supplier's retained cash explains the difference. These figures are exact conditional budget limits, not observed savings or full-lifecycle ROI.

The residual includes actual acquisition/replacement and terminal value, integration, qualification, software renewal, repair/continuity, tax/finance and downstream work beyond the recorded bills, net of the matched baseline and any proven benefit. These amounts are unknown, not zero. One must not add supplier fees and the same supplier resources twice. Benefits from better maintenance are not estimated. A benefit claim needs accepted findings joined to changed decisions, completed work and a credible counterfactual.

Timing can bind before aggregate resources: fixed has only $34 of extra initial provider-resource headroom and mobile $78 at the inherited fee schedule and opening cash. At one cent above each boundary, the first monitoring booking fails even though human fallback still completes all four windows. Four full Treasury replays verify these switches. Supplier terminal cash of $76 or $162 is therefore not an upfront repair budget. Actual maintenance bills and operating/support terms must be joined to timing; this does not recommend a price or funding transaction.

## What to acquire next

Start with the utility U1/U3 join: exact due property and all residual field duties, fixed/mobile measurement qualification, complete failed and successful reviews, acceptance times and available funded fallback. Collect U5 paid-contract terms concurrently; released minutes are insufficient. Obtain U2 executed applicable rights and support/renewal conditions, and U6 actual payer cash/resources, with the historical authorization traces kept separate. The source records identify official municipal records as a permitted route, but no outreach is initiated and no private records are presumed available.

For hospital, the analogous evidence is complete due deliveries and urgency/custody, escort/fallback/receiving duties, support entitlement and actual staffing/cash. For automotive it is the complete part/handoff/takt contract, preparation/quality/recovery duties, supported generation and actual paid obligations. Each retains its own acceptance owner and comparator. Their model parameters are not derived from utility thresholds.

Perfect information was assumed costless for the sensitivity exercise. Acquisition effort, noise and delay remain unpriced; the regret reductions are neither expected value of information nor willingness to pay. Real uncertainty cannot be eliminated by choosing the favorable branch in the explorer. The remaining empirical dependency is an applicable joined packet. The new result narrows its priority and rejection conditions without claiming that simulation supplied it.
''')
    return ''.join(out)

if __name__=='__main__':
    p=ROOT/'research/inspection_uncertainty.md';p.write_text(build());print(p)
