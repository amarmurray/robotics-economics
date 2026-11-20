const jointHammingAudit = function jointHammingAudit(){
  const assert=(ok,msg)=>{if(!ok)throw Error(msg)};
  const upper=(c00,c01,c10,c11,uc,uq)=>{
    let best=-1,bestPath=null;
    for(let z=0;z<=Math.min(c00,uc,uq);z++){
      const x=Math.min(c10,uq-z),y=Math.min(c01,uc-z),v=c11+x+y+z;
      if(v>best){best=v;bestPath={x,y,z};}
    }
    return {max11:best,by:bestPath};
  };
  const lower=(c11,uc,uq)=>Math.max(0,c11-uc-uq);
  let cases=0;
  for(let n00=0;n00<=8;n00++)for(let n01=0;n01<=8-n00;n01++)for(let n10=0;n10<=8-n00-n01;n10++){
    const n11=8-n00-n01-n10;
    for(let uc=0;uc<=4;uc++)for(let uq=0;uq<=4;uq++){
      const u=upper(n00,n01,n10,n11,uc,uq);
      let b=n11;
      for(let z=0;z<=Math.min(n00,uc,uq);z++)
       for(let x=0;x<=Math.min(n10,uq-z);x++)
        for(let y=0;y<=Math.min(n01,uc-z);y++) b=Math.max(b,n11+x+y+z);
      assert(u.max11===b,"upper disagreement");
      const l=lower(n11,uc,uq);
      assert(l<=n11 && n11<=u.max11 && u.max11<=8,"bad support");
      cases++;
    }
  }
  const A=upper(6,2,4,8,4,4), B=upper(0,2,0,18,1,1);
  const Aupper=A.max11/40, Blower=lower(18,1,1)/40;
  const G=(s)=>Math.max(3,4*(0.5+s))-0.5;
  assert(A.max11===14 && B.max11===19,"case maxima");
  assert(Aupper===0.35 && G(Aupper)===2.9,"case A economics");
  assert(Blower===0.4 && G(Blower)===3.1,"case B economics");
  const naiveA=(8+4+4)/40;
  assert(naiveA===0.4 && G(naiveA)===3.1,"naive vs refined bound");
  return {model:"conditional joint original buyer and safe qualification two-bit transport",
     assumption:"same original eligible H registry, policy/menu supported, upper bounds on paired cross-policy bit flips; not observed robotics returns",
     baseline_grid_denominator:8,baseline_4cell_distributions:165,change_budget_pairs:25,exhaustive_cases:cases,
     case_A:{conditional_cells_00_01_10_11:[6,2,4,8],conditional_change_budgets:[4,4],units:20,
       baseline_global_joint_s:0.2,crude_global_upper:naiveA,sharp_global_upper:Aupper,
       X_net:3,G_net_upper:G(Aupper),retained_R_net:2,upper_atom_conversions:A.by},
     case_B:{conditional_cells_00_01_10_11:[0,2,0,18],conditional_change_budgets:[1,1],units:20,
       baseline_global_joint_s:0.45,sharp_global_lower:Blower,
       X_net:3,G_net_lower:G(Blower),retained_R_net:2},
     real_original_buyer_panel:false,physically_approved_joint_second_service:false,
     credible_counterfactual_switch_bounds_estimated:false,independent_novelty_review:false,
     full_repository_CI:false,nov22_gate_passed:false};
};
const result = jointHammingAudit();
if (typeof process !== 'undefined' && process.stdout) process.stdout.write(JSON.stringify(result,null,2)+'\n');
