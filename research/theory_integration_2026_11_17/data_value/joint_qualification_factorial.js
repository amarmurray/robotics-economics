/* Private research: factorial economic value under joint qualification.
 * Node JS; synthetic dyadic-rational model, NOT robotics data.
 * All distributions/outcomes use integer quarter units.
 */
"use strict";
const SIGN=[1,-1,-1,1];
let checks=0;
function ok(cond,msg){checks++;if(!cond)throw new Error(msg);}
function dist(t){ok(Number.isInteger(t)&&t>=0&&t<=2,"joint mass");return [t,2-t,2-t,t];}
function dot(a,b){return a.reduce((s,x,i)=>s+x*b[i],0);}
function calc(ts,fs,cs=[0,0,0,0]){
  const ps=ts.map(dist),js=ps.map((p,z)=>dot(p,fs[z])-cs[z]);
  const total=dot(SIGN,js);
  const learning=fs[0].reduce((sum,v,q)=>sum+v*SIGN.reduce((s,sgn,z)=>s+sgn*ps[z][q],0),0);
  const response=SIGN.reduce((sum,sgn,z)=>sum+sgn*dot(ps[z],fs[z].map((v,q)=>v-fs[0][q])),0);
  const cost=-dot(SIGN,cs);
  ok(total===learning+response+cost,"exact decomposition");
  return {total,learning,response,cost,armValues:js};
}
function permutations(a){
  if(!a.length)return [[]];
  return a.flatMap((x,i)=>permutations(a.filter((_,j)=>i!==j)).map(rest=>[x,...rest]));
}
function run(){
  const f=[0,0,0,4],same=[f,f,f,f];
  for(let t=0;t<=2;t++){const p=dist(t);ok(dot(p,[1,1,1,1])===4,"total mass");
    ok(p[1]+p[3]===2&&p[2]+p[3]===2,"fixed qualification marginals");}
  const positive=calc([1,1,1,2],same),negative=calc([1,1,1,0],same);
  ok(positive.total===4&&negative.total===-4,"opposite economic interaction at equal technical marginals");
  const network=calc([1,1,1,2],[f,f,f,[0,0,0,2]]);
  ok(network.learning===4&&network.response===-4&&network.total===0,"production response cancels qualification effect");
  function det(v){return v[3]-v[1]-v[2]+v[0];}
  ok(det([0,0,0,3])===3,"bundle complementarity");
  ok(det([0,1,1,1])===-1,"resource substitution");
  ok(det([2,2,2,1])===-1,"whole-service order displacement");
  const tables=[
    [f,f,f,f],
    [f,f,f,[0,0,0,2]],
    [[1,0,2,4],[2,1,1,4],[0,1,2,3],[2,0,1,5]]
  ];
  let cases=0;
  for(const fs of tables)
    for(let a=0;a<=2;a++)for(let b=0;b<=2;b++)
      for(let c=0;c<=2;c++)for(let e=0;e<=2;e++){
        calc([a,b,c,e],fs,[0,1,0,2]);cases++;
      }
  ok(cases===243,"three service response structures times 81 joint laws");
  const Y=[[0,1,2,4],[1,2,2,3],[3,1,4,5],[2,0,1,3]];
  const assignments=permutations([0,1,2,3]);
  ok(assignments.length===24,"balanced design permutations");
  const sumEstimate=assignments.reduce((s,az)=>s+az.reduce((v,z,i)=>v+SIGN[z]*Y[i][z],0),0);
  const sumPotential=Y.reduce((s,row)=>s+dot(SIGN,row),0);
  ok(4*sumEstimate===24*sumPotential,"balanced randomized contrast unbiased");
  const mu=[0,1,2].map(z=>Y.reduce((s,row)=>s+row[z],0)/4);
  const missing11=[0-mu[1]-mu[2]+mu[0],5-mu[1]-mu[2]+mu[0]];
  ok(missing11[1]-missing11[0]===5,"unsupported arm preserves worst-case interval");
  return {
    assertions:checks,
    arithmetic:"exact integers in quarter units; illustrative, no field observations",
    identicalMarginalsDifferentInteraction:{positive:positive.total/4,negative:negative.total/4},
    economicDecomposition:{qualification:network.learning/4,serviceResponse:network.response/4,total:network.total/4,eachArm:network.armValues.map(v=>v/4)},
    productionCounterexamples:{complementaryBundle:3,substitution:-1,originalOrderDisplacement:-1},
    exactJointDistributionCases:cases,
    randomizedWholeNetwork:{assignments:24,averageEstimate:sumEstimate/24,populationContrast:sumPotential/4},
    missingApproved11Arm:missing11,
    fieldValidation:false
  };
}
if(typeof module!=="undefined"&&require.main===module)console.log(JSON.stringify(run(),null,2));
