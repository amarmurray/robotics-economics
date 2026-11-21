/* Conditional cross-arm joint qualification and buyer demand. Run: node joint_qualification_cross_arm.js */
const run = function run(){
 const T=[[0,0,0,0],[0,0,0,1],[0,1,0,1],[0,0,1,1],[0,1,1,1],[1,1,1,1]];
 const M=[T[0],T[2],T[3],T[5]];
 const witnesses={
  monotone_low:{types:T,atoms:[[0,0,1],[0,2,2],[0,3,2],[0,5,3],[1,0,2],[4,0,1],[4,5,1],[5,0,4],[5,5,4]],expected_h11:5},
  monotone_high:{types:T,atoms:[[0,0,5],[0,5,3],[1,4,2],[4,1,1],[4,5,1],[5,0,3],[5,1,1],[5,5,4]],expected_h11:9},
  modular_low:{types:M,atoms:[[0,0,2],[0,1,2],[0,2,2],[0,3,2],[1,0,1],[1,3,1],[2,0,1],[2,3,1],[3,0,4],[3,3,4]],expected_h11:6},
  modular_high:{types:M,atoms:[[0,0,5],[0,3,3],[1,2,2],[2,1,1],[2,3,1],[3,0,3],[3,1,1],[3,3,4]],expected_h11:9}
 };
 let checked=0;
 const ensure=(cond,msg)=>{checked++;if(!cond)throw Error(msg)};
 let result={};
 for(const [key,w] of Object.entries(witnesses)){
  const pa=[0,0,0,0],pb=[0,0,0,0],h=[0,0,0,0];
  const n=w.atoms.reduce((v,atom)=>v+atom[2],0);ensure(n===20,key+" mass");
  for(const [i,j,mass] of w.atoms){
   for(let z=0;z<4;z++){pa[z]+=mass*w.types[i][z];pb[z]+=mass*w.types[j][z];h[z]+=mass*w.types[i][z]*w.types[j][z]}
  }
  ensure(JSON.stringify(pa)===JSON.stringify([8,10,10,12]),key+" A marginals");
  ensure(JSON.stringify(pb)===JSON.stringify([8,10,10,12]),key+" B marginals");
  ensure(JSON.stringify(h.slice(0,3))===JSON.stringify([4,5,5]),key+" R/S/G joint");
  ensure(h[3]===w.expected_h11,key+" SG joint");
  const netSGnumeratorOver20=28+8*h[3]; // 7/5 + 8h, scaled by 20
  result[key]={joint_qualification_numerators_over20:h,net_SG_numerator_over20:netSGnumeratorOver20,embodiment_E_numerator_over20:80};
 }
 for(const f of T){for(const g of T){
  const h=f.map((x,z)=>x*g[z]);
  ensure(h[3]>=h[1]&&h[3]>=h[2],"monotone joint lower");
  for(const z of [1,2])ensure(h[3]<=h[z]+f[3]-f[z]+g[3]-g[z],"monotone union upper");
 }}
 for(const f of M){for(const g of M){
  const h=f.map((x,z)=>x*g[z]);ensure(h[3]+h[0]>=h[1]+h[2],"pathwise lattice joint lower");
 }}
 // hSG=9/20, pA=pB=3/5. For bundle F=(0,2,2,12), gross=6.
 const bundleGrossNumeratorOver20=2*12+2*12+8*9;
 ensure(bundleGrossNumeratorOver20===120,"bundle gross 6");
 // Single slot F=(0,2,2,2), gross=3/2.
 const singleGrossNumeratorOver20=2*12+2*12-2*9;
 ensure(singleGrossNumeratorOver20===30,"single-slot gross 3/2");
 // 3/4 bundle + 1/4 single -> gross 39/8? 0.75*6+0.25*1.5=39/8.
 ensure(3*bundleGrossNumeratorOver20+singleGrossNumeratorOver20===390,"mixture gross 39/8 scaled /80");
 const mixedNetNumeratorOver8=39-8;
 ensure(mixedNetNumeratorOver8===31 && mixedNetNumeratorOver8<32,"SG mixture loses to E net4");
 return {type:"conditional_exact_model_not_empirical",denominator:20,arms:["R","S","G","SG"],witnesses:result,identified_sets:{marginal_only:"[1/5,3/5]",pathwise_task_monotone:"[1/4,9/20]",pathwise_task_modular:"[3/10,9/20]"},economic:{high_SG_net:"5",modular_low_SG_net:"19/5",monotone_low_SG_net:"17/5",E_only_net:"4",bundle_gross:"6",single_slot_gross:"3/2",mixed_3_4_bundle_gross:"39/8",mixed_SG_net:"31/8"},finite_response_pairs_checked:{monotone:36,modular:16},exact_integer_assertions:checked,limitations:["Hypothetical qualification response types and signed production contributions only","No field learner, paid customer receipts, signed comparative policies, numerical industry network or independent novelty validation"]};
};
const result=run();
if(typeof module !== 'undefined' && module.exports)module.exports={run};
if(typeof require !== 'undefined' && require.main===module)console.log(JSON.stringify(result,null,2));
