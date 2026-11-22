'use strict';
// Node 18+ executable; no dependencies; every comparison exact integer.
const result = (function exactOfferSuite(){
let assertions=0, grids=0;
const assert=(x,m)=>{if(!x) throw Error(m);assertions++};
const payoff=(mask,a,b,capacity=1)=>mask===0?0:mask===1?a:mask===2?b:capacity===2?a+b:Math.max(a,b);
for(let a=1;a<=12;a++)for(let b=1;b<=12;b++)for(let ca=0;ca<=10;ca++)for(let cb=0;cb<=10;cb++)for(let j=Math.max(0,ca+cb-10);j<=Math.min(ca,cb);j++){
let p=[10-ca-cb+j,ca-j,cb-j,j], direct=p.reduce((s,w,i)=>s+w*payoff(i,a,b),0), formula=a*ca+b*cb-Math.min(a,b)*j;
assert(p.every(x=>x>=0)&&p.reduce((s,x)=>s+x,0)===10,"probability");
assert(direct===formula,"single-slot identity");
let double=p.reduce((s,w,i)=>s+w*payoff(i,a,b,2),0);
assert(double===a*ca+b*cb,"two slot");
grids++;
}
const v=k=>({P:300-10*k,D:260-8*k,E:240});
const worlds={separated:{P:v(0).P,D:v(10).D,E:v(0).E},coincident:{P:v(10).P,D:v(0).D,E:v(0).E}};
assert(worlds.separated.P>worlds.separated.D&&worlds.separated.P>worlds.separated.E,"separated P optimal");
assert(worlds.coincident.D>worlds.coincident.P&&worlds.coincident.D>worlds.coincident.E,"coincident D optimal");
assert(v(6).P===v(6).E,"P E tie");
for(let k=0;k<=10;k++){assert(v(k).P===300-10*k,"P grid");assert(v(k).D===260-8*k,"D grid");assert(v(k).E===240,"E grid");}
const logsWorlds={withoutHiddenB:{P:20,D:8},withHiddenB:{P:20,D:40}};
assert(logsWorlds.withoutHiddenB.P>logsWorlds.withoutHiddenB.D,"served only world0");
assert(logsWorlds.withHiddenB.D>logsWorlds.withHiddenB.P,"served only world1");
return {units:"normalized values; all headline contributions in /400 units",grid_cases:grids,assertions,worlds,full_joint_half_marginal_series:{k_0:v(0),k_6:v(6),k_10:v(10)},unseen_original_offer_example:logsWorlds,limitations:"Exact finite arithmetic. No field data, legal approval, causal identification or empirical calibration."};
})();
console.log(JSON.stringify(result, null, 2));
