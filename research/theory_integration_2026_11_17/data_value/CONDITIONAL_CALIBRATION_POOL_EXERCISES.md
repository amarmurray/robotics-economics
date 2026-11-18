# Exercises — conditional diagnostics and controller-pool data value

*18 Nov 2026. Standalone student packet. All values synthetic; assume the chapter's model and hard feasible-menu conditions.*

1. **Pooled calibration is not transport.** Let \(P(H=1)=P(D=1)=1/2\), \(P(Z=1\mid H=1)=.9\), \(P(Z=1\mid H=0)=.1\), and \(m=P(Z=1,D=1)=.34\). Without \(Z\perp D\mid H\), derive bounds on \(t=P(H=1,D=1)\). Give both endpoints as complete joint \((H,D,Z)\) distributions. Compare a route payoff \(J_R-J_G=10t-3\).
2. **Extra assumptions.** Repeat (1) with the extra conditional invariance \(P(Z=1\mid H=1,D)=.9\), \(P(Z=1\mid H=0,D)=.1\). Explain exactly which new observable or validation assumption earns a positive paired certificate and why pooled accuracy did not.
3. **Pair interference.** If independently randomized route assignments R with chance x fill two slots on a shared controller and each discordant pair loses L normalized accepted-service contribution per slot, derive \(J_\kappa(x,t)\) from \(J_0=8-3x+(10x-2)t\). Solve its maximin allocation for \(\kappa=0,3,-3\) with \(t\in[0,1/2]\), and give a general threshold for G to regain a maximin floor of 7.
4. **An actually optional alternative.** With \(\kappa=3\), allow pure R/G, E=6, S=5, and an isolated independent mixed policy at cost c=.5 per slot, but retain frozen old policies. What is the gross maximum maximin value of a perfect population-t diagnostic before paying for the diagnostic? What changes if the cost of isolation falls to zero? Why is this not evidence that optional free data harms value?
5. **Prospective identification.** Design a study to distinguish pooled miscalibration, negative shared-controller interference, and rare pathwise recovery overload without observing both potential outcomes on the same robot. Specify assignment unit, zero-order denominator, qualifications, retained-policy alternative, cluster-level inference and which proposed experiment is inadmissible under recovery cap 2 if it has a supported peak-3 continuation. State at least one pre-registration or ethical limit.

Use the [separate instructor solutions](CONDITIONAL_CALIBRATION_POOL_SOLUTIONS.md) after attempting the problems.
