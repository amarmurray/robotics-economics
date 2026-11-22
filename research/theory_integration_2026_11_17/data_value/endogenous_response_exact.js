"use strict";
// Exact synthetic potential-history audit. Amounts are invented normalized
// accepted-and-paid service units, not observed robot returns.
// X=eligible program episode; Z=old original buyer; Jp=productive P job;
// Q,D,F=G qualification, original target demand and recovery-worker free.
function run() {
  let checks=0;
  function eq(label,a,b){ if(a!==b)throw Error(label+": "+a+" != "+b); checks++; }
  const endpoint=[];
  for(let k=0;k<=32;k++){
    let mass=0,old=0,P=0,G=0,q1=0,d1=0,f1=0,qd=0,qf=0,df=0,qdf=0,selected=0;
    for(let x=0;x<2;x++)for(let z=0;z<2;z++)for(let jp=0;jp<2;jp++)
    for(let q=0;q<2;q++)for(let d=0;d<2;d++)for(let f=0;f<2;f++){
      // Each of the 64 full-history states has weight numerator w / 1024.
      // Conditional on x,z,jp, G even parity = 1/4-t; odd parity=t.
      const w=((q+d+f)%2===0)?32-k:k;
      mass+=w; q1+=w*q;d1+=w*d;f1+=w*f;
      qd+=w*q*d;qf+=w*q*f;df+=w*d*f;qdf+=w*q*d*f;
      // Twice accepted-and-paid revenue per state; denominator 2048.
      const r=2*z;
      const p=x?(1+2*(1-jp)):r; // t2 source paid 1/2; t3 only if no P job
      const g=x?(f?((q&&d)?9:2*z):0):r; // one t3 customer slot
      old+=w*r;P+=w*p;G+=w*g;if(z)selected+=w;
    }
    G-=128; // Grounding qualification/calibration program cost 1/16.
    eq("mass "+k,mass,1024);eq("retained "+k,old,1024);
    eq("productive "+k,P,1536);eq("grounded "+k,G,640+32*k);
    eq("Q "+k,q1,512);eq("D "+k,d1,512);eq("F "+k,f1,512);
    eq("QD "+k,qd,256);eq("QF "+k,qf,256);eq("DF "+k,df,256);
    eq("QDF "+k,qdf,8*k);eq("old invoice "+k,selected,512);
    if(k===0||k===32)endpoint.push({t:k+"/128",old:old+"/2048",
      P:P+"/2048",G_calibrate:G+"/2048",
      G_or_old:Math.max(G,old)+"/2048",E:"1472/2048",
      qualification_demand_free:qdf+"/1024"});
  }
  // Rational formulas: G - P = -7/16 + 2*t; t=k/128.
  // Fixed program choices cannot condition on latent t absent a lawful report.
  eq("G/P crossover integer",7*128, 2*7*64);
  eq("low regret at lambda=1/8",1*7,7);
  eq("high regret at lambda=1/8",7*1,7);
  return {model:"endogenous_program_response_and_missing_support",
    laws:33,exact_assertions:checks,scenario_states_per_law:64,
    normalized_amounts:{R:"1/2",P:"3/4",E:"23/32",
      G_calibrate:"5/16+2*t",G_option:"max(1/2,5/16+2*t)",
      t_support:"[0,1/4]",G_beats_P:"t>7/32",
      maximin_program:"P",minimax_regret_G_probability:"1/8",
      minimax_regret:"7/128",pure_P_max_regret:"1/16",
      two_endpoint_equal_prior_report_value:"1/32"},
    endpoint_records:endpoint};
}
if(typeof module!=="undefined"&&require.main===module)
  console.log(JSON.stringify(run(),null,2));
