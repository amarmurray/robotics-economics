# Student exercises — report selection and robotics production data

**Student version: solutions deliberately excluded.** Use the common model in [the chapter](TARGET_REPORT_SELECTION_THEORY.md); all quantities are hypothetical complete-service contributions.

1. Let original customer order report S=h with probability q. A report is retained with probability ρ_h conditional on h and ρ_l conditional on l. Derive selected high and low masses a,b and the sharp unrestricted interval for q when recording propensities are unknown.

2. Original demand contains N=1000 independent L-state opportunities, of which 400 have a selected high report and zero a selected low report. Derive the realized-panel bound on h share. Explain why it is not a confidence interval for superpopulation q without independence of original orders.

3. Under the setup in (2), suppose independently certified high-report recording probability is between 2/3 and 1, and low reports are never recorded. Solve the population q interval treating a=2/5 as known; explain the role of positivity and why the claim cannot be obtained from selected cases alone.

4. Construct the two observation-equivalent target worlds with (q_L,ρ_h)=(2/5,1) and (3/5,2/3). With q_H=3/5 and F=(0,0),S=(3/4,3/4),G=(3,−1),T=(4,−6) and equal H/L demand, find the known-kernel optima and prove the robust value across the two worlds even with randomized report-contingent decisions.

5. Derive the simultaneous Hoeffding conservative outer report confidence set for m predeclared strata using *both* selected-high and selected-low indicator counts. Identify precisely why an arbitrary optional stopping rule or correlated robot/customer records invalidates it.

6. Let original demand p belong to set P and report rows q∈C. If every approved complete-service contribution lies in [a,b], prove a bound involving diameter_TV(P) and report row-width weighted by sup_p p_z times the statewise service span. Identify the economic difference between shrinking this bound and measuring the actual value of purchasing an audit.

7. Explain why positive effects of simulated or teleoperated data on one robot-policy benchmark do not identify the optimized value of an optional source dataset, the economic benefit of a frozen diagnostic report, or physical qualification for a new embodiment.
