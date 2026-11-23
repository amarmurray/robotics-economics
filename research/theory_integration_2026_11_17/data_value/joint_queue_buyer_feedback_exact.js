"use strict";
// Synthetic eligible original-customer failure clusters; four equiprobable latent types.
// One original unpaid ticket A, plus a distinct follow-up ticket B only after accepted A.
// The two safety/validation repair jobs G and K each consume one of two t3 worker slots.
const V=[1,1,0,0];
function chooseTwo(n){const r=[];for(let i=0;i<n;i++)for(let j=i+1;j<n;j++)r.push([i,j]);return r;}
function histogram(x){const h={};for(const k of x){h[k]=(h[k]||0)+1}return Object.entries(h).sort();}
function evaluate(zOn){const Z=Array.from({length:4},(_,i)=>+zOn.includes(i));let nIntersect=0;
 const G=[],K=[],QT=[];let R4=0,G4=0,K4=0,GK4=0,safe4=0,earlyA4=0,lateB4=0;
 for(let i=0;i<4;i++){
  const v=V[i],z=Z[i],repairJobs=v+z,workerSlots=Math.max(0,2-repairJobs);
  const paidA=workerSlots>=1?1:0;
  const followupB=paidA; // newly authorized distinct ticket: no service, no renewal
  if(paidA&&workerSlots<1)throw Error("infeasible paid service");
  if(followupB&&!paidA)throw Error("fabricated buyer order");
  if(repairJobs>2)throw Error("queue violation");
  nIntersect+=+(v&&z);
  // R serves old complete recipe A; no follow-up in this stylized old policy.
  R4+=2;
  // G and K singly have at most one safety job and can serve one A ticket.
  G4+=3;K4+=3;
  earlyA4+=4*paidA;lateB4+=followupB;
  GK4+=4*paidA+followupB;
  // Nonanticipative safe policy observes G validation V before deciding on K.
  // With V=1 skip K, so one G job plus A/B service; with V=0 run K.
  safe4+=(v?3:5);
  G.push([v,1,1,1].join("/")); // G validation job; qualified A; original A paid; follow-up B paid
  K.push([z,1,1,1].join("/")); // K validation job; K-qualified A; original A paid; follow-up B paid
  QT.push("1/1"); // both independently qualifying complete A service recipes
 }
 return {Z_atoms:zOn,overlap_quarters:nIntersect,values_quarters:{R:R4,G:G4,K:K4,GK:GK4,E:17,adaptive_safe:safe4},originalA_quarters:earlyA4,followupB_quarters:lateB4,observable:{G:histogram(G),K:histogram(K),QT:histogram(QT)}};
}
function run(){let assertions=0;const assert=(yes,why)=>{assertions++;if(!yes)throw Error(why)};
 const worlds=chooseTwo(4).map(evaluate),ref=JSON.stringify(worlds[0].observable);
 for(const w of worlds){
  assert(JSON.stringify(w.observable)===ref,"separate complete arm/paired technical laws");
  for(const [name,n] of Object.entries({R:8,G:12,K:12,E:17,adaptive_safe:16}))assert(w.values_quarters[name]===n,"invariant "+name);
  assert(w.values_quarters.GK===20-5*w.overlap_quarters,"full program value");
  assert(w.values_quarters.GK===w.originalA_quarters+w.followupB_quarters,"no double counting");
  assert(w.originalA_quarters===4*w.followupB_quarters,"renewal generated only by paid A");
  assert(w.overlap_quarters>=0&&w.overlap_quarters<=2,"Frechet support");
 }
 const gs=worlds.map(x=>x.values_quarters.GK).sort((a,b)=>a-b);
 assert(JSON.stringify(gs)==="[10,15,15,15,15,20]","sharp six worlds");
 const regretAllAtNoOverlap=17-20; // GK best, E short by 3/4
 const eShort=20-17;
 const gShort=17-10;
 assert(eShort===3&&gShort===7,"regret payoffs in quarters");
 // Mixture α GK vs 1-α E across observationally identical endpoint laws.
 // Worst regret = max(3*(1-α),7*α)/4. Equality at α=3/10, regret21/40.
 const num=3,den=10;
 assert(3*(den-num)===7*num,"regret equality");
 assert((3*(den-num))/(4*den)===21/40,"regret value");
 assert(regretAllAtNoOverlap===-3,"regret sign check");
 // Conditional optimization with legally observed validation V before K:
 // U law inferred from hypothetical signed joint audit, not known under old arm data.
 // Value = max(4,5-5z) where z is Pr(V=1,Z=1).
 for(let t=0;t<=2;t++){
  const z=t/4,full=5*(1-z),opt=Math.max(4,full);
  const gV1=3, kV1=5*(1-t/2);
  assert(opt===2.5+0.5*Math.max(gV1,kV1),"conditional decision policy");
 }
 return {synthetic:true,exact_assertions:assertions,unit:"per four equally weighted eligible failed original tickets, quarter units",worlds:worlds.map(w=>({Z_atoms:w.Z_atoms,overlap_quarters:w.overlap_quarters,values_quarters:w.values_quarters,originalA_quarters:w.originalA_quarters,followupB_quarters:w.followupB_quarters})),observable_histogram:worlds[0].observable,sharp_full_program_quarters:[10,20],E_quarters:17,adaptive_safe_quarters:16,unknown_joint_overlap_bound:[0,"1/2"],precommitment_minimax_regret_full_GK_fraction:"3/10",precommitment_worst_regret:"21/40",conditional_if_joint_law_known_adaptive_value:"max(4,5-5z)"};
}
if(typeof module!=="undefined"){module.exports={run,evaluate,chooseTwo};if(require.main===module)console.log(JSON.stringify(run(),null,2));}
