'use strict';
function witness(source){
 const {suffixStage,legalRecipes,revenue}=new Function(source+";return {suffixStage,legalRecipes,revenue};")();
 const results=[];
 for(const rule of [1,-1]){
 const s=[1,0,0,0,rule===1?0:2,0,728,0,0],z=[1,0,0,0,1,1,728,0,0],zz=z.slice();zz[4]|=2;
 const u0=suffixStage(s,z,6,4,rule),u1=suffixStage(s,zz,6,4,rule),t0=suffixStage(s,z,12,12,rule),t1=suffixStage(s,zz,12,12,rule);
 const fixed=(x,B,q)=>Math.max(...legalRecipes(x,B).map(r=>revenue(r.q,q)-r.cost));
 const d=[u1.v[1]-u0.v[1],t1.v[1]-t0.v[1],fixed(zz,4,u0.a.q)-fixed(z,4,u0.a.q),fixed(zz,12,t0.a.q)-fixed(z,12,t0.a.q)];
 if(JSON.stringify(d)!=="[-2,1,0,1]")throw Error("calendar witness");
 const calendars=[];for(let n=2;n<=8;n++)for(let N=1;N<=16;N++)calendars.push({n,N,conditionalDifference:(n-1)*d[0]+N*d[1],probabilityQuarterDifference:((n-1)*d[0]+N*d[1])/4,fixedRivalDifference:((n-1)*d[2]+N*d[3])/4});
 results.push({rule,s,z,suffix:[u0,u1],terminal:[t0,t1],d,calendars});
 }return results
}
const fs=require('fs'),path=require('path'),crypto=require('crypto');
const e=require('./event_probability_audit_results.json');
const names=['service_window.js','staggered_window.js','concurrent_window.js','mixed_continuation.js','event_suffix.js','event_reservations.js','event_reserve_factor.js'];
const src=names.map(n=>{const b=fs.readFileSync(path.join(__dirname,n));const id=crypto.createHash('sha1').update('blob '+b.length+'\0').update(b).digest('hex');if(id!==e.source_blobs[n])throw Error('source Git blob mismatch '+n);return b.toString('utf8')});
const {factorBuild,compact}=new Function(src[6]+';return {factorBuild,compact};')();
const a=factorBuild(src[5],src[4]);
const chosen=process.argv[2]===undefined?e.runs:e.runs.filter((_,i)=>i===Number(process.argv[2]));
if(!chosen.length)throw Error('unknown run');
for(const r of chosen)if(JSON.stringify(compact(a.study(src.slice(0,4),r.spec)))!==JSON.stringify(r))throw Error('audit replay mismatch '+JSON.stringify(r.spec));
if(JSON.stringify(witness(src[4]))!==JSON.stringify(e.witnesses))throw Error('calendar witness replay mismatch');
console.log('verified '+chosen.length+' audits and both conditional calendar witnesses');
