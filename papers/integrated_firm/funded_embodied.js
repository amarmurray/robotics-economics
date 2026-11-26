// Funded cash quotient of embodied_game.js; see FUNDED_EMBODIED.md.
// CPU-only exact integer-scaled public-state game. Run: node funded_embodied.js
function embodied(){
 const cases=[0,1,2].map(cap=>({name:"funded_four_date_cap"+cap,T:4,H:3,C:4,A:[18,14],B:120,K:[0,0],I:[0,0],m:[0,0],p:0,cap,parts:[1,2]}));
 function solve(c,manufacture,rule){
 const S0=[...c.K,...c.I,...c.m,c.p,c.B],{T,H,C,A,cap}=c;
 // All histories are funded, even if no receipts arrive. Prices are nonnegative.
 if(A.some(a=>a<4)||c.B<T*(2*H+C+10+Math.max(...c.parts)+1))throw Error('funding bound');
 const pow=Array.from({length:T+1},(_,i)=>16**i);
 const mc=new Map(), memo=new Map();let profiles=0,checks=0,menuChecks=0;
 const salvage=s=>s[0]+2*s[1];
 // stock order: installed arm/mobile, kits arm/mobile, model physical/digital, procedure, cash.
 function menu(s,h){
  const id=[h,...s].join();if(mc.has(id))return mc.get(id);
  const [ka,kb,ia,ib,mp,md,p,B]=s;
  let rs=[["none",0,0,0,0,-1]];
  if(h>1)for(let m=0;m<=p;m++){
   for(let j=0;j<2;j++)if(s[4+j]<2){
    rs.push(["train"+j,1,2,0,2+m,4+j],["contract"+j,1,0,5,2+m,4+j]);
   }
   if(p<cap)rs.push(["develop",1,3,0,2+m,6],["contract_develop",1,0,6,2+m,6]);
  }
  if(h>1&&p<cap)rs.push(["license",1,0,10,4,6]);
  let bs=[["none",0,0,0,-1,0]];
  if(manufacture&&h>1)for(let j=0;j<2;j++)if(!s[j]){
   if(s[2+j])bs.push(["assemble"+j,1,1,0,j,1]);
   else if(h>2)bs.push(["order"+j,0,0,(c.parts||[6,8])[j],j,0]);
  }
  let out=new Map();
  for(let pr of [0,1,2,3]){ // 0 absent; 1 human; 2 arm; 3 mobile
   if(pr===2&&!ka||pr===3&&!kb)continue;
   for(let dg of [0,1,2]){ // absent, human, agent
    for(let ep=0;ep<=(pr>=2?mp:0);ep++)for(let ed=0;ed<=((pr>=2||dg===2)?md:0);ed++){
     let human=(pr===1?3:pr===2?Math.max(0,2-ep):pr===3?Math.max(0,1-ep):0)+(dg===1?2:dg===2?Math.max(0,1-ed):0);
     const auto=+(pr>=2)+ +(dg===2),copies=Math.ceil(auto/(1+ +(ed===2)));
     let compute=copies+copies*(copies-1)/2+(pr>=2?(ep===0?2:1):0)+(dg===2?(ed===0?2:1):0);
     for(const r of rs)for(const b of bs){
      const hh=human+r[1]+b[1],cc=compute+r[2]+b[2],cost=2*hh+cc+r[3]+b[3]+1;
      if(hh>H||cc>C||cost>B)continue;
      let a={q:[+(pr>0),+(dg>0)],pr,dg,ep,ed,copies,hh,cc,cost,r,b};
      const key=h===1?a.q.join():[...a.q,r[4],r[5],b[4],b[5]].join();
      if(!out.has(key)||out.get(key).cost>cost)out.set(key,a);
     }
    }
   }
  }
  // Insolvent idle is free lab suspension for the current date, not a changed scope.
  if(B===0)out.set("idle",{q:[0,0],pr:0,dg:0,ep:0,ed:0,copies:0,hh:0,cc:0,cost:0,r:rs[0],b:bs[0]});
  const result=[...out.values()];if(!result.length)throw Error("empty menu");
  mc.set(id,result);menuChecks++;return result;
 }
 function revenue(a,b){return a.q.reduce((v,q,j)=>v+q*(A[j]-2*(q+b.q[j])),0)}
 function next(s,a,rev){
  let x=s.slice();x[7]=c.B;
  if(a.b[4]>=0){let j=a.b[4];if(a.b[5]){x[j]++;x[2+j]--}else x[2+j]++}
  let r=a.r;if(!r[4])return [[x,4]];
  let y=x.slice();y[r[5]]++;
  return [[x,4-r[4]],[y,r[4]]].filter(z=>z[1]);
 }
 function V(s,z,h){
  const id=[h,...s,...z].join();if(memo.has(id))return memo.get(id);
  if(h===0)return {v:[salvage(s),salvage(z)]};
  const aa=menu(s,h),bb=menu(z,h),br0=bb.map(()=>-Infinity),br1=aa.map(()=>-Infinity);
  const mat=aa.map((a,i)=>bb.map((b,j)=>{
   if(++profiles>6000000)throw Error("profile budget");
   let rev=revenue(a,b),rev2=revenue(b,a),v=[0,0];
   if(h===1)v=[16*(rev-a.cost+salvage(s)),16*(rev2-b.cost+salvage(z))];
   else for(const [x,w] of next(s,a,rev))for(const [y,u] of next(z,b,rev2)){
    let k=V(x,y,h-1).v;v[0]+=w*u*k[0];v[1]+=w*u*k[1];
   }
   if(h>1){v[0]+=pow[h]*(rev-a.cost);v[1]+=pow[h]*(rev2-b.cost)}
   if(v[0]>br0[j])br0[j]=v[0];if(v[1]>br1[i])br1[i]=v[1];return v;
  }));
  let e=null,eq=0;
  for(let i=0;i<aa.length;i++)for(let j=0;j<bb.length;j++){
   const v=mat[i][j];if(v[0]!==br0[j]||v[1]!==br1[i])continue;eq++;
   if(!e||rule*(v[0]+v[1]-e.v[0]-e.v[1])>0||v[0]+v[1]===e.v[0]+e.v[1]&&v[0]>e.v[0])e={v,i,j};
  }
  if(!e)throw Error("no pure equilibrium "+id);
  for(let i=0;i<aa.length;i++){if(mat[i][e.j][0]>e.v[0])throw Error("deviation");checks++}
  for(let j=0;j<bb.length;j++){if(mat[e.i][j][1]>e.v[1])throw Error("deviation");checks++}
  let result={v:e.v,a:aa[e.i],b:bb[e.j],eq};memo.set(id,result);return result;
 }
 try{
  let root=V(S0,S0,T),dist=new Map([[S0.concat(S0).join(),1]]),rows=[];
  for(let t=0;t<T;t++){
   let h=T-t,den=pow[t],nd=new Map(),row={date:t+1};
   for(let [key,w] of dist){
    const state=key.split(",").map(Number),ss=[state.slice(0,8),state.slice(8)],e=memo.get([h,...ss.flatMap(s=>[...s.slice(0,7),c.B])].join()),as=[e.a,e.b];
    function put(k,v){row[k]=(row[k]||0)+w*v/den}
    for(let i=0;i<2;i++){
     let s=ss[i],a=as[i],b=as[1-i];
     // Independent ledger: recompute resources and cash from chosen recipe.
     let hh=[0,3,Math.max(0,2-a.ep),Math.max(0,1-a.ep)][a.pr]+[0,2,Math.max(0,1-a.ed)][a.dg]+a.r[1]+a.b[1];
     let cp=Math.ceil((+(a.pr>=2)+ +(a.dg===2))/(1+ +(a.ed===2)));
     let cc=cp+cp*(cp-1)/2+(a.pr>=2?2- +(a.ep>0):0)+(a.dg===2?2- +(a.ed>0):0)+a.r[2]+a.b[2];
     let cost=2*hh+cc+a.r[3]+a.b[3]+1;if(s[7]===0)cost=0;
     if(hh!==a.hh||cc!==a.cc||cost!==a.cost||cost>s[7]||hh>H||cc>C||a.pr>=2&&!s[a.pr-2])throw Error("resource ledger");
     put("physical"+i,a.q[0]);put("digital"+i,a.q[1]);put("revenue"+i,revenue(a,b));put("cost"+i,cost);put("cash_start"+i,s[7]);put("arm"+i,s[0]);put("mobile"+i,s[1]);put("arm_kit"+i,s[2]);put("mobile_kit"+i,s[3]);put("train"+i,+(a.r[5]>=4&&a.r[5]<=5));put("procedure"+i,s[6]);put("physical_model"+i,s[4]);put("digital_model"+i,s[5]);put("successor_attempt"+i,+(a.r[5]===6));
     for(let name of ["order0","order1","assemble0","assemble1"])put(name+"_"+i,+(a.b[0]===name));
    }
    for(let j=0;j<2;j++){let Q=as[0].q[j]+as[1].q[j];row["cs"+j]=(row["cs"+j]||0)+w*Q*Q/den}
    for(let u=0;u<4;u++)for(let v=0;v<4;v++){
     let x=ss.map((s,i)=>{
      let a=as[i],z=s.slice(),j=a.b[4];
      z[7]=s[7]+revenue(a,as[1-i])-a.cost;
      if(j>=0){if(a.b[5]){if(!s[2+j])throw Error("parts conservation");z[j]=1;z[2+j]=0}else z[2+j]=1}
      if((i===0?u:v)<a.r[4])z[a.r[5]]++;
      return z;
     }).flat().join();nd.set(x,(nd.get(x)||0)+w);
    }
   }
   if([...nd.values()].reduce((a,b)=>a+b,0)!==pow[t+1])throw Error("probability mass");
   dist=nd;rows.push(row);
  }
  let terminal=[0,0],cash=[0,0],sal=[0,0];
  for(let [key,w] of dist){let x=key.split(",").map(Number);for(let i=0;i<2;i++){let s=x.slice(8*i,8*i+8);cash[i]+=w*s[7];sal[i]+=w*salvage(s);terminal[i]+=w*(s[7]+salvage(s))}}
  if(terminal.some((v,i)=>v!==root.v[i]+c.B*pow[T]))throw Error("terminal replay");
  for(let i=0;i<2;i++){let replay=c.B+rows.reduce((v,r)=>v+r["revenue"+i]-r["cost"+i],0);if(replay!==cash[i]/pow[T])throw Error("cash replay")}
  return {status:"solved",manufacture,rule,wealth:terminal.map(v=>v/pow[T]),new_cash:cash.map(v=>v/pow[T]-c.B),salvage:sal.map(v=>v/pow[T]),exact:terminal.map(v=>v+"/"+pow[T]),root:[root.a,root.b],root_equilibria:root.eq,profiles,states:memo.size,deviation_checks:checks,menu_checks:menuChecks,dated:rows};
 }catch(e){return {status:"open",manufacture,rule,reason:String(e),profiles,states:memo.size}}
 }
 return {synthetic:true,units:"cash ticks, accepted jobs, human and compute slots, kit and installed machine counts",cases:cases.map(c=>({parameters:c,results:[true].flatMap(b=>[1,-1].map(rule=>solve(c,b,rule)))}))}
}
console.log(JSON.stringify(embodied(),null,2));
