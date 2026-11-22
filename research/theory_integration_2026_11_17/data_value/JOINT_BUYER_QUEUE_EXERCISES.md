# Student exercises — joint original-buyer/queue auditing

Work from [the theorem chapter](JOINT_BUYER_QUEUE_AUDIT_AND_TIMING.md). Do not consult the separate instructor solutions until attempting each proof.

1. **Physical transition.** Starting with H, Y, date-2 dispatch T/R, and terminal order Z, write the recovery queue at date 3 and derive \(V_{P,T}-V_{P,R}\). Identify exactly which signals are observable before date-2 choice, and which paid service is displaced.
2. **Nonrectangular law.** Verify the parity family has all fair independent pairwise H,Y,Z tables, yet \(b=\Pr(H=0,Y=1,Z=1)\) ranges over [0,1/4]. Why can separately fitting the three pairs fail to identify the whole original buyer service?
3. **P/G/E decision.** With known accepted original-customer paid coefficients \(r=3/4,k=1/2,c_G=1/32,E=9/16\), compute the unique winning program on each open subinterval of b. Distinguish the T-versus-R threshold from the P-versus-E investment threshold.
4. **Audit projection.** Prove the row-span sufficient condition for ranking every policy in a fixed legal menu. Explain why a full A,Z original buyer link still cannot identify a permitted but untried G action's conditional economic uplift.
5. **Timing and robust implementation.** Under a uniform prior on b=0,1/8,1/4, calculate ex-ante value when the perfect b report arrives before program choice, after program but before dispatch choice, and after both. Calculate a no-report worst-case investment guarantee. Explain why a report about the distribution is not a prediction of the realized late buyer.
6. **Generalization objection.** Replace unchanged Z by program-dependent \(Z^G,Z^P\) and the one-interval T recovery by uncertain duration. Specify which additional lawful original-buyer/worker/learner moments are required, and why a benchmark-only skill score cannot fill them.
