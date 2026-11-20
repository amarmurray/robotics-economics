# Proof ledger — policy-set inclusion, latent regression and selective fallback

**20 November 2026 UTC. Standard set inclusion, potential outcomes, Fréchet and linear programming. Conditional proofs, no field observation and no independent originality judgment.**

## 1. Policy-set inclusion does not imply casewise qualification inclusion

For fixed state law P, payoff G(pi,h) and resources, let Pi0 subset Pi1. Then sup_{pi in Pi1} E_P[G(pi,h)] >= sup_{pi in Pi0} E_P[G(pi,h)] because the old maximizer remains feasible. This is an ordering of **optimized scalar values**, not of every realization G(pi1,h) versus G(pi0,h), nor of binary Q. If an acquisition requires nonrefundable K, the enlarged optimum net of K can be smaller. If learning or acquiring the option changes P, customer demand, rights, shared physical resources or the old feasible policy, the set-inclusion proof's common-objective premise fails.

For the four equiprobable histories in the chapter, R=(1,1,0,0), X_N=(1,1,1,0), X_C=(0,1,1,1). Each X has mean 3/4, R 1/2; selecting the better entire policy gives 3/4 in both worlds. But Q_XC(A)<Q_R(A). The physically unattested OR payoff is 3/4 under X_N and 1 under X_C, proving that an imagined oracle fallback adds a different policy class and is not identified from separate arm marginals. Positive mean learning does not establish individual monotone treatment response.

## 2. Selector identity and the necessary safety condition

Assume T|Z=z is Bernoulli(t_z) independent of the vector (B,Q_R,Q_X) conditional on Z, and there is a single stable original buyer/window/captured margin and no cross-assignment interference. Write Q_T=(1-T)Q_R+TQ_X. By iterated expectation,

E[BQ_T|z]=(1-t_z)E[BQ_R|z]+t_z E[BQ_X|z].

Subtract R, multiply by p_z v_z, and deduct incremental per-selection cost p_z t_z c_z and acquisition cost K to get (1). This algebra **does not** require conditional independence between B and qualifications or Q_R and Q_X. Since Q_T-Q_R=T(Q_X-Q_R), it is nonnegative for every original case iff Pr(T=1,Q_R=1,Q_X=0)=0. Conditional independence gives sum_z p_z t_z Pr(Q_R=1,Q_X=0|z)=0, equivalent to each nonnegative summand being zero. If T depends on a fully observed baseline original B, incorporate B into Z. If an X action changes shared networks, the assumed Q_T consistency fails; replace the unit by a complete assigned network and derive its actual potential outcomes.

## 3. Sharp regression envelope

Condition on B=1 within Z=z. The total mass is b, the R-success mass h_R and the X-success mass h_X. Let o be their overlap. Feasibility of the four cells yields max(0,h_R+h_X-b) <= o <= min(h_R,h_X). Regression l=h_R-o therefore satisfies max(0,h_R-h_X) <= l <= min(h_R,b-h_X), while gain g=h_X-o=l+h_X-h_R. Every o in the interval produces four nonnegative cells (both=o, R-only=h_R-o, X-only=h_X-o, neither=b-h_R-h_X+o), so bounds are sharp in the divisible population (integer-grid sharp when masses are integer multiples of the original denominator). For all eligible physical cases set B=1 and b=1, h_R=q_R, h_X=q_X. This is *not* a physical test that the allowed system can execute OR or rollback.

Notice the economic expected difference h_X-h_R is identified from separately randomized full policy arm means under consistency, exchangeability and positivity, even when l/g remain unidentified. In particular, the original stable-B nested theorem is one stronger restriction l=0, giving d=g; without that restriction d=g-l. No contradiction: the previous theorem bounds an unobserved **gross new-demand matching** when only a technical marginal d and baseline buyer support M,N are available.

## 4. Sharp expected-regression frontier and domain of validity

Under independent Z-stratum coupling possibilities, physical regression l_z^all can range up to rho_z=min(q_Rz,1-q_Xz). For any nonnegative selectors t_z, the supremum of sum_z p_z t_z l_z^all is sum_z p_z t_z rho_z: attain the maximum in each stratum by taking minimum joint R/X-success overlap. Consequently (4) is the exact *statistical* robust expected-regression constrained linear program for those rectangular latent couplings. If interactions couple latent states across strata, the sum is still an upper bound where each marginal bound holds, but it need not be sharp; if assignment changes each stratum's eligibility or the network's payoff law it may cease to be a valid bound at all. Costs c_z accrue for selected network cases, not only qualified sales.

For positive benefit a_z=p_z[v_z(h_Xz-h_Rz)-c_z] and risk weight r_z=p_z rho_z>0, maximize sum a_z t_z subject to sum r_z t_z<=alpha. Taking an increment from a lower a/r selected stratum and assigning the same risk mass to a higher one increases value, yielding standard fractional-knapsack ordering. Zero-risk positive-benefit strata can be included. The optimization is a **decision criterion conditional on permitting expected harm**, not a per-case safety proof and not an additional data-premium term.

Exact example with B=1: p_A=p_B=1/2. A: q_R=1/2,q_X=3/4,v=8,c=1/2 yields a_A=3/4, r_A=1/8; B: q_R=1/4,q_X=1/2,v=4,c=0 yields a_B=1/2,r_B=1/8. So objective (3t_A+2t_B)/4 and worst loss (t_A+t_B)/8. For alpha=1/8, select t_A=1,t_B=0, gain3/4. For alpha=1/16, t_A=1/2,t_B=0, gain3/8. For alpha>=1/4 select both, gain5/4. A constrained physical controller may disallow fractional cluster switching or reassignments; the continuous LP is then a relaxation.

## 5. Rejected generalizations and empirical discriminants

- **Rejected:** freely optional source-data availability implies Q_X>=Q_R. Counterexample 1 disproves it, while preserving optimized gross value monotonicity.
- **Rejected:** observed q_X>=q_R proves no original case can be harmed. Fréchet upper physical regression is positive unless q_R=0 or q_X=1 (or a separately certified structural restriction applies).
- **Rejected:** safe policy improvement in expected return under fixed environment is equivalent to casewise safe robotics qualifications and operator tails. Different objects.
- **Rejected:** precommitment B and fixed posted menu are automatically stable when X/G/E changes perceived quality or service guarantees. Requires binding buyer/quality/receipt evidence.
- **Rejected:** separate site assignments can identify whole-network arm means when learner/operator/parent procurement spillovers cross assignment boundaries.

Positive identification route: physically signed noninterfering fallback/selector and original B plus matched baseline jointly qualified Q; or direct permitted complete-network arm outcomes with original order denominators. Avoid mapping task benchmarks or source-data volumes to customer receipts.

## Reproducibility and prior-art scope

[Exact self-contained JS audit](safe_fallback_selector_audit.js) exhausts all integer denominators D=8 with 0<=q_R,q_X<=b<=8, all compatible latent overlaps, checks endpoints, performs both counterworlds and a small exact-integer randomization frontier. An independent local Python Fraction check reproduced the counterworld and the two frontier choices. These arithmetic checks do not establish any physical selector, approval, buyer invariance, empirical causal effect, or mathematical novelty. Relevant foundations: [Manski 1997](https://ideas.repec.org/a/ecm/emetrp/v65y1997i6p1311-1334.html); [Manski 1999/2004](https://www.nber.org/papers/t0242); [Laroche et al. 2019](https://proceedings.mlr.press/v97/laroche19a.html); [Farboodi–Koh–Xia 2026](https://arxiv.org/abs/2606.10127).
