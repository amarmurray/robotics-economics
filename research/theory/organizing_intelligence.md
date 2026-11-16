# Competence, coordination, and the limits of physical replication

First mechanism reconstruction, theory phase checkpoint 1. This is a reconstruction of a selected worked mechanism, not replication of the whole paper or a claim of novelty.

## Source and reading boundary

Alex Imas, Andrew Koh, and Shane Legg, *Organizing Intelligence*, author PDF dated **October 29, 2026**, retrieved November 16 UTC (November 15 Eastern), 2026. [Primary PDF](https://storage.googleapis.com/deepmind-media/papers/organizing-intelligence.pdf). SHA-256: `f763c6c2d8de4b653cd6d78ec96ec0ee206360cb4ea7e8c6d432c34e1100553a`. The supplied arXiv discovery entry is `2611.05417`; version equivalence has not been checked. Do not substitute its date for the inspected PDF's date.

Read the worked environment in §2.1–2.2 (printed pp. 3–7), formal primitives in §3.1, equilibrium definition in §4.1–4.2, and the concentration statement/discussion in §5.2 (Proposition 3, p. 33). The initial checkpoint did not reconstruct the remaining proofs. The continuation below now reconstructs Appendix A.2.3 and the concentration argument; equilibrium existence and the other propositions are not independently audited. A local downloaded source lives in ignored `work/theory_sources/`; the URL and hash permit recovery without redistributing the paper.

## Mechanism card

**Question.** Why can better individual competence fail to produce larger organizations, while better coordination changes the returns to scale?

**Agents and primitives.** Humans have heterogeneous vectors of productive skills and coordination, fixed supplies, and outside options. Copies of a machine type have a common vector and can be rented without quantity limit at per-copy cost. A firm selects its size and composition. The worked example has two productive skills, six coders `(9,1,.75)`, six writers `(1,9,.75)`, and two coordinators `(1,1,.97)`. Firm competence is the harmonic mean of average skills. Coordination changes the scale term. Output faces either deep or finite demand.

**Information and solution concept.** These are known profiles, not learning states or beliefs. The formal paper combines competitive continuation (price/wage taking, break-even, no profitable entry, labor clearing) with replacement stability against a proposed alternative industry and transfers. Its surplus equivalence relies on that specified concept; it is not ordinary oligopoly pricing or the private provider problem below.

**Assumptions doing the work.** Complementary productive skills; aggregation of skills within firms; separability of competence from the size term at fixed composition; copyable AI at a rental price; no robot manufacture, physical qualification, payer-specific liquidity, or customer learning transition in this worked mechanism. Do not infer from these omissions that the whole paper considers every possible physical constraint and rejects it.

## Reconstructed worked result

Let `m>0` be continuous firm size, `L>0` competence, `y` average coordination, and `phi=7/4`. The example's output per worker is

`g(m)=L exp(phi*m/(1+m)) (1+m)^(y-1)`.

Thus

`d log(g)/dm = [phi - (1-y)(1+m)]/(1+m)^2`.

For `y<1` and `phi>1-y`, the unique interior maximum is

`m*=phi/(1-y)-1`.

The numerator decreases strictly with m, so its single zero changes the derivative from positive to negative. This proves global optimality on positive m. If `phi<=1-y`, g decreases on positive m and the supremum is at the lower boundary; with a minimum admissible size, maximize there. For `y>=1`, the derivative is positive at every finite m (at `y=1`, productivity increases toward the finite asymptote `L exp(phi)`). The distinction between a bounded asymptote and unbounded growth matters: the paper's Proposition 3 expressly excludes its knife-edge coordination exponent of one.

Holding composition fixed, multiplying L does not change m*. In contrast, `dm*/dy=phi/(1-y)^2>0` in the interior region. This is a productivity-maximizing size result, not an unconditional profit-maximizing fleet-size theorem.

For six coders, `L=2/(1/9+1)=9/5` and `y=3/4`, hence `m*=6`. Total output is about 29.8. Twelve coders in one firm produce about 57.2, whereas two size-six firms produce about 59.5. Equal coder/writer weights have average skills `(5,5)`, so L becomes 5 even though every individual specialist has standalone L=1.8. This reproduces the selected paper example's complementarity and size calculations. The executable check uses the source's functional form; numerical agreement verifies transcription and arithmetic, not its empirical validity.

**What is not established.** Proposition 3 is an asymptotic equilibrium claim as market depth grows, under the paper's formal assumptions. It is not a prediction that any finite robotics market tips to a single firm when an observed coordination score exceeds one. Our calculation neither replicates its equilibrium nor tests that threshold empirically.

## Changed assumption: finite physical replication

For a fixed recipe of physical units, suppose size is restricted to `0<m<=K`, with K the number of compatible, commissioned, supported units available this period. Under the same productivity objective and an interior unconstrained optimum, `m_hat=min(K,m*)`; when y>=1, `m_hat=K`. This is an immediate restricted-domain result. Better coordination still changes productivity, but need not change feasible scale. Expanding K requires a separate investment/delivery/qualification transition.

Moreover, even with abundant hardware, finite downstream demand can reverse the size implication. If useful sales are bounded by D, and each installed unit costs r>0, a simple alternative objective is `p min(F(m),D)-r*m`. Once output reaches D, adding units strictly lowers profit. Improving L can reduce the smallest fleet needed to serve D. Thus fixed-composition competence independence of the productivity-maximizing size does not imply competence independence of the profitable physical fleet. This is a change of objective and constraint, not a counterexample to the authors' theorem.

## Robotics mapping and proposed extension

| Source mechanism | Robotics interpretation | Boundary that must change |
| --- | --- | --- |
| Copies at rental cost | Reusing a policy/model on compatible robots | Qualified hardware, delivery, support, rights, and cash do not replicate for free |
| Complementary skill averages | A configured service may need sensing, mobility, manipulation, recovery | Physical capabilities may require a joint bundle; averaging skill vectors need not make a service feasible |
| Coordination changes scale | Shared supervision, routing and exception handling | Congestion, latency and correlated failure need separate evidence |
| Competence changes level | Better rate, reliability, accepted work | A benchmark improvement need not change complete-service output |
| Market depth supports scale | Customer output can absorb additional service | Customer revenue, procurement authority and funding differ from aggregate willingness to pay |

The proposed extension is a **private two-period investment problem**: a deployment yields cash, a directional cost/capability change, and access to a customer demand curve; costly investment changes supported capacity. This explicitly replaces unlimited contemporaneous replication. It does not yet explain endogenous legal firm boundaries or solve the source paper's equilibrium. See [the model and derivation](deployment_investment.md).

The [next seed mechanism](data_driven_automation.md) now distinguishes endogenous accumulation and directed spillovers from this known-transition investment problem. Its Proposition 5 proof has subsequently been reconstructed; the other long-run and welfare propositions remain unreplicated.


## Continuation: concentration depends on the cost of replication

Inspected Proposition 3 (printed p.33), Assumption 1 (pp.16–17), and complete Appendix A.2.3 (pp.70–72). This reconstructs the source's asymptotic mechanism. It does not establish finite-market robotics concentration or independently audit all equilibrium-support results used upstream.

**The author result and object.** With demand P_N(Q)=P(Q/N), fixed finite human supply, machine viability and the source equilibrium/technology assumptions, gamma_M<1 implies the largest active complete-firm output share vanishes as N grows. Gamma_M>1 implies the relaxed concentration integral integral(q_f/Q)^2 d sigma(f) tends to one. The knife edge gamma_M=1 is excluded. The integral is defined for an industry measure that permits non-integer activity intensities; it is not automatically an observed integer-firm HHI or evidence about legal ownership.

### Reconstructed cost and concentration argument

Machine viability supplies a constant-cost feasible benchmark. For some z>0, P(z) exceeds its unit cost cbar. Efficiency bounds equilibrium surplus below by N times the positive integral of P(u)-cbar over [0,z]. Since surplus is at most P(0)*Q_N, equilibrium Q_N grows without bound (indeed at least linearly in N).

When gamma_M<1, any diverging feasible firm becomes almost entirely machine-staffed: its human input is bounded by the fixed total human supply. The uniform power tail and continuity then imply output per worker tends to zero, while resource cost per worker remains bounded away from zero. Unit cost diverges. Active firms have a bounded unit cost under supporting prices and the atomistic benchmark, so their size and output are uniformly bounded. Divide by Q_N tending to infinity to obtain vanishing complete-firm shares. This uses finite human supply, not an assertion that all conceivable organizational complements disappear.

For gamma=gamma_M>1, set alpha=1/gamma in (0,1). A large machine-only firm produces Q at resource cost (cstar+o(1))*Q^alpha, where cstar=r*A_machine^(-alpha). The proof also needs a *sharp matching lower bound*, not merely the same exponent: sufficiently large feasible firms satisfy C(f)>=(cstar-epsilon)*q_f^alpha. Fixed human supply, uniform tail errors and the Lipschitz exponent under mixing imply the lower bound. The exponent error is of order 1/m; its multiplicative effect is bounded by exp(-constant*log(m)/m), which tends to one. This is why an arbitrarily small human share cannot secretly retain a different cost coefficient/exponent in the limit.

Small/atomistic activities have a positive lower average cost, while the single large machine firm's total cost is order Q^alpha=o(Q). Thus small activities provide only a vanishing output share in a least-cost industry. For the remaining large firms, write s_f=q_f/Q. Market fit implies 0<=s_f<=1. Comparing their sharp lower costs with the one-firm upper cost bounds integral s_f^alpha close to one; their total share integral s_f also approaches one.

The final inequality is s^alpha-s >= (1-alpha)*s*(1-s). For s>0 it follows from convexity of s^(alpha-1) and its tangent at one; at zero it holds by continuity. Therefore a positive share-weighted dispersion integral s*(1-s) would cause a strictly positive excess cost relative to the one-firm benchmark. Let epsilon tend to zero to obtain integral s_f^2 tending to one. Source equilibrium efficiency makes this least-cost argument applicable to the equilibrium industry.

This is a stronger reconstruction than simply noting that output has increasing returns. Linear machine rental, an available large machine-only firm, the cost coefficient bound, market fit and equilibrium efficiency all enter. A financing-constrained provider cannot simply borrow the conclusion from the production exponent.

### Changed assumption: scale-dependent physical support costs

Keep this as a separate illustrative production-unit problem, not a modification silently claimed to satisfy all source assumptions. Consider homogeneous service units with m>0, output F(m)=m^gamma and resource cost C(m)=r*m+kappa*m^beta, with r,kappa>0 and beta>gamma>1. The added term represents genuinely consumed support/integration resources that rise with the scale of a single operating unit. It is not an internal transfer or a debt repayment counted as a new social cost. This exact pure-power toy excludes the source's atomistic activity construction.

Cost per output is r*m^(1-gamma)+kappa*m^(beta-gamma). It diverges at both zero and infinity. Differentiation gives the unique global minimum

m_star = [r*(gamma-1)/(kappa*(beta-gamma))]^(1/(beta-1)).

Thus superlinear output alone does not force unbounded optimal operating-unit size. Under free replication of identical units without shared congestion, arbitrarily large demand can be served by replicating bounded units near m_star. If instead support costs arise at the industry level and cannot be avoided by splitting units, that replication argument fails. Whether the unit is a site, team, platform or legal firm must be specified; one owner could still operate many bounded units.

An exact synthetic example sets gamma=2, beta=3 and r=kappa=1. Unit cost is 1/m+m>=2, with equality at m=1. For total output four, four size-one units cost eight, whereas one size-two unit costs ten. Without the extra support term (kappa=0), those costs are four versus two, favoring the single large unit. The same output exponent therefore yields opposite production-unit rankings because resource costs changed. This is familiar scale economics and an explicit assumption challenge, not a claimed novel counterexample to Proposition 3.

**Scope consequence.** Keep organization/coordination as a broader-program branch unless this mechanism is needed by the deployment-allocation paper. Empirically distinguish physical support cost, reusable digital coordination, payer financing and common ownership. Neither a measured productivity gain nor a larger fleet identifies the relevant cost tail or legal boundary.
