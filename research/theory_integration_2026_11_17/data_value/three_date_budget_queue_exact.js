// Reproduce in Node: node three_date_budget_queue_exact.js
// Exact integer arithmetic; outcome values /20, regret /2000, report value /40.
// CONDITIONAL SYNTHETIC CONSTRUCTION; no measured robot-customer data.
const verify = function verify(){
  let checks=0;
  const eq=(a,b,label)=>{checks++;if(a!==b)throw new Error(`${label}: ${a} != ${b}`)};
  const ok=(a,label)=>{checks++;if(!a)throw new Error(label)};
  const rows=[];
  for(let k=0;k<=10;k++){
    // Joint original buyer latent t2 demand D, C under G, mass denominator 20.
    // (D,C)=(1,1),(1,0),(0,1),(0,0)
    const atoms=[k,10-k,10-k,k];
    const D=atoms[0]+atoms[1],C=atoms[0]+atoms[2];
    const g0=3*atoms[0]+2*atoms[1]+3*atoms[2];
    eq(atoms.reduce((a,b)=>a+b,0),20,`mass ${k}`);
    eq(D,10,`D marginal ${k}`);eq(C,10,`C marginal ${k}`);
    ok(atoms.every(n=>n>=0),`nonnegative ${k}`);
    eq(g0,50-2*k,`budget/one-slot G0 ${k}`);
    // P: source sale 4/5, field-data transfer Q_C=1, 1/5 two-shift incident, C demand 1/2;
    // G early: licensed target qualification, 1/2 two-shift incident, C demand 1/2;
    // E: independent t2 robot and worker, independent capacity cost 2/5.
    const p0=20,p1=16+3*8,g1=16+3*5,e0=2*D+3*10-8,e1=16+3*10-8;
    eq(p1,40,`P1 ${k}`);eq(g1,31,`G1 ${k}`);
    eq(e0,42,`E0 ${k}`);eq(e1,38,`E1 ${k}`);
    ok(p1>p0,`P chooses productive source ${k}`);
    ok(e0>e1,`E chooses budget-preserving late sales ${k}`);
    const gopt=Math.max(g0,g1);
    eq(gopt,k===10?31:g0,`grounding dispatch ${k}`);
    const best=Math.max(p1,e0,gopt);
    eq(best,Math.max(g0,e0),`full lawful oracle menu ${k}`);
    eq(Math.sign(g0-e0),Math.sign(4-k),`E/G ranking threshold ${k}`);
    // Two-unit repair workload after early service: one shift clears one, leaving a late block iff J=1.
    for(let j=0;j<=1;j++){
      const L2=Math.max(0,2*j-1);
      eq(L2,j,`conserved queue ${k}:${j}`);
      for(let early=0;early<=1;early++){
        const B2=1-early;
        ok(B2>=0 && B2<=1,`budget ${k}:${j}:${early}`);
        for(let d=0;d<=1;d++){
          const paidAnchorEarly=early;
          const paidAnchorLate=B2*d;
          ok(paidAnchorEarly+paidAnchorLate<=1,`one original buyer budget ${k}:${j}:${early}:${d}`);
        }
      }
    }
    rows.push({overlap_mass_over_20:k,G_skip_over_20:g0,G_serve_over_20:g1,P_over_20:p1,E_over_20:e0,optimal_over_20:best});
  }
  // All ex-ante mixtures of G-skip, G-serve and E on 1/100 grid;
  // compare each fixed policy to best arm in each world, never an ex-post G dispatch.
  let best=Infinity, winners=[];
  for(let ng0=0;ng0<=100;ng0++){
    for(let ng1=0;ng1+ng0<=100;ng1++){
      const ne=100-ng0-ng1;
      const badLow=5000-(ng0*50+ng1*31+ne*42);
      const badHigh=4200-(ng0*30+ng1*31+ne*42);
      const worst=Math.max(badLow,badHigh); // denominator 2000
      ok(badLow>=0 && badHigh>=0,`regret nonnegative ${ng0}:${ng1}`);
      if(worst<best){best=worst;winners=[[ng0,ng1,ne]]}
      else if(worst===best) winners.push([ng0,ng1,ne]);
    }
  }
  eq(best,480,"minimax regret numerator over 2000");
  eq(winners.length,1,"unique grid optimizer");
  eq(winners[0].join(","),"40,0,60","optimal G-skip/E mixture");
  const reports=[];
  for(let h=10;h<=20;h++){
    // accuracy h/20 for symmetric binary early G-regime report, prior 1/2.
    const favorableG=30+h,unfavorableG=50-h,baselineE=42;
    const numerator=Math.max(favorableG,baselineE)+Math.max(unfavorableG,baselineE)-2*baselineE;
    // Bayesian signal value is numerator/40, only if signal is lawful and precommitment.
    eq(numerator,Math.max(0,h-12),`signal threshold ${h}`);
    reports.push({accuracy_over_20:h,gross_signal_value_over_40:numerator});
  }
  eq(reports[5].gross_signal_value_over_40,3,"3/4 signal value");
  return {model:"three-date budget-and-recovery source P/grounding G/embodiment E synthetic witness",assertions:checks,
     world_low:{G_skip:"5/2",G_serve:"31/20",P:"2",E:"21/10",winner:"G-skip"},
     world_high:{G_skip:"3/2",G_serve:"31/20",P:"2",E:"21/10",winner:"E"},
     minimax_regret:{G_skip_probability:"2/5",E_probability:"3/5",G_serve_probability:"0",worst_regret:"6/25"},
     report:{accuracy:"3/4",gross_value:"3/40",minimum_decisive_accuracy:"3/5"},
     rows,reports};
};
console.log(JSON.stringify(verify(), null, 2));
