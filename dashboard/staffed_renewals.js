'use strict';
let staffedRenewalsState={data:null,current:null,selection:'complete_control',inputs:{},imported:false,loading:false,error:'',requestId:0};
function staffedRenewalsPanel(){
 const s=staffedRenewalsState,visible=()=>['customer','commercial'].includes(activeView);
 if(!s.data&&!s.loading&&!s.error){s.loading=true;fetch('/api/staffed-renewals').then(async r=>{const d=await r.json();if(!r.ok)throw Error(d.error||'Crew renewal cases unavailable');s.data=d;s.current=d.cases.complete_control;}).catch(e=>s.error=e.message).finally(()=>{s.loading=false;if(visible())render();});}
 const head='<section id="staffed-renewals"><h3>Winning work must fit the paid crew</h3>';
 if(!s.data)return head+empty(s.error||'Loading crew commitments and actual awards…')+'</section>';
 const r=s.current,w=r.staffed_renewals,crew=w.inputs.incumbent,q=v=>Number(v.numerator)/Number(v.denominator),cash=v=>'$'+fmt(v/100,2);
 const field=(key,label,value,money=false)=>`<label>${esc(label)}<input data-sr-key="${key}" data-sr-money="${money}" type="number" min="0" step="${money?'.01':'1'}" value="${money?value/100:value}"></label>`;
 const opening=r.opening_treasury.actors.find(a=>a.actor_id==='incumbent').cash_cents;
 const controls=s.imported?'<p>Complete opening inputs were replayed. Select a standard world to edit controls.</p>':`<details id="staffed-renewals-controls"><summary>Edit crew minutes and prospective overtime funding</summary><div class="grid">${field('target_cash_cents','Target opening cash, USD',opening,true)}${field('minutes_per_block','Qualified minutes per regular block',crew.minutes_per_block)}${field('overtime_minutes_per_month','Optional prepaid overtime block, minutes',crew.overtime_minutes_per_month)}</div><button id="apply-staffed-renewals">Apply and recompute</button></details>`;
 const months=r.enterprise.months.map(m=>({month:m.month,accepted:m.total_delivered_units,whole:q(m.total_delivered_units)===r.enterprise.inputs.market.baseline_units&&w.months.filter(x=>x.month===m.month).every(x=>x.complete_obligation)}));
 return head+notice('Synthetic crews, work rates and contract rules. Each operating company reserves local robot work and outside duties before bidding. Optional overtime is quoted earlier and prepaid before awards. Common ownership supplies neither another company’s crew nor its cash.',true)+
 `<label>Crew and renewal world<select id="staffed-renewals-case">${Object.keys(s.data.case_inputs).map(k=>`<option value="${k}" ${s.selection===k?'selected':''}>${esc(title(k))}</option>`).join('')}${['custom','imported'].includes(s.selection)?`<option selected value="${s.selection}">${esc(title(s.selection))}</option>`:''}</select></label>`+controls+
 `<p id="staffed-renewals-state" role="status" class="small">${esc(s.error||'Display and export use applied inputs. Annual scenario controls do not change this execution.')}</p>`+
 `<div class="grid">${metric('Complete whole-service months',months.filter(m=>m.whole).length+' / '+months.length,'Both cleaning and retained outside jobs must be complete')}${metric('Accepted cleaning zones',fmt(months.reduce((n,m)=>n+q(m.accepted),0),2),'Outside inventory jobs stay a separate unit')}${metric('Paid staffing and overtime',cash(w.cash.staff_paid_cents+w.cash.overtime_paid_cents),'Declared synthetic commitments, not measured payroll removal')}${metric('All-payer resource cash',cash(w.cash.all_payer_resource_and_transaction_cash_cents),'Resource and transaction payments; terminal assets and claims remain')}</div>`+
 table(w.months,[['month','Month'],['operator_id','Operator',esc],['scheduled_blocks','Paid blocks'],['funded_capacity_before_awards','Offer capacity',v=>fmt(q(v),2)],['cleaning_required_zones','Assigned zones'],['accepted_cleaning_zones','Accepted zones',v=>fmt(q(v),2)],['outside_required_jobs','Outside due'],['outside_completed_jobs','Outside done'],['overtime_paid_minutes','Extra minutes'],['unused_minutes','Unused minutes',v=>fmt(q(v),2)],['complete_obligation','All own duties',v=>v?'Yes':'No']])+
 `<details id="staffed-renewals-comparison"><summary>Compare ${s.data.summary.length} complete executions</summary>${table(s.data.summary,[['case','World',v=>esc(title(v))],['complete_market_months','Cleaning complete'],['complete_whole_service_months','All duties complete'],['accepted_zones','Zones',v=>fmt(q(v),2)],['outside_completed_jobs','Outside done'],['outside_required_jobs','Outside due'],['staff_paid_cents','Staff USD',cash],['overtime_paid_cents','Overtime USD',cash],['all_payer_resource_and_transaction_cash_cents','Resource/transaction USD',cash]])}<p>${esc(s.data.comparison_boundary)}</p></details>`+
 `<details id="staffed-renewals-ledger"><summary>Inspect crew minutes, notices, awards and all-payer cash</summary><pre>${esc(JSON.stringify({workforce:w,renewals:r.competition,ownership:r.renewing_entry,source_sha256:r.source_sha256},null,2))}</pre></details>`+
 `<p><button id="export-staffed-renewals">Export complete crew case</button> <label>Reload crew case<input id="import-staffed-renewals" type="file" accept="application/json,.json"></label></p><p class="small">Case ${esc(r.case_hash.slice(0,14))}. <a href="/research/shared_workforce.md#paid-crews-and-actual-customer-awards-edition-041" target="_blank">Decision findings ↗</a> · <a href="/model/ENTRY_TRANSITIONS.md" target="_blank">Methods ↗</a></p></section>`;
}
function buildStaffedRenewalsEvents(){
 const s=staffedRenewalsState,visible=()=>['customer','commercial'].includes(activeView);
 const fail=message=>{s.error=message+' Display and export retain the last applied case.';if($('staffed-renewals-state'))setText('staffed-renewals-state',s.error);};
 const calculate=async(body,selection,id)=>{
  if($('staffed-renewals-state'))setText('staffed-renewals-state','Recomputing paid crew, retained work and actual awards…');
  try{const response=await fetch('/api/staffed-renewals',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(body)}),data=await response.json();if(id!==s.requestId)return;if(!response.ok)throw Error(data.error||'Crew calculation failed');s.current=data.result;s.inputs=body.inputs||{};s.selection=selection;s.imported=selection==='imported';s.error=body.saved_case&&body.saved_case.case_hash!==data.result.case_hash?'Recomputed from complete inputs; saved hash differs.':'';if(visible())render();}catch(e){if(id===s.requestId)fail(e.message);}
 };
 document.addEventListener('click',e=>{
  if(e.target.id==='export-staffed-renewals'&&s.current)download('staffed-renewals-'+s.current.case_hash.slice(0,10)+'.json',JSON.stringify(s.current,null,2),'application/json');
  if(e.target.id!=='apply-staffed-renewals')return;const id=++s.requestId;
  try{const x=structuredClone(s.inputs);x.entry=x.entry||{};x.crews=x.crews||{};x.crews.incumbent=x.crews.incumbent||{};
   for(const f of document.querySelectorAll('#staffed-renewals [data-sr-key]')){const raw=f.value.trim(),key=f.dataset.srKey;let value;
    if(f.dataset.srMoney==='true'){if(!/^\d+(\.\d{1,2})?$/.test(raw))throw Error('Use nonnegative USD with at most two decimals.');const parts=raw.split('.');value=Number(parts[0])*100+Number((parts[1]||'').padEnd(2,'0'));}else value=Number(raw);
    if(raw===''||!Number.isSafeInteger(value)||value<0)throw Error('Exact nonnegative money and whole minutes are required.');
    if(key==='target_cash_cents')x.entry[key]=value;else x.crews.incumbent[key]=value;
   }calculate({inputs:x},'custom',id);
  }catch(e){fail(e.message);}
 });
 document.addEventListener('change',async e=>{
  if(e.target.id==='staffed-renewals-case'&&s.data&&Object.hasOwn(s.data.case_inputs,e.target.value)){const id=++s.requestId;await calculate({inputs:s.data.case_inputs[e.target.value]},e.target.value,id);}
  if(e.target.id==='import-staffed-renewals'){const id=++s.requestId;try{const f=e.target.files[0];if(!f)return;if(f.size>8000000)throw Error('Crew cases are limited to 8 MB.');const saved=JSON.parse(await f.text());if(id===s.requestId)await calculate({saved_case:saved},'imported',id);}catch(e){if(id===s.requestId)fail('Import error: '+e.message);}}
 });
 document.addEventListener('input',e=>{if(e.target.dataset.srKey){++s.requestId;if($('staffed-renewals-state'))setText('staffed-renewals-state','Edits are pending. Apply to recompute; export retains the displayed case.');}});
}
