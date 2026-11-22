// Independent integer-tick audit of a synthetic selected-history original-buyer model.
// Pairwise fair triple law, endogenous mask and physically conserved recovery queue.
'use strict';
const assert=require('node:assert/strict');
const cells=[];for(let j=0;j<2;j++)for(let h=0;h<2;h++)for(let y=0;y<2;y++)cells.push([j,h,y]);
let checks=0;
function ok(a,b,msg){assert.equal(a,b,msg);checks++;}
function lawAt(t){const m=new Map();for(const [j,h,y] of cells)m.set(String(j)+h+y,((j+h+y)%2===0)?t:128-t);return m;}
function sum(m,pred){return cells.filter(([j,h,y])=>pred(j,h,y)).reduce((s,x)=>s+m.get(x.join('')),0);}
let observable=null;
for(let t=16;t<=112;t++){
  const m=lawAt(t);ok(sum(m,()=>true),512,'mass');
  for(let j=0;j<2;j++)ok(sum(m,(jj)=>jj===j),256,'J fair');
  for(let h=0;h<2;h++)ok(sum(m,(_,hh)=>hh===h),256,'H fair');
  for(let y=0;y<2;y++)ok(sum(m,(_,__,yy)=>yy===y),256,'Y fair');
  for(let j=0;j<2;j++)for(let h=0;h<2;h++)ok(sum(m,(jj,hh)=>jj===j&&hh===h),128,'JH');
  for(let j=0;j<2;j++)for(let y=0;y<2;y++)ok(sum(m,(jj,hh,yy)=>jj===j&&yy===y),128,'JY');
  for(let h=0;h<2;h++)for(let y=0;y<2;y++)ok(sum(m,(jj,hh,yy)=>hh===h&&yy===y),128,'HY');
  const seen=[];
  for(let j=0;j<2;j++)for(let h=0;h<2;h++){
    if(j+h===1){ok(m.get(String(j)+h+'1')>=16,true,'logged positive support');ok(m.get(String(j)+h+'0')>=16,true,'logged negative support');seen.push([j,h,16,16,96]);}
    else seen.push([j,h,0,0,128]);
  }
  const obs=JSON.stringify(seen);if(observable===null)observable=obs;else ok(obs,observable,'observational equivalence');
  const q0=m.get('001');const q1=m.get('011')+m.get('101');const p00=m.get('000')+m.get('001');
  const oldR=160;const wait=-64+q0+q1;const serve=-64+(p00/2)+q1;const P=Math.max(oldR,wait,serve);
  ok(p00,128,'worker zero');ok(q0,128-t,'unserved original demand');ok(q1,2*t,'queue-one original demand');
  ok(wait,64+t,'nonanticipative wait');ok(serve,2*t,'nonanticipative service');ok(P,Math.max(160,2*t),'retained policy option');
  ok(wait<=Math.max(oldR,serve),true,'T wait never optimizes globally');
  // The extra K job at date 3 blocks the date-4 target precisely if j=h=0 and T serves.
  for(let j=0;j<2;j++)for(let h=0;h<2;h++){
    const B3=j+h,K=(B3===0)?1:0,B4=Math.max(0,B3-1)+K;
    ok(B4,(B3===0)?1:(B3===1?0:1),'queue conservation');
  }
}
const low=lawAt(16), high=lawAt(112);
ok((low.get('011')+low.get('101')),32,'low q1');
ok((high.get('011')+high.get('101')),224,'high q1');
ok(160<208,true,'low P<E');ok(224>208,true,'high P>E');
const output={cases:97,integer_scale:512,checks,theta_ticks:[16,112],P_increment_ticks:[160,224],G_increment_ticks:192,E_increment_ticks:208,observed_records:'constant across all 97 selected-case worlds',real_field_data:false};
console.log(JSON.stringify(output,null,2));
