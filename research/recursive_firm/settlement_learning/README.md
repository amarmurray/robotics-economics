# When the next paid order can diagnose a transfer failure

The [partition discovery study](../partition_discovery/README.md) constructed a target-site shift that left all incumbent training and validation records unchanged. Settlements could still reveal a loss. Can the organization identify *where* to repair from those receipts? We compare buying an audit at the new site, buying an equally costly incumbent audit and deliberately staggering releases so the next aggregate settlement becomes informative.

## Identification depends on the deployed policy

A digital router serves one fixed-arm order and one mobile order per shift. Each completed job pays the same margin. The firm normally learns only whether zero, one or two jobs paid. Each robot has the current shared action convention and a stored correction. Let the hidden state be the pair of conventions the robots actually require. If one lane is affected, the two possible states are 01 and 10. Under a symmetric release (00 or 11), the success probabilities in those states are permutations of each other. The generating function for the aggregate count is

$$
G(z)=(1-p_1+p_1 z)(1-p_2+p_2 z).
$$

Swapping the probabilities leaves every coefficient unchanged. Any number of these observations can reveal deterioration but cannot distinguish the two locations given symmetric priors and transitions. Under release 01 the probabilities instead become (high, high) in state 01 and (low, low) in state 10. The next count now has different likelihoods. One deployable resource of the firm is the ability to vary releases separately and preserve the record of which action produced the outcome. Site-specific payouts or asymmetric known baseline rates can also break the symmetry. For exactly one order per lane, unequal known margins can reveal identity from cash alone.

## Experiment and accounts

Each 48-shift world starts healthy, then one randomly chosen robot needs a correction at a random shift from 8 through 19. The digital release reduces routing success from 0.93 to 0.68 during shifts 18–27. Conditional physical success is 0.90 under the right convention and 0.25 under the wrong one. Independent routing and physical outcomes generate actual paid jobs at 5 units each. A shared release slot allows one lane to change per shift for 0.60. There is no per-case training data in this extension. A write installs an available correction. The organization learns which checkpoint to install and whether to purchase independent evidence. These experiments isolate attribution while holding offered orders constant.

The controller filters over four possible joint states, discounts old evidence using independent per-lane flip probability 0.025, and chooses a release. This transition prior differs from the test generator. A myopic policy maximizes immediate expected net contribution. A planning policy also prices the best next reachable release after observing the next settlement, approximating its remaining life by a calibrated horizon. A matched planner uses the same continuation value, horizon, switching cost and feasible actions while assigning zero value to the information from its *next* receipt. Both use every actual past receipt. This comparison separates diagnostic deployment from planning ahead around the one-write constraint. Neither planner solves the full sequential control problem.

An audit buys a noisy convention label (90% accurate) for 2 units, with a separate review budget of one label per review date. The target policy inspects the lane with greatest marginal uncertainty. Controls rotate the location, spend the same fee at an incumbent site independent of this fault, or act on target audits alone. A selective buyer skips a scheduled audit if the expected improvement from one revised release over its planning window falls short of the fee. Late reports are filtered at their observation date and intervening settlements are replayed. Calibration on 192 worlds selected horizons from 0, 3 and 9 and audit intervals from 4, 8 and 16, as applicable. Policies were frozen for 1,536 fresh matched worlds per regime. Intervals below cover paired simulation uncertainty conditional on that selection.

## Operating value of evidence

| Net contribution difference over 48 shifts | Persistent single fault | Common fault | Single fault reverses at shift 32 |
| --- | ---: | ---: | ---: |
| Pricing the next receipt versus the matched planner | +12.84 [11.49, 14.20] | −5.59 [−6.69, −4.50] | +15.94 [14.59, 17.29] |
| Target versus equally priced incumbent audits | +5.55 [4.63, 6.46] | +1.48 [0.62, 2.33] | +11.86 [10.80, 12.91] |
| Scheduled target audits versus diagnostic deployment alone | −2.02 [−3.01, −1.03] | −0.77 [−1.75, 0.21] | +1.39 [0.28, 2.50] |

In the persistent-fault regime, diagnostic deployment without audits achieved 88.49% convention alignment, 69.93 paid jobs and 346.27 net units. Scheduled target auditing improved alignment to 89.67% and paid work to 70.46 jobs, with net contribution of 344.25. Across three audits, its break-even price against diagnostic deployment was 1.33 per audit for these fixed policies. With three-shift report lag, scheduled target audits lost 3.38 against deployment alone. The selective buyer purchased 1.43 audits per world and earned 0.53 more than deployment alone [−0.18, 1.24]. Under stability the matched planner beat diagnostic deployment by 7.53. Under an unannounced digital slowdown, the audit-only learner out-earned the scheduled target learner that also interpreted receipts by 4.79 [3.58, 6.00]. A misspecified model can charge a routing loss to the wrong physical controller.

## How many settlements need attribution?

Only one-paid-job shifts are ambiguous. We independently disclosed the successful robot's identity on 0%, 25%, 50% or 100% of those shifts, using the same operating tapes, a fixed planning horizon and zero posted tag price. Controllers knew the disclosure probability before deploying. This randomization changes both the value of an experimental release and the frequency of subsequent ambiguous settlements.

| Share of singly paid shifts identified | Tags per world | Planning versus immediate optimization | Incremental net versus planning with zero tags |
| ---: | ---: | ---: | ---: |
| 0% | 0 | +40.74 [38.99, 42.49] | 0 |
| 25% | 4.41 | +1.33 [0.49, 2.17] | +5.20 [4.31, 6.10] |
| 50% | 8.58 | −0.25 [−0.69, 0.19] | +9.05 [8.16, 9.93] |
| 100% | 16.92 | −0.60 [−0.97, −0.22] | +12.52 [11.64, 13.39] |

Matching continuation value isolates the narrower gain from pricing the information in the next release. This gain fell from 12.84 with zero tags to 0.36 [−0.40, 1.13] with 25% disclosure. At full attribution a residual 0.87 [0.40, 1.34] remained. Task identity removes the permutation ambiguity, while future observations can still improve confidence about whether a shock occurred.

The first disclosure policy could pay up to 1.18 units per tagged receipt before surrendering its gain over zero tags. Full disclosure could pay 0.74 per tag by the same comparison. These are average break-even fees for frozen policies, not marginal prices of a demonstration or an estimate of customer willingness to pay. The organization can substitute data lineage for disruptive experimentation. The return to changing a release depends on its ability to identify outcomes it already earns.

## Public measurement and falsification

Two selected cells per policy from the published WidowX robot evaluation illustrate the accounting problem. Across ten trials per task, RT-1-X scored 0 on standard eggplant-to-pot and 1 on standard carrot-to-plate. Octo scored 1 and 0. Pooling gives each policy one rubric point across twenty trials. These are physical evaluation scores, including the source's partial-credit convention where applicable. The example was selected to demonstrate exact aggregation loss. It cannot establish equal underlying performance, paired trial responses, or any financial return. [Kim et al., OpenVLA, Appendix B.1.3, Table 4](https://arxiv.org/html/2406.09246v1)

The policy comparisons above use synthetic digital and physical controllers, assumed prices and candidate corrections supplied in advance. They estimate no scaling exponent. The earlier [scaling and mixed-fleet study](../learning_dynamics/README.md) covers independent exposure, correlated evidence, and published breadth measurements. Here the new inference concerns designing the observation channel inside the firm.

**Next discriminating test.** With one digital stage and multiple robot tasks, cross randomized staggered releases with randomly revealed job-level attribution. Hold the audit budget, offered workload and feasible checkpoints fixed. In addition to random attribution, test selective missingness: sites that grant retention rights may have easier jobs or newer controllers. Keep a small random reference sample. Does buying the next tag at a poorly represented site outperform buying more tags where failures are cheap to identify? Compare against learning from known margin differences, routing telemetry and a free correlated site label. Score the calibration of fault location, paid orders and net contribution after the next reversal. The substitution mechanism fails if attributed receipts resolve fault location but the benefit of diagnostic release variation persists after matching continuation value. If both aggregate and attributed ledgers already identify the fault, a benefit from separating releases needs a different explanation.

[Simulation and published inputs](study.py) · [Numerical results](results.json) · [Regression checks](test_study.py). From this directory run `OPENBLAS_NUM_THREADS=1 python study.py` and `python -m unittest -q` with Python 3 and NumPy.
