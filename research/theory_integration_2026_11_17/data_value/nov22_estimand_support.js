function modelCheck(){
  let checks=0;
  function ok(b,msg){if(!b)throw Error(msg);checks++;}
  const worlds=[
    {label:"nested",both:1,only0:0,only1:2,neither:1},
    {label:"nonnested",both:0,only0:1,only1:3,neither:0}
  ];
  for(const w of worlds){
    ok(w.both+w.only0+w.only1+w.neither===4,"population");
    ok(w.both+w.only0===1,"source0 success");
    ok(w.both+w.only1===3,"source1 success");
    ok(w.only1-w.only0===2,"net success difference");
  }
  ok(worlds[0].both===1 && worlds[1].both===0,"coupling endpoints");
  ok(worlds[0].only0===0 && worlds[1].only0===1,"regression difference");
  const fullJ0Twentieths=2*5+15,fullJ1Twentieths=2*15+5;
  ok(fullJ0Twentieths===25,"J0 full information");
  ok(fullJ1Twentieths===35,"J1 full information");
  const j0Lower=2*5+10, j0Upper=j0Lower+2*5;
  const j1=2*15+5;
  ok(j0Lower===20 && j0Upper===30,"partial support");
  ok(j1===35,"x1 policy");
  ok(j1-j0Upper===5 && j1-j0Lower===15,"contrast");
  const c=8; // extra source cost 2/5 = 8/20
  ok(j1-c-j0Upper===-3 && j1-c-j0Lower===7,"cost sensitivity");
  // Every pair of feasible response-type worlds in the constructed evidence class
  // has the same arm-marginal policy value, despite different cross-world overlap.
  for (const w of worlds){
    const p0=w.both+w.only0, p1=w.both+w.only1;
    ok(2*p0+(4-p0)===5,"J0 invariant in quarter-units");
    ok(2*p1+(4-p1)===7,"J1 invariant in quarter-units");
  }
  return {test_status:"passed",assertions:checks,design:"two exact response-type couplings; separate sharp-under-rectangularity partial-support calculation",couplings:worlds,unit_denominator:20,observed_dynamic_J:{x0:"5/4",x1:"7/4",difference:"1/2"},partial_support:{x0:["1","3/2"],x1:"7/4",contrast:["1/4","3/4"],after_x1_cost_2_over_5:["-3/20","7/20"]},note:"Exact integer arithmetic for synthetic illustration only; proofs and all field admission assumptions in companion text."};
}
if(typeof console !== 'undefined')console.log(JSON.stringify(modelCheck(),null,2));
