'use strict';
// Exact integer-tick synthetic program; one tick = 1/4 normalized paid contribution.
// These are mathematical constructions, not observed robotics economics.
const assert = require('node:assert/strict');
const pool = {
  idle: [0, 0],
  oldA: [4, 0],
  oldB: [0, 4],
  learnedB: [0, 4],
  learnedUniversal: [3, 3]
};
function numerator(menu, informed) {
  assert(menu.length > 0);
  if (informed) return Math.max(...menu.map(k => pool[k][0])) + Math.max(...menu.map(k => pool[k][1]));
  return Math.max(...menu.map(k => pool[k][0] + pool[k][1]));
}
// All returned integers have units of 1/8 paid contribution (the prior is 1/2 each).
function assess(oldMenu, newMenu) {
  const v00 = numerator(oldMenu, false), v01 = numerator(oldMenu, true);
  const v10 = numerator(newMenu, false), v11 = numerator(newMenu, true);
  return {v00,v01,v10,v11,sourceWithout:v10-v00,sourceWith:v11-v01,
    infoBefore:v01-v00,infoAfter:v11-v10,interaction:v11-v10-v01+v00};
}
const positive=assess(['idle','oldA'],['idle','oldA','learnedB']);
const negative=assess(['idle','oldA','oldB'],['idle','oldA','oldB','learnedUniversal']);
assert.deepEqual(positive,{v00:4,v01:4,v10:4,v11:8,sourceWithout:0,sourceWith:4,infoBefore:0,infoAfter:4,interaction:4});
assert.deepEqual(negative,{v00:4,v01:8,v10:6,v11:8,sourceWithout:2,sourceWith:0,infoBefore:4,infoAfter:2,interaction:-2});
let checks=2, strictPositive=0, strictNegative=0, zero=0, nested=0;
const candidates=['idle','oldA','oldB','learnedUniversal'];
for(let oldMask=1;oldMask<16;oldMask++) {
  for(let newMask=1;newMask<16;newMask++) {
    if ((newMask & oldMask)!==oldMask || newMask===oldMask) continue;
    const old=candidates.filter((_,i)=>(oldMask&(1<<i))!==0);
    const expanded=candidates.filter((_,i)=>(newMask&(1<<i))!==0);
    const r=assess(old,expanded);nested++;
    assert(r.sourceWithout>=0 && r.sourceWith>=0 && r.infoBefore>=0 && r.infoAfter>=0);checks++;
    assert.equal(r.interaction,r.sourceWith-r.sourceWithout);checks++;
    assert.equal(r.interaction,r.infoAfter-r.infoBefore);checks++;
    if(r.interaction>0)strictPositive++;
    else if(r.interaction<0)strictNegative++;
    else zero++;
  }
}
assert.equal(nested,50);
// A constant-C controller chooses one action for both Z; the old R policy's
// oldA is optimal at both types (including an allowable tie at B), but SG's
// optimal action sets are disjoint: oldA at A and learnedB at B.
function argmax(menu,z){const m=Math.max(...menu.map(k=>pool[k][z]));return menu.filter(k=>pool[k][z]===m);}
const oldArg=[argmax(['idle','oldA'],0),argmax(['idle','oldA'],1)];
const sgArg=[argmax(['idle','oldA','learnedB'],0),argmax(['idle','oldA','learnedB'],1)];
assert(oldArg[0].some(a=>oldArg[1].includes(a)));checks++;
assert(!sgArg[0].some(a=>sgArg[1].includes(a)));checks++;
const result={units:'value = numerator/8 normalized paid units',worlds:{positive,negative},
  allNestedFourActionWorlds:{count:nested,strictPositive,strictNegative,zero,checks},
  oldCommonOptimalAction:true,sourceTrainedCommonOptimalAction:false,
  fieldObservations:false,originalBuyerSettlementData:false,authorizedInterventions:false};
console.log(JSON.stringify(result,null,2));
