'use strict';
let learningQualificationRoute='generated_data';
function learningQualificationPacket(){return boot.evidence_packages.find(p=>p.path==='data/learning_data_economics.json');}
function learningQualificationPanel(){
 const packet=learningQualificationPacket(),d=packet?.data;if(!d?.qualification_routes)return '';
 const route=d.qualification_routes.find(r=>r.route_id===learningQualificationRoute)||d.qualification_routes[0];
 const matched=d.evidence.filter(r=>route.evidence_refs.includes(r.evidence_id)&&recordMatches(r,'evidence'));
 const refsVisible={evidence_refs:matched.map(r=>r.evidence_id)};
 return `<section id="learning-qualification" class="card"><h3>R&D progress → qualified operating capacity</h3>`+
 `<p>Generated data, video metrics, policy tests, technical integration and supported supply are different evidence stages. These source records inform qualification; they change no synthetic learning coefficient.</p>`+
 `<label>Decision to inspect<select id="learning-qualification-route">${d.qualification_routes.map(r=>`<option value="${esc(r.route_id)}" ${r.route_id===route.route_id?'selected':''}>${esc(r.title)}</option>`).join('')}</select></label>`+
 `<p><b>What the source establishes:</b> ${esc(route.established)}</p><p><b>Decision still unresolved:</b> ${esc(route.decision_gap)}</p><p><b>Next test:</b> ${esc(route.gate_to_test)}</p>`+
 `<p class="small">Reference evidence applies across the three decision packs. Cell/year scenario controls do not turn it into target operating data.</p>`+
 (matched.length?`<div id="learning-qualification-sources">${refButtons(refsVisible)}</div>`:empty('The route sources are outside the current evidence filters. Clear the filters to inspect them.'))+
 `<details><summary>Inspect the qualification chain and three service boundaries</summary><ol>${d.qualification_gate_contract.stages.map(s=>`<li>${esc(s)}</li>`).join('')}</ol>`+
 table(Object.entries(d.qualification_gate_contract.three_pack_application).map(([pack,boundary])=>({pack,boundary})),[['pack','Decision pack',title],['boundary','Acceptance to preserve',esc]])+`</details>`+
 `<details><summary>Prepared challenges, not additional completed replays</summary>${table(d.qualification_gate_contract.next_counterfactuals,[['name','Challenge',esc],['intervention','Intervention',esc],['required_conservation','What must remain accounted for',esc]])}</details>`+
 `<details><summary>Inspect source versions, conflicts and full quantities</summary><pre>${esc(JSON.stringify({source_snapshot_sha256:packet.sha256,evidence:d.evidence.filter(r=>route.evidence_refs.includes(r.evidence_id))},null,2))}</pre></details>`+
 `<p><button id="export-learning-qualification">Export selected evidence route</button> <a href="/research/learning_qualification.md" target="_blank">R&D and qualification analysis ↗</a></p><p class="small">This export is an evidence snapshot with source fingerprints and limits. Scenario reload continues to use scenario files; source facts remain fixed.</p></section>`;
}
function buildLearningQualificationEvents(){
 document.addEventListener('change',e=>{if(e.target.id==='learning-qualification-route'){
  const routes=learningQualificationPacket()?.data?.qualification_routes||[];
  if(routes.some(r=>r.route_id===e.target.value)){learningQualificationRoute=e.target.value;render();}
 }});
 document.addEventListener('click',e=>{if(e.target.id==='export-learning-qualification'){
  const p=learningQualificationPacket(),d=p.data,route=d.qualification_routes.find(r=>r.route_id===learningQualificationRoute);
  download('learning-qualification-'+route.route_id+'.json',JSON.stringify({schema_version:'learning-qualification-evidence/0.1',source_package:p.path,source_snapshot_sha256:p.sha256,route,evidence:d.evidence.filter(r=>route.evidence_refs.includes(r.evidence_id)),qualification_contract:d.qualification_gate_contract,scope:d.qualification_followup},null,2),'application/json');
 }});
}
