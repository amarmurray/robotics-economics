'use strict';
let coordinationState={data:null,loading:false,selection:'mixed_exact',current:null,error:'',requestId:0,imported:false};

function conventionalCoordinationPanel(){
 const state=coordinationState;
 if(!state.data&&!state.loading&&!state.error){state.loading=true;fetch('/api/conventional-coordination').then(async response=>{const data=await response.json();if(!response.ok)throw Error(data.error||'Coordination unavailable');state.data=data;}).catch(error=>state.error=error.message).finally(()=>{state.loading=false;if(activeView==='learning')render();});}
 const opening='<section id="conventional-coordination"><h3>Competent conventional coordination</h3>';
 if(!state.data)return opening+empty(state.error||'Planning the observed service queue…')+'</section>';
 const r=state.current||state.data.cases[state.selection],s=r.summary,w=r.workload,c=r.controller,cents=v=>'$'+fmt(v/100,2);
 const field=(group,key,label,value,money=false)=>`<label>${esc(label)}<input data-cc-group="${group}" data-cc-key="${key}" data-cc-kind="${money?'money':'integer'}" type="number" min="0" step="${money?'.01':'1'}" value="${money?value/100:value}"></label>`;
 const controls=state.imported||c.fixed_proposals!==null?'<p>This complete saved or adversarial proposal case is read-only here. Choose a standard witness to edit assumptions.</p>':`<details><summary>Edit response time, paid capacity and cash</summary><div class="grid">${field('controller','latency_ticks','Proposal delay, ticks (0–3)',c.latency_ticks)}${field('controller','planning_cents_per_slot','Planning capacity per decision slot, USD',c.planning_cents_per_slot,true)}${field('controller','verification_cents_per_slot','Verification capacity per slot, USD',c.verification_cents_per_slot,true)}${field('workload','opening_cash_cents','Opening service cash, USD',w.opening_cash_cents,true)}</div><label><input data-cc-group="controller" data-cc-key="urgent_fast_path" data-cc-kind="boolean" type="checkbox" ${c.urgent_fast_path?'checked':''}> Immediate conventional urgent path</label><label><input data-cc-group="workload" data-cc-key="robot_available" data-cc-kind="boolean" type="checkbox" ${w.robot_available?'checked':''}> Robot is available under the declared operating contract</label><label><input data-cc-group="workload" data-cc-key="urgent_courier_reserve" data-cc-kind="reserve" type="checkbox" ${w.urgent_courier_reserve[1]>w.urgent_courier_reserve[0]?'checked':''}> Reserve courier ticks 2–4 for urgent work</label><p><button id="apply-coordination">Apply coordination assumptions</button></p></details>`;
 const events=r.events.map(e=>({tick:e.tick,event:title(e.kind),request:e.request_id||'Robot availability',detail:e.kind==='started'?e.mode_id+'; finishes at '+e.finish:e.kind==='observed_robot_outage'?'Unavailable until '+e.unavailable_until+(e.recovery_paid?'; recovery funded':'; recovery unfunded'):'Accepted once'}));
 return opening+notice('Synthetic courier window, not observed hospital performance. Both policies can plan and replan the same visible queue under the same resource and cash guard. Proposal variants use this same exact solver with stated delay and cost; no LLM is evaluated. Mandatory service is a separate gate, and paid staffing remains.')+
 `<label>Conventional comparison witness<select id="coordination-case">${Object.keys(state.data.cases).map(k=>`<option value="${k}" ${state.selection===k?'selected':''}>${esc(title(k))}</option>`).join('')}${['custom','imported'].includes(state.selection)?`<option value="${state.selection}" selected>${state.imported?'Imported replay':'Custom assumptions'}</option>`:''}</select></label>`+controls+
 `<p id="coordination-input-state" class="small" role="status">${esc(state.error||'Display and export use the last applied case. Exactness covers the currently observed bounded queue, not unknown future events.')}</p><div class="grid">${metric('Accepted requests',s.accepted+' / '+s.requested,'Unique completions by their declared deadline')}${metric('Mandatory service gate',s.mandatory_service_gate_met?'Met':'Missed',s.mandatory_accepted+' / '+s.mandatory_requested+' mandatory requests accepted')}${metric('Paid window resources',cents(s.paid_resource_cents),'Includes '+cents(s.paid_staff_cents)+' paid staffing; excludes asset lifecycle cost')}</div>`+
 `<p>${w.horizon} ticks × ${w.tick_minutes} assumed minutes. ${s.attempts_started} attempts started; ${s.failed_attempts} failed attempts. ${s.controller_calls} proposal calls within ${s.declared_decision_slots} booked decision slots. ${s.unfunded_required_capacity?'Required window capacity is unfunded; service is blocked.':''}</p>`+
 table(events,[['tick','Tick'],['event','Observed event',esc],['request','Request',esc],['detail','Result',esc]])+
 `<details><summary>Compare twelve complete service-window worlds</summary>${table(state.data.summary,[['case','World',v=>esc(title(v))],['accepted','Accepted'],['mandatory_service_gate_met','Mandatory gate',v=>v?'Met':'Missed'],['failed_attempts','Failed attempts'],['paid_resource_cents','Paid resources',cents],['paid_staff_cents','Paid staff',cents]])}<p>${esc(state.data.comparison_boundary)}</p></details><details><summary>Trace visible queues, proposals, authority and all-attempt bills</summary><pre>${esc(JSON.stringify({workload:w,controller:c,observations:r.observations,proposals:r.proposals,admissions:r.admissions,failed_attempts:r.failed_attempts,cost_lines:r.cost_lines,source_sha256:r.source_sha256},null,2))}</pre></details><p><button id="export-coordination">Export coordination case</button> <label>Reload coordination case<input id="import-coordination" type="file" accept="application/json,.json"></label></p><p class="small">Case ${esc(r.case_hash.slice(0,14))}. <a href="/model/CONVENTIONAL_COORDINATION.md" target="_blank">Methods and exclusions ↗</a> · <a href="/research/conventional_coordination.md" target="_blank">Decision findings ↗</a></p></section>`;
}

function buildCoordinationEvents(){
 const state=coordinationState;
 const fail=message=>{state.error=message+' Display and export retain the last valid case.';if($('coordination-input-state'))setText('coordination-input-state',state.error);};
 const calculate=async(body,selection,id)=>{
  if($('coordination-input-state'))setText('coordination-input-state','Replanning visible work and checking execution…');
  try{const response=await fetch('/api/conventional-coordination',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(body)}),data=await response.json();if(id!==state.requestId)return;if(!response.ok)throw Error(data.error||'Coordination calculation failed');state.current=data.result;state.selection=selection;state.imported=selection==='imported';state.error=body.saved_case&&body.saved_case.case_hash!==data.result.case_hash?'Recomputed from complete inputs under current source; saved hash differs.':'';if(activeView==='learning')render();}catch(error){if(id===state.requestId)fail(error.message);}
 };
 document.addEventListener('click',e=>{
  if(e.target.id==='export-coordination'&&state.data){const r=state.current||state.data.cases[state.selection];download('conventional-coordination-'+r.case_hash.slice(0,10)+'.json',JSON.stringify(r,null,2),'application/json');}
  if(e.target.id!=='apply-coordination')return;
  const id=++state.requestId;
  try{const r=state.current||state.data.cases[state.selection],inputs=JSON.parse(JSON.stringify({workload:r.workload,controller:r.controller}));
   for(const field of document.querySelectorAll('#conventional-coordination [data-cc-key]')){
    const group=field.dataset.ccGroup,key=field.dataset.ccKey,kind=field.dataset.ccKind,raw=field.value.trim();let value;
    if(kind==='boolean')value=field.checked;
    else if(kind==='reserve')value=field.checked?[2,4]:[0,0];
    else if(kind==='money'){if(!/^\d+(\.\d{1,2})?$/.test(raw))throw Error('Money requires nonnegative USD with at most two decimals.');const parts=raw.split('.');value=Number(parts[0])*100+Number((parts[1]||'').padEnd(2,'0'));if(!Number.isSafeInteger(value))throw Error('Money exceeds exact range.');}
    else{value=Number(raw);if(raw===''||!Number.isSafeInteger(value)||value<0)throw Error('Delay requires a nonnegative whole number.');}
    inputs[group][key]=value;
   }
   calculate({inputs},'custom',id);
  }catch(error){fail(error.message);}
 });
 document.addEventListener('change',async e=>{
  if(e.target.id==='coordination-case'&&state.data&&Object.hasOwn(state.data.cases,e.target.value)){++state.requestId;state.selection=e.target.value;state.current=null;state.error='';state.imported=false;render();}
  if(e.target.id==='import-coordination'){const id=++state.requestId;try{const file=e.target.files[0];if(!file)return;const saved=JSON.parse(await file.text());if(id===state.requestId)await calculate({saved_case:saved},'imported',id);}catch(error){if(id===state.requestId)fail('Import error: '+error.message);}}
 });
 document.addEventListener('input',e=>{if(e.target.dataset.ccKey&&$('coordination-input-state'))setText('coordination-input-state','Edits are pending. Apply to recompute; export retains the displayed case.');});
}
