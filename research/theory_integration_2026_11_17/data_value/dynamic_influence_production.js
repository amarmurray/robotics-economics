/* Dynamic qualified-production interference certificate.
 * Synthetic, exact rational CPU diagnostic, not field evidence.
 * Execute with Node.js: node dynamic_influence_production.js
 */
"use strict";
function gcd(a,b){while(b!==0n){const c=a%b;a=b;b=c;}return a<0n?-a:a;}
function F(n,d=1n){n=BigInt(n);d=BigInt(d);if(!d)throw Error("zero denom");if(d<0n){n=-n;d=-d;}const g=gcd(n,d);return {n:n/g,d:d/g};}
const Z=F(0),O=F(1);
function add(a,b){return F(a.n*b.d+b.n*a.d,a.d*b.d);}
function neg(a){return F(-a.n,a.d);}
function sub(a,b){return add(a,neg(b));}
function mul(a,b){return F(a.n*b.n,a.d*b.d);}
function div(a,b){return F(a.n*b.d,a.d*b.n);}
function eq(a,b){return a.n===b.n&&a.d===b.d;}
function show(a){return a.d===1n?a.n.toString():a.n.toString()+"/"+a.d.toString();}
function sum(xs){return xs.reduce(add,Z);}
function dot(x,y){return sum(x.map((a,i)=>mul(a,y[i])));}
function matvec(A,v){return A.map(r=>dot(r,v));}
function chk(t,msg){if(!t)throw Error("failed: "+msg);checks++;}
let checks=0;
function construct(A,initial,T=4){
  const q=[Array(initial.length).fill(Z)];
  for(let t=1;t<=T;t++)q.push(t===1?initial:matvec(A,q[t-1]));
  return q;
}
function exposureBound(A,initial,L,T=4){
  const q=construct(A,initial,T);
  const weighted=q.slice(1).map(row=>dot(L,row));
  return {q,weighted,epsilon:sum(weighted)};
}
function compute(){
  checks=0;
  const A=[
    [Z,F(1,4),Z],
    [F(1,5),Z,F(1,10)],
    [Z,F(1,2),Z]
  ];
  const b=[F(1,10),F(1,5),Z];
  const L=[F(2),F(1),F(4)];
  const full=exposureBound(A,b,L);
  const wrongA=A.map(row=>row.slice());wrongA[2][1]=Z;
  const omitted=exposureBound(wrongA,b,L);
  const expectedQ=[
    ["0","0","0"],["1/10","1/5","0"],["1/20","1/50","1/10"],
    ["1/200","1/50","1/100"],["1/200","1/500","1/100"]
  ];
  for(let t=0;t<expectedQ.length;t++)for(let k=0;k<3;k++){chk(show(full.q[t][k])===expectedQ[t][k],"full reachability "+t+","+k);}
  chk(eq(full.epsilon,F(521,500)),"complete dynamic bound");
  chk(eq(omitted.epsilon,F(273,500)),"omitted operator-to-demand edge");
  chk(eq(sub(full.epsilon,omitted.epsilon),F(62,125)),"missing path causes understated bound");
  const D=F(2,5),p=F(1,2);
  const width=mul(sub(O,p),full.epsilon);
  const wrongWidth=mul(sub(O,p),omitted.epsilon);
  chk(eq(width,F(521,1000)),"symmetric I9 width");
  chk(eq(wrongWidth,F(273,1000)),"invalid truncated width");
  chk(eq(sub(D,width),F(-121,1000)),"correct lower remains inconclusive");
  chk(eq(sub(D,wrongWidth),F(127,1000)),"invalid positive certification");
  const base=F(3),u=F(3,4),h=F(1);
  function site(own,other){return add(base,sub(mul(u,F(own)),mul(h,F(own*other))));}
  const incumbent=sum([site(0,0),site(0,0)]);
  const one=sum([site(1,0),site(0,1)]);
  const both=sum([site(1,1),site(1,1)]);
  const ownMixed=sub(add(mul(sub(O,p),sub(site(1,0),site(0,0))),mul(p,sub(site(1,1),site(0,1)))),Z);
  const fullMarket=div(sub(both,incumbent),F(2));
  chk(eq(incumbent,F(6))&&eq(one,F(27,4))&&eq(both,F(11,2)),"whole order policy portfolios");
  chk(eq(ownMixed,F(1,4))&&eq(fullMarket,F(-1,4)),"lagged-edge direct-vs-adoption sign reversal");
  // Same marginals, different joint qualification coupling (binary Q and O).
  const correlated={"00":F(1,2),"11":F(1,2),"01":Z,"10":Z};
  const anti={"00":Z,"11":Z,"01":F(1,2),"10":F(1,2)};
  function marg(law,idx){return sum(Object.entries(law).filter(([key])=>key[idx]==="1").map(([,v])=>v));}
  for(let i=0;i<2;i++)chk(eq(marg(correlated,i),F(1,2))&&eq(marg(anti,i),F(1,2)),"matching marginal kernel "+i);
  chk(eq(correlated["11"],F(1,2))&&eq(anti["11"],Z),"joint accepted recipe not marginal-identified");
  return {
    label:"Entirely synthetic structural diagnostics; no empirical certificate",
    dynamic_example:{
      components:["qualified-controller state Q","shared operator O","customer original-demand D"],
      q_by_time:full.q.map(r=>r.map(show)),
      weighted_complete_service_by_time:full.weighted.map(show),
      correct_exposure_bound:show(full.epsilon),
      operator_demand_edge_omitted_bound:show(omitted.epsilon),
      understatement:show(sub(full.epsilon,omitted.epsilon)),
      hypothetical_site_direct_D:show(D),
      p:show(p),
      valid_market_T_interval:[show(sub(D,width)),show(add(D,width))],
      invalid_omitted_edge_interval:[show(sub(D,wrongWidth)),show(add(D,wrongWidth))]
    },
    lagged_spillover_counterexample:{
      incumbent_market:show(incumbent),one_site_source:show(one),universal_source:show(both),
      randomized_own_site_direct:show(ownMixed),whole_market_per_site:show(fullMarket)
    },
    joint_kernel_counterexample:{
      each_binary_marginal:"1/2 under both laws",qualified_complete_recipe_correlated:"1/2",
      qualified_complete_recipe_anticorrelated:"0"
    },
    checks
  };
}
if(typeof module!=="undefined"&&require.main===module){process.stdout.write(JSON.stringify(compute(),null,2)+"\n");}
