# Instructor solutions — incomplete target support and economic policy divergence

Separate from [student exercises](PAIRED_RESIDUAL_EXERCISES.md).

1. d=1/2, overlap=1/4, l=1,h=5,eta=1. Sharp bounds d*l-overlap*eta=1/4; d*h+overlap*eta=11/4. Independent lower=(3/4)*1-(1/4)*5=-1/2; independent upper=(3/4)*5-(1/4)*1=7/2. The joint policy divergence restriction prevents simultaneously maximally disparate residuals.
2. Write p_a u_a-p_b u_b=(p_a-p_b)u_b+p_a(u_a-u_b), with d<0. Minimum at u_b=h,u_a=h-eta gives d*h-p_a*eta. Both values belong to [l,h] because eta<=h-l. This is a conditional mean linear optimization; no qualification independence is invoked.
3. D=-1/20, d=1/4, overlap=1/4. eta=0 gives [-1/20,19/20]. eta=1/2 gives [-7/40,43/40]. eta=4 gives [-21/20,39/20]. Every interval contains zero, so neither policy strictly dominates the other uniformly.
4. d=1/4, D=-1/20, [l,h]=[3,4], eta=1. Lower = -1/20+3/4-1/4=9/20>0, upper=-1/20+1+1/4=6/5. It establishes a conditional economic comparison if the diagnostic and identical K,p assumptions truly hold; it does not certify physical safety or evaluate against S/F.
5. Keep identical K,p in the previous example but set (u_copy,u_no)=(0,4) in one world and (4,0) in another. Net contrasts -21/20 and 39/20. We need independently admissible matched whole-network post-exit service/recovery/demand/dispatch/operator evidence or a verified structural constraint on their *difference*.
6. A controller pose is not the entire economic Markov state. The remaining original-order queue, time windows and operator constraints may differ under the same actuator fallback. Audit customer-order survival, queue version, recoveries and operator allocations under both complete qualified policies.
7. No. Narrowing eta (at fixed K,p) improves an uncertainty certificate's lower endpoint but does not change a realized policy's production. If a credible diagnostic changes which already qualified policy the manager selects, value is expected reduction in decision error net its cost. If it produces no decision change, its decision value can be zero despite a tighter bound.
