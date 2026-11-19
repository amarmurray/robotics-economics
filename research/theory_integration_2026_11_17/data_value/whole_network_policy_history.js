const result=(function diagnostic(){
"use strict";
let assertions=0;
function ok(x,m){assertions++;if(!x)throw Error(m);}
const policies=["R","A","X","G","E"], cost={R:0,A:1,X:3,G:1,E:2};
function network(i,k){
 if(!Number.isInteger(i)||i<0||i>=8||!policies.includes(k))throw Error("invalid type/policy");
 const qb=(i>>2)&1, db=(i>>1)&1, lb=i&1;
 const q0=(k==="X"&&(i===1||i===3))?1:qb;
 const d1= ((k==="X"||k==="G")&&i===5)||(k==="E"&&i===2)?1:db;
 const q1=((k==="X"||k==="G")&&i===6)?1:lb;
 const operator=(k==="A"||k==="E")?1:q0; // A's safe nonactuating first-risk report preserves recovery on a predicted failure
 const y0=q0, y1=d1*q1*operator;
 return {i,k,q0,d1,q1,operator,y0,y1,originalOrders:1+d1,accepted:y0+y1,gross:5*y0+9*y1,net:5*y0+9*y1-cost[k],cost:cost[k]};
}
function combo(n,k){
 const out=[]; function rec(start,a){if(a.length===k){out.push(a.slice());return;}for(let j=start;j<=n-(k-a.length);j++){a.push(j);rec(j+1,a);a.pop();}}
 rec(0,[]);return out;
}
function reduced(a,b){function gcd(x,y){while(y){let t=x%y;x=y;y=t}return x;}let g=gcd(Math.abs(a),Math.abs(b));return {numerator:a/g,denominator:b/g};}
const rows=Array.from({length:8},(_,i)=>Object.fromEntries(policies.map(k=>[k,network(i,k)])));
const total=Object.fromEntries(policies.map(k=>[k,rows.reduce((s,r)=>s+r[k].net,0)]));
const gross=Object.fromEntries(policies.map(k=>[k,rows.reduce((s,r)=>s+r[k].gross,0)]));
const count=Object.fromEntries(policies.map(k=>[k,rows.reduce((s,r)=>s+r[k].accepted,0)]));
ok(gross.X===66&&gross.G===47,"gross accounting");
ok(total.X===42&&total.G===39&&total.R===29,"network totals");
ok(gross.G*count.X>gross.X*count.G,"selected-only mean reverses net whole-network ranking");
ok(total.X>total.G,"whole-network policy ranking");
for(const r of rows)for(const k of policies){
 const z=r[k]; ok(z.y1<=z.d1&&z.y1<=z.q1&&z.y1<=z.operator,"accepted complete service feasibility");
 ok(z.net===z.gross-z.cost,"cost counted once");
}
const assignments=combo(8,4);ok(assignments.length===70,"balanced assignments");
let sumD=0,sumD2=0,minD=Infinity,maxD=-Infinity;const D=total.X-total.G;
for(const a of assignments){
 const x=new Set(a),sx=a.reduce((s,i)=>s+rows[i].X.net,0);
 const sg=rows.reduce((s,r,i)=>s+(!x.has(i)?r.G.net:0),0);
 const d=sx-sg,dev=2*d-D; // estimator=d/4, finite-pop contrast=D/8
 sumD+=d;sumD2+=dev*dev;minD=Math.min(minD,d);maxD=Math.max(maxD,d);
}
ok(8*sumD===4*assignments.length*D,"design unbiased: all 70 assignments");
function sqDev(k){return rows.reduce((s,r)=>s+(8*r[k].net-total[k])**2,0);}
const diff=rows.map(r=>r.X.net-r.G.net),sqd=diff.reduce((s,v)=>s+(8*v-D)**2,0);
const neymanNumerator=2*(sqDev("X")+sqDev("G"))-sqd;
ok(512*7*sumD2===64*assignments.length*neymanNumerator,"exact Neyman variance identity");
ok(neymanNumerator>=0&&sqd>=0,"nonnegative variance");
const supported=rows.slice(0,6).reduce((s,r)=>s+r.X.net-r.G.net,0);
const lower=supported-2*16,upper=supported+2*12;
ok(lower<=D&&D<=upper,"partial eligible-unmeasured support bounds");
for(let i=0;i<8;i++){
 const r=rows[i];ok(r.X.net>=-3&&r.X.net<=11&&r.G.net>=-1&&r.G.net<=13,"policy earnings envelope");
}
return {
 schema:"full-history approved whole-network synthetic policy contrasts v1",
 construction:"Eight fixed prepolicy network types; two dates; first failure occupies operator recovery unless safe report A or extra safe capacity E; source X and grounding G can change qualification and future original demand. No field measurements.",
 costs:cost,
 per_network:rows.map(r=>({i:r.R.i,R:r.R.net,A:r.A.net,X:r.X.net,G:r.G.net,E:r.E.net,X_original_orders:r.X.originalOrders,G_original_orders:r.G.originalOrders,X_accepted:r.X.accepted,G_accepted:r.G.accepted})),
 totals:total,means_over_8:Object.fromEntries(policies.map(k=>[k,reduced(total[k],8)])),
 accepted_service_selected_means:{X:reduced(gross.X,count.X),G:reduced(gross.G,count.G),counts:count},
 X_minus_G_true:reduced(D,8),
 complete_randomization:{units:8,assigned_X:4,assigned_G:4,assignments:assignments.length,mean_estimate:reduced(sumD,assignments.length*4),min_estimate:reduced(minD,4),max_estimate:reduced(maxD,4),exact_variance:reduced(sumD2,64*assignments.length),neyman_variance:reduced(neymanNumerator,512*7),unidentified_individual_effect_variance:reduced(sqd,64*7)},
 partially_supported:{supported_networks:6,missing_networks:2,supported_sum_difference:supported,net_bounds_X:[-3,11],net_bounds_G:[-1,13],contrast_lower:reduced(lower,8),contrast_upper:reduced(upper,8),sharp_only_under:"unrestricted joint response types with independent per-policy payout envelopes for unsupported but approved networks"},
 assertions,limitations:"Counterfactual reference table synthetic; randomization is enumerated, not conducted. No actual network isolation, physical approval, robot production, sector calibration, cost evidence or external replication."
};
} )()
if(typeof process!=="undefined"&&process.stdout)process.stdout.write(JSON.stringify(result,null,2)+"\n");
