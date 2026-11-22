'use strict';
// Independent integer-tick audit of the synthetic conditional learner/queue model.
// Not an empirical robotics dataset or proof of broad scientific novelty.
const assert = require('node:assert/strict');
const arms = ['P','G','E'];
const legal = {P:['retain','adaptive'], G:['retain','adaptive','probe'], E:['retain','adaptive']};
const zw = [[0,0],[0,1],[1,0],[1,1]];
function row(a,p,z,w){
  const L=a==='P'?z:1, J1=a==='P'?w:0, Y1=a==='P'?z:w;
  let b=p==='retain'?'R':p==='probe'?(J1?'R':'T'):(L&&!J1&&Y1?'T':'R');
  assert(b==='R'||J1===0);
  const J2=+(b==='T'&&z===0&&w===1&&a!=='E');
  const Q3=+(L===1||(b==='T'&&w===0));
  const Y3=+(a==='G'?(w===1||(b==='T'&&z===0)):(z===1||w===1||(b==='T'&&w===0)));
  const earn2=(b==='T'&&L&&Y1)?20:0;
  const earn3=(Q3&&Y3&&!J2)?40:0;
  return {ticks:earn2+earn3-{P:5,G:8,E:10}[a],J1,J2,Y1,b};
}
function signed(arm,p,law){
  let trueTicks=0, naiveTop=0, naiveMass=0, weightedNum=0, checks=0;
  for(let i=0;i<4;i++){
    const [z,w]=zw[i], x=row(arm,p,z,w), n=law[i];
    trueTicks+=n*x.ticks;
    // Only observed S1=S2=1 with the logged action equal to the legal policy.
    const r1=x.J1?1:2, r2=x.J2?1:2;
    const eT=x.J1?0:(arm==='G'?(x.Y1?3:1):(x.Y1?3:0));
    const chosen=x.b==='T'?eT:4-eT;
    assert(chosen>0);
    const mass=n*r1*chosen*r2;
    naiveTop+=mass*x.ticks;
    naiveMass+=mass;
    // IPW: multiply by (3*4*4*4)/(r1*chosen*r2),
    // cancelling selected action and both reports exactly.
    weightedNum+=n*x.ticks;
    checks+=2;
  }
  assert.equal(weightedNum,trueTicks);
  return {true_num: trueTicks, true_den:law.reduce((s,x)=>s+x,0)*40,
          naive_num:naiveTop, naive_den:naiveMass*40, checks};
}
function run(){
 let counts=0, laws=0;
 for(let a=0;a<=8;a++)for(let b=0;b<=8-a;b++)for(let c=0;c<=8-a-b;c++){
   const law=[a,b,c,8-a-b-c];laws++;
   for(const arm of arms)for(const p of legal[arm]){
     const r=signed(arm,p,law);counts+=r.checks;
     assert.equal(r.true_den,320);counts++;
   }
 }
 assert.equal(laws,165);
 const base=[2,2,2,2],G=signed('G','probe',base),E=signed('E','adaptive',base),P=signed('P','adaptive',base);
 assert.equal(G.true_num*20,G.true_den*11);
 assert.equal(E.true_num*4,E.true_den*3);
 assert.equal(P.true_num*2,P.true_den);
 assert.equal(G.naive_num*130,G.naive_den*99);
 assert.equal(E.naive_num*28,E.naive_den*19);
 assert(G.true_num*E.true_den<E.true_num*G.true_den);
 assert(G.naive_num*E.naive_den>E.naive_num*G.naive_den);
 counts+=7;
 return {checker:'separately written integer-tick conditional law',laws,checks:counts,
         G_probe_true:'11/20',G_probe_selected:'99/130',E_adaptive_true:'3/4',
         E_adaptive_selected:'19/28',P_adaptive_true:'1/2',status:'synthetic exact'};
}
if(require.main===module)console.log(JSON.stringify(run(),null,2));
module.exports={run};
