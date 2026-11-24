"use strict";
function run(){
 const N=12;let checks=0,worlds=0;const ck=(b,m)=>{checks++;if(!b)throw Error(m)};
 const values=(a,b,j)=>[5*N,5*N+4*a,5*N+4*b,5*N+4*j];
 const opt=(a,b,j)=>Math.max(6*N,...values(a,b,j));
 const env=[];for(let k=0;k<=2*N;k++){let best=6*N,forced=6*N;
 for(let a=0;a<=N;a++)for(let b=0;b<=N;b++)for(let j=0;j<=N;j++){
 if(2*a>k||2*b>k||j>k)continue;worlds++;
 const v=opt(a,b,j);
 ck(v<=Math.max(6*N,5*N+6*k),"typed potential bound");
 ck(v<=Math.max(6*N,5*N+4*k),"batch potential bound");
 best=Math.max(best,v);
 if(j===0){ck(v<=Math.max(6*N,5*N+2*k),"forced and uniform growth bound");forced=Math.max(forced,v);}
 if(k<=4)ck(v<7.5*N,"E strictly better under cap");
 }
 ck(best===Math.max(6*N,5*N+4*Math.min(N,k)),"sharp batch bound");
 ck(forced===Math.max(6*N,5*N+4*Math.min(N,Math.floor(k/2))),"grid-sharp forced bound");
 env.push({c:k/N,typed_upper:Math.max(6,5+6*k/N),batch_exact:best/N,forced_exact:forced/N});
 }
 ck(opt(0,0,0)===6*N&&opt(N,0,0)===9*N,"observational rank reversal");
 ck(values(0,0,0)[3]===values(N,0,0)[3],"forced histories have same payoff");
 ck(opt(N/2,0,0)===7*N&&Math.max(6*N,values(N/2,0,0)[1]+N)===8*N,"free matching routine flips");
 ck(Math.max(6*N,7.5*N-2*N)===6*N,"shared staff embodiment");
 // verify generation-potential inequalities in a two-type, discounted example:
 // beta=1/2, A produces two B, B produces one A, both earn 1.
 // w_A=4, w_B=3: 1+(1/2)*2*3=4; 1+(1/2)*4=3.
 ck(4===1+3&&3===1+4/2,"two-type discounted reproduction potential");
 // resource cap: sum of discounted positive per-period payoff ≤ k/(1-beta)
 ck(2/(1-0.5)===4,"independent physical cap");
 return {synthetic:true,ticks_per_unit:N,assertions:checks,compatible_cap_law_cases:worlds,cap_envelopes:env,low_G:6,high_G:9,forced_committed_G:5,independent_E:7.5,typed_upper_at_one_third:7,batch_upper_at_one_third:19/3,forced_plus_uniform_upper_at_one_third:6,free_routine_intermediate:8,shared_staff_E:6,discounted_two_type_potential:[4,3]};
}
console.log(JSON.stringify(run(),null,2));
