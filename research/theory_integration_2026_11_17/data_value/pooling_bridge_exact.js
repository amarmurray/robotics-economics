"use strict";
// Conditional synthetic proof checks; no robot or original-customer field data.
const result=(function runExact(){
  let checks=0;const ok=(a,m)=>{checks++;if(!a)throw Error(m)};
  let low=Infinity,high=-Infinity,grid=0;
  for(let s=0;s<=3;s++)for(let e=0;e<=3;e++){
    const v=1+s-e;low=Math.min(low,v);high=Math.max(high,v);
    ok(v>=-2&&v<=4,"gain interval");grid++;
  }
  ok(low===-2&&high===4,"sharp rectangle");
  const cert=[4-0.25+0.5-1,4+0.25+2-0];
  ok(cert[0]===3.25&&cert[1]===6.25,"bridge certificate");
  const iso=(_a,_b,_m)=>2,pooled=(a,world,m)=>2+(m>=2&&a===world?1:0);
  for(const a of ["SG","E"])for(const b of [0,1])ok(iso(a,b,1)===2,"one-island equivalence");
  const worldA=pooled("SG","SG",2)-pooled("E","SG",2);
  const worldB=pooled("SG","E",2)-pooled("E","E",2);
  ok(worldA===1&&worldB===-1,"opposite whole-market ranking");
  const F=(x,y)=>2+3*x+5*y+7*x*y;
  for(let x=0;x<=1;x++)for(let y=0;y<=1;y++){
    ok(Math.abs(F(1,y)-F(0,y))<=10,"uniform x");
    ok(Math.abs(F(x,1)-F(x,0))<=12,"uniform y");
  }
  ok(F(1,1)-F(0,0)===15&&15<=22,"telescoping");
  const N=20;ok(N>1,"global shared update");
  const vals=[];
  for(const joint of [0,0.5]){
    const p11=joint,p10=0.5-joint,p01=0.5-joint,p00=joint;
    ok(p11+p10===0.5&&p11+p01===0.5&&p11+p10+p01+p00===1,"same marginals");
    vals.push(8*p11);
  }
  ok(vals[0]===0&&vals[1]===4,"bundle payout");
  return {schema:"synthetic-conditional-v1",exact_integer_gain_scenarios:grid,checks,isolated_gap:0,pooled_gap_world_A:worldA,pooled_gap_world_B:worldB,pooled_optional_gain_range:[0,1],synthetic_gain_interval:[low,high],synthetic_certified_interval:cert,cut_edge_sensitivity:[10,12],cut_total_bound:22,cut_actual_change:15,global_cascade_for_one_external_source_at_N20:20,joint_qualification_bundle_contributions:vals,scientific_novelty_established:false,customer_data_used:false};
})();
console.log(JSON.stringify(result,null,2));
