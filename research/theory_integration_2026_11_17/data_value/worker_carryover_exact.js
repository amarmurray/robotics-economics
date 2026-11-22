// Exact synthetic two-site learner/recovery carryover model (no field estimates).
// Execute with: node worker_carryover_exact.js
(() => {
  const S = ["00", "10", "01", "11"];
  let tests = 0, compositions = 0;
  function ok(condition, label) {
    tests += 1;
    if (!condition) throw new Error("Failed: " + label);
  }
  function outcome(mass) {
    const n = mass.reduce((a,b)=>a+b,0), h=mass[1]+mass[3]+mass[5]+mass[7];
    const singleton = mass[2]+mass[3]+mass[4]+mass[5];
    const p=mass[2]+mass[4]; // S2 singleton and recovery operator free
    let future4=0;
    for(let i=0;i<4;i++)for(let busy=0;busy<2;busy++) {
      const m=mass[2*i+busy];
      const value4=busy ? 18 : (i===1||i===2 ? 25 : 20);
      future4 += m*value4; // t2 + t3 production in quarter-units
    }
    const b4n=7*n+future4, r4n=28*n;
    const j8n=24*n+Math.max(r4n,b4n); // L=.5; failed L branch value 6
    const formula4n=27*n-2*h+5*p;
    ok(future4===20*n-2*h+5*p,"statewise Bellman decomposition");
    ok(b4n===formula4n,"pilot Bellman value");
    ok(j8n===24*n+Math.max(r4n,formula4n),"full adaptive program");
    ok(p>=Math.max(0,singleton-h)&&p<=Math.min(singleton,n-h),"Fréchet support");
    ok(j8n>=52*n,"free optional retained controller");
    return {n,h,singleton,p,b4n,r4n,j8n,den:8*n};
  }
  function visit(k,left,row) {
    if(k===1) {
      const m=[...row,left]; outcome(m); compositions++; return;
    }
    for(let x=0;x<=left;x++)visit(k-1,left-x,[...row,x]);
  }
  visit(8,4,[]);
  ok(compositions===330,"all 8-cell integer laws of total mass 4");
  function world(busySet) {
    const m=[];
    for(let i=0;i<4;i++) {
      const isBusy=busySet.includes(S[i]);
      m.push(isBusy?0:1,isBusy?1:0);
    }
    return outcome(m);
  }
  const diversified=world(["00","11"]);
  const synchronized=world(["10","01"]);
  ok(diversified.h===2&&diversified.singleton===2&&diversified.p===2,"diversified marginals");
  ok(synchronized.h===2&&synchronized.singleton===2&&synchronized.p===0,"synchronized marginals");
  ok(diversified.b4n===114 && diversified.j8n===210,"diversified full program 105/16");
  ok(synchronized.b4n===104 && synchronized.j8n===208,"synchronized full program 13/2");
  ok(synchronized.j8n<209&&diversified.j8n>209,"E=209/32 between the two P values");
  const result={
    schema:"worker-carryover-synthetic-v1",
    legal_filtration:"t1 knows L only; t2 observes S2,H2; t3 learns S3,H3 before dispatch but not cleared payment",
    input:{Pr_L:"1/2",r1_R:"2",r1_B:"7/4",r2_R:"2",r2_T:"9/4",r3_R:"2",r3_T:"4",Pr_recovery_busy_R:"1/2",Pr_order_after_recovery_R:"1/2",Pr_terminal_paid_eligibility_after_free_R:"1/2"},
    test_summary:{exhaustive_eight_cell_laws:compositions,exact_integer_assertions:tests},
    diversified:{h:"1/2",singleton:"1/2",free_singleton:"1/2",B_complete_if_L:"57/8",P_complete:"105/16"},
    synchronized:{h:"1/2",singleton:"1/2",free_singleton:"0",B_complete_if_L:"13/2",P_complete:"13/2"},
    E_complete:"209/32",
    partial_id:"P in [13/2,105/16] for fixed h=singleton=1/2 and unrestricted joint coupling",
    observed_robotics_data:false
  };
  if(typeof process!=="undefined" && typeof console!=="undefined") console.log(JSON.stringify(result,null,2));
  return result;
})()
