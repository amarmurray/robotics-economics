// Reproducible CPU-only finite population audit; no external dependencies. No customer observations.
'use strict';
const run = function run(){
 let checks=0,cases=0;
 function eq(a,b,label){checks++;if(a!==b)throw Error(`${label}: ${a} != ${b}`)}
 function exhaustive(M,N,d){let xs=[];for(let x=0;x<=M;x++)for(let y=0;y<=N;y++)if(x+y===d)xs.push(x);return [Math.min(...xs),Math.max(...xs)]}
 for(let M=0;M<=8;M++)for(let N=0;N<=8-M;N++)for(let d=0;d<=M+N;d++){
  let b=exhaustive(M,N,d);eq(b[0],Math.max(0,d-N),"lower");eq(b[1],Math.min(d,M),"upper");cases++
 }
 const main=exhaustive(2,2,3),agg=exhaustive(2,2,2),stratA=exhaustive(2,0,1),stratB=exhaustive(0,2,1);
 eq(main[0],1,"main lower");eq(main[1],2,"main upper");
 eq(agg[0],0,"global lower");eq(agg[1],2,"global upper");
 eq(stratA[0]+stratB[0],1,"strat lower");eq(stratA[1]+stratB[1],1,"strat upper");
 const B0=[1,1,0,0,1,1,0,0],Q0=[0,0,0,0,1,1,1,1],Q1=[1,0,1,1,1,1,1,1],B1=[0,1,0,0,1,1,0,0];
 const t0=B0.reduce((x,v,i)=>x+v*Q0[i],0),t1=B1.reduce((x,v,i)=>x+v*Q1[i],0),retained=B0.reduce((x,v,i)=>x+v*Q1[i],0);
 eq(t0,2,"baseline paid");eq(retained,3,"stable demand paid");eq(t1,2,"drift paid");
 for(let i=0;i<8;i++){eq(Q1[i]>=Q0[i],true,"nested qualification")}
 const legalMenu6=6*4/8,legalMenu4=4*(6+1)/8;eq(Math.max(legalMenu6,legalMenu4),3.5,"menu-varying first choice");eq(Math.max(legalMenu6,4*(4+1)/8),3,"false shared first choice");
 return {enumerated_integer_baseline_gain_cases:cases,scoped_exact_assertions:checks,main:{denominator:8,M:2,N:2,d:3,incremental_paid_numerators:main,incremental_net_with_price4_cost_quarter:["1/4","3/4"]},strata:{aggregate_paid_gain_numerators:agg,predeclared_stratum_paid_gain_numerators:[1,1]},buyer_drift:{baseline_paid_numerator:t0,after_nested_upgrade_fixed_buyer:retained,after_one_buyer_flip:t1},menu_response:{correct_precommitted_menu_value:"7/2",wrong_shared_first_purchase_value:"3"}}
};
if(typeof module !== 'undefined' && require.main === module) process.stdout.write(JSON.stringify(run(),null,2)+'\n');
module.exports={run};
