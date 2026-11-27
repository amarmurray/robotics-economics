'use strict';
// Event clock and one optional same-recipe qualification release.
const retrieved_sha256={"service_window.js":"186a31e6242696293ba43d0de99adb04f29243ab9029a0bf945d3d0940d58269","staggered_window.js":"d60d120033a4c5fcaacd0b11791bb89008a59138d8a51c8861ad0bd8ada13730","concurrent_window.js":"81093d955cc3b0b019075d50d7981200a72e0aed6df568d199f21940a66d1e97","mixed_continuation.js":"1b7207e5c5b15eb65eb4de4f25a30d5fbb1607d03cc92dbfed1ca0f06a03ebbe"};
const pins={"service_window.js":"004bb37abae4176ab49a144b40c82d95fa7a11d6","staggered_window.js":"dc0243b11599ef87e584824eebf7a66a91394007","concurrent_window.js":"8d7d8090bf90f160835b72793e108f5c1fad9216","mixed_continuation.js":"4c27fbb1b0a4b59a3fd6de51feaf0ff019df1b06"};
function study(src,{S=10,concurrent=true,cap=2,rule=1,release=false,mixed=false,scaleFactor=125}={}){
 const [base,w,a,m]=src;
 let s;
 if(mixed){
  let x=m.slice(m.indexOf('function makeStudy('),m.indexOf('\nfunction run('));
  x=x.replace('return new Function(s+";return {windowStudy,MIX}")();','return s;');
  s=new Function(x+';return makeStudy;')()(base,w,a);
  s=s.replace('const F=[1,1,1,125,125]', 'const F=[1,1,1,'+scaleFactor+','+scaleFactor+']');
  s=s.replace(/if\(id==="3,1,0,0,0,0,0,1348,1,1,1,0,0,0,0,0,1348,1,1"&&rule===1\)\{/,'if(false){');
 }else{
  const acc=new Function(a.slice(a.indexOf('function acceleratedSource('),a.indexOf('\nconst compact='))+';return acceleratedSource;')();
  s=acc(base,w);
 }
 const counts={raw_actions:0,own_action_rival_quantity_cases:0,branch_checks:0,release_eligible_actions:0,max_refund:0};
 const pop=x=>+(!!(x&1))+(!!(x&2))+(!!(x&4));
 const saving=a=>{
  if(!release||!['train','contract'].includes(a.r[0]))return 0;
  const [pr,d1]=a.modes,auto=(pr>=2?1:0)|(d1===2?2:0),bit=1<<a.r[5];
  return auto&bit&&!(a.use&bit)?3*(a.shifts-1):0;
 };
 const eff=a=>4*a.cost-saving(a)*a.r[4];
 function recipes(a,use){
  const [pr,d1,d2]=a.modes;
  if(d2!==0)throw Error('unexpected third market');
  const human=[0,3,2,1][pr]+[0,2,1][d1]-pop(use);
  const copies=+(pr>=2)+ +(d1===2);
  return [human,3*copies+copies*(copies-1)/2-pop(use)];
 }
 function event(s,a,R){
  const gross=a.cost,k=a.r[5],chance=a.r[4];
  if(gross>s[6]||!Number.isInteger(R/a.shifts))throw Error('event upfront reservation');
  const p=[...s];p[6]-=gross;
  let due=0;for(let j=0;j<a.shifts;j++)due+=R/a.shifts;
  p[6]+=due;p[7]|=a.keep;p[8]=a.ng;
  const b=a.b;
  if(b[0]==='order'){if(s[b[4]]||s[b[4]+2])throw Error('event order');p[b[4]+2]=1}
  if(b[0]==='assemble'){if(s[b[4]]||!s[b[4]+2])throw Error('event assembly');p[b[4]]=1;p[b[4]+2]=0}
  if(!chance)return [[p,4]];
  const y=p.slice();
  if(a.r[0]==='buy_archive')y[7]|=1<<k;
  else if(k===3)y[5]+=1;
  else if(k>=0)y[4]|=1<<k;
  y[6]+=saving(a);
  return chance===4?[[y,4]]:[[p,4-chance],[y,chance]];
 }
 function audit(s,a,h,rev,legacy){
  counts.raw_actions++;
  const [l,c]=recipes(a,a.use),r=a.r,b=a.b,g=s[8];
  if(a.hh!==l+r[1]+b[1]||a.cc!==c+r[2]+b[2]+pop(a.keep))throw Error('event first shift resources');
  if(a.hh>3||a.cc>5||l>3||c>5||l<0||c<0)throw Error('event resource bound');
  const base=2*l+c+g,setup=2*(r[1]+b[1])+r[2]+b[2]+pop(a.keep)+r[3]+b[3]+2*+(!g&&a.ng);
  let total=setup;for(let j=0;j<a.shifts;j++)total+=base;
  if(total!==a.cost||total>s[6])throw Error('event cost identity');
  const refund=saving(a);
  if(refund){
   const [l1,c1]=recipes(a,a.use|(1<<r[5]));
   if(l1!==l-1||c1!==c-1||l1<0||c1<0||!(r[0]==='train'||r[0]==='contract')||s[4]&(1<<r[5]))throw Error('event release qualification');
   if(r[0]==='train'&&(!(s[7]&(1<<r[5]))||!g))throw Error('event inherited evidence');
   counts.release_eligible_actions++;counts.max_refund=Math.max(counts.max_refund,refund);
  }
  for(let q=0;q<4;q++){
   let R=0;for(let j=0;j<2;j++)if(a.q&(1<<j))R+=([18,14][j]-2-2*+(!!(q&(1<<j))))*a.shifts;
   if(R!==rev(a,{q}))throw Error('event revenue identity');
   const x=legacy(s,a,R),y=event(s,a,R);
   if(x.length!==y.length)throw Error('event transition length');
   for(let i=0;i<x.length;i++){
    const [old,w]=x[i],[nu,z]=y[i],success=r[4]===4||i===1;
    const expect=old.slice();if(success)expect[6]+=refund;
    if(w!==z||JSON.stringify(expect)!==JSON.stringify(nu))throw Error('event transition mismatch '+JSON.stringify({s,a,R,expect,nu}));
    counts.branch_checks++;
   }
   counts.own_action_rival_quantity_cases++;
  }
 }
 function patch(x,y){if(!s.includes(x))throw Error('source mismatch '+x);s=s.replace(x,y)}
 patch('function next(s,a,R){','function next(s,a,R){return EVENT(s,a,R)}\n function legacyNext(s,a,R){');
 patch('let a={q,shifts:shifts(h),modes:[pr,d1,d2],use,copies,hh,cc,cost,r,b,keep,ng};','let a={q,shifts:shifts(h),modes:[pr,d1,d2],use,copies,hh,cc,cost,r,b,keep,ng};AUDIT(s,a,h,rev,legacyNext);');
 patch('out.get(key).cost>cost','EFF(out.get(key))>EFF(a)');
 patch('a.cost<prev.a.cost','EFF(a)<EFF(prev.a)');
 patch('scale*(rev(a.a,b.a)-a.a.cost)+cv0[k],scale*(rev(b.a,a.a)-b.a.cost)+cv1[k]','scale*(rev(a.a,b.a)-a.a.cost+SAVE(a.a)*a.a.r[4]/4)+cv0[k],scale*(rev(b.a,a.a)-b.a.cost+SAVE(b.a)*b.a.r[4]/4)+cv1[k]');
 patch('row["net"+i]+=wt*(R[i]-cost)','row["net"+i]+=wt*(R[i]-cost+SAVE(a)*a.r[4]/4);row.release_refunds=(row.release_refunds||0)+wt*SAVE(a)*a.r[4]/4');
 patch('z[6]+=R[i]-a.cost;','z[6]+=R[i]-a.cost+((i?v:u)<a.r[4]?SAVE(a):0);');
 const run=new Function('EVENT','AUDIT','SAVE','EFF',s+';return {windowStudy,mixes:typeof MIX===\"undefined\"?[]:MIX};')(event,audit,saving,eff);
 const result=run.windowStudy({N:Math.ceil(S/2),early:[1,1,Math.floor(S/2)],entry:3,kitPrice:4,concurrent,only:['scale_'+cap],rules:[rule],license:100,contractDev:100,developCompute:1,developBase:3,budget:30000000}).results[0];
 return {spec:{S,concurrent,cap,rule,release,mixed,scaleFactor},counts,result,mixed_subgames:run.mixes.map(x=>({id:x.id,p:[x.m.pn,x.m.pd],q:[x.m.qn,x.m.qd],matrix:x.m.matrix,checked:x.checked,den:x.den}))};
}
module.exports={study,pins};
if(require.main===module){const fs=require('fs'),path=require('path'),crypto=require('crypto');const src=Object.entries(pins).map(([name,sha])=>{const b=fs.readFileSync(path.join(__dirname,name));const actual=crypto.createHash('sha256').update(b).digest('hex');if(actual!==retrieved_sha256[name])throw Error('input bytes mismatch '+name);return b.toString('utf8')});const expected=require('./event_release_results.json');for(const e of expected.runs){const r=study(src,e.spec);if(JSON.stringify(r)!==JSON.stringify(e))throw Error('replay mismatch '+JSON.stringify(e.spec));}console.log('verified '+expected.runs.length+' event-clock games');}
