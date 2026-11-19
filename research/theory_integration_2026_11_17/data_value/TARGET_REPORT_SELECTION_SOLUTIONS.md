# Instructor solutions — report selection and whole-network customer production

**19 November 2026.** Separate instructor version. See [student exercises](TARGET_REPORT_SELECTION_EXERCISES.md). All values synthetic.

1. By conditioning, a=P(O=1,S=h)=qρ_h and b=P(O=1,S=l)=(1−q)ρ_l. With completely unrestricted recording, a≤q≤1−b; allocate any fraction of the unrecorded mass m=1−a−b to h. Every q in that interval is attained by some latent allocation, showing sharpness.

2. For N=1000,H=400,L=0, there are M=600 unseen reports. The realized high-report share is between 400/1000=2/5 and 1, on the finite-panel 1/1000 lattice. A panel fraction and superpopulation probability are different: without an independent original-order sample (or documented probability design), no ordinary iid confidence interpretation follows.

3. With population selected-high share a=2/5 and independently validated ρ_h∈[2/3,1], q=a/ρ_h∈[2/5,3/5]. Zero low-report recording gives no extra restriction. Treating a=400/1000 as exactly equal to the population a is not justified in finite data; a fixed-n confidence set must be imposed first.

4. World A: q_L=2/5,ρ_h=1; World B: q_L=3/5,ρ_h=2/3. Both have P(selected h)=2/5, P(selected l)=0 and P(no record)=3/5 for every original opportunity, even when total N is known. With q_H=3/5, A's report rule G(h)/S(l) earns 3/4+(9/8)(3/5)−(7/8)(2/5)=43/40, the maximum over the 16 deterministic rules. In B the reporter is uninformative (q_H=q_L); constant G earns 1, above constant S=3/4, F=0 and T=−1. At this admissible B kernel, all randomized report rules earn at most 1 because the objective is linear in each report-specific policy simplex. Constant G earns 1 in **both** worlds, certifying maximin 1 over randomized policies, not merely a pure-policy search.

5. Let H_i and L_i indicate selected-high and selected-low labels among *all* original opportunities. Their expectations are a,b, regardless of correlation between a report and its own recording indicator. With N_z iid opportunities in each of m fixed strata, use 2m two-sided Hoeffding bounds; choose ε_z=sqrt(log(4m/δ)/(2N_z)). Jointly q_z≥a_z≥H_z/N_z−ε_z and q_z≤1−b_z≤1−L_z/N_z+ε_z, clipped to [0,1]. Optional stopping, time dependence, policy feedback and network interference defeat this iid guarantee without additional design.

6. For any fixed report-action lottery, a demand change p→p' affects expected complete-service contribution by at most (y_max−y_min) TV(p,p'). Holding p' fixed, a report-kernel change q→q' affects it by at most Σp'_zR_z|q_z−q'_z|. Apply the triangle inequality and compare the true optimal π* with the worst feasible p',q' to obtain (y_max−y_min)diam_TV(P)+Σ_z sup_P p_z R_z width(C_z). Shrinking such an epistemic upper bound is **not** estimating the Bayesian value of paying for an audit.

7. Simulator, teleoperation and customer trajectory data can have different rights, observation and action distributions and different effects on *joint* qualification. A benchmark delta neither proves physical approval nor identifies displacement, accepted customer service and optimized continuation value. A frozen nonactuating diagnostic holds the physical menu fixed; source training or a changed embodiment does not. The safe alternative and any paid/forced acquisition are compared inside the original dynamic J, without a second data premium.

