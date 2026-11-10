#!/usr/bin/env python3
"""Render the bounded evidence sequence from its authoritative synthesis matrix."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
SOURCE=ROOT/'research/deployment_evidence_matrix.json'
OUTPUT=ROOT/'research/deployment_evidence_sequence.md'

def cell(value):
    return str(value).replace('|','&#124;').replace('\n',' ')

def table(headers,rows):
    return '\n'.join(['| '+' | '.join(headers)+' |','| '+' | '.join(['---']*len(headers))+' |']+
                     ['| '+' | '.join(cell(v) for v in row)+' |' for row in rows])

def build():
    d=json.loads(SOURCE.read_text())
    sources={e['evidence_id']:e for e in d['source_index']}
    def refs(r):
        return ' '.join('['+eid+'](#source-'+eid.lower()+')' for eid in r['evidence_ids'])
    out=['''# Minimum evidence for the three deployment decisions

Edition 0.53 · 10 November 2026 · bounded synthesis of accepted edition 0.52.

**First obtain one coherent target record, not another headline.** None of the three packs yet supplies a current, target-specific joined service, staffing and payer account. The first acquisition is a named site/configuration/decision owner and common service contract. Then obtain the smallest linked packet capable of accepting or rejecting the particular claim. A useful information or capacity service need not remove payroll; scale or operating-company entry requires additional rights, funding and customer evidence.

This sequence operationalizes the existing [three decision packs](deployment_entry_decisions.md), [hospital denominator audit](field_support_denominators.md), [utility audit](quadruped_operator_followup.md) and [automotive comparison](automotive_workcell_decision.md). It adds no source observations, measured savings, model calibration or status promotion. The authoritative rows, dependencies and accepted source-package fingerprints are in [the structured matrix](deployment_evidence_matrix.json); this document is generated from it.

“Minimum” means the required **record types and joins for a bounded claim**, not an arbitrary sample size or universal performance threshold. A complete evidence packet may show failure. Acceptance of the packet is separate from approval to deploy. The actual service owner must prespecify quality, timeliness, operating conditions and decision-relevant uncertainty limits; none is supplied by a synthetic scenario. If uncertainty still crosses the proposed decision boundary, collect the missing exposure or retain a narrower conclusion.

A historical-claim audit can use an already identified episode—such as Laredo file25-260 or the BMW Figure02 Spartanburg cohort—without choosing a new site. Its result stays historical. A forward deployment decision additionally needs current applicability, rights and supported configuration. No current target site, entrant, acquisition or financier has been selected by this synthesis. Named historical source parties are not assumed to own every needed dataset or to permit access. All proposed custodians below are roles to resolve, not contacts or outreach instructions. Request-only, confidential, paid, authenticated and previously denied routes remain closed. This tranche specifies future evidence acceptance; it initiates no data request, experiment, purchase or commercial action.
''']
    out.append('## Immediate decision and first packet\n')
    out.append(table(['Existing case','Supported direction and boundary','First packet','Decision after a qualified bounded result'],[
        [c['label'],c['recommendation']+' '+c['target_status'],', '.join(c['first_packet']),c['minimum_decision']] for c in d['cases']]))
    out.append('''\nThe three unselected cells—3PL tote transfer, specialist floor cleaning and construction installation—retain their existing comparison roles. They inherit the join/acceptance method only; no hospital, utility or automotive rate or cost transfers. This is a dependency order, not a new ranking of market returns.\n''')
    out.append('## Cross-case minimum evidence matrix\n')
    out.append(table(['Case','Supported conclusion','Unresolved claim','Minimum evidence packet','Acceptance criteria','Likely owner/source','Decision consequence'],[
        [c['label']]+[c['matrix_summary'][k] for k in ['supported','unresolved','minimum','acceptance','owner','decision']] for c in d['cases']]))
    out.append('\nThe detailed rows below specify exact joins and conditional extensions for each packet. A complete cost claim requires the relevant H6/U6/A6 records even where no payroll saving is claimed.\n')
    out.append('## Keep six evidence stages separate\n')
    out.append(table(['Stage','What this record establishes','What remains unproven'],[
        [s['name'],s['proves'],s['does_not_prove']] for s in d['stage_semantics']]))
    out.append('''\nThese are distinct evidence states, not a mandatory payment chronology. Collect financial records in parallel: a prepayment can precede delivery, and accepted service can precede settlement. Never use advancement in one lane to fill an unknown in another. Installation acceptance is also distinct from recurring accepted service.

For maintenance, distinguish the robot's own repair/support from the customer's downstream asset decision. In utility inspection, a reviewed “no action” disposition can be valid information without a realized saving. Hospital and automotive cases need their own robot-maintenance, service-continuity and work-change records; they do not inherit an avoided-outage benefit.\n''')
    out.append('## Acquire in this order, with explicit stopping points\n')
    out.append(table(['Batch','Requirement IDs','Packet and reuse','Stop or change the claim when'],[
        [b['batch_id'],', '.join(b['requirements']),b['output'],b['exit']] for b in d['acquisition_batches']]))
    out.append('''\nCollect the work/resource fields during the same observation window as service, even though benefit and cash conclusions are evaluated later. Do not wait until a favorable performance result to look for escort, review, downtime or upstream preparation costs. B4 is conditional: a capacity-only hospital case need not establish a staff cut; an information-only utility case need not claim avoided outages. Every economic claim still needs its own complete cost boundary.

Use one revision-controlled packet per case with these shared keys: site and acceptance owner; unique due service/asset/part and attempt IDs; hardware/software/payload/interface revision; legal actor/payer; due/capture/acceptance/action/invoice/payment timestamps; cohort and exclusions; and obligation/PO/invoice/payment references. Allocate shared people, infrastructure and support once across cases, retaining each service unit. A paid fee and the same provider resource cost must not both enter consolidated cost.

**Minimal first handoff:** H1–H3 for hospital; U1–U3 for utility; A1–A3 for automotive. A named case manifest, owner authorization and applicable operating/support terms precede a target deployment judgment. An authorized service-only evaluation does not require a new equipment purchase: a missing sales order leaves the commercial-commitment claim open while service evidence can still be assessed. A matched service dataset then determines whether more expensive benefit/return analysis is warranted. The Laredo order/receiving record is a specific way to close its historical transaction trace; it cannot resolve the substation target's service or economics.\n''')
    out.append('## Claim-level evidence matrix\n')
    out.append('''Each row preserves a supported source conclusion, a still-open target claim, the minimum missing evidence, a packet acceptance test, a proposed custodian and the decision consequence. Dependencies are evidential prerequisites, not authorization to acquire private records. X1/X2 use the applicable case packet; they never feed a synthetic result back into an empirical gap.\n''')
    for c in d['cases']+[dict(case_id='CROSS-CASE',label='Conditional stronger claims: digital contribution and entry')]:
        out.append('### '+c['label']+'\n')
        for r in [r for r in d['requirements'] if r['case_id']==c['case_id']]:
            # One vertical matrix per row keeps full acceptance tests readable in Markdown/PDF.
            out.append('#### '+r['requirement_id']+' · '+r['stage'].replace('_',' ')+'\n')
            dep=', '.join(r['depends_on']) or 'Target selection / applicable case packet as described above'
            if r['conditional_dependencies']:
                dep+='; conditional: '+'; '.join(x['claim']+' → '+', '.join(x['requires']) for x in r['conditional_dependencies'])
            out.append(table(['Field','Decision evidence requirement'],[
                ['Prerequisites',dep],
                ['Supported conclusion',r['supported_conclusion']+' '+refs(r)],
                ['Unresolved claim',r['unresolved_claim']],
                ['Minimum evidence',' '.join(r['minimum_evidence'])],
                ['Accept this evidence only if',r['evidence_acceptance_criteria']],
                ['Likely custodian/source',r['likely_custodian_or_source']],
                ['Decision consequence',r['decision_consequence']]
            ])+'\n')
    out.append('''## Reading a completed packet

Keep an intake receipt with the target/claim ID, supplied artifacts and revision, row IDs satisfied, unresolved conflicts, accepted and rejected denominators, owner of the decision and one of four outcomes: **bounded supported conclusion; reject/redesign this proposal; wait for specified missing evidence; narrower claim only**. Do not turn “packet received” into “deployment approved.” A missing source remains unknown, not zero or evidence of abandonment.

For incremental digital/model claims, reuse the physical service and cost records with equal baseline information, human authority and target rights. Preserve no-change/no-learning comparisons and failed qualification cost. For entry/scale, add actual supported allocation and legal-entity funding/customer obligations; acquisition reassigns existing activity. The current synthetic witnesses identify possible reversals and fields to inspect. They supply no empirical value, success rate or transferable contract.

**Remaining dependency:** one missing joined packet for an explicitly identified historical episode or current target, with an identifiable acceptance owner. Existing named source episodes can supply the case key; selecting a new site is not a prerequisite for auditing those historical claims. That is the next concrete handoff; neither another generic source search nor additional favorable synthetic cases closes it. No empirical requirement is marked complete by this matrix.\n''')
    out.append('## Accepted source index\n')
    out.append('''All records below were already accepted at the input commit. Dates and evidence classes are preserved; original URLs are provenance links, not newly retrieved sources. Full claims, incentives, conflicts and limits remain in the linked local packages. A null publication date remains unknown. The structured matrix records exact package hashes for this input.\n''')
    for eid,e in sources.items():
        out.append('### Source '+eid+'\n')
        out.append('['+eid+' accepted record](../'+e['accepted_package']+') · '+str(e['publication_date'] or 'Publication date unknown')+' · '+str(e['source_status'])+'. ['+e['title'].replace('[','(').replace(']',')')+']('+str(e['source_url'])+').\n')
    return '\n'.join(out).rstrip()+'\n'

if __name__=='__main__':
    OUTPUT.write_text(build())
    print('Wrote',OUTPUT.relative_to(ROOT))
