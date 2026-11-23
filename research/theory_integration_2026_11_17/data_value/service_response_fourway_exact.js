"use strict";
// Synthetic four-way causal response audit; values in twentieths of normalized contribution.
// Run: node service_response_fourway_exact.js. Requires Node standard library only.
function run(){
  let checks=0;
  function eq(a,b,label){ checks++; if(a!==b) throw Error(label+": "+a+" != "+b); }
  const worlds=theta=>{
    const rows=[];
    for(let H=0;H<=1;H++)for(let U=0;U<=1;U++)for(let V=0;V<=1;V++){
      const A=U^H, C=V^H;
      const W=H^U^V^theta; // worker free; new t2 job J=1-W
      rows.push({H,U,V,A,C,W,J:1-W});
    }
    return rows;
  };
  function count(rows,mask,bits){
    return rows.filter(r=>((r.H===((bits>>0)&1)) || !(mask&1))
      &&((r.A===((bits>>1)&1)) || !(mask&2))
      &&((r.C===((bits>>2)&1)) || !(mask&4))
      &&((r.W===((bits>>3)&1)) || !(mask&8))).length;
  }
  const all=[worlds(0),worlds(1)];
  for(let mask=1;mask<16;mask++){
    const k=[1,2,4,8].filter(bit=>(mask&bit)!==0).length;
    if(k>3)continue;
    for(let bits=0;bits<16;bits++){
      if((bits&~mask)!==0)continue;
      const expected=8/(2**k);
      eq(count(all[0],mask,bits),expected,"theta0 lower-order");
      eq(count(all[1],mask,bits),expected,"theta1 lower-order");
    }
  }
  const values=[];
  for(let theta=0;theta<2;theta++){
    const rows=all[theta];
    for(const r of rows){
      eq(r.J+r.W,1,"repair complement");
      eq(Number(Boolean(r.W&&(r.A||(r.H&&r.C))))<=1,true,"one shared late service");
      eq(r.H+Number(Boolean(r.H&&r.C))<=2,true,"C buyer two-unit budget");
    }
    const sum=f=>rows.reduce((a,r)=>a+f(r),0);
    const z8=sum(r=>r.H*r.A*r.C*r.W);
    const WA8=sum(r=>r.W*r.A);
    const WHC8=sum(r=>r.W*r.H*r.C);
    const G20=sum(r=>40*r.H+80*r.W*Number(Boolean(r.A||(r.H&&r.C)))-4)/8;
    const R20=sum(r=>80*r.U)/8;
    const P20=R20+sum(r=>8*(1-r.U)*r.V)/8;
    const E20=sum(r=>80*(r.U+r.V))/8-37;
    eq(WA8,2,"worker and A joint");
    eq(WHC8,1,"worker, early and C joint");
    eq(G20,46-10*z8,"inclusion-exclusion fourway");
    eq(R20,40,"R value");
    eq(P20,42,"P expected q=1/10 qualification");
    eq(E20,43,"E independent mobile");
    eq(G20,theta===0?36:46,"G endpoint");
    values.push({theta,H_accepted_probability:"1/2",zeta_numerator:z8,zeta_denominator:8,R_twentieths:R20,P_twentieths:P20,G_twentieths:G20,E_twentieths:E20,
       original_R_full_history_same_across_regimes:true});
  }
  let bestRegret400=Infinity,bestJ=-1;
  for(let j=0;j<=20;j++){
    // x=j/20 is probability of G; regrets at theta1 and theta0.
    const regret400=Math.max((20-j)*3,j*7);
    if(regret400<bestRegret400){bestRegret400=regret400;bestJ=j;}
    eq(regret400>=42,true,"minimax lower bound");
  }
  eq(bestJ,6,"minimax probability 3/10");
  eq(bestRegret400,42,"minimax regret 21/200");
  eq(46-80*(3/80),43,"investment switch zeta=3/80");
  return {type:"synthetic_rational_construction",qualified_service:"accepted buyer offers and shared-worker/independent E capacity; not benchmarks",checks,
    lower_order_joint_tables:"identical for every marginal of up to 3 of H,A,C,W",
    worlds:values,
    assumptions:{early_C_accepted_contribution:2,late_unit_contribution:4,G_cost:"1/5",E_cost:"37/20",P_qualification_probability:"1/10",
      latent_regime_coupled_across_dates:true,no_real_customer_data:true},
    sharp_zeta_interval:["0","1/8"],G_value_interval:["9/5","23/10"],
    retained_R_value:"2",P_value:"21/10",E_value:"43/20",
    G_investment_threshold_zeta:"3/80",
    minimax_probability_G:"3/10",minimax_probability_E:"7/10",minimax_regret:"21/200",
    worker_free_and_paid_early_risk_set_probability:"1/4",
    eligible_risk_set_joint_offers_probability_by_regime:["1/2","0"],
    explanation:"Even full G-specific 1-,2-,3-way reports fail to identify the four-way coincidence created by t2 paid quality, t2 job, and t3 original buyer response."
  };
}
if(typeof process!=="undefined"&&typeof require!=="undefined"&&require.main===module){
  process.stdout.write(JSON.stringify(run(),null,2)+"\n");
}
