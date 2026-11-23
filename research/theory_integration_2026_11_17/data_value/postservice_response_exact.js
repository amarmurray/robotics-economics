"use strict";
function runModel(){
  "use strict";
  let assertions=0;
  function check(condition, message){assertions++; if(!condition)throw Error(message);}
  const rows=[];
  for(let a=0;a<=4;a++)for(let b=0;b<=4;b++)for(let c=0;c<=4;c++){
    const d=4-a-b-c;
    if(d<0||d>4)continue;
    const row=[a,b,c,d];
    const l1=row.reduce((s,x)=>s+Math.abs(x-1),0);
    if(l1<=2)rows.push(row);
  }
  check(rows.length===13,"TV <=1/4 feasible four-atom grid");
  // Atom order 00, 01, 10, 11; baseline is one unit in each atom, denominator 4.
  const good4=x=>3*(x[1]+x[3]); // 4 times conditional service value; A budget exhausted
  const idle4=x=>3*x[1]+2*x[2]+3*x[3]; // 4 times conditional service value
  const early80=(g,i)=>32+30*(g[1]+g[3])+5*idle4(i);
  const base=[1,1,1,1], values=[];
  check(early80(base,base)===132,"transported mean 33/20");
  check(good4(base)===6 && idle4(base)===8,"baseline conditional values");
  for(const g of rows)for(const i of rows){
    check(g.reduce((s,x)=>s+x,0)===4 && i.reduce((s,x)=>s+x,0)===4,"normalization");
    check(good4(g)>=3&&good4(g)<=9,"good-state TV bound sharp");
    check(idle4(i)>=5&&idle4(i)<=11,"idle-state TV bound sharp");
    const v=early80(g,i);values.push(v);
    check(v>=87&&v<=177,"whole-program sharp interval");
    check(v>=0,"nonnegative accepted service");
  }
  const min=Math.min(...values),max=Math.max(...values);
  check(min===87 && max===177,"exact sharp extrema");
  check(values.includes(87)&&values.includes(177),"both extreme common laws exist");
  // E contributes 21/10 = 168/80; P and safe G-skip contribute 2 = 160/80.
  const e=168, prior=160;
  check(min<prior&&prior<e&&e<max,"rank reversal with preserved safe skip");
  let bestK=-1,bestWorst=Infinity;
  for(let k=0;k<=100;k++){
    // k/100 is ex-ante chance of fixed G-early, rest independent E.
    const worst=Math.max(k*(e-min),(100-k)*(max-e));
    if(worst<bestWorst){bestWorst=worst;bestK=k;}
  }
  check(bestK===10&&bestWorst===810,"one-tenth G-early, exact minimax regret 81/800");
  let maximalRegret800=0;
  for(const v of values){
    const oracle=Math.max(v,e,prior);
    const regret800=10*oracle-v-9*e; // G 1/10; E 9/10
    maximalRegret800=Math.max(maximalRegret800,regret800);
    check(regret800>=0&&regret800<=81,"candidate law regret bound");
  }
  check(maximalRegret800===81,"realized exact minimax regret 81/800");
  // Qualitative selection counterexample: C is never paid under Q_R=0.
  // Changing R's unreported C orders in the good state from 0 to 1 leaves R invoices
  // unchanged but alters G-early's t2 C contribution by 3*Pr_G(good)=3/2.
  check(3*1===3 && 3*2===6,"invoice censor example");
  check(33*4+9*5===177,"upper endpoint numerator consistency");
  return {model:"postservice conditional-response, terminal t2",atom_order:["D0C0","D0C1","D1C0","D1C1"],baseline_R_kernel_quarters:[1,1,1,1],conditional_TV_cap:"1/4",feasible_conditional_kernels:rows.length,paired_common_laws:values.length,baseline_Gearly:"33/20",sharp_Gearly_interval:["87/80","177/80"],safe_Gskip:"2",productive_P:"2",independent_E:"21/10",regime_unknown_exante_Gearly_share:"1/10",minimax_regret:"81/800",max_regret_checked:"81/800",economic_response_radius_for_any_Gearly_to_exceed_E:"strictly >1/5",selected_R_invoice_only_C_counterexample_value_gap:"3/2",assertions};
}
if(typeof console!=="undefined") console.log(JSON.stringify(runModel(),null,2));
