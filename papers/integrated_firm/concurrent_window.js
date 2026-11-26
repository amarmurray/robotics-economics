// Exact funded transition-class quotient of the accepted staggered block game.
// CPU only. Run node concurrent_window.js [variant]; all by default.
const fs=require("fs"),path=require("path"),crypto=require("crypto");
const expected=require("./concurrent_window_results.json");
function acceleratedSource(base,wrapper){
 const {edits,transform}=new Function(wrapper.slice(wrapper.indexOf("const edits="),wrapper.indexOf("const compact="))+";return {edits,transform}")();
 let src=transform(base,edits);
 function patch(a,b){if(!src.includes(a))throw Error("source mismatch "+a);src=src.replace(a,b)}
 patch("early=[1,1,1]}","early=[1,1,1],archiveProjection=true,transitionReduction=true}");
 patch("let memo=new Map(),menus=new Map(),profiles=0,dev=0;","let memo=new Map(),menus=new Map(),groups=new Map(),profiles=0,dev=0,fullDev=0,kernelPairs=0;");
 patch("if(quotient){\n   for(const x of [a,b])x[6]","if(quotient){\n   if(archiveProjection)for(const x of [a,b])x[7]&=~x[4];\n   for(const x of [a,b])x[6]");
 const old=src.slice(src.indexOf(" function V(s,z,h){"),src.indexOf(" try{\n  let root="));
 if(!old.includes("let e=null,n=0"))throw Error("V source mismatch");
 const replacement=` function V(s,z,h){
  [s,z]=canon(s,z,h);let id=[h,...s,...z].join();if(memo.has(id))return memo.get(id);
  if(s[6]<L(h)||z[6]<L(h))throw Error("funding quotient not applicable");
  let scale=16**h;
  function group(s){
   let id=[h,...s].join();if(groups.has(id))return groups.get(id);
   let trans=[],ids=new Map(),out=new Map(),all=[];
   for(const [idx,a] of menu(s,h).entries()){
    let d=new Map();
    if(h>1)for(const [x,w] of next(s,a,0)){
      let y=canon(x,x,h-1)[0],k=y.join(),r=d.get(k);if(r)r[1]+=w;else d.set(k,[y,w])
    }
    let k=[...d.entries()].sort((a,b)=>a[0]<b[0]?-1:a[0]>b[0]?1:0).map(([k,[x,w]])=>k+":"+w).join(";");
    if(!ids.has(k)){ids.set(k,trans.length);trans.push([...d.values()])}
    let j=ids.get(k),q=a.q+","+j,prev=out.get(q),record={a,j,idx};all.push(record);
    if(!prev||a.cost<prev.a.cost)out.set(q,record)
   }
   let g={a:transitionReduction?[...out.values()].sort((x,y)=>x.idx-y.idx):all,trans,all};groups.set(id,g);return g
  }
  let ga=group(s),gb=group(z),aa=ga.a,bb=gb.a,br0=bb.map(()=>-Infinity),br1=aa.map(()=>-Infinity);
  let ca=ga.trans.length,cb=gb.trans.length,cv0=new Float64Array(ca*cb),cv1=new Float64Array(ca*cb),seen=new Uint8Array(ca*cb);
  function value(a,b){
   let k=a.j*cb+b.j;
   if(!seen[k]){
    let v0=0,v1=0;kernelPairs++;
    if(h===1){v0=scale*sal(s);v1=scale*sal(z)}
    else for(const [x,w] of ga.trans[a.j])for(const [y,u] of gb.trans[b.j]){let t=V(x,y,h-1).v;v0+=w*u*t[0];v1+=w*u*t[1]}
    cv0[k]=v0;cv1[k]=v1;seen[k]=1
   }
   let v=[scale*(rev(a.a,b.a)-a.a.cost)+cv0[k],scale*(rev(b.a,a.a)-b.a.cost)+cv1[k]];
   if(!v.every(Number.isSafeInteger))throw Error("integer precision");return v
  }
  for(let i=0;i<aa.length;i++)for(let j=0;j<bb.length;j++){
   if(++profiles>budget)throw Error("profile budget");let v=value(aa[i],bb[j]);
   br0[j]=Math.max(br0[j],v[0]);br1[i]=Math.max(br1[i],v[1])
  }
  let e=null,n=0;for(let i=0;i<aa.length;i++)for(let j=0;j<bb.length;j++){
   let v=value(aa[i],bb[j]);if(v[0]!==br0[j]||v[1]!==br1[i])continue;n++;
   if(!e||rule*(v[0]+v[1]-e.v[0]-e.v[1])>0||v[0]+v[1]===e.v[0]+e.v[1]&&v[0]>e.v[0])e={v,i,j}
  }
  if(!e)throw Error("no pure equilibrium "+id);
  for(let i=0;i<aa.length;i++){if(value(aa[i],bb[e.j])[0]>e.v[0])throw Error("dev0");dev++}
  for(let j=0;j<bb.length;j++){if(value(aa[e.i],bb[j])[1]>e.v[1])throw Error("dev1");dev++}
  for(const a of ga.all){if(value(a,bb[e.j])[0]>e.v[0])throw Error("unreduced dev0");fullDev++}
  for(const b of gb.all){if(value(aa[e.i],b)[1]>e.v[1])throw Error("unreduced dev1");fullDev++}
  let result={v:e.v,a:aa[e.i].a,b:bb[e.j].a,n};memo.set(id,result);return result
 }
`;
 patch(old,replacement);
 patch("dated,profiles,states:memo.size,deviations:dev","dated,profiles,states:memo.size,deviations:dev,fullDev,kernelPairs");
 return src;
}
const compact=x=>({name:x.name,status:x.status,rule:x.rule,wealth:x.wealth,wealth_numerator:x.wealth_numerator,wealth_denominator:x.wealth_denominator,reason:x.reason,profiles:x.profiles,states:x.states,deviations:x.deviations,fullDev:x.fullDev,kernelPairs:x.kernelPairs,dated:x.dated});
function makeStudy(base,wrapper){return new Function(acceleratedSource(base,wrapper)+"\nreturn windowStudy")()}
function runVariant(study,common,v){return study({...common,...v.opts}).results.map(compact)}

function reproduce(name){
 let base=fs.readFileSync(path.join(__dirname,"service_window.js"),"utf8"),w=fs.readFileSync(path.join(__dirname,"staggered_window.js"),"utf8");
 for(const [s,k] of [[base,"base_source_sha256"],[w,"staggered_source_sha256"]])if(crypto.createHash("sha256").update(s).digest("hex")!==expected[k])throw Error("input source changed "+k);
 let study=makeStudy(base,w),vv=expected.variants.filter(v=>!name||v.name===name);
 if(!vv.length)throw Error("unknown variant");
 return vv.map(v=>{let results=runVariant(study,expected.common,v);if(JSON.stringify(results)!==JSON.stringify(v.results))throw Error("mismatch "+v.name);return {...v,results}})
}
module.exports={reproduce};if(require.main===module)console.log(JSON.stringify(reproduce(process.argv[2]),null,2));
