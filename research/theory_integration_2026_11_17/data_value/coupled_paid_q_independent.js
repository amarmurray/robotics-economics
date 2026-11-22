'use strict';
// Independent integer-only check of the half-half shared-learner construction.
let checks=0, peak=-1, at=[];
for(let k=0;k<=100;k++) {
  const direct=Math.max(0,k)+Math.max(0,k-100)-Math.max(0,2*k-100);
  const piecewise=Math.min(k,100-k);
  if(direct!==piecewise) throw Error(`Mismatch at ${k}`);
  checks++;
  if(direct>peak){peak=direct;at=[k];} else if(direct===peak) at.push(k);
}
if(peak!==50||at.length!==1||at[0]!==50) throw Error('Interior peak failed'); checks++;
const independentCorner=Math.max(0,100)+Math.max(0,-100)-Math.max(0,100-100);
if(independentCorner!==100) throw Error('Rectangular corner failed'); checks++;
console.log(JSON.stringify({checks, units:'loss is numerator/200; theta is k/100', coupled_max_numerator:peak, coupled_peak_k:at[0], rectangular_max_numerator:independentCorner, measured_robotics:false}));
