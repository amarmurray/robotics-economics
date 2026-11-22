// Conditional P/G/E structural-zero model. Node.js 18+; source function executed in research run.
function exactSupportZeroAuditModel(){
  const must=(condition,msg)=>{if(!condition) throw new Error(msg)};
  let checked=0,cases=0;
  const ext={P:[1e5,-1e5],G:[1e5,-1e5],E:[1e5,-1e5],GminusP:[1e5,-1e5]};
  let witnesses={};
  for(let k=0;k<=8;k++){
    const p16=4+k;
    for(let j=0;j<=p16;j++){
      const P=10*(p16-2);                   // denominator 160
      const Gsafe=5*(p16-2);               // p/2 - 1/16
      const Gprobe=5*(2*j-3);              // theta - 3/32
      const G=Math.max(Gsafe,Gprobe), E=72; // 9/20
      const obj={P,G,E,GminusP:G-P};
      cases++;
      for(const [key,value] of Object.entries(obj)){
        ext[key][0]=Math.min(ext[key][0],value);
        ext[key][1]=Math.max(ext[key][1],value);
        must(Number.isInteger(value),`fraction ticks nonintegral ${key}`);
        checked++;
      }
      must(j<=p16 && p16>=4 && p16<=12,"wrong physical joint buyer/capacity support");checked++;
      must(G>=Gsafe && G>=Gprobe,"option not preserved");checked++;
      if((k===0&&j===0)||(k===8&&j===12)||(k===8&&j===0)){
        const winner=Object.entries({P,G,E}).sort((a,b)=>b[1]-a[1])[0][0];
        witnesses[`${k}_${j}`]={p:`${p16}/16`,theta:`${j}/16`,values_160:{P,G,E},winner};
      }
    }
  }
  const expected={P:[20,100],G:[10,105],E:[72,72],GminusP:[-50,5]};
  for(const key of Object.keys(expected)){must(ext[key].join(",")===expected[key].join(","),`sharp ${key} ${ext[key]}`);checked++;}
  must(cases===81,"wrong grid size");checked++;
  must(witnesses["0_0"].winner==="E" && witnesses["8_0"].winner==="P" && witnesses["8_12"].winner==="G","witness winners");checked++;
  const weights=[6,4,3,1],costs=[99,1,1,1],budget=2;let best=-1,choices=[];
  for(let mask=0;mask<16;mask++){
    let cost=0,value=0;for(let i=0;i<4;i++){if(mask&(1<<i)){cost+=costs[i];value+=weights[i];}}
    if(cost<=budget){
      if(value>best){best=value;choices=[mask];}
      else if(value===best){choices.push(mask);}
    }
    checked++;
  }
  must(best===7 && choices.length===1 && choices[0]===6,"lawful best audit 1,2");checked++;
  return {status:"synthetic_exact_rational_tick_model",denominator:160,feasible_joint_laws_grid:cases,exact_assertions:checked,
    value_extrema_ticks_160:ext,witnesses, audit:{missing_binary_weights_sixteenths:weights,legal_audit_indices:[1,2,3],budget,chosen_indices:[1,2],initial_width_sixteenths:14,post_audit_width_sixteenths:7,irreducible_forbidden_cell_sixteenths:6},
    limitations:"A conditional synthetic face of the common potential-history polytope, not robot measurements or a complete multi-date calibration."};
}
const result=exactSupportZeroAuditModel();
process.stdout.write(JSON.stringify(result,null,2)+"\n");
