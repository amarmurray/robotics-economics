'use strict';
// Whole finite-game certificate in a common mobile-kit price, across all dates.
// Fixes a complete behavioral equilibrium at the seed, including mixed probabilities.
const fs=require('fs'),path=require('path'),crypto=require('crypto');
function makeCertificate(seed=4,concurrent=false,cap=2,rule=1){
 if(!Number.isInteger(seed)||seed<0||seed>500)throw Error('integer seed outside prefunded domain');
 const names=['service_window.js','staggered_window.js','concurrent_window.js'];
 const expected=JSON.parse(fs.readFileSync(path.join(__dirname,'mixed_continuation_results.json'),'utf8'));
 const src=names.map(n=>{let s=fs.readFileSync(path.join(__dirname,n),'utf8');if(crypto.createHash('sha256').update(s).digest('hex')!==expected.source_sha256[n])throw Error('Antecedent changed '+n);return s;});
 let wrapper=fs.readFileSync(path.join(__dirname,'mixed_continuation.js'),'utf8');
 if(crypto.createHash('sha256').update(wrapper).digest('hex')!=='7457f682f5bbd1933f386b5ad1167715cc134dfa195366a3a22ea3e38d038514')throw Error('mixed source changed');
 wrapper=wrapper.slice(wrapper.indexOf('function makeStudy('),wrapper.indexOf('\nfunction run('));
 wrapper=wrapper.replace('return new Function(s+";return {windowStudy,MIX}")();','return s;');
 let s=new Function(wrapper+';return makeStudy;')()(...src);
 const replaySource=s,SAVED=new Map();
 function patch(a,b){if(!s.includes(a))throw Error('Source mismatch '+a);s=s.replace(a,b);}
 patch('cv1=new Float64Array(ca*cb),seen=', 'cv1=new Float64Array(ca*cb),cd0=new Float64Array(ca*cb),cd1=new Float64Array(ca*cb),seen=');
 patch('let v0=0,v1=0;kernelPairs++;','let v0=0,v1=0,d0=0,d1=0;kernelPairs++;');
 patch('let t=V(x,y,h-1).v;v0+=w*u*t[0]*F[h]/F[h-1];v1+=w*u*t[1]*F[h]/F[h-1]',
       'let child=V(x,y,h-1),t=child.v;v0+=w*u*t[0]*F[h]/F[h-1];v1+=w*u*t[1]*F[h]/F[h-1];d0+=w*u*child.dv[0]*F[h]/F[h-1];d1+=w*u*child.dv[1]*F[h]/F[h-1]');
 patch('cv0[k]=v0;cv1[k]=v1;seen[k]=1','cv0[k]=v0;cv1[k]=v1;cd0[k]=d0;cd1[k]=d1;seen[k]=1');
 patch('throw Error("integer precision");return v', 'throw Error("integer precision");v.d=[cd0[k]-scale*ORDER(a.a),cd1[k]-scale*ORDER(b.a)];if(!v.d.every(Number.isSafeInteger))throw Error("slope precision");if(!v.d.every(x=>x>=-scale&&x<=0))throw Error("at most one mobile order");return v');
 patch('if(!out.has(key)||out.get(key).cost>cost)out.set(key,a);',
       'if(out.has(key)&&ORDER(out.get(key))!==ORDER(a))throw Error("parameter-dependent menu reduction");if(!out.has(key)||out.get(key).cost>cost)out.set(key,a);');
 patch('let result={v:m.v,mix,cert:{den},n:0};', `
 let ds=[0,0];for(const [x,p] of [[i,pd-pn],[k,pn]])for(const [y,q] of [[j,qd-qn],[l,qn]]){
  const d=value(aa[x],bb[y]).d;ds[0]+=p*q*d[0];ds[1]+=p*q*d[1];
 }
 const dv=ds.map(x=>x/den);if(!dv.every(Number.isSafeInteger))throw Error('mixed slope denominator');
 for(const a of ga.all){const x=value(a,bb[j]),y=value(a,bb[l]);CERT.add(m.v[0]*qd-u(x[0],y[0],qn,qd),dv[0]*qd-u(x.d[0],y.d[0],qn,qd),{id,player:0,action:a.a,kind:'mixed',scale:scale*qd});}
 for(const b of gb.all){const x=value(aa[i],b),y=value(aa[k],b);CERT.add(m.v[1]*pd-u(x[1],y[1],pn,pd),dv[1]*pd-u(x.d[1],y.d[1],pn,pd),{id,player:1,action:b.a,kind:'mixed',scale:scale*pd});}
 let result={v:m.v,dv,mix,cert:{den},n:0};`);
 patch('let result={v:e.v,a:aa[e.i].a,b:bb[e.j].a,n};', `
 const dv=value(aa[e.i],bb[e.j]).d;
 for(const a of ga.all){const v=value(a,bb[e.j]);CERT.add(e.v[0]-v[0],dv[0]-v.d[0],{id,player:0,action:a.a,kind:'pure',scale});}
 for(const b of gb.all){const v=value(aa[e.i],b);CERT.add(e.v[1]-v[1],dv[1]-v.d[1],{id,player:1,action:b.a,kind:'pure',scale});}
 let result={v:e.v,dv,a:aa[e.i].a,b:bb[e.j].a,n};`);
 // The previous local fee witness is a separate study, and is not assumed invariant.
 patch('if(id==="3,1,0,0,0,0,0,1348,1,1,1,0,0,0,0,0,1348,1,1"&&rule===1){','if(false){');
 patch('dated,profiles,states:memo.size,deviations:dev','dated,root_slope:root.dv.map(x=>x/(16**c.T*F[c.T])),profiles,states:memo.size,deviations:dev');
 const certificates=[];
 const CERT={add(a,b,detail){if(!Number.isSafeInteger(a)||!Number.isSafeInteger(b))throw Error('certificate precision');if(a<0)throw Error('seed incentive violated');certificates.push({a,b,...detail});}};
 s=s.replaceAll('memo.set(id,result);return result','SAVED.set(id,result);memo.set(id,result);return result');
 const study=new Function('CERT','SAVED','const ORDER=a=>+(a.b[0]==="order"&&a.b[4]===1);'+s+';return {windowStudy,MIX};')(CERT,SAVED);
 const opts={N:5,early:[1,1,5],entry:3,kitPrice:seed,concurrent,only:['scale_'+cap],rules:[rule],license:100,contractDev:100,developCompute:1,developBase:3,budget:30000000};
 const result=study.windowStudy(opts).results[0];
 if(result.status!=='solved')return {seed,concurrent,cap,rule,result};
 const gcd=(a,b)=>b?gcd(b,a%b):a<0n?-a:a;
 const fraction=(n,d=1n)=>{if(d<0n){n=-n;d=-d;}const g=gcd(n,d);return [n/g,d/g];};
 const cmp=(x,y)=>x[0]*y[1]-y[0]*x[1];
 let lower=[0n,1n],upper=[500n,1n],lowBindings=[],upBindings=[];
 for(const c of certificates){if(!c.b)continue;
  const bound=fraction(BigInt(seed)*BigInt(c.b)-BigInt(c.a),BigInt(c.b));
  if(c.b>0){const d=cmp(bound,lower);if(d>0n){lower=bound;lowBindings=[c];}else if(d===0n)lowBindings.push(c);}
  else{const d=cmp(bound,upper);if(d<0n){upper=bound;upBindings=[c];}else if(d===0n)upBindings.push(c);}
 }
 if(cmp(lower,upper)>0n)throw Error('empty certificate containing seed');
 for(const x of [lower,upper])for(const c of certificates){
  const v=BigInt(c.a)*x[1]+BigInt(c.b)*(x[0]-BigInt(seed)*x[1]);if(v<0n)throw Error('endpoint certificate failed');
 }
 const enc=x=>x.map(Number);
 const endpointReplay=[lower,upper].map(x=>{if(x[1]!==1n)throw Error('endpoint replay requires integer endpoint');return replayFixedProfile(replaySource,SAVED,opts,seed,Number(x[0]));});
 if(endpointReplay.some(r=>r.states!==SAVED.size||r.full_deviations!==certificates.length))throw Error('endpoint state or deviation coverage');
 const totalOrders=result.dated.reduce((a,r)=>a+r.orders,0);
 if(result.root_slope.reduce((a,b)=>a+b,0)!==-totalOrders)throw Error('root order envelope');
 const compact=c=>({state:c.id,player:c.player,kind:c.kind,slack_at_seed:c.a,slope:c.b,scale:c.scale,action:{q:c.action.q,research:c.action.r[0],build:c.action.b[0],retain:c.action.keep,next_scope:c.action.ng}});
 return {seed,concurrent,cap,rule,status:'certified',endpoint_replay:endpointReplay,root_order_envelope:{expected_total_orders:totalOrders,total_price_slope:result.root_slope.reduce((a,b)=>a+b,0)},interval:{lower:enc(lower),upper:enc(upper),closed:true},binding_counts:{lower:lowBindings.length,upper:upBindings.length},binding_examples:{lower:lowBindings.slice(0,4).map(compact),upper:upBindings.slice(0,4).map(compact)},certificate_count:certificates.length,identical_slacks:certificates.filter(c=>c.a===0&&c.b===0).length,mixed_subgames:study.MIX.length,mixed_probabilities:study.MIX.map(m=>({state:m.id,p:[m.m.pn,m.m.pd],q:[m.m.qn,m.m.qd]})),generated_wealth:result.wealth.map(x=>x-10000),root_slope:result.root_slope,states:result.states,profiles:result.profiles,full_deviations:result.fullDev,dated:result.dated};
}

// Independent endpoint arithmetic: re-evaluate the fixed behavioral profile at the
// actual endpoint price, without using derivative propagation or root finding.
// Every baseline state is explicitly visited, including joint-deviation states.
function replayFixedProfile(source,saved,opts,seed,price){
 let s=source,visited=0,maxGain=0;
 function patch(a,b){if(!s.includes(a))throw Error('replay source mismatch '+a);s=s.replace(a,b);}
 const signature=a=>JSON.stringify([a.q,a.modes,a.use,a.r,[a.b[0],a.b[1],a.b[2],a.b[4],a.b[5]],a.keep,a.ng]);
 const safe=x=>{if(!Number.isSafeInteger(x))throw Error('replay integer precision');return x;};
 const replay=(id,ga,gb,value)=>{
  const old=saved.get(id);if(!old)throw Error('endpoint state outside certified domain '+id);
  const find=(all,a)=>{const key=signature(a),r=all.find(r=>signature(r.a)===key);if(!r)throw Error('endpoint action missing');return r;};
  const den=old.cert?.den??1;
  const profiles=(old.mix??[{a:old.a,b:old.b,w:1}]).map(p=>({a:find(ga.all,p.a),b:find(gb.all,p.b),w:p.w}));
  const v=[0,0];for(const p of profiles){let q=value(p.a,p.b);for(let i=0;i<2;i++)v[i]=safe(v[i]+safe(p.w*q[i]));}
  for(let i=0;i<2;i++){
   v[i]=safe(v[i]/den);
   if(BigInt(v[i])!==BigInt(old.v[i])+BigInt(old.dv[i])*BigInt(price-seed))throw Error('affine endpoint value mismatch');
  }
  let checked=0;
  for(let i=0;i<2;i++)for(const a of (i===0?ga.all:gb.all)){
   let deviation=0;for(const p of profiles)deviation=safe(deviation+safe(p.w*(i===0?value(a,p.b):value(p.a,a))[i]));
   const gain=safe(deviation-safe(den*v[i]));if(gain>0)throw Error('endpoint profitable deviation');maxGain=Math.max(maxGain,gain);checked++;
  }
  visited++;
  return {result:{v,mix:profiles.map(p=>({a:p.a.a,b:p.b.a,w:p.w})),cert:{den},n:0},checked};
 };
 patch('  for(let i=0;i<aa.length;i++)for(let j=0;j<bb.length;j++){',
       '  {const checked=REPLAY(id,ga,gb,value);fullDev+=checked.checked;memo.set(id,checked.result);return checked.result;}\n  for(let i=0;i<aa.length;i++)for(let j=0;j<bb.length;j++){');
 patch('let root=V(...S,c.T),mixDen=1,dist=',
       'let root=V(...S,c.T);for(const id of SAVED.keys()){const x=id.split(",").map(Number);V(x.slice(1,10),x.slice(10),x[0]);}let mixDen=1,dist=');
 const run=new Function('REPLAY','SAVED',s+';return windowStudy;')(replay,saved);
 const result=run({...opts,kitPrice:price}).results[0];
 if(result.status!=='solved'||visited!==saved.size)throw Error('endpoint replay incomplete');
 return {price,states:visited,full_deviations:result.fullDev,max_deviation_gain: maxGain,
  generated_wealth:result.wealth.map(x=>x-10000),jobs:result.dated.reduce((x,r)=>x+r.jobs,0),
  customer_surplus:result.dated.reduce((x,r)=>x+r.customer_surplus,0),dated_accounting:'passed',all_state_affine_values:'passed'};
}
module.exports={makeCertificate};
if(require.main===module){
 if(process.argv[2]==='--reproduce'){
  const expected=JSON.parse(fs.readFileSync(path.join(__dirname,'dynamic_kit_certificate_results.json'),'utf8'));
  for(const e of expected.runs){const got=makeCertificate(e.seed,e.concurrent,e.cap,e.rule);if(JSON.stringify(got)!==JSON.stringify(e))throw Error('certificate replay mismatch');}
  console.log('verified '+expected.runs.length+' common-price certificates and '+2*expected.runs.length+' full-state endpoint replays');
 }else console.log(JSON.stringify(makeCertificate(Number(process.argv[2]||4),process.argv[3]==='concurrent',Number(process.argv[4]||2),Number(process.argv[5]||1)),null,2));
}
