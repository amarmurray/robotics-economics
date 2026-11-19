// Reproducible, self-contained Node.js exact-tick diagnostic; no external packages.
// All table inputs are synthetic; integer arithmetic until display output.
const result=(function run() {
  let checks=0;
  function ok(v,why){checks++;if(!v)throw Error("FAILED "+why)}
  const A=["I","Z","X","G","E"];
  const pay={I:[40,40],Z:[120,-80],X:[130,-70],G:[140,-120],E:[80,60]};
  const gross={I:[40,40],Z:[120,-80],E:[100,80],G:[160,-100]};
  function best(p,d,table=pay){
    let winner=null,val=-Infinity;
    for(const a of Object.keys(table)){
      const v=table[a][0]*p+table[a][1]*(d-p);
      if(v>val){val=v;winner=a}
    }
    return {action:winner,numerator:val};
  }
  function audit(p,d){
    const hi=best(p,d),lo=best(d-p,d);
    return {high:hi.action,low:lo.action,score20_num:-8*d+hi.numerator+lo.numerator,score20_den:2*d};
  }
  function eqR(x,y){return 20+(2*(pay[x][0]+pay[x][1])+3*(pay[y][0]+pay[y][1]))/10}
  let ra={v:-Infinity},aa={v:-Infinity},policyCount=0;
  for(const h of A){for(const l of A){
    policyCount++;
    const vA=-4+(pay[h][0]+pay[l][1])/2;
    const vR=eqR(h,l);
    if(vA>aa.v)aa={v:vA,high:h,low:l};
    if(vR>ra.v)ra={v:vR,selected:h,missing:l};
  }}
  ok(policyCount===25,"25 rules");
  ok(aa.v===96&&aa.high==="G"&&aa.low==="E","perfect audit optimum");
  ok(ra.v===90&&ra.selected==="E"&&ra.missing==="E","selected routine optimum");
  ok(20+(best(180,180).numerator+best(0,180).numerator)/(2*180)===120,"perfect routine signal");
  const samples=[[90,180,"E","E"],[130,180,"X","E"],[144,180,"X","E"],[150,180,"X","E"],[171,180,"G","E"],[180,180,"G","E"]];
  const auditGrid=[];
  for(const [n,d,h,l] of samples){
    const r=audit(n,d);
    ok(r.high===h&&r.low===l,`q=${n}/${d} policy ${h}/${l}`);
    const val=(r.score20_num/r.score20_den)/20;
    auditGrid.push({accuracy:`${n}/${d}`,high:r.high,low:r.low,value:Number(val.toFixed(8))});
  }
  ok(auditGrid[0].value===3.3,"uninformative audit");
  ok(auditGrid[2].value===3.65,"80 percent audit");
  ok(auditGrid[3].value===3.8,"5/6 audit tie");
  ok(auditGrid[4].value===4.5,"95 percent audit break even");
  ok(auditGrid[5].value===4.8,"perfect audit");
  const information={};
  for(const [name,acts,expected] of [["incumbent",["I","Z"],40],["new_embodiment",["I","Z","E"],10],["new_grounding",["I","Z","G"],60]]){
    const t=Object.fromEntries(acts.map(a=>[a,gross[a]]));
    const no=best(1,2,t).numerator/2;
    const yes=(best(1,1,t).numerator+best(0,1,t).numerator)/2;
    ok(yes-no===expected,`menu value-of-information ${name}`);
    information[name]={no_signal:no/20,perfect_signal:yes/20,information_value:(yes-no)/20};
  }
  ok(Math.abs((3/5)*(2/3)-2/5)<1e-12 && (2/5)*1===2/5,"selected high events equal");
  ok(4+20<=24 && 20<=24,"budget covers audit and grounding");
  for(let n=90;n<=180;n++){
    const x=audit(n,180);
    const h=n<=130?"E":n<=150?"X":"G";
    if(n===130||n===150){ok(["X","E","G"].includes(x.high),"ties at thresholds");}
    else ok(x.high===h,`piecewise optimal high action n=${n}`);
    ok(x.low==="E",`piecewise optimal low action n=${n}`);
    const sign=x.score20_num-90*x.score20_den;
    ok((n>171&&sign>0)||(n===171&&sign===0)||(n<171&&sign<0),`audit versus routine threshold n=${n}`);
  }
  return {model:"two-date, retained qualified production, synthetic and uncalibrated",units:"one unit = twenty score ticks",budget_units:1.2,actions:A,terminal_net_payoffs_in_twentieths:pay,selected_log_law:"P(recorded high|H)=P(recorded high|L)=2/5; selected lows=0; no record=3/5",routine_100_selected_logs_value:ra.v/20,perfect_audit_value:aa.v/20,perfect_routine_info_value:6,perfect_audit_policy:aa,unobserved_log_policy:ra,audit_accuracy_grid:auditGrid,qualification_menu_info_value:information,decision_thresholds:{source_vs_embodiment:"13/18",grounding_vs_source:"5/6",audit_vs_productive_routine:"19/20"},tested_assertions:checks};
})();
console.log(JSON.stringify(result,null,2));
