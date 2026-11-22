"use strict";
/*
  Exact finite-horizon lawful production/learning menu example.
  All values are integers in units of 1/40 normalized net paid contribution.
  Two ex-ante original buyers A,B each have probability 1/2. A "pilot" is
  accepted/paid service at t=0 and, only with G_info license, reports the order.
  Source S qualifies recipe b; embodiment E qualifies recipe e.
  This is a conditional synthetic reference-table, not an empirical estimate.
*/
function assert(x, description) { if (!x) throw new Error(description); }
const PROGRAMS = {
  R:  {actions:["a"],report:false,cost:0},
  S:  {actions:["a","b"],report:false,cost:0},
  G:  {actions:["a"],report:true,cost:0},
  SG: {actions:["a","b"],report:true,cost:8},
  E:  {actions:["a","e"],report:false,cost:2}
};
const REFERENCE={a:{A:40,B:0},b:{A:0,B:40},e:{A:30,B:30}};
const buyers=["A","B"];
function qValue(pay,action,observation) {
  return observation==="A"||observation==="B" ?
     pay[action][observation] :
     (pay[action].A+pay[action].B)/2;
}
function bestValue(pay,acts,obs) {
  return Math.max(...acts.map(a=>qValue(pay,a,obs)));
}
// History can reveal order only after licensed paid production; hidden buyer is
// not spuriously inserted into the firm's information state without a report.
function continuation(pay,acts,first,licensed) {
  if (first==="pilot"&&licensed) {
    return (bestValue(pay,acts,"A")+bestValue(pay,acts,"B"))/2;
  }
  return bestValue(pay,acts,"N");
}
function optimize(program,hideReport=false,pay=REFERENCE,pilotReceipt=8) {
  const acts=program.actions,licensed=program.report&&!hideReport;
  const values=[
    {first:"skip",gross:continuation(pay,acts,"skip",licensed)},
    {first:"pilot",gross:pilotReceipt+continuation(pay,acts,"pilot",licensed)}
  ];
  const best=values.reduce((x,y)=>y.gross>x.gross?y:x);
  const reportOn=best.first==="pilot"&&licensed;
  const choose=(obs)=>acts.find(a=>qValue(pay,a,obs)===bestValue(pay,acts,obs));
  return {first:best.first,actions:reportOn?{A:choose("A"),B:choose("B")}:{N:choose("N")},
    gross:best.gross,net:best.gross-program.cost,allFirstValues:values};
}
function restrictedPolicyValue(program,first,action,pay=REFERENCE,pilotReceipt=8) {
  return (first==="pilot"?pilotReceipt:0)+qValue(pay,action,"N");
}
// Bellman optimality telescoping, evaluated using FULL information histories
// reached under the restricted policy. The first decision can itself lose value.
function regretCertificate(program,first,action,pay=REFERENCE,pilotReceipt=8) {
  const full=optimize(program,false,pay,pilotReceipt);
  const licensed=program.report;
  const firstFullQ=(first==="pilot"?pilotReceipt:0)+continuation(pay,program.actions,first,licensed);
  const stageZero=full.gross-firstFullQ;
  const stageOne= first==="pilot"&&licensed ?
    ((bestValue(pay,program.actions,"A")-qValue(pay,action,"A"))+
     (bestValue(pay,program.actions,"B")-qValue(pay,action,"B")))/2 :
    bestValue(pay,program.actions,"N")-qValue(pay,action,"N");
  const restricted=restrictedPolicyValue(program,first,action,pay,pilotReceipt);
  assert(stageZero>=0&&stageOne>=0,"Bellman regrets must be nonnegative");
  assert(stageZero+stageOne===full.gross-restricted,"exact occupancy regret telescoping");
  return {firstDecision:stageZero,continuation:stageOne,total:stageZero+stageOne};
}
function main() {
  let checks=0;
  const results={};
  for(const name of Object.keys(PROGRAMS)) {
    const p=PROGRAMS[name],full=optimize(p,false),coarsened=optimize(p,true);
    assert(full.gross>=coarsened.gross,"information monotonicity");checks++;
    const chosen=Object.values(coarsened.actions)[0];
    const cert=regretCertificate(p,coarsened.first,chosen);
    assert(cert.total===full.gross-coarsened.gross,"program-specific regret equality");checks++;
    results[name]={full,coarsened,regret:cert};
  }
  assert(results.SG.full.gross===48&&results.SG.coarsened.gross===28,"SG licensed report");
  assert(results.E.full.gross===38&&results.E.coarsened.gross===38,"E common optimal");
  assert(results.SG.regret.firstDecision===0&&results.SG.regret.continuation===20,"t1 omission, not t0");
  checks+=3;
  const gapFull=results.SG.full.net-results.E.full.net;
  const gapCoarsened=results.SG.coarsened.net-results.E.coarsened.net;
  assert(gapFull===4&&gapCoarsened===-16,"investment reversal");
  assert(gapFull===gapCoarsened+results.SG.regret.total-results.E.regret.total,"gap identity");
  checks+=2;
  // Exhaust payoff-table *structures* (all 3^4 two-action two-buyer maps),
  // four pilot receipts, both first actions and both report-blind dispatches.
  // These checks corroborate implementation, NOT the mathematical proof.
  let tables=0,policyChecks=0,zeroRegret=0;
  const choices=[0,20,40],pilotChoices=[-20,0,8,20];
  const p={actions:["a","b"],report:true,cost:0};
  for(const aa of choices)for(const ab of choices)for(const ba of choices)for(const bb of choices) {
    const pay={a:{A:aa,B:ab},b:{A:ba,B:bb}};tables++;
    for(const pilot of pilotChoices){
      const full=optimize(p,false,pay,pilot),reduced=optimize(p,true,pay,pilot);
      assert(full.gross>=reduced.gross,"nested-policy inequality");checks++;
      for(const first of ["skip","pilot"])for(const action of p.actions){
        const cert=regretCertificate(p,first,action,pay,pilot);checks++;
        policyChecks++;if(cert.total===0)zeroRegret++;
      }
    }
  }
  return {units:"1/40 normalized paid contribution",synthetic:true,
     programs:results,gapFull,gapCoarsened,
     exactGapDecomposition:{reportRegretSG:results.SG.regret.total,
       reportRegretE:results.E.regret.total},
     exhaustiveStructuralChecks:{twoBuyerPayoffTables:tables,pilotReceipts:pilotChoices.length,
       policyChecks,zeroRegretPolicies:zeroRegret},
     assertions:checks,notes:"All buyer receipts, licensed report and recipe payoffs are stipulated; nothing is a field estimate."};
}
if (typeof module!=="undefined"&&require.main===module)
  process.stdout.write(JSON.stringify(main(),null,2)+"\n");
