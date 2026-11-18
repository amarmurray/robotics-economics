# Separate solutions: productive teleoperation and economic data value

## 1. Service-price mapping

Incremental value is
\(5[\max(0,w-2)-\max(0,w-6)]\).
The values at w = 1, 3, 6, 8, 12 are 0, 5, 20, 20, 20.

At high enough payment both recipes deliver the same quantity, so the incremental gain is the cost saving, not an unbounded multiple of revenue. A capacity difference, demand response, different service quality, fixed qualification cost, customer bargaining or an incumbent contract can change the mapping. Do not count the existing alternative's entire revenue as newly created by learning.

## 2. Rational arithmetic

Let H be reusable transfer and + the favorable diagnostic.

\(P(+)=\frac14\frac{19}{20}+\frac34\frac1{20}=\frac{11}{40}\).

\(P(H\mid +)=19/22\).

\(P(-)=29/40\) and \(P(H\mid -)=1/58\).

After grounding, buying the source sacrifices two current contribution units. Its expected future gain is \(20P(H\mid Z)\). After + it is worth buying; after - it is not. The gross future gain under the adaptive policy is \(20P(H,+)=20(19/80)=19/4\).

Relative to two routine slots:
\[
19/4-4-2(11/40)=1/5.
\]
Total expected value is \(6+1/5=31/5\).

A precommitted pair earns \(1-1+(1/4)20=5\), below routine production's 6. Source-only and grounding-only do not unlock terminal value in this particular example. Thus the best precommitment is routine. Current margins include operator pay and other contemporaneous costs; the opportunity costs 2 and 4 capture the routine work forgone, not additional cash invoices.

## 3. General terminal technology

Source alone yields
\(-k_S+E[F_H(1,0)-F_H(0,0)]\).

Grounding first gives the standalone grounding increment
\(-k_G+E[F_H(0,1)-F_H(0,0)]\)
plus an option to buy the source. Define
\(M(Z)=E[F_H(1,1)-F_H(0,1)\mid Z]\).
After observing Z, the source is bought exactly when \(M(Z)>k_S\), with indifference at equality. Its expected option contribution is \(E[(M(Z)-k_S)_+]\).

Those alternatives and no acquisition exhaust the two-slot menu because a first-slot uninformative source can only lead to source alone or the fixed pair. Grounding first can always imitate the fixed pair, so it weakly dominates that pair. A sufficiently useful source alone can nevertheless dominate grounding.

The information premium is
\(E[(M-k_S)_+]-(E[M]-k_S)_+\).
Jensen gives nonnegativity. It is strictly positive when M has positive probability strictly below and strictly above k_S. If all realizations lead to the same acquisition decision, it is zero.

The proof requires that fixed-batch terminal effects do not change with report timing and that final usable recipes are observed before terminal operation. Otherwise the terminal belief-state decision must also be modeled.

## 4. Countermodels

With prior 1/2 and first-slot-only source availability, source then grounding earns
\(1-1+(1/2)20=10\).
Grounding first cannot acquire the missing source next, so it cannot implement the informative adaptive route. Routine first also loses the source window. The violated premise is stationary availability, not Jensen's inequality.

At the original prior 1/4, a target-only route with current contribution -4 and future gain 9, combined with a routine slot, earns \(-4+9+3=8\). This beats 6.2. The source-sharing narrative does not justify ignoring the specialist.

## 5. Price and timing

At wage 1/2, manual future service costs 2 and teaching costs 3.5, so current human teaching is zero and total hours are four. At wage 2, manual service costs 8 while teaching costs 5, so current teaching rises to one hour but total hours fall to one.

For two wages \(w_2>w_1\), let optimal policies have gross contribution G_i and total discounted hours H_i. Their two optimality inequalities imply
\((w_2-w_1)(H_1-H_2)\geq0\).
Hence H_2 cannot exceed H_1. The inequality contains no restriction on the time profile of those hours. It also assumes the feasible policy set, technology and other prices do not change with the wage.

## 6. Identification

Assisted completion contains the contemporaneous contribution of the human. It cannot by itself establish how much the resulting dataset changes a retained autonomous policy.

For physical learning, compare matched starting policies with and without inclusion of specified teleoperation data, holding the allowed compute, evaluation distribution, validation and training protocol fixed. Evaluate autonomous performance separately from the system with retained assistance, and count all failed attempts, resets and human monitoring in cost.

For information timing, keep the initial grounding procedure fixed and release a non-safety transfer diagnostic before or after the next acquisition choice. Offer the same alternatives and preserve every operational safety requirement. Measure whether acquisition adapts to a report that actually predicts target usefulness. The mechanism is absent if the report does not predict usefulness, cannot arrive before commitment, or cannot affect the next decision. No actual field experiment was run in this tranche.

## 7. Joint qualification

The correct expected gain is \((1/4)20=5\). The invented independent model gives \((1/4)^2 20=1.25\). Independence changes the chance of the complete recipe, even though it leaves each marginal pass probability unchanged. Two distinct technical requirements do not imply independently generated qualification outcomes.

## 8. Routine useful data

With no incremental source opportunity cost, k_S = 0. Optional use and retained policies imply M(Z) is nonnegative, hence both terms in T7 equal E[M(Z)]. The information-timing premium is zero. In the example both information schedules can earn \(3-1+(1/4)20=7\).

Grounding still produces a physical input required for the future service. What disappears is the value of avoiding a costly source batch after an unfavorable report. Establish the incremental labor, state-visitation, curation, rights or capacity cost of obtaining the relevant source data before applying the original positive-cost comparison.

