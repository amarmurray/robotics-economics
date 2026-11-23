# Replicate the exact conditional two-embodiment construction

1. In this directory run: node two_embodiment_joint_audit_exact.js
2. Compare printed JSON with TWO_EMBODIMENT_JOINT_AUDIT_RESULTS.json.
3. The script works with the standard JavaScript BigInt integer implementation, no npm packages. It uses **one joint law** per mixture weight w=0..16, eight parity states split by an independent Q, and scaled integer payoffs; its denominator is 1024.
4. For each of 17 laws verify normalization; every A,C,W marginal is 1/2, every pair is 1/4, triple Pr(ACW)=w/64; R=1/2, P=3/4-w/64, G=7/8-w/32 and E=3/4. Verify endpoint G/E differences, and 1/16-grid minimax regret G share 1/4 and value 3/32. The continuous optimum follows analytically by equating the endpoint lines, not merely from the grid.
5. The uploaded script's exact source string was executed with V8 and passed **226 assertions over 17 laws**, then stored as Git blob db900b591e8f88ef3626bfc516d74026ea390465. Whole-repository tests and actual Node replay were not executed by the connector session; the Node instruction is provided for independent replication. This is an arithmetic check, not a proof of the general audit theorem or external robotics evidence.
6. A separate future validation should test synthetic policy-dependent t2 job arrivals and t3 original offers with G-specific lawful support; the current fixed-law witness intentionally cannot identify those causal effects.

Nearest theoretical precedents: Robins (1986) longitudinal causal support; Manski (2004) treatment choice under regret; linear program/finite-state Bellman theory and DDA §5/Appendix B. None of these source titles is presented as empirical calibration.
