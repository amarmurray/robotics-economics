"use strict";
// Conditional finite original-buyer paid-production and active-report counterworlds. All values synthetic.
function activeSignalChecks(){
  const assert=(condition,msg)=>{if(!condition)throw Error(msg)};
  const attrs=[...Array(16)].map((_,i)=>({y:i&1,q:(i>>1)&1,b:(i>>2)&1,f:(i>>3)&1}));
  function getSums(atoms) {
    const q=[0,0],s=[0,0],b=[0,0],f=[0,0],m=[0,0];
    for(const a of atoms){m[a.y]+=a.w;b[a.y]+=a.w*a.b;f[a.y]+=a.w*a.f;q[a.y]+=a.w*a.q;s[a.y]+=a.w*a.q*a.b*a.f}
    return {q,s,b,f,m};
  }
  function economicNumerator(atoms,denom){
    const t=getSums(atoms);
    const extra=t.q.reduce((z,q,y)=>z+Math.max(0,4*t.s[y]-2*q),0);
    return {num:2*denom+extra,extra,q:t.q,s:t.s,b:t.b,f:t.f,m:t.m};
  }
  function directNumerator(atoms,denom) {
    let best=-1;
    for(let mask=0;mask<4;mask++){
      let val=0;
      for(const a of atoms)val+=a.w*((a.q&&((mask>>a.y)&1))?(a.b*a.f*4):2);
      if(val>best)best=val;
    }
    return best;
  }
  let assertions=0,tableCases=0,frechetPatterns=0;
  function enumerateSlots(slots,n,visit){
    const v=new Array(slots).fill(0);
    function rec(i,left){if(i===slots-1){v[i]=left;visit(v);return}for(let k=0;k<=left;k++){v[i]=k;rec(i+1,left-k)}}
    rec(0,n);
  }
  enumerateSlots(16,4,w=>{
    tableCases++;
    const atoms=attrs.map((a,i)=>({...a,w:w[i]}));
    const t=economicNumerator(atoms,4);
    assert(t.num===directNumerator(atoms,4),"stagewise optimizer disagreed");assertions++;
    for(let y=0;y<2;y++){
      const lower=Math.max(0,t.q[y]+t.b[y]+t.f[y]-2*t.m[y]), upper=Math.min(t.q[y],t.b[y],t.f[y]);
      assert(t.s[y]>=lower && t.s[y]<=upper,"Frechet stratum violation");assertions++;
    }
  });
  const feasible=new Map();
  const three=[...Array(8)].map((_,i)=>({q:i&1,b:(i>>1)&1,f:(i>>2)&1}));
  enumerateSlots(8,4,w=>{
    let q=0,b=0,f=0,s=0;
    for(let i=0;i<8;i++){q+=w[i]*three[i].q;b+=w[i]*three[i].b;f+=w[i]*three[i].f;s+=w[i]*three[i].q*three[i].b*three[i].f}
    const key=[q,b,f].join(",");
    const prior=feasible.get(key)||{lo:Infinity,hi:-Infinity};
    prior.lo=Math.min(prior.lo,s);prior.hi=Math.max(prior.hi,s);feasible.set(key,prior);
  });
  for(const [key,t] of feasible){const [q,b,f]=key.split(",").map(Number);assert(t.lo===Math.max(0,q+b+f-8) && t.hi===Math.min(q,b,f),"Frechet sharpness failed");assertions++;frechetPatterns++}
  function make(kind,world,report){
    const atoms=[];
    for(let z=0;z<=1;z++)for(let q=0;q<=(kind==="P"?1:0);q++){
      const Q=kind==="P"?q:1;
      const B=z,F=kind==="D"&&world==="II"?1-z:z; // free operator F; world II busy when buyer orders
      if(report==="perfect")atoms.push({y:z,q:Q,b:B,f:F,w:kind==="P"?2:4});
      else for(let y=0;y<=1;y++)atoms.push({y,q:Q,b:B,f:F,w:kind==="P"?1:2});
    }
    assert(atoms.reduce((x,a)=>x+a.w,0)===8,"wrong total");assertions++;
    return atoms;
  }
  const value=(kind,world,report)=>economicNumerator(make(kind,world,report),8).num;
  const Pcoin=value("P","I","coin"),Pperfect=value("P","I","perfect"),
        DIcoin=value("D","I","coin"),DIperfect=value("D","I","perfect"),
        DIIcoin=value("D","II","coin"),DIIperfect=value("D","II","perfect");
  for(const [x,n] of [[Pcoin,16],[Pperfect,20],[DIcoin,16],[DIperfect,24],[DIIcoin,16],[DIIperfect,16]]){assert(x===n,"headline mismatch");assertions++}
  // Denominator eight. P pilot receipt +4; D teleop cost -2. E is 12/5.
  const Pnet=Pcoin+4, DI_net=DIperfect-2, DII_net=DIIperfect-2;
  assert(Pnet===20 && DI_net===22 && DII_net===14,"net policy values");assertions++;
  assert(DI_net>Pnet && Pnet*5>12*8,"world I ranking");assertions++;
  assert(Pnet>DII_net && DII_net*5<12*8,"world II ranking");assertions++;
  const bridgeI=DIperfect-DIcoin-Pperfect+Pcoin;
  const bridgeII=DIIperfect-DIIcoin-Pperfect+Pcoin;
  assert(bridgeI===4&&bridgeII===-4,"interaction check");assertions++;
  // Never infer an action-dependent kernel from a report-only Blackwell comparison.
  return {
    synthetic_only:true,denominator:8,table_cases:tableCases,frechet_patterns:frechetPatterns,exact_integer_assertions:assertions,
    P:{uninformative_F_eighths:Pcoin,perfect_F_eighths:Pperfect,paid_pilot_eighths:4,net_eighths:Pnet},
    D_world_I:{uninformative_F_eighths:DIcoin,perfect_F_eighths:DIperfect,teleop_cost_eighths:2,net_eighths:DI_net},
    D_world_II:{uninformative_F_eighths:DIIcoin,perfect_F_eighths:DIIperfect,teleop_cost_eighths:2,net_eighths:DII_net},
    independent_embodiment_net:"12/5",kernel_signal_interaction_eighths:{world_I:bridgeI,world_II:bridgeII},
    science_gate:"OPEN",customer_paid_data:false
  };
}
const result=activeSignalChecks();
if(typeof module!=="undefined"&&module.exports)module.exports={activeSignalChecks};
if(typeof require!=="undefined"&&require.main===module)console.log(JSON.stringify(result,null,2));
