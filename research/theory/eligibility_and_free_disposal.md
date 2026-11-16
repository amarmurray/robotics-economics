# Eligibility, validation obligations, and the option to retain a policy

Conditional analytical extension to the [qualification-finance model](qualification_finance.md). The [source audit](qualification_evidence.md) does not identify either an industrial acceptance threshold or a validation-cost slope. All numerical inputs below are synthetic. These are standard feasible-set and linear-inequality arguments, not a selected original contribution.

## A restriction on the claim that more experience can hurt

Let A(e) be the feasible deployment/investment plans after experience e, and let F(a) be terminal payer value, including all remaining obligations. If e2>=e1 implies A(e1) is a subset of A(e2), and the payoff of every retained plan is unchanged, then sup F over A(e2) is at least sup F over A(e1). Proof: every plan available before is still an admissible competitor afterward. The result does not require concavity, transferable cash, or a connected opportunity network.

Thus *free, optional* experience cannot reduce optimized private value when the old policy, rights, qualification and cash remain available. Negative transfer for a particular retrained policy does not refute this statement. Costly data acquisition, mandatory replacement, changed liability, loss of rights, or cash spent generating the experience can violate its assumptions. Compare those states explicitly. Higher realized performance need not imply greater value; greater freely usable choice weakly raises optimized value.

This is a decision-theoretic dominance bound, not a welfare result. Private optimization can still impose external effects. It also does not establish the value of an additional costly deployment.

## Smallest eligibility and validation model

Retain two financing dates and the fixed directed payment capacities of the existing model. At the start of the investment date, payers hold cash b; all experience-acquisition expenses are already included in b. For this comparative static hold b fixed, so additional experience is a free availability experiment, not an uncosted deployment choice. All costs and cash are normalized currency. The last period has no residual assets or unpaid support: V is total collected operating profit net of operating and terminal obligations; retaining cash is available.

A policy version indexed by incorporated experience x in [0,Ebar] attains deterministic validated quality q(x)=q0+alpha*x, alpha>0. This is a stylized service metric, **not** a probability inferred from benchmark scores. An externally specified matched service requires q>=qbar. Eligibility begins at L=max(0,(qbar-q0)/alpha). Until a physical service requirement is observed, qbar is an illustrative primitive only.

Deploying version x requires payer obligations k_a(x)=k_a0+gamma_a*x, with nonnegative k_a0 and gamma_a. These are retained adaptation, validation and integration obligations; the positive slopes represent a case in which broader modification requires more work. They are not measured learning curves and need not hold in another setting. Customer demand, operating costs, and contract capture determine a fixed V once the matched service is admitted, as in Model A. Above-threshold quality earns no additional price here. Price/volume responses or quality-dependent V would require a different calculation.

For each nonempty payer subset U define base funding slack S_U=b(U)+t(incoming U)-k0(U) and validation slope G_U=sum gamma_a. Funding version x requires x*G_U<=S_U for every cut. If any S_U<0 there is no feasible x>=0, since obligations only increase. Otherwise let

Ubar = min(Ebar, min over cuts with G_U>0 of S_U/G_U),

where an empty inner minimum is infinity. Combining eligibility and cash gives exactly the closed interval [L,Ubar], empty when L>Ubar. This follows directly from the prior necessary-and-sufficient funding cuts. Equality is feasible. This extends the earlier cost-decreasing threshold only to expose an alternative transition: learning can open technical eligibility while consuming scarce validation capacity/cash.

Under **mandatory incorporation**, the only candidate version is x=e. Its optimized value, including the option not to deploy, is B when e is outside [L,Ubar] and max(B,B-K0-G*e+V) inside, where B=sum b, K0=sum k0 and G=sum gamma. Feasibility can disappear as e rises. This does not presume that firms actually must adopt a new version; it isolates the assumption needed for the adverse example.

Under **optional incorporation**, available versions satisfy 0<=x<=e, and their certification/rights remain valid. Since V is fixed and costs are nondecreasing, x=L minimizes cost among eligible versions. Value is B if e<L or L>Ubar, and max(B,B-K0-G*L+V) otherwise. It is weakly increasing in available experience. The optimum may preserve an earlier qualified version despite possessing more data. With G=0 there can be ties; L remains a minimizer. With negative or nonlinear slopes this explicit formula may fail, but nested-set dominance still applies if retaining old plans is genuinely feasible.

## Exact counterexample and repair

Take b=(5,3), k0=(2,1), gamma=(0,1), no early transfers, Ebar=3, q0=0, alpha=1 and qbar=1. V=10 is the combined operating profit from the prior customer-demand contract; no extra option premium is added. The operator cut imposes x<=2; the combined-cash cut allows x<=5 and is not binding. Thus eligible, financeable versions are [1,2].

| Available experience e | Mandatory-version optimum | Optional-version optimum |
| --- | ---: | ---: |
| 0 | 8: retain cash | 8: retain cash |
| 1 | 14: deploy x=1 | 14: deploy x=1 |
| 2 | 13: deploy x=2 | 14: retain and deploy x=1 |
| 3 | 8: retain cash; x=3 unfunded | 14: retain and deploy x=1 |

At x=1 obligations are (2,2), and equal operating-profit shares (5,5) yield terminal balances (8,6), so both payers improve on (5,3). At x=2 the balances are (8,5). A permitted one-unit provider-to-operator contribution makes x=3 financeable, but does not force its adoption or make it cheaper. Aggregate value then is 12 under mandatory incorporation, still 14 under optional incorporation. Individual transfers and profit shares here are implementable stipulated contracts, not equilibrium bargaining results.

This **rejects the unrestricted claim** that more freely available experience can lower optimized profit. It preserves the narrower possibility that a particular forced or costly update lowers value. A claim that a learning deployment is harmful must account for its acquisition cash, rights or irreversibility instead of silently removing the old policy from the choice set.

## Empirical consequence and next question

The useful measurement is not just whether a new policy scores higher. Record whether an old policy can legally and physically remain deployed, whether its qualification persists, which validation work is repeated after a version change, and which payer funds that work before collection. Mandatory upgrades and expiring approvals are hypotheses requiring evidence, not assumed industry facts. The present source slice supplies none of those terms.

Next integrate *costly choice of initial deployment* with the eligibility interval only if doing so changes a conclusion beyond the already-known constrained-investment result. Otherwise retain this note as a counterexample check and teaching boundary, not a separate paper claim. Reproduce the exact table and interval checks with `python scripts/check_eligibility_free_disposal.py`.
