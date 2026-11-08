#!/usr/bin/env python3
"""Assemble report from authoritative research chapters; no independent calculations."""
from pathlib import Path
import csv
import hashlib
import json
import re
ROOT = Path(__file__).resolve().parents[1]
CHAPTERS = [
 ('Executive argument and strategic implications','integrated_decisions.md'),
 ('Economic atlas and deployment pathways','economic_atlas.md'),
 ('Capabilities, learning and physical-digital coordination','capability_learning.md'),
 ('Customer formation, adoption and provider value capture','customer_value.md'),
 ('Digital-AI ecosystem, benchmarks and direct contributions','digital_ecosystem.md'),
 ('Digital infrastructure and physical production','digital_infrastructure.md'),
 ('Physical supply, embodiments, quadrupeds and drones','physical_supply_field.md'),
 ('Frontier robotics models, deployment and value capture','frontier_models.md'),
]
FOLLOWUPS = {
 'integrated_decisions.md': [('Deployment and entry decision packs', 'deployment_entry_decisions.md')],
 'frontier_models.md': [('Generalist, Dyna and customer service economics', 'generalist_dyna_deployment.md'), ('Regional model releases, rights and operating evidence', 'regional_frontier_models.md'), ('Conditional architecture resources and value allocation', 'intelligence_architecture_scenarios.md'), ('Funded intelligence roles and monthly qualification', 'monthly_intelligence_execution.md')],
 'economic_atlas.md': [('Physical requirements and employment classifications', 'physical_requirements_crosswalk.md')],
 'capability_learning.md': [('Learning-data economics and validation boundaries', 'learning_data_economics.md'), ('Automotive workcells, buffering and qualified generation', 'automotive_workcell_decision.md')],
 'customer_value.md': [('Hospital service, support and economic denominators', 'field_support_denominators.md'), ('Monthly commercial funding and title', 'monthly_commercial_finance.md'), ('A shared entrant market and funded execution', 'shared_enterprise_finance.md'), ('Dated finance, service continuity and cash recovery', 'financed_execution.md'), ('Digital paths, cohorts and the operating calendar', 'calendar_digital_execution.md'), ('Funded acquisition, inherited obligations and hybrid entry', 'entry_transitions.md'), ('Operating rollout, contract value and provider funding', 'commercial_disclosure_boundaries.md'), ('Funded renewals and the entry cash window', 'competitive_renewals.md'), ('Installed support and finite expansion commitments', 'support_expansion.md'), ('Hospital support, repair and replacement obligations', 'hospital_support_contracts.md'), ('Funded asset recovery and restored service', 'asset_recovery.md')],
 'digital_ecosystem.md': [('Benchmark reproducibility and transaction authority', 'coordination_reproducibility.md'), ('Annual digital scenarios and the moving adoption comparison', 'annual_digital_scenarios.md'), ('Competent conventional coordination and mandatory service', 'conventional_coordination.md'), ('R&D progress, qualification and supported capacity', 'learning_qualification.md'), ('Funded learning, physical qualification and supported service', 'learning_execution.md')],
 'physical_supply_field.md': [('Non-Spot operator evidence and retained-deployment limits', 'quadruped_operator_followup.md'), ('Utility inspection, fixed sensing and residual visits', 'utility_inspection_decision.md')],
 'digital_infrastructure.md': [('Onboard workload qualification and operating deadlines', 'onboard_workload_qualification.md')],
}
def chapter(text, depth=1):
    lines=text.splitlines()
    # Remove chapter title, then nest its remaining headings below report chapter.
    if lines and lines[0].startswith('# '): lines=lines[1:]
    lines=[('#'*depth+x if x.startswith('#') else x) for x in lines]
    s='\n'.join(lines).strip()
    s=s.replace('(../data/','(data/').replace('(../model/','(model/').replace('(../reviews/','(reviews/').replace('(../RESEARCH_', '(RESEARCH_').replace('(../DEPLOYMENT_', '(DEPLOYMENT_')
    for path in (ROOT/'research').glob('*.md'):
        s=s.replace('('+path.name+'#','(research/'+path.name+'#')
        s=s.replace('('+path.name+')','(research/'+path.name+')')
    return s

def build():
    sources=CHAPTERS+[item for items in FOLLOWUPS.values() for item in items]
    missing=[name for _,name in sources if not (ROOT/'research'/name).exists()]
    if missing:raise SystemExit('Missing substantive chapters: '+', '.join(missing))
    out=['''# Robotics Economics — integrated research report

Edition 0.29, supplier-contract and financing-denominator checkpoint of the Deployment and Entry Decision campaign, 8 November 2026. A primary-source challenge separates physical recovery, company acquisition, usable contracts and supported service. Original financing illustrations remain unreconciled and uncalibrated. All fourteen bounded challenge families / 158 worlds retain their numerical results. Empirical full-service economics and broader annual-resource integration remain incomplete. This is **an early checkpoint of the same active 168-hour campaign, not completion**.

Launch input: `campaign launch snapshot (see ignored sync_receipt.json)`. Historical evidence keeps its recorded retrieval date; the Generalist/Dyna and restaurant-workflow continuations were retrieved on 7 November 2026. The decision review also retrieved its two adverse sources on 7 November. The inspection continuation retrieved three additional public source records on 7 November; public-summary-only and research-plan boundaries remain explicit. The automotive follow-up retrieved three primary source records on 7 November, preserving different plants/tasks, supplier-versus-operator status and inconsistent pilot chronology. Its physical and funding mechanisms remain synthetic. The R&D follow-up reviewed four sources across 7–8 November, with final source records dated 8 November. Its proceedings PDF and readiness-code fingerprints are recorded; undated mutable documentation is not assigned a fabricated release day. Source observation periods and publication dates remain distinct. This report is generated from authoritative chapters in `research/` by `python3 scripts/build_report.py`; numerical tables consume source-hashed exports from the documented model modules.

The original campaign ran from 2026-10-25T15:52:14Z to 2026-11-01T15:52:14Z and ended incomplete. The user has now activated a new 168-hour objective. Its single recorded execution T0 is 2026-11-07T20:12:27Z and deadline is 2026-11-14T20:12:27Z; the native activation timestamp is not exposed. See [the active campaign contract](DEPLOYMENT_ENTRY_CAMPAIGN.md). No work during interruptions or uninterrupted-compute claim is implied.

The report uses a US quantitative labor anchor with global provider, research and supply evidence. Synthetic scenario outputs explore mechanisms; they are not empirical market forecasts, measured ROI or estimates of payroll actually removed. The hospital, quadruped, benchmark/coordination, learning-data and onboard-workload follow-ups are integrated into the relevant chapters below. The [reproduction instructions](REPRODUCE.md), [acceptance audit](ACCEPTANCE_AUDIT.md), [requirement register](acceptance_register.json) and [continuing roadmap](RESEARCH_ROADMAP.md) support this report. The local dashboard entry is `python3 scripts/serve.py`.

Begin with the executive argument for the decision logic, then use the economic atlas to orient the technical, organizational and supply evidence. The common-engine section connects those findings to conditional scenarios. Detailed source locators, explicit conflicts and unknowns remain in the chapters and their machine-readable evidence packages; no favorable headline substitutes for their operating boundary. This expanded edition deliberately retains the full source analysis rather than compressing it into a short investment thesis.

The historical launch requested several specialist agents. The latest user instruction limits continuation to one agent. The annual-path implementation and checks below were performed by the sole lead; no new independent reviewer or independently verified serving-model identity is claimed.

The initial editions were produced in a cloud checkout. The local continuation began in the canonical Mac checkout and moved to a verified execution clone during iCloud stalls. The canonical folder remains preserved and unreconciled. That earlier cloud transfer was unconfirmed. After edition 0.11, the user authorized one new cloud execution chat because the old executor could not be reattached. This continuation executes in the published robotics-economics cloud environment after fresh shell, repository, byte-hash, test and dashboard checks. The original chats and canonical Mac checkout remain preserved; no continuous execution between sessions is claimed. The unpublished annual-path and physical-crosswalk edits described in the supplied cloud handoff were unavailable here. The annual mechanism was implemented from the accepted design, preserving the local regression fixture. The crosswalk was newly extracted from the original BLS workbooks; unavailable cloud code or tests are not claimed as recovered. Publication to the private repository does not establish consumption by a separate Work session.
''']
    contents=[]
    headings=[f'{i}. {title}' for i,(title,_) in enumerate(CHAPTERS,1)]+[
        '9. Common-engine scenarios and interpretation',
        '10. Local experiments: cash settlement and transaction state',
        '11. What remains unresolved',
    ]
    for heading in headings:
        anchor=re.sub(r'[^a-z0-9 -]', '', heading.lower()).replace(' ', '-')
        contents.append(f'- [{heading}](#{anchor})')
    out.append('## Contents\n\n'+'\n'.join(contents))
    for i,(title,name) in enumerate(CHAPTERS,1):
        out.append(f'## {i}. {title}\n\nAuthoritative chapter: [research/{name}](research/{name}).\n\n'+chapter((ROOT/'research'/name).read_text()))
        for follow_title,follow_name in FOLLOWUPS.get(name,[]):
            out.append(f'### Focused follow-up: {follow_title}\n\nAuthoritative analysis: [research/{follow_name}](research/{follow_name}).\n\n'+chapter((ROOT/'research'/follow_name).read_text(),depth=2))
    research=json.loads((ROOT/'model/results/observed_research_summary.json').read_text())
    if hashlib.sha256((ROOT/'model/research_calculations.py').read_bytes()).hexdigest()!=research['calculation_code_sha256']:
        raise SystemExit('Stale research calculation code')
    for name,digest in research['source_snapshot_sha256'].items():
        if hashlib.sha256((ROOT/'data'/name).read_bytes()).hexdigest()!=digest:
            raise SystemExit('Stale research source: '+name)
    disclosure=research['commercial_disclosures']
    disclosure_table=['| Reproduced disclosure arithmetic | USD | Equation | Scope |','| --- | ---: | --- | --- |']
    for row in disclosure['calculations'].values():
        disclosure_table.append(f"| {row['label']} | {row['value']:,.0f} | {row['formula']} | {row['scope']} |")
    financial_table=['| Agility standalone period | Net sales | COGS | Gross result | Net result | Operating cash flow |','| --- | ---: | ---: | ---: | ---: | ---: |']
    for row in disclosure['financial_periods']:
        financial_table.append('| '+row['period']+' | '+' | '.join(f"{row[k]:,}" for k in ['net_sales','cost_of_goods_sold','gross_result','net_result','operating_cash_flow'])+' |')
    insert_at=next(i for i,text in enumerate(out) if text.startswith('### Focused follow-up: Operating rollout'))+1
    out.insert(insert_at,'#### Reproduced disclosure components and company accounts\n\n'+'\n'.join(disclosure_table)+'\n\nAll amounts are USD; the first three rows use five-year management assumptions. Approximate slide headlines may differ from component arithmetic. These are not executed customer terms or whole-system returns.\n\n'+'\n'.join(financial_table)+'\n\nNegative figures are losses or cash outflows. Periods are unequal and are not annualized. Generated from [observed_research_summary.json](model/results/observed_research_summary.json), source FG-E021 (prospectus pp.132–133 and standalone statements F-47/F-49/F-73/F-75) and FG-E022 (post-close gross funding). Site rate, payroll removal, ROI/payback, net closing cash and runway remain unknown. Source identifiers, equations and hashes accompany the export.')
    rights=research['recovery_contracts']
    rights_table=['| Source currency | Displayed hourly amount | Displayed monthly payment | Planned hours/month | Monthly payment / planned hours | Illustrated monthly components over term |','| --- | ---: | ---: | ---: | ---: | ---: |']
    for row in rights['rows']:
        rights_table.append(f"| {row['currency']} | {row['headline_hourly']:,.2f} | {row['monthly_payment']:,.2f} | {row['planned_hours_per_month']:g} | {row['implied_payment_per_planned_hour']:,.5f} | {row['undiscounted_payment_components']:,.2f} |")
    at=next(i for i,t in enumerate(out) if t.startswith('### Focused follow-up: Funded asset recovery and restored service'))+1
    out.insert(at,'#### Reproduced financing-denominator audit\n\n'+'\n'.join(rights_table)+'\n\nSource FG-E030; the illustrated duration is 48 months. '+rights['boundary']+' Source identity, equations and input IDs are preserved in [observed_research_summary.json](model/results/observed_research_summary.json).')
    workcell=json.loads((ROOT/'model/results/automotive_workcell.json').read_text())
    for case in workcell['cases'].values():
        for path,digest in case['source_sha256'].items():
            if hashlib.sha256((ROOT/path).read_bytes()).hexdigest()!=digest:raise SystemExit('Stale automotive dependency: '+path)
    workcell_table=['| Synthetic workcell | On-time kits | Late | Undelivered | Busy ticks | Retained staff, USD | Operator outlay, USD |', '| --- | ---: | ---: | ---: | ---: | ---: | ---: |']
    for row in workcell['summary']:
        workcell_table.append(f"| {row['case']} | {row['on_time_kits']} | {row['late_kits']} | {row['undelivered_kits']} | {row['manipulator_busy_ticks']} | {row['paid_staff_cents']/100:,.2f} | {row['operator_outlay_cents']/100:,.2f} |")
    insert_at=next(i for i,text in enumerate(out) if text.startswith('### Focused follow-up: Automotive workcells'))+1
    out.insert(insert_at,'#### Reproduced automotive-workcell worlds\n\n'+'\n'.join(workcell_table)+'\n\nGenerated from [automotive_workcell.json](model/results/automotive_workcell.json). Every kit requires three unique components by its deadline. Picking and loading share one manipulator. Source rates do not calibrate these synthetic ticks. Opening assets, transport and lifecycle costs are excluded; compare matched complete service before cash.')
    inspection=json.loads((ROOT/'model/results/utility_inspection.json').read_text())
    for case in inspection['cases'].values():
        for path,digest in case['source_sha256'].items():
            if hashlib.sha256((ROOT/path).read_bytes()).hexdigest()!=digest:raise SystemExit('Stale inspection dependency: '+path)
    inspection_table=['| Synthetic inspection world | Complete windows | Human visits | Paid field crew, USD | Operator outlay, USD | External resource cash, USD |', '| --- | ---: | ---: | ---: | ---: | ---: |']
    for row in inspection['summary']:
        inspection_table.append(f"| {row['case']} | {row['complete_service_windows']} | {row['visits_completed']} | {row['paid_field_crew_cents']/100:,.2f} | {row['operator_outlay_cents']/100:,.2f} | {row['external_resource_cash_cents']/100:,.2f} |")
    insert_at=next(i for i,text in enumerate(out) if text.startswith('### Focused follow-up: Utility inspection'))+1
    out.insert(insert_at,'#### Reproduced inspection-window worlds\n\n'+'\n'.join(inspection_table)+'\n\nGenerated from [utility_inspection.json](model/results/utility_inspection.json). Compare matched complete service before cash. The field-duty row has a matching human field-duty comparator. Fees cancel at the operator/provider perimeter; external resource bills and retained commitments remain. No lifecycle ROI or avoided-outage value is inferred.')
    monthly = json.loads((ROOT/'model/results/monthly_commercial.json').read_text())
    for path, digest in monthly['source_sha256'].items():
        if hashlib.sha256((ROOT/path).read_bytes()).hexdigest() != digest:
            raise SystemExit('Stale monthly-commercial dependency: '+path)
    monthly_table = ['| Synthetic witness | Accepted service units, five months | Physical vendor outlay, USD | Unpaid invoices, USD | Refund liabilities, USD |',
                     '| --- | ---: | ---: | ---: | ---: |']
    for row in monthly['summary']:
        q=row['total_accepted_output']; quantity=q['numerator']/q['denominator']
        monthly_table.append(f"| {row['case'].replace('_',' ')} | {quantity:,.2f} | {row['external_physical_outlay_cents']/100:,.2f} | {row['outstanding_invoices_cents']/100:,.2f} | {row['outstanding_refunds_cents']/100:,.2f} |")
    insert_at=next(i for i,text in enumerate(out) if text.startswith('### Focused follow-up: Monthly commercial'))+1
    out.insert(insert_at, '#### Reproduced monthly commercial witnesses\n\n'+'\n'.join(monthly_table)+'\n\nGenerated from [monthly_commercial.json](model/results/monthly_commercial.json). Each row is a separate alternative world. Unpaid invoices include future-eligible receivables as well as arrears; inspect the ledger for due dates. Refund liabilities are not revenue. Physical vendor outlays are a bounded cash proxy, not full lifecycle cost. These synthetic terms do not calibrate the annual, entrant or K architecture models.')
    shared=json.loads((ROOT/'model/results/shared_enterprise.json').read_text())
    bridge=json.loads((ROOT/'model/results/enterprise_funding_bridge.json').read_text())
    for artifact in (shared,bridge):
        for path,digest in artifact['source_sha256'].items():
            if hashlib.sha256((ROOT/path).read_bytes()).hexdigest()!=digest:
                raise SystemExit('Stale shared-enterprise dependency: '+path)
    shared_table=['| Synthetic world | Market units, 8 months | Entrant units | Entrant installed robots | Closing entrant cash, USD | Due unpaid, USD | Added equity, USD |',
                  '| --- | ---: | ---: | ---: | ---: | ---: | ---: |']
    for row in shared['summary']:
        total=row['total_market_delivered_units'];entry=row['entrant_delivered_units']
        shared_table.append(f"| {row['case'].replace('_',' ')} | {total['numerator']/total['denominator']:,.2f} | {entry['numerator']/entry['denominator']:,.2f} | {row['entrant_installed_robots']} | {row['entrant_closing_cash_cents']/100:,.2f} | {row['entrant_closing_due_unpaid_cents']/100:,.2f} | {row['equity_received_cents']/100:,.2f} |")
    insert_at=next(i for i,text in enumerate(out) if text.startswith('### Focused follow-up: A shared entrant'))+1
    out.insert(insert_at,'#### Reproduced shared-market worlds\n\n'+'\n'.join(shared_table)+f"\n\nGenerated from [shared_enterprise.json](model/results/shared_enterprise.json). Rows are mutually exclusive worlds, not additive markets. Human and robot work reconcile in one accepted-bundle unit. The separate [fixed-policy funding search](model/results/enterprise_funding_bridge.json) finds {bridge['minimum_extra_upfront_equity_cents']/100:,.2f} USD of additional upfront equity over {bridge['opening_entrant_cash_cents']/100:,.2f} USD opening entrant cash; one cent less fails. These are synthetic cash-execution results, not profit, valuation, capital access or empirical penetration estimates.")
    financed=json.loads((ROOT/'model/results/enterprise_finance.json').read_text())
    for path,digest in financed['source_sha256'].items():
        if hashlib.sha256((ROOT/path).read_bytes()).hexdigest()!=digest:
            raise SystemExit('Stale financed-enterprise dependency: '+path)
    finance_table=['| Synthetic financed world | Entrant bundles, 8 months | First debt default month | Principal recovered, USD | Principal still owed, USD | Interest still owed, USD | Starts |',
                   '| --- | ---: | ---: | ---: | ---: | ---: | ---: |']
    for row in financed['summary']:
        q=row['entrant_delivered_units'];default=row['first_debt_default_month']
        finance_table.append(f"| {row['case'].replace('_',' ')} | {q['numerator']/q['denominator']:,.2f} | {'None' if default is None else default} | {row['principal_recovered_cents']/100:,.2f} | {row['principal_outstanding_cents']/100:,.2f} | {row['interest_outstanding_cents']/100:,.2f} | {row['total_started_robots']} |")
    insert_at=next(i for i,text in enumerate(out) if text.startswith('### Focused follow-up: Dated finance'))+1
    out.insert(insert_at,'#### Reproduced financed-execution worlds\n\n'+'\n'.join(finance_table)+'\n\nGenerated from [enterprise_finance.json](model/results/enterprise_finance.json). These are mutually exclusive worlds in the same synthetic floor-service unit, not additive activity or empirically calibrated decision packs. No debt default does not ensure funded support. Cash recovery preserves remaining claims and does not sell assets. Fourteen worlds implement bounded DE-CF11/12 mechanisms; they do not satisfy the campaign requirement for broad counterfactual coverage.')
    calendar=json.loads((ROOT/'model/results/calendar_bridge.json').read_text())
    for path,digest in calendar['source_sha256'].items():
        if hashlib.sha256((ROOT/path).read_bytes()).hexdigest()!=digest:
            raise SystemExit('Stale calendar-bridge dependency: '+path)
    calendar_table=['| Synthetic calendar world | Accepted zones, 8 months | Retained human task hours | Staffing committed, USD | External physical/operating cash outlays, USD | Supported robot-months | Qualified upgrades |',
                    '| --- | ---: | ---: | ---: | ---: | ---: | ---: |']
    for row in calendar['summary']:
        q=row['accepted_cleaning_zones'];h=row['retained_human_task_hours']
        calendar_table.append(f"| {row['case'].replace('_',' ')} | {int(q['numerator'])/int(q['denominator']):,.2f} | {int(h['numerator'])/int(h['denominator']):,.2f} | {row['staff_commitment_cents']/100:,.2f} | {row['external_physical_and_enterprise_cash_cents']/100:,.2f} | {row['supported_robot_months']} | {row['upgrade_count']} |")
    insert_at=next(i for i,text in enumerate(out) if text.startswith('### Focused follow-up: Digital paths, cohorts'))+1
    out.insert(insert_at,'#### Reproduced calendar and cohort worlds\n\n'+'\n'.join(calendar_table)+'\n\nGenerated from [calendar_bridge.json](model/results/calendar_bridge.json). The four C00/C01/C10/C11 branches share a paid-staff/customer-move policy and ample capital. Cash outlays include actual starts and retained inventory; opening assets predate the cash window. They are not lifecycle costs or an optimal investment ranking. Partial years are aggregated without extrapolation; no historical floor-bundle conversion or extra annual fleet is assumed.')
    monthly_arch=json.loads((ROOT/'model/results/monthly_architectures.json').read_text())
    for path,digest in monthly_arch['source_sha256'].items():
        if hashlib.sha256((ROOT/path).read_bytes()).hexdigest()!=digest:
            raise SystemExit('Stale monthly-architecture dependency: '+path)
    role_table=['| Synthetic architecture world | Accepted zones | Robot zones | Paid staffing, USD | Supported robot-months | Qualified units | Paid external bills, USD |',
                '| --- | ---: | ---: | ---: | ---: | ---: | ---: |']
    for row in monthly_arch['summary']:
        q=row['accepted_zones'];robot=row['robot_zones']
        role_table.append(f"| {row['case'].replace('_',' ')} | {int(q['numerator'])/int(q['denominator']):,.2f} | {int(robot['numerator'])/int(robot['denominator']):,.2f} | {row['staff_cash_paid_cents']/100:,.2f} | {row['supported_robot_months']} | {row['qualified_units']} | {row['external_physical_and_enterprise_cash_cents']/100:,.2f} |")
    insert_at=next(i for i,text in enumerate(out) if text.startswith('### Focused follow-up: Funded intelligence roles'))+1
    out.insert(insert_at,'#### Reproduced funded architecture worlds\n\n'+'\n'.join(role_table)+'\n\nGenerated from [monthly_architectures.json](model/results/monthly_architectures.json). One active synthetic cleaning-service business retains the same demand and paid staffing. Opening hardware predates the cash window; some worlds never start production or retain unqualified assets. Lower cash expenditure is not an investment ranking. Model resources replace the opaque digital bundle, and fees cancel at the complete legal-entity boundary.')
    coordination=json.loads((ROOT/'model/results/conventional_coordination.json').read_text())
    for case in coordination['cases'].values():
        for path,digest in case['source_sha256'].items():
            if hashlib.sha256((ROOT/path).read_bytes()).hexdigest()!=digest:
                raise SystemExit('Stale conventional-coordination dependency: '+path)
    coordination_table=['| Synthetic service-window world | Accepted requests | Mandatory accepted | Failed attempts | Paid window resources, USD | Paid staff, USD |',
                        '| --- | ---: | ---: | ---: | ---: | ---: |']
    for row in coordination['summary']:
        coordination_table.append(f"| {row['case'].replace('_',' ')} | {row['accepted']} | {row['mandatory_accepted']} / {row['mandatory_requested']} | {row['failed_attempts']} | {row['paid_resource_cents']/100:,.2f} | {row['paid_staff_cents']/100:,.2f} |")
    insert_at=next(i for i,text in enumerate(out) if text.startswith('### Focused follow-up: Competent conventional coordination'))+1
    out.insert(insert_at,'#### Reproduced observed-queue coordination worlds\n\n'+'\n'.join(coordination_table)+'\n\nGenerated from [conventional_coordination.json](model/results/conventional_coordination.json). Exactness covers the currently observed bounded queue. Mandatory service remains a separate gate; all paid attempt, recovery and capacity costs remain. These synthetic window bills exclude lifecycle economics, and no LLM performance is measured.')
    entry=json.loads((ROOT/'model/results/entry_transitions.json').read_text())
    for path,digest in entry['source_sha256'].items():
        if hashlib.sha256((ROOT/path).read_bytes()).hexdigest()!=digest:
            raise SystemExit('Stale entry-transition dependency: '+path)
    entry_table=['| Synthetic entry world | Closing | Accepted zones | Paid share price, USD | Target equity, USD | Buyer closing cash, USD | Paid staffing, USD |',
                 '| --- | --- | ---: | ---: | ---: | ---: | ---: |']
    for row in entry['summary']:
        q=row['accepted_zones']
        entry_table.append(f"| {row['case'].replace('_',' ')} | {row['close_status']} | {int(q['numerator'])/int(q['denominator']):,.2f} | {row['paid_share_price_cents']/100:,.2f} | {row['paid_target_equity_cents']/100:,.2f} | {row['buyer_closing_cents']/100:,.2f} | {row['paid_staff_cents']/100:,.2f} |")
    insert_at=next(i for i,text in enumerate(out) if text.startswith('### Focused follow-up: Funded acquisition, inherited obligations'))+1
    out.insert(insert_at,'#### Reproduced funded entry worlds\n\n'+'\n'.join(entry_table)+'\n\nGenerated from [entry_transitions.json](model/results/entry_transitions.json). Purchase consideration goes to the seller; target working capital and separate growth need actual settled equity. The company retains its liabilities, assets and customers. Share transfers cancel at the fixed wider boundary, and terminal equity value remains unknown; these cash figures are not ROI or an investment ranking.')
    renewals=json.loads((ROOT/'model/results/competitive_renewals.json').read_text())
    for path,digest in renewals['source_sha256'].items():
        if hashlib.sha256((ROOT/path).read_bytes()).hexdigest()!=digest:raise SystemExit('Stale competitive-renewal dependency: '+path)
    renewal_table=['| Synthetic renewal world | Entrant accepted zones | First cash crossing, month | Maintained through horizon from month | Terminal operating cash after recorded bills, USD |', '| --- | ---: | --- | --- | ---: |']
    for row in renewals['summary']:
        q=row['entrant_delivered_zones'];first=row['entrant_first_cash_break_even_month'];held=row['entrant_cash_break_even_held_through_horizon_month']
        renewal_table.append(f"| {row['case'].replace('_',' ')} | {int(q['numerator'])/int(q['denominator']):,.2f} | {first if first is not None else 'Not observed'} | {held if held is not None else 'Not observed'} | {row['entrant_terminal_cash_after_recorded_bills_cents']/100:,.2f} |")
    insert_at=next(i for i,text in enumerate(out) if text.startswith('### Focused follow-up: Funded renewals and the entry cash window'))+1
    out.insert(insert_at,'#### Reproduced competitive renewal worlds\n\n'+'\n'.join(renewal_table)+'\n\nGenerated from [competitive_renewals.json](model/results/competitive_renewals.json). Months start at zero. Funding-adjusted bank change excludes equity and net loan principal, then reserves recorded unpaid operating bills. This is not residual asset value, distributable cash or lifetime ROI. Current funded capacity cannot guarantee all future locked service.')
    expansion=json.loads((ROOT/'model/results/support_expansion.json').read_text())
    for path,digest in expansion['source_sha256'].items():
        if hashlib.sha256((ROOT/path).read_bytes()).hexdigest()!=digest:raise SystemExit('Stale support-expansion dependency: '+path)
    expansion_table=['| Synthetic support/expansion world | Accepted zones | Funded starts | New commissioned | Opening-cohort supported robot-months | Provider closing cash, USD |', '| --- | ---: | ---: | ---: | ---: | ---: |']
    for row in expansion['summary']:
        q=row['accepted_zones'];expansion_table.append(f"| {row['case'].replace('_',' ')} | {int(q['numerator'])/int(q['denominator']):,.2f} | {row['funded_starts']} | {row['commissioned_new_units']} | {row['opening_cohort_supported_unit_months']} | {row['provider_closing_cash_cents']/100:,.2f} |")
    insert_at=next(i for i,text in enumerate(out) if text.startswith('### Focused follow-up: Installed support and finite expansion commitments'))+1
    out.insert(insert_at,'#### Reproduced installed-support and expansion worlds\n\n'+'\n'.join(expansion_table)+'\n\nGenerated from [support_expansion.json](model/results/support_expansion.json). Eight explicit months require 8,000 cleaning zones. Opening robots predate the cash window. Provider fees transfer within the operating boundary; loans, outstanding claims and terminal assets remain separate. Passing the recurring-support reserve does not fund every commissioning or future obligation.')
    recovery=json.loads((ROOT/'model/results/asset_recovery.json').read_text())
    for path,digest in recovery['source_sha256'].items():
        if hashlib.sha256((ROOT/path).read_bytes()).hexdigest()!=digest:raise SystemExit('Stale asset-recovery dependency: '+path)
    recovery_table=['| Synthetic recovery world | Sale | Buyer accepted zones | Remaining principal, USD | First supported buyer month | Final physical state |','| --- | --- | ---: | ---: | --- | --- |']
    for row in recovery['summary']:
        q=row['buyer_accepted_zones'];recovery_table.append(f"| {row['case'].replace('_',' ')} | {'Completed' if row['sale_completed'] else 'None'} | {int(q['numerator'])/int(q['denominator']):,.2f} | {row['closing_principal_claim_cents']/100:,.2f} | {row['first_buyer_supported_month'] if row['first_buyer_supported_month'] is not None else 'None'} | {row['final_physical_state']} |")
    insert_at=next(i for i,text in enumerate(out) if text.startswith('### Focused follow-up: Funded asset recovery and restored service'))+1
    out.insert(insert_at,'#### Reproduced funded recovery worlds\n\n'+'\n'.join(recovery_table)+'\n\nGenerated from [asset_recovery.json](model/results/asset_recovery.json). One fixed cleaning asset retains its identity; 7,200 zones are due across eight months. Purchase consideration is an internal transfer and initial relocation is counted once as a resource expense. Later failed qualification leaves paid buyer title and no restored service. Original customer/staff/debt obligations survive. No actual salvage value, legal priority or lifecycle ROI is identified.')
    physical = json.loads((ROOT/'model/results/physical_requirements_summary.json').read_text())
    for path, digest in physical['source_hashes'].items():
        if hashlib.sha256((ROOT/path).read_bytes()).hexdigest() != digest:
            raise SystemExit('Stale physical-requirements summary dependency: '+path)
    def reported(q):
        if q['value'] is not None:
            return f"{q['value']:,.1f}" if 'percent' in q['unit'] else f"{q['value']:,.0f}"
        if q.get('comparison') and 'bound' in q:
            return q['comparison']+str(q['bound'])
        return 'Not published / no exact match'
    physical_table = ['| Occupation (SOC 2018) | Exact-code OEWS jobs | Mean workday standing, % | Workers requiring fine manipulation, % | Workers requiring overhead reach, % | Join boundary |',
                      '| --- | ---: | ---: | ---: | ---: | --- |']
    for row in physical['occupations']:
        req = row['requirements']
        physical_table.append(f"| {row['occupation']} ({row['soc_2018']}) | {reported(row['employment'])} | {reported(req['standing_mean']['estimate'])} | {reported(req['fine_manipulation']['estimate'])} | {reported(req['reaching_overhead']['estimate'])} | {row['join_status']} |")
    # Place the observed table directly after its economic-atlas follow-up, not in the synthetic model section.
    insert_at = next(i for i,text in enumerate(out) if text.startswith('### Focused follow-up: Physical requirements'))+1
    out.insert(insert_at, '#### Observed crosswalk from preserved BLS workbooks\n\n'+ '\n'.join(physical_table) + '\n\nGenerated from [physical_requirements_summary.json](model/results/physical_requirements_summary.json). ORS requirements and OEWS employment have different populations. Published ranges and absent rows remain explicit. No row is multiplied into physical-work hours or robot-addressable jobs; the original workbooks, source rows and all standard-error footnotes are retained for reproduction.')
    frontier = json.loads((ROOT/'model/results/frontier_model_summary.json').read_text())
    for path, digest in frontier['source_hashes'].items():
        if hashlib.sha256((ROOT/path).read_bytes()).hexdigest() != digest:
            raise SystemExit('Stale frontier-model summary dependency: '+path)
    checks=frontier['regional_source_checks']
    table9=['| Source condition | Printed full / partial / failure counts | Score from stated rule | Printed score | Printed percent |',
            '| --- | --- | ---: | ---: | ---: |']
    for row in checks['rldx_table9']['rows']:
        c=row['printed_counts'];table9.append(f"| {row['condition']} | {c['full']} / {c['partial']} / {c['fail']} | {row['score_from_printed_counts_and_rule']:g} | {row['printed_score']:g} | {row['printed_percent']:.1f}% |")
    rynn=['| Reported training regime | Mean complete-task success | Mean subtask progress | Full completions implied by percentages | Protocol trials |',
          '| --- | ---: | ---: | ---: | ---: |']
    for row in checks['rynn_trials']['regimes']:
        rynn.append(f"| {row['regime']} | {row['reported_final_success_percent']:.2f}% | {row['reported_process_percent']:.2f}% | {row['full_completions_implied_by_percentages']} | {row['protocol_trials']} |")
    insert_at=next(i for i,text in enumerate(out) if text.startswith('### Focused follow-up: Regional model releases'))+1
    out.insert(insert_at,'#### Generated regional source checks\n\n'+ '\n'.join(table9)+'\n\nThe RLDX Table 9 counts and score column are preserved as published. The stated rule is full = 1, partial = 0.5 and failure = 0 over 24 trials; the discrepancy is unresolved. Conditional reconstruction is not a corrected empirical result.\n\n'+ '\n'.join(rynn)+'\n\nRynnBrain figures use three tasks and 20 trials per task; implied counts are arithmetic, not independently verified logs. Progress, full success, median inference and commercial accepted-output rates are separate measures. Generated from [frontier_model_summary.json](model/results/frontier_model_summary.json), with source locators in the accepted packet. No scenario coefficient or cross-model ranking is derived.')
    deployment=frontier['deployment_source_checks']['napkin_service']
    source_table=['| Reported restaurant service | Value |','| --- | ---: |']
    for key,label in [('reported_folds_per_hour','Reported folds per hour'),('reported_quality_percent','Accepted quality, percent'),('reported_window_hours','Service window, hours'),('required_accepted_napkins','Required accepted napkins'),('arithmetic_accepted_per_window','Rate times quality times hours'),('surplus_as_percent_of_required_output','Surplus as percent of requirement')]:
        source_table.append(f"| {label} | {deployment[key]:,.2f} |")
    insert_at=next(i for i,text in enumerate(out) if text.startswith('### Focused follow-up: Generalist, Dyna'))+1
    out.insert(insert_at,'#### Reproduced customer-output boundary\n\n'+'\n'.join(source_table)+'\n\nGenerated from [frontier_model_summary.json](model/results/frontier_model_summary.json), using K-E039. These are source arithmetic and issuer-reported inputs, not an independent operating audit or financial ROI. Hourly-rate timing is unspecified; no additional uptime penalty is applied. The conditional time-loss margin requires an active-time interpretation and is not observed availability. Synthetic scenario coefficients remain unchanged.')
    transaction=frontier['transaction']
    table=['| Seller-disclosed transaction item | USD millions |','| --- | ---: |']
    for key,label in [('cash_consideration','Cash consideration'),('equity_fair_value','Long-term investment fair value'),('escrow_fair_value','Indemnification escrow fair value'),('total_consideration','Reported total consideration'),('net_assets_sold','Reported net assets sold'),('seller_gain','Reported seller gain')]:
        table.append(f"| {label} | {transaction[key]:,.0f} |")
    out.append('### Reproduced acquisition disclosure\n\n'+ '\n'.join(table) + '\n\nGenerated from [frontier_model_summary.json](model/results/frontier_model_summary.json). Completion was March 27, 2026; announcement was April 15. Components reconcile to the reported total, and consideration less net assets reconciles to seller gain. These are seller accounting amounts, not Skild operating margin or an all-cash purchase. No model-customer economics are inferred.')
    summary=ROOT/'model/results/scenario_summary.csv'
    out.append('## 9. Common-engine scenarios and interpretation\n\nAll results in this section are **synthetic illustrations**. Each selected cell has a named service unit; unlike services must not be summed as a single output quantity. Assumed labor avoidability is separate from observed payroll removal. Fractional fleets represent continuous cohort relaxations, not an integer deployment schedule. Annual capital envelopes are assumptions; they do not establish available financing. See [model methods](model/METHODS.md) for exact scope and limitations.\n')
    if summary.exists():
        rows=list(csv.reader(summary.open()))
        if rows:
            out.append('Generated source: [scenario_summary.csv](model/results/scenario_summary.csv). No values are manually recalculated in this report.\n\n'+'\n'.join(['| '+' | '.join(rows[0])+' |','| '+' | '.join(['---']*len(rows[0]))+' |']+['| '+' | '.join(row)+' |' for row in rows[1:]]))
            cases={row['preset']:row for row in csv.DictReader(summary.open())}
            def n(preset,key): return f"{float(cases[preset][key]):,.0f}"
            out.append(f"""### What the scenario contrasts teach

The delayed-supply case ends with {n('delayed_supply','active_stock_expected_units')} active expected units versus {n('reference','active_stock_expected_units')} in the reference, but produces only {n('delayed_supply','cumulative_baseline_equivalent_hours')} cumulative baseline-equivalent hours versus {n('reference','cumulative_baseline_equivalent_hours')}. Later cohorts avoid some endpoint retirements. A terminal fleet snapshot therefore gives a misleading ranking of productive contribution; the full time path matters.

Ample supply with unready customers produces {n('ample_supply_unready','cumulative_baseline_equivalent_hours')} cumulative baseline-equivalent hours. Service stress produces {n('service_stress','cumulative_baseline_equivalent_hours')}. These are constructed counterexamples to the proposition that manufacturing capacity alone determines useful scale. They do not estimate the prevalence or magnitude of those bottlenecks in actual markets.

Digital-first produces {n('digital_first','cumulative_baseline_equivalent_hours')} robot-delivered baseline-equivalent hours, compared with {n('reference','cumulative_baseline_equivalent_hours')} in the reference. Less robot deployment is not necessarily a welfare loss: the human-led alternative also improves, changing the incremental economic case. This preset changes both human time reduction and robot coordination; it does not isolate either channel. Hold coordination fixed for a one-control comparison of the human-time mechanism. The model does not estimate economy-wide welfare from these scenario outputs.

In the separate monthly entrant case, delayed incumbent response requires peak funding of ${n('newco_raas','newco_peak_funding_usd')}; prompt response requires ${n('prompt_response','newco_peak_funding_usd')} and exposes a ${n('prompt_response','newco_funding_gap_usd')} gap under the same assumed commitment. Equal robot access does not guarantee equal commercial survival. This comparison isolates an assumed response mechanism; it is not evidence that those prices, demand shares or financing commitments are attainable. Its robots are not separately allocated from the annual fleet resource pool, so the two paths must not be added as jointly feasible output.
""")
    else:out.append('Scenario exports are not yet available; no numerical result is claimed in this build.')
    annual_path = ROOT/'model/results/annual_digital_comparison.json'
    if not annual_path.exists():
        raise SystemExit('Missing annual comparison; run scripts/export_trajectory.py')
    annual = json.loads(annual_path.read_text())
    for path, digest in annual['source_hashes'].items():
        if hashlib.sha256((ROOT/path).read_bytes()).hexdigest() != digest:
            raise SystemExit('Stale annual comparison dependency: '+path)
    out.append("### Annual digital paths and a moving alternative\n\nModel 0.2.0 implements the reviewed three-channel design and retains the corrected 0.1.1 hardware boundary. Constant paths preserve all 69,315 existing numerical fields across eight presets and both configurations. The six generated counterfactuals below use the same tote-handoff cell at 2030, five scenario years and no learned increment. Values are synthetic constant-2026 USD/site/year; reference resource costs and customer contract savings are separate measures.\n\nGenerated source: [annual_digital_comparison.json](model/results/annual_digital_comparison.json).")
    lines = ['| Counterfactual | Digital human C01 | Joint C11 | Robot resource value versus C01 | Customer savings | Economic sites / 12 | Installed expected robots |',
             '| --- | ---: | ---: | ---: | ---: | ---: | ---: |']
    for name, result in annual['results'].items():
        final = result['joint_by_year'][-1]
        joint = next(x for x in final['comparisons'] if x['cell_id'] == annual['cell_id'])
        cell = next(x for x in result['fleet']['cells'] if x['cell_id'] == annual['cell_id'] and x['year'] == final['year'])
        lines.append(f"| {name} | {joint['C01']:,.2f} | {joint['C11']:,.2f} | {joint['robotics_saving_on_digital_baseline']:,.2f} | {cell['economics']['customer_savings_usd']:,.2f} | {sum(x['economic'] for x in cell['sites'])} | {cell['active_stock']:,.2f} |")
    out.append('\n'.join(lines))
    out.append("The improving-human case lowers combined resource cost while closing new robot admission. Existing stock persists; the inherited acquisition/payback eligibility cap can suppress modeled output and is not an optimal continuation rule. Cheaper additional robot service can change that commercial result without directly changing capability. The conventional combined case retains the digital human baseline and required robot control, removing only the incremental coordination/service bundle. These alternatives neither calibrate an actual product nor form a jointly funded company model. See the [annual analysis](research/annual_digital_scenarios.md) and [implementation review](reviews/annual_trajectory_review.md).")
    architectures=json.loads((ROOT/'model/results/architecture_comparison.json').read_text())
    architecture_witnesses=json.loads((ROOT/'model/results/architecture_experiments.json').read_text())
    for packet in (architectures,architecture_witnesses):
        for path,digest in packet['source_hashes'].items():
            if hashlib.sha256((ROOT/path).read_bytes()).hexdigest()!=digest:
                raise SystemExit('Stale architecture dependency: '+path)
    def amount(value):return 'Not admitted' if value is None else f'{value:,.2f}'
    def interval(value):
        if value['status']=='internal_transfer_eliminated':return 'Internal transfer eliminated'
        return f"{value['lower_usd_year']:,.2f} to {value['upper_usd_year']:,.2f}; {value['status']}"
    table=['| Generic architecture | Resource cost/year, USD | Consolidated allocated cash benefit/year, USD | Model-fee interval, USD/year |', '| --- | ---: | ---: | --- |']
    for r in architectures['architectures']:
        table.append(f"| {r['label']} | {amount(r.get('resource_cost_usd_year'))} | {amount(r.get('cash_benefit_usd_year'))} | {interval(r['fee_intervals']['model_fee']) if r.get('fee_intervals') else 'Not admitted'} |")
    out.append('### Conditional architecture economics and fee allocation\n\nSynthetic one-site reference: '+architectures['cell']['label']+', '+str(architectures['comparison_scope']['year'])+'. Selected-year conditions are held over service life; integer-cent charges and transfers are reconciled, with no discounting, company funding or actual staffing schedule. This is not a named-vendor comparison. Generated source: [architecture_comparison.json](model/results/architecture_comparison.json).\n\n'+'\n'.join(table))
    table=['| Synthetic witness | Selected architecture | Resource cost/year, USD | Consolidated allocated cash benefit/year, USD | Robot accepted units/year |', '| --- | --- | ---: | ---: | ---: |']
    for name,result in architecture_witnesses['cases'].items():
        selected='open_adapted' if name=='lean_open_adaptation' else 'licensed_independent'
        r=next(x for x in result['architectures'] if x['architecture_id']==selected)
        table.append(f"| {name} | {selected} | {amount(r.get('resource_cost_usd_year'))} | {amount(r.get('cash_benefit_usd_year'))} | {amount(r.get('robot_accepted_units_year'))} |")
    out.append('Generated source: [architecture_experiments.json](model/results/architecture_experiments.json). Each row is a separate counterfactual; these are not additive deployments.\n\n'+'\n'.join(table)+'\n\nChanging a fee alone reallocates the same gain. Adaptation changes resources without directly improving physical output; intervention affects both support expense and robot contribution. Leaner open adaptation can reverse a conditional ranking. A better digital-human alternative can reduce robot value even when combined cost falls. Compatibility/rights/quality premises that fail produce no economic ranking. See [architecture methods](model/ARCHITECTURES.md) and [implementation audit](reviews/architecture_economics_review.md).')
    experiments = ROOT/'model/results/treasury_witnesses.json'
    if experiments.exists():
        treasury=json.loads(experiments.read_text())
        coordination=json.loads((ROOT/'model/results/coordination_witnesses.json').read_text())
        monthly=json.loads((ROOT/'model/results/monthly_deployment_witnesses.json').read_text())
        for packet in (treasury,coordination,monthly):
            if hashlib.sha256((ROOT/packet['code_path']).read_bytes()).hexdigest()!=packet['code_sha256']:
                raise SystemExit('Stale isolated experiment export: '+packet['code_path'])
            for path,digest in packet.get('source_hashes',{}).items():
                if hashlib.sha256((ROOT/path).read_bytes()).hexdigest()!=digest:
                    raise SystemExit('Stale experiment dependency: '+path)
        out.append('''## 10. Local experiments: cash settlement and transaction state

These experiments are separate, deterministic **synthetic software witnesses**. They do not supply empirical coefficients, alter the eight deployment scenarios, or establish a jointly funded physical fleet. The treasury design's full monthly physical integration remains incomplete. The coordination fixture neither imports nor runs RMF/ROS and controls no robot. Their narrow purpose is to make important failure cases reproducible before attempting a larger model or target installation.

### Treasury: a positive assumed spread can coexist with a cash shortfall

The first financial core records legal actors, cash, obligations, disjoint earmarks, restricted deposits and explicit credit contracts. It settles invoices against actual available balances with recorded event order. A future receivable or an undrawn commitment cannot be spent as current cash. Paying an invoice consumes its own earmark once; an unrelated invoice cannot use that reservation. Principal repayment changes the loan balance rather than being labeled an operating expense. All figures below are constructed accounting examples in USD.

Generated source: [treasury_witnesses.json](model/results/treasury_witnesses.json). The complete events and counterparty balances are retained there. See [the core boundary](model/TREASURY_CORE.md) and [independent review](reviews/treasury_core_review.md).
''')
        finance_cases=[
            ('witness_1_unfunded','provider','Payroll paid; proposed start blocked before future collection'),
            ('witness_1_funded_next_month','provider','Explicit draw funds the start; later collection and principal repayment complete'),
            ('witness_2_start_costs_once','provider','Two starts paid; one accepted sale collected; no second manufacturing charge'),
            ('witness_3_restricted_deposit_refunded','provider','Restricted deposit cannot fund start; refund restores original provider cash'),
            ('witness_5_unpaid_fee','entrant','Full-or-nothing fee remains unpaid; no automatic overdraft'),
            ('witness_7_earmark_consumed','payer','Own invoice consumes earmark; unrelated payment is blocked'),
        ]
        table=['| Financial witness | Selected actor | Closing cash, USD | Interpretation |','| --- | --- | ---: | --- |']
        for key,actor,meaning in finance_cases:
            account=next(a for a in treasury['result'][key]['actors'] if a['actor_id']==actor)
            table.append(f"| {key} | {actor} | {account['cash_cents']/100:,.2f} | {meaning} |")
        out.append('\n'.join(table))
        out.append('''The funded and unfunded paths are alternative worlds, not balances to add. A financial settlement test does not prove that a robot was manufactured, commissioned, supported or reassigned. The stage-1 yield case tests the payment boundary only; the fee case tests an unpaid liability only. The core also lacks an automatic payment scheduler, credit-maturity collection/default and interest accrual. Actual financing terms and supplier working capital remain separate empirical questions.
''')
        out.append('''### Monthly physical progress must also be paid and supported

The next isolated fixture connects that cash core to integer unit identities, compatible components, deterministic accepted/rejected counts, shipment, commissioning and supported service. It uses one provider-owned system, fixed operator assignments and preplanned actions. Opening robots are historically funded stocks; their acquisition cost lies outside the horizon. Output is an exact rational synthetic service flow, not measured customer throughput.

Generated source: [monthly_deployment_witnesses.json](model/results/monthly_deployment_witnesses.json). Each row below is a separate constructed world; closing stocks count units, cash is USD, and output shows each operator's last modeled month. Source hashes cover both the monthly implementation and the treasury dependency.
''')
        table=['| Witness | Closing physical stocks | Provider closing cash, USD | Last-month accepted service |','| --- | --- | ---: | --- |']
        for key,case in monthly['result'].items():
            row=case['months'][-1]
            stocks='; '.join(f'{name}: {value}' for name,value in row['closing_stock'].items())
            outputs=[]
            for output in row['outputs']:
                value=output['accepted_output_units']
                rendered=str(value['numerator']) if value['denominator']==1 else f"{value['numerator']}/{value['denominator']}"
                outputs.append(output['operator_id']+': '+rendered)
            table.append(f"| {key} | {stocks} | {row['closing_cash_cents'][case['plan']['provider_actor']]/100:,.2f} | {'; '.join(outputs)} |")
        out.append('\n'.join(table))
        out.append('''A paid start at month 0, phase 5 is accepted at month 1, phase 4 and can ship in phase 5 of that same month. With one-month commissioning lead, it commissions at month 2, phase 4 and delivers 25 units at phase 6 under one quarter-rate ramp; its next full month delivers 100. There is no extra finished-stock month or second annual half-year penalty. If commissioning cash is missing, the already paid unit remains in transit and produces zero. If the start is rejected, its manufacturing expense and consumed components remain sunk.

The static shared-allocation case begins with five finished and two installed units. Common support and commissioning limits permit two new incumbent assignments and one entrant assignment, leaving two finished units. The entrant's first-month output is 25, even though its request is ten robots. This tests conservation and actual assignment; it does not connect the separate ENTRY-FG-01 business, simulate customer competition, or establish an entrant return.

Existing installed support has strict priority. Receipts arriving after its phase-3 support attempt cannot retroactively repair that month's service; any unsupported opening installed unit blocks additions under this deliberately conservative policy. Contingent prepayment bookings can be canceled when work is not delivered, while previously earned obligations are not erased. The fixture does not schedule every opening company obligation, model sale/lease terms or operator cash, enforce default/recovery, or make endogenous investments. See [methods and limitations](model/MONTHLY_DEPLOYMENT.md) and [independent review](reviews/monthly_deployment_review.md). The full shared-treasury/entrant requirement remains partial.

### Coordination: retained uncertainty is sometimes the correct result

The local fixture compares blind resubmission with a durable business-intent ledger plus explicit authoritative reconciliation. Each policy receives the same invented order, fault and mock lookup capability. The deliberately naive comparator is a weak baseline, not an evaluation of a mature industrial integrator or an LLM. The reconciler relies on an added ability to find all tasks for a business key and establish dispatch finality; the inspected RMF sources do not establish that capability.

Generated source: [coordination_witnesses.json](model/results/coordination_witnesses.json). “Effect units” are invented irreversible actions, with no mapping to deliveries, elapsed time, wages or physical throughput. “Verified records” counts reconciled local completion; the naive comparator has no such ledger and therefore reports unknown rather than crediting API responses as completed business work.
''')
        table=['| Injected fault | Policy | External tasks | Synthetic effect units | Verified local records |','| --- | --- | ---: | ---: | ---: |']
        for case in coordination['result']['cases']:
            accepted=case['accepted_business_outputs']
            table.append(f"| {case['fault']} | {case['policy']} | {case['external_task_count']} | {case['synthetic_effect_units']} | {'Unknown' if accepted is None else accepted} |")
        out.append('\n'.join(table))
        out.append('''When authoritative lookup is unavailable, blocking a retry can prevent a duplicate while leaving completion unverified. A local journal cannot make a remote effect and its local acknowledgment atomic. Even an empty lookup is insufficient if the original request might arrive later. Separate cancellation traces retain partial effects after acknowledgment, and completion racing with cancellation requires review. This establishes behavior of the constructed protocol under its declared assumptions, not incident rates or economic benefits in an installed system. See [fixture methods and limits](model/COORDINATION_TRANSACTION_FIXTURE.md) and [independent review](reviews/coordination_fixture_review.md).

### Inspecting the scenario calculation

The dashboard's joint comparison tables now expose the four branches through **Trace inputs and costs**. The trace calls the same engine and shows human/site digital cost, robot operating cost, annual capital consumption, accepted robot output and retained human hours. Exact inputs, source-function excerpts and matching scenario/engine hashes are available in the dialog. The reference follows the selected annual year and its resolved digital conditions, without learned increments; it remains a matched site contrast, not an installed-fleet estimate. A changed scenario or selected scope invalidates an open trace. This closes a bounded explanatory gap, while result-specific lineage for the rest of the dashboard remains incomplete.

The **Evidence fields** panel adds exact recorded geography, system/configuration, embodiment, harness, openness-layer and license selectors. Missing fields can be selected explicitly. A compound geography description remains the source's compound value, and a license label leaves commercial and hardware rights to the full artifact terms. These filters change evidence navigation only; they do not reclassify unknown records or alter scenario populations. Dedicated resource-grade filtering and comprehensive typed joins remain incomplete. See [filter semantics](dashboard/EVIDENCE_FILTERS.md).
''')
    out.append('''## 11. What remains unresolved

The sources establish bounded workflows, relationships and constraints. Public disclosures often do not establish accepted-output exposure, all human support, retained deployment, negotiated prices, avoidable staffing, qualified supply or complete costs. These gaps limit market ranking and investment conclusions. A functioning mechanism model does not resolve them by assigning synthetic inputs.

Workstream K now contributes nine actor-role records, four contrasting dossiers, six model/release cards and eight artifact-rights cards. Their source and cost boundaries remain explicit. The four-architecture service comparison now has a separate synthetic calculation and sensitivities. Actual target costs, effective rights and qualified configurations remain unknown; the calculation does not fill those source gaps. The next research priorities are: reconcile field service/intervention denominators; challenge shared-resource and financial accounting; validate digital coordination against a strong simpler baseline; test customer entry against a prompt incumbent with equal technology access; qualify specific supply/workload dependencies; deepen labor crosswalks without invented physical shares; and expand non-Spot operator and nonadoption evidence. Each has a bounded action, evidence need and stopping condition in the continuing roadmap.

The acceptance register records individual requirements and limitations. Source counts and view counts do not themselves establish substantive completion. The original campaign window has ended with incomplete requirements. This separately dated continuation preserves the earlier edition and its gaps; the handoff records the interruption and next actions without backdating work or resetting the week.
''')
    (ROOT/'REPORT.md').write_text('\n\n'.join(out).rstrip()+'\n')
    print('Wrote REPORT.md:',len((ROOT/'REPORT.md').read_text().split()),'words')
if __name__=='__main__':build()
