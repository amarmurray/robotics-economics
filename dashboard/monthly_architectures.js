'use strict';
let monthlyArchitectureState={data:null,loading:false,selection:'licensed_independent',current:null,inputs:null,error:'',requestId:0,imported:false};

function monthlyArchitecturePanel(){
 const state=monthlyArchitectureState;
 if(!state.data&&!state.loading&&!state.error){
  state.loading=true;
  fetch('/api/monthly-architectures').then(async response=>{const data=await response.json();if(!response.ok)throw Error(data.error||'Monthly architecture execution unavailable');state.data=data;state.inputs=data.case_inputs[state.selection];}).catch(error=>state.error=error.message).finally(()=>{state.loading=false;if(activeView==='commercial')render();});
 }
 const opening='<section id="monthly-architectures"><h3>Funded intelligence architectures</h3>';
 if(!state.data)return opening+empty(state.error||'Calculating monthly roles, resources and cash…')+'</section>';
 const r=state.current||state.data.cases[state.selection],a=r.architecture_execution,x=a.inputs,number=q=>Number(q.numerator)/Number(q.denominator),cents=v=>'$'+fmt(v/100,2);
 const service=r.enterprise.months.reduce((sum,m)=>sum+number(m.total_delivered_units),0),robots=r.enterprise.months.reduce((sum,m)=>sum+m.operators.reduce((n,o)=>n+number(o.robot_delivered_units),0),0);
 const field=(group,key,label,kind,value)=>`<label>${esc(label)}<input data-ma-group="${group}" data-ma-key="${key}" data-ma-kind="${kind}" type="number" min="0" step="${kind==='integer'?'1':'.01'}" value="${kind==='money'?value/100:value}"></label>`;
 const controls=state.imported?'<p>Complete saved physical, role and cash inputs were replayed. Select a witness to edit shortcut controls.</p>':`<details><summary>Edit fees, capital and qualification capacity</summary><div class="grid">${field('common','model_fee_usd_year','Model fee per supported robot-year, USD','usd',a.effective_settings.common.model_fee_usd_year)}${field('root','service_cents_per_accepted_zone','Customer-to-operator price per accepted zone, USD','money',x.service_cents_per_accepted_zone)}${field('root','engineering_hours_per_month','Architecture engineering hours per month','integer',x.engineering_hours_per_month)}${field('root','demonstration_hours_per_month','Additional demonstration hours per month','integer',x.demonstration_hours_per_month)}${['customer','operator','oem','model_supplier','integrator'].map(role=>field('cash',role,title(role)+' logical-role opening cash, USD','money',x.role_opening_cash_cents[role])).join('')}</div><label><input data-ma-group="profile" data-ma-key="assume_rights_available" data-ma-kind="boolean" type="checkbox" ${a.profile.assume_rights_available?'checked':''}> Assume model rights are available for this scenario</label><p><button id="apply-monthly-architectures">Apply funded architecture</button></p></details>`;
 const months=a.months.map((m,i)=>({month:m.month,service:number(r.enterprise.months[i].total_delivered_units),supported:r.months[i].support.used,qualified:m.qualified_unit_ids.length,engineering:number(m.engineering_hours_used),demonstrations:number(m.demonstration_hours_used)}));
 return opening+notice('Synthetic cleaning-service contracts with one active business. Actual role accounts pay resources and receive fees; internal payments cancel. Qualification, prices and rights are assumptions. Fixed staffing stays paid, and these cash windows do not rank lifetime investments.')+
 `<label>Monthly architecture witness<select id="monthly-architecture-case">${Object.keys(state.data.cases).map(k=>`<option value="${k}" ${state.selection===k?'selected':''}>${esc(title(k))}</option>`).join('')}${['custom','imported'].includes(state.selection)?`<option value="${state.selection}" selected>${state.imported?'Imported replay':'Custom assumptions'}</option>`:''}</select></label>`+controls+
 `<p id="monthly-architecture-input-state" class="small" role="status">${esc(state.error||'Display and export use the last applied case. Real product qualification and whole-system economics remain unknown.')}</p><p>Robot policy: <strong>${esc(title(a.status))}</strong>. ${a.failed_assumptions.length?'Unmet scenario premises: '+esc(a.failed_assumptions.join(', '))+'. Paid human fallback is reported separately.':''}</p><div class="grid">${metric('Accepted zones',fmt(service,2),'Same demand ledger; no double-counted activity')}${metric('Robot-delivered zones',fmt(robots,2),'Actual supported, qualified cohorts')}${metric('Paid external bills',cents(a.consolidation.external_physical_and_enterprise_cash_cents),'Includes physical, staff and itemized architecture resources once')}</div>`+
 table(a.entities,[['actor_id','Legal account',esc],['roles','Logical roles',v=>esc(v.join(', '))],['opening_cash_cents','Opening cash',cents,true],['closing_cash_cents','Closing cash',cents,true],['due_unpaid_cents','Due unpaid',cents,true]])+
 table(months,[['month','Month'],['service','Accepted zones',v=>fmt(v,2)],['supported','Supported robots'],['qualified','Units with initial qualification'],['engineering','Architecture engineering hours',v=>fmt(v,2)],['demonstrations','Additional demonstration hours',v=>fmt(v,2)]])+
 `<details><summary>Trace obligations, resource bills and eliminated transfers</summary><pre>${esc(JSON.stringify({contract:a.contract,inputs:a.inputs,role_entities:a.role_entities,cash_lines:a.cash_lines,consolidation:a.consolidation,events:a.events,source_sha256:r.source_sha256},null,2))}</pre></details><details><summary>Compare ten complete architecture worlds</summary>${table(state.data.summary,[['case','World',v=>esc(title(v))],['accepted_zones','Accepted zones',v=>fmt(number(v),2)],['robot_zones','Robot zones',v=>fmt(number(v),2)],['staff_cash_paid_cents','Paid staff',cents],['supported_robot_months','Supported robot-months'],['qualified_units','Qualified units'],['external_physical_and_enterprise_cash_cents','Paid external bills',cents]])}<p>${esc(state.data.comparison_boundary)}</p></details><p><button id="export-monthly-architecture">Export monthly architecture</button> <label>Reload monthly architecture<input id="import-monthly-architecture" type="file" accept="application/json,.json"></label></p><p class="small">Case ${esc(r.case_hash.slice(0,14))}. <a href="/model/MONTHLY_ARCHITECTURES.md" target="_blank">Methods and limitations ↗</a></p></section>`;
}

function buildMonthlyArchitectureEvents(){
 const state=monthlyArchitectureState;
 const fail=message=>{state.error=message+' Display and export retain the last valid case.';if($('monthly-architecture-input-state'))setText('monthly-architecture-input-state',state.error);};
 const calculate=async(body,selection,id)=>{
  if($('monthly-architecture-input-state'))setText('monthly-architecture-input-state','Calculating funded roles and resource qualification…');
  try{const response=await fetch('/api/monthly-architectures',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(body)}),data=await response.json();if(id!==state.requestId)return;if(!response.ok)throw Error(data.error||'Monthly architecture calculation failed');state.current=data.result;state.inputs=data.inputs;state.selection=selection;state.imported=selection==='imported';state.error=body.saved_case&&body.saved_case.case_hash!==data.result.case_hash?'Recomputed under current source and complete inputs; saved hash differs.':'';if(activeView==='commercial')render();}catch(error){if(id===state.requestId)fail(error.message);}
 };
 document.addEventListener('click',e=>{
  if(e.target.id==='export-monthly-architecture'&&state.data){const r=state.current||state.data.cases[state.selection];download('monthly-architecture-'+r.case_hash.slice(0,10)+'.json',JSON.stringify(r,null,2),'application/json');}
  if(e.target.id!=='apply-monthly-architectures')return;
  const id=++state.requestId;
  try{const r=state.current||state.data.cases[state.selection],inputs=JSON.parse(JSON.stringify(state.inputs));inputs.architecture_inputs=JSON.parse(JSON.stringify(r.architecture_execution.inputs));const a=inputs.architecture_inputs;
   for(const field of document.querySelectorAll('#monthly-architectures [data-ma-key]')){
    const key=field.dataset.maKey,group=field.dataset.maGroup,kind=field.dataset.maKind,raw=field.value.trim();let value;
    if(kind==='boolean')value=field.checked;
    else if(kind==='money'||kind==='usd'){if(!/^\d+(\.\d{1,2})?$/.test(raw))throw Error('Money requires nonnegative USD with at most two decimals.');const parts=raw.split('.'),cents=Number(parts[0])*100+Number((parts[1]||'').padEnd(2,'0'));if(!Number.isSafeInteger(cents))throw Error('Money exceeds exact integer range.');value=kind==='money'?cents:cents/100;}
    else {value=Number(raw);if(raw===''||!Number.isSafeInteger(value)||value<0)throw Error('Resource capacity requires nonnegative whole hours.');}
    if(group==='root')a[key]=value;else if(group==='cash')a.role_opening_cash_cents[key]=value;else if(group==='common')a.architecture_overrides.common[key]=value;else a.architecture_overrides.profiles[a.architecture_id][key]=value;
   }
   calculate({inputs},'custom',id);
  }catch(error){fail(error.message);}
 });
 document.addEventListener('change',async e=>{
  if(e.target.id==='monthly-architecture-case'&&state.data&&Object.hasOwn(state.data.cases,e.target.value)){++state.requestId;state.selection=e.target.value;state.inputs=state.data.case_inputs[e.target.value];state.current=null;state.error='';state.imported=false;render();}
  if(e.target.id==='import-monthly-architecture'){const id=++state.requestId;try{const file=e.target.files[0];if(!file)return;const saved=JSON.parse(await file.text());if(id===state.requestId)await calculate({saved_case:saved},'imported',id);}catch(error){if(id===state.requestId)fail('Import error: '+error.message);}}
 });
 document.addEventListener('input',e=>{if(e.target.dataset.maKey&&$('monthly-architecture-input-state'))setText('monthly-architecture-input-state','Edits are pending. Apply to recompute; export retains the displayed case.');});
}
