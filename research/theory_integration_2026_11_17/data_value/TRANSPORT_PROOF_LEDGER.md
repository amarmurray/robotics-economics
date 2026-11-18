# Transport, demand, and support — proof/claim ledger

Companion to [TRANSPORT_AND_SAFETY_IDENTIFICATION.md](TRANSPORT_AND_SAFETY_IDENTIFICATION.md), 18 November 2026. An executed synthetic model is *not* a proof or empirical finding. The original integrated proof history and all prior restrictions remain in force.

| Statement | Status and proof | Restrictions / falsifier |
| --- | --- | --- |
| T1 demand-weighted matched route difference | Conditional identity from a common optimized production payoff on each site × demand × order window | Single additional whole accepted B/C bundle, comparable retained incumbent, cost counted once, common pre-action target distribution, route-isolated lineages; invalid without redefining \(z\) if \(\Delta\) and acceptance co-vary |
| T1 robust lower \(L=\sum\mu(b-k-\Delta u)\) | Proved by nonnegative weighted sum of conditional upper bounds; sharp only when endpoints are jointly attainable | Uniform pathwise feasible menu required first; latent fixed-world constraints may rule out simultaneous endpoints |
| A pooled matched upper bound transports unchanged | **Rejected**; two admissible site laws yield observed \(d=.08\) versus target \(d=.23\), R−E +.36 versus −.84 | Same route component marginals at both sites; source versus target site weights differ |
| Missing-support mass is harmless when most sites are matched | **Rejected**; sharp bound \(b-\Delta[(1-\epsilon)d_m+\epsilon u_m]\); threshold 1/12 for declared synthetic values | Missing \(u_m=.4\) uses valid Fréchet bounds; not a confidence interval or field-coverage estimate |
| Stable technical quality yields stable economic ranking | **Rejected**; with stable \(d=.1\), \(b=1\), \(\Delta=8\to12\) flips R−E +.2 to −.2 | Customer value/capture changes; not a claim that one physical service or contractual tariff has a verified price |
| T2 report-conditional pathwise resource certification | Proven by definition of support-based feasibility plus constructed same-marginal W0/W1 worlds | Cannot infer safe continuation from marginal high-recovery share and marginal report frequency; both worlds must be admitted if joint remains unknown |
| One set of target-site upper differences certifies every adaptive data policy | **Rejected**; T1 only compares fixed feasible R/E after conditioning, not specialist, deliberate grounding, diagnostics or arbitrary feedback decisions | Need common full-policy identification set \(\Theta\), report/action coupling, demand selection and nonrectangular treatment |
| Positive independent source-data transfer implies positive economic increment | **Rejected** by earlier integrated envelope results | Customer demand, complete-service qualification, resource shadow prices and competent old policy determine value |
| More optional free data can never help | **Rejected direction**; larger optional information/action sets weakly improve optimized value if old policies and rights remain feasible | Forced retraining, time, compute/curation or irreversible embodiment can be harmful |
| New robotics scientific theorem or calibrated industrial benchmark | **Not established** | Pearl/Bareinboim transportability, Stuart et al. external validity, Manski decision theory, Fréchet bounds and support-safe control are prior art; no audited customer field data |

## Direct finite exactness argument

For identical component marginals \(p\), a joint B,C success probability \(q\in[\max(0,2p-1),p]\) has cells \(P(00)=1-2p+q\), \(P(10)=P(01)=p-q\), \(P(11)=q\). For \(p_R=.75,p_E=.9\), A has \((q_R,q_E)=(.75,.8)\), B \((.5,.85)\). Every cell is nonnegative. The study/target mixes are \(\nu=(.9,.1)\), \(\mu=(.4,.6)\). All result arithmetic is in the main chapter and [transport_safety_results.json](transport_safety_results.json); no indirect statistic can turn a sample weighted mean into its distinct target weighted mean without a valid transport assumption.

For target missing-share \(\epsilon\), measured upper \(d_m=.1\), uncovered upper \(u_m=.4\), and \(b=1,\Delta=8\), \(L=1-8(.1+.3\epsilon)=.2-2.4\epsilon\). The bound is positive exactly for \(\epsilon<1/12\), weakly nonnegative at equality, and unattested beyond it. Measured \((q_R,q_E)=(.7,.8)\) and unmeasured \((.5,.9)\) achieve these extremes with valid copulas, establishing sharpness under rectangular sitewise possibilities.

For recovery, two distributions have the same marginals \(P(good)=.5\) and \(P(high)=.1\). W0 has no good/high cell; W1 has good/high mass .1. A report-good-only target attempt with initial resource 1, low terminal resource 1, high terminal resource 2 and budget 2.1 meets every supported path under W0, but would require 3 on a supported path under W1. An unexecuted potential high recovery is not recorded as a physical overrun. A policy feasible against the identified set must use a safe fallback in W1 or reserve at least 3.

## Verification boundaries

Source [transport_safety_identification.js](transport_safety_identification.js) is an isolated CPU-only synthetic exact-source test with four-cell validity, sample/target reweighting, sitewise grid extremum, demand-change reversal and recovery-joint-support checks. The result JSON records its assertion count and exact inputs. It does not run hardware, verify transfer learning, certify safe action, validate data, measure a market, replace historic CI, or establish independence from the assistant's own derivation.

## Bounded closest-prior-art audit

Publisher-abstract checks on 2026-11-18: Pearl/Bareinboim AAAI 2011 (causal transportability), Stuart et al. JRSS A first online 2010 (trial-to-population weighting), Manski Econometrica 2004 (heterogeneous treatment rules), Zivich et al. Epidemiology 2024 (positivity failure), Hudgens/Halloran JASA 2008 (interference). URLs and identified applicability restrictions are in the chapter. The literature is *not* comprehensively reviewed; sources have not been fully reproduced. No theorem number/credit beyond its actual mathematical antecedent is asserted.
