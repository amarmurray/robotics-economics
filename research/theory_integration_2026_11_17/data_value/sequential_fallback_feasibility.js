"use strict";
const auditResult = (function () {
  const D = 8;
  const check = (ok, msg) => { if (!ok) throw Error(msg); };
  const keys = new Map(), detailed = new Map();
  let tables = 0, assertions = 0;
  // Partition the X-failure population into successful and unsuccessful post-X retries.
  // r1 is old R success among X successes, r2 among X failures/retry successes,
  // r3 among X failures/retry failures. The physical old-case regression is r3.
  for (let x = 0; x <= D; x++) {
    for (let b = 0; b <= D - x; b++) {
      const retry = D - x - b, k = D - x;
      for (let r1 = 0; r1 <= x; r1++) for (let r2 = 0; r2 <= retry; r2++)
      for (let r3 = 0; r3 <= b; r3++) {
        tables++;
        const r = r1 + r2 + r3, a = r2 + r3;
        const first = [r,x,b].join("/"), second = [r,x,b,a].join("/");
        const update = (map,key,v) => {
          const s = map.get(key) || { min: v, max: v, n: 0 };
          s.min = Math.min(s.min,v); s.max = Math.max(s.max,v); s.n++;
          map.set(key,s);
        };
        update(keys,first,r3); update(detailed,second,r3);
        check(r3 >= Math.max(0,r+b-D) && r3 <= Math.min(r,b),"coarse bound fails");
        check(r3 >= Math.max(0,a+b-k) && r3 <= Math.min(a,b),"paired X-failure bound fails");
        assertions += 2;
      }
    }
  }
  for (const [key,law] of keys) {
    const [r,x,b] = key.split("/").map(Number);
    check(law.min === Math.max(0,r+b-D) && law.max === Math.min(r,b),
          "coarse sharpness "+key); assertions++;
  }
  for (const [key,law] of detailed) {
    const [r,x,b,a] = key.split("/").map(Number), k = D-x;
    check(law.min === Math.max(0,a+b-k) && law.max === Math.min(a,b),
          "conditional sharpness "+key); assertions++;
  }
  // Two eight-history physical worlds: identical R, X, sequential F marginal
  // qualifications, but different old-success/new-sequential-failure overlap.
  const X = [1,1,1,0,1,1,1,0];
  const after = [0,0,0,1,0,0,0,0]; // actionable only if X==0
  const R_nested = [1,1,1,1,0,0,0,0];
  const R_crossed = [1,1,1,0,0,0,0,1];
  const F = X.map((v,i) => v || after[i]);
  const sum = v => v.reduce((a,b)=>a+b,0);
  const loss = R => R.reduce((a,v,i)=>a+(v === 1 && F[i] === 0 ? 1 : 0),0);
  check(sum(X)===6 && sum(F)===7 && sum(R_nested)===4 && sum(R_crossed)===4,
        "counterworld marginal check"); assertions++;
  check(loss(R_nested)===0 && loss(R_crossed)===1,"physical regression worlds"); assertions++;
  const oldPaid = 4*sum(R_nested)/D;
  const goodGross = 4*sum(F)/D;
  const buyerAltered = [1,1,1,0,0,0,0,0];
  const buyerDriftGross = 4*sum(F.map((v,i)=>v*buyerAltered[i]))/D;
  check(oldPaid===2 && goodGross===3.5 && buyerDriftGross===1.5,"buyer and cost worlds"); assertions++;
  check(goodGross-2<oldPaid && goodGross>oldPaid && buyerDriftGross<oldPaid,
        "qualification and net production ranking"); assertions++;
  return {
    status:"passed",denominator:D,full_atom_tables:tables,coarse_margin_groups:keys.size,
    paired_X_failure_groups:detailed.size,integer_assertions:assertions,
    physical_counterworlds:{
      old_R_successes:4,X_successes:6,post_X_retry_failures:1,
      sequential_F_successes:7,regressions_nested:0,regressions_crossed:1
    },
    original_order_market_synthetic:{
      old_paid_contribution:oldPaid,all_buyer_support_F_gross:goodGross,
      F_net_with_additional_cost_2:goodGross-2,
      changed_buyer_F_gross_no_extra_cost:buyerDriftGross
    },
    scope:"Finite denominator-8 table enumeration and synthetic exact integer/rational examples only; formula proofs are separate. No physical safety approval or market estimate."
  };
})();
if (typeof module !== "undefined") {
  module.exports = auditResult;
  if (require.main === module) console.log(JSON.stringify(auditResult, null, 2));
}
auditResult;
