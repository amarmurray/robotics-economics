"use strict";
// Finite state/action enumeration. All checks use exact integer arithmetic.
const execute = function execute(){
function pc(n){let c=0;while(n){n&=n-1;c++}return c}
function parts(n){const out=[];function rec(i,a,m){if(i===n){out.push(a.slice());return}for(let j=0;j<=m+1;j++){a.push(j);rec(i+1,a,Math.max(m,j));a.pop()}}rec(1,[0],0);return out}
function cover(M){let k=4;for(let s=1;s<8;s++)if(M.every(q=>(q&s)!==0))k=Math.min(k,pc(s));return k}
function works(p,M){const d={};for(let i=0;i<p.length;i++)d[p[i]]=d[p[i]]===undefined?M[i]:(d[p[i]]&M[i]);return Object.values(d).every(x=>x!==0)}
let counts={},profiles=0,checks=0;
for(let n=2;n<=5;n++){const P=parts(n),base=7,N=base**n;let local=0;for(let z=0;z<N;z++){let v=z,M=[];for(let i=0;i<n;i++){M.push(v%base+1);v=Math.floor(v/base)}const k=cover(M);let kp=n+1;for(let p of P){local++;if(works(p,M))kp=Math.min(kp,new Set(p).size)}local++;if(k!==kp)throw new Error(`label mismatch n=${n},z=${z},${k},${kp}`)}profiles+=N;checks+=local;counts[n]={profiles:N,partitions:P.length,assertions:local}}
const triple=[3,6,5];if(cover(triple)!==2||triple.reduce((x,y)=>x&y,7)!==0||!(triple[0]&triple[1])||!(triple[1]&triple[2])||!(triple[0]&triple[2]))throw new Error("triple");checks+=5;
const parity=[1,2,2,1];function val(f){const g=new Map();for(let i=0;i<4;i++){let k=f(i);if(!g.has(k))g.set(k,[]);g.get(k).push(i)}let z=0;for(let I of g.values()){let a=0,b=0;for(let i of I){if(parity[i]&1)a++;if(parity[i]&2)b++}z+=Math.max(a,b)}return z}
let xor={none:val(()=>"all"),first:val(i=>i>>1),second:val(i=>i&1),joint:val(i=>i)};
if(JSON.stringify(xor)!==JSON.stringify({none:2,first:2,second:2,joint:4}))throw new Error("parity");checks+=4;
let sub=0;for(let z=0;z<729;z++){let t=z,Q=[[],[]];for(let i=0;i<2;i++)for(let a=0;a<3;a++){Q[i][a]=t%3;t=Math.floor(t/3)}const f=s=>Q.reduce((v,row)=>{let b=0;for(let a=0;a<3;a++)if(s&(1<<a))b=Math.max(b,row[a]);return v+b},0);for(let S=0;S<8;S++)for(let T=0;T<8;T++)if((S&T)===S){if(f(S)>f(T))throw new Error("nonmonotone");sub++;for(let a=0;a<3;a++)if(!(T&(1<<a))){if(f(S|(1<<a))-f(S)<f(T|(1<<a))-f(T))throw new Error("not submodular");sub++}}}
return {scope:"synthetic finite one-decision program, fixed lawful menus, exogenous context, integer unit payoffs",minimal_paid_report:{all_nonempty_optimal_action_mask_profiles:profiles,exact_assertions:checks,by_state_count:counts,number_candidate_actions:3},three_context_example:{masks:triple,pairwise_common_optima:true,three_way_common_optimum:false,minimum_labels:2,full_paid:"1",no_report_paid:"2/3",lost_paid:"1/3"},complementary_report_fields:{no_report_numerator:xor.none,first_only_numerator:xor.first,second_only_numerator:xor.second,both_numerator:xor.joint,denominator:4,information_value_individual:"0",joint:"1/2"},submodular_oracle_action_label_budget:{q_tables:729,checks:sub,nonnegative_baseline:0},source_type:"artificial payoff and admissible optimal-action set tables",actual_customers:false,actual_field_robot:false,validated_paid_Q:false};
};
const result=execute();
if (typeof module !== "undefined" && require.main === module) console.log(JSON.stringify(result,null,2));
if (typeof module !== "undefined") module.exports={execute};
