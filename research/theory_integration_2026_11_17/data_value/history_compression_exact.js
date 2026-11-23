'use strict';
// Finite, synthetic normalized qualified-production decision. Node 22, stdlib only.
const assert = require('node:assert/strict');
const ACTIONS = ['retain','arm','mobile','kit'];
const states = [
  {id:'field', records:['field'], probability:1/4},
  {id:'recovery', records:['recovery'], probability:1/4},
  {id:'field-field', records:['field','field'], probability:1/4},
  {id:'field-recovery', records:['field','recovery'], probability:1/4}
];
function net(h, a) {
  // All actions use at most one final service/validation slot and one buyer budget;
  // old retained recipe is always feasible. All values include action costs.
  const f=h.records.includes('field'), r=h.records.includes('recovery');
  if(a==='retain') return 2;
  if(a==='arm') return f ? 3 : 0;
  if(a==='mobile') return r ? 3 : 0;
  if(a==='kit') return f && r ? 7 : -1; // gross 8, validation costs 1
  throw Error('unknown action');
}
function signature(h) {return Number(h.records.includes('field'))+':'+Number(h.records.includes('recovery'));}
function count(h){return String(h.records.length);}
function full(h){return h.id;}
function constant(){return 'all';}
function classify(key){
  const groups=new Map();
  for(const h of states){const label=key(h);if(!groups.has(label)) groups.set(label,[]);groups.get(label).push(h);}
  const cells=[];
  for(const [label,hs] of groups){
    const mass=hs.reduce((s,h)=>s+h.probability,0);
    const actionValues=Object.fromEntries(ACTIONS.map(a=>[a,hs.reduce((s,h)=>s+h.probability*net(h,a),0)/mass]));
    const maxValue=Math.max(...Object.values(actionValues));
    const best=ACTIONS.filter(a=>actionValues[a]===maxValue);
    const intersection=ACTIONS.filter(a=>hs.every(h=>net(h,a)===Math.max(...ACTIONS.map(x=>net(h,x)))));
    cells.push({label,ids:hs.map(h=>h.id),mass,actionValues,best,commonArgmax:intersection,contribution:mass*maxValue});
  }
  return {value:cells.reduce((s,g)=>s+g.contribution,0),cells};
}
// All set partitions of n histories using canonical restricted-growth codes.
function* partitions(n, idx=1, codes=[0],max=0){
  if(idx===n){yield [...codes];return;}
  for(let i=0;i<=max+1;i++)yield* partitions(n,idx+1,[...codes,i],Math.max(max,i));
}
const outcome={full:classify(full),count:classify(count),signature:classify(signature),constant:classify(constant), alternatives:{E:3,P:2.75,R:2}};
let checks=0;
function check(condition,label){assert.ok(condition,label);checks++;}
check(outcome.full.value===4,'full optimized');
check(outcome.count.value===2.5,'count aggregate');
check(outcome.signature.value===4,'provenance+joint signature');
check(outcome.constant.value===2.25,'all pooled');
check(outcome.full.value>outcome.alternatives.E,'G beats E when provenance retained');
check(outcome.count.value<outcome.alternatives.E,'E beats G when only counts retained');
check(outcome.signature.value-outcome.count.value===1.5,'priced timely provenance report');
for(const h of states){check(net(h,'retain')===2,'old option feasible');check(h.probability===1/4,'uniform states');}
for(const codes of partitions(4)){
  const c=classify(h=>String(codes[states.indexOf(h)]));
  const loss=outcome.full.value-c.value;
  const commonAll=c.cells.every(g=>g.commonArgmax.length>0);
  check(loss>=0,'free information monotonic');
  check((loss===0)===commonAll,'finite-menu zero-loss iff each fiber has common maximizing action');
  // For this fully settled finite economy, the gap equals the conditional Jensen gap.
  const fullValueByCell=c.cells.reduce((s,g)=>s+g.mass*states.filter(h=>g.ids.includes(h.id))
    .reduce((ss,h)=>ss+h.probability/g.mass*Math.max(...ACTIONS.map(a=>net(h,a))),0),0);
  check(fullValueByCell-c.value===loss,'conditional max Jensen identity');
}
check([...partitions(4)].length===15,'Bell(4) complete partitions');
// Nonanticipative t3 signal illustrates that compression can change acquisition itself.
const exante=[
 {name:'A-needs-field',prob:1/2,S:5,M:0},
 {name:'C-needs-recovery',prob:1/2,S:1,M:6}
];
const fullAcquisition=exante.reduce((s,h)=>s+h.prob*Math.max(h.S,h.M),0);
const noSignalAcquisition=Math.max(...['S','M'].map(a=>exante.reduce((s,h)=>s+h.prob*h[a],0)));
check(fullAcquisition===5.5,'adaptive original-service/acquisition policy');
check(noSignalAcquisition===3,'compressed nonanticipative acquisition policy');
check(5.5>4.2 && 3<4.2,'ranking reversal against independently staffed embodiment');
console.log(JSON.stringify({schema:'roboecon.history-compression.v1',as_of:'2026-11-23',assumptions:'synthetic normalized, timely lawful provenance, one buyer budget and one validation/service slot; no field calibration', terminal:outcome,partitionChecks:15,preaction:{withSignal:fullAcquisition,withoutSignal:noSignalAcquisition,E:4.2},checks},null,2));
