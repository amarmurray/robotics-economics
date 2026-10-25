#!/usr/bin/env python3
"""Assemble report from authoritative research chapters; no independent calculations."""
from pathlib import Path
import csv
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
def chapter(text):
    lines=text.splitlines()
    # Remove chapter title, then nest its remaining headings below report chapter.
    if lines and lines[0].startswith('# '): lines=lines[1:]
    lines=[('#'+x if x.startswith('#') else x) for x in lines]
    s='\n'.join(lines).strip()
    s=s.replace('(../data/','(data/').replace('(../model/','(model/').replace('(../RESEARCH_', '(RESEARCH_')
    for _,name in CHAPTERS:s=s.replace('('+name+')','(research/'+name+')')
    return s

def build():
    missing=[name for _,name in CHAPTERS if not (ROOT/'research'/name).exists()]
    if missing:raise SystemExit('Missing substantive chapters: '+', '.join(missing))
    out=['''# Robotics Economics — first integrated research checkpoint

Edition 0.1, campaign in progress. This is a substantive early checkpoint, **not completion of the seven-day campaign**.

Launch input: `campaign launch snapshot (see ignored sync_receipt.json)`. Evidence retrieved on 25 October 2026 unless an individual record states otherwise. Source observation periods and publication dates remain distinct. This report is generated from the authoritative chapters in `research/` by `python3 scripts/build_report.py`; quantitative scenario exports come only from `model/engine.py`.

Campaign T0: October 25, 2026, 11:52:14 EDT. Deadline: November 1, 2026, 10:52:14 EST, America/New_York; exactly 168 elapsed hours. Work continues through available execution windows. No uninterrupted-compute or full-week-work claim is made.

The report uses a US quantitative labor anchor with global provider, research and supply evidence. Synthetic scenario outputs explore mechanisms; they are not empirical market forecasts, measured ROI or estimates of payroll actually removed. Read the latest [continuation findings](CONTINUATION_FINDINGS.md), [reproduction instructions](REPRODUCE.md), the [acceptance audit](ACCEPTANCE_AUDIT.md), [requirement register](acceptance_register.json) and [continuing roadmap](RESEARCH_ROADMAP.md) with the findings. The local dashboard entry is `python3 scripts/serve.py`.

Six specialist launch requests explicitly selected GPT-6 Astra / Ultra and were accepted. Actual serving model/reasoning is not independently exposed; lead settings cannot be verified or changed through the available tools. That limitation is disclosed rather than silently treated as a verified configuration.

The original Mac checkout was unavailable. Work occurred in a fresh cloud checkout, preserving unseen local edits. Publication to the private repository does not establish consumption by a separate Work session.
''']
    for i,(title,name) in enumerate(CHAPTERS,1):
        out.append(f'## {i}. {title}\n\nAuthoritative chapter: [research/{name}](research/{name}).\n\n'+chapter((ROOT/'research'/name).read_text()))
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
    out.append('''## 9. What remains unresolved

The sources establish bounded workflows, relationships and constraints. Public disclosures often do not establish accepted-output exposure, all human support, retained deployment, negotiated prices, avoidable staffing, qualified supply or complete costs. These gaps limit market ranking and investment conclusions. A functioning mechanism model does not resolve them by assigning synthetic inputs.

The next research priorities are: reconcile field service/intervention denominators; challenge shared-resource and financial accounting; validate digital coordination against a strong simpler baseline; test customer entry against a prompt incumbent with equal technology access; qualify specific supply/workload dependencies; deepen labor crosswalks without invented physical shares; and expand non-Spot operator and nonadoption evidence. Each has a bounded action, evidence need and stopping condition in the continuing roadmap.

The acceptance register records individual requirements and limitations. Source counts and view counts do not themselves establish substantive completion. The campaign remains active within the original elapsed-time window, with interruptions and next actions recorded honestly in the handoff. At the deadline, the strongest verified edition must be packaged with any coverage gaps, rather than backdating work or resetting the week.
''')
    (ROOT/'REPORT.md').write_text('\n\n'.join(out).rstrip()+'\n')
    print('Wrote REPORT.md:',len((ROOT/'REPORT.md').read_text().split()),'words')
if __name__=='__main__':build()
