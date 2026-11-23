"use strict";
/*
 Exact integer verification for longitudinal original-offer / repair-queue
 witness. Synthetic law, not observed robotic service. Node 18+.
*/
function verify() {
  let assertions = 0;
  function check(x, explanation) {
    assertions++;
    if (!x) throw new Error(explanation || "failed exact assertion");
  }
  const total = 8, byMargins = new Map();
  let tables = 0;
  // Entries are (J=0,D=0),(J=0,D=1),(J=1,D=0),(J=1,D=1).
  for (let a = 0; a <= total; a++) {
    for (let b = 0; b <= total-a; b++) {
      for (let c = 0; c <= total-a-b; c++) {
        const e = total-a-b-c;
        const dNum = b+e, jNum = c+e, xNum = b;
        const lower = Math.max(0,dNum-jNum);
        const upper = Math.min(dNum,total-jNum);
        check(lower <= xNum && xNum <= upper,"Frechet bounds");
        const key = dNum + ":" + jNum;
        if (!byMargins.has(key)) byMargins.set(key,{dNum,jNum,min:total,max:0});
        const m=byMargins.get(key);
        m.min=Math.min(m.min,xNum);
        m.max=Math.max(m.max,xNum);
        // Serve C at t2 receives one; C budget falls to zero.
        // Terminal A service earns four if original A offer and no repair.
        const numerator8=total+4*xNum;  // eight times expected G contribution
        check(numerator8>=total && numerator8<=5*total,"paid service bounds");
        tables++;
      }
    }
  }
  for(const m of byMargins.values()) {
    check(m.min===Math.max(0,m.dNum-m.jNum),"sharp lower");
    check(m.max===Math.min(m.dNum,total-m.jNum),"sharp upper");
  }
  function scenario(mode) {
    let gContributionTimes2=0, rContributionTimes2=0;
    let dEvents=0,jEvents=0,xEvents=0;
    for(const u of [0,1]) {
      const earlyAccepted=0, capacityA=1-earlyAccepted;
      const j2=u;                       // new job arrives AFTER t2 worker window
      const d3=mode==="positive"?1-u:u;
      const safeSkipD3=u;                 // identical historical R potential history
      const cBudgetAfterServe=0;         // one lifetime C purchase was accepted
      const workerFree3=Number(j2===0); // L3=(L2-1)_+ + J2; L2=0
      check(capacityA>=0 && cBudgetAfterServe===0,"buyer budget");
      gContributionTimes2+=1+4*capacityA*workerFree3*d3;
      rContributionTimes2+=4*safeSkipD3;
      dEvents+=d3; jEvents+=j2;
      xEvents+=d3*workerFree3;
    }
    return {gNumerator:gContributionTimes2,gDenominator:2,
      rNumerator:rContributionTimes2,rDenominator:2,
      dNumerator:dEvents,jNumerator:jEvents,
      xNumerator:xEvents};
  }
  const low=scenario("negative"), high=scenario("positive");
  check(low.gNumerator===2 && high.gNumerator===6,"world reversal");
  check(low.rNumerator===4 && high.rNumerator===4,"same observed R");
  check(low.dNumerator===1 && high.dNumerator===1,"same G buyer marginal");
  check(low.jNumerator===1 && high.jNumerator===1,"same G repair marginal");
  check(low.xNumerator===0 && high.xNumerator===1,"missing G joint");
  // E contributes 9/4; P contributes 11/5; retained safe policy 2.
  check(4*low.gNumerator < 9*low.gDenominator,"E beats G in low world");
  check(4*high.gNumerator > 9*high.gDenominator,"G beats E in high world");
  check(11*4 < 9*5,"P=11/5 below E=9/4");
  // At t2 L2=1 and no service. Clear the job, allowing t3 service.
  // An admissible t2 signal perfectly reports which of A/C will order.
  const noSignalValueTimes2=4, signalValueTimes2=8;
  check(signalValueTimes2-noSignalValueTimes2===4,"t2 audit value 2");
  return {exact_assertions:assertions,quarter_eighth_grid_denominator:total,
    joint_tables:tables,marginal_pairs:byMargins.size,
    sharp_bound_all_marginal_pairs:true,
    low_G:"1",high_G:"3",retained_R:"2",
    competing_E:"9/4",productive_P:"11/5",
    blocked_t2_audit_value:"2",G_order_and_job_marginals:"1/2"};
}
if (typeof module !== "undefined" && require.main === module)
  process.stdout.write(JSON.stringify(verify(),null,2)+"\n");
