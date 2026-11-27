'use strict';
// Reservation-constrained public suffix stage in the accepted four-block economy.
// All costs and service are integer ticks/jobs. No new evidence, training, assembly,
// scope or collection within the suffix. The event gate is an actual qualification.
const pins={"service_window.js":"004bb37abae4176ab49a144b40c82d95fa7a11d6","staggered_window.js":"dc0243b11599ef87e584824eebf7a66a91394007","concurrent_window.js":"8d7d8090bf90f160835b72793e108f5c1fad9216","mixed_continuation.js":"4c27fbb1b0a4b59a3fd6de51feaf0ff019df1b06"};
const A=[18,14],pop=m=>+(!!(m&1))+(!!(m&2));
function recipe(pr,d,use,g){
 const n=+(pr>=2)+ +(d===2),h=[0,3,2,1][pr]+[0,2,1][d]-pop(use),c=3*n+n*(n-1)/2-pop(use);
 return {q:+(pr>0)+2*+(d>0),pr,d,use,h,c,cost:2*h+c+g};
}
function reserve(a,g){return recipe(a.modes[0],a.modes[1],a.use,g).cost;}
function releaseBit(a){return ['train','contract'].includes(a.r[0])?1<<a.r[5]:0;}
function revenue(q,z){let v=0;for(let j=0;j<2;j++)if(q&(1<<j))v+=A[j]-2-2*+(!!(z&(1<<j)));return v}
function cs(q,z){let x=0;for(let j=0;j<2;j++){let n=+(!!(q&(1<<j)))+ +(!!(z&(1<<j)));x+=n*n}return x}
function contested(q,z){return pop(q&z)}
function legalRecipes(s,B,entry=true){
 let out=[];
 for(let pr=0;pr<4;pr++){
  if(pr===2&&!s[0]||pr===3&&!s[1])continue;
  for(let d=0;d<(entry?3:1);d++){
   let auto=+(pr>=2)+2*+(d===2);
   for(let use=0;use<4;use++){
    if(use&~(auto&s[4]))continue;
    const a=recipe(pr,d,use,s[8]);
    if(a.h<=3&&a.c<=5&&a.cost<=B)out.push(a);
   }
  }
 }
 return out;
}
function suffixStage(s,z,B,D,rule=1,entry=true){
 const full=[legalRecipes(s,B,entry),legalRecipes(z,D,entry)];
 const menu=full.map(ls=>{const m=new Map();for(const a of ls)if(!m.has(a.q)||m.get(a.q).cost>a.cost)m.set(a.q,a);return [...m.values()].sort((a,b)=>a.q-b.q)});
 const payoff=(a,b)=>[revenue(a.q,b.q)-a.cost,revenue(b.q,a.q)-b.cost];
 const potential=(a,b)=>revenue(a.q,0)+revenue(b.q,0)-2*pop(a.q&b.q)-a.cost-b.cost;
 const eq=[];
 for(const a of menu[0])for(const b of menu[1]){
  const v=payoff(a,b),P=potential(a,b);
  for(const c of full[0])if(payoff(c,b)[0]-v[0]!==potential(c,b)-P)throw Error('potential 0');
  for(const c of full[1])if(payoff(a,c)[1]-v[1]!==potential(a,c)-P)throw Error('potential 1');
  if(full[0].every(c=>payoff(c,b)[0]<=v[0])&&full[1].every(c=>payoff(a,c)[1]<=v[1]))eq.push({a,b,v});
 }
 if(!eq.length)throw Error('suffix pure existence');
 eq.sort((x,y)=>rule*(y.v[0]+y.v[1]-x.v[0]-x.v[1])||y.v[0]-x.v[0]||x.a.q-y.a.q||x.b.q-y.b.q);
 return {...eq[0],equilibria:eq.length,full:full.map(a=>a.length)};
}
function makeSuffix(rule,enabled=true){
 const cache=new Map(),stats={stage_games:0,full_recipe_counts:0,stage_calls:0,changed_quantities:0,max_stage_equilibria:0};
 function adjust(ss,aa,win){
  const n=aa[0].shifts;if(n!==aa[1].shifts)throw Error('clock mismatch');
  const q=aa.map(a=>a.q),old=[0,1].map(i=>reserve(aa[i],ss[i][8]));
  const bit=aa.map((a,i)=>win[i]?releaseBit(a):0);
  const zero={delta:[0,0],q,refund:[0,0],rev:[0,0],gate:0};
  if(!enabled||n<=1||!bit.some(Boolean))return zero;
  const nu=ss.map((s,i)=>{let x=s.slice();x[4]|=bit[i];return x});
  const key=[...nu.flatMap(x=>[x[0],x[1],x[4],x[8]]),...old].join();
  let e=cache.get(key);
  if(!e){
   e=suffixStage(nu[0],nu[1],old[0],old[1],rule,true);cache.set(key,e);
   stats.stage_games++;stats.full_recipe_counts+=e.full[0]+e.full[1];stats.max_stage_equilibria=Math.max(stats.max_stage_equilibria,e.equilibria);
  }
  const nq=[e.a.q,e.b.q],refund=[e.a,e.b].map((a,i)=>(old[i]-a.cost)*(n-1));
  const rev=nq.map((x,i)=>(revenue(x,nq[1-i])-revenue(q[i],q[1-i]))*(n-1));
  if(refund.some(x=>x<0))throw Error('reservation exceeded');
  // The old operating recipe is always feasible, including in the updated mask.
  for(let i=0;i<2;i++){
   const a=aa[i],r=recipe(a.modes[0],a.modes[1],a.use,ss[i][8]);
   if(r.cost!==old[i]||r.h>3||r.c>5||r.use&~nu[i][4])throw Error('lost old policy');
  }
  stats.stage_calls++;if(nq.some((x,i)=>x!==q[i]))stats.changed_quantities++;
  return {delta:refund.map((x,i)=>x+rev[i]),q:nq,refund,rev,gate:1};
 }
 return {adjust,stats};
}
function study(src,{S=10,concurrent=true,cap=2,rule=1,enabled=true,mixed=false,scaleFactor=125}={}){
 const [base,w,a,m]=src;
 let s;
 if(mixed){
  let x=m.slice(m.indexOf('function makeStudy('),m.indexOf('\nfunction run('));
  x=x.replace('return new Function(s+";return {windowStudy,MIX}")();','return s;');
  s=new Function(x+';return makeStudy;')()(base,w,a);
  s=s.replace('const F=[1,1,1,125,125]','const F=[1,1,1,'+scaleFactor+','+scaleFactor+']');
  s=s.replace(/if\(id==="3,1,0,0,0,0,0,1348,1,1,1,0,0,0,0,0,1348,1,1"&&rule===1\)\{/,'if(false){');
 }else{
  const acc=new Function(a.slice(a.indexOf('function acceleratedSource('),a.indexOf('\nconst compact='))+';return acceleratedSource;')();
  s=acc(base,w);
 }
 function patch(x,y){if(!s.includes(x))throw Error('source mismatch '+x);s=s.replace(x,y)}
 const suffix=makeSuffix(rule,enabled),stats=suffix.stats;
 // Equal transition and quantity are insufficient: differing gross reservation
 // changes the post-release feasible set. Keep separate representatives.
 function signature(a,s,h){
  return enabled&&h>1&&a.shifts>1?','+reserve(a,s[8])+','+releaseBit(a)+','+(releaseBit(a)?a.r[4]:0):'';
 }
 const adjMemo=new Map();
 function expected(s,z,a,b){
  if(!enabled||a.shifts<=1||(!releaseBit(a)&&!releaseBit(b)))return [0,0];
  const k=[s[0],s[1],s[4],s[8],z[0],z[1],z[4],z[8],a.shifts,a.q,b.q,reserve(a,s[8]),reserve(b,z[8]),releaseBit(a),releaseBit(b),a.r[4],b.r[4]].join();
  let v=adjMemo.get(k);if(v)return v;
  v=[0,0];
  for(let x=0;x<2;x++)for(let y=0;y<2;y++){
   const wt=(x?a.r[4]:4-a.r[4])*(y?b.r[4]:4-b.r[4]);if(!wt)continue;
   const e=suffix.adjust([s,z],[a,b],[x,y]);
   for(let i=0;i<2;i++)v[i]+=wt*e.delta[i];
  }
  // integer numerator with denominator 16.
  adjMemo.set(k,v);return v;
 }
 patch('keep,ng,(h===1||quotient&&B>=L(h))?0:cost].join();','keep,ng,(h===1||quotient&&B>=L(h))?0:cost].join()+SIG(a,s,h);');
 patch('q=a.q+","+j,prev=out.get(q)','q=a.q+","+j+SIG(a,s,h),prev=out.get(q)');
 patch('let v=[scale*(rev(a.a,b.a)-a.a.cost)+cv0[k],scale*(rev(b.a,a.a)-b.a.cost)+cv1[k]];','let ex=EXPECT(s,z,a.a,b.a);let v=[scale*(rev(a.a,b.a)-a.a.cost)+cv0[k]+scale/16*ex[0],scale*(rev(b.a,a.a)-b.a.cost)+cv1[k]+scale/16*ex[1]];');
 patch('for(let u=0;u<4;u++)for(let v=0;v<4;v++){','for(let u=0;u<4;u++)for(let v=0;v<4;v++){let ext=ADJUST(ss,actions,[u<actions[0].r[4],v<actions[1].r[4]]);let mass=wt/16,ns=actions[0].shifts-1;row.suffix_gate=(row.suffix_gate||0)+mass*ext.gate;for(let i=0;i<2;i++){let dq=ext.q[i],oq=actions[i].q;row.jobs+=mass*ns*(POP(dq)-POP(oq));row.physical+=mass*ns*(+(!!(dq&1))- +(!!(oq&1)));row.digital+=mass*ns*(+(!!(dq&2))- +(!!(oq&2)));row["net"+i]+=mass*ext.delta[i];row.suffix_refunds=(row.suffix_refunds||0)+mass*ext.refund[i];row.suffix_revenue_change=(row.suffix_revenue_change||0)+mass*ext.rev[i];}row.customer_surplus+=mass*ns*(CS(ext.q[0],ext.q[1])-CS(actions[0].q,actions[1].q));row.contested_market_shifts+=mass*ns*(CONT(ext.q[0],ext.q[1])-CONT(actions[0].q,actions[1].q));');
 patch('z[6]+=R[i]-a.cost;','z[6]+=R[i]-a.cost+ext.delta[i];');
 const run=new Function('SIG','EXPECT','ADJUST','POP','CS','CONT',s+';return {windowStudy,mixes:typeof MIX==="undefined"?[]:MIX};')(signature,expected,suffix.adjust,pop,cs,contested);
 const result=run.windowStudy({N:Math.ceil(S/2),early:[1,1,Math.floor(S/2)],entry:3,kitPrice:4,concurrent,only:['scale_'+cap],rules:[rule],license:100,contractDev:100,developCompute:1,developBase:3,budget:30000000}).results[0];
 return {spec:{S,concurrent,cap,rule,enabled,mixed,scaleFactor},stats,result,mixed_subgames:run.mixes.map(x=>({id:x.id,p:[x.m.pn,x.m.pd],q:[x.m.qn,x.m.qd],matrix:x.m.matrix,checked:x.checked,den:x.den}))};
}
function witnesses(){
 let all=[],counts={own_signatures:0,stage_profiles:0,changes:0,adverse_rival:0,positive_jobs:0,negative_jobs:0},examples={};
 // Enumerate every installed arm/mobile mask, inherited qualified mask and lab state,
 // every feasible first service recipe, and every single newly qualified target.
 for(let k=0;k<4;k++)for(let m=0;m<4;m++)for(let g=0;g<2;g++){
  const s=[+(!!(k&1)),+(!!(k&2)),0,0,m,0,10000,3,g],seen=new Set();
  for(const a of legalRecipes(s,10000)){
   for(const bit of [0,1,2]){
    if(bit&m)continue;
    // A successful training action must actually fit the first shift, either
    // internal 1H+2C with open lab or outside 1H+0C. Both preserve hardware.
    if(bit&&a.h+1>3)continue;
    const key=[a.q,a.cost,bit].join();if(seen.has(key))continue;seen.add(key);
    all.push({s,a,bit});
   }
  }
 }
 counts.own_signatures=all.length;
 for(const x of all)for(const y of all){
  if(!x.bit&&!y.bit)continue;
  let nu=[x.s.slice(),y.s.slice()];nu[0][4]|=x.bit;nu[1][4]|=y.bit;
  const e=suffixStage(nu[0],nu[1],x.a.cost,y.a.cost,1);
  const oq=[x.a.q,y.a.q],nq=[e.a.q,e.b.q],old=[revenue(oq[0],oq[1])-x.a.cost,revenue(oq[1],oq[0])-y.a.cost];
  const dj=pop(nq[0])+pop(nq[1])-pop(oq[0])-pop(oq[1]);
  counts.stage_profiles++;if(nq.some((q,i)=>q!==oq[i]))counts.changes++;
  if(dj>0)counts.positive_jobs++;if(dj<0)counts.negative_jobs++;
  if(x.bit&&!y.bit&&e.v[1]<old[1])counts.adverse_rival++;
  for(const [name,ok] of [['expansion',dj>0],['contraction',dj<0],['rival_loss',x.bit&&!y.bit&&e.v[1]<old[1]],['reservation_sensitive',false]]){
   if(ok&&!examples[name])examples[name]={x,y,old,e,dj};
  }
 }
 return {counts,examples};
}

function qualificationAudit(){
 const all=[];
 for(let k=0;k<4;k++)for(let m=0;m<4;m++)for(let g=0;g<2;g++){
  const s=[+(!!(k&1)),+(!!(k&2)),0,0,m,0,10000,3,g],seen=new Set();
  for(const a of legalRecipes(s,10000))for(const bit of [0,1,2]){
   if(bit&m||bit&&a.h+1>3)continue;
   const key=[a.q,a.cost,bit].join();if(seen.has(key))continue;seen.add(key);all.push({s,a,bit});
  }
 }
 const res={};
 for(const rule of [1,-1]){
  const cache=new Map(),counts={matched:0,strict_gain:0,tie:0,strict_loss:0,rival_losses:0,unique_both_losses:0,gate_gain:0,gate_tie:0,gate_loss:0},examples={};
  function E(s,z,B,D){const key=[s[0],s[1],s[4],s[8],z[0],z[1],z[4],z[8],B,D].join();if(!cache.has(key))cache.set(key,suffixStage(s,z,B,D,rule));return cache.get(key)}
  for(const x of all)for(const y of all){
   if(!x.bit||y.bit)continue;
   const s=x.s.slice();s[4]|=x.bit;
   const e0=E(x.s,y.s,x.a.cost,y.a.cost),e1=E(s,y.s,x.a.cost,y.a.cost),v=e1.v[0]-e0.v[0],rg=e1.v[1]-e0.v[1],locked=revenue(x.a.q,y.a.q)-x.a.cost,g=e1.v[0]-locked;
   counts.matched++;counts[v>0?"strict_gain":v<0?"strict_loss":"tie"]++;counts[g>0?"gate_gain":g<0?"gate_loss":"gate_tie"]++;
   if(rg<0)counts.rival_losses++;if(v<0&&e0.equilibria===1&&e1.equilibria===1)counts.unique_both_losses++;
   for(const [n,b] of [["own_loss",v<0],["unique_own_loss",v<0&&e0.equilibria===1&&e1.equilibria===1],["rival_loss",rg<0],["gate_loss",g<0]])if(b&&!examples[n])examples[n]={x,y,e0,e1,locked,v,rg,g};
  }
  res[rule]={counts,examples,games:cache.size};
 }
 return res;
}
function reservationWitness(){
 const s=[1,0,0,0,1,0,10000,2,1],z=[0,0,0,0,0,0,10000,0,0],nu=s.slice();nu[4]|=2;
 const low=recipe(2,0,1,1),high=recipe(2,0,0,1);
 if([low,high].some(a=>a.h+1>3||a.c+2>5))throw Error("infeasible first shift with internal training");
 const l=suffixStage(nu,z,low.cost,0),h=suffixStage(nu,z,high.cost,0);
 const n=5,p=1/2,setup=4;
 const expected=(a,e)=>n*(revenue(a.q,0)-a.cost)-setup+p*(n-1)*(e.v[0]-revenue(a.q,0)+a.cost);
 const v=[expected(low,l),expected(high,h)];
 if(JSON.stringify(v)!==JSON.stringify([51,60])||l.equilibria!==1||h.equilibria!==1)throw Error("reservation witness");
 return {s,z,low,high,success_low:l,success_high:h,n,p,setup,expected_net:v,difference:v[1]-v[0]};
}
function gateWitness(){
 const s=[0,1,0,0,1,0,10000,3,0],z=[1,0,0,0,3,0,10000,3,0],nu=s.slice();nu[4]|=2;
 const a=recipe(3,1,1,0),b=recipe(2,0,0,0);
 if(a.h+1>3)throw Error("infeasible qualification");
 // Outside training (coordination 1H, no in-house compute), same fee in both outcomes.
 const locked=revenue(a.q,b.q)-a.cost;
 const oldFixed=Math.max(...legalRecipes(s,a.cost).map(r=>revenue(r.q,b.q)-r.cost));
 const newFixed=Math.max(...legalRecipes(nu,a.cost).map(r=>revenue(r.q,b.q)-r.cost));
 const openFailure=suffixStage(s,z,a.cost,b.cost),openSuccess=suffixStage(nu,z,a.cost,b.cost);
 if(locked!==20||oldFixed!==20||newFixed!==21||openFailure.v[0]!==18||openSuccess.v[0]!==19||openFailure.equilibria!==1||openSuccess.equilibria!==1)throw Error("gate witness");
 return {s,z,a,b,locked,oldFixed,newFixed,openFailure,openSuccess};
}
const retrieved_sha256={"service_window.js":"186a31e6242696293ba43d0de99adb04f29243ab9029a0bf945d3d0940d58269","staggered_window.js":"d60d120033a4c5fcaacd0b11791bb89008a59138d8a51c8861ad0bd8ada13730","concurrent_window.js":"81093d955cc3b0b019075d50d7981200a72e0aed6df568d199f21940a66d1e97","mixed_continuation.js":"1b7207e5c5b15eb65eb4de4f25a30d5fbb1607d03cc92dbfed1ca0f06a03ebbe"};
if(typeof module!=='undefined'){module.exports={study,pins,suffixStage,witnesses,qualificationAudit,reservationWitness,gateWitness};if(require.main===module){const fs=require('fs'),path=require('path'),crypto=require('crypto');const src=Object.entries(retrieved_sha256).map(([name,sha])=>{const b=fs.readFileSync(path.join(__dirname,name));const h=crypto.createHash('sha256').update(b).digest('hex');if(h!==sha)throw Error('input bytes mismatch '+name+' got '+h);return b.toString('utf8')});const exp=require('./event_suffix_results.json');for(const e of exp.runs){const r=study(src,e.spec);if(JSON.stringify(r)!==JSON.stringify(e))throw Error('replay mismatch '+JSON.stringify(e.spec))}for(const [k,f] of Object.entries({witnesses,qualificationAudit,reservationWitness,gateWitness}))if(JSON.stringify(f())!==JSON.stringify(exp[k]))throw Error(k+' replay mismatch');console.log('verified '+exp.runs.length+' suffix games and exhaustive suffix states')}}
