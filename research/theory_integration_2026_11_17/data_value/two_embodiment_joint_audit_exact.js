"use strict";
// Exact synthetic two-embodiment, one-worker, original-buyer audit study.
// Scale every per-world contribution by eight and every law weight by 128.
// No external dependencies, field estimates, or model-training execution.
function assert(condition, message) { if (!condition) throw Error(message); }
function evaluate(w) {
  // Mix even parity weight (16-w) and odd parity weight w.
  // For each of four parity states, Q=0 and Q=1 have equal weight.
  assert(Number.isInteger(w) && w >= 0 && w <= 16, "invalid weight");
  const totals = {R:0n,P:0n,G:0n,E:0n};
  const singles={A:0n,C:0n,W:0n}, pairs={AC:0n,AW:0n,CW:0n};
  let triple=0n, mass=0n;
  for(let A=0; A<=1; A++) for(let C=0; C<=1; C++)
  for(let W=0; W<=1; W++) for(let Q=0; Q<=1; Q++) {
    const odd=(A+C+W)%2;
    const m=BigInt(odd ? w : 16-w);
    const canShared=Number(Boolean(A || C)), canP=Number(Boolean(A || (Q && C)));
    const value={R:16*W*A,P:16*W*canP,G:16*W*canShared-1,
                 E:16*C+16*W*A-6};
    for(const k of Object.keys(totals)) totals[k]+=m*BigInt(value[k]);
    mass+=m;
    singles.A+=m*BigInt(A); singles.C+=m*BigInt(C); singles.W+=m*BigInt(W);
    pairs.AC+=m*BigInt(A*C); pairs.AW+=m*BigInt(A*W); pairs.CW+=m*BigInt(C*W);
    triple+=m*BigInt(A*C*W);
  }
  assert(mass===128n,"law must normalize");
  return {total:totals,singles,pairs,triple,mass,denominator:1024n};
}
function run() {
  let assertions=0;
  function eq(a,b,n){assert(a===b,n+": "+a+" != "+b); assertions++;}
  for(let w=0;w<=16;w++) {
    const s=evaluate(w);
    for(const k of ["A","C","W"])eq(s.singles[k],64n,"single "+k);
    for(const k of ["AC","AW","CW"])eq(s.pairs[k],32n,"pair "+k);
    eq(s.triple,BigInt(2*w),"triple");
    eq(s.total.R,512n,"R");
    eq(s.total.P,BigInt(768-16*w),"P");
    eq(s.total.G,BigInt(896-32*w),"G");
    eq(s.total.E,768n,"E");
  }
  const low=evaluate(0), high=evaluate(16);
  eq(low.total.G-low.total.E,128n,"low G gain");
  eq(high.total.E-high.total.G,384n,"high E gain");
  // Minimax regret over all sixteen-step mixtures.
  let minWorst=null, argmins=[];
  for(let k=0;k<=16;k++){
    const lowRegret=BigInt(8*(16-k));  // numerator over 1024
    const highRegret=BigInt(24*k);     // numerator over 1024
    const worst=lowRegret>highRegret?lowRegret:highRegret;
    if(minWorst===null || worst<minWorst){minWorst=worst;argmins=[k];}
    else if(worst===minWorst)argmins.push(k);
    eq(lowRegret,BigInt((16-k)*8),"endpoint regret low");
    eq(highRegret,BigInt(k*24),"endpoint regret high");
  }
  eq(minWorst,96n,"minimax regret numerator");
  eq(BigInt(argmins[0]),4n,"minimax G sixteenths");
  eq(BigInt(argmins.length),1n,"unique minimax grid weight");
  return {checked_assertions:assertions,laws:17,denominator:"1024",
    low:{R:"1/2",P:"3/4",G:"7/8",E:"3/4",triple:"0"},
    high:{R:"1/2",P:"1/2",G:"3/8",E:"3/4",triple:"1/4"},
    formulas:{R:"1/2",P:"3/4-t",G:"7/8-2t",E:"3/4",t:"w/64"},
    minimax:{G_probability:"1/4",E_probability:"3/4",worst_regret:"3/32"}};
}
if (typeof module !== "undefined" && module.exports) module.exports={evaluate,run};
if (typeof require !== "undefined" && typeof module !== "undefined" && require.main===module)
  console.log(JSON.stringify(run(),null,2));
