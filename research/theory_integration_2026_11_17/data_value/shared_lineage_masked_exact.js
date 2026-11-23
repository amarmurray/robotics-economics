"use strict";
const run = function run(){
 let checks=0;const ck=(b,m)=>{checks++;if(!b)throw Error(m)};
 const rows=[];
 for(let j=0;j<=8;j++){
  const a=[];for(let h=0;h<2;h++)for(let y=0;y<2;y++)for(let z=0;z<2;z++)a.push({h,y,z,n:(h+y+z)%2?j:8-j});
  const sum=f=>a.reduce((v,x)=>v+x.n*f(x),0);
  ck(sum(()=>1)===32,"release mass");
  for(const [u,v] of [["h","y"],["h","z"],["y","z"]])for(let x=0;x<2;x++)for(let w=0;w<2;w++)ck(sum(t=>+(t[u]===x&&t[v]===w))===8,"full pair law");
  const gain=(k,t)=>k===0?0:k===1?-3+12*t.y*t.z:-3+8*t.y*(1-t.z);
  const value=(k,l)=>768+sum(t=>gain(t.h?l:k,t));
  const v=[];for(let k=0;k<3;k++)for(let l=0;l<3;l++)v.push(value(k,l));
  ck(value(0,0)===768,"L/W baseline");
  ck(value(1,1)===768,"M alone");ck(value(2,2)===736,"N alone");
  ck(value(1,2)===832-20*j,"even policy");ck(value(2,1)===672+20*j,"odd policy");
  ck(Math.max(...v)===768+Math.max(0,48-12*j,-48+8*j)+Math.max(0,-48+12*j,16-8*j),"known-law optimal");
  for(let a0=0;a0<=4;a0++)for(let a1=0;a1<=4-a0;a1++)for(let b0=0;b0<=4;b0++)for(let b1=0;b1<=4-b0;b1++){
   const w0=[4-a0-a1,a0,a1],w1=[4-b0-b1,b0,b1];
   const lottery=v.reduce((u,x,i)=>u+w0[Math.floor(i/3)]*w1[i%3]*x,0);
   ck(lottery<=16*Math.max(...v),"feasible randomized policy cannot exceed known-law maximum");
   if(j===4)ck(lottery<=16*768,"common midpoint robust upper");
  }
  if(j<=1){ck(value(1,2)>=812,"direct audit lower");ck(value(1,2)>=808,"uniform feasible support bound");}
  // Difference of two schedules with one occupied slot: same coefficients cancel.
  for(let k=0;k<3;k++)for(let l=0;l<3;l++){
    const d0=[0,3,-3],d1=[0,-3,1];
    const actual0=[0,3*8-6*j,-3*8+4*j],actual1=[0,-3*8+6*j,8-4*j];
    for(const [d,act] of [[d0,actual0],[d1,actual1]]){
     const err=Math.abs((act[k]-act[l])-8*(d[k]-d[l]));
     const weights=[0,6*j,4*j]; const bound=k===l?0:weights[k]+weights[l];
     ck(err<=bound,"paired schedule error certificate");
    }
  }
  rows.push({j,denominator:128,all_L:value(0,0),all_M:value(1,1),all_N:value(2,2),even_policy:value(1,2),odd_policy:value(2,1),known_law_best:Math.max(...v),assumed_E:800});
 }
 ck(rows[0].even_policy>800&&rows[8].even_policy<800,"ranking reversal");
 ck(rows[4].known_law_best===768,"maximin upper attained by L");
 return {synthetic:true,units:"1/128",checks,rows,robust_G:768,retained_R:640,independent_E:800,free_P_L:896,shared_E_committed:544,audit_even_p_at_most_eighth:812,uniform_support_lower:808};
};
console.log(JSON.stringify(run(),null,2));
