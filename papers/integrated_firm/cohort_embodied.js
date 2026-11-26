// CPU-only exact public-state game. Run: node cohort_embodied.js
function cohortStudy(){
 const H=3,C=5,A=[18,14,14],parts=[1,2],Cbar=24,pow=h=>16**h;
 const capCash=h=>h?12+(h-1)*Cbar:0;
 const swap=m=>(m&1)|((m&2)<<1)|((m&4)>>1),pop=m=>+(!!(m&1))+(!!(m&2))+(!!(m&4));
 const cases=[
  {name:"overlap_two_dates",T:2,B:80,K:[0,0,1,1],M:[2,2],P:0,cap:0},
  {name:"split_two_dates",T:2,B:80,K:[0,0,1,1],M:[2,4],P:0,cap:0},
  {name:"binding_overlap",T:2,B:7,K:[0,0,1,1],M:[2,2],P:0,cap:0},
  {name:"binding_split",T:2,B:7,K:[0,0,1,1],M:[2,4],P:0,cap:0},
  ...[0,1,2].map(cap=>({name:"four_dates_cap"+cap,T:4,B:120,K:[0,0,0,0],M:[0,0],P:0,cap})),
  ...[1,2].map(cap=>({name:"inherited_three_dates_cap"+cap,T:3,B:80,K:[0,0,1,1],M:[0,0],P:1,cap}))
 ];
 const budget=1800000;
 function solve(c,rule,quotient=true){
  let memo=new Map(),mc=new Map(),profiles=0,dev=0;
  const S=c.M.map(m=>[...c.K,m,c.P,c.B]),sal=s=>s[0]+2*s[1];
  function canon(s,z,h){
   let a=s.slice(),b=z.slice();
   if(quotient){
    a[6]=Math.min(a[6],capCash(h));b[6]=Math.min(b[6],capCash(h));
    let x=swap(a[4]),y=swap(b[4]);if(x<a[4]||x===a[4]&&y<b[4]){a[4]=x;b[4]=y}
   }return [a,b];
  }
  function menu(s,h){
   const key=[h,...s].join();if(mc.has(key))return mc.get(key);
   let [ka,kb,ia,ib,m,p,B]=s,rs=[["none",0,0,0,0,-1]],bs=[["none",0,0,0,-1,0]];
   if(h>1)for(let old=0;old<=p;old++){
    for(let j=0;j<3;j++)if(!(m&(1<<j)))rs.push(["train",1,2,0,2+old,j],["contract",1,0,5,2+old,j]);
    if(p<c.cap)rs.push(["develop",1,3,0,2+old,3],["contract_develop",1,0,6,2+old,3]);
   }
   if(h>1&&p<c.cap)rs.push(["license",1,0,10,4,3]);
   if(h>1)for(let j=0;j<2;j++)if(!s[j]){if(s[j+2])bs.push(["assemble",1,1,0,j,1]);else if(h>2)bs.push(["order",0,0,parts[j],j,0])}
   let out=new Map();
   for(let pr=0;pr<4;pr++){
    if(pr===2&&!ka||pr===3&&!kb)continue;
    for(let d1=0;d1<3;d1++)for(let d2=0;d2<3;d2++){
     let modes=[pr,d1,d2],q=(pr?1:0)|(d1?2:0)|(d2?4:0);
     let auto=(pr>=2?1:0)|(d1===2?2:0)|(d2===2?4:0),copies=pop(auto);
     for(let use=0;use<8;use++){
      if(use&~(m&auto))continue;
      let human=[0,3,2- +(!!(use&1)),1- +(!!(use&1))][pr]+(d1===1?2:d1===2?1- +(!!(use&2)):0)+(d2===1?2:d2===2?1- +(!!(use&4)):0);
      let compute=copies+copies*(copies-1)/2+2*copies-pop(use);
      for(const r of rs)for(const b of bs){
       let hh=human+r[1]+b[1],cc=compute+r[2]+b[2],cost=2*hh+cc+r[3]+b[3]+1;
       if(hh>H||cc>C||cost>B)continue;
       if(cost>(h===1?12:Cbar))throw Error("cash bound");
       let a={q,modes,use,copies,hh,cc,cost,r,b};
       // Only discard higher costs when next cash provably cannot affect continuation.
       // The labeled check retains all distinct cost levels, even when fully funded.
       let id=[q,r[4],r[5],b[4],b[5],quotient&&(h===1||B>=capCash(h))?0:cost].join();
       if(!out.has(id)||out.get(id).cost>cost)out.set(id,a);
      }
     }
    }
   }
   if(B===0)out.set("idle",{q:0,modes:[0,0,0],use:0,copies:0,hh:0,cc:0,cost:0,r:rs[0],b:bs[0]});
   let v=[...out.values()];if(!v.length)throw Error("empty menu");mc.set(key,v);return v;
  }
  function rev(a,b){let x=0;for(let j=0;j<3;j++)if(a.q&(1<<j))x+=A[j]-2-2* +(!!(b.q&(1<<j)));return x}
  function next(s,a,R){
   let z=s.slice();z[6]+=R-a.cost;let j=a.b[4];
   if(j>=0){if(a.b[5]){z[j]=1;z[j+2]=0}else z[j+2]=1}
   let w=z.slice(),k=a.r[5];if(k===3)w[5]++;else if(k>=0)w[4]|=1<<k;
   return a.r[4]===0?[[z,4]]:a.r[4]===4?[[w,4]]:[[z,4-a.r[4]],[w,a.r[4]]];
  }
  function V(s,z,h){
   if(!h)return {v:[sal(s),sal(z)]};
   [s,z]=canon(s,z,h);let id=[h,...s,...z].join();if(memo.has(id))return memo.get(id);
   let aa=menu(s,h),bb=menu(z,h),br0=bb.map(()=>-Infinity),br1=aa.map(()=>-Infinity),mat=[];
   const scale=pow(h),ta=new Map(),tb=new Map();
   for(let i=0;i<aa.length;i++){let a=aa[i],row=[];for(let j=0;j<bb.length;j++){
    if(++profiles>budget)throw Error("profile budget");
    let b=bb[j],R=rev(a,b),Z=rev(b,a),v=[scale*(R-a.cost),scale*(Z-b.cost)];
    if(h===1){v[0]+=scale*sal(s);v[1]+=scale*sal(z)}
    else{
     let k=i+","+b.q,l=j+","+a.q;
     if(!ta.has(k))ta.set(k,next(s,a,R));if(!tb.has(l))tb.set(l,next(z,b,Z));
     for(let [x,w] of ta.get(k))for(let [y,u] of tb.get(l)){let t=V(x,y,h-1).v;v[0]+=w*u*t[0];v[1]+=w*u*t[1]}
    }
    if(!v.every(Number.isSafeInteger))throw Error("nonexact integer");
    if(v[0]>br0[j])br0[j]=v[0];if(v[1]>br1[i])br1[i]=v[1];row.push(v);
   }mat.push(row)}
   let e=null,n=0;
   for(let i=0;i<aa.length;i++)for(let j=0;j<bb.length;j++){let v=mat[i][j];if(v[0]!==br0[j]||v[1]!==br1[i])continue;n++;if(!e||rule*(v[0]+v[1]-e.v[0]-e.v[1])>0||v[0]+v[1]===e.v[0]+e.v[1]&&v[0]>e.v[0])e={v,i,j}}
   if(!e)throw Error("no pure equilibrium at "+id);
   for(let i=0;i<aa.length;i++){if(mat[i][e.j][0]>e.v[0])throw Error("dev0");dev++}
   for(let j=0;j<bb.length;j++){if(mat[e.i][j][1]>e.v[1])throw Error("dev1");dev++}
   let r={v:e.v,a:aa[e.i],b:bb[e.j],n};memo.set(id,r);return r;
  }
  try{
   let root=V(...S,c.T),dist=new Map([[S.flat().join(),1]]),dated=[];
   for(let t=0;t<c.T;t++){
    let h=c.T-t,nd=new Map(),row={date:t+1,jobs:0,customer_surplus:0,train:0,successor:0,orders:0,assembly:0,cash0:0,cash1:0,net0:0,net1:0};
    for(let [k,w] of dist){
     let x=k.split(",").map(Number),ss=[x.slice(0,7),x.slice(7)];
     let cs=canon(...ss,h),flipped=cs[0][4]!==ss[0][4]||cs[1][4]!==ss[1][4];
     let e=memo.get([h,...cs.flat()].join()),as=[e.a,e.b].map(a=>{
      if(!flipped)return a;
      let r=a.r.slice();if(r[5]===1||r[5]===2)r[5]=3-r[5];
      return {...a,q:swap(a.q),use:swap(a.use),modes:[a.modes[0],a.modes[2],a.modes[1]],r};
     });
     let wt=w/pow(t),R=as.map((a,i)=>rev(a,as[1-i]));
     for(let i=0;i<2;i++){
      let a=as[i],s=ss[i],[pr,d1,d2]=a.modes,auto=(pr>=2?1:0)|(d1===2?2:0)|(d2===2?4:0);
      let hh=[0,3,2- +(!!(a.use&1)),1- +(!!(a.use&1))][pr]+[0,2,1- +(!!(a.use&2))][d1]+[0,2,1- +(!!(a.use&4))][d2]+a.r[1]+a.b[1];
      let n=pop(auto),cc=n*(n+1)/2+2*n-pop(a.use)+a.r[2]+a.b[2];
      let cost=s[6]===0?0:2*hh+cc+a.r[3]+a.b[3]+1;
      if(cost!==a.cost||hh!==a.hh||cc!==a.cc||cost>s[6]||hh>H||cc>C||a.use&~(s[4]&auto)||pr>=2&&!s[pr-2])throw Error("ledger infeasible");
      if(a.r[5]>=0&&a.r[5]<3&&(s[4]&(1<<a.r[5])))throw Error("already qualified");
      row.jobs+=wt*pop(a.q);row.train+=wt* +(a.r[5]>=0&&a.r[5]<3);row.successor+=wt* +(a.r[5]===3);row.orders+=wt* +(a.b[0]==="order");row.assembly+=wt* +(a.b[0]==="assemble");row["cash"+i]+=wt*s[6];row["net"+i]+=wt*(R[i]-cost);
     }
     for(let j=0;j<3;j++){let Q=+(!!(as[0].q&(1<<j)))+ +(!!(as[1].q&(1<<j)));row.customer_surplus+=wt*Q*Q}
     for(let u=0;u<4;u++)for(let v=0;v<4;v++){
      let y=ss.map((s,i)=>{let a=as[i],z=s.slice(),j=a.b[4];z[6]+=R[i]-a.cost;if(j>=0){if(a.b[5]){if(!s[j+2]||s[j])throw Error("kit ledger");z[j]=1;z[j+2]=0}else{if(s[j+2]||s[j])throw Error("order ledger");z[j+2]=1}}
       if((i? v:u)<a.r[4]){if(a.r[5]===3)z[5]++;else z[4]|=1<<a.r[5]}return z}).flat().join();
      nd.set(y,(nd.get(y)||0)+w);
     }
    }
    if([...nd.values()].reduce((a,b)=>a+b,0)!==pow(t+1))throw Error("mass");
    dist=nd;dated.push(row);
   }
   let wealth=[0,0],cash=[0,0],salvage=[0,0],p2=[0,0];
   for(let [k,w] of dist){let x=k.split(",").map(Number);for(let i=0;i<2;i++){let s=x.slice(i*7,i*7+7);wealth[i]+=w*(s[6]+sal(s));cash[i]+=w*s[6];salvage[i]+=w*sal(s);p2[i]+=w* +(s[5]===2)}}
   let den=pow(c.T);for(let i=0;i<2;i++){if(wealth[i]!==root.v[i]+c.B*den||cash[i]/den!==c.B+dated.reduce((a,r)=>a+r["net"+i],0))throw Error("cash replay")}
   return {status:"solved",rule,quotient,wealth:wealth.map(x=>x/den),new_cash:cash.map(x=>x/den-c.B),salvage:salvage.map(x=>x/den),p2:p2.map(x=>x/den),root:[root.a,root.b],root_equilibria:root.n,profiles,states:memo.size,deviations:dev,dated};
  }catch(e){return {status:"open",rule,quotient,reason:String(e),profiles,states:memo.size}}
 }
 let results=cases.map(c=>({parameters:c,results:[1,-1].map(r=>solve(c,r))}));
 let checks=[];
 for(const c of cases.slice(0,4))for(let r of [1,-1]){
  let a=results.find(x=>x.parameters.name===c.name).results.find(x=>x.rule===r),b=solve(c,r,false);
  if(a.status!=="solved"||b.status!=="solved"||a.wealth.some((x,i)=>x!==b.wealth[i]))throw Error("labeled uncapped value check "+c.name+" "+r+" "+JSON.stringify([a,b]));
  checks.push({case:c.name,rule:r,quotient_profiles:a.profiles,labeled_uncapped_profiles:b.profiles,wealth:a.wealth});
 }
 return {synthetic:true,description:"One physical site and two distinct exchangeable digital sites; exact capped-cash and joint permutation quotient with binary local qualification. No scope or archive changes.",Cbar,terminal_cost_bound:12,profile_budget:budget,results,labeled_value_checks:checks};
}
console.log(JSON.stringify(cohortStudy(),null,2));
