# Exercises — delayed orders, learning transfer and scarce recovery

Work from the assumptions in [the theorem](LAGGED_DEMAND_LEARNING_AND_OPERATOR_OCCUPANCY.md). This is a constructed teaching environment; none of these numbers is observed robotics revenue.

1. **Fréchet economic frontier.** A pays 2, B pays 1 and is qualified with probability q=1/2. Original B offers with probability b=1/2, and old A offers with probability a=1/2. One operator chooses the higher paid value. Prove sharp lower and upper bounds on complete date-1 production with no joint observation. State which original buyer/learner joint event would point identify the missing contribution.

2. **Feedback and data value.** In the date-0 synthetic P/D/E example, calculate the full net program contributions in staggered and synchronized P worlds, taking account of paid P pilot revenue, fixed P cost, D acquisition and genuinely independent E capacity. Why does equal technical B qualification q=1/2 under P and D not imply equal economic data value?

3. **Learning versus rescue.** At date 1 A pays 1, B pays 3/4; a B service yields date-2 Q_C probability 5/8 and H operator downtime probability 1/4. C pays 2 conditional on Q_C with old A offering 1; no operator capacity while H=1. Compute the B-minus-A choice difference at j=Pr(Q_C,H)=0, 5/32 and 1/4. Describe the legal/source evidence required for deploying B as an economically productive learning policy.

4. **Change the information structure.** Suppose the C buyer will only order with probability d conditional on Q_C and independently of H once Q_C occurs. Derive the date-2 continuation under B; identify which dependence claims are needed to replace Pr(Q_C,O_C,not-H) by d*(q-j). Explain why a reported technical success rate cannot determine d.

5. **Embodiment and full network.** A second robot body is added but both bodies share the same H recovery worker. Does this remove the capacity penalty? Explain when the E value 5/8 and the terminal one-slot identity cease to be applicable. Describe one test that discriminates independent capacity from two bodies with shared scarcity.

Solutions are maintained separately in [LAGGED_DEMAND_OPERATOR_SOLUTIONS.md](LAGGED_DEMAND_OPERATOR_SOLUTIONS.md).
