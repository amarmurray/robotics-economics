// CPU-only exact rational benchmark and independent labeled-menu/cash replay.
// Run: node pooled_recursion.js > pooled_recursion_results.json
function experiment(){
 const rat=(n,d)=>{let a=n<0n?-n:n,b=d;while(b){let r=a%b;a=b;b=r}return `${n/a}/${d/a}`};
 const num=(n,d)=>Number(n)/Number(d);
 function run(c,cap,rule){
  const {n,H,C,A,T,coord,sat}=c, maxCost=2*H+C+11, B0=T*maxCost;
  if(A<2*n)throw Error("negative receipt bound");
  if(sat&&!(A>3*n-1+4&&H>=2*n+1&&C>=2*n+3&&coord===0))throw Error("saturation premise");
  const menuCache=new Map(), memo=new Map();let profiles=0,checks=0,labelChecks=0;
  function menu(k,p,h){
   const id=[k,p,h>1].join();if(menuCache.has(id))return menuCache.get(id);
   const rs=[["none",0,0,0,0,0]];
   if(h>1){
    for(let m=0;m<=p;m++){
     if(k<n)rs.push(["train",2+m,1,2,0,m],["contract_train",2+m,1,0,5,m]);
     if(p<cap)rs.push(["develop",2+m,1,3,0,m],["contract_develop",2+m,1,0,6,m]);
    }
    if(p<cap)rs.push(["license",4,1,0,10,0]);
   }
   const out=[];
   for(const r of rs){
    const best=new Map();
    for(let v=0;v<=k;v++)for(let u=0;u<=n-v;u++)for(let l=0;l<=n-v-u;l++){
     const q=v+u+l,hh=2*l+u+r[2],cc=2*v+3*u+coord*(v+u)*(v+u-1)/2+r[3];
     if(hh>H||cc>C)continue;
     const cost=2*hh+cc+r[4]+1;
     if(!best.has(q)||best.get(q).cost>cost)best.set(q,{q,cost,r,v,u,l,hh,cc});
    }
    // Independent labeled service enumeration: skip, human, old, qualified.
    // Every distinct cheapest cost at each quantity/research option must agree.
    if(!sat){
     const alt=new Map();
     function walk(j,q,hh,cc,copy){
      if(j===n){cc+=coord*copy*(copy-1)/2;if(hh<=H&&cc<=C){let v=2*hh+cc+r[4]+1;if(!alt.has(q)||v<alt.get(q))alt.set(q,v)}return}
      walk(j+1,q,hh,cc,copy);walk(j+1,q+1,hh+2,cc,copy);
      walk(j+1,q+1,hh+1,cc+3,copy+1);if(j<k)walk(j+1,q+1,hh,cc+2,copy+1);
     }
     walk(0,0,r[2],r[3],0);
     if(alt.size!==best.size||[...alt].some(([q,v])=>best.get(q)?.cost!==v))throw Error("labeled menu disagreement");
     labelChecks++;
    }else{
     if(best.get(n)?.cost!==4*(n-k)+2*k+2*r[2]+r[3]+r[4]+1)throw Error("saturated cost identity");
     labelChecks++;
    }
    for(const a of best.values())if(!sat||a.q===n)out.push(a);
   }
   menuCache.set(id,out);return out;
  }
  function next(k,p,r){
   if(!r[1])return [[k,p,4]];
   const x=r[0].includes("train")?[k+1,p]:[k,p+1];
   return [[k,p,4-r[1]],[...x,r[1]]].filter(z=>z[2]);
  }
  const D=sat?4n:16n, powers=Array.from({length:T+1},(_,i)=>D**BigInt(i));
  function V(k,p,l,z,h){
   if(!h)return {v:sat?[0n]:[0n,0n]};
   const id=[k,p,l,z,h].join();if(memo.has(id))return memo.get(id);
   const aa=menu(k,p,h),bb=sat?[null]:menu(l,z,h),S=powers[h];
   const br0=bb.map(()=>null),br1=aa.map(()=>null);
   const mat=aa.map((a,i)=>bb.map((b,j)=>{
    profiles++;
    const price=A-a.q-(sat?n:b.q),v=sat?[BigInt(a.q*price-a.cost)*S]:[BigInt(a.q*price-a.cost)*S,BigInt(b.q*price-b.cost)*S];
    if(h>1)for(const x of next(k,p,a.r))for(const y of sat?[[0,0,1]]:next(l,z,b.r)){
     const w=V(x[0],x[1],y[0],y[1],h-1).v;
     for(let f=0;f<v.length;f++)v[f]+=BigInt(x[2]*y[2])*w[f];
    }
    if(br0[j]===null||v[0]>br0[j])br0[j]=v[0];
    if(!sat&&(br1[i]===null||v[1]>br1[i]))br1[i]=v[1];
    return v;
   }));
   let e=null,eq=0;
   for(let i=0;i<aa.length;i++)for(let j=0;j<bb.length;j++){
    const v=mat[i][j];if(v[0]!==br0[j]||(!sat&&v[1]!==br1[i]))continue;
    eq++;const total=v.reduce((a,b)=>a+b,0n),old=e?.v.reduce((a,b)=>a+b,0n);
    if(!e||BigInt(rule)*(total-old)>0n||(total===old&&v[0]>e.v[0]))e={v,i,j};
   }
   if(!e)throw Error("no pure equilibrium "+id);
   // Explicit unilateral-deviation certificate over the complete reduced menu.
   for(let i=0;i<aa.length;i++){if(mat[i][e.j][0]>e.v[0])throw Error("deviation 0");checks++}
   if(!sat)for(let j=0;j<bb.length;j++){if(mat[e.i][j][1]>e.v[1])throw Error("deviation 1");checks++}
   const out={v:e.v,a:aa[e.i],b:bb[e.j],eq};memo.set(id,out);return out;
  }
  try{
   const root=V(0,0,0,0,T);
   let dist=new Map([["0,0,0,0",1n]]), rows=[], cash=[0n,0n];
   const metrics=["q0","q1","revenue0","revenue1","outlay0","outlay1","human0","human1","compute0","compute1","develop0","develop1","contract_develop0","contract_develop1","license0","license1","train0","train1","psi2_0","psi2_1","qualified0","qualified1","cs_twice"];
   for(let t=0;t<T;t++){
    const h=T-t,den=powers[t],acc=Object.fromEntries(metrics.map(k=>[k,0n])), nd=new Map();
    function put(k,v,w){acc[k]+=BigInt(v)*w}
    for(const [s,w] of dist){
     const [k,p,l,z]=s.split(",").map(Number),e=memo.get([k,p,l,z,h].join()),aa=[e.a,sat?e.a:e.b],price=A-aa[0].q-aa[1].q;
     for(let i=0;i<2;i++){
      const a=aa[i],r=a.r[0];
      put("q"+i,a.q,w);put("revenue"+i,a.q*price,w);put("outlay"+i,a.cost,w);
      put("human"+i,a.hh,w);put("compute"+i,a.cc,w);
      for(const kind of ["develop","contract_develop","license"])put(kind+i,+(r===kind),w);
      put("train"+i,+r.includes("train"),w);
      put("psi2_"+i,+((i===0||sat?p:z)===2),w);put("qualified"+i,i===0||sat?k:l,w);
     }
     put("cs_twice",(aa[0].q+aa[1].q)**2,w);
     // Independently replay four equiprobable uniforms per firm; no next() call.
     for(let u=0;u<4;u++)for(let v=0;v<(sat?1:4);v++){
      let x=[k,p,l,z];
      for(let i=0;i<(sat?1:2);i++){const r=aa[i].r;if((i===0?u:v)<r[1])x[2*i+(r[0].includes("train")?0:1)]++}
      const key=x.join();nd.set(key,(nd.get(key)||0n)+w);
     }
    }
    if([...nd.values()].reduce((a,b)=>a+b,0n)!==powers[t+1])throw Error("mass");
    for(let i=0;i<2;i++)cash[i]+=(acc["revenue"+i]-acc["outlay"+i])*powers[T-t];
    rows.push({date:t+1,...Object.fromEntries(metrics.map(k=>[k,num(acc[k],den)])),cs:num(acc.cs_twice,2n*den)});
    dist=nd;
   }
   for(let i=0;i<2;i++)if(cash[i]!==root.v[sat?0:i])throw Error("independent cash replay");
   const terminal=[0n,0n];
   for(const [key,w] of dist){let x=key.split(",").map(Number);terminal[0]+=BigInt(x[1]===2)*w;terminal[1]+=BigInt((sat?x[1]:x[3])===2)*w}
   const sum={};for(const k of metrics.concat(["cs"]))sum[k]=rows.reduce((s,r)=>s+r[k],0);
   return {status:"solved",cap,rule:sat?"both: separable saturated equilibrium":rule===1?"highest total then firm 0":"lowest total then firm 0",B0,values_exact:cash.map(x=>rat(x,powers[T])),values:cash.map(x=>num(x,powers[T])),root:[root.a,sat?root.a:root.b],root_equilibria:root.eq,states:memo.size,profiles,deviation_checks:checks,menu_checks:labelChecks,terminal_psi2_probability:terminal.map(x=>num(x,powers[T])),totals:sum,dated:rows};
  }catch(e){return {status:"open",cap,rule,reason:String(e),states:memo.size,profiles,menu_checks:labelChecks}}
 }
 const cases=[
  {name:"active_shared_coordination",n:4,H:8,C:14,A:14,T:8,coord:1,sat:false},
  {name:"active_low_coordination",n:6,H:12,C:16,A:22,T:12,coord:0,sat:false},
  {name:"saturated_eight_targets",n:8,H:17,C:19,A:28,T:16,coord:0,sat:true},
  {name:"saturated_twelve_targets",n:12,H:25,C:27,A:40,T:20,coord:0,sat:true}
 ];
 return {synthetic:true,units:"cash ticks, accepted jobs, human slots, compute slots",cases:cases.map(c=>({parameters:c,results:[0,1,2].flatMap(cap=>(c.sat?[1]:[1,-1]).map(rule=>run(c,cap,rule)))}))};
}
console.log(JSON.stringify(experiment(),null,2));
