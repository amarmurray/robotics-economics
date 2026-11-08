'use strict';
let renewingEntryState={data:null,current:null,selection:'hybrid',inputs:{},imported:false,loading:false,error:'',requestId:0};
function renewingEntryPanel(){
 const s=renewingEntryState,visible=()=>['customer','commercial'].includes(activeView);
 if(!s.data&&!s.loading&&!s.error){s.loading=true;fetch('/api/renewing-entry').then(async r=>{const d=await r.json();if(!r.ok)throw Error(d.error||'Entry and renewals unavailable');s.data=d;s.current=d.cases.hybrid;}).catch(e=>s.error=e.message).finally(()=>{s.loading=false;if(visible())render();});}
 const head='<section id="renewing-entry"><h3>Buying a company and winning its customers are different events</h3>';
 if(!s.data)return head+empty(s.error||'Loading funded entry and customer renewals…')+'</section>';
 const r=s.current,a=r.entry_transition,g=r.renewing_entry,c=a.cash,q=v=>Number(v.numerator)/Number(v.denominator),cash=v=>'$'+fmt(v/100,2);
 const field=(key,label,value,money=true)=>`<label>${esc(label)}<input data-re-key="${key}" data-re-money="${money}" type="number" min="0" step="${money?'.01':'1'}" value="${money?value/100:value}"></label>`;
 const controls=s.imported?'<p>Complete opening inputs were replayed. Select a standard world to edit shortcut controls.</p>':`<details id="renewing-entry-controls"><summary>Edit acquisition funding, disruption and contract length</summary><div class="grid">${field('buyer_cash_cents','Parent opening cash, USD',c.buyer_opening_cents)}${field('target_equity_cents','Separate target cash injection, USD',a.inputs.target_equity_cents)}${field('disruption_months','Declared target interruption, months',a.inputs.disruption_months,false)}${field('term_months','Renewal contract length, months',r.competition.inputs.term_months,false)}</div><button id="apply-renewing-entry">Apply and recompute</button></details>`;
 return head+notice('Synthetic share closing and actual recurring contracts share one physical and cash execution. The parent, target and growth company keep separate accounts. Common ownership retains declared separate offer mandates; this is not independent competition, optimal pricing or a valuation.',true)+
 `<label>Entry and renewal world<select id="renewing-entry-case">${Object.keys(s.data.case_inputs).map(k=>`<option value="${k}" ${s.selection===k?'selected':''}>${esc(title(k))}</option>`).join('')}${['custom','imported'].includes(s.selection)?`<option selected value="${s.selection}">${esc(title(s.selection))}</option>`:''}</select></label>`+controls+
 `<p id="renewing-entry-state" role="status" class="small">${esc(s.error||'Display and export use applied inputs. Annual scenario controls do not change this separate execution.')}</p>`+
 `<div class="grid">${metric('Company closing',title(a.close_status),'Seller proceeds are separate from target working cash')}${metric('Accepted zones',fmt(r.enterprise.months.reduce((n,m)=>n+q(m.total_delivered_units),0),2),'One conserved '+r.enterprise.inputs.market.baseline_units+'-zone monthly obligation')}${metric('Contracts reclassified at close',g.contracts_reclassified_at_share_close.reduce((n,x)=>n+x.units,0),'Assigned zones per period; not new service or customer wins')}${metric('New platform contract volume',g.months.reduce((n,m)=>n+m.new_platform_contract_units,0),'First awarded lot volume; excludes equity reclassification and regained work')}</div>`+
 table(g.months.map((m,i)=>({...m,target_disrupted:a.months[i].target_disrupted})),[['month','Month'],['common_owner_of_active_firms','Common owner',v=>v?'Yes':'No'],['platform_assigned_units','Platform assigned'],['platform_delivered_zones','Platform delivered',v=>fmt(q(v),2)],['new_platform_contract_units','New lot volume'],['intra_platform_reassigned_units','Internal reassignment'],['target_disrupted','Target interrupted',v=>v?'Yes':'No'],['parent_available_cash_cents','Parent available USD',cash]])+
 `<details id="renewing-entry-comparison"><summary>Compare ten complete entry and renewal executions</summary>${table(s.data.summary,[['case','World',v=>esc(title(v))],['close_status','Closing',v=>esc(title(v))],['complete_months','Complete months'],['accepted_zones','Accepted zones',v=>fmt(q(v),2)],['equity_reclassified_contract_units','Equity reclassification'],['new_platform_contract_units','New lot volume'],['buyer_closing_cents','Parent cash USD',cash],['external_operating_and_transaction_cash_cents','Resource/transaction cash USD',cash]])}<p>${esc(s.data.comparison_boundary)}</p></details>`+
 `<details id="renewing-entry-ledger"><summary>Inspect closing, renewal, liability and ownership records</summary><p>Gross awards from outside or unassigned contracts may include regained work. New contract-lot IDs are counted only once and exclude equity reclassification. Neither metric counts unique people.</p><pre>${esc(JSON.stringify({joint:g,entry:a,renewals:r.competition,source_sha256:r.source_sha256},null,2))}</pre></details>`+
 `<p><button id="export-renewing-entry">Export complete joint case</button> <label>Reload joint case<input id="import-renewing-entry" type="file" accept="application/json,.json"></label></p><p class="small">Case ${esc(r.case_hash.slice(0,14))}. <a href="/research/entry_transitions.md#actual-renewal-and-company-entry-edition-038" target="_blank">Decision findings ↗</a> · <a href="/model/ENTRY_TRANSITIONS.md" target="_blank">Methods ↗</a></p></section>`;
}
function buildRenewingEntryEvents(){
 const s=renewingEntryState,visible=()=>['customer','commercial'].includes(activeView);
 const fail=message=>{s.error=message+' Display and export retain the last applied case.';if($('renewing-entry-state'))setText('renewing-entry-state',s.error);};
 const calculate=async(body,selection,id)=>{
  if($('renewing-entry-state'))setText('renewing-entry-state','Recomputing share settlement, funded service and customer renewals…');
  try{const response=await fetch('/api/renewing-entry',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(body)}),data=await response.json();if(id!==s.requestId)return;if(!response.ok)throw Error(data.error||'Joint entry calculation failed');s.current=data.result;s.inputs=body.inputs||{};s.selection=selection;s.imported=selection==='imported';s.error=body.saved_case&&body.saved_case.case_hash!==data.result.case_hash?'Recomputed from full opening inputs; saved hash differs.':'';if(visible())render();}catch(e){if(id===s.requestId)fail(e.message);}
 };
 document.addEventListener('click',e=>{
  if(e.target.id==='export-renewing-entry'&&s.current)download('renewing-entry-'+s.current.case_hash.slice(0,10)+'.json',JSON.stringify(s.current,null,2),'application/json');
  if(e.target.id!=='apply-renewing-entry')return;const id=++s.requestId;
  try{const x=structuredClone(s.inputs);x.transition=x.transition||{};x.market=x.market||{};x.market.competition=x.market.competition||{};
   for(const field of document.querySelectorAll('#renewing-entry [data-re-key]')){const raw=field.value.trim(),key=field.dataset.reKey;let value;
    if(field.dataset.reMoney==='true'){if(!/^\d+(\.\d{1,2})?$/.test(raw))throw Error('Use nonnegative USD with at most two decimals.');const parts=raw.split('.');value=Number(parts[0])*100+Number((parts[1]||'').padEnd(2,'0'));}
    else value=Number(raw);
    if(raw===''||!Number.isSafeInteger(value)||value<0)throw Error('Exact nonnegative money and whole months are required.');
    if(key==='buyer_cash_cents')x[key]=value;else if(key==='term_months')x.market.competition[key]=value;else x.transition[key]=value;
   }calculate({inputs:x},'custom',id);
  }catch(e){fail(e.message);}
 });
 document.addEventListener('change',async e=>{
  if(e.target.id==='renewing-entry-case'&&s.data&&Object.hasOwn(s.data.case_inputs,e.target.value)){const id=++s.requestId;await calculate({inputs:s.data.case_inputs[e.target.value]},e.target.value,id);}
  if(e.target.id==='import-renewing-entry'){const id=++s.requestId;try{const f=e.target.files[0];if(!f)return;if(f.size>8000000)throw Error('Joint case files are limited to8 MB.');const saved=JSON.parse(await f.text());if(id===s.requestId)await calculate({saved_case:saved},'imported',id);}catch(e){if(id===s.requestId)fail('Import error: '+e.message);}}
 });
 document.addEventListener('input',e=>{if(e.target.dataset.reKey){++s.requestId;if($('renewing-entry-state'))setText('renewing-entry-state','Edits are pending. Apply to recompute; export retains the displayed case.');}});
}
