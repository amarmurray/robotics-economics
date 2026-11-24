"use strict";
const run=function(){
  // All economic totals below are integer ticks, N ticks per unit.
  const N=16;let checks=0,worlds=0,flows=0;const ck=(ok,m)=>{checks++;if(!ok)throw Error(m)};
  const opt=(p,a,b)=>Math.max(5*N,5*N-N/2+p*a,5*N-N/2+p*b,4*N+p*(a+b));
  const rect=p=>5*N+Math.max(0,p-2)*N/2;
  const upper=(p,c)=>5*N+Math.max(0,p-2)*c;
  const profile=[];
  for(let c=0;c<=N/2;c++){
    let pure6=-Infinity,flow6=-Infinity;
    for(let p=0;p<=12;p++){
      let best=-Infinity,flowbest=-Infinity;
      for(let a=0;a<=N/4;a++)for(let b=0;b<=N/4;b++){
        if(a+b>c)continue;
        worlds++;
        for(let mask=0;mask<4;mask++){
          const i=mask&1,j=(mask>>1)&1,v=5*N-(i+j)*N/2+p*(i*a+j*b);
          ck(v<=upper(p,c),"common cap upper on every fixed policy");
          ck(v<=rect(p),"rectangular upper");
        }
        const v=opt(p,a,b);best=Math.max(best,v);
        ck(v<=upper(p,c),"optimized upper");
      }
      // Relaxed occupancy: x is probability mass of verification, y of joint paid success.
      for(let ya=0;ya<=N/4;ya++)for(let yb=0;yb<=N/4;yb++){
        if(ya+yb>c)continue;
        for(let xa=2*ya;xa<=N/2;xa++)for(let xb=2*yb;xb<=N/2;xb++){
          flows++;const v=5*N-xa-xb+p*(ya+yb);
          ck(v<=upper(p,c),"dual upper");
          flowbest=Math.max(flowbest,v);
        }
      }
      ck(flowbest===upper(p,c),"attained relaxed dual");
      if(c===0||c===4||c===8)ck(best===upper(p,c),"attained pure endpoint");
      if(p===6){pure6=best;flow6=flowbest;}
    }
    profile.push({cap:c/N,pure_optimum_envelope:pure6/N,flow_upper:flow6/N});
  }
  const low=opt(6,4,0),high=opt(6,4,4),E=6.5*N,R=6*N;
  ck(low===6*N&&high===7*N&&low<E&&high>E,"investment reversal");
  ck(rect(6)===7*N&&upper(6,4)===6*N,"coupling materially tightens");
  ck(opt(6,4,0)+N===7*N,"matching free routine");
  ck(Math.max(R,2.5*N)===R,"shared staff E declines");
  ck(profile[6].flow_upper===6.5&&profile[6].pure_optimum_envelope===6.25,"relaxation gap");
  ck(upper(6,5)<E&&upper(6,6)===E,"cap drift threshold");
  // fixed verify-both policy as lower, independent of which report class contains success
  for(let a=0;a<=4;a++)for(let b=0;b<=4;b++){
    const v=4*N+6*(a+b);if(a+b>=7)ck(v>E,"robust fixed rule lower");
  }
  return {synthetic:true,ticks_per_unit:N,assertions:checks,compatible_law_price_cases:worlds,relaxed_flow_cases:flows,cap_profile_at_p6:profile,rectangular_upper:7,coupled_cap_quarter_upper:6,high_world_G:7,independent_E:6.5,retained_R:6,free_routine_low_world:7,shared_staff_E:6,strict_cap_drift_limit:0.125};
};
console.log(JSON.stringify(run(),null,2));
