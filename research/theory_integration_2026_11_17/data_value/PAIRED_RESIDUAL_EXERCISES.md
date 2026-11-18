# Exercises — incomplete target support and economic policy divergence

Student questions only. Read [the conditional theory](PAIRED_RESIDUAL_SENSITIVITY_THEORY.md). All numbers are synthetic normalized contribution; policies are not physically certified.

1. For two policies with first-exit probabilities p_a=3/4 and p_b=1/4, unknown residuals in [1,5] and |u_a-u_b|<=1, derive sharp bounds for p_a u_a-p_b u_b. Explain why independent endpoint subtraction is too pessimistic.
2. Prove the single-label lower extremum for p_a<p_b without assuming independent robot qualifications. Identify a feasible pair of residuals attaining it.
3. Reuse source-copy/no-copy K and p from the chapter with residual box [0,4]. Calculate intervals at eta=0, eta=1/2 and eta=4. Are either source-copy and no-copy unconditionally ranked?
4. Suppose a diagnostic shows both residual means lie in [3,4] under a genuinely valid joint model, but does not change the policies. With eta=1, determine whether copy can be certified economically better than no-copy. Would this certify robot safety?
5. Give a two-world counterexample with identical pre-exit source and accepted-order logs but reversed post-exit service ranking. Explain which new kind of evidence, not a task benchmark, is required to narrow eta.
6. A proposed controller fallback resets robotic pose but not a customer-order queue or operator call history. Identify the violated assumption behind eta=0 and describe a test that would falsify the claimed common continuation.
7. Does reducing a policy-discrepancy bound by one unit necessarily create economic output equal to the overlap exposure? Justify with an information/decision versus production example.
