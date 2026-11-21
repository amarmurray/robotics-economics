# Instructor solutions — policy-occupancy source-data value

1. Conditional final-paid difference is |q p−q s|=q|p−s|. Since Q reaches that kernel with probability q, its occupancy contribution is q|p−s|. For q=.1,p=1,s=0 the value gap and bound are exactly .1; a uniform maximum-kernel bound returns 1.
2. Reference optimized SG=.4, E=.55, so E wins. Fully pooled P optimizes SG to 1 through the risky recipe and beats E. Logging safe only has TV=0 while the optimal risky action is unsupported. Optimized value differs by .6.
3. m=.99(0)+.01(1)=.01; the Q-reference risky occupancy of the P-optimal policy is 1, so C=1/.01=100; valid bound R min(1,C m)=1 for R=1. E/SG ranking is not certified by this bound.
4. D2=3(−.15)−3(−.15)−.15=−.15. D_all=1−.55=.45. The unobserved third dividend is .60. Within-SG paid value rises from .4 to 1 with optional source availability, so monotonicity cannot identify the cross-program dividend.
5. Write J_P=J_P(Pi0)+e_P and J_Q=J_Q(Pi0)+e_Q. Take the difference and use |e_P−e_Q|<=max(e_P,e_Q), then |J_P−J_Q|<=b_(Pi0)+max(e_P,e_Q). The extra policy must be proven physically/legal feasible and its paid value bounded.
