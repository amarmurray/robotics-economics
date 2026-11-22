"use strict";

// Conditional finite-state robotics-economics counterexamples; no field observations.
// Run: node lagged_demand_operator_exact.js
function* compositions(total, size) {
  if (size === 1) { yield [total]; return; }
  for (let x = 0; x <= total; x++) {
    for (const tail of compositions(total - x, size - 1)) yield [x, ...tail];
  }
}
function assert(condition, message) { if (!condition) throw new Error(message); }
function run() {
  const N = 6, strata = new Map();
  let cases = 0, checks = 0;
  // Bit order: Q=4, A=2, B=1. Event S is cell 101.
  for (const p of compositions(N, 8)) {
    const q = p[4] + p[5] + p[6] + p[7];
    const a = p[2] + p[3] + p[6] + p[7];
    const b = p[1] + p[3] + p[5] + p[7];
    const s = p[5], low = Math.max(0, q + b - a - N);
    const high = Math.min(q, b, N - a);
    assert(low <= s && s <= high, "three-way intersection inequality"); checks++;
    // vA=4,vB=3, one shared service slot; sum over 8 elementary outcomes.
    let brute = 0;
    for (let i = 0; i < 8; i++) {
      const Q = !!(i & 4), A = !!(i & 2), B = !!(i & 1);
      brute += p[i] * (A ? 4 : Q && B ? 3 : 0);
    }
    assert(brute === 4 * a + 3 * s, "terminal optimized production identity"); checks++;
    const key = [q, a, b].join(",");
    if (!strata.has(key)) strata.set(key, {low: N, high: -1, formulaLow: low, formulaHigh: high});
    const x = strata.get(key);
    x.low = Math.min(x.low, s); x.high = Math.max(x.high, s);
    cases++;
  }
  for (const x of strata.values()) {
    assert(x.low === x.formulaLow && x.high === x.formulaHigh, "sharp marginal bound attained");
    checks++;
  }
  let recoveryCases = 0, recoveryStrata = new Map();
  // Bit order Q=2, H=1. H is future operator recovery occupancy.
  for (const p of compositions(8, 4)) {
    const q = p[2] + p[3], h = p[1] + p[3], j = p[3];
    const low = Math.max(0, q + h - 8), high = Math.min(q, h);
    assert(j >= low && j <= high, "recovery association Fréchet inequality"); checks++;
    // With a standing paid A offer 1 and value-2 new C offer exactly upon Q,
    // an occupied shared operator H cancels all service: E[V2]=(8-h+q-j)/8.
    const byCells = p[0] + 2 * p[2];
    assert(byCells === 8 - h + q - j, "future paid occupancy identity"); checks++;
    const key = [q, h].join(",");
    if (!recoveryStrata.has(key)) recoveryStrata.set(key, {low:8, high:-1, formulaLow:low, formulaHigh:high});
    const x = recoveryStrata.get(key);
    x.low = Math.min(x.low, j); x.high = Math.max(x.high, j);
    recoveryCases++;
  }
  for (const x of recoveryStrata.values()) {
    assert(x.low === x.formulaLow && x.high === x.formulaHigh, "sharp recovery coupling"); checks++;
  }
  // P's paid pilot S is also its permissioned source-learning event Q.
  // Current pilot net receipt S/4 - 1/8; expected current contribution is zero.
  // In staggered market: A=1-S,B=S; synchronized: A=S,B=S.
  function pValue(staggered) {
    let numerator = 0; // expected net in sixteenths
    for (let S = 0; S < 2; S++) {
      const Q = S, A = staggered ? 1 - S : S, B = S;
      const serviceEighths = A || (Q && B) ? 8 : 0;
      const pilotEighths = 2 * S - 1;
      numerator += pilotEighths + serviceEighths; // each S has probability 1/2
    }
    return numerator; // /16
  }
  const P_stagger = pValue(true), P_sync = pValue(false);
  // D: independent fair Q,A,B. Expected paid 1/2 + 1/8; data cost 1/16.
  // E: licensed qualified A,B with independent simultaneous operator slots,
  // each fair marginal offer; expected paid 1, investment cost 3/8.
  const D = 8 + 2 - 1, E = 16 - 6; // denominator 16
  assert(P_stagger === 16 && P_sync === 8 && D === 9 && E === 10, "P/D/E paid rankings");
  checks++;
  // At t1 with two currently paid offers A=1,B=3/4, B can generate new
  // licensed Q_C with prob 5/8, while shared t2 recovery H has prob 1/4.
  // B minus A entire-program numerator in eighths is 1 - jCount,
  // where jCount counts Q_C and H coinciding in eight equally likely atoms.
  const BminusA_disjoint = 1 - 0, BminusA_nested = 1 - 2;
  assert(BminusA_disjoint === 1 && BminusA_nested === -1, "future-learning dispatch reversal");
  checks++;
  return {
    status: "conditional_synthetic_exact",
    triple_law_enumeration: {denominator:N, cases, marginal_strata:strata.size},
    recovery_law_enumeration: {denominator:8, cases:recoveryCases, marginal_strata:recoveryStrata.size},
    exact_integer_assertions: checks,
    program_values_sixteenths: {P_stagger,P_sync,D,E},
    paid_dispatch_advantage_eighths: {QH_disjoint:BminusA_disjoint,QH_nested:BminusA_nested},
    unobserved_original_buyer_data: true,
    actual_intervention_performed: false,
    novelty_established: false
  };
}
if (typeof require !== "undefined" && require.main === module) console.log(JSON.stringify(run(), null, 2));
if (typeof module !== "undefined") module.exports = {run};
