'use strict';
function ok(v,s){if(!v)throw new Error(s);}
function bounds(p,c,N){let lo=0,hi=0,ma=0,sum=0;for(let i=0;i<c.length;i++){ma=Math.max(ma,p[i]);sum+=p[i];const diff=c[i]-(c[i+1]||0);lo+=diff*ma;hi+=diff*Math.min(N,sum);}return [lo,hi];}
function audit(){
 const N=8,c=[6,4,2],a=new Array(8).fill(0),groups=new Map();let laws=0;
 function record(){laws++;const p=c.map((_,i)=>a.reduce((s,n,mask)=>s+((mask&(1<<i))?n:0),0)),key=p.join(',');
  const v=a.reduce((s,n,mask)=>{let best=0;for(let j=0;j<c.length;j++)if(mask&(1<<j))best=Math.max(best,c[j]);return s+n*best;},0);
  const x=groups.get(key);if(!x)groups.set(key,[v,v]);else{x[0]=Math.min(x[0],v);x[1]=Math.max(x[1],v);}
 }
 function rec(i,left){if(i===7){a[7]=left;record();return;}for(let z=0;z<=left;z++){a[i]=z;rec(i+1,left-z);}}
 rec(0,N);let checks=0;
 for(const [key,observed]of groups){const predicted=bounds(key.split(',').map(Number),c,N);ok(predicted[0]===observed[0]&&predicted[1]===observed[1],key);checks++;}
 ok(laws===6435&&checks===729,'coverage');
 const x0=5,xHalf=3,g=4,e=2,r=2;
 ok(bounds([4,4],[6,4],8).join(',')==='24,40','two buyer');ok((x0+xHalf)/2===g &&(Math.max(x0,g,e,r)+Math.max(xHalf,g,e,r))/2===4.5,'value of information');
 return {joint_laws_enumerated:laws,marginal_vectors_verified:checks,one_slot_numerator_bounds_at_p_half:[24,40],source_X_disjoint:x0,source_X_nested:xHalf,grounding_G:g,embodiment_E:e,retained_R:r,investment_crossover_joint_probability:0.25,no_signal_expected_best:4,perfect_paired_report_expected_best:4.5,gross_information_option:0.5,field_calibrated:false};
}
const result=audit();
if(typeof module!=='undefined'&&require.main===module)console.log(JSON.stringify(result,null,2));
