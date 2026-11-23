function study() {
  let assertions=0;
  function check(test,msg){ assertions++; if(!test) throw new Error(msg); }
  const rows=[];
  for(let k=0;k<=10;k++){
    const n00=k,n01=10-k,n10=10-k,n11=k;
    check(n00>=0 && n01>=0 && n10>=0 && n11>=0,"nonnegative "+k);
    check(n00+n01+n10+n11===20,"common law total "+k);
    check(n10+n11===10 && n01+n11===10,"source marginals "+k);
    const orOracleNumer=10+Math.max(0,9-k);
    const andOracleNumer=Math.max(0,3*k-1);
    const orCommittedNumer=19-k;
    const andCommittedNumer=3*k-1;
    check(orOracleNumer===10+Math.max(0, n01-1),"OR optional "+k);
    check(andOracleNumer===Math.max(0,3*n11-1),"AND optional "+k);
    check(orCommittedNumer===n10+n11+n01-1,"OR committed "+k);
    check(andCommittedNumer===3*n11-1,"AND committed "+k);
    const hedgeNumer80=3*orCommittedNumer+andCommittedNumer;
    check(hedgeNumer80===56,"shared-law portfolio hedge "+k);
    rows.push({overlap:k+"/20",joint_counts:{F0T0:n00,F0T1:n01,F1T0:n10,F1T1:n11},or_optional:orOracleNumer/20,and_optional:andOracleNumer/20,or_precommit:orCommittedNumer/20,and_precommit:andCommittedNumer/20,source_hedge:hedgeNumer80/80,embodied_E:0.75});
  }
  check(rows[0].or_optional===0.95,"first OR endpoint");
  check(rows[0].and_optional===0,"first AND endpoint");
  check(rows[5].or_optional===0.7 && rows[5].and_optional===0.7,"interior indifference");
  check(rows[10].or_optional===0.5 && rows[10].and_optional===1.45,"last endpoint");
  check(rows[0].or_optional>0.75 && rows[5].or_optional<0.75 && rows[10].and_optional>0.75,"three-way ranking reversal");
  check(Math.min(...rows.map(x=>Math.max(x.or_optional,x.and_optional)))===0.7,"known-law oracle min");
  check(Math.min(...rows.map(x=>x.source_hedge))===0.7,"precommitted hedge");
  check(Math.min(...rows.map(x=>x.or_optional))===0.5,"optional O min");
  check(Math.min(...rows.map(x=>x.and_optional))===0,"optional A min");
  check(rows.every(x=>x.embodied_E>x.source_hedge),"independent E maximin");
  return {status:"pass",assertions,laws:rows.length,model:"Two source qualifications, OR/AND alternative customer production architectures, optional safe fallback, one post-F validation opportunity, common latent law",rows};
}

console.log(JSON.stringify(study(),null,2));
