'use strict';
// Factored first-shift and suffix payoff, same full funded game; independent reserve and both-open only.
// Source-specific transformations fail closed. Forward dated ledger remains inherited.
function factorBuild(reservationSource,suffixSource){
 const patch=(s,a,b)=>{if(!s.includes(a))throw Error("missing "+a);return s.replace(a,b)};
 const injections=[
 ['let trans=[],ids=new Map(),out=new Map(),all=[];','let trans=[],ids=new Map(),out=new Map(),all=[],sigs=new Map();'],
 ['let j=ids.get(k),q=a.q+","+j+SIG(a,s,h),prev=out.get(q),record={a,j,idx};','let j=ids.get(k),sig=SIG(a,s,h);if(!sigs.has(sig))sigs.set(sig,sigs.size);let q=a.q+","+j+sig,prev=out.get(q),record={a,j,idx,si:sigs.get(sig)};'],
 ['trans,all};groups.set(id,g);','trans,all,ns:sigs.size};groups.set(id,g);'],
 ['function value(a,b){','let sd0=new Float64Array(ga.ns*gb.ns),sd1=new Float64Array(ga.ns*gb.ns),sseen=new Uint8Array(ga.ns*gb.ns);function value(a,b){'],
 ['let ex=EXPECT(s,z,a.a,b.a);let v=[scale*(rev(a.a,b.a)-a.a.cost)+cv0[k]+scale/16*ex[0],scale*(rev(b.a,a.a)-b.a.cost)+cv1[k]+scale/16*ex[1]];','let v;if(a.a.reopen){let l=a.si*gb.ns+b.si;if(!sseen[l]){let ex=EXPECT(s,z,a.a,b.a);sd0[l]=ex[0];sd1[l]=ex[1];sseen[l]=1}let n=a.a.shifts;v=[scale*(rev(a.a,b.a)/n-a.a.cost+(n-1)*a.a.reservation)+cv0[k]+scale/16*sd0[l],scale*(rev(b.a,a.a)/n-b.a.cost+(n-1)*b.a.reservation)+cv1[k]+scale/16*sd1[l]]}else v=[scale*(rev(a.a,b.a)-a.a.cost)+cv0[k],scale*(rev(b.a,a.a)-b.a.cost)+cv1[k]];']
 ];
 let insert=injections.map(([a,b])=>"patch("+JSON.stringify(a)+","+JSON.stringify(b)+");").join("\n");
 let old=" return new Function(source+';return {study,suffixStage,legalRecipes,recipe,revenue,reservationWitness,gateWitness};')();";
 let lines=[
 ["a.shifts,a.q,b.q,reserve(a,s[8]),reserve(b,z[8]),releaseBit(a),releaseBit(b),a.r[4],b.r[4]","a.shifts,reserve(a,s[8]),reserve(b,z[8]),releaseBit(a),releaseBit(b),releaseBit(a)?a.r[4]:0,releaseBit(b)?b.r[4]:0"],
 ["const e=suffix.adjust([s,z],[a,b],[x,y]);","const e=suffix.adjust([s,z],[{...a,q:0},{...b,q:0}],[x,y]);"],
 ["v[i]+=wt*e.delta[i]","v[i]+=wt*(e.delta[i]-(a.shifts-1)*reserve(i?b:a,i?z[8]:s[8]))"],
 [" const run=new Function('INDEPENDENT','RESERVES','AUDIT','SIG','EXPECT','ADJUST','POP','CS','CONT',",insert+"\n const run=new Function('INDEPENDENT','RESERVES','AUDIT','SIG','EXPECT','ADJUST','POP','CS','CONT',"],
 ["budget:30000000","budget:120000000"]
 ];
 reservationSource=patch(reservationSource,old,lines.map(([a,b])=>"p("+JSON.stringify(a)+","+JSON.stringify(b)+");").join("\n")+"\n"+old);
 const core=new Function(reservationSource+";return build;")()(suffixSource);
 return {...core,study:(src,spec)=>{if(!spec.enabled||!spec.independent||!spec.alwaysOpen||spec.mixed)throw Error("Only the prefunded both-open independent-reserve pure selector is certified");return core.study(src,spec)}}
}
function compact(r){const x=r.result;return {spec:r.spec,status:x.status,reason:x.reason,wealth:x.wealth,wealth_numerator:x.wealth_numerator,wealth_denominator:x.wealth_denominator,root:x.root,dated:x.dated,profiles:x.profiles,states:x.states,deviations:x.deviations,fullDev:x.fullDev,kernelPairs:x.kernelPairs,checks:r.checks,mixed_subgames:r.mixed_subgames};}
if(typeof module!=='undefined'){
 module.exports={factorBuild,compact};
 if(require.main===module){
 const fs=require('fs'),path=require('path'),crypto=require('crypto');
 const e=require('./event_reserve_factor_results.json');
 const names=['service_window.js','staggered_window.js','concurrent_window.js','mixed_continuation.js','event_suffix.js','event_reservations.js'];
 const src=names.map(n=>{const b=fs.readFileSync(path.join(__dirname,n));if(crypto.createHash('sha256').update(b).digest('hex')!==e.source_sha256[n])throw Error('source bytes mismatch '+n);return b.toString('utf8')});
 const a=factorBuild(src[5],src[4]);
 const chosen=process.argv[2]===undefined?e.runs:e.runs.filter((r,i)=>i===Number(process.argv[2]));
 if(!chosen.length)throw Error('unknown run index');
 for(const r of chosen){const z=compact(a.study(src.slice(0,4),r.spec));if(JSON.stringify(z)!==JSON.stringify(r))throw Error('replay mismatch '+JSON.stringify(r.spec))}
 console.log('verified '+chosen.length+' factored games');
 }
}
