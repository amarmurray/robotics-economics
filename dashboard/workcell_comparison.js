'use strict';
let workcellComparisonState={data:null,loading:false,current:null,selection:'fixed_vs_human',reference:'human_direct',sourceHash:null,error:'',requestId:0};
function workcellComparisonPanel(applied){
 const s=workcellComparisonState;
 if(!s.data&&!s.loading&&!s.error){s.loading=true;fetch('/api/workcell-comparison').then(async response=>{const d=await response.json();if(!response.ok)throw Error(d.error||'Comparison unavailable');s.data=d;}).catch(e=>s.error=e.message).finally(()=>{s.loading=false;if(activeView==='embodiment')render();});}
 const opening='<section id="workcell-comparison"><h3>Matched workcell labor and cash bounds</h3>';
 if(!s.data)return opening+empty(s.error||'Replaying matched workcell comparisons…')+'</section>';
 const r=s.current||s.data.comparisons[s.selection],v=r.bounds,money=n=>'$'+fmt(n/100,2);
 const refs=[...new Set(Object.values(s.data.pairs).map(p=>p.baseline))];
 const stale=s.sourceHash&&s.sourceHash!==applied.case_hash;
 return opening+notice('Synthetic, complete-service window comparison. Station work plus separately executed preparation is counted. Paid staff, supplier receipts and actual supplier resource costs are different quantities. A staff-invoice ceiling does not establish a removable shift; opening/terminal assets and lifecycle costs remain incomplete.')+
 `<label>Saved matched comparison<select id="workcell-comparison-case">${Object.keys(s.data.comparisons).map(k=>`<option value="${k}" ${s.selection===k?'selected':''}>${esc(title(k))}</option>`).join('')}${['applied','imported'].includes(s.selection)?`<option selected value="${s.selection}">${esc(title(s.selection))} complete pair</option>`:''}</select></label><label>Reference for applied workcell<select id="workcell-comparison-reference">${refs.map(k=>`<option value="${k}" ${s.reference===k?'selected':''}>${esc(title(k))}</option>`).join('')}</select></label><p><button id="compare-applied-workcell">Compare last applied workcell with reference</button></p>`+
 `<p id="workcell-comparison-state" role="status">${esc(stale?'Applied workcell changed; this is the previous comparison. Recompare to update.':s.error||'Display/export retain the complete selected or last applied pair. Pending workcell edits are not applied.')}</p>`+
 (v?`<div class="grid">${metric('Customer cash change',money(v.operator_cash_change_cents),'Alternative minus baseline; not lifecycle ROI')}${metric('Modeled person-time change',v.modeled_person_seconds_change+' seconds','Station '+v.station_person_seconds_change+'; preparation '+v.preparation_person_seconds_change)}${metric('Conditional station-staff invoice ceiling',money(v.alternative_staff_bill_ceiling_cents),'Necessary arithmetic only; retained duties/capacity must still be funded')}</div>`:notice('No economic bound: '+r.comparison.reasons.join('; '),true))+
 table(Object.entries(r.accounts).map(([role,a])=>({role,...a})),[['role','Role',esc],['operator_cash_cents','Customer outlay',money],['paid_staff_cents','Station staff paid',money],['station_person_seconds','Station person-seconds'],['preparation_person_seconds','Preparation person-seconds'],['modeled_person_seconds','Total modeled person-seconds']])+
 `<p>Supplier resource costs and profit are unknown: external payee receipts do not establish either. Any incremental omitted net cost must fit within ${v?money(v.incremental_net_omitted_cost_allowance_cents):'an uncomputed allowance'} for parity; negative values require a cost reduction or additional proven net value.</p><details><summary>Equations, complete obligations, assets and funded executions</summary><pre>${esc(JSON.stringify(r,null,2))}</pre></details><p><button id="export-workcell-comparison">Export complete comparison</button> <label>Reload comparison<input id="import-workcell-comparison" type="file" accept="application/json,.json"></label></p><p class="small">Comparison ${esc(r.comparison_hash.slice(0,14))}. <a href="/model/WORKCELL_COMPARISON.md" target="_blank">Methods and payer boundary ↗</a> · <a href="/research/workcell_cash_decision.md" target="_blank">Decision findings ↗</a></p></section>`;
}
function buildWorkcellComparisonEvents(){
 const s=workcellComparisonState;
 const applied=()=>automotiveWorkcellState.current||automotiveWorkcellState.data?.cases[automotiveWorkcellState.selection];
 const fail=m=>{s.error=m+' Display/export retain the last valid pair.';if($('workcell-comparison-state'))setText('workcell-comparison-state',s.error);};
 const calculate=async(body,selection,sourceHash,id)=>{
  if($('workcell-comparison-state'))setText('workcell-comparison-state','Replaying full service, work and cash…');
  try{const response=await fetch('/api/workcell-comparison',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(body)}),data=await response.json();if(id!==s.requestId)return;if(!response.ok)throw Error(data.error||'Comparison failed');if(sourceHash&&applied()?.case_hash!==sourceHash){fail('Applied workcell changed during comparison; recompare.');return;}s.current=data.result;s.selection=selection;s.sourceHash=sourceHash;s.error=body.saved_pair&&body.saved_pair.comparison_hash!==data.result.comparison_hash?'Recomputed complete inputs; saved result/hash differed.':'';if(activeView==='embodiment')render();}catch(e){if(id===s.requestId)fail(e.message);}
 };
 document.addEventListener('click',e=>{
  if(e.target.id==='export-workcell-comparison'&&s.data){const r=s.current||s.data.comparisons[s.selection];download('workcell-comparison-'+r.comparison_hash.slice(0,10)+'.json',JSON.stringify(r,null,2),'application/json');}
  if(e.target.id==='compare-applied-workcell'&&s.data&&applied()){
   const id=++s.requestId,k=Object.keys(s.data.pairs).find(k=>s.data.pairs[k].baseline===s.reference),r=applied();
   calculate({inputs:{baseline:s.data.comparisons[k].inputs.baseline,alternative:r.inputs}},'applied',r.case_hash,id);
  }
 });
 document.addEventListener('change',async e=>{
  if(e.target.id==='workcell-comparison-case'&&s.data&&Object.hasOwn(s.data.comparisons,e.target.value)){++s.requestId;s.selection=e.target.value;s.current=null;s.sourceHash=null;s.error='';render();}
  if(e.target.id==='workcell-comparison-reference'){++s.requestId;s.reference=e.target.value;s.error='Reference changed. Compare to apply; the previous pair remains displayed.';if($('workcell-comparison-state'))setText('workcell-comparison-state',s.error);}
  if(e.target.id==='import-workcell-comparison'){const id=++s.requestId;try{const f=e.target.files[0];if(!f)return;const saved=JSON.parse(await f.text());if(id===s.requestId)await calculate({saved_pair:saved},'imported',null,id);}catch(e){if(id===s.requestId)fail('Import error: '+e.message);}}
 });
}
