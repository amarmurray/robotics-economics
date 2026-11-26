# Computed results and economic interpretation

All values are synthetic accounting ticks. Initial cash is an endowment. Newly generated cash, salvage and terminal wealth are reported separately. The finite programs enumerate outcomes; floating-point results are checked against independent accounting, and the cohort extension has exact rational verification.

## 1. The concurrent firm

| Economy | Initial cash | Newly generated cash | Terminal equipment salvage | Terminal wealth | First research / construction |
| --- | ---: | ---: | ---: | ---: | --- |
| Baseline, 2 periods | 12 | 12.250000 | 1.000000 | 25.250000 | none / none |
| Baseline, 3 periods | 12 | 18.625000 | 1.000000 | 31.625000 | none / none |
| Baseline, 4 periods | 12 | 26.512500 | 1.000000 | 39.512500 | train_physical_to_digital / none |
| 4 periods, training/procedure learning disabled | 12 | 26.062500 | 1.000000 | 39.062500 | none / none |
| 4 periods, initial cash 18 | 18 | 27.062500 | 1.000000 | 46.062500 | none / none |
| 4 periods, initial cash 18 and both models at level 1 | 18 | 50.000000 | 1.000000 | 69.000000 | none / none |
| Entry with qualified models, construction allowed | 18 | 51.000000 | 1.000000 | 70.000000 | none / arm |
| Same entry, construction disabled | 18 | 42.000000 | 0.000000 | 60.000000 | none / none |
| No archive initially, retention permitted | 18 | 27.171875 | 1.000000 | 46.171875 | none / none; retain digital |
| Same economy, retention prohibited | 18 | 27.062500 | 1.000000 | 46.062500 | none / none |

The baseline starts with one arm, model levels zero, one usable physical archive, an internal lab, cash 12 and a 0.6 prior probability of strong cross-domain transfer.

With two periods remaining it serves current work. With four, it serves one physical job and trains the digital model from physical evidence in period 0, spending 12 before receiving 12. It chooses next-period external scope: the internal lab closes after the current project. The cross-training attempt succeeds with probability 0.4. Its retained capability is then worth using even though continuing to maintain the lab is not.

This learning policy generates 26.5125 cash ticks, compared with 26.0625 when training and procedure improvement are unavailable. The 0.45 increment is a reoptimized program comparison, not an assigned return to data.

Increasing initial cash from 12 to 18 raises terminal wealth by 6.55 and newly generated cash by 0.55. The favored first action changes to current service without research. Additional liquidity permits another operating/scope combination. Thus more finance raises the opportunity-set value while reducing selected first-period research in this economy.

The qualified-stack row is an endowment comparison. Its extra model capabilities were not acquired for free inside a profitability calculation: their acquisition cost is outside that particular intervention and would need to be compared with the resulting value.

### Construction becomes optimal when the controller is already qualified

The entry pair begins with no robot, physical model 2, digital model 1, cash 18 and no internal lab. Demand intercepts are fixed at physical 18 and digital 8. Construction, research, outside data/learning alternatives and service choices are still optimized jointly.

The unrestricted firm builds an arm while supplying one physical and one digital service in the first period. It earns 51 new cash ticks over three periods, versus 42 without construction, and ends with one additional salvage tick. The choice is an arm, not the more expensive mobile platform: with this qualified physical model their labor requirements no longer justify the mobile premium. This is a conditional embodiment choice, not a general ranking of robots.

### Ordinary work creates the evidence used for later improvement

The evidence pair starts with neither archive and cash 18. It uses the stated admitted-research technology with zero internal human coordination, one training compute unit and one procedure compute unit. Other operating recipes and the outside-data alternative remain available.

When retention is permitted, the first action supplies one physical and one digital service and pays one tick to retain the digital case family. A usable case arrives with probability 0.75. The next-period policy trains on that inherited archive when available; a successful training qualification has probability 0.5. The final expected digital-model increment is therefore 0.375.

Newly generated cash is 27.171875 with retention and 27.0625 without permission, an incremental value of 0.109375. The restricted firm can still purchase outside data; that alternative does not win under the stated price. Retention has a small positive value here because it changes a later feasible action. The amount is not an empirical data valuation.

### The four-period baseline operating path

| Period | Physical accepted service | Digital accepted service | Total human input | Total compute | Research probability | Internal lab at start |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 0 | 1.0000 | 0.0000 | 4.0000 | 2.0000 | 1.0000 | 1.0000 |
| 1 | 0.8500 | 1.2500 | 3.6000 | 2.4500 | 0.0000 | 0.0000 |
| 2 | 0.7750 | 1.3750 | 3.6000 | 2.3750 | 0.0000 | 0.0000 |
| 3 | 0.7375 | 1.4375 | 3.6000 | 2.3375 | 0.0000 | 0.0000 |

The human and compute columns include research and manufacture, not just operating inputs. Fractional quantities are expectations across discrete histories. All realized actions satisfy the original capacity and prefunding constraints.

## 2. Physical changes and private values differ

The following are reoptimized current-service finite differences with three periods remaining. They are not fixed-dispatch technological derivatives. Each comparison holds other inherited coordinates fixed.

| Increment | Physical service change | Digital service change | Private terminal-wealth change | Newly generated cash change |
| --- | ---: | ---: | ---: | ---: |
| arm added to no robot | 0 | 0 | 1.00000 | 0.00000 |
| mobile added | 0 | 1 | 8.37500 | 6.37500 |
| physical model increment | 0 | 1 | 9.37500 | 9.37500 |
| digital model increment | 0 | 1 | 11.25000 | 11.25000 |
| procedure increment | 0 | 0 | 0.03125 | 0.03125 |
| reference added | 0 | 0 | 1.00000 | 0.00000 |
| cash increment | 0 | 1 | 2.00000 | 1.00000 |

Adding a mobile platform raises current digital service by one while leaving physical service unchanged. The physical input changes the use of shared labor and hence another market's output. Its private value is 8.375, including two salvage ticks; the corresponding extra generated cash is 6.375.

Adding one cash tick raises terminal wealth by two. One tick is recovered principal and one is the liquidity premium. An extra arm in the low-capability initial state and an extra reference apparatus have only their salvage value in this three-period comparison. Those results do not imply that robots or reference instruments are universally unproductive.

## 3. A solved second-generation procedure choice

[SUCCESSOR_PROCEDURES.md](SUCCESSOR_PROCEDURES.md) derives the eight-period operating gain from qualifying a recipient: \(G=3841/128=30.0078125\). It then solves research over distinct target tasks. The research budget remains 16 windows as target scope changes.

| Targets | Procedure fixed at 0 | One successor allowed | Two successors allowed |
| --- | ---: | ---: | ---: |
| 2 | 40.0101 | 40.0101 | 40.0101 |
| 4 | 79.7711 | 81.3450 | 81.3479 |
| 8 | 144.3459 | 173.3710 | 179.9733 |
| 12 | 159.8024 | 241.8939 | 278.8125 |

Values are incremental net receipts above operating all recipients with their original models. They already deduct research costs. A capable ordinary contingent planner is allowed in every column; the change is the productive procedure menu.

At eight targets, allowing the second procedure adds 6.6023 ticks. The policy produces the second procedure internally with probability 0.9884033 and buys it with probability 0.0115967. It completes all eight qualifications by the operating date. With only two targets, it trains directly and never pays for a successor.

At eight targets and only ten research windows, the optimal first action becomes a guaranteed external license. More time can change the preferred organizational route without changing the target's operating payoff. Finite targets and generations eventually saturate; this is not a sustained-growth result.

## 4. Competition with the same technology

The game has two firms, common linear final-market prices, separately constrained resources and cash, and one common latent transfer regime. First-period service, research, investment and scope are simultaneous. Every continuation is a solved terminal quantity game. Two disclosed tie-breaks reverse the final lexicographic preference after first maximizing joint operating profit and then its minimum among terminal Nash equilibria.

Terminal and root deviations are checked exhaustively. The selection chooses among Nash equilibria; it does not choose a collusive non-equilibrium profile.

| Case | First-period research in every reported root equilibrium | Equilibrium terminal wealth |
| --- | --- | --- |
| Symmetric baseline, cash 12 each | Neither firm trains | Allocations include (19,21), (20,20) and their label reversals |
| Firm 1 has an inherited digital-model lead | Neither firm trains | (27.25,18.50), under both tie-breaks |
| Matched cash 18 and both archives; reviewed research | Neither firm trains | Allocations include (25,27), (26,26) and reversals |
| Same cash/archives; admitted automated research | Both train their own digital model | Each firm's wealth lies between 25.50 and 26.6875; total 52.1875 |

The automated-research regime lowers the human coordination requirement from one to zero, training compute from two to one, and procedure compute from three to one. It changes a declared technology bundle; it is not an estimate of actual autonomous research capability.

The matched reviewed regime has total terminal wealth 52. The automated regime has 52.1875, so the joint private cash-flow gain is 0.1875 after subtracting the same initial cash and salvage. Each firm's chosen training is optimal against the rival's complete action and selected continuation. This establishes an internally priced research-and-competition example, not a large calibrated productivity premium.

The inherited digital lead changes the allocation between firms. The rival's response is solved. Its payoff loss should not be confused with a reduction in total physical output or social welfare, neither of which can be inferred from private wealth alone.

## 5. Verification and remaining closure

The concurrent checker independently reconstructs 7,434 joint kernels, verifies the posterior martingale, and replays each reported optimal policy across the underlying latent regimes. Baseline four-period terminal wealth agrees exactly at 39.5125; its cash identity discrepancy is below \(2\times10^{-14}\). All other accepted cases carry their own independent replay.

The cohort calculation agrees with independent rational arithmetic on 18 cases. Its operating margin reconstruction and closed-form \(G_L=4L-2(1-2^{-L})\) agree with the parent production solver.

The competitive files record all pure root equilibria under both selected continuation conventions, maximum unilateral-deviation gains and the potential-identity discrepancy. The reported residuals are zero up to numerical precision. Pure equilibria here do not establish pure equilibrium for a general dynamic game.

The larger integration problem is now specific: retain enough recipient tasks for a second procedure to matter while restoring concurrent shared resources, cash commitments and competing recipient markets. That next model must determine its recipient payoff internally. It cannot simply carry this cohort's additive \(G\) into a different economy.

