# Student exercises: data, customer orders and newly generated recovery jobs

Companion to [the conditional theory](ADAPTIVE_QUEUE_LEARNER_DEMAND_COUPLING.md). All examples are synthetic; do not use unverified field data.

1. With Pr(U3^T=1)=3/4 and Pr(J2^T=1)=1/2, derive the exact interval for z=Pr(U3^T=1,J2^T=0). Construct a complete valid joint table for both extreme laws. Explain why their worker histories are physically possible given the new date-2 job and why treating F3 as an independent date-3 shock is not equivalent.

2. Reconstruct the paid-production Bellman value under D1 in {1,2} equally likely, t2 feasible target premium 1/8, and site-2 retained-R qualification/buyer probabilities 4/5 and 5/8. Derive the t2 T/R policy cutoff and P's sharp whole-program interval, preserving the optional R controller.

3. Compute G from 7/10 future buyer-qualified opportunity and 21/50 grounding cost. Compute E from 9/10 additional order opportunity and 3/5 **full** independent-body-and-worker cost. Rank P/G/E in both joint extreme worlds. Explain why neither a benchmark performance percentage nor the recovery marginal alone identifies the ranking.

4. Suppose the true z is hidden before the date-2 decision and T is chosen with fixed probability x after observing D1=1. Derive P(x,z), find the maximin x, and contrast the robust implementable P guarantee to max_z J_P(z). State exactly what lawful early report or identification would be needed to achieve the latter.

5. Generalize the queue with two newly arriving recovery jobs, one old job and arbitrary worker service c_t. Specify the state variables and a physically feasible transition constraint. Explain why statewise independent ambiguity may choose incompatible worker durations across programs, and propose one field statistic to falsify the simple one-new-job example.