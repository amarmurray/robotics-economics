# Instructor solutions: dynamic original-buyer economic opportunity

1. For any legal u_t, the true complete-event law is in Kbar_t; apply E[y_t+B_{t+1}|z_t,u_t] <= B_t. Iterating conditional expectations under the selected nonanticipating policy and applying terminal B_H >= y_H telescopes to E sum y <= E B_0. Supremizing over policies preserves the inequality. Correlated ambiguity sets across times do not invalidate this *outer* inequality; rectangularity matters for identifying a minimal robust Bellman value as the value of an actual admissible worst-case joint model.

2. Since E sum g_k <= b_k, E sum y <= lambda.b+E sum(y-lambda.g). Apply the bound from (1) to the adjusted stage reward. For an actual policy, M_t=sum_{s<t}(y_s-lambda.g_s)+B_t^lambda(z_t) is a supermartingale by conditional expectation. The lambda terms cancel in the accounting comparison; they are dual penalties inside an optimization relaxation, not another operating expenditure on top of costs already present in y.

3. The first paid success and failure are exclusive. Upon success, optional licensed learning yields positive incremental q-c=13/20. Upon failure, approved optional recovery has positive net r-d=9/20. Hence J_SG=(2/5)(1+13/20)+(3/5)(9/20)=93/100, smaller than E=95/100. Adding unweighted branch maxima instead yields 2/5+13/20+9/20=3/2, a valid but weak upper estimate; it double counts mutually exclusive opportunities as if both branches occurred.

4. J_SG=(2/5)[1+(q-3/20)]+(3/5)(9/20)=61/100+(2/5)q for q>3/20. Equality to 95/100 gives q=17/20. In an alternative world with q=9/10, J_SG=97/100>E, while q=4/5 gives 93/100<E. Keep p,r and all first-service logs unchanged; the distinguishing observation is future distinct buyer eligibility, accepted service and finally cleared settlement conditional on first-stage data/rights.

5. Training/second buyer action is not in the legal menu. J_SG=2/5+(3/5)(1/2-1/20)=67/100. This is a rights or menu restriction. With truly free optional access and unchanged old law/menu, SG can still choose the no-training fallback and cannot be worse.

6. World A has p=1/2,q=0, no recovery or costs, J_A=1/2. World B has p=0,q=1, J_B=0. A rectangular hull combines p=1/2 and q=1 and reports 1. It is larger than max{J_A,J_B}=1/2 but remains an upper bound. Joint full-fleet checkpoint/source lineage with same original-buyer stagewise outcome data could restrict such incompatible recombinations; unrelated task benchmarks cannot.

7. With q_g above training cost c, J(x,g)=f+p_x(1+q_g-c-f), giving cross difference (p_1-p_0)(q_1-q_0), or use [(q_1-c)_+-(q_0-c)_+] when optional thresholds bind. For a counterexample fix p=8/20, c=0, q_00=0 and q_10=q_01=q_11=16/20. Both optional inputs improve net paid service by 0.32 alone, but together have no extra gain: the cross-difference is -0.32. Positive economic interaction is conditional on the distinct p_x/q_g channels, not implied by free optional data or monotone technology.
