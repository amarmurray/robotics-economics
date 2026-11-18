# Learning exercises: productive teleoperation and economic data value

Use the main chapter but keep TELEOPERATION_SOLUTIONS.md closed initially. These exercises do not certify mastery; they are a route to independently reconstructing the argument.

## 1. Price is not yet data value

A provider can serve five orders at payment w each, using a competent alternative costing 6 per order. A qualified robot would cost 2. Capacity and quantities are otherwise equal. Compute incremental operating value at w = 1, 3, 6, 8 and 12. Explain the saturation and identify two reasons the formula would change in a real deployment.

## 2. A productive diagnostic

Two routine slots earn 3 each. Source teleoperation earns 1 and supplies a source batch. Target teleoperation earns -1 and supplies grounding plus a diagnostic. Both batches create future incremental value 20 only in a reusable regime with prior 1/4. Diagnostic sensitivity and specificity are 19/20.

Derive both signal probabilities and posteriors. Find the optimal second action after each signal, then compute the first action and its expected value. Compare with the best precommitted plan. Which costs are already included in current margins, and which opportunity costs are implicit in choosing another job?

## 3. Prove the arbitrary-technology formula

Let F_H(x,g) be a general terminal value table. Source reveals nothing before the second choice; grounding reveals Z; batch effects commute; there are two stationary slots and at most one batch of each type.

Derive the three terms in T6 without assuming that a partial batch has zero value. Explain why grounding-first weakly dominates a precommitted pair but need not beat source-only production. Prove T7 and give a strictness condition.

## 4. Break the ordering claim constructively

Use the binary model with prior 1/2. Make the source opportunity available only in the first slot. Compute the best policy and name precisely the assumption that failed. Then add a target-only route that uses one slot, earns -4 currently and contributes 9 at the terminal date independently of transfer. Compare it with the original noisy-diagnostic case at prior 1/4.

## 5. Human work can move earlier

One option uses four future human hours to deliver a fixed accepted service. Another uses one current teaching hour and three nonlabor units, then supplies the same future service autonomously. Ignore discounting.

Compare wages 1/2 and 2. Prove the general monotonicity of total expected discounted human time when all other primitives are fixed, and explain why the proof does not imply monotonicity of current human time.

## 6. Design the empirical test

Why does an intervention-aided completion rate fail to identify the effect of training data on autonomous capability? Propose one test of physical learning and one test of information timing. Specify what needs to be held fixed, how failure episodes enter cost measurement, and what result would falsify the information mechanism.

## 7. Joint validation

A development program qualifies two required components together with probability 1/4 and otherwise qualifies neither. The new complete recipe is worth 20; either component alone is worth zero. Compute expected value under the actual law and under an unjustified independence assumption. Explain why multiplying two reported marginal pass percentages is not a neutral simplification.

## 8. Strengthen the production comparator

Suppose a routine operating mode already supplies exactly the same usable source batch at no additional cost. Under optional use, prove that the early report has no acquisition-timing premium in T7. Calculate early and delayed values in the binary example when the source margin rises from 1 to 3. What empirical fact must be established before claiming the original scarce-data mechanism?

