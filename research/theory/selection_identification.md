# Financing can mask the learning value revealed by project selection

Candidate analytical identification result, not a selected paper contribution. The exact observational-equivalence example below is synthetic. It changes a financing assumption around an inspected source diagnostic; it does not refute that diagnostic under the source's own assumptions, or establish that financing explains its pharmaceutical evidence.

## Closest source and version discipline

Alexander P. Frankel, Joshua L. Krieger, Danielle Li and Dimitris Papanikolaou, *Evaluation and Learning in R&D Investment*, NBER Working Paper 31290, May 2023, **revised December 2024**, DOI [10.3386/w31290](https://doi.org/10.3386/w31290). [Current primary PDF retrieved](https://www.nber.org/system/files/working_papers/w31290/w31290.pdf), November 16, 2026 UTC, SHA-256 `b97e429aa0aaf754654f57cd236d1714798fc9f8497130b7b36ad8e751c08416`. The initially discovered May 2023 rev0 has a different hash (`46ae8ad87183e58888d4aaeadf8e956df1abbcf17848d9f51c05be9653d8a15a`) and proposition numbering. The analysis here uses the December 2024 revision, not an assumption that versions match.

Inspected §3.1–3.3 (printed pp.12–18), the value decomposition and maintained assumption, and Appendix A.3's Proposition 3.2 proof (p.58, visually checked after text extraction). The full empirical dataset, causal interpretation, every multistage lemma and other source propositions are not replicated here. An algebraic sign inconsistency was visible in the older rev0 proof after equation (16); it is not imported as an assumption. The governing maintained restriction is that private learning value is below initial development cost.

**Mechanism card.** A firm considers an incremental or novel first-period project. Both start with the same revenue and success distributions, but incremental projects receive an extra screening signal that eliminates some failures. After screening, the firm sees revenue and decides whether to pay development costs. Developing a novel project improves evaluation of possible successors; a fraction of those opportunities is appropriable by the firm. Private continuation gain depends on discounting, successor arrival and appropriability. The formal model does not impose a separately binding initial financing gate on the development choice.

**Author diagnostic, reconstructed.** Economic development thresholds Rbar_N solve direct value minus cost plus the novel project's private continuation benefit equal to zero. Under the common revenue distribution and the source's independence/screening assumptions, the development rate conditional on entering preclinical testing is 1-F_R(Rbar_N). Expected revenue conditional on successful development is E[R | R>=Rbar_N]. The former falls and the latter rises with the threshold. Proposition 3.2 therefore links the ordering of novel/incremental thresholds to the ordering of these observables. It is not a claim that arbitrary cross-market deployment rates and revenues identify learning value without controlling opportunity sets and selection.

The source already formalizes willingness to accept lower current direct returns for more future learning. That tradeoff is prior art, as is staged discovery in the [Caplin audit](staged_discovery_prior_art.md).

## Minimal financing extension

Work after the initial screen. A project of type n has success probability pi_n, successful revenue R, initial cost C and private future learning value L_n, all known to the firm. Revenue is independent of success conditional on type, and both types draw R from the same continuous distribution. There is one development stage, a permitted simplification M=1 of the source's ladder; the future learning term is reduced form, not a simulation of its full successor economy. Learning value is not paid immediately or pledgeable for this initial loan. Interest and discounting are absorbed into these values; the example uses zero interest.

The unconstrained economic threshold is T_n=(C-L_n)/pi_n. Assume 0<=L_n<C so T_n is positive. The firm has current cash B<C, and the specified credit contract advances no more than a_n*R, with 0<a_n<=pi_n. A borrower can repay the required loan from a suitable success-state share without negative payments. This is a **given advance restriction**, not a claim that optimal contracting necessarily produces a_n. The actual credit terms must be observed or separately derived; perfectly pledgeable future learning profits could change them.

Initial funding adds the threshold F_n=(C-B)/a_n. The observed development threshold is

Theta_n=max(T_n,F_n).

Proof: development requires both nonnegative private surplus and the date-zero funding inequality. Their intersection is exactly R>=Theta_n. Principal is repaid later, so the loan is not added to private surplus. The source's truncation argument still describes observable selection, but it now recovers Theta, not necessarily T. The change is to the interpretation of the inferred threshold, not the algebra of truncation.

For known C, pi, F and an observed interior cutoff Theta:

- If Theta>F, the financing gate is slack at the margin, T=Theta and L=C-pi*Theta within this model.
- If Theta=F, T<=F, hence L>=C-pi*F. Together with 0<=L<C this is an interval, not a point. Values in this interval give the same first-project selection rule.
- Theta<F contradicts the maintained model/measurement assumptions.

This is a conditional partial-identification result with ideal population observables. Finite data, unobserved rejected opportunities, uncertain costs and heterogeneous terms require additional bounds; no statistical confidence interval is claimed.

## Exact observational equivalence with different learning priorities

Let R be uniform on [0,10], C=16/5, initial cash B=7/5 and the lender advance at most three quarters of expected direct revenue: a_n=(3/4)*pi_n. Set pi_I=4/5 for screened incremental opportunities and pi_N=2/5 for novel ones. These can arise from the same pre-screen success prior 2/5 when the incremental signal eliminates 5/6 of failures. Condition the comparison on passing the screen, as the source diagnostic does; do not compare raw awareness counts instead.

Incremental learning value is zero, so T_I=4, while F_I=3 and Theta_I=4. Consider two novel-project environments with all observed first-project primitives and financing terms identical:

| Environment | Novel private learning value | Economic T_N | Finance F_N | Observed Theta_N | Develop probability | Mean successful revenue |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Learning dominates evaluation in threshold ordering | 12/5 | 2 | 6 | 6 | 2/5 | 8 |
| Evaluation dominates learning in threshold ordering | 6/5 | 5 | 6 | 6 | 2/5 | 8 |

For incremental projects the corresponding develop probability is 3/5 and mean successful revenue seven. Both environments therefore show fewer novel developments and higher revenue conditional on their success, even though their *economic* threshold orderings relative to T_I=4 differ. The entire first-project joint distribution of type-conditional revenue, entry, success, required loan and repayments is the same, not just these two moments. Future successor outcomes/value are excluded from this equivalence; observing them could distinguish the environments.

The financing restriction is internally feasible: at the novel entry boundary R=6 the required loan is C-B=9/5. Repayment conditional on success is (9/5)/(2/5)=9/2, exactly three quarters of successful revenue. It does not require a claim exceeding project revenue. The learner's future value is not counted as lender collateral or as current cash.

Even if the observer knows the financing terms, Theta_N=F_N=6 only gives L_N in [4/5,16/5). The threshold ordering switches at L_N=8/5, which lies inside this interval. Hence those terms plus first-project observations still do not determine which learning priority is present.

## A discriminating variation and its limits

Increase cash to B=23/10, holding opportunities, costs, quality, credit fractions and learning values fixed. The novel finance threshold falls to three; the incremental economic threshold remains four. The high-learning environment now has Theta_N=3, development probability 7/10 and mean successful revenue 13/2. The low-learning environment retains Theta_N=5, probability 1/2 and mean successful revenue 15/2. Cash variation separates the formerly identical first-project policies. If the cash change also changes demand, quality, project availability, control rights or bargaining, this interpretation need not hold.

A practical validation design would need the denominator of genuinely offered/qualified opportunities, rejected as well as accepted projects, cash and credit terms before the decision, complete upfront costs, and comparable prospective revenue/quality measures. Exogenous liquidity variation could be informative if its exclusions are defensible. An announced equity round is **not automatically such an instrument**. Cross-market robot performance scores and aggregate vendor revenues do not satisfy the source diagnostic's conditioning assumptions.

This result narrows a possible first paper toward what deployment choices can reveal about learning value under finance. Its prior-art status remains unsettled: maximum-of-threshold censoring and constrained revealed preference are standard ideas. The exact extension is useful because it targets a specific observable diagnostic and a measurement that can distinguish explanations; that usefulness alone is not a publishable novelty claim.

Replication: `python -m model.selection_identification`; `python -m unittest tests.test_selection_identification`.
