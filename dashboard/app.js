'use strict';
const $ = id => document.getElementById(id);
const esc = v => String(v ?? '').replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const fmt = (v, decimals=0) => v === null || v === undefined ? 'Unknown' : typeof v === 'number' ? v.toLocaleString('en-US',{maximumFractionDigits:decimals}) : esc(v);
const money = v => v === null || v === undefined ? 'Unknown' : '$'+fmt(v);
const title = s => String(s).replaceAll('_',' ').replace(/\b\w/g,x=>x.toUpperCase());
const safeURL = v => typeof v === 'string' && /^https?:\/\//.test(v) ? v : null;
let enterpriseState={data:null,loading:false,selection:"shared_reference",current:null,inputs:null,error:"",requestId:0};
let financeState={data:null,loading:false,selection:"term_reference",current:null,inputs:null,error:"",requestId:0,imported:false};
let bridgeState={data:null,loading:false,selection:"calendar_improving",current:null,inputs:null,error:"",requestId:0,imported:false};
let monthlyCommercialCache=null,monthlyCommercialCase="sale",monthlyCommercialLoading=false;
let digitalPaths=null,architectureOverrides=null,architectureCache={key:null},architectureRequestId=0;
let boot, result, activeView='atlas', overrides={}, requestId=0, allRecords=[], evidenceById=new Map(), comparisonResults=null, detailRequestId=0, activeTraceHash=null;
const viewNames = [
 ['atlas','01','Economic atlas'],['deployment','02','Market deployment'],['providers','03','Providers & systems'],
 ['improvement','04','Improvement'],['fleet','05','Fleet & bottlenecks'],['learning','06','Learning & coordination'],
 ['customer','07','Customer adoption'],['commercial','08','Business models'],['digital','09','Digital AI ecosystem'],
 ['analogy','10','Analogies & contributions'],['supply','11','Supply & production'],['embodiment','12','Embodiment & deployment'],
 ['evidence','13','Scenarios & evidence']
];
const controlGroups = [
 ['Capability & operating work',[
  ['capability','Initial capability threshold index',0,1,.01],['capability_progress','Annual capability increment',0,.10,.005],
  ['uptime','Technical uptime',0,1,.01],['intervention_minutes','Support minutes / robot hour',0,60,1],
  ['labor_avoidability','Released labor value avoided as cash',0,1,.05],['retirement_years','Service life, years',2,12,1]]],
 ['Digital baseline & learning',[
  ['digital_efficiency','Human time reduction',0,.6,.01],['coordination','Robot scheduling change (can worsen)',-.4,.6,.05],
  ['digital_cost_usd','Robot digital cost, USD/year',0,20000,500],['learning_transfer','Within-system transfer hypothesis',0,.15,.01],
  ['learning_cost_usd','Validation cash / system / year',0,500000,5000],['onboard_configuration','Embedded board configuration','select']]],
 ['Shared deployment resources',[
  ['integration_hours','Integration hours / shipped robot',0,1000,10],['integration_budget_hours','Shared integration hours/year',0,50000,200],
  ['support_budget_hours','Shared support hours/year',0,100000,500],['customer_capital_usd','Customer funding envelope/year',0,20000000,100000],
  ['provider_capital_usd','Provider funding envelope/year',0,20000000,100000],['customer_profile','Customer mechanisms','select'],
  ['arrangement','Robot commercial terms','select'],['price_multiplier','Contract price multiplier',.25,3,.05]]],
 ['Supply, qualification & target',[
  ['supply_multiplier','Accessible qualified receipts scale',0,10,.1],['qualification_delay','Qualification delay, years',0,10,1],
  ['expansion_delay','Expansion begins at year index',0,12,1],['assembly_yield','Final assembly yield (applied once)',.1,1,.05],
  ['spares_rate','Actuator spares / installed BOM / year',0,.5,.01],['target_active_stock','Backcast retained robot target',1,10000,1],
  ['target_year','Backcast target year index',2,14,1],['years','Scenario periods, years',3,15,1]]],
 ['Newco formation & competition',[
  ['newco_funding_usd','Entrant equity commitment assumption',0,10000000,50000],['demand_capture','Capturable demand scenario coefficient',0,1,.05],
  ['incumbent_response_month','Incumbent response, months',0,120,6],['demand_expansion','Additional demand / reference activity',0,1,.05],
  ['formation_route','Operating-company formation route','select']]]
];

function setText(id,value){$(id).textContent=value;}
function notice(text,info=false){return `<div class="notice ${info?'info':''}">${text}</div>`;}
function empty(text){return `<div class="empty">${esc(text)}</div>`;}
function metric(label,value,sub=''){return `<div class="card metric"><div class="label">${esc(label)}</div><div class="value">${value}</div><div class="sub">${esc(sub)}</div></div>`;}
function table(rows,columns){if(!rows.length)return empty('No records in this scope. Unknown is not zero.');return `<div class="table-wrap"><table><thead><tr>${columns.map(c=>`<th>${esc(c[1])}</th>`).join('')}</tr></thead><tbody>${rows.map(row=>`<tr>${columns.map(c=>`<td class="${c[3]?'number':''}">${c[2]?c[2](row[c[0]],row):fmt(row[c[0]],2)}</td>`).join('')}</tr>`).join('')}</tbody></table></div>`;}
function cellLabel(id){return boot.catalog.cells.find(x=>x.cell_id===id)?.label || id;}
function selectedCells(){return boot.catalog.cells.filter(x=>$('cell-filter').value==='all'||x.cell_id===$('cell-filter').value);}
function selectedRows(allYears=false){const ids=new Set(selectedCells().map(x=>x.cell_id));return result.fleet.cells.filter(x=>ids.has(x.cell_id)&&(allYears||x.year===Number($('year-filter').value)));}
function selectedJoint(){const ids=new Set(selectedCells().map(x=>x.cell_id));return result.joint_by_year.find(y=>y.year===Number($('year-filter').value)).comparisons.filter(x=>ids.has(x.cell_id));}
function sum(rows,key){return rows.reduce((n,x)=>n+(x[key]||0),0);}
function scopeName(){return $('cell-filter').value==='all'?'Six illustrative cells':cellLabel($('cell-filter').value);}
function bars(values){const max=Math.max(1,...values.map(x=>x[1]));return values.map(([name,v])=>`<div class="bar-row"><span>${esc(title(name))}</span><div class="bar-track"><div class="bar-fill" style="width:${Math.max(0,v/max*100)}%"></div></div><span class="bar-value">${fmt(v)}</span></div>`).join('');}
function chart(rows,xKey,series){
 if(!rows.length)return empty('No modeled periods.');
 const w=820,h=240,left=60,right=20,top=20,bottom=35;
 const all=rows.flatMap(r=>series.map(s=>Number(r[s[0]])||0));const min=Math.min(0,...all),max=Math.max(1,...all),span=max-min;
 const xx=i=>left+i*(w-left-right)/Math.max(1,rows.length-1), yy=v=>h-bottom-(v-min)/span*(h-top-bottom);
 let svg=`<svg class="chart" viewBox="0 0 ${w} ${h}" role="img" aria-label="${esc(series.map(s=>s[1]).join(', '))}">`;
 for(let n=0;n<=4;n++){const value=min+span*n/4;svg+=`<line x1="${left}" x2="${w-right}" y1="${yy(value)}" y2="${yy(value)}" stroke="#dde6df"/><text x="${left-8}" y="${yy(value)+4}" text-anchor="end">${fmt(value)}</text>`;}
 rows.forEach((r,i)=>{if(i%Math.max(1,Math.floor(rows.length/9))===0||i===rows.length-1)svg+=`<text x="${xx(i)}" y="${h-8}" text-anchor="middle">${esc(r[xKey])}</text>`;});
 for(const [key,label,color]of series){svg+=`<polyline fill="none" stroke="${color}" stroke-width="2.5" points="${rows.map((r,i)=>xx(i)+','+yy(Number(r[key])||0)).join(' ')}"/>`;}
 svg+='</svg><div class="legend">'+series.map(s=>`<span><b style="background:${s[2]}"></b>${esc(s[1])}</span>`).join('')+'</div>';return svg;
}
function scopedTimeline(){return result.fleet.years.map(y=>{const rows=selectedRows(true).filter(x=>x.year===y.year);return {year:y.year,active_stock:sum(rows,'active_stock'),commissioned:sum(rows,'commissioned'),retired:sum(rows,'retired'),hours:sum(rows,'baseline_equivalent_hours'),capability:rows.length?sum(rows,'capability')/rows.length:0};});}
function refs(obj){const ids=new Set();const walk=x=>{if(Array.isArray(x))x.forEach(walk);else if(x&&typeof x==='object')Object.entries(x).forEach(([k,v])=>{if(/evidence_(ids|refs)$/.test(k)&&Array.isArray(v))v.filter(z=>typeof z==='string').forEach(z=>ids.add(z));else if(k==='evidence_id'&&typeof v==='string')ids.add(v);else if(typeof v==='object')walk(v);});};walk(obj);return [...ids];}
function refButtons(obj){return refs(obj).map(id=>`<button class="ref" data-evidence="${esc(id)}">${esc(id)} ↗</button>`).join('');}
function recordId(r){return r.evidence_id||r.cell_id||r.system_id||r.analogy_id||r.contribution_id||r.artifact_id||r.deployment_id||r.benchmark_id||r.id||Object.entries(r).find(([k,v])=>k.endsWith('_id')&&typeof v==='string')?.[1]||'Record';}
function recordStatus(r){return r.epistemic_status||r.evidence_status||r.status||r.deployment_phase||r.phase||r.source_class||'Status in record';}
function recordTitle(r){return r.label||r.title||r.name||r.claim||r.mechanism||r.case_name||r.system_name||r.product||recordId(r);}
function recordCellIds(r){const text=JSON.stringify(r);return boot.catalog.cells.filter(c=>text.includes(c.cell_id)||r.market_id===c.market_id||(Array.isArray(r.market_ids)&&r.market_ids.includes(c.market_id))).map(c=>c.cell_id);}
function facetSelections(){return Object.fromEntries(EvidenceFacets.definitions.map(d=>[d.id,$('facet-'+d.id)?.value||'']));}
function recordMatches(r,key=''){const text=JSON.stringify(r).toLowerCase();const query=$('evidence-search').value.toLowerCase();const status=$('status-filter').value;const cell=$('cell-filter').value;const ids=recordCellIds(r);return (!query||text.includes(query))&&(status==='all'||text.includes(status.toLowerCase()))&&(cell==='all'||!ids.length||ids.includes(cell))&&EvidenceFacets.matches(r,facetSelections(),key);}
function cards(records,limit=30,applyFilters=true){const filtered=applyFilters?records.filter(r=>recordMatches(r.value,r.key)):records;if(!filtered.length)return empty('No source objects match the scope. The relevant evidence may be missing or supplied in another package.');return `${filtered.length>limit?notice(`Showing ${limit} of ${filtered.length} records. Narrow the evidence search for remaining records.`,true):''}<div class="grid">${filtered.slice(0,limit).map(({value:r,key,path})=>{const id=recordId(r),name=recordTitle(r),status=recordStatus(r),urls=[...new Set([r.url||r.source_url,...(Array.isArray(r.urls)?r.urls:[])].map(safeURL).filter(Boolean))];const brief=r.summary||r.finding||r.interpretation||r.decision_implication||r.description||r.limitations;return `<article class="card record"><div class="id">${esc(id)} · ${esc(key)}</div><h3>${esc(typeof name==='string'?name:JSON.stringify(name))}</h3><span class="chip">${esc(typeof status==='string'?status:JSON.stringify(status))}</span>${!recordCellIds(r).length&&$('cell-filter').value!=='all'?'<p class="reference-badge">Reference record; no explicit link to the selected cell.</p>':''}${brief?`<p>${esc(typeof brief==='string'?brief:JSON.stringify(brief))}</p>`:''}<div>${refButtons(r)}</div><div class="small"><a href="/${esc(path)}" target="_blank">Saved record package ↗</a>${urls.map((url,i)=>` · <a href="${esc(url)}" target="_blank" rel="noopener">Primary source${urls.length>1?' '+(i+1):''} ↗</a>`).join('')}</div><details><summary>Inspect full record, dates and limits</summary><pre>${esc(JSON.stringify(r,null,2))}</pre></details></article>`;}).join('')}</div>`;}
function recordsFor(pattern,packagePattern=null){return allRecords.filter(r=>pattern.test(r.key)&&(!packagePattern||packagePattern.test(r.path)));}
function evidenceSection(pattern,packagePattern=null,limit=20){return cards(recordsFor(pattern,packagePattern),limit);}
function docs(pattern){const paths=boot.documents.filter(x=>pattern.test(x));return `<div class="links">${paths.map(x=>`<a href="/${esc(x)}" target="_blank">${esc(title(x.split('/').pop().replace('.md','')))} ↗</a>`).join('')}</div>`;}
function decisionContext(){
 const packet=boot.evidence_packages.find(p=>p.path==='data/market_evidence.json')?.data;
 if(!packet?.decision_packs)return '';
 const selected=new Set(selectedCells().map(c=>c.cell_id));
 const reviews=packet.decision_reassessment.filter(r=>selected.has(r.cell_id));
 const packs=packet.decision_packs.filter(p=>selected.has(p.cell_id));
 return `<section id="decision-context" class="card"><h3>Deployment and entry decisions · provisional</h3><p>Six-cell reassessment and three service-specific decision packs. Decision gates follow the selected cell; evidence search filters source cards. Full costs, payroll effects and integrated counterfactuals are still incomplete.</p><p class="small">Current execution: eligible data, funded trials, compatible module delivery and finite support now gate a hypothetical workcell improvement. No-learning retains research cost; no-transfer preserves old cohorts. Earlier scenarios remain unchanged. <a href="/research/learning_execution.md" target="_blank">Learning and qualification findings ↗</a></p><p class="small">Supported expansion: new requests, qualified units, announced capacity, actual service and each payer’s cash now share a bounded admission test. A recurring-support reserve does not guarantee commissioning. <a href="/research/support_expansion.md" target="_blank">Expansion findings ↗</a></p><p class="small">Customer renewal: funded capacity, locked prices and prior service now determine a bounded entry window. A first cash crossing can reverse; customer retention cannot guarantee delivery. <a href="/research/competitive_renewals.md" target="_blank">Renewal findings ↗</a></p><p class="small">Commercial evidence: operating rollout, negotiated value and provider funding require separate demonstrations. Planned generation changes and gross financing do not close service or cash gates. <a href="/research/commercial_disclosure_boundaries.md" target="_blank">Disclosure audit ↗</a></p><p class="small">Hospital continuity: installation, eligible maintenance, repair remedies and funded fallback are separate obligations. Catalog components and an award value do not establish accepted service or current site economics. <a href="/research/hospital_support_contracts.md" target="_blank">Support and exit evidence ↗</a></p><details><summary>Inspect decisions for ${esc(scopeName())}</summary>`+
 table(reviews,[['cell_id','Cell',cellLabel],['selection','Current selection',esc],['reason','Decision value',esc],['strongest_counterargument','Strongest challenge',esc]])+
 packs.map(p=>`<article class="decision-pack" data-decision-id="${esc(p.decision_id)}"><h3>${esc(p.title)}</h3><p><b>Accepted service:</b> ${esc(p.accepted_service)}</p><p>${esc(p.recommendation)}</p>`+
 table(Object.entries(p.gates).map(([gate,condition])=>({gate,condition})),[['gate','Gate',title],['condition','Condition',esc]])+
 `<p><b>What reverses the decision:</b> ${esc(p.ranking_reversal)}</p><p>${esc(p.evidence_consequence)}</p>${refButtons(p)}<details><summary>Alternatives, retained work, cost boundaries and unknowns</summary>`+
 table(p.alternatives,[['alternative','Alternative',esc],['fit','Fit',esc],['retained_work','Retained work',esc],['qualification_limit','Limit',esc]])+
 `<pre>${esc(JSON.stringify({observation_contract:p.observation_contract,cash_and_resource_boundary:p.cash_and_resource_boundary,empirical_decision_metrics:p.empirical_decision_metrics,model_use:p.model_use,hospital_support_gate:p.hospital_support_gate,provider_contract_gate:p.provider_contract_gate,competitive_continuity_gate:p.competitive_continuity_gate,supported_expansion_gate:p.supported_expansion_gate,r_and_d_qualification_gate:p.r_and_d_qualification_gate},null,2))}</pre></details></article>`).join('')+
 `<p class="small"><a href="/research/deployment_entry_decisions.md" target="_blank">Decision analysis and required model bridges ↗</a> · <a href="/DEPLOYMENT_ENTRY_CAMPAIGN.md" target="_blank">Active campaign contract ↗</a></p></details></section>`;
}
function observedEstimate(q){if(q.value!==null)return fmt(q.value,1);if(q.comparison&&Number.isFinite(q.bound))return esc(q.comparison)+fmt(q.bound,2);return 'Not published';}
function physicalCrosswalk(){
 const packet=boot.observed_physical_requirements;
 if(!packet?.occupations)return '';
 const selected=$('cell-filter').value;
 const rows=packet.occupations.filter(r=>selected==='all'||r.cell_ids.includes(selected));
 return `<section id="physical-crosswalk"><h3 class="section-label">Observed physical requirements · selected occupations</h3>`+
  notice('ORS 2025 preliminary requirements and May 2025 OEWS employment have different populations. Matching occupation codes do not authorize employment × requirement percentages. Standing is workday duration; manipulation and reaching are worker incidence. No physical-hour or robot-addressability total is inferred.',true)+
  table(rows,[['soc_2018','SOC'],['occupation','Occupation',esc],['employment','OEWS jobs',q=>q.value===null?'No exact code':fmt(q.value),true],['requirements','Mean day standing, %',r=>observedEstimate(r.standing_mean.estimate),true],['requirements','Workers: fine manipulation, %',r=>observedEstimate(r.fine_manipulation.estimate),true],['requirements','Workers: overhead reach, %',r=>observedEstimate(r.reaching_overhead.estimate),true]])+
  `<details><summary>All seven requirements, uncertainty and source rows</summary>${rows.map(r=>`<h3>${esc(r.soc_2018+' '+r.occupation)}</h3>`+table(Object.values(r.requirements),[['label','Requirement',esc],['estimate','Estimate',observedEstimate],['estimate','Unit',q=>esc(q.unit)],['standard_error','Standard error, points',q=>q.measurement_status==='not_available'?'Unavailable':observedEstimate(q)],['source_row','Workbook row',v=>v===null?'No published row':fmt(v)]])+`<p class="small">${esc(r.join_status)}. Source footnotes and survey boundaries are retained in the saved package. ${refButtons(r)}</p>`).join('')}</details>`+
  `<div class="links">${refButtons({evidence_ids:['PRC-006','PRC-007']})}<a href="/research/physical_requirements_crosswalk.md" target="_blank">Crosswalk analysis ↗</a><a href="/data/physical_requirements_crosswalk.json" target="_blank">Saved requirements and source locators ↗</a></div></section>`;
}
function frontierActors(){return deploymentSourceChecks()+regionalSourceChecks()+`<section id="frontier-actors"><h3>Frontier model and deployment roles</h3>`+notice('Dated primary-source map. Lab, OEM, integrator, operator and transaction-counterparty roles can coexist. Releases, benchmarks, partnerships and productive fleets have separate evidence boundaries.',true)+docs(/frontier_models|generalist_dyna_deployment/)+evidenceSection(/^model_labs$/,/frontier_model_economics/,20)+`</section>`;}
function deploymentSourceChecks(){
 const checks=boot.observed_frontier_models?.deployment_source_checks;if(!checks||checks.status==='not_available_in_this_packet')return '';
 const n=checks.napkin_service;
 return `<section id="deployment-source-checks"><h3>Does reported output meet the customer's service target?</h3>`+
  notice('7 November continuation · Dyna-reported restaurant case. Source arithmetic is separate from the synthetic scenarios. Contract price, support costs and paid staffing changes remain unknown.',true)+
  table([n],[['reported_folds_per_hour','Reported folds / hour',v=>fmt(v),true],['reported_quality_percent','Accepted quality',v=>fmt(v,1)+'%',true],['reported_window_hours','Window, hours',v=>fmt(v),true],['required_accepted_napkins','Required napkins',v=>fmt(v),true],['arithmetic_accepted_per_window','Rate × quality × hours',v=>fmt(v,1),true],['surplus_as_percent_of_required_output','Above requirement',v=>fmt(v,2)+'%',true]])+
  `<p>The source rounds output to ${fmt(n.reported_accepted_napkins)}. The resulting margin is a capacity comparison; financial ROI is unknown. ${refButtons({evidence_ids:n.evidence_ids})}</p>`+
  `<details><summary>Inspect the conditional time margin</summary><p>At the stated rate and quality, the target requires ${fmt(n.conditional_effective_hours_required,2)} effective hours, leaving ${fmt(n.conditional_additional_time_loss_budget_hours,2)} hours. ${esc(n.time_sensitivity_condition)} Applying another uptime factor to a rate that already includes stops would count the same loss twice.</p></details>`+
  `<h4>Scores retain their original meaning</h4><p>Dyna's robot-scale average rises ${checks.dyna_scaling.rungs.map(r=>fmt(r.reported_percent_of_task_ceiling)+'%').join(' → ')} of heterogeneous task ceilings after robot post-training. Its language-following scores include half-credit failures. Neither measure is a whole-job probability. ${refButtons({evidence_ids:['K-E035','K-E037']})}</p>`+
  `<p>Generalist's GEN-1.5 reports fast adaptation on short tasks; a public waitlist does not establish a qualified service contract. ${refButtons({evidence_ids:['K-E031','K-E033']})}</p><a href="/research/generalist_dyna_deployment.md" target="_blank">Generalist, Dyna and customer evidence ↗</a></section>`;
}
function regionalSourceChecks(){
 const source=boot.observed_frontier_models,checks=source?.regional_source_checks;if(!checks||checks.status==='not_available_in_this_packet')return '';
 const conflict=checks.rldx_table9,latency=checks.rldx_latency;
 const rows=conflict.rows.map(x=>({...x,counts:`${x.printed_counts.full} / ${x.printed_counts.partial} / ${x.printed_counts.fail}`}));
 return `<section id="regional-source-checks"><h3>What the reported model results establish</h3>`+notice('Source arithmetic and protocol checks. These tables do not execute a policy, rank models across different tasks, or calibrate the economic scenarios.')+
  `<h4>RLDX Table 9 · unresolved count/score reconciliation</h4><p>The original PDF and HTML give trial counts that do not reproduce the printed score totals under the stated 1 / 0.5 / 0 rule. A corrected measured effect is unknown. ${refButtons({evidence_ids:['K-E030']})}</p>`+
  table(rows,[['condition','Condition',v=>esc(title(v))],['counts','Full / partial / fail',esc],['trials','Trials',v=>fmt(v),true],['score_from_printed_counts_and_rule','Score from counts and rule',v=>fmt(v,2),true],['printed_score','Printed score',v=>fmt(v,2),true],['printed_percent','Printed percent',v=>fmt(v,1)+'%',true]])+
  `<h4>RynnBrain · complete-task success and subtask progress</h4>`+table(checks.rynn_trials.regimes,[['regime','Training regime',v=>esc(title(v))],['reported_final_success_percent','Final success',v=>fmt(v,2)+'%',true],['reported_process_percent','Process score',v=>fmt(v,2)+'%',true],['full_completions_implied_by_percentages','Implied full completions',v=>fmt(v),true],['protocol_trials','Protocol trials',v=>fmt(v),true]])+
  `<p class="small">${esc(checks.rynn_trials.scope)} ${refButtons({evidence_ids:['K-E028','K-E029']})}</p>`+
  `<p><strong>RLDX ALLEX:</strong> its ${fmt(checks.allex.reported_mean,1)} mean combines binary task measures and graded progress, so it is not a complete-job probability. ${refButtons({evidence_ids:['K-E016']})}</p>`+
  `<p><strong>RLDX reported desktop p50:</strong> ${fmt(latency.eager_p50_ms,2)} to ${fmt(latency.optimized_p50_ms,2)} ms (${fmt(latency.recomputed_ratio,2)}×) on ${esc(latency.hardware)}. ${esc(latency.scope)} ${refButtons({evidence_ids:['K-E017']})}</p><a href="/research/regional_frontier_models.md" target="_blank">Regional source analysis and limits ↗</a></section>`;
}
function regionalRights(){
 const rows=recordsFor(/^model_rights_cards$/,/frontier_model_economics/).map(x=>x.value).filter(x=>x.public_grant);
 if(!rows.length)return '';
 return `<section id="regional-rights"><h3>Rights attach to particular artifacts</h3>`+notice('Public code, model weights, datasets, controllers and private service agreements have different scopes. Noncommercial public grants do not disclose private enterprise permission or price.',true)+
  table(rows,[['label','Artifact',esc],['openness_layer','Layer',v=>esc(title(v))],['license','Inspected declaration',esc],['public_grant','Public scope',v=>esc(title(v))],['evidence_ids','Sources',v=>refButtons({evidence_ids:v})]])+
  `<p class="small">The exact evaluated RynnBrain-VLA policy is not identified by the inspected base-model release cards. Existing Unitree WMA/SDK records retain their own source identities. These observations change no synthetic cost or capability input.</p></section>`;
}
function regionalDeployments(){
 return `<section id="regional-deployments"><h3>Operator use, model partnership and future plans</h3>`+notice('Packing, hotel data capture, laundry and restaurant references concern different services from the synthetic floor-service market. Repeated announcements are one event; partner names or a model family do not identify an executed checkpoint.',true)+evidenceSection(/^deployment_cards$/,/frontier_model_economics/,4)+`</section>`;
}
function hospitalSupportPanel(){
 const entry=recordsFor(/^disclosure_audits$/,/customer_evidence/).find(x=>x.value.audit_id==='FG-AUDIT-02');
 if(!entry)return '';
 const a=entry.value,heading='<section id="hospital-support-contracts"><h3>Who keeps hospital deliveries running during repair?</h3>';
 if(!recordMatches(a,entry.key))return heading+empty('The hospital support audit is outside the current evidence filters. Clear filters to inspect it.')+'</section>';
 const source=evidenceById.get(a.catalog_evidence_id)?.value, award=evidenceById.get(a.award_evidence_id)?.value;
 const prices=source?.quantities||[], awardRow=award?.quantities||[];
 const cols=[['label','Disclosed item',esc],['value','Amount',v=>fmt(v,2),true],['unit','Currency and unit',esc],['denominator','Scope',esc]];
 return heading+notice(a.summary,true)+`<p>${esc(a.catalog_boundary)} ${refButtons(a)}</p>`+
 table(a.gates,[['gate','Decision gate',esc],['finding','Source consequence',esc]])+
 `<details><summary>Inspect schedule line items and the separate award</summary>`+table(prices,cols)+
 `<p>Separate UK buyer award; no annualization, currency conversion or per-robot division.</p>`+table(awardRow,cols)+`<p>${esc(award?.limitations||'')}</p></details>`+
 `<details><summary>Keep seven missing economic and service outcomes explicit</summary>`+
 table(Object.entries(a.unknowns).map(([key,v])=>({label:title(key),...v})),[['label','Outcome',esc],['value','Estimate',fmt],['reason','Missing evidence',esc]])+`</details>`+
 `<p><a href="/research/hospital_support_contracts.md" target="_blank">Hospital support and exit analysis ↗</a></p></section>`;
}

function commercialDisclosurePanel(){
 const entry=recordsFor(/^disclosure_audits$/,/customer_evidence/).find(x=>x.value.audit_id==='FG-AUDIT-01');
 const r=boot.observed_research_summary?.commercial_disclosures;
 if(!entry||!r)return '';
 const a=entry.value;
 const heading='<section id="commercial-disclosures"><h3>Operating rollout, contract value and provider funding</h3>';
 if(!recordMatches(a,entry.key))return heading+empty('The tote-workflow source audit is outside the current evidence filters. Clear filters to inspect it.')+'</section>';
 return heading+notice('Dated public-source audit. Management planning assumptions, historical company accounts and achieved site service remain separate. These figures do not change with synthetic scenario controls.',true)+
  `<p>${esc(a.summary)} ${refButtons(a)}</p>`+
  table([['Operating acceptance',a.service_gate],['Customer contract',a.contract_gate],['Provider funding',a.provider_gate],['Digital qualification',a.digital_gate]].map(([gate,meaning])=>({gate,meaning})),[['gate','Gate',esc],['meaning','What decides it',esc]])+
  `<details><summary>Reproduce disclosed payment and cost components</summary>`+
  table(Object.values(r.calculations),[['label','Calculation',esc],['value','USD',money,true],['formula','Equation',esc],['scope','Boundary',esc]])+
  `<p>${esc(r.rounding_boundary)}</p><pre>${esc(JSON.stringify(r.calculations,null,2))}</pre></details>`+
  `<details><summary>Keep company losses and operating cash use distinct</summary>`+
  table(r.financial_periods,[['period','Agility standalone period',esc],['net_sales','Net sales, USD',money,true],['cost_of_goods_sold','COGS, USD',money,true],['gross_result','Gross result, USD',money,true],['net_result','Net result, USD',money,true],['operating_cash_flow','Operating cash flow, USD',money,true]])+
  `<p>Negative values are losses or cash outflows. Unequal periods are not annualized or allocated per robot. The later completed financing is distinct from this historical operating record. ${refButtons({evidence_ids:['FG-E021','FG-E022']})}</p></details>`+
  `<details><summary>Unresolved operating and financial outcomes</summary>`+
  table(Object.entries(r.unknowns).map(([key,x])=>({label:title(key),...x})),[['label','Outcome',esc],['value','Estimate',fmt],['reason','Missing evidence',esc]])+'</details>'+
  `<p><a href="/research/commercial_disclosure_boundaries.md" target="_blank">Decision analysis and source boundaries ↗</a> · <a href="/model/results/observed_research_summary.json" target="_blank">Reproduced source arithmetic ↗</a></p></section>`;
}

function napkinComparison(){
 const entry=recordsFor(/^comparisons$/,/customer_evidence/).find(x=>x.value.comparison_id==='FG-CMP-03');
 if(!entry)return '';
 const c=entry.value;
 if(!recordMatches(c,entry.key))return `<section id="napkin-comparison"><h3>Restaurant napkin workflow</h3>${empty('The M09 reference comparison is outside the current evidence filters. Clear filters to inspect it.')}</section>`;
 return `<section id="napkin-comparison"><h3>Restaurant napkin workflow: what must actually be delivered?</h3>`+
  notice('M09 hospitality/foodservice source reference, outside the six synthetic cells. A proposed matched-service protocol; no observed cost ranking. Annual cell/year and scenario controls do not alter this evidence.',true)+
  `<p><strong>Service unit:</strong> ${esc(c.service_unit)}</p><p>${esc(c.summary)}</p>`+
  table(c.alternatives,[['label','Alternative',esc],['feeding','Loading and input work',esc],['quality_handoff','Acceptance and handoff',esc],['retained_work','Other work to measure',esc],['unknown','Unresolved',esc]])+
  `<p class="small">The employer base rate describes a bundled job. BETA's maximum item rate has a different, unqualified denominator from Dyna's accepted-output arithmetic. Neither is a payroll-saving coefficient. ${refButtons(c)}</p>`+
  `<details><summary>Match the service and measure the whole workflow</summary><ul>${c.fixed_baseline.map(x=>`<li>${esc(x)}</li>`).join('')}</ul><ol>${c.measurement_protocol.map(x=>`<li>${esc(x)}</li>`).join('')}</ol><p>${esc(c.source_arithmetic.clock_boundary)}</p></details>`+
  `<details><summary>Separate task time, capacity and paid labor</summary>`+
  table(c.labor_outcomes,[['outcome','Outcome',esc],['proof_needed','Evidence required',esc]])+`</details>`+
  `<details><summary>Whose cash and which resources?</summary>`+
  table(c.accounting_boundaries,[['perspective','Boundary',esc],['include','Include and reconcile',esc]])+
  table(Object.entries(c.economic_outcomes).map(([name,x])=>({name:name==='roi'?'ROI':title(name),...x})),[['name','Estimate',esc],['value','Result',v=>fmt(v)],['reason','Why unavailable',esc]])+`</details>`+
  `<p><a href="/research/customer_value.md#restaurant-napkin-workflow-comparison" target="_blank">Full comparison and entry implications ↗</a> · <a href="/data/customer_evidence.json" target="_blank">Saved FG-CMP-03 record ↗</a></p></section>`;
}

function calendarBridgePanel(){
 const state=bridgeState;
 if(!state.data&&!state.loading&&!state.error){state.loading=true;fetch('/api/calendar-bridge').then(async response=>{const data=await response.json();if(!response.ok)throw Error(data.error||'Calendar execution unavailable');state.data=data;state.inputs=data.case_inputs[state.selection];}).catch(error=>state.error=error.message).finally(()=>{state.loading=false;if(activeView==='customer')render();});}
 const opening='<section id="calendar-bridge"><h3>Annual digital paths inside monthly execution</h3>';
 if(!state.data)return opening+empty(state.error||'Calculating calendar and cohort execution…')+'</section>';
 const r=state.current||state.data.cases[state.selection],b=r.calendar_bridge,p=b.annual_parameters,x=state.inputs||state.data.case_inputs[state.selection],number=v=>v.numerator/v.denominator,cents=v=>'$'+fmt(v/100,2);
 const total=r.enterprise.months.reduce((n,m)=>n+number(m.total_delivered_units),0),hours=b.months.flatMap(m=>m.human_work).reduce((n,h)=>n+number(h.retained_human_task_hours),0),committed=b.months.flatMap(m=>m.human_work).reduce((n,h)=>n+h.staff_commitment_cents,0),paid=b.months.flatMap(m=>m.human_work).reduce((n,h)=>n+h.current_period_staff_cash_paid_cents,0);
 const basic=[['start_year','Start year','integer'],['start_month','Start calendar month','integer'],['support_hours_per_month','Allocated support / upgrade hours per month','integer'],['integration_hours_per_month','Allocated integration hours per month','integer'],['upgrade_cost_cents_per_robot','Qualification per changed robot, USD','money'],['upgrade_hours_per_robot','Qualification hours per changed robot','integer']];
 const finance=[['entrant_cash_cents','Entrant opening cash, USD','money'],['loan_cents','Entrant term loan, USD','money'],['maturity_month','Loan maturity month','integer']];
 const fields=(list,group)=>list.map(([key,label,kind])=>`<label>${esc(label)}<input data-bridge-group="${group}" data-bridge-key="${key}" data-bridge-kind="${kind}" type="number" min="0" step="${kind==='money'?'.01':'1'}" value="${kind==='money'?x[group][key]/100:x[group][key]}"></label>`).join('');
 const controls=state.imported?'<p>Complete saved unit, calendar, cohort and Treasury inputs were replayed. Select a standard witness to edit shortcut assumptions.</p>':`<details><summary>Edit calendar, annual paths and funding</summary><div class="grid">${fields(basic,'bridge_inputs')}${fields(finance,'finance_inputs')}<label>Software policy<select data-bridge-key="software_policy" data-bridge-group="bridge_inputs" data-bridge-kind="choice">${['paid_calendar_upgrade','frozen_cohort'].map(v=>`<option value="${v}" ${x.bridge_inputs.software_policy===v?'selected':''}>${esc(title(v))}</option>`).join('')}</select></label>${[['capability','Initial capability'],['capability_progress','Annual capability increment']].map(([key,label])=>`<label>${esc(label)}<input data-bridge-group="annual" data-bridge-key="${key}" data-bridge-kind="number" type="number" step=".01" value="${p[key]}"></label>`).join('')}${[['digital_efficiency','Annual human digital efficiency'],['coordination','Annual robot coordination'],['digital_cost_usd','Annual robot digital cost, USD']].map(([key,label])=>`<label>${esc(label)} (${p.years} comma-separated levels)<input data-bridge-group="path" data-bridge-key="${key}" data-bridge-kind="series" value="${b.resolved_digital_paths[key].join(', ')}"></label>`).join('')}</div><label><input data-bridge-group="bridge_inputs" data-bridge-key="digital_enabled" data-bridge-kind="boolean" type="checkbox" ${x.bridge_inputs.digital_enabled?'checked':''}> Additional digital tools enabled</label><label><input data-bridge-group="root" data-bridge-key="human_only" data-bridge-kind="boolean" type="checkbox" ${x.human_only?'checked':''}> Human-only physical plan, with the same paid staff and customer moves</label><p><button id="apply-calendar">Apply calendar execution</button></p></details>`;
 const months=b.months.map((m,i)=>({month:m.month,date:m.calendar_year+'-'+String(m.calendar_month).padStart(2,'0'),service:number(r.enterprise.months[i].total_delivered_units),supported:m.cohorts.length,upgrades:m.cohorts.filter(c=>c.upgrade_performed).length,support:number(m.support_hours_used),qualification:number(m.qualification_hours_used),integration:number(m.integration_hours_used),cash:r.months[i].closing_cash_cents.entrant}));
 return opening+notice('Synthetic matched cleaning-zone contract. Annual digital levels now affect actual supported monthly cohorts and funded invoices. Historical floor bundles have no inferred conversion. A separate funded four-architecture comparison is available in Business models. A separate bounded conventional courier comparator is available in Learning & coordination; its service units are not pooled with cleaning zones.')+`<label>Calendar witness<select id="calendar-case">${Object.keys(state.data.cases).map(k=>`<option value="${k}" ${state.selection===k?'selected':''}>${esc(title(k))}</option>`).join('')}${['custom','imported'].includes(state.selection)?`<option value="${state.selection}" selected>${state.imported?'Imported replay':'Custom assumptions'}</option>`:''}</select></label>`+controls+
 `<p id="calendar-input-state" class="small" role="status">${esc(state.error||'Results and exports use the last applied case. All unit, cost and qualification mappings are synthetic assumptions.')}</p><div class="grid">${metric('Accepted cleaning zones',fmt(total,2),'Actual delivery summed over observed months')}${metric('Retained human task hours',fmt(hours,2),'Task time is distinct from paid shifts')}${metric('Staff committed / paid',cents(committed)+' / '+cents(paid),'No payroll removal is inferred')}</div>`+
 table(months,[['date','Calendar month',esc],['month','Execution month',v=>fmt(v)],['service','Accepted zones',v=>fmt(v,2),true],['supported','Supported robots',v=>fmt(v),true],['upgrades','Qualified upgrades',v=>fmt(v),true],['support','Support hours',v=>fmt(v,2),true],['qualification','Upgrade hours',v=>fmt(v,2),true],['integration','Integration hours',v=>fmt(v,2),true],['cash','Entrant cash',cents,true]])+
 `<details><summary>Calendar-year totals without extrapolation</summary>${table(b.calendar_years,[['calendar_year','Year',v=>String(v)],['whole_month_count','Observed months'],['accepted_cleaning_zones','Accepted zones',v=>fmt(number(v),2)],['supported_robot_months','Robot-months'],['supported_robot_year_equivalents','Robot-year equivalents',v=>fmt(number(v),3)]])}</details><details><summary>Trace unit, cost, cohort and resource mappings</summary>${table(b.metric_lineage,[['metric','Metric',esc],['equation','Equation / rule',esc],['inputs','Inputs',esc],['implementation','Calculation',esc],['basis','Boundary',esc]])}<pre>${esc(JSON.stringify({unit_contract:b.unit_contract,cost_and_resource_contract:b.cost_and_resource_contract,cohorts:b.months,charge_lines:b.charge_lines,source_sha256:r.source_sha256},null,2))}</pre></details><details><summary>Compare eight complete calendar worlds</summary>${table(state.data.summary,[['case','World',v=>esc(title(v))],['accepted_cleaning_zones','Accepted zones',v=>fmt(number(v),2)],['retained_human_task_hours','Human task hours',v=>fmt(number(v),2)],['staff_commitment_cents','Committed staff',cents],['external_physical_and_enterprise_cash_cents','External physical / operating outlays',cents],['upgrade_count','Upgrades']])}<p>${esc(state.data.comparison_boundary)}</p><pre>${esc(JSON.stringify(state.data.joint,null,2))}</pre></details><p><button id="export-calendar">Export calendar case</button> <label>Reload calendar case<input id="import-calendar" type="file" accept="application/json,.json"></label></p><p class="small">Case ${esc(r.case_hash.slice(0,14))}. <a href="/model/CALENDAR_BRIDGE.md" target="_blank">Methods and limitations ↗</a></p></section>`;
}

function buildCalendarEvents(){
 const fail=message=>{bridgeState.error=message+' Display and export retain the last valid case.';if($('calendar-input-state'))setText('calendar-input-state',bridgeState.error);};
 const calculate=async(body,selection,id)=>{
  if($('calendar-input-state'))setText('calendar-input-state','Calculating actual cohorts, annual paths and cash…');
  try{const response=await fetch('/api/calendar-bridge',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(body)}),data=await response.json();if(id!==bridgeState.requestId)return;if(!response.ok)throw Error(data.error||'Calendar calculation failed');bridgeState.current=data.result;bridgeState.inputs=data.inputs;bridgeState.selection=selection;bridgeState.imported=selection==='imported';bridgeState.error=body.saved_case&&body.saved_case.case_hash!==data.result.case_hash?'Replayed with current source or changed inputs; historical hash differs.':'';if(activeView==='customer')render();}catch(error){if(id===bridgeState.requestId)fail(error.message);}
 };
 document.addEventListener('click',e=>{
  if(e.target.id==='export-calendar'&&bridgeState.data){const r=bridgeState.current||bridgeState.data.cases[bridgeState.selection];download('calendar-execution-'+r.case_hash.slice(0,10)+'.json',JSON.stringify(r,null,2),'application/json');}
  if(e.target.id!=='apply-calendar')return;const id=++bridgeState.requestId;
  try{const inputs=JSON.parse(JSON.stringify(bridgeState.inputs)),r=bridgeState.current||bridgeState.data.cases[bridgeState.selection];inputs.bridge_inputs.annual_overrides={...inputs.bridge_inputs.annual_overrides};inputs.bridge_inputs.digital_paths={schema_version:'digital-annual-paths/0.1',base_year:r.calendar_bridge.resolved_digital_paths.base_year,epistemic_status:'synthetic_assumption'};
   for(const field of document.querySelectorAll('#calendar-bridge [data-bridge-key]')){const key=field.dataset.bridgeKey,kind=field.dataset.bridgeKind,group=field.dataset.bridgeGroup,raw=field.value.trim();let value;
    if(kind==='boolean')value=field.checked;else if(kind==='choice')value=raw;else if(kind==='series'){const parts=raw.split(',').map(v=>v.trim());if(parts.some(v=>v===''||!Number.isFinite(Number(v))))throw Error('Annual paths require finite comma-separated levels.');value=parts.map(Number);if(value.length!==r.calendar_bridge.annual_parameters.years)throw Error('Annual path length must match the saved annual horizon.');}
    else if(kind==='money'){if(!/^\d+(\.\d{1,2})?$/.test(raw))throw Error('Cash requires nonnegative USD with at most two decimals.');const parts=raw.split('.');value=Number(parts[0])*100+Number((parts[1]||'').padEnd(2,'0'));if(!Number.isSafeInteger(value))throw Error('Cash exceeds the exact integer range.');}
    else{if(raw===''||!Number.isFinite(Number(raw)))throw Error('A finite numeric value is required.');value=Number(raw);if(kind==='integer'&&!Number.isSafeInteger(value))throw Error('Calendar and resource fields require exact integers.');}
    if(group==='root')inputs[key]=value;else if(group==='path')inputs.bridge_inputs.digital_paths[key]=value;else if(group==='annual')inputs.bridge_inputs.annual_overrides[key]=value;else inputs[group][key]=value;
   }calculate({inputs},'custom',id);
  }catch(error){fail(error.message);}
 });
 document.addEventListener('change',async e=>{
  if(e.target.id==='calendar-case'&&bridgeState.data&&Object.hasOwn(bridgeState.data.cases,e.target.value)){++bridgeState.requestId;bridgeState.selection=e.target.value;bridgeState.inputs=bridgeState.data.case_inputs[e.target.value];bridgeState.current=null;bridgeState.imported=false;bridgeState.error='';render();}
  if(e.target.id==='import-calendar'){const id=++bridgeState.requestId;try{const file=e.target.files[0];if(!file)return;const saved=JSON.parse(await file.text());if(id===bridgeState.requestId)await calculate({saved_case:saved},'imported',id);}catch(error){if(id===bridgeState.requestId)fail('Import error: '+error.message);}}
 });
 document.addEventListener('input',e=>{if(e.target.dataset.bridgeKey&&$('calendar-input-state'))setText('calendar-input-state','Edits are pending. Apply to recompute; export retains the displayed case.');});
}

function financePanel(){
 const state=financeState;
 if(!state.data&&!state.loading&&!state.error){state.loading=true;fetch('/api/enterprise-finance').then(async response=>{const data=await response.json();if(!response.ok)throw Error(data.error||'Financed execution unavailable');state.data=data;state.inputs=data.case_inputs[state.selection];}).catch(error=>state.error=error.message).finally(()=>{state.loading=false;if(activeView==='customer')render();});}
 const opening=`<section id="enterprise-finance"><h3>Dated finance, service interruption and cash recovery</h3>`;
 if(!state.data)return opening+empty(state.error||'Calculating financed execution…')+'</section>';
 const r=state.current||state.data.cases[state.selection],f=r.finance,x=state.inputs||state.data.case_inputs[state.selection],c=f.consolidation;
 const focus=r.enterprise.inputs.businesses.find(b=>b.operator_id==='entrant')||r.enterprise.inputs.businesses[0];
 const header=opening+notice(esc(`Synthetic financed execution: ${r.plan.months} months in ${r.enterprise.inputs.market.work_id}. The monthly table follows operator ${focus.operator_id}; headline cash totals include all loans. Loans require funded counterparties. These floor-bundle witnesses retain their original unit; the calendar bridge uses a separately specified cleaning contract. The separate funded architecture comparison is available in Business models.`));
 const cents=v=>'$'+fmt(v/100,2),number=v=>v.numerator/v.denominator;
 const rows=f.months.map((m,i)=>{const loans=m.loans.filter(l=>l.borrower===focus.actor_id),sum=key=>loans.reduce((n,l)=>n+l[key],0),service=r.enterprise.months[i],entry=service.operators.find(o=>o.operator_id===focus.operator_id);return {month:m.month,service:number(entry.total_delivered_units),market:number(service.total_delivered_units),cash:r.months[i].closing_cash_cents[focus.actor_id],principal:sum('principal_outstanding_cents'),due:sum('principal_due_cents'),interest:sum('interest_due_cents'),halted:m.halted_actors.includes(focus.actor_id)};});
 const fields=[['entrant_cash_cents','Entrant opening cash, USD','money'],['loan_cents','Loan amount, USD','money'],['lender_cash_cents','Lender opening cash, USD','money'],['draw_month','Draw month (0–7)','integer'],['maturity_month','Maturity month (1–48)','integer'],['monthly_rate_basis_points','Monthly rate, basis points','integer'],['rescue_equity_cents','Scheduled rescue equity, USD','money'],['rescue_equity_month','Rescue month (0–7)','integer'],['incumbent_procurement_month','Incumbent procurement month','integer'],['reinvestment_reserve_cents','Cash retained after later starts, USD','money']];
 const selects=[['payment_priority','Payment order',['operations_then_debt','debt_then_operations']],['default_policy','After debt default',['suspend_until_cured','stop_permanently']],['principal_repayment_policy','Principal repayment',['partial_allowed','full_or_nothing']]];
 const controls=state.imported?'<p>Complete saved inputs were replayed. Choose a recorded witness to edit the standard controls; the imported full ledger remains exportable.</p>':`<details><summary>Edit dated finance assumptions</summary><div class="grid">${fields.map(([key,label,kind])=>`<label>${esc(label)}<input data-finance-key="${key}" data-finance-kind="${kind}" type="number" min="0" step="${kind==='money'?'.01':'1'}" value="${kind==='money'?x[key]/100:x[key]}"></label>`).join('')}${selects.map(([key,label,values])=>`<label>${esc(label)}<select data-finance-key="${key}" data-finance-kind="choice">${values.map(v=>`<option value="${v}" ${x[key]===v?'selected':''}>${esc(title(v))}</option>`).join('')}</select></label>`).join('')}<label>Customer-return attempt month<select data-finance-key="response_month" data-finance-kind="optional-integer"><option value="none" ${x.response_month===null?'selected':''}>No scheduled return</option>${Array.from({length:8},(_,i)=>`<option value="${i}" ${x.response_month===i?'selected':''}>${i}</option>`).join('')}</select></label></div>${[['delayed_receipts','Four-month collection lag for entrant work billed from month 3'],['later_start_candidate','Offer one additional paid assembly start in month 3']].map(([key,label])=>`<label><input type="checkbox" data-finance-key="${key}" data-finance-kind="boolean" ${x[key]?'checked':''}> ${esc(label)}</label>`).join('')}<p><button id="apply-finance">Apply financed execution</button></p></details>`;
 return header+`<label>Financing witness<select id="finance-case">${Object.keys(state.data.cases).map(k=>`<option value="${k}" ${state.selection===k?'selected':''}>${esc(title(k))}</option>`).join('')}${['custom','imported'].includes(state.selection)?`<option value="${state.selection}" selected>${state.imported?'Imported replay':'Custom assumptions'}</option>`:''}</select></label>`+controls+
 `<p id="finance-input-state" role="status" class="small">${esc(state.error||'Displayed/exported results use the last applied case. All rates and contract terms are assumptions.')}</p><div class="grid">${metric('Loan cash received',cents(c.loan_draw_cash_cents),'A commitment without lender funds supplies no cash')}${metric('Principal recovered / still owed',cents(c.principal_recovery_cash_cents)+' / '+cents(c.closing_principal_claim_cents),'Maturity outside the horizon leaves the claim outstanding')}${metric('First tracked operator debt default',Object.hasOwn(f.first_debt_default_month,focus.actor_id)?'Month '+f.first_debt_default_month[focus.actor_id]:'None','A stopped operator retains its assets, assignments and unpaid obligations')}</div>`+
 table(rows,[['month','Month',v=>fmt(v),true],['service','Tracked operator service',v=>fmt(v,2),true],['market','Whole market',v=>fmt(v,2),true],['cash','Operator cash',cents,true],['principal','Principal owed',cents,true],['due','Principal due',cents,true],['interest','Interest due',cents,true],['halted','Debt policy halts service',v=>v?'Yes':'No']])+
 `<details><summary>Trace equations, assumed inputs and payment policy</summary>${table(f.metric_lineage,[['metric','Metric',esc],['equation','Equation / rule',esc],['inputs','Input lineage',esc],['implementation','Calculation',esc],['basis','Evidence or assumption',esc]])}<pre>${esc(JSON.stringify({finance_inputs:f.inputs,interest_lines:f.interest_lines,consolidation:f.consolidation,source_sha256:r.source_sha256},null,2))}</pre></details><details><summary>Compare the ${state.data.summary.length} financed worlds</summary>`+
 table(state.data.summary,[['case','World',v=>esc(title(v))],['entrant_delivered_units','Entrant service',v=>fmt(number(v),2),true],['principal_recovered_cents','Principal recovered',cents,true],['principal_outstanding_cents','Principal still owed',cents,true],['total_started_robots','Starts',v=>fmt(v),true]])+
 `</details><details><summary>Full physical, customer, invoice, credit and cash replay</summary><pre>${esc(JSON.stringify(r,null,2))}</pre></details><p><button id="export-finance">Export financed case</button> <label>Reload financed case<input id="import-finance" type="file" accept="application/json,.json"></label></p><p class="small">Case ${esc(r.case_hash.slice(0,14))}. Cash recovery does not sell or repossess assets. Later starts are declared candidates, gated by actual funds and the reserve; no autonomous investment optimum is claimed. <a href="/model/ENTERPRISE_FINANCE.md" target="_blank">Methods and boundaries ↗</a></p></section>`;
}

function buildFinanceEvents(){
 const fail=message=>{financeState.error=message+' Display and export retain the last valid case.';if($('finance-input-state'))setText('finance-input-state',financeState.error);};
 const calculate=async(body,selection,id)=>{
  if($('finance-input-state'))setText('finance-input-state','Calculating dated finance and delivered service…');
  try{
   const response=await fetch('/api/enterprise-finance',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(body)}),data=await response.json();
   if(id!==financeState.requestId)return;
   if(!response.ok)throw Error(data.error||'Calculation failed');
   financeState.current=data.result;financeState.inputs=data.inputs;financeState.selection=selection;financeState.imported=selection==='imported';
   financeState.error=body.saved_case&&body.saved_case.case_hash!==data.result.case_hash?'Replayed with current source. The saved historical case hash differs.':'';
   if(activeView==='customer')render();
  }catch(error){if(id===financeState.requestId)fail(error.message);}
 };
 document.addEventListener('click',e=>{
  if(e.target.id==='export-finance'&&financeState.data){const r=financeState.current||financeState.data.cases[financeState.selection];download('financed-enterprise-'+r.case_hash.slice(0,10)+'.json',JSON.stringify(r,null,2),'application/json');}
  if(e.target.id!=='apply-finance')return;
  const id=++financeState.requestId;
  try{
   const inputs={};
   for(const field of document.querySelectorAll('#enterprise-finance [data-finance-key]')){
    const kind=field.dataset.financeKind,key=field.dataset.financeKey,raw=field.value.trim();
    if(kind==='boolean'){inputs[key]=field.checked;continue;}
    if(kind==='choice'){inputs[key]=raw;continue;}
    if(kind==='optional-integer'&&raw==='none'){inputs[key]=null;continue;}
    if(kind==='money'){
     if(!/^\d+(\.\d{1,2})?$/.test(raw))throw Error('Cash requires nonnegative USD with at most two decimals.');
     const parts=raw.split('.');inputs[key]=Number(parts[0])*100+Number((parts[1]||'').padEnd(2,'0'));
    }else{if(!/^\d+$/.test(raw))throw Error('Months and basis points require nonnegative integers.');inputs[key]=Number(raw);}
    if(!Number.isSafeInteger(inputs[key]))throw Error('Input exceeds the supported integer range.');
   }
   calculate({inputs},'custom',id);
  }catch(error){fail(error.message);}
 });
 document.addEventListener('change',async e=>{
  if(e.target.id==='finance-case'&&financeState.data&&Object.hasOwn(financeState.data.cases,e.target.value)){
   ++financeState.requestId;financeState.selection=e.target.value;financeState.inputs=financeState.data.case_inputs[e.target.value];financeState.current=null;financeState.error='';financeState.imported=false;render();
  }
  if(e.target.id==='import-finance'){
   const id=++financeState.requestId;
   try{const file=e.target.files[0];if(!file)return;const saved=JSON.parse(await file.text());if(id===financeState.requestId)await calculate({saved_case:saved},'imported',id);}
   catch(error){if(id===financeState.requestId)fail('Import error: '+error.message);}
  }
 });
 document.addEventListener('input',e=>{if(e.target.dataset.financeKey&&$('finance-input-state'))setText('finance-input-state','Edits are pending. Apply to recompute; export still contains the displayed case.');});
}

function sharedEnterprisePanel(){
 const state=enterpriseState;
 if(!state.data&&!state.loading&&!state.error){state.loading=true;fetch('/api/shared-enterprise').then(async response=>{const data=await response.json();if(!response.ok)throw Error(data.error||'Shared calculation unavailable');state.data=data;state.inputs=data.case_inputs[state.selection];}).catch(error=>state.error=error.message).finally(()=>{state.loading=false;if(activeView==='customer')render();});}
 const header=`<section id="shared-enterprise"><h3>One market, shared robots, funded delivery</h3>`+notice('Synthetic eight-month floor-service experiment. Incumbent and entrant share the same robot pool and accepted bundle definition. Customer assignments persist through failure; only delivered work creates a sales invoice, and only settlement creates cash. Annual cell/year controls do not change this separate market.');
 if(state.error&&!state.data)return header+empty(esc(state.error))+'</section>';
 if(!state.data)return header+'<p>Calculating shared-market witnesses…</p></section>';
 const data=state.data,r=state.current||data.cases[state.selection],e=r.enterprise,inputs=state.inputs||data.case_inputs[state.selection];
 const value=q=>q.numerator/q.denominator,cents=x=>'$'+fmt(x/100,2);
 const rows=e.months.map((m,i)=>{const entrant=m.operators.find(x=>x.operator_id==='entrant'),inc=m.operators.find(x=>x.operator_id==='incumbent'),physical=r.months[i],ep=physical.outputs.find(x=>x.operator_id==='entrant');return {month:m.month,total:value(m.total_delivered_units),incumbent:value(inc.total_delivered_units),entrant:value(entrant.total_delivered_units),baseline:e.inputs.market.baseline_units,installed:ep.assigned_installed,supported:ep.supported_units,cash:physical.closing_cash_cents.entrant,arrears:m.due_unpaid_by_actor_cents.entrant};});
 const outcome=e.business_outcomes.find(x=>x.actor_id==='entrant'),installed=rows.at(-1).installed,requested=r.plan.operators.find(x=>x.operator_id==='entrant').requested_additions;
 const openingCash=Object.fromEntries(r.opening_treasury.actors.map(a=>[a.actor_id,a.cash_cents]));
 const actorCash=r.closing_treasury.actors.map(a=>({...a,opening:openingCash[a.actor_id],change:a.cash_cents-openingCash[a.actor_id]}));
 const controls=`<div class="grid"><label>Entrant opening cash, USD<input id="enterprise-cash" type="number" min="0" step="0.01" value="${inputs.entrant_cash_cents/100}"></label><label>Extra equity commitment at month 0, USD<input id="enterprise-equity" type="number" min="0" step="0.01" value="${inputs.extra_equity_cents/100}"></label><label>Incumbent procurement month<input id="enterprise-procurement" type="number" min="0" max="7" step="1" value="${inputs.incumbent_procurement_month}"></label><label>Customer-return attempt month<select id="enterprise-response"><option value="none" ${inputs.response_month===null?'selected':''}>No scheduled return</option>${Array.from({length:8},(_,i)=>`<option value="${i}" ${inputs.response_month===i?'selected':''}>${i}</option>`).join('')}</select></label></div><label><input id="enterprise-lag" type="checkbox" ${inputs.delayed_receipts?'checked':''}> Four-month collection lag for entrant work billed from month 3</label><label><input id="enterprise-no-entry" type="checkbox" ${inputs.no_entry?'checked':''}> Incumbent-only alternative</label><p><button id="apply-enterprise">Apply shared-market assumptions</button> <button id="export-enterprise">Export this shared-market case</button></p><p id="enterprise-input-state" class="small" role="status">${esc(state.error||'Displayed results use the last applied assumptions. Apply edits before changing scope.')}</p>`;
 return header+`<label>Shared-market witness<select id="enterprise-case">${Object.keys(data.cases).map(k=>`<option value="${k}" ${state.selection===k?'selected':''}>${esc(title(k))}</option>`).join('')}${state.selection==='custom'?'<option value="custom" selected>Custom assumptions</option>':''}</select></label>`+controls+
  `<div class="grid">${metric('Entrant robot requests / installed',requested+' / '+installed,'Shared qualified stock and support determine actual delivery')}${metric('Entrant closing cash',cents(rows.at(-1).cash),'Bank balance after actual receipts and payments; not profit')}${metric('First failed payment',outcome.first_failed_payment_at?'Month '+outcome.first_failed_payment_at.month:'None','Due unpaid at close: '+cents(outcome.closing_due_unpaid_cents))}</div>`+
  `<div class="card"><h3>Delivered accepted bundles · one recurring market</h3>${chart(rows,'month',[['total','Combined delivery','#00796e'],['incumbent','Incumbent','#326c9c'],['entrant','Entrant','#b86020'],['baseline','Original served baseline','#82729d']])}</div>`+
  table(rows,[['month','Month',v=>fmt(v),true],['total','Market delivered',v=>fmt(v,2),true],['incumbent','Incumbent',v=>fmt(v,2),true],['entrant','Entrant',v=>fmt(v,2),true],['installed','Entrant installed',v=>fmt(v),true],['supported','Supported',v=>fmt(v),true],['cash','Entrant cash',cents,true],['arrears','Due unpaid',cents,true]])+
  `<p class="small">Actual equity received: ${cents(e.consolidation.equity_cash_received_cents)}. The investor must fund a commitment from its explicit cash. A customer-return attempt before capture can fail; there is no automatic switchback. Shared-case identity: ${esc(r.case_hash.slice(0,12))}.</p><details><summary>Who paid and received cash?</summary>`+table(actorCash,[['actor_id','Legal actor',v=>esc(title(v))],['opening','Opening cash',cents,true],['cash_cents','Closing cash',cents,true],['change','Cash change',cents,true],['available_cents','Spendable at close',cents,true]])+`<p class="small">Cash changes are not profits. Receivables, due/future obligations and asset title remain in the full ledger.</p></details><details><summary>Compare the eight recorded worlds</summary>`+table(data.summary,[['case','World',v=>esc(title(v))],['total_market_delivered_units','Market units / 8 months',v=>fmt(value(v),2),true],['entrant_delivered_units','Entrant units',v=>fmt(value(v),2),true],['entrant_installed_robots','Entrant installed',v=>fmt(v),true],['entrant_closing_cash_cents','Closing entrant cash',cents,true],['equity_received_cents','Added equity',cents,true]])+`</details><details><summary>Inspect customer assignments, physical identities, invoices and complete cash ledger</summary><pre>${esc(JSON.stringify(r,null,2))}</pre></details><p><a href="/model/SHARED_ENTERPRISE.md" target="_blank">Shared-market methods</a> · <a href="/research/shared_enterprise_finance.md" target="_blank">Findings and limits</a></p><p class="small">Human staffing is a paid fixed shift; less human work does not automatically remove payroll. New/unmet demand, commercial terms and funding are invented. Replay this export with scripts/export_enterprise.py --case downloaded-case.json --output replay.json; it is not an annual-scenario import.</p></section>`;
}

function monthlyCommercialPanel(){
 if(!monthlyCommercialCache&&!monthlyCommercialLoading){
  monthlyCommercialLoading=true;
  fetch('/api/monthly-commercial').then(async response=>{const data=await response.json();if(!response.ok)throw Error(data.error||'Monthly calculation unavailable');monthlyCommercialCache=data;}).catch(error=>{monthlyCommercialCache={error:error.message};}).finally(()=>{monthlyCommercialLoading=false;if(activeView==='commercial')render();});
 }
 const header=`<section id="monthly-commercial"><h3>Who funds the next physical step?</h3>`+notice('Fixed five-month synthetic plan: sale, independent lease and provider service use the same requested manufacture, transport, installation and support. Funding failures can change realized output. Annual assumptions and calendar filters do not change these witnesses. No end-market revenue or lifecycle profit is inferred.');
 if(!monthlyCommercialCache)return header+'<p>Calculating monthly commercial witnesses…</p></section>';
 if(monthlyCommercialCache.error)return header+empty(esc(monthlyCommercialCache.error))+'</section>';
 const data=monthlyCommercialCache,r=data.cases[monthlyCommercialCase],cents=v=>'$'+fmt(v/100,2),quantity=v=>fmt(v.numerator/v.denominator,2);
 const rows=data.summary.map(x=>({...x,output:quantity(x.total_accepted_output)}));
 const months=r.months.map(m=>({month:m.month,started:m.flows.started,shipped:m.flows.shipped,installed:m.closing_stock.installed,supported:m.support.used,output:m.outputs.reduce((a,o)=>a+o.accepted_output_units.numerator/o.accepted_output_units.denominator,0),provider:m.closing_cash_cents.provider,customer:m.closing_cash_cents.customer,lessor:m.closing_cash_cents.lessor}));
 const terms=r.commercial.contracts[0];
 const termText=terms.arrangement==='sale'?`Customer purchase: ${cents(terms.purchase_cents_per_robot)} per successful accepted-unit shipment.`:terms.arrangement==='lease'?`Lessor purchase: ${cents(terms.purchase_cents_per_robot)} per successful shipment. Customer rent: ${cents(terms.rent_cents_per_robot_month)} per installed robot-month, including commissioning.`:`Provider retains title. Availability fee: ${cents(terms.service_cents_per_supported_month)} per supported robot-month; collection lag ${terms.service_collection_lag_months} month(s).`;
 const depositText=terms.deposit_cents?` Security deposit: ${cents(terms.deposit_cents)}, ${terms.deposit_restricted?'restricted':'spendable'} and refundable.`:' No security deposit.';
 const cancelText=terms.cancel_month===null?'':` Cancellation requested in month ${terms.cancel_month}; spent manufacturing cash is not reversed.`;
 return header+table(rows,[['case','Witness',v=>esc(title(v))],['output','Accepted units',esc,true],['external_physical_outlay_cents','Physical vendor outlay',cents,true],['outstanding_invoices_cents','Unpaid invoices',cents,true],['outstanding_refunds_cents','Refund liabilities',cents,true]])+
  `<p class="small">Unpaid invoices include receivables not yet due; the full ledger distinguishes dates and arrears. Cash columns show bank balances; restrictions and spendable cash are recorded for every month.</p><label>Inspect monthly witness <select id="monthly-commercial-case">${Object.keys(data.cases).map(k=>`<option value="${esc(k)}" ${k===monthlyCommercialCase?'selected':''}>${esc(title(k))}</option>`).join('')}</select></label>`+
  `<p>Arrangement: <strong>${esc(title(terms.arrangement))}</strong>. ${termText}${depositText}${cancelText}</p>`+
  table(months,[['month','Month',v=>fmt(v),true],['started','Starts',v=>fmt(v),true],['shipped','Shipped',v=>fmt(v),true],['installed','Installed',v=>fmt(v),true],['supported','Supported',v=>fmt(v),true],['output','Accepted units',v=>fmt(v),true],['provider','Provider cash',cents,true],['customer','Customer cash',cents,true],['lessor','Lessor cash',cents,true]])+
  `<h4>Closing title and custody</h4>`+table(r.commercial.months.at(-1).assets,[['unit_id','Robot',esc],['physical_state','State',esc],['title_owner','Title owner',esc],['custodian','Custodian',esc],['workflow_authority','Workflow authority',v=>v?esc(v):'None'],['supported','Supported this month',v=>v?'Yes':'No']])+
  `<details><summary>Inspect blocked actions, contracts and complete financial / physical ledgers</summary><pre>${esc(JSON.stringify(r,null,2))}</pre></details><p><a href="/model/MONTHLY_COMMERCIAL.md" target="_blank">Methods and exclusions</a> · <a href="/research/monthly_commercial_finance.md" target="_blank">Interpretation</a></p><button id="export-monthly-commercial">Export this monthly case</button><p class="small">Replay with scripts/export_monthly_commercial.py --case downloaded-case.json --output replay.json. These cases are separate from annual scenario import.</p></section>`;
}

function frontierArchitectures(){
 const packet=boot.observed_frontier_models;if(!packet?.transaction)return '';
 const t=packet.transaction;
 return architecturePanel()+`<section id="frontier-architectures"><h3>Observed model-layer evidence · target costs unresolved</h3>`+
  notice('These are four design alternatives for the manufacturing material-presentation cell. Compatible service and full costs are not established; the conditional calculator above uses separate assumptions and establishes no real-vendor ranking. Synthetic controls do not change these observed records.')+
  evidenceSection(/^architecture_alternatives$/,/frontier_model_economics/,4)+
  `<h3>Observed transaction disclosure · separate from scenario cash</h3><p>Robotics-business sale completed ${esc(t.completion_date)}; announced ${esc(t.announcement_date)}. USD millions, seller disclosure.</p>`+
  table([{item:'Cash consideration',amount:t.cash_consideration},{item:'Equity investment fair value',amount:t.equity_fair_value},{item:'Indemnification escrow fair value',amount:t.escrow_fair_value},{item:'Reported total consideration',amount:t.total_consideration},{item:'Reported net assets sold',amount:t.net_assets_sold},{item:'Reported seller gain',amount:t.seller_gain}],[['item','Item'],['amount','USD millions',v=>fmt(v),true]])+
  `<p>${esc(t.boundary)} ${refButtons(t)}</p></section>`;
}
function architectureScope(){return {cell_id:$('cell-filter').value==='all'?boot.catalog.cells[0].cell_id:$('cell-filter').value,year:Number($('year-filter').value)};}
function architectureKey(){const s=architectureScope();return result.scenario_hash+'|'+s.cell_id+'|'+s.year;}
async function loadArchitecture(key){
 const id=++architectureRequestId,snapshot=result,scope=architectureScope();
 try{
  const response=await fetch('/api/architectures',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({preset:snapshot.preset,overrides:snapshot.parameters,digital_paths:snapshot.digital_paths,architecture_overrides:snapshot.architecture_parameters,...scope})});
  const data=await response.json();if(id!==architectureRequestId||key!==architectureKey())return;
  if(!response.ok)throw Error(data.error);
  if(data.scenario_hash!==snapshot.scenario_hash)throw Error('Source state changed; recalculate the scenario.');
  architectureCache={key,data};if(activeView==='commercial')render();
 }catch(error){if(id!==architectureRequestId||key!==architectureKey())return;architectureCache={key,error:error.message};if(activeView==='commercial')render();}
}
function feeInterval(x){
 if(x.status==='internal_transfer_eliminated')return 'Internal transfer eliminated';
 const range='$'+fmt(x.lower_usd_year,2)+'–$'+fmt(x.upper_usd_year,2)+'/year';
 if(x.status!=='feasible_interval')return 'No nonnegative interval ('+range+')';
 return range+(x.selected_within_interval?' · selected payment inside':' · selected payment outside')+(x.other_entities_nonnegative?'':' · another counterparty has a loss');
}
function architecturePanel(){
 const key=architectureKey(),scope=architectureScope(),a=result.architecture_parameters,c=a.common,p=a.profiles.licensed_independent;
 if(architectureCache.key!==key){architectureCache={key,pending:true};loadArchitecture(key);}
 const input=(id,label,value,extra='')=>`<label>${esc(label)}<input id="${id}" type="number" step="any" value="${value}" ${extra}></label>`;
 const controls=`<div class="architecture-controls">`+
  input('arch-model-fee','Model payment, USD/year',c.model_fee_usd_year,'data-arch-common="model_fee_usd_year" min="0"')+
  input('arch-adaptation','Licensed-policy adaptation engineering, hours',p.adaptation_engineering_hours,'data-arch-profile="licensed_independent" data-arch-key="adaptation_engineering_hours" min="0"')+
  input('arch-support','Licensed-policy support change, minutes/robot-hour',p.support_minutes_delta,'data-arch-profile="licensed_independent" data-arch-key="support_minutes_delta"')+
  input('arch-service-price','Operating-provider service price / digital-human baseline',c.service_price_fraction,'data-arch-common="service_price_fraction" min="0"')+
  `<label>Customer path<select id="arch-customer-path" data-arch-common="customer_path"><option value="incumbent" ${c.customer_path==='incumbent'?'selected':''}>Incumbent</option><option value="newco" ${c.customer_path==='newco'?'selected':''}>Newco</option></select></label>`+
  input('arch-newco-setup','Additional newco setup, USD',c.newco_setup_usd,'data-arch-common="newco_setup_usd" min="0"')+
  `<label><input id="arch-compatible" type="checkbox" data-arch-profile="licensed_independent" data-arch-key="assume_compatible" ${p.assume_compatible?'checked':''}> Assume licensed configuration compatible</label></div><button id="apply-architectures">Apply architecture assumptions</button> <button id="reset-architectures">Reset architecture assumptions</button><p id="arch-input-state" class="small" role="status">Displayed results use the last applied assumptions. Apply edits before changing scope.</p>`;
 let content=empty(architectureCache.error?'Architecture calculation unavailable: '+architectureCache.error:'Calculating the selected service reference…');
 if(architectureCache.data){
  const data=architectureCache.data;
  const rows=data.architectures.map(r=>({...r,model_interval:r.fee_intervals?.model_fee,service_interval:r.fee_intervals?.service_payment,
   parties:r.entities?.map(e=>title(e.entity).replace(/\bOem\b/g,'OEM')+': '+'$'+fmt(e.annual_equivalent_net_usd,2)+'/year').join('; ')}));
  content=table(rows,[['label','Architecture',esc],['resource_cost_usd_year','Resource cost/year',v=>v===null?'Not admitted':'$'+fmt(v,2),true],['cash_benefit_usd_year','Allocated cash benefit/year',v=>v===undefined?'Not admitted':'$'+fmt(v,2),true],['all_entities_nonnegative_at_selected_payments','Entity annual equivalents',v=>v===undefined?'Not admitted':v?'All nonnegative':'At least one negative']])+`<h3>Conditional external payment ranges</h3>`+table(rows,[['label','Architecture',esc],['model_interval','Model payment',v=>v?feeInterval(v):'Not admitted'],['service_interval','Service payment',v=>v?feeInterval(v):'Not admitted']])+`<details><summary>Who receives the allocated cash benefit?</summary>`+table(data.architectures.flatMap(r=>(r.entities||[]).map(e=>({architecture:r.label,entity:e.entity,annual:e.annual_equivalent_net_usd}))),[['architecture','Architecture',esc],['entity','Entity',v=>esc(v==='oem'?'OEM':title(v))],['annual','Annual equivalent, USD',v=>'$'+fmt(v,2),true]])+`</details>`+
   `<p class="small">Digital-human resource reference: ${money(data.alternatives.digital_human_resource_cost_usd_year)}/year. Human reference: ${money(data.alternatives.human_resource_cost_usd_year)}. Specialized scenario: ${money(data.alternatives.specialized_resource_cost_usd_year)}. ${esc(data.alternatives.specialized_boundary)}</p>`+
   `<h3>Equal technology · customer paths</h3>`+table(data.customer_path_comparison,[['architecture_id','Architecture',v=>esc(boot.architecture_catalog.labels[v])],['incumbent_resource_cost_usd_year','Incumbent cost/year',money,true],['newco_resource_cost_usd_year','Newco cost/year',money,true],['physical_service_identical','Same physical service',v=>v===null?'Not admitted':v?'Yes':'No']])+
   `<p class="small">Path labels do not change productivity. Only explicit additional setup costs differ. Demand capture, response timing and company finance remain separate.</p>`+
   `<details><summary>Inspect assumptions, cost lines, transfers and entity cash schedules</summary><pre>${esc(JSON.stringify(data,null,2))}</pre></details><button id="export-architectures">Export architecture comparison</button>`;
 }
 return `<section id="architecture-calculator"><h3>Conditional architecture economics · ${esc(cellLabel(scope.cell_id))}, ${scope.year}</h3>`+
  notice('Synthetic assumptions, not vendor prices or qualified product rankings. One matched service site, selected-year conditions held over service life. Resource expenses are separate from fees; internal transfers cancel. Hardware is bought by the operator; the legacy sale/lease/service selector governs the separate reference tables below.',true)+
  `<p class="small">${$('cell-filter').value==='all'?'All-cell scope uses the manufacturing cell as an explicitly labeled reference. ':''}The robot digital-service input becomes reference inference-resource expense in this case, replacing the scalar bundle rather than adding it twice. Allocated upfront development costs are not an actual company cash calendar. Real rights and service qualification remain unknown.</p>`+
  controls+content+`<p><a href="/model/ARCHITECTURES.md" target="_blank">Architecture methods and boundaries ↗</a></p></section>`;
}
function jointTable(){const annual=result.joint_by_year.find(y=>y.year===Number($('year-filter').value)),p=annual.effective_digital_parameters;return `<p class="small">Reference comparison for ${$('year-filter').value}, using that year’s digital conditions and exogenous capability with no learned increment. This is matched site economics, not realized fleet savings. Human time reduction: ${fmt(p.digital_efficiency*100,1)}%; coordination: ${fmt(p.coordination*100,1)}%; additional robot service: ${money(p.digital_cost_usd)}/robot-year.</p>`+table(selectedJoint(),[['cell_id','Matched annual site',v=>esc(cellLabel(v))],['C00','Human baseline',money,true],['C01','Digital human',money,true],['C10','Robot + required software',money,true],['C11','Joint system',money,true],['robotics_saving_on_digital_baseline','Robot value vs digital human',money,true],['cost_interaction','Cost interaction',money,true],['cell_id','Calculation',v=>`<button class="ref" data-calculation="${esc(v)}">Trace inputs and costs ↗</button>`]]);}
function showEvidence(id){++detailRequestId;activeTraceHash=null;const record=evidenceById.get(id);$('evidence-detail').innerHTML=record?`<div class="eyebrow">SAVED EVIDENCE · NOT A SCENARIO OVERRIDE</div><h2>${esc(id)}</h2>${cards([record],1,false)}`:empty(`Unresolved evidence reference ${id}. See validation report; do not infer a source.`);$('evidence-dialog').showModal();}


async function showCalculation(cellId){
 const detailId=++detailRequestId;
 const snapshot=result;const selectedYear=Number($('year-filter').value);activeTraceHash=snapshot.scenario_hash;
 $('evidence-detail').innerHTML='<h2>Calculation trace</h2><p>Loading the current scenario calculation…</p>';
 $('evidence-dialog').showModal();
 try{
  const response=await fetch('/api/joint-trace',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({cell_id:cellId,preset:snapshot.preset,overrides:snapshot.parameters,digital_paths:snapshot.digital_paths,year:selectedYear,architecture_overrides:snapshot.architecture_parameters})});
  const trace=await response.json();if(detailId!==detailRequestId)return;if(!response.ok)throw Error(trace.error);
  if(trace.scenario_hash!==snapshot.scenario_hash||result.scenario_hash!==snapshot.scenario_hash||Number($('year-filter').value)!==selectedYear)throw Error('The engine or assumptions changed. Recalculate the scenario before tracing it.');
  const rows=trace.branches.map(b=>({branch:b.branch,...b.calculation,operating:b.robot?b.calculation.provider_operating_cost_usd:0}));
  $('evidence-detail').innerHTML=`<div class="eyebrow">SYNTHETIC CALCULATION · ${esc(trace.reference_year)}</div><h2>${esc(cellLabel(cellId))}</h2><p>${esc(trace.scope)}</p>`+
   notice(esc(trace.source_boundary),true)+
   `<p>Matched output: <strong>${fmt(trace.cell.annual_units_per_site)} ${esc(trace.cell.output_unit)}/site/year</strong>. Capability index: ${fmt(trace.capability,4)}.</p>`+
   table(rows,[['branch','Branch'],['customer_human_and_digital_cost_usd','Human + site digital',money,true],['operating','Robot operating',money,true],['capital_consumption_usd_year','Annual capital',money,true],['resource_cost_usd','Total USD/year',money,true]])+
   table(rows,[['branch','Branch'],['robot_accepted_units','Robot accepted units/year',v=>fmt(v,2),true],['retained_human_hours','Retained human hours/year',v=>fmt(v,2),true]])+
   `<p class="small">C00: human baseline; C01: digital human; C10: robot with required software; C11: joint system. Total resource cost adds the three cost columns. This values labor opportunity cost; removed payroll remains unknown. Price transfers are excluded.</p>`+
   `<p>Robot value against the digital baseline: C01 − C11 = ${money(trace.comparison.robotics_saving_on_digital_baseline)}. Cost interaction: C11 − C10 − C01 + C00 = ${money(trace.comparison.cost_interaction)}.</p>`+
   `<details><summary>Exact cell, system and scenario inputs</summary><pre>${esc(JSON.stringify({cell:trace.cell,system:trace.system,effective_parameters:trace.parameters,scalar_parameters:trace.scalar_parameters,resolved_digital_paths:trace.resolved_digital_paths},null,2))}</pre></details>`+
   `<details><summary>Engine equations and literal assumptions</summary>${[...trace.functions,...trace.path_functions].map(f=>`<h3>${esc(f.path)}:${f.start_line} · ${esc(f.function)}</h3><pre>${esc(f.source)}</pre>`).join('')}</details>`+
   `<p class="small">Scenario ${esc(trace.scenario_hash)}<br>Engine SHA-256 ${esc(trace.engine_sha256)}</p><a href="/model/assumptions.json" target="_blank">Saved synthetic assumptions ↗</a> · <a href="/model/METHODS.md" target="_blank">Methods and limits ↗</a>`;
 }catch(error){if(detailId===detailRequestId)$('evidence-detail').innerHTML=empty('Calculation trace unavailable: '+error.message);}
}

const renderers={
 atlas(){const markets=recordsFor(/^markets$/);const obs=boot.observed_summary;const statistics=obs.market_employment?`<div class="grid">${metric('All 15 mapped families',fmt(obs.market_employment.value/1000,3)+'m','2025 wage-and-salary jobs · national reference')}${metric('Selected occupation groups',fmt(obs.selected_occupation_jobs.value/1000000,3)+'m','May 2025 OEWS jobs · separate overlapping view')}${metric('Physical-work hours','Unknown','No scenario fills empirical missingness')}</div>`:'';return statistics+notice('Sourced employment is an economic anchor. Physical-work shares, annual hours and robot addressability remain separate fields. The illustrative 72-site pool below is excluded from every empirical aggregate.',true)+docs(/market|atlas/)+
  `<h3 class="section-label">Dated empirical coverage map</h3>`+table(markets.filter(x=>recordMatches(x.value)).map(x=>x.value),[['market_id','Market'],['label','End-market family'],['economic_baseline','Employment, thousand jobs',v=>fmt(v.employment,1),true],['coverage_status','Employment coverage'],['physical_work_coverage_status','Physical-work coverage']])+cards(markets,20)+
  physicalCrosswalk()+`<h3 class="section-label">Linked model cells · synthetic population</h3>`+table(selectedCells(),[['label','Market and stage',v=>esc(v)],['annual_units_per_site','Accepted units/site/year',v=>fmt(v),true],['output_unit','Output unit'],['human_hours_per_unit','Baseline human h/unit',v=>fmt(v,2),true],['physical_fit','Conditional physical fit']])+evidenceSection(/^cells$/,/market/);
 },
 deployment(){const rows=selectedRows();const flow={};rows.forEach(r=>Object.entries(r.waterfall).forEach(([k,v])=>flow[k]=(flow[k]||0)+v));return `<div class="grid">${metric('Relevant constructed work',fmt(flow.relevant_work),'Baseline-equivalent human hours/year')}${metric('Realized baseline output',fmt(flow.realized_baseline_output),'Same denominator; additional demand excluded')}${metric('Active robot stock',fmt(sum(rows,'active_stock'),1),'Expected fractional units · not orders or shipments')}</div>`+
  `<div class="card"><h3>Conditional cohort waterfall</h3>${bars(Object.entries(flow))}<p class="small">Twelve heterogeneous sites per cell. Technical, economic and readiness predicates are evaluated on each site; gate percentages are not multiplied independently. Installed capacity and supported/ramped output retain the same denominator.</p></div>`+
  table(rows,[['cell_id','Cell',v=>esc(cellLabel(v))],['capability','Capability index',v=>fmt(v,2),true],['binding_constraints','Observed model constraint',v=>esc(v.join(', ')||'No unfilled eligible demand')],['economics','Assumed annual customer cash saving',v=>money(v.customer_savings_usd),true],['economics','Potential payback',v=>v.payback_years===null?'No positive cash gain':fmt(v.payback_years,1)+' years',true]])+
  notice(`Customer cash assumes ${fmt(result.parameters.labor_avoidability*100)}% of released labor value can actually be avoided. This is not an observed payroll result.`)+evidenceSection(/^cells$|market_implications|deployment_pathways/,null,12)+docs(/field_support_denominators/)+`<h3>Audited deployment denominators and limitations</h3>`+evidenceSection(/^cases$|^conflicts$/,/field_support_denominators/,12);
 },
 providers(){return frontierActors()+notice('Configured systems and observed phases are evidence objects. A demonstration, order, pilot or mission count does not establish productive fleet scale. The virtual SYN-H/SYN-Q model configurations are not product BOMs.',true)+docs(/capability|physical|onboard_workload_qualification/)+evidenceSection(/^systems$|^configurations$|player|provider|supply_links/,null,36)+`<h3>Layered access and rights</h3>`+evidenceSection(/openness/,null,10);},
 improvement(){return notice('The curve below is an explicit threshold scenario, not an empirical scaling fit. No digital benchmark score, data-scaling exponent or manufacturer specification is converted into robot productivity.')+
  `<div class="card"><h3>Selected cohorts · mean capability threshold index</h3>${chart(scopedTimeline(),'year',[['capability','Scenario capability','#00796e']])}<p class="small">Base progress and optional same-system learning are distinct. Improvements to installed cohorts assume compatible software and no hardware redesign; retrofit expense is not modeled.</p></div>`+
  jointTable()+`<h3>Evidence: operating claims and evaluation boundaries</h3>`+evidenceSection(/^capabilities$|learning_relationships|benchmark/,null,24);},
 fleet(){const year=Number($('year-filter').value),global=result.fleet.years.find(x=>x.year===year);return `<div class="card"><h3>Commissioning and retained stock · ${esc(scopeName())}</h3>${chart(scopedTimeline(),'year',[['active_stock','Active stock','#00796e'],['commissioned','Commissioned','#326c9c'],['retired','Retired','#b86020']])}</div>`+
  notice('Resource budgets below are the shared six-cell reference pool. Selecting one cell never gives it exclusive access to this pool.',true)+
  table(Object.keys(global.resource_budgets).map(k=>({resource:k,budget:global.resource_budgets[k],used:global.resource_used[k]})),[['resource','Shared resource'],['budget','Available',v=>fmt(v),true],['used','Used/reserved',v=>fmt(v),true]])+
  `<p class="small">Existing-fleet support: ${fmt(global.support_existing_used)} of ${fmt(global.support_existing_required)} required hours. Spare parts and support are reserved before expansion; physically installed stock can be unsupported.</p>`+
  table(selectedRows(),[['cell_id','Cell',v=>esc(cellLabel(v))],['active_stock','Active',v=>fmt(v,2),true],['commissioned','Commissioned',v=>fmt(v,2),true],['replacement_commissioned','Replacement',v=>fmt(v,2),true],['expansion_commissioned','Expansion',v=>fmt(v,2),true],['support_fraction','Supported fraction',v=>fmt(v,2),true],['baseline_equivalent_hours','Realized baseline h',v=>fmt(v),true]])+
  notice('Annual funding envelopes refresh exogenously. Operating cash is not automatically reinvested. Allocation is a transparent savings-ranked heuristic, not an optimal portfolio.');},
 learning(){const y=result.fleet.years.find(x=>x.year===Number($('year-filter').value));return learningExecutionPanel()+learningQualificationPanel()+conventionalCoordinationPanel()+`<div class="flow"><span>Supported deployment</span><i>→</i><span>Experience exposure</span><i>→</i><span>Rights + validation</span><i>→</i><span>Same-system directed transfer</span><i>→</i><span>Future capability threshold</span></div>`+
  notice('A robot-hour is exposure, not useful accessible training data. Optional transfer is unvalidated and limited to the same virtual configuration; cross-embodiment and cross-market empirical effects remain unknown. Default transfer is an assumption of no transfer, not evidence of zero transfer.')+
  `<div class="grid">${metric('Validation cash this year',money(y.learning_validation_cash_usd),'Whole-portfolio reference pool')}${metric('Transfer coefficient',fmt(result.parameters.learning_transfer,2),'Scenario only; no added data-value premium')}</div>`+
  table(selectedRows(),[['cell_id','Cell',v=>esc(cellLabel(v))],['learning_increment','Applied capability increment',v=>fmt(v,4),true],['capability','Resulting capability',v=>fmt(v,3),true]])+
  docs(/learning_data_economics|coordination_reproducibility/)+evidenceSection(/transfer_edges|learning_relationships|coordination_archetypes|direct_contribution|contribution_maps|interface_ledger/,null,35)+`<h3>Learning-data economics: bounded source evidence</h3>`+evidenceSection(/^evidence$/,/learning_data_economics/,8);},
 customer(){const n=result.newco;return hospitalSupportPanel()+supportExpansionPanel()+competitiveRenewalPanel()+commercialDisclosurePanel()+entryTransitionPanel()+calendarBridgePanel()+financePanel()+sharedEnterprisePanel()+napkinComparison()+regionalDeployments()+`<div class="card"><h3>${esc(result.customer_mechanisms.label)}</h3><p>${esc(result.customer_mechanisms.explanation)}</p>${table([result.customer_mechanisms],[['ready_delay_years','Approval delay, years'],['authority_sites','Sites under authority / 12'],['site_cash_limit_usd','Site cash ceiling',money],['implementation_sites_year','Implementation sites/year'],['max_payback_years','Maximum payback']])}</div>`+
  evidenceSection(/adopter|profile|entry_cases|customer_cases|organization|pathways/,/customer/,12)+
  `<details><summary>Historical independent ENTRY-FG-01 reference</summary><h3>ENTRY-FG-01 · earlier independent illustration</h3>`+notice('This historical fixed floor-service reference case (CELL-M11), with normalized accepted service bundles/month. It is not added to the annual six-cell fleet denominator. Identical robot technology and terms are available to the incumbent.',true)+
  `<div class="grid">${metric('Formation + asset cash at t0',money(n.upfront_usd),'Build/acquire/hybrid changes cash, not underlying demand')}${metric('Peak funding need',money(n.peak_funding_required_usd),'Includes overhead, ramp and receivables')}${metric('Unfunded amount',money(n.funding_gap_usd),'First unfunded month: '+(n.first_unfunded_month??'none'))}</div>`+
  `<div class="card"><h3>Conditional cash balance · USD</h3>${chart(n.rows,'month',[['cash_balance_usd','Cash balance','#00796e']])}<p class="small">${esc(n.limitation)}</p></div>`+
  `<div class="card"><h3>Capacity, demand and delivered service · units/month</h3>${chart(n.rows,'month',[['capacity_units','Newco capacity','#00796e'],['demand_units','Won demand','#b86020'],['served_units','Delivered','#326c9c'],['incumbent_same_robot_capacity_units','Incumbent same robot capacity','#82729d']])}</div>`+
  `<details><summary>Inspect exact entrant assumptions and full monthly cash path</summary><pre>${esc(JSON.stringify(n,null,2))}</pre></details></details>`;},
 commercial(){const ids=new Set(selectedCells().map(x=>x.cell_id));const cases=result.commercial_by_cell.filter(x=>ids.has(x.cell_id));return hospitalSupportPanel()+commercialDisclosurePanel()+monthlyArchitecturePanel()+monthlyCommercialPanel()+regionalRights()+frontierArchitectures()+notice('Customer business ownership and robot-asset ownership are separate dimensions. Prices redistribute value; manufacturer resource expenditure is not customer price. Cash tables hold initial capability and year-zero digital conditions for the full one-site lifetime; the calendar-year filter does not change them. They are incremental to an assumed avoidable baseline and include deployment investment once.',true)+
  cases.map(c=>`<div class="card"><h3>${esc(cellLabel(c.cell_id))} · ${esc(c.arrangement)}</h3><p class="small">${esc(c.scope)}</p><p>Robot owner: <strong>${esc(c.rights.robot_asset_owner)}</strong> · Workflow authority: ${esc(c.rights.workflow_authority)} · Data reuse: ${esc(c.rights.data_reuse)}</p>${table(c.cashflows,[['period','Period'],['customer_cash_usd','Customer',money,true],['provider_cash_usd','Provider',money,true],['financier_cash_usd','Financier',money,true],['consolidated_incremental_cash_usd','Consolidated',money,true]])}</div>`).join('')+
  evidenceSection(/commercial|arrangement|rights|business_model|value_capture/,/customer/,18);},
 digital(){return hospitalSupportPanel()+commercialDisclosurePanel()+learningQualificationPanel()+notice('Edges in this workspace describe dated contractual, physical, data or control relationships. They are not measured material/cash flow widths. Onboard embedded memory is never pooled with datacenter HBM or training resources.',true)+docs(/digital|infrastructure|coordination_reproducibility|onboard_workload_qualification/)+
  `<div class="flow"><span>Power · sites · equipment</span><i>→</i><span>Compute · memory · networks</span><i>→</i><span>Training / inference</span><i>→</i><span>Models · tools · distribution</span><i>→</i><span>Deployment firms / operating customers</span></div>`+
  evidenceSection(/ecosystem|relationship|supply_chain|actor|infrastructure|deployment_dossiers|digital_dossiers|^dossiers$|value_chain/,/digital|infrastructure/,36)+`<h3>Coordination reproducibility and execution boundaries</h3>`+evidenceSection(/benchmark_audits|interface_ledger|mechanism_constraints/,/coordination_reproducibility/,16)+
  `<h3>Frontier model releases and layered rights</h3>`+docs(/frontier_models/)+evidenceSection(/^frontier_models$|^model_rights_cards$/,/frontier_model_economics/,14)+`<h3>Moving physical-production counterfactual</h3>`+jointTable()+notice('The human digital-efficiency control changes the human baseline as well as retained human work in robot sites. Coordination and the annual robot digital-service bundle change robot economics separately; this bundle is not a per-token inference price. No QJE, coding-study or benchmark coefficient is imported.');},
 analogy(){return `<h3>Matched 2 × 2 scenario</h3>`+jointTable()+notice('Costs value labor opportunity cost at fixed accepted output and quality. C01 − C11 is robotics value against a digital-improved human baseline. C11 − C10 − C01 + C00 is the cost interaction; positive values can reveal overlapping savings. This is a scenario contrast, not a causal estimate.',true)+
  `<h3>Source/target analogy tests and direct contributions</h3>`+evidenceSection(/analog|transfer_tests|direct_contribution|contribution|benchmark/,null,40);},
 supply(){const year=Number($('year-filter').value),b=result.backcast;return notice('Supply tables refer to the common pool for all six cells. Qualified receipts are already net of external commitments and upstream yield. Assembly yield is applied once. Humanoid and quadruped actuators remain incompatible; shared embedded boards are a hypothetical compatible pool.',true)+
  `<div class="flow"><span>Qualified net components</span><i>→</i><span>Service spares reserved</span><i>→</i><span>Assembly starts</span><i>+ 1 year →</i><span>Accepted finished inventory</span><i>→</i><span>Shipment</span><i>+ 1 year →</i><span>Commissioned fleet</span></div>`+
  table(result.fleet.components.filter(x=>x.year===year),[['resource_id','Compatible class'],['opening_inventory','Opening',v=>fmt(v,2),true],['qualified_net_receipts','Receipts',v=>fmt(v,2),true],['service_consumed','Service',v=>fmt(v,2),true],['assembly_consumed','Assembly',v=>fmt(v,2),true],['closing_inventory','Closing',v=>fmt(v,2),true]])+
  table(result.fleet.production.filter(x=>x.year===year),[['system_id','Configuration'],['assembly_starts','Starts',v=>fmt(v,2),true],['accepted_completions','Accepted',v=>fmt(v,2),true],['rejected_completions','Rejected',v=>fmt(v,2),true],['shipments','Shipped',v=>fmt(v,2),true],['work_in_progress','WIP',v=>fmt(v,2),true],['closing_finished','Finished stock',v=>fmt(v,2),true]])+
  `<h3>Backcast: ${fmt(b.target_active_stock)} retained robots by ${b.target_year}</h3>`+notice(esc(b.reason))+
  table(b.rows,[['commission_year','Commission year'],['latest_assembly_start_year','Latest starts'],['commissioned_required','Commissions',v=>fmt(v,2),true],['retirements','Replacements',v=>fmt(v,2),true],['assembly_starts_required','Required starts',v=>fmt(v,2),true],['actuator_h_for_starts','H actuators',v=>fmt(v),true],['actuator_q_for_starts','Q actuators',v=>fmt(v),true],['support_hours_required','Support hours',v=>fmt(v),true],['manufacturing_cash_required_usd','Manufacture cash',money,true]])+
  evidenceSection(/supply_links|configurations|component|capacity/,/physical|infrastructure/,18)+`<h3>Onboard workload qualification</h3>`+docs(/onboard_workload_qualification/)+evidenceSection(/^benchmark_cards$|^conflicts$/,/onboard_workload_qualification/,6);},
 embodiment(){const ids=new Set(selectedCells().map(c=>c.cell_id));const rows=result.embodiment_comparisons.filter(x=>ids.has(x.cell_id));return automotiveWorkcellPanel()+utilityInspectionPanel()+notice('Matched comparisons below are final-horizon reference alternatives at the same accepted annual output; the year filter does not change this table. Specialized cost factor and $5,000 capital allowance are explicit synthetic assumptions. Mixed operation allocates half of output to each process, with costs once. They do not establish a preferred real product.')+
  table(rows,[['cell_id','Cell',v=>esc(cellLabel(v))],['human','Human',money,true],['digital','Digital human',money,true],['robot','Configured robot',money,true],['specialized','Specialized candidate',money,true],['mixed','50/50 mixed allocation',money,true],['fit','Specialized fit boundary']])+
  notice('A sensor-only quadruped is not a manipulation substitute. A drone cannot automatically satisfy a ground-route or indoor inspection standard. Infeasible or unmatched physical functions receive no invented equivalent-output estimate.',true)+
  `<h3>Matched field comparisons, deployment episodes and layered rights</h3>`+docs(/quadruped_operator_followup|field_support_denominators/)+evidenceSection(/embodiment_comparisons|deployments|openness_cards|transfer_tests|^cases$|^conflicts$/,/physical|quadruped_operator_followup|field_support_denominators/,44);},
 evidence(){return `<div class="links"><button id="compare-presets">Compare all saved scenarios</button><a href="/model/assumptions.json" target="_blank">Authoritative assumptions ↗</a></div><div id="scenario-comparison">${comparisonResults?comparisonTable():''}</div>`+
  `<p class="small">Compare cumulative output as well as terminal stock: a delayed deployment may have a younger fleet at the final-year boundary because earlier cohorts have retired.</p><h3 class="section-label">Current version and model assumptions</h3>`+table(result.assumptions,[['id','Assumption ID'],['status','Status'],['description','Meaning and boundary']])+
  `<h3>Saved evidence packages</h3>`+table(boot.evidence_packages,[['path','Package',v=>`<a href="/${esc(v)}" target="_blank">${esc(v)}</a>`],['sha256','Snapshot SHA-256',v=>`<span class="small">${esc(v||'Unavailable')}</span>`]])+
  `<h3>Claim-level evidence drilldown</h3>`+cards(allRecords.filter(x=>x.key==='evidence'),50)+
  `<h3>Known limits</h3><ul>${result.limitations.map(x=>`<li>${esc(x)}</li>`).join('')}</ul>`;}
};

function comparisonTable(){const ids=new Set(selectedCells().map(x=>x.cell_id));return table(comparisonResults.map(r=>{const cells=r.fleet.cells.filter(x=>ids.has(x.cell_id)&&x.year===r.fleet.years.at(-1).year);return {preset:r.preset,stock:sum(cells,'active_stock'),hours:sum(cells,'baseline_equivalent_hours'),cumulative:sum(r.fleet.cells.filter(x=>ids.has(x.cell_id)),'baseline_equivalent_hours'),gap:r.newco.funding_gap_usd};}),[['preset','Saved scenario'],['stock','Final selected active stock',v=>fmt(v,2),true],['hours','Final baseline-equivalent h',v=>fmt(v),true],['cumulative','Cumulative baseline-equivalent h',v=>fmt(v),true],['gap','Fixed newco reference funding gap',money,true]]);}
function render(){if(!result)return;describeFacets();const v=viewNames.find(x=>x[0]===activeView);setText('view-kicker',`WORKSPACE ${v[1]} / 13`);setText('view-title',v[2]);setText('scope',`${scopeName()} · ${$('year-filter').value}`);$('content').innerHTML=decisionContext()+renderers[activeView]();document.querySelectorAll('nav button').forEach(b=>b.classList.toggle('active',b.dataset.view===activeView));setText('model-hash',`Engine ${result.model_version} · scenario ${result.scenario_hash.slice(0,14)}`);}
function invalidateTrace(message){if(activeTraceHash){++detailRequestId;activeTraceHash=null;$('evidence-detail').innerHTML=empty(message);}}
function updateControls(){
 for(const group of controlGroups)for(const [key]of group[1]){
  const el=$('p-'+key);if(el){el.value=result.parameters[key];const output=$('v-'+key);if(output)output.textContent=fmt(result.parameters[key],3);
   el.disabled=Boolean(digitalPaths&&(Object.hasOwn(digitalPaths,key)||key==='years'));
   el.title=el.disabled?'Annual paths override this control. Clear paths to change the horizon.':'';
  }
 }
 for(const key of ScenarioIO.channels)$('path-'+key).value=digitalPaths?.[key]?.join(', ')||'';
 const years=result.fleet.years;setText('path-horizon',`${years.length} annual levels: ${years[0].year}–${years.at(-1).year}. Clear paths before changing the horizon.`);
 setText('path-status',digitalPaths?'Annual paths applied. Supplied levels replace their scalar controls.':'Constant values from the scalar controls are applied each year.');
}
async function run(){
 const id=++requestId;setText('run-state','Recalculating authoritative Python model…');
 try{
  const response=await fetch('/api/run',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({preset:$('preset').value,overrides,digital_paths:digitalPaths,architecture_overrides:architectureOverrides})});
  const data=await response.json();if(id!==requestId)return false;if(!response.ok)throw Error(data.error);
  const oldYear=$('year-filter').value;result=data;digitalPaths=result.digital_paths;architectureOverrides=result.architecture_parameters;
  invalidateTrace('The scenario changed. Close this dialog and trace the updated comparison.');
  $('year-filter').innerHTML=result.fleet.years.map(x=>`<option value="${x.year}">${x.year}</option>`).join('');
  $('year-filter').value=result.fleet.years.some(x=>String(x.year)===oldYear)?oldYear:String(result.fleet.years.at(-1).year);
  updateControls();render();$('run-state').classList.remove('error');setText('run-state',`Recomputed · ${result.scenario_hash.slice(0,12)} · evidence unchanged`);return true;
 }catch(error){if(id!==requestId)return false;setText('run-state','Model error: '+error.message+'. Display and export retain the last valid result.');$('run-state').classList.add('error');return false;}
}
function download(name,text,type){const url=URL.createObjectURL(new Blob([text],{type}));const link=document.createElement('a');link.href=url;link.download=name;link.click();setTimeout(()=>URL.revokeObjectURL(url),500);}
function csv(rows){const keys=Object.keys(rows[0]||{});const quote=v=>'"'+String(typeof v==='object'?JSON.stringify(v):v??'').replaceAll('"','""')+'"';return [keys.map(quote).join(','),...rows.map(r=>keys.map(k=>quote(r[k])).join(','))].join('\r\n');}
function buildFacets(){
 $('evidence-facets').innerHTML=EvidenceFacets.definitions.map(d=>{
  const options=EvidenceFacets.options(allRecords,d);
  return `<label>${esc(d.label)}<select id="facet-${d.id}"><option value="">All recorded values</option><option value="missing">No explicit field (${options.missing} records)</option>${options.values.map(([v,n])=>`<option value="${esc('v:'+v)}" title="${esc(v)}">${esc(v.length>100?v.slice(0,97)+'…':v)} (${n})</option>`).join('')}</select></label>`;
 }).join('');
 $('evidence-facets').addEventListener('change',render);
 $('clear-facets').addEventListener('click',()=>{for(const d of EvidenceFacets.definitions)$('facet-'+d.id).value='';render();});
}
function describeFacets(){
 const selections=facetSelections();const active=Object.values(selections).some(Boolean);
 const count=allRecords.filter(r=>EvidenceFacets.matches(r.value,selections,r.key)).length;
 setText('facet-scope',active?`${count} of ${allRecords.length} saved record objects match these fields. Search, status and cell scope can narrow this further. Counts include claims and supporting objects.`:'No evidence-field filter. Values retain source wording; a license label alone does not establish commercial or hardware rights.');
}
function buildControls(){
 $('preset').innerHTML=Object.entries(boot.catalog.presets).map(([k,v])=>`<option value="${esc(k)}">${esc(v.label)}</option>`).join('');
 $('cell-filter').innerHTML+='<optgroup label="Six linked market-stage cells">'+boot.catalog.cells.map(c=>`<option value="${esc(c.cell_id)}">${esc(c.label)}</option>`).join('')+'</optgroup>';
 $('controls').innerHTML=controlGroups.map(([label,controls],i)=>`<details class="control-group" ${i===0?'open':''}><summary>${esc(label)}</summary>${controls.map(([key,name,min,max,step])=>`<label>${esc(name)}${min==='select'?`<select id="p-${key}" data-parameter="${key}">${boot.choices[key].map(v=>`<option value="${esc(v)}">${esc(title(v))}</option>`).join('')}</select>`:`<output class="control-value" id="v-${key}"></output><input id="p-${key}" data-parameter="${key}" type="range" min="${min}" max="${max}" step="${step}">`}</label>`).join('')}</details>`).join('');
 $('views').innerHTML=viewNames.map(([id,num,label])=>`<button data-view="${id}" title="${esc(label)}">${num} ${esc(label)}</button>`).join('');
}
async function init(){
 try{const response=await fetch('/api/catalog');boot=await response.json();if(!response.ok)throw Error(boot.error||'Accepted evidence catalog unavailable');
 for(const pack of boot.evidence_packages){if(!pack.data)continue;for(const [key,value]of Object.entries(pack.data)){if(Array.isArray(value))value.filter(v=>v&&typeof v==='object').forEach(v=>allRecords.push({key,value:v,path:pack.path}));}}
 allRecords.filter(x=>x.key==='evidence').forEach(r=>evidenceById.set(r.value.evidence_id,r));
 buildControls();buildFinanceEvents();buildCalendarEvents();buildMonthlyArchitectureEvents();buildCoordinationEvents();buildEntryTransitionEvents();buildCompetitiveRenewalEvents();buildSupportExpansionEvents();buildUtilityInspectionEvents();buildAutomotiveWorkcellEvents();buildLearningQualificationEvents();buildLearningExecutionEvents();buildFacets();const statuses=[...new Set(allRecords.filter(x=>x.key==='evidence').map(x=>recordStatus(x.value)).filter(x=>typeof x==='string'))].sort();$('status-filter').innerHTML+='<optgroup label="Saved provenance/status labels">'+statuses.map(x=>`<option value="${esc(x)}">${esc(x)}</option>`).join('')+'</optgroup>';
 $('controls').addEventListener('input',e=>{const k=e.target.dataset.parameter;if(k&&$('v-'+k))$('v-'+k).textContent=fmt(Number(e.target.value),3);});
 $('controls').addEventListener('change',e=>{const k=e.target.dataset.parameter;if(k){overrides[k]=boot.choices[k]?e.target.value:Number(e.target.value);comparisonResults=null;run();}});
 $('preset').addEventListener('change',()=>{overrides={};digitalPaths=null;architectureOverrides=null;comparisonResults=null;run();});$('reset').addEventListener('click',()=>{overrides={};digitalPaths=null;architectureOverrides=null;comparisonResults=null;run();});
 $('apply-paths').addEventListener('click',async()=>{const previous=digitalPaths;try{digitalPaths=ScenarioIO.annualPaths(boot.catalog.base_year,Object.fromEntries(ScenarioIO.channels.map(k=>[k,$('path-'+k).value])));comparisonResults=null;if(!await run())digitalPaths=previous;}catch(error){digitalPaths=previous;setText('path-status','Path error: '+error.message);}});
 $('clear-paths').addEventListener('click',()=>{digitalPaths=null;comparisonResults=null;run();});
 ['cell-filter','year-filter','status-filter'].forEach(id=>$(id).addEventListener('change',()=>{invalidateTrace('The selected scope changed. Close this dialog and trace the selected comparison.');render();}));$('evidence-search').addEventListener('input',render);
 $('views').addEventListener('click',e=>{if(e.target.dataset.view){activeView=e.target.dataset.view;location.hash=activeView;render();}});
 document.addEventListener('click',async e=>{const ref=e.target.closest('[data-evidence]');if(ref)showEvidence(ref.dataset.evidence);const calculation=e.target.closest('[data-calculation]');if(calculation)showCalculation(calculation.dataset.calculation);if(e.target.id==='compare-presets'){e.target.disabled=true;e.target.textContent='Calculating saved scenarios…';comparisonResults=await Promise.all(Object.keys(boot.catalog.presets).map(preset=>fetch('/api/run',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({preset})}).then(r=>r.json())));render();}});
 for(const eventName of ['input','change'])document.addEventListener(eventName,e=>{if(e.target.dataset.archCommon||e.target.dataset.archProfile)setText('arch-input-state','Unapplied edits. Display and export retain the last computed case.');});
 document.addEventListener('change',e=>{if(e.target.id==='enterprise-case'&&e.target.value!=='custom'){++enterpriseState.requestId;enterpriseState.selection=e.target.value;enterpriseState.current=null;enterpriseState.inputs=enterpriseState.data.case_inputs[e.target.value];enterpriseState.error='';render();}});
 for(const eventName of ['input','change'])document.addEventListener(eventName,e=>{if(e.target.id.startsWith('enterprise-')&&e.target.id!=='enterprise-case')setText('enterprise-input-state','Unapplied edits. Display and export retain the last calculated case.');});
 document.addEventListener('click',async e=>{
  if(e.target.id==='export-enterprise'&&enterpriseState.data)download('shared-enterprise-'+enterpriseState.selection+'.json',JSON.stringify(enterpriseState.current||enterpriseState.data.cases[enterpriseState.selection],null,2),'application/json');
  if(e.target.id==='apply-enterprise'){
   const id=++enterpriseState.requestId;
   try{
    const readCents=id=>{const raw=$(id).value.trim();if(!/^\d+(\.\d{1,2})?$/.test(raw))throw Error('Cash must be nonnegative USD with no more than two decimals.');const parts=raw.split('.'),value=Number(parts[0])*100+Number((parts[1]||'').padEnd(2,'0'));if(!Number.isSafeInteger(value))throw Error('Cash is outside the supported integer range.');return value;};
    const procurement=$('enterprise-procurement').value;if(!/^\d+$/.test(procurement))throw Error('Procurement month must be an integer.');
    const response=$('enterprise-response').value,inputs={entrant_cash_cents:readCents('enterprise-cash'),extra_equity_cents:readCents('enterprise-equity'),incumbent_procurement_month:Number(procurement),response_month:response==='none'?null:Number(response),delayed_receipts:$('enterprise-lag').checked,no_entry:$('enterprise-no-entry').checked};
    setText('enterprise-input-state','Calculating shared physical, demand and cash ledgers…');
    const responseData=await fetch('/api/shared-enterprise',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({inputs})}),data=await responseData.json();if(!responseData.ok)throw Error(data.error||'Calculation failed');if(id!==enterpriseState.requestId)return;
    enterpriseState.selection='custom';enterpriseState.current=data.result;enterpriseState.inputs=data.inputs;enterpriseState.error='';render();
   }catch(error){if(id===enterpriseState.requestId)setText('enterprise-input-state','Input error: '+error.message+' Display and export retain the last valid case.');}
  }
 });
 document.addEventListener('change',e=>{if(e.target.id==='monthly-commercial-case'){monthlyCommercialCase=e.target.value;render();}});
 document.addEventListener('click',async e=>{
  if(e.target.id==='export-monthly-commercial'&&monthlyCommercialCache?.cases)download('monthly-'+monthlyCommercialCase+'.json',JSON.stringify(monthlyCommercialCache.cases[monthlyCommercialCase],null,2),'application/json');
  if(e.target.id==='apply-architectures'){
   const previous=architectureOverrides;
   try{
    const candidate=JSON.parse(JSON.stringify(result.architecture_parameters));
    for(const field of document.querySelectorAll('#architecture-calculator [data-arch-common], #architecture-calculator [data-arch-profile]')){
     const common=field.dataset.archCommon,profile=field.dataset.archProfile,key=field.dataset.archKey;
     let value;if(field.type==='checkbox')value=field.checked;else if(common==='customer_path')value=field.value;else{if(field.value.trim()==='')throw Error('Blank is not a numeric assumption.');value=Number(field.value);if(!Number.isFinite(value))throw Error('Enter a finite number.');}
     if(common)candidate.common[common]=value;else candidate.profiles[profile][key]=value;
    }
    architectureOverrides=candidate;comparisonResults=null;
    if(!await run()){architectureOverrides=previous;setText('arch-input-state','Inputs rejected. Display and export retain the last valid case.');}
   }catch(error){architectureOverrides=previous;setText('arch-input-state','Architecture input error: '+error.message);}
  }
  if(e.target.id==='reset-architectures'){architectureOverrides=null;run();}
  if(e.target.id==='export-architectures'&&architectureCache.key===architectureKey()&&architectureCache.data)download('architecture-'+architectureCache.data.case_hash.slice(0,10)+'.json',JSON.stringify(architectureCache.data,null,2),'application/json');
 });
 $('close-dialog').addEventListener('click',()=>$('evidence-dialog').close());$('evidence-dialog').addEventListener('close',()=>{++detailRequestId;activeTraceHash=null;});
 $('download-json').addEventListener('click',()=>download('robotics-scenario-'+result.scenario_hash.slice(0,10)+'.json',JSON.stringify(result,null,2),'application/json'));
 $('download-csv').addEventListener('click',()=>download('selected-cohorts.csv',csv(selectedRows(true)),'text/csv'));
 $('import').addEventListener('change',async e=>{try{const file=e.target.files[0];if(!file)return;const saved=ScenarioIO.savedInput(JSON.parse(await file.text()),boot.catalog.presets);if(saved.comparison_scope&&!boot.catalog.cells.some(c=>c.cell_id===saved.comparison_scope.cell_id))throw Error('Unknown saved comparison cell.');$('preset').value=saved.preset;overrides=saved.overrides;digitalPaths=saved.digital_paths;architectureOverrides=saved.architecture_overrides;comparisonResults=null;if(await run()&&saved.comparison_scope){if(!result.fleet.years.some(y=>y.year===saved.comparison_scope.year))throw Error('Saved comparison year is outside the horizon.');$('cell-filter').value=saved.comparison_scope.cell_id;$('year-filter').value=String(saved.comparison_scope.year);activeView='commercial';render();}}catch(error){setText('run-state','Import error: '+error.message);}});
 if(viewNames.some(x=>x[0]===location.hash.slice(1)))activeView=location.hash.slice(1);
 await run();
 }catch(error){$('content').innerHTML=notice('Could not load local model: '+esc(error.message));}
}
init();
