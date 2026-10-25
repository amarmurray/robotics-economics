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
]
FOLLOWUPS = {
 'capability_learning.md': [('Learning-data economics and validation boundaries', 'learning_data_economics.md')],
 'customer_value.md': [('Hospital service, support and economic denominators', 'field_support_denominators.md')],
 'digital_ecosystem.md': [('Benchmark reproducibility and transaction authority', 'coordination_reproducibility.md')],
 'physical_supply_field.md': [('Non-Spot operator evidence and retained-deployment limits', 'quadruped_operator_followup.md')],
 'digital_infrastructure.md': [('Onboard workload qualification and operating deadlines', 'onboard_workload_qualification.md')],
}
def chapter(text, depth=1):
    lines=text.splitlines()
    # Remove chapter title, then nest its remaining headings below report chapter.
    if lines and lines[0].startswith('# '): lines=lines[1:]
    lines=[('#'*depth+x if x.startswith('#') else x) for x in lines]
    s='\n'.join(lines).strip()
    s=s.replace('(../data/','(data/').replace('(../model/','(model/').replace('(../RESEARCH_', '(RESEARCH_')
    for path in (ROOT/'research').glob('*.md'):
        s=s.replace('('+path.name+')','(research/'+path.name+')')
    return s

def build():
    sources=CHAPTERS+[item for items in FOLLOWUPS.values() for item in items]
    missing=[name for _,name in sources if not (ROOT/'research'/name).exists()]
    if missing:raise SystemExit('Missing substantive chapters: '+', '.join(missing))
    out=['''# Robotics Economics — integrated research report

Edition 0.4, campaign in progress. This full report integrates the broad research chapters and their reviewed follow-ups. It remains **an interim edition within the seven-day campaign**.

Launch input: `campaign launch snapshot (see ignored sync_receipt.json)`. Evidence retrieved on 25 October 2026 unless an individual record states otherwise. Source observation periods and publication dates remain distinct. This report is generated from the authoritative chapters in `research/` by `python3 scripts/build_report.py`; quantitative scenario exports come only from `model/engine.py`.

Campaign T0: October 25, 2026, 11:52:14 EDT. Deadline: November 1, 2026, 10:52:14 EST, America/New_York; exactly 168 elapsed hours. Work continues through available execution windows. No uninterrupted-compute or full-week-work claim is made.

The report uses a US quantitative labor anchor with global provider, research and supply evidence. Synthetic scenario outputs explore mechanisms; they are not empirical market forecasts, measured ROI or estimates of payroll actually removed. The hospital, quadruped, benchmark/coordination, learning-data and onboard-workload follow-ups are integrated into the relevant chapters below. The [reproduction instructions](REPRODUCE.md), [acceptance audit](ACCEPTANCE_AUDIT.md), [requirement register](acceptance_register.json) and [continuing roadmap](RESEARCH_ROADMAP.md) support this report. The local dashboard entry is `python3 scripts/serve.py`.

Begin with the executive argument for the decision logic, then use the economic atlas to orient the technical, organizational and supply evidence. The common-engine section connects those findings to conditional scenarios. Detailed source locators, explicit conflicts and unknowns remain in the chapters and their machine-readable evidence packages; no favorable headline substitutes for their operating boundary. This expanded edition deliberately retains the full source analysis rather than compressing it into a short investment thesis.

Six specialist launch requests explicitly selected GPT-6 Astra / Ultra and were accepted. Actual serving model/reasoning is not independently exposed; lead settings cannot be verified or changed through the available tools. That limitation is disclosed rather than silently treated as a verified configuration.

The original Mac checkout was unavailable. Work occurred in a fresh cloud checkout, preserving unseen local edits. Publication to the private repository does not establish consumption by a separate Work session.
''']
    contents=[]
    headings=[f'{i}. {title}' for i,(title,_) in enumerate(CHAPTERS,1)]+[
        '8. Common-engine scenarios and interpretation',
        '9. Local experiments: cash settlement and transaction state',
        '10. What remains unresolved',
    ]
    for heading in headings:
        anchor=re.sub(r'[^a-z0-9 -]', '', heading.lower()).replace(' ', '-')
        contents.append(f'- [{heading}](#{anchor})')
    out.append('## Contents\n\n'+'\n'.join(contents))
    for i,(title,name) in enumerate(CHAPTERS,1):
        out.append(f'## {i}. {title}\n\nAuthoritative chapter: [research/{name}](research/{name}).\n\n'+chapter((ROOT/'research'/name).read_text()))
        for follow_title,follow_name in FOLLOWUPS.get(name,[]):
            out.append(f'### Focused follow-up: {follow_title}\n\nAuthoritative analysis: [research/{follow_name}](research/{follow_name}).\n\n'+chapter((ROOT/'research'/follow_name).read_text(),depth=2))
    summary=ROOT/'model/results/scenario_summary.csv'
    out.append('## 8. Common-engine scenarios and interpretation\n\nAll results in this section are **synthetic illustrations**. Each selected cell has a named service unit; unlike services must not be summed as a single output quantity. Assumed labor avoidability is separate from observed payroll removal. Fractional fleets represent continuous cohort relaxations, not an integer deployment schedule. Annual capital envelopes are assumptions; they do not establish available financing. See [model methods](model/METHODS.md) for exact scope and limitations.\n')
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
    out.append('''### Corrected hardware comparison and the next dynamic baseline

Model 0.1.1 corrects a high-memory accounting omission: its synthetic $800 annual configuration charge now appears in both robot branches. Previously C10 omitted that charge, overstating the cost interaction by $800. The same additional power burden already applied to both branches. At 2,000 operating hours, each robot branch incurs $832 above its standard-board counterpart under the specified electricity price. All numerical fields in the eight standard presets remain unchanged; engine, catalog and evidence-provenance hashes are regenerated. The [independent correction review](reviews/high_memory_cost_review.md) records the comparison against the previous committed version.

The next digital extension has a [reviewed design](research/digital_trajectory_design.md), with [independent numerical witnesses](reviews/digital_trajectory_design_review.md), but no implemented annual trajectory runner yet. It proposes three independently specified synthetic paths: human time reduction, signed robot coordination, and annual additional robot digital-service cost. Every annual adoption gate, resource-cost comparison and operating result must use the same contemporaneous values. A lower robot-service price can change cash margins without changing competence; an improving human baseline can weaken adoption even when the combined robot process also gets cheaper.

Implementation must reproduce the corrected scalar engine on constant paths, preserve stock when economic eligibility changes, retain adverse/nonmonotone paths and keep direct changes separate from deployment-mediated learning. The proposed service-cost path does not supply a token-use, failed-attempt or latency model. Existing all-vintage software upgrades, current-condition screening and separate initial-year commercial/monthly-entry references remain explicit limitations. Design acceptance alone does not close the evolving-comparator requirement.
''')
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
        out.append('''## 9. Local experiments: cash settlement and transaction state

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

The dashboard's joint comparison tables now expose the four branches through **Trace inputs and costs**. The trace calls the same engine and shows human/site digital cost, robot operating cost, annual capital consumption, accepted robot output and retained human hours. Exact inputs, source-function excerpts and matching scenario/engine hashes are available in the dialog. The reference remains one annual site at the final horizon, without learned increments; changing the display year does not turn it into an installed-fleet estimate. A changed scenario invalidates an open trace. This closes a bounded explanatory gap, while result-specific lineage for the rest of the dashboard remains incomplete.

The **Evidence fields** panel adds exact recorded geography, system/configuration, embodiment, harness, openness-layer and license selectors. Missing fields can be selected explicitly. A compound geography description remains the source's compound value, and a license label leaves commercial and hardware rights to the full artifact terms. These filters change evidence navigation only; they do not reclassify unknown records or alter scenario populations. Dedicated resource-grade filtering and comprehensive typed joins remain incomplete. See [filter semantics](dashboard/EVIDENCE_FILTERS.md).
''')
    out.append('''## 10. What remains unresolved

The sources establish bounded workflows, relationships and constraints. Public disclosures often do not establish accepted-output exposure, all human support, retained deployment, negotiated prices, avoidable staffing, qualified supply or complete costs. These gaps limit market ranking and investment conclusions. A functioning mechanism model does not resolve them by assigning synthetic inputs.

The next research priorities are: reconcile field service/intervention denominators; challenge shared-resource and financial accounting; validate digital coordination against a strong simpler baseline; test customer entry against a prompt incumbent with equal technology access; qualify specific supply/workload dependencies; deepen labor crosswalks without invented physical shares; and expand non-Spot operator and nonadoption evidence. Each has a bounded action, evidence need and stopping condition in the continuing roadmap.

The acceptance register records individual requirements and limitations. Source counts and view counts do not themselves establish substantive completion. The campaign remains active within the original elapsed-time window, with interruptions and next actions recorded honestly in the handoff. At the deadline, the strongest verified edition must be packaged with any coverage gaps, rather than backdating work or resetting the week.
''')
    (ROOT/'REPORT.md').write_text('\n\n'.join(out).rstrip()+'\n')
    print('Wrote REPORT.md:',len((ROOT/'REPORT.md').read_text().split()),'words')
if __name__=='__main__':build()
