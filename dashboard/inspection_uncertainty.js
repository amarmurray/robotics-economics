'use strict';
const labels={staffing:'Paid field staffing',field_duty:'Mandatory physical duty',fixed_fit:'Fixed-sensor qualification',mobile_fit:'Mobile-sensor result',review_capacity:'Review person-minutes',deadline_minute:'Service deadline (minutes)'};
const choices={committed:'Paid commitment retained',per_visit:'Visit payment is avoidable',false:'No separate physical duty',true:'Physical duty remains',complete:'Complete qualified coverage',one_unqualified:'One measurement unqualified',one_quality_failure:'One failed quality review',late_capture:'Capture after review cutoff'};
const $=id=>document.getElementById(id);
const money=n=>n===null?'Not admissible':new Intl.NumberFormat('en-US',{style:'currency',currency:'USD',maximumFractionDigits:2}).format(n/100);
const describe=(k,v)=>choices[String(v)]||String(v);
let data;
function branch(objective,known){
 const keys=Object.keys(known),d=data.decisions[objective];
 if(!keys.length)return {...d.before_evidence,state_count:data.state_count};
 const p=d.evidence_partitions.find(x=>x.revealed_axes.length===keys.length&&keys.every(k=>x.revealed_axes.includes(k)));
 return p.branches.find(b=>keys.every(k=>b.observed[k]===known[k]));
}
function render(){
 const known={};Object.keys(labels).forEach(k=>{const v=$(k).value;if(v!=='')known[k]=JSON.parse(v);});
 const b=branch($('objective').value,known);
 $('result').innerHTML=`<span class="badge">${b.state_count} compatible synthetic possibilities</span><h2>Conditional minimax choice: ${b.minimax_policies.join(', ')}</h2><p>Worst remaining regret: <strong>${money(b.worst_regret_cents)}</strong>. This selects the feasible option with the smallest worst cash disadvantage within the displayed assumptions.</p><div class="scroll"><table><thead><tr><th>Policy</th><th>Service/funding failures in compatible states</th><th>Worst cash regret</th></tr></thead><tbody>${Object.entries(b.policies).map(([p,v])=>`<tr><td>${p}</td><td>${v.infeasible_state_count}</td><td>${money(v.worst_regret_cents)}</td></tr>`).join('')}</tbody></table></div>`;
 const rows=data.states.filter(s=>Object.keys(known).every(k=>s.state[k]===known[k]));
 $('state-table').innerHTML='<table><thead><tr><th>State / assumptions</th><th>Policy</th><th>Complete windows</th><th>Paid crew</th><th>Customer cash</th><th>Consolidated cash</th><th>Extra net cost allowed vs human: customer / consolidated</th></tr></thead><tbody>'+rows.map(s=>Object.entries(s.policies).map(([p,v])=>{const l=s.residual_cost_limits.find(x=>x.baseline==='human'&&x.alternative===p);return `<tr><td>${s.state_id}<br><span class="small">${Object.keys(labels).map(k=>describe(k,s.state[k])).join(' · ')}</span></td><td>${p}</td><td>${v.summary.complete_service_windows}/4${v.feasible?'':' · inadmissible'}</td><td>${money(v.summary.paid_field_crew_cents)}</td><td>${money(v.cash.customer_outlay_cents)}</td><td>${money(v.cash.consolidated_resource_cash_cents)}</td><td>${l?money(l.customer_incremental_net_residual_allowance_cents)+' / '+money(l.consolidated_incremental_net_residual_allowance_cents):'Comparator'}</td></tr>`;}).join('')).join('')+'</tbody></table>';
}
async function start(){
 const response=await fetch('/model/results/inspection_uncertainty.json');if(!response.ok)throw Error('Artifact HTTP '+response.status);
 data=await response.json();if(data.schema_version!=='inspection-uncertainty/1.0')throw Error('Unsupported artifact');
 for(const [k,title]of Object.entries(labels)){
  const label=document.createElement('label');label.textContent=title;const select=document.createElement('select');select.id=k;
  select.add(new Option('Unresolved', ''));data.inputs.axes[k].forEach(v=>select.add(new Option(describe(k,v),JSON.stringify(v))));
  select.addEventListener('change',render);label.append(select);$('controls').append(label);
 }
 const packets=[[],['field_duty','fixed_fit','review_capacity'],['field_duty','fixed_fit','mobile_fit','review_capacity'],['staffing','field_duty','fixed_fit','mobile_fit','review_capacity']];
 $('sequence').innerHTML=packets.map(keys=>{const vals=Object.values(data.decisions).map(d=>keys.length?d.evidence_partitions.find(p=>p.revealed_axes.length===keys.length&&keys.every(k=>p.revealed_axes.includes(k))).worst_remaining_regret_cents:d.before_evidence.worst_regret_cents);return `<tr><td>${keys.length?keys.map(k=>labels[k]).join(' + '):'None (any single field or pair leaves the same worst regret)'}</td><td>${money(vals[0])}</td><td>${money(vals[1])}</td></tr>`;}).join('');
 $('objective').addEventListener('change',render);$('reset').addEventListener('click',()=>{Object.keys(labels).forEach(k=>$(k).value='');render();});render();
}
start().catch(e=>{$('error').textContent=e.message;$('result').textContent='Unable to load the verified simulation. No decision displayed.';});
