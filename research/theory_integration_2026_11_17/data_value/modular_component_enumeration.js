function run() {
  const names=["X_source","G_grounding","E_embodiment"];
  const val=(kind,m)=>6+4*(
    kind==="source_only"?Number((m&1)!==0):
    kind==="ground_only"?Number((m&2)!==0):
    kind==="body_only"?Number((m&4)!==0):
    kind==="all_required"?Number(m===7):
    kind==="two_suffice"?Number(((m&1)!==0)+((m&2)!==0)+((m&4)!==0)>=2):
    Number(m!==0)
  );
  function shapley6(v,i) {
    const bit=1<<i,other=[0,1,2].filter(j=>j!==i);
    return 2*(v[bit]-v[0]) +
      other.reduce((a,j)=>a+v[bit|(1<<j)]-v[1<<j],0) +
      2*(v[7]-v[7^bit]);
  }
  const triple=v=>v[7]-v[6]-v[5]-v[3]+v[4]+v[2]+v[1]-v[0];
  const pairXE=v=>v[5]-v[1]-v[4]+v[0];
  const exemplars={};
  for (const kind of ["source_only","ground_only","body_only","all_required","two_suffice","any_suffice"]) {
    const v=Array.from({length:8},(_,m)=>val(kind,m));
    const phi6=names.map((_,i)=>shapley6(v,i));
    if(v[0]!==6||v[7]!==10||phi6.reduce((a,b)=>a+b,0)!==24) throw Error("failed exemplar");
    exemplars[kind]={payoffs_by_bitmask:v,shapley_in_sixths:phi6,three_way_interaction:triple(v),XE_interaction_without_G:pairXE(v)};
  }
  let cases=0,feasible=0,phiMin=[Infinity,Infinity,Infinity],phiMax=[-Infinity,-Infinity,-Infinity];
  let tripleMin=Infinity,tripleMax=-Infinity,pairMin=Infinity,pairMax=-Infinity,assertions=0;
  for (let index=0;index<15625;index++) {
    let t=index,v=[6];for(let i=0;i<6;i++){v.push(6+(t%5));t=Math.floor(t/5)}
    v.push(10);cases++;
    let admissible=true;
    for(let a=0;a<8&&admissible;a++)for(let b=0;b<8;b++) {
      if((a&b)===a && v[a]>v[b]){admissible=false;break}
    }
    if(!admissible)continue;
    feasible++;
    const p=names.map((_,i)=>shapley6(v,i));
    for(let i=0;i<3;i++){phiMin[i]=Math.min(phiMin[i],p[i]);phiMax[i]=Math.max(phiMax[i],p[i]);if(p[i]<0||p[i]>24)throw Error("option bound");assertions++}
    if(p.reduce((a,b)=>a+b,0)!==24)throw Error("efficiency");
    assertions++;
    const z=triple(v),g=pairXE(v);
    tripleMin=Math.min(tripleMin,z);tripleMax=Math.max(tripleMax,z);
    pairMin=Math.min(pairMin,g);pairMax=Math.max(pairMax,g);
  }
  if(cases!==15625||feasible!==1884||phiMin.some(x=>x!==0)||phiMax.some(x=>x!==24)||tripleMin!==-8||tripleMax!==4||pairMin!==-4||pairMax!==4)throw Error("enumeration mismatch");
  return {date:"2026-11-20",model:"synthetic normalized entire original-customer network net contribution; no field measures",
    components:names,bitmask:"bit0=X source, bit1=G target grounding, bit2=E new embodiment",
    observation:"only baseline v(000)=6 and bundled v(111)=10 are observable in example",
    enumeration:{grid_middle_cell_values:[6,7,8,9,10],candidate_complete_tables:cases,monotone_optional_tables:feasible,
      bounded_shapley_in_sixths:{min:phiMin,max:phiMax},three_way_interaction:{min:tripleMin,max:tripleMax},
      source_embodiment_interaction_at_G0:{min:pairMin,max:pairMax},integer_assertions:assertions},
    exemplars,conditions:"all eight policies physically admissible, original-buyer version constant, free optional components, retained fallback",
    limitations:"no causal robot training; no original-customer receipts; bounded finite grid does not prove sharp continuous generality"};
}

if (typeof module !== 'undefined' && require.main === module) console.log(JSON.stringify(run(), null, 2));
if (typeof module !== 'undefined') module.exports = {run};
