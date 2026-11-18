# Proof and falsification ledger — safe pool factorial, 18 November 2026

Companion to [SAFE_POOL_FACTORIAL_THEORY.md](SAFE_POOL_FACTORIAL_THEORY.md). All propositions below are conditional. The finite calculations were checked by [safe_pool_factorial.js](safe_pool_factorial.js) and independently by exact Python `fractions.Fraction` arithmetic in the execution session; no customer or robot evidence was acquired. These tools are **arithmetic checks, not proofs**.

## Direct randomized full-policy mean

Fix N_d preassignment pools in stratum d, full approved route vector a, and fixed potential complete-history contribution Y_i(a). Let I_i(a) indicate cluster assignment and let p_i(a)>0 be known. With actual randomization at the no-cross-cluster-interference unit, E[I_i(a)Y_i(a)/p_i(a) | potential outcomes, D=d] =Y_i(a). Linear averaging proves unbiasedness of SP1. It identifies finite-population full-policy means; the joint distribution of Y_i(a) and Y_i(b) remains unobserved. A downstream order is an outcome, not a selection variable; excluding zeros violates the estimand. Safety/rights eligibility and positivity must be established before the assignment; a hypothetical unapproved action has no experiment-based identification claim.

## Higher-order identity and sharp bounded-mean nonidentification

For three binary slots, define \(\beta_S=\sum_{U\subseteq S}(-1)^{|S|-|U|}\mu(U)\). Summing over S subset T and exchanging sums yields each \(\mu(U)\) with coefficient \((1-1)^{|T|-|U|}\); only U=T survives. This is standard Möbius inversion. In the symmetric table f0=7, f1=15/2, f2=37/5, the lower-order-extrapolated f3 is 3(37/5)-3(15/2)+7 = 67/10. The exact third-order contrast is \(\beta_{123}=f_3-67/10\). If \(f_3\in[6,9]\), its identified interval is \([-7/10,23/10]\). Each endpoint is attained by assigning the same constant potential mean for every fixed treatment vector in an admissible artificial population; all other seven complete-vector outcomes are unchanged, and every bound holds. This proves **sharpness relative to unrestricted mean potential outcomes with this interval**, not relative to any additional controller transition or physical restrictions. RRR exceeds the best observed fixed-one-R value 15/2 iff \(\beta_{123}>15/2-67/10=4/5\). This is a policy rank counterexample, not a positive scientific novelty claim.

## Independent Bernoulli support and safe fixed saturation

With exchangeability by number of R slots and Bernoulli independent slot assignment, K~Binomial(3,x), hence
\[
F=7(1-x)^3+\tfrac{45}{2}x(1-x)^2+\tfrac{111}{5}x^2(1-x)+zx^3
=7+\tfrac32x-\tfrac95x^2+(z-\tfrac{67}{10})x^3.
\]
For fixed x, the worst z in [6,9] is z=6 because coefficient x³≥0. Thus \(F_L=7+\frac32x-\frac95x^2-\frac7{10}x^3\); \(F'_L=\frac32-\frac{18}5x-\frac{21}{10}x^2\), strictly decreasing throughout [0,1], with unique root \(x^*=(\sqrt{71}-6)/7\). Endpoints and the sign change imply the unique maximum is \(F_L(x^*)=(1184+71\sqrt{71})/245\approx7.274516873\). Fixed saturation at K=1 produces 15/2=7.5, a larger guarantee under the stated symmetric known table. This does not imply randomization is generally inefficient with learning/report adaptation or latent heterogeneity: the contrast holds under the fixed complete-potential-outcome table. Bernoulli P(K=3)=x³>0 for all x>0, so if K=3 is *not* approved under a hard pathwise operator budget, every such x must be excluded, not merely penalized in expected utility.

## Partial transport and selective robust deployment

Let A/B target pre-action shares be 7/10 and 3/10. All-G mean 7 in each. A's approved mixed-one-R mean is 15/2; B's approved but unobserved mixed mean b lies in [5,9], with no restrictions linking b to A. A global mixed policy has \(J_M=(7/10)(15/2)+(3/10)b=21/4+3b/10\), therefore [27/4,159/20]=[6.75,7.95]. Relative to all-G 7, the sharp interval is [-1/4,19/20]. Both endpoints are obtained by admissible fixed-mean populations with b=5 or 9. A selective A-mixed/B-G policy gives \((7/10)(15/2)+(3/10)7=147/20=7.35\). Against global all-G, its advantage is 7/20=.35 before any real segmentation overhead. It strictly wins if the extra *captured contribution* cost c satisfies c<7/20, and ties at c=7/20. If B mixing is unapproved, the global mixed policy is not a candidate and the b interval must not be used to license it. Any cross-pool spillover or D-dependent shift in customer opportunity violates the simple target weighting.

## Identification/interpretation limits

A randomized estimate of \(\mu_d(a)\) controls the average effect *for its assignment population* but not the latent persistent-regime conditional payoff vector, unit-level individual gains, required recovery support in unobserved paths, or private customer capture after contracts change. Positive support in the assignment probability is not evidence of pathwise technical safety. A high-order economic interaction can be produced by qualification, scarce operator coordination, or induced customer demand; interpreting it as data complementarity requires frozen market conditions and held-out controller learning tests. If old qualified controllers can be freely retained, include them in the feasible menu; a compulsory conflicting update is not free optional data.

## Prior art and reproducibility

Standard factorial inversion, group interference, and randomization-based exposure-mapping results are prior to this chapter. Public bibliographic sources confirmed 18 November 2026: [Hudgens–Halloran (2008), PubMed Central](https://pmc.ncbi.nlm.nih.gov/articles/PMC2600548/) and [Aronow–Samii (2017), Yale publication record](https://isps.yale.edu/resource/estimating-average-causal-effects-under-general-interference-with-application-to-a-social). The chapter does not replicate their full proofs or assert novelty. Local independent exact-arithmetic checks of f3=67/10, beta interval, binomial expansion, segment bounds and the superiority threshold passed. The committed JavaScript file executes its own explicit finite assertions; historical CI, production field measurement and independent peer review are absent.

**Remaining proof gap:** add coupled *network-level* potential histories when pools share a versioned controller, teleoperators, safety reserves or actual downstream customers. In that regime SP1 requires a different interference unit/exposure map; SP2 remains an arithmetic expansion but observed subset-cell means may be contaminated. Keep the persistent-world identified-set theorem distinct from a randomized population-average estimand.
