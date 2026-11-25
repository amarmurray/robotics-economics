// Run with Node.js; synthetic exact finite checks, not field data.
function solveChecks(){
  let checks=0,cases=0;const ck=(a,b)=>{checks++;if(Math.abs(a-b)>1e-9)throw Error(JSON.stringify({a,b}))};
  // q = native routine qualification; e = extra retained eligible source record;
  // h = available dated crew slots; f = funded, ready-to-order body.
  function enumerate(p,s){
    let best={value:-Infinity,b:0};
    for(let b=0;b<=1;b++){
      if(b&&(!s.f||s.h<p.dc))continue;
      const routes=[{duration:0,cost:0,ready:s.q}];
      if(s.e)routes.push({duration:p.dg,cost:p.g,ready:true});
      routes.push({duration:p.dx,cost:p.x,ready:true});
      for(const r of routes){
        if(r.duration+b*p.dc>s.h)continue;
        for(let a=0;a<=1;a++)for(let z=0;z<=1;z++){
          if(a+z>1+b||z&&!r.ready)continue;
          const value=a*p.u+z*p.v-r.cost-b*p.c;
          if(value>best.value+1e-9||(Math.abs(value-best.value)<1e-9&&b<best.b))best={value,b};
        }
      }
    }
    return best;
  }
  function formula(p,s){
    const route=b=>s.q?0:Math.min(s.e&&s.h-b*p.dc>=p.dg?p.g:Infinity,s.h-b*p.dc>=p.dx?p.x:Infinity);
    const v0=p.u+Math.max(0,p.v-p.u-route(0));
    const v1=s.f&&s.h>=p.dc?p.u+Math.max(0,p.v-route(1))-p.c:-Infinity;
    return {value:Math.max(v0,v1),b:Number(v1>v0)};
  }
  for(let u=1;u<=4;u++)for(let v=1;v<=6;v++)for(let c=1;c<=4;c++)for(let g=0;g<=2;g++)for(let x=g;x<=3;x++)for(let dg=1;dg<=2;dg++)for(let dx=dg;dx<=3;dx++)for(let dc=1;dc<=2;dc++){
    const p={u,v,c,g,x,dg,dx,dc};
    for(let h=0;h<=6;h++)for(let q=0;q<=1;q++)for(let e=0;e<=1;e++)for(let f=0;f<=1;f++){
      const s={h,q,e,f}; const a=enumerate(p,s), b=formula(p,s); cases++;ck(a.value,b.value);ck(a.b,b.b);
      if(g<x&&x<v-u&&0<c&&c<u){
        const pred=Number(f&&(q?h>=dc:h>=dc+dx||e&&h>=dc+dg));ck(b.b,pred);
        const d=formula(p,{...s,e:1}).b-formula(p,{...s,e:0}).b;
        ck(d,Number(f&&!q&&h>=dc+dg&&h<dc+dx));
      }
    }
  }
  const p={u:4,v:10,c:2,g:1,x:3,dg:1,dx:2,dc:1};
  const table=Array.from({length:4},(_,h)=>[0,1].map(e=>formula(p,{h,e,q:0,f:1})));
  const gain=table.map(row=>row[1].value-row[0].value);[0,5,4,2].forEach((x,i)=>ck(gain[i],x));
  const mean=(h,e)=>({value:(1-e)*table[h][0].value+e*table[h][1].value,b:(1-e)*table[h][0].b+e*table[h][1].b});
  const witness={repair_release:{baseline:mean(1,1),routine:{...mean(2,.25),value:mean(2,.25).value+.5},instrumented:{...mean(2,.75),value:mean(2,.75).value+.5-.5}},repair_no_dated_release:{baseline:mean(2,1),routine:{...mean(2,.25),value:mean(2,.25).value+4},instrumented:{...mean(2,.75),value:mean(2,.75).value+4-3}}};
  ck(witness.repair_release.baseline.value,9);ck(witness.repair_release.routine.value,8.5);ck(witness.repair_release.instrumented.value,10);ck(witness.repair_release.instrumented.b,.75);ck(witness.repair_no_dated_release.routine.value,12);ck(witness.repair_no_dated_release.routine.b,.25);ck(witness.repair_no_dated_release.instrumented.value,11);
  // Exact sharp overlap bounds under equal-mass finite states, all subsets of evidence.
  let overlapCases=0;for(let n=1;n<=8;n++)for(let w=0;w<=n;w++)for(let e=0;e<=n;e++){
    let min=Infinity,max=-Infinity;for(let mask=0;mask<(1<<n);mask++){let count=0,j=0;for(let i=0;i<n;i++)if(mask&(1<<i)){count++;if(i<w)j++}if(count===e){min=Math.min(min,j);max=Math.max(max,j)}}
    ck(min,Math.max(0,w+e-n));ck(max,Math.min(w,e));overlapCases++;
  }
  // Weighted allocation sharpness (nonuniform gains, including zero).
  let weightedCases=0;for(let n=1;n<=6;n++)for(let code=0;code<3**n;code++){let v=code;const d=Array.from({length:n},()=>{let x=v%3;v=Math.floor(v/3);return x});const sorted=[...d].sort((a,b)=>a-b);
    for(let e=0;e<=n;e++){let min=Infinity,max=-Infinity;for(let mask=0;mask<(1<<n);mask++){let count=0,sum=0;for(let i=0;i<n;i++)if(mask&(1<<i)){count++;sum+=d[i]}if(count===e){min=Math.min(min,sum);max=Math.max(max,sum)}}
      ck(min,sorted.slice(0,e).reduce((a,b)=>a+b,0));ck(max,sorted.slice(n-e).reduce((a,b)=>a+b,0));weightedCases++;
    }
  }
  return {checks,cases,overlapCases,weightedCases,table,gain,witness,scope:"Synthetic exact integer allocation enumeration and arithmetic; no empirical calibration or full CI"};
}
console.log(JSON.stringify(solveChecks(),null,2));
