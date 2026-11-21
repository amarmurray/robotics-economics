# Instructor solutions — correlated data and recursive production

Keep separate from [student exercises](CONDITIONAL_COMPONENT_EXERCISES.md).

1. From p_U=p_V=1/2 and p_11=w, p_10=p_01=1/2-w and p_00=w. All entries nonnegative iff 0<=w<=1/2, and each endpoint defines a valid law, so the interval is sharp.
2. A lawful future attempt is worth (q-c)_+=1/2 per joint success. Old G policy has 1+(1/4)(1/2)=9/8. New trained SG policy has 1+w/2. Optional source access allows max of both: J_SG=1+max(w,1/4)/2, with range [9/8,5/4]. Since E=19/16, the sign switches at w=3/8.
3. At w=1/2: R=17/16; S=1+(1/2)(1/2-1/4)=9/8; G=1+(1/4)(3/4-1/4)=9/8; SG=5/4. Cross=5/4-9/8-9/8+17/16=1/16. No change to either marginal P(U=1),P(V=1) is needed: joint success reaches a new economic opportunity.
4. With w<=1/3 for *all legal new SG policies* and an old G fallback, J_SG<=1+max(1/3,1/4)/2=7/6<19/16; E wins if its paid value lower bound holds. With a genuine feasible policy w>=2/5, J_SG>=1+(2/5)/2=6/5>19/16, so SG wins if its original buyer q/c and E upper bound are validated. Neither is inferred from marginals.
5. Pick lambda>=0 and projected potentials phi_it. Verify phi_it+eps_it>=E[y_it-lambda*g_it+phi_i,t+1 | complete h_t, any legal global u_t] and phi_iH>=terminal y_iH. Sum and telescope conditional expectations (linearity needs no independence); add lambda*b from the true aggregate expected resource budget to get J<=lambda*b+E sum_i phi_i0+sum eps_it. If shared c' is omitted and unbounded conditional on the local projection, the inequality may be false for otherwise identical local histories. Lambda is a dual certificate subtracted from the potential recursion and added through the budget, not a second payment.
