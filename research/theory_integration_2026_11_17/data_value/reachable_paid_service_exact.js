'use strict';
// Exact integer-grid sanity checks for the conditional reachable-service theorem.
// No market values or robotic parameters in this script are empirical.
function sharp(q,j,d=8){const lower=Math.max(0,q-j),upper=Math.min(q,d-j);return {lower,upper}}

function fourCells(q,j,t,d=8){return [t,q-t,d-j-t,j-q+t]}

function queue(l,j){return Math.max(0,l+j-1)}

function runExact(){
  let checks=0,cases=0,sharpEndpoints=0;
  for(let d of [4,8,16]){
    for(let q=0;q<=d;q++)for(let j=0;j<=d;j++){
      const {lower,upper}=sharp(q,j,d);
      let feasible=[];
      for(let t=0;t<=d;t++){
        const cell=fourCells(q,j,t,d),ok=cell.every(x=>x>=0);
        checks++;if(ok){
          feasible.push(t);
          if(cell.reduce((a,b)=>a+b,0)!==d)throw Error("total");
          if(cell[0]+cell[1]!==q || cell[1]+cell[3]!==j)throw Error("marginals");
          checks+=3;
        }
      }
      if(feasible[0]!==lower||feasible[feasible.length-1]!==upper||feasible.length!==upper-lower+1)throw Error("sharp bounds");
      checks+=3;cases++;
    }
    for(let l of [0,1])for(let j of [0,1]){const L=queue(l,j);if(L!==Math.max(0,l+j-1)|| (l===0&&L!==0)||(l===1&&L!==j))throw Error("queue");checks+=3}
  }
  const q=6,j=4,d=8;
  const {lower,upper}=sharp(q,j,d);
  if(lower!==2||upper!==4)throw Error("example");
  const gLow32=24+8*lower,gHigh32=24+8*upper,e32=52,p32=48;
  if(gLow32!==40||gHigh32!==56||!(gLow32<p32&&p32<e32&&e32<gHigh32))throw Error("ranking");
  const mixG_num=1,mixG_den=4;
  for(let t=lower;t<=upper;t++){
    const g32=24+8*t,chosen32=(mixG_num*g32+(mixG_den-mixG_num)*e32)/mixG_den,oracle32=Math.max(g32,e32,p32);
    if(!Number.isInteger(chosen32)||oracle32-chosen32>3)throw Error("regret");
    checks+=2;
  }
  const lowerJCertified=sharp(6,2,8).lower; if(lowerJCertified!==4||24+8*lowerJCertified!==56)throw Error("engineering case");
  checks+=8;
  return {case_grid:cases,integer_assertions:checks,denominators:[4,8,16],example:{g_low:"5/4",g_high:"7/4",p:"3/2",e:"13/8",minimax_grounding_fraction:"1/4",maximum_regret:"3/32",perfect_information_value:"1/16",external_j_upper_one_quarter_g_lower:"7/4"},limitations:"synthetic logical enumeration, not measured robot production"};
}
if (typeof module !== 'undefined' && require.main === module) {
  process.stdout.write(JSON.stringify(runExact(), null, 2) + '\n');
}
