# Instructor solutions — reachable paid service

1. L0=0 gives L1=max(0,J-1)=0 if J<=1. L0=1 gives L1=J. If J=2, then L0=0 gives L1=1, so J can block service even in the initially empty stratum. A new model is required.

2. Let s=Pr(A,J=0). The four cells ordered (A,J=0),(A,J=1),(not A,J=0),(not A,J=1) are (s,q-s,1-j-s,j-q+s). Nonnegativity gives max(0,q-j)<=s<=min(q,1-j). Both endpoints are valid probability distributions. No independence is used.

3. G=3/4+2s. With q=3/4,j=1/2, s in [1/4,1/2], giving G in [5/4,7/4]; E=13/8 is inside. Q,D can be 7/8 each by splitting the QD=0 cell half into Q-only and D-only, in both worlds. P potential outcomes can be identical; G has zero support.

4. With L<e<U, worst regret is max{x(e-L),(1-x)(U-e)}. Equalize to x=(U-e)/(U-L) and value (e-L)(U-e)/(U-L). Here x=1/4, regret=3/32. Maximin picks E because e>L. If L0 arrives after irreversible program commitment, conditional choice by L0 would be an illegal foresight assumption.

5. q0>=3/4,q1>=3/4,j1<=1/4 imply s1>=1/2, hence G>=3/4+2(1/2)=7/4 >13/8. P-only customer/worker records and static G benchmark accuracy do not identify qG or jG. Even QG/DG individual marginal bounds may not establish QD's required lower bound.

6. Suppose one worker starts with one queued job and processes one per date. A period-0 newly generated job remains at date 1 and cannot simultaneously be absent at date 1 and reappear as an unprocessed period-0 job at date 2 without a permitted transition. A per-date rectangular minimizer that chooses contradictory queue states violates conservation. Enumerate joint original-buyer/learner/job trajectories z with pathwise queue transitions and one law mu; each lawful policy has payoff R_pi(z). Minimize over the common feasible mu polytope and optimize policies without adapting to unseen z.
