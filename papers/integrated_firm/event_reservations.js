'use strict';
// Extend accepted suffix institution. All new decisions remain inside the funded four-block economy.
function build(source){
 function p(a,b){if(!source.includes(a))throw Error('wrapper mismatch '+a);source=source.replace(a,b)}
 p('function makeSuffix(rule,enabled=true){','function makeSuffix(rule,enabled=true,alwaysOpen=true){');
 p('return recipe(a.modes[0],a.modes[1],a.use,g).cost;','return a.reservation??recipe(a.modes[0],a.modes[1],a.use,g).cost;');
 p('if(!enabled||n<=1||!bit.some(Boolean))return zero;','if(!enabled||n<=1||!aa[0].reopen||(!alwaysOpen&&!bit.some(Boolean)))return zero;');
 p('r.cost!==old[i]','(!a.independent&&r.cost>old[i])');
 p('mixed=false,scaleFactor=125}={})','mixed=false,scaleFactor=125,alwaysOpen=true,independent=false,audit=true}={})');
 p('const suffix=makeSuffix(rule,enabled),stats=suffix.stats;','if(independent&&(!alwaysOpen||!enabled))throw Error("independent reservation requires always-open institution");const suffix=makeSuffix(rule,enabled,alwaysOpen),stats=suffix.stats;');
 p('if(!enabled||a.shifts<=1||(!releaseBit(a)&&!releaseBit(b)))return [0,0];','if(!enabled||a.shifts<=1||!a.reopen||(!alwaysOpen&&!releaseBit(a)&&!releaseBit(b)))return [0,0];');
 // Add reservation choice before any menu reduction. Cash and resources remain dated.
 const from='let a={q,shifts:shifts(h),modes:[pr,d1,d2],use,copies,hh,cc,cost,r,b,keep,ng};';
 const to='const reopen=h>1&&shifts(h)>1,unit=2*human+compute+g;for(const reservation of INDEPENDENT&&reopen?RESERVES(s,r):[unit]){let reserveExtra=(shifts(h)-1)*(reservation-unit),gross=cost+reserveExtra;if(gross>B)continue;let a={q,shifts:shifts(h),modes:[pr,d1,d2],use,copies,hh,cc,cost:gross,r,b,keep,ng,reopen,reservation,reserveExtra,...(INDEPENDENT&&reopen?{independent:true}:{})};';
 p(" const adjMemo=new Map();", " const adjMemo=new Map();\n patch("+JSON.stringify(from)+","+JSON.stringify(to)+");\n patch('if(!out.has(key)||out.get(key).cost>cost)out.set(key,a);','if(!out.has(key)||out.get(key).cost>gross)out.set(key,a); }');\n patch('if(cost!==a.cost||hh!==a.hh','cost+=a.reserveExtra??0;if(cost!==a.cost||hh!==a.hh');");
 // Inject an audit of full continuation values for same-cost probability changes.
 const anchor='  let e=null,n=0;for(let i=0;i<aa.length;i++)';
 const injection='  if(h===2)AUDIT(s,z,ga.all,gb.all,value,scale);\\n';
 p(" const run=new Function('SIG','EXPECT','ADJUST','POP','CS','CONT',", " if(audit)patch("+JSON.stringify(anchor)+","+JSON.stringify(injection.replace("\\n","\n")+anchor)+");\n const checks={comparisons:0,gain:0,tie:0,loss:0,min:null,max:null,witness:null};\n function auditValues(s,z,aa,bb,value,scale){for(let i=0;i<2;i++){const own=i?bb:aa,other=i?aa:bb,groups=new Map();for(const x of own){if(!releaseBit(x.a))continue;const a=x.a,k=JSON.stringify({...a,r:a.r.map((v,j)=>j===4?0:v)});if(!groups.has(k))groups.set(k,[]);groups.get(k).push(x)}for(const ls of groups.values()){ls.sort((x,y)=>x.a.r[4]-y.a.r[4]);for(let j=1;j<ls.length;j++){const lo=ls[j-1],hi=ls[j];if(lo.a.r[4]===hi.a.r[4])continue;for(const b of other){const x=i?value(b,lo)[1]:value(lo,b)[0],y=i?value(b,hi)[1]:value(hi,b)[0],v=(y-x)/scale;checks.comparisons++;checks[v>0?'gain':v<0?'loss':'tie']++;if(checks.min===null||v<checks.min){checks.min=v;checks.witness={firm:i,s,z,low:lo.a,high:hi.a,rival:b.a,lowValue:x/scale,highValue:y/scale}}if(checks.max===null||v>checks.max)checks.max=v;}}}}}\n const reserveCache=new Map();\n function reserves(s,r){const bit=['train','contract'].includes(r[0])?1<<r[5]:0,key=[s[0],s[1],s[4],s[8],bit].join();if(reserveCache.has(key))return reserveCache.get(key);const v=new Set([s[8]]);for(const m of [s[4],s[4]|bit]){const x=s.slice();x[4]=m;const best=new Map();for(const a of legalRecipes(x,12,true))if(!best.has(a.q)||best.get(a.q)>a.cost)best.set(a.q,a.cost);for(const c of best.values())v.add(c)}const ans=[...v].sort((a,b)=>a-b);reserveCache.set(key,ans);return ans}\n const run=new Function('INDEPENDENT','RESERVES','AUDIT','SIG','EXPECT','ADJUST','POP','CS','CONT',");
 p("')(signature,expected,suffix.adjust,pop,cs,contested);","')(independent,reserves,auditValues,signature,expected,suffix.adjust,pop,cs,contested);");
 p('return {spec:{S,concurrent,cap,rule,enabled,mixed,scaleFactor},stats,result,','return {spec:{S,concurrent,cap,rule,enabled,mixed,scaleFactor,alwaysOpen,independent,audit},stats,checks,result,');
 return new Function(source+';return {study,suffixStage,legalRecipes,recipe,revenue,reservationWitness,gateWitness};')();
}
if(typeof module!=='undefined')module.exports={build};


function verifyMechanisms(source){
 const {suffixStage,legalRecipes,recipe,revenue}=new Function(source+';return {suffixStage,legalRecipes,recipe,revenue};')();
 const menu=(s,B)=>{const c=Array(4).fill(null);for(const a of legalRecipes(s,B,true))if(c[a.q]===null||c[a.q]>a.cost)c[a.q]=a.cost;return c};
 let reserveChecks=0,types=0,removed=0;
 for(let k=0;k<4;k++)for(let m=0;m<4;m++)for(let g=0;g<2;g++)for(const bit of [0,1,2]){
  if(bit&m)continue;
  const s=[+(!!(k&1)),+(!!(k&2)),0,0,m,0,10000,3,g],z=s.slice();z[4]|=bit;
  const thresholds=[...new Set([g,...menu(s,12),...menu(z,12)].filter(v=>v!==null))].sort((a,b)=>a-b);
  types++;
  for(let B=g;B<=12;B++){
   const b=Math.max(...thresholds.filter(t=>t<=B));
   for(const x of [s,z]){if(JSON.stringify(menu(x,B))!==JSON.stringify(menu(x,b)))throw Error('reservation quotient');reserveChecks++}
   if(B!==b)removed++;
  }
 }
 // Full continuation witness: firm 1 qualifies digital at equal cost.
 const s=[1,0,0,0,0,0,728,0,0],z=[1,0,0,0,1,1,728,0,0],zz=z.slice();zz[4]|=2;
 const a=recipe(1,0,0,0),b=recipe(0,1,0,0),n=5,N=5,setup=102;
 const u0=suffixStage(s,z,6,4,1),u1=suffixStage(s,zz,6,4,1),t0=suffixStage(s,z,12,12,1),t1=suffixStage(s,zz,12,12,1);
 const first=revenue(b.q,a.q)-b.cost-setup,salvage=1;
 const W0=first+(n-1)*u0.v[1]+N*t0.v[1]+salvage,W1=first+(n-1)*u1.v[1]+N*t1.v[1]+salvage;
 const best=(x,B,q)=>Math.max(...legalRecipes(x,B,true).map(r=>revenue(r.q,q)-r.cost));
 const fixed0=first+(n-1)*best(z,4,u0.a.q)+N*best(z,12,t0.a.q)+salvage;
 const fixed1=first+(n-1)*best(zz,4,u0.a.q)+N*best(zz,12,t0.a.q)+salvage;
 if(W0!==45||W1!==42||fixed0!==45||fixed1!==50)throw Error('full conditional witness');
 const value=p=>((1-p)*W0+p*W1);
 // Match both-open reservations, same first physical quantity and same research.
 const y=[1,0,0,0,1,0,10000,2,1],idle=[0,0,0,0,0,0,10000,0,0],yy=y.slice();yy[4]|=2;
 const low=recipe(2,0,1,1),high=recipe(2,0,0,1);
 const comps=[[low,5],[high,8],[low,8]].map(([r,B])=>{
  if(r.h+1>3||r.c+2>5)throw Error('first shift');
  const f=suffixStage(y,idle,B,0,1),p=suffixStage(yy,idle,B,0,1);
  const gross=r.cost+4+(n-1)*B;
  const fNet=n*0+revenue(r.q,0)-r.cost-4+(n-1)*f.v[0];
  const pNet=revenue(r.q,0)-r.cost-4+(n-1)*p.v[0];
  return {first:r,reservation:B,gross,fail:f.v[0],success:p.v[0],expected:(fNet+pNet)/2}
 });
 if(JSON.stringify(comps.map(x=>x.expected))!=='[51,66,69]')throw Error('independent reserve witness');
 return {reserveChecks,types,removed,fullWitness:{s,z,first,suffix:[u0,u1],terminal:[t0,t1],conditional:[W0,W1],fixed:[fixed0,fixed1],lowValue:value(.5),highValue:value(.75),difference:value(.75)-value(.5),fixedDifference:.25*(fixed1-fixed0)},reservationWitness:comps}
}


if(typeof module!=='undefined'){
 module.exports={build,verifyMechanisms};
 if(require.main===module){
  const fs=require('fs'),path=require('path'),crypto=require('crypto');
  const e=JSON.parse(fs.readFileSync(path.join(__dirname,'event_reservations_results.json'),'utf8'));
  const names=['service_window.js','staggered_window.js','concurrent_window.js','mixed_continuation.js','event_suffix.js'];
  const src=names.map(n=>{const b=fs.readFileSync(path.join(__dirname,n));if(crypto.createHash('sha256').update(b).digest('hex')!==e.source_sha256[n])throw Error('source bytes mismatch '+n);return b.toString('utf8')});
  const suffix=src.pop(),a=build(suffix);
  const chosen=process.argv[2]===undefined?e.runs:e.runs.filter((r,i)=>i===Number(process.argv[2]));
  if(!chosen.length)throw Error('unknown run index');
  for(const r of chosen)if(JSON.stringify(a.study(src,r.spec))!==JSON.stringify(r))throw Error('run replay mismatch '+JSON.stringify(r.spec));
  if(JSON.stringify(verifyMechanisms(suffix))!==JSON.stringify(e.mechanisms))throw Error('mechanism replay mismatch');
  console.log('verified '+chosen.length+' complete games and reservation/continuation witnesses');
 }
}
