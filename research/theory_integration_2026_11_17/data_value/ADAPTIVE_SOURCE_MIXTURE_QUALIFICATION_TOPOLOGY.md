# Source-mixture choice under alternative and complementary qualification

23 November 2026 · *When Capabilities Become Production* · continuation of \`FROM_HETEROGENEOUS_EVIDENCE_TO_PAID_PRODUCTION.md\`. The November 22 scientific gate is **OPEN**. This chapter is conditional economic theory and an exactly enumerated synthetic test, not measured robotics returns, an estimate of transfer coefficients or a claim to general mathematical priority.

## The same question, one date later

The previous support-aware kernel note bounds one admissible G/T action's joint target-qualification, original-buyer and worker-free outcome. What changes when a first, production-generated field record informs a subsequent choice to acquire an additional recovery/teleoperation record, and the records qualify a customer recipe **as alternatives or as complements**? This is the missing link between a source-to-qualification data map and an investment among more source data (P), licensed grounding (G), and a new independently staffed embodiment (E). The customer pays for a qualified, safely accepted service, not for a benchmark score. Each additional record has its own admission, curatorial, compute, worker and rights costs.

The result below is deliberately an analytical submodel of the existing dynamic firm problem. It identifies a **qualification-topology interaction**, an endogenous source-selection rule and the difference between an oracle knowing the cross-source law and an implementable precommitted allocation. A subsequent production generation can change that law; invariance across periods is not assumed.

## 1. The economic outcome table and a two-source identity

Let \`F,T ∈ {0,1}\` be source-specific *validated usefulness indicators* after a fixed, versioned, admissible learning-and-test protocol. \`F\` comes from field work already performed; \`T\` would come from a separately qualified recovery/teleoperation intervention, independent audit, simulation or another permitted source, with its **specific source type explicitly recorded**. This notation does not identify all those modalities with one kind of data. \`T\` is a generic second-source indicator in the theorem, not a claim about teleoperation sufficiency.

For a customer and a fixed physical production menu, let \`w_ij\` be the **incremental optimized paid-service contribution** if the validated indicators are \`F=i,T=j\`. It is measured relative to the safe existing recipe, after acceptance deadlines, original customer offers, available worker slots and displaced qualified jobs are respected. It is net of routine serving costs, but **before** the explicit acquisition cost of \`T\`. The same target job is never paid twice. \`w_ij\` can differ by customer and embodiment. Holding this four-cell payoff table fixed, put \`p=Pr(F=1)\`, \`q=Pr(T=1)\` and \`x=Pr(F=1,T=1)\`. Every compatible common law has

\`\`\`
             T=0           T=1
F=0       1-p-q+x        q-x
F=1          p-x           x
\`\`\`

and the sharp Fréchet domain is \`max(0,p+q-1) ≤ x ≤ min(p,q)\`. Direct enumeration gives

\`E[w(F,T)] = w_00 + p(w_10-w_00) + q(w_01-w_00) + x(w_11-w_10-w_01+w_00).\`

Thus the economically relevant cross-source interaction is

\`Δ = w_11 - w_10 - w_01 + w_00.\`

At fixed source marginals, increasing the overlap \`x\` changes expected contribution by \`Δ\` per unit of overlap. This is the established multilinear / supermodularity identity, now interpreted on **optimized accepted customer production** rather than model accuracy. Under a substitutable complete-service recipe (\`w_00=0,w_10=w_01=w_11=m\`), \`Δ=-m\`. Under a genuinely complementary two-stage recipe (\`w_00=w_10=w_01=0,w_11=m\`), \`Δ=+m\`. Identical positive technical success marginals therefore have opposite economic correlation comparative statics. Negative \`Δ\` is not a claim that a free optional dataset reduces optimized firm value; it states that overlap makes *two nominally useful sources redundant at fixed marginals*.

This identity has conditions: the source indicators must represent comparable qualified potential results, the payoff table must be fixed and both indicators must have a joint causal meaning under the same admissible policy. If buying \`T\` changes the first source's training protocol, buyer orders, worker occupation, hardware or qualification rule, its program-specific kernel must be valued again and the four fixed cells cannot simply be transported. Demand/worker/quality may instead be included in a larger joint outcome \`ω\` and \`w_ij\` then refers to its lawfully identified conditional expected contribution. Mere marginal success rates do not fix those conditional values.

## 2. Deliberate acquisition after production-generated evidence

At t3, the firm already holds an admitted \`F\` record generated while completing production. At t4 it sees \`F=i\`, and may allocate a scarce qualified validation/support slot to acquire, test and release \`T\`. Its incremental all-in acquisition/displacement cost is \`c_i ≥ 0\`, including a versioned target grounding and an actual opportunity cost rather than an extra fictitious wage charge. At t5 the firm takes the best feasible qualified recipe for a customer's original order. The old policy remains available if lawful and physically feasible. Let \`B_i = w_i0\` be the paid-service baseline without \`T\`; let \`L_i = w_i1-w_i0\` be the improvement *if* \`T\` is successful under matched conditions. When \`L_i ≥0\` and the outcome law is known, the optimal post-\`F\` continuation is

\`V*(p,q,x) = Σ_i Pr(F=i) B_i + Σ_i max(0, Pr(F=i,T=1)L_i − Pr(F=i)c_i).\`

This is simply backward induction: at each observed \`F\` choose between retaining the old qualified recipe and buying a second source. More generally, if failed \`T\` changes the continuation state, replace the terms with the corresponding full Bellman difference; the displayed shortcut assumes failed validation leaves the safe menu intact. If the conditional gain can be negative, buying \`T\` is optional, so its value is truncated at zero. Positive transfer under a forced training recipe and value from optional *availability* of additional evidence are distinct concepts.

For a **substitutable recipe** with target upside \`m_O\`, \`F=1\` already qualifies the paid order, so \`T\` matters only when \`F=0\`. With common audit cost \`c\`:

\`V_O^*(x) = m_O p + max(0, m_O(q-x) - c(1-p)).\`

For a **complementary recipe** with upside \`m_A\`, both source qualifications are needed, so \`T\` matters only when \`F=1\`:

\`V_A^*(x) = max(0, m_A x - c p).\`

The right to act on a source result is economically essential. If the audit arrives after the customer's deadline, the incremental paid value from this order is zero; later effects belong in the next state. If an audit uses the same scarce worker as customer service, \`c\` must include displaced production or the feasible transition must model both explicitly. These equations do **not** authorize intervention or replace an absent G/M treatment group with R history.

## 3. Exact common-law synthetic test

Hold \`p=q=1/2\` and let \`x=k/20\`, \`k=0,1,…,10\`. There are exactly 20 equally weighted latent atoms with counts \`(n00,n01,n10,n11)=(k,10-k,10-k,k)\`; every law has the same separate F and T success rates. The first-source observation is from already paid and legitimately retained work, so its prior contribution and costs cancel in this *incremental* comparison. A second licensed validation has economic cost \`c=1/10\` including shadow cost of a worker/compute slot. Two **alternative** downstream production architectures use the same validated sources but face different customer-recipes:

- O: an alternative-embodiment route; either admitted source can qualify the complete accepted service; incremental paid contribution if qualified \`m_O=1\`.
- A: a two-stage arm+mobile kit; the complete paid order requires both independent source qualifications; incremental paid contribution if qualified \`m_A=3\`.

These payoffs are deliberately stipulated normalized complete-order margins, **not** benchmark-percent conversions, observed customer prices or evidence that either architecture is deployed. O and A are separately committed customer/embodiment architectures; they are not costlessly usable simultaneously. The safe existing program R has incremental value 0; an independent embodied-and-staffed E program has normalized incremental contribution 3/4 net of its real separate capital and staffing expenditure. A program with additional source production P belongs to the general optimization but is not assigned a fictional numerical return here.

For this economy, with known \`x=k/20\`, the **oracle after learning the common law** values are

\`V_O^*(k) = [10 + max(0,9-k)]/20,\qquad V_A^*(k) = max(0,3k-1)/20.\`

The exact checks show:

| Shared latent overlap | O known-law optimum | A known-law optimum | Independent E | Best program |
| --- | ---: | ---: | ---: | --- |
| \`k=0\` (complementary evidence across sources) | 19/20 | 0 | 3/4 | O |
| \`k=5\` | 7/10 | 7/10 | 3/4 | E |
| \`k=10\` (maximally redundant evidence) | 1/2 | 29/20 | 3/4 | A |

A low overlap favors the **alternative** evidence route; high overlap favors the **jointly required** route, even though every single-source qualification rate is unchanged. At intermediate overlap, an independently qualified embodied capacity addition dominates both. This is a change in qualification topology and source dependence, not a new draw of the same one-source cost parameters.

**The oracle distinction is material.** The optional formulas above use knowledge of \`x\` to decide whether the second source is worth acquiring. A manager who has seen only marginal source scores cannot use that future information. For any \`k\`, one can instead precommit to O and audit \`T\` exactly when F=0, yielding \`(19-k)/20\`; or precommit to A and audit \`T\` exactly when F=1, yielding \`(3k-1)/20\`. Neither rule observes an untried \`T\` outcome first.

For comparable independent deployment clusters, allocate probability 3/4 to O's committed rule and 1/4 to A's committed rule. Its ex ante contribution is

\`(3/4)(19-k)/20 + (1/4)(3k-1)/20 = 7/10\`

**for every common joint law in the stated family.** It is an implementable randomized *portfolio* hedge in expectation, not a guarantee on one indivisible order. This demonstrates why independent rowwise worst cases are insufficient when both architectures share the same underlying source law: their payoffs move in opposite directions. A deterministic single-architecture policy using no source-overlap signal can guarantee only 1/2 here (O without the second-source audit), while the mixed source policy guarantees 7/10. Nevertheless, E yields 3/4, so it wins the maximin comparison under these specified costs. The common-law clairvoyant minimum of max(O,A) is 7/10 at k=5; that number is *not itself* an information-feasible choice. The 3/4–1/4 mixed rule is an explicit implementable policy attaining 7/10 without observing k.

For fixed first-source mass and known T marginal, a paired conditional audit in just one F stratum can identify x algebraically, **provided** that stratum's intervention kernel is transportable to the desired program and its observation probabilities are positive. Without a lawful known T marginal or when production policy changes its data supply, the other stratum must also be studied. O selectively audits F=0, A selectively audits F=1. Comparing the two customer architectures on selected old logs without admitting both risk sets leaves the cross-source law and causal T effect unidentified.

## 4. The economically sufficient dynamic state and testable counterfactual

In the full P/G/E/R system, update a state \`s=(rights, provenance, corpus mixture, physical policy/embodiment, joint qualification, original buyer budgets/offers, worker queue, deadlines, beliefs)\`. With source acquisition action \`a\`, the lawful kernel \`K_z(s', y | s,a)\` determines new evidence and who can use it. A finite-horizon policy obeys

\`J_t(s)=max_{a∈A_z(s)} Σ_{s',y} K_z(s',y|s,a)[r_z(s,a,s',y)+βJ_{t+1}(s')]\`.

The two-source identity is a **single-transition payoff projection**. Recursion means that decisions about which source to sample also change the admissible future corpus, model errors, failure arrivals and opportunity set, so \`K\` and the future qualifying events become policy-dependent. This is why the same \`x\` should **not** be assumed stationary after an intervention changes the robot population or the recording rule. Retaining only one source count, rather than origin/right/version, is not generally a sufficient statistic for deciding how to acquire the next source.

There is a precise testable challenge to additive positive transfer: obtain *matched* source-to-target updates (F only, T only, both, neither), with accepted joint recipe qualification and a priced, separately documented production opportunity. Hold evaluation compute and target protocols matched, randomize source admission within rights and safety gates, and record original buyer/no-order and worker occupied/free events. If the accepted-service payoff satisfies \`w11-w10-w01+w00>0\` after resource accounting, the sources are economically complementary for that specified customer/recipe; if negative, substitutable. An individual technical positive transfer cannot settle the sign. Repeat under two demand mixes and two embodiments to distinguish customer complementarity from a model-transfer artifact. The observation mechanism must cover nonselected failures and audits; policy-selected logged interventions alone are insufficient.

**Prospective evidence design:** [ADAPTIVE_SOURCE_MIXTURE_EVIDENCE.md](ADAPTIVE_SOURCE_MIXTURE_EVIDENCE.md). **Exact reproducible checker:** [adaptive_source_mixture_exact.js](adaptive_source_mixture_exact.js); instructions in [ADAPTIVE_SOURCE_MIXTURE_REPLICATION.md](ADAPTIVE_SOURCE_MIXTURE_REPLICATION.md); separate [exercises](ADAPTIVE_SOURCE_MIXTURE_EXERCISES.md) and [solutions](ADAPTIVE_SOURCE_MIXTURE_SOLUTIONS.md).

## 5. Scope, closest antecedents and next proof gap

Farboodi, Koh and Xia's *Data-Driven Automation*, NBER WP 35320, June 2026, already treats task-specific data, endogenous accumulation and spillovers, and its section 5 and Appendix B already discuss the future value of data and data complements. The new exercise is not a claim to invent those elements. The two-source expectation is elementary multilinear algebra; dynamic source admission uses standard finite-horizon control; the counterexample follows Fréchet dependence bounds and classical partial identification. Murphy (2003), *Optimal Dynamic Treatment Regimes*, gives the relevant sequentially randomized/g-formula identification benchmark (different application domain). The synthetic source mixture does not identify commercial robotics training effects, rights or willingness to pay.

Primary references checked 23 November 2026:
- Farboodi, Koh & Xia, *Data-Driven Automation*, NBER working paper 35320 (June 2026), https://www.nber.org/papers/w35320
- Murphy, *Optimal Dynamic Treatment Regimes*, JRSS B 65(2) (2003), https://academic.oup.com/jrsssb/article/65/2/331/7092852
- Li, Litvin & Manski, *Partial Identification of Personalized Treatment Response with Trial-reported Analyses of Binary Subgroups*, arXiv 2208.03381 (2022), https://arxiv.org/abs/2208.03381
- Earlier integrated source/qualification note: [FROM_HETEROGENEOUS_EVIDENCE_TO_PAID_PRODUCTION.md](FROM_HETEROGENEOUS_EVIDENCE_TO_PAID_PRODUCTION.md)

**Actual next proof obligation, not a new topic:** make the next source-mixture probability \`p_{t+1},q_{t+1},x_{t+1}\` depend on current qualified production, sampling, recovery and customer demand; derive a common-law, nonrectangular dynamic value/partial-identification bound with *feasible*, legally supported audits that may themselves occupy worker capacity. Keep physical qualification and original buyer service in the same transition. Test whether the four-cell payoff projection remains sufficient when the source law changes endogenously, and quantify when the independent E option substitutes for further source acquisition. The November 29 theory/empirical backbone remains a target, not a passed acceptance gate; final December 25, 2026 23:59 America/New_York unchanged.
