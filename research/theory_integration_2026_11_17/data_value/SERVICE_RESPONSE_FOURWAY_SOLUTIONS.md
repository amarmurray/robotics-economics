# Instructor solutions — four-way causal paid-service audit

1. \(A=U\oplus H,C=V\oplus H,W=H\oplus U\oplus V\oplus\theta\); XORing all four leaves \(\theta\). The t2 job is \(J=1-W\), created after that period's clearance. Worker outcome uses only the already existing U,V and realized early H; late orders are determined later from these same latent propensities, not fed backward into the job equation.

2. Each parity class has eight equiprobable 4-bit strings. Fix any k<=3 bits: there are \(2^{3-k}\) completions in either class, so every k-tuple is uniform. The all-ones state has even parity: probability 1/8 at theta0, zero at theta1. In R, H_R=0, A_R=U, C_R=V and W_R=1; theta does not enter, so even a complete R registry is observationally equivalent.

3. For binary variables \(A\lor HC=A+HC-AHC\). Multiply by W and take expectations. Under each G regime \(E H=1/2,E WA=1/4,E WHC=1/8\), so \(V_G=1+4(3/8-\zeta)-1/5=23/10-4\zeta\). R = 4(1/2)=2. P=2+4(1/10)(1/4)=21/10. E=4(1/2+1/2)-37/20=43/20. Adding separate A and C t3 payoffs inside one shared slot double-counts the single qualified service whenever W=A=H=C=1.

4. The feasible parity mixtures produce \(\zeta\in[0,1/8]\), hence \(V_G\in[9/5,23/10]\). In good theta1, failing to choose G loses 3/20; in bad theta0 choosing G loses 7/20. Thus \(R(x)=\max\{(1-x)3/20,x7/20\}\), minimized at \(x=3/10\), regret \(21/200\). The guaranteed-return maximin policy is E=43/20.

5. \(\zeta=P(H=W=1)P(A=C=1\mid H=W=1)\). Given the first probability from G-supported pairwise data and H,W observed, randomly audit both original offers in a positive probability \(\eta\) of the H=W=1 risk set; correct independent missingness with \(M/\eta\). There is no need to observe original A,C on H=W=0 for this **fixed terminal contrast**, but future continuation changes that scope. R may have a different G-induced worker and buyer response, so its audit cannot transport the counterfactual under G without verified invariance. Invoices select on actual accepted service and omit unserved/no-order original demand.

6. Let a t3 report identify whether an A buyer will place a payable t4 order after an inherited job clears before t4; at t3 W=0 so no terminal paid service. The firm has one t3 validation slot choosing an A-target versus C-target policy for t4, and a verified report tells it which target will be ordered. The report can improve expected t4 accepted contribution despite zero t3 production. Its value depends on t3 quality and demand histories in the W=0 states, so the H=W=1-only terminal audit no longer suffices.
