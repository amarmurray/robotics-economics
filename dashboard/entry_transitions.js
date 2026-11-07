'use strict';
let entryTransitionState={data:null,loading:false,selection:'share_acquisition',current:null,inputs:null,error:'',requestId:0,imported:false};
function entryTransitionPanel(){
 const state=entryTransitionState;
 if(!state.data&&!state.loading&&!state.error){state.loading=true;fetch('/api/entry-transitions').then(async response=>{const data=await response.json();if(!response.ok)throw Error(data.error||'Entry transitions unavailable');state.data=data;state.inputs=data.case_inputs[state.selection];}).catch(error=>state.error=error.message).finally(()=>{state.loading=false;if(activeView==='customer')render();});}
 const opening='<section id="entry-transitions"><h3>Build, acquire or combine</h3>';
 if(!state.data)return opening+empty(state.error||'Settling ownership and operating obligations…')+'</section>';
 const r=state.current||state.data.cases[state.selection],a=r.entry_transition,c=a.cash,t=a.inputs,cents=v=>'$'+fmt(v/100,2),num=q=>Number(q.numerator)/Number(q.denominator);
 const field=(key,label,value,money=true)=>`<label>${esc(label)}<input data-et-key="${key}" data-et-kind="${money?'money':'integer'}" type="number" min="0" step="${money?'.01':'1'}" value="${money?value/100:value}"></label>`;
 const growth=r.enterprise.inputs.equity.filter(x=>x.funder_actor==='platform_buyer'&&x.recipient_actor==='entrant').reduce((s,x)=>s+x.amount_cents,0);
 const controls=state.imported?'<p>Complete saved company, physical, contract and Treasury inputs were replayed. Choose a standard witness to edit shortcut terms.</p>':`<details><summary>Edit purchase, working capital and transition terms</summary><div class="grid">${field('buyer_cash_cents','Buyer opening cash, USD',c.buyer_opening_cents)}${field('target_cash_cents','Target opening operating cash, USD',c.target_opening_cents)}${field('price_cents','Share consideration to seller, USD',t.price_cents)}${field('target_equity_cents','Separate target working-capital injection, USD',t.target_equity_cents)}${field('diligence_cents','Committed diligence bill, USD',t.diligence_cents)}${field('transition_cents','Conditional transition resources, USD',t.transition_cents)}${field('close_month','Scheduled closing month (0–7)',t.close_month,false)}${field('disruption_months','Assumed service interruption, months (0–8)',t.disruption_months,false)}${['build','hybrid'].includes(t.mode)?field('growth_equity_cents','Separate growth-company equity, USD',growth):''}</div><label><input data-et-key="assumed_transfer_consent" data-et-kind="boolean" type="checkbox" ${t.assumed_transfer_consent?'checked':''}> Assume required transfer consent and operating rights are available</label><p><button id="apply-entry-transition">Apply entry terms</button></p></details>`;
 return opening+notice('Synthetic share acquisition. The target company keeps its customers, leased robots, receivables and liabilities. Purchase money goes to the seller; operating cash needs a separate funded injection. Growth is separately committed. No asset purchase, legal conclusion, valuation, synergy or ROI is inferred.')+
 `<label>Entry route witness<select id="entry-transition-case">${Object.keys(state.data.cases).map(k=>`<option value="${k}" ${state.selection===k?'selected':''}>${esc(title(k))}</option>`).join('')}${['custom','imported'].includes(state.selection)?`<option value="${state.selection}" selected>${state.imported?'Imported replay':'Custom terms'}</option>`:''}</select></label>`+controls+
 `<p id="entry-transition-input-state" class="small" role="status">${esc(state.error||'Display and export use the last applied case. Owned-company cash is separate from buyer cash.')}</p><div class="grid">${metric('Closing',title(a.close_status),a.closed_month===null?'No ownership transfer':'Ownership changes in month '+a.closed_month)}${metric('Accepted zones',fmt(r.enterprise.months.reduce((s,m)=>s+num(m.total_delivered_units),0),2),'Existing demand ledger; ownership creates no service')}${metric('Buyer closing cash',cents(c.buyer_closing_cents),'Excludes target-company cash and unknown share value')}</div>`+
 `<p>Paid seller consideration: <strong>${cents(c.paid_share_price_cents)}</strong>. Target working equity: ${cents(c.paid_target_equity_cents)}. Separate growth equity: ${cents(c.paid_growth_equity_cents)}. Transaction resource bills paid: ${cents(c.paid_diligence_cents+c.paid_transition_resources_cents)}.</p>`+
 table(a.months.map((m,i)=>({...m,owner:title(m.ultimate_owners.incumbent),accepted:num(r.enterprise.months[i].total_delivered_units)})),[['month','Month'],['owner','Target ultimate owner',esc],['accepted','Accepted zones',v=>fmt(v,2)],['target_cash_cents','Target cash',cents],['buyer_cash_cents','Buyer cash',cents],['target_due_unpaid_cents','Target due unpaid',cents],['target_disrupted','Service interrupted',v=>v?'Yes':'No']])+
 `<details><summary>Compare fifteen complete entry worlds</summary>${table(state.data.summary,[['case','World',v=>esc(title(v))],['close_status','Closing',v=>esc(title(v))],['accepted_zones','Accepted zones',v=>fmt(num(v),2)],['paid_share_price_cents','Paid share price',cents],['paid_staff_cents','Paid staff',cents],['external_operating_and_transaction_cash_cents','External cash outlays',cents]])}<p>${esc(state.data.comparison_boundary)}</p></details><details><summary>Trace ownership, unchanged leases, funding and liabilities</summary><pre>${esc(JSON.stringify({terms:t,events:a.events,months:a.months,entry_invoices:a.entry_invoices,cash:c,consolidation:a.consolidation,source_sha256:r.source_sha256},null,2))}</pre></details><p><button id="export-entry-transition">Export entry case</button> <label>Reload entry case<input id="import-entry-transition" type="file" accept="application/json,.json"></label></p><p class="small">Case ${esc(r.case_hash.slice(0,14))}. <a href="/model/ENTRY_TRANSITIONS.md" target="_blank">Methods and limits ↗</a> · <a href="/research/entry_transitions.md" target="_blank">Decision findings ↗</a></p></section>`;
}
function buildEntryTransitionEvents(){
 const state=entryTransitionState;
 const fail=message=>{state.error=message+' Display and export retain the last valid case.';if($('entry-transition-input-state'))setText('entry-transition-input-state',state.error);};
 const calculate=async(body,selection,id)=>{
  if($('entry-transition-input-state'))setText('entry-transition-input-state','Settling entry terms and operating obligations…');
  try{const response=await fetch('/api/entry-transitions',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(body)}),data=await response.json();if(id!==state.requestId)return;if(!response.ok)throw Error(data.error||'Entry calculation failed');state.current=data.result;state.inputs=body.inputs||null;state.selection=selection;state.imported=selection==='imported';state.error=body.saved_case&&body.saved_case.case_hash!==data.result.case_hash?'Recomputed under current source and complete inputs; saved hash differs.':'';if(activeView==='customer')render();}catch(error){if(id===state.requestId)fail(error.message);}
 };
 document.addEventListener('click',e=>{
  if(e.target.id==='export-entry-transition'&&state.data){const r=state.current||state.data.cases[state.selection];download('entry-transition-'+r.case_hash.slice(0,10)+'.json',JSON.stringify(r,null,2),'application/json');}
  if(e.target.id!=='apply-entry-transition')return;
  const id=++state.requestId;
  try{const inputs={...state.inputs};
   for(const field of document.querySelectorAll('#entry-transitions [data-et-key]')){
    const key=field.dataset.etKey,kind=field.dataset.etKind,raw=field.value.trim();let value;
    if(kind==='boolean')value=field.checked;
    else if(kind==='money'){if(!/^\d+(\.\d{1,2})?$/.test(raw))throw Error('Money requires nonnegative USD with at most two decimals.');const parts=raw.split('.');value=Number(parts[0])*100+Number((parts[1]||'').padEnd(2,'0'));if(!Number.isSafeInteger(value))throw Error('Money exceeds exact range.');}
    else{value=Number(raw);if(raw===''||!Number.isSafeInteger(value)||value<0)throw Error('Timing requires nonnegative whole months.');}
    inputs[key]=value;
   }
   calculate({inputs},'custom',id);
  }catch(error){fail(error.message);}
 });
 document.addEventListener('change',async e=>{
  if(e.target.id==='entry-transition-case'&&state.data&&Object.hasOwn(state.data.cases,e.target.value)){++state.requestId;state.selection=e.target.value;state.inputs=state.data.case_inputs[e.target.value];state.current=null;state.error='';state.imported=false;render();}
  if(e.target.id==='import-entry-transition'){const id=++state.requestId;try{const file=e.target.files[0];if(!file)return;const saved=JSON.parse(await file.text());if(id===state.requestId)await calculate({saved_case:saved},'imported',id);}catch(error){if(id===state.requestId)fail('Import error: '+error.message);}}
 });
 document.addEventListener('input',e=>{if(e.target.dataset.etKey&&$('entry-transition-input-state'))setText('entry-transition-input-state','Edits are pending. Apply to recompute; export retains the displayed case.');});
}
