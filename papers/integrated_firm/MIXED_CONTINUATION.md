# Intermediate mixed continuation and the first exact incentive interval

November 26, 2026. Input main `85ec881b7ef01c31954c64087f8ebf9457ec78f5`. This is a continuation of [globally reoptimized thresholds](GLOBAL_EQUILIBRIUM_THRESHOLDS.md), not a new technology or calibration.

## Economic closure

A firm's current policy affects the public state (including lab scope, qualification, archives and hardware) at which rivals act later. A pure-only algorithm can therefore fail in an off-path subgame even when the equilibrium root action is pure. Dropping that subgame would invalidate root deviation checks. The finite game is solved by backward induction: every action pair receives the expectation of the selected downstream equilibrium values, not a frozen program payoff. Independent mixed actions are legal; each support action must maximize expected private continuation value, including the cost of current resources. This is standard finite-game equilibrium logic, not a novelty claim.

For a nondegenerate two-action support with payoff arrays A and B, row 1 probability p and column 1 probability q (indices zero and one), indifference requires q=(A10-A00)/(A01-A00-A11+A10) and p=(B01-B00)/(B10-B00-B11+B01). Fractions must lie in (0,1); then check **all** original retained actions, not merely the support. A two-action support is not guaranteed to exist in a general finite game. The algorithm fails explicitly if none certifies, or if the integer scale cannot carry its denominator.

Use the accepted prefunded block calendar (1,1,5,5), kit price 4, entry date 3, and the same operating, research, hardware, ordinary learning and outside alternatives. Pure equilibria have priority; otherwise enumerate nondegenerate 2-by-2 supports and rank certified candidates by the specified total-payoff rule, then firm 0. This is a selection convention, not the whole correspondence. Each date-two joint support denominator divides 125. Multiply the original integer value scale by 125 at dates two and one, and carry that scale through expectations. Forward state masses use the corresponding common denominator at each date, even when the state is pure. Integer checks and the dated cash/resource replay prevent an approximate continuation from silently becoming an exact solution.

## The mechanism in the first failed pure subgame

Both firms start this subgame with an arm, a retained physical archive, no qualifications and open labs. The support actions both produce physical service and train on their own archive with probability 1/2; the only distinction is whether the lab is closed (C) or kept (K) for the next block. The continuation-inclusive net value matrix (excluding inherited cash) is:

| | Rival C | Rival K |
|---|---|---|
| C | 133,128 | 130.5,131 |
| K | 132.25,129.25 | 131,129.125 |

Firm 0 prefers C against C and K against K; firm 1 prefers K against C and C against K. These opposite best responses eliminate a pure equilibrium in this retained support. The full menu of 32 actions per firm is checked. Indifference gives p=24/25, q=3/5, and values 131.5 and 129.2. The asymmetry is induced by the chosen downstream equilibrium policy (including label-based tie breaking), not by asymmetric technologies at this state. Under lower-total pure selection the exclusive root result is identical and no intermediate mix is needed; thus the disappearance of pure continuations is selection-dependent, not a universal structural result.

## First interval-wide mixed incentive certificate

Introduce a nonnegative fee f on retaining one's lab **at this date-two subgame only**, paid from prefunded cash; all other states, legal actions and downstream policies remain fixed. The fee is an additive stage payoff for each action with next scope ng=1. Fractional monetary units are a relaxation of the original integer cash grid; the prefunding slack ensures unchanged resource feasibility and the cash quotient remains valid. This is not a global kit-price or lab-cost parameter perturbation.

The support indifference equations give q(f)=3/5+4f/5, p(f)=24/25-8f/25. These are interior for 0<=f<1/2. At f=1/2 the second firm's mixing probability reaches one. Against the stated affine rival mix, every deviation's expected payoff is affine: the fee depends only on own action and hence has no interaction with the rival randomization. A support payoff minus each deviation is affine too. Nonnegative slacks at both endpoints therefore certify the whole closed interval, by linear interpolation; indifference also holds throughout. All 32 original actions of each firm have nonnegative exact integer-scaled slacks at both endpoints (the stored result gives each slack numerator and denominator). The interval is maximal for this specified interior support along the nonnegative direction because q>1 beyond 1/2. The endpoint is a weak equilibrium; no claim is made about the next support or other equilibria. This is an actual incentive-region certificate for the conditional subgame, not merely a sampled break-even crossing.

More generally affine payoff coefficients with parameter-dependent indifference denominators give rational mixing probabilities and polynomial sign tests after partitioning by denominator sign. Downstream mixed values can make upstream incentives rational rather than affine. The next computational obligation is to certify whole dynamic profiles and their selection regions, not extrapolate this conditional interval.

## Solved root and economic comparison

| Investment regime / selection | Generated wealth per firm | Accepted jobs | Customer surplus | Intermediate mixed states |
|---|---:|---:|---:|---:|
| Exclusive cap 2, higher-total pure-first | 160 | 44 | 88 | 9 |
| Exclusive cap 2, lower-total pure-first | 160 | 44 | 88 | 0 |
| Exclusive cap 1, higher-total pure-first | 160 | 44 | 88 | 9 |
| Concurrent cap 2, higher-total pure-first | 163.625 | 42 | 84 | 0 |

The exclusive root orders then assembles mobile robots, closes labs and does not learn. Its equilibrium was previously unresolved; the computed value now matches the old diagnostic P value, for a verified reason rather than by assumption. The concurrent alternative raises combined generated private wealth by 7.25 while losing two early accepted jobs and four customer-surplus units. The qualification cost return and market opportunity cost, rather than an increased physical output frontier, explain the tradeoff. No welfare ranking follows without accounting for real resource costs and ownership transfers.

The primary exclusive solve evaluates 1,108,797 reduced profiles in 3,898 memoized public states and checks 114,578 original retained-menu deviations, including nine mixed states. Exact backward payoffs and forward dated balances agree. Four comparisons were executed in the same engine; the primary result replayed exactly. Source SHA-256 checks bind the three inherited files. This is not an independent implementation and does not enumerate mixed equilibria when pure equilibria exist, degenerate or larger supports, or every possible selection. No empirical parameters were inferred. Source branch histories remain unchanged.

Reproduce in this directory with `node mixed_continuation.js`; [implementation](mixed_continuation.js) and [full exact results](mixed_continuation_results.json). The historical global-threshold result retains its original pure-only open status as provenance; this extension supplies the resolved comparator.

Next: Extend the exact local incentive certificate to complete contingent profiles across parameter regions, starting with a common kit-price or research-cost perturbation. Propagate mixed rational continuation values and track denominator changes, legal-menu changes, and selector inequalities separately; retain ordinary learning and outside research. Then vary service timing, qualification/transfer probabilities and costs, and test within-block contingent learning, binding finance, directed archives, common latent reports and input-market closure. Long-run stability requires a solved repeated/infinite-horizon economy. Preserve November 27 recursive-pilot, November 29 program, December 2 theory-week, December 6 contribution and December 25 final gates.
