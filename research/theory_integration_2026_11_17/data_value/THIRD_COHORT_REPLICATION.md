# Reproduction and audit — conditional third-cohort failure/recovery value

Source: [third_cohort_failure_overlap_exact.js](third_cohort_failure_overlap_exact.js). Results: [third_cohort_failure_overlap_results.json](third_cohort_failure_overlap_results.json). Run Node >=18:
\`\`\`sh
node third_cohort_failure_overlap_exact.js
\`\`\`

The eight equally weighted **conditional failed-first-service** atoms use D=1 on indices 0..5, W=1 on indices 0,1,2,6, and gate D W=1 on indices 0,1,2. World A has G={1,2,4,5,6,7} and K={0,6}; world B has G={1,2,3,4,5,7} and K={1,6}. K is always a subset of W. All exact comparisons use integer numerators/8 for conditional moments and /32 for entire-program contributions. The script tests both worlds, enumerates every 6-of-8 G and 2-of-4 recovery-supported K assignment, and finds 18 laws satisfying overlap 1/8 and individual gated x_G=2/8, x_K=1/8. It verifies both attainable economic endpoints, the payoff identity and regret arithmetic.

Independent cross-check (performed in Python with fractions.Fraction on 23 November) enumerated the same 18 laws, confirmed λ in {0,1/8}, program vectors A=(7/8,1,15/16,17/16,33/32) and B=(7/8,1,15/16,15/16,33/32) in R,G,K,GK,E order, and minimax fraction 1/4 with regret3/128. The V8 source-function test ran 85 assertions. This is exact finite arithmetic, **not** a proof of causal transport, scientific novelty or empirical robotics economics. No full repository CI or real intervention was run. The symbolic identity and endpoint construction are proved separately in the chapter.

The full counterfactual assumption is selectable checkpoint OR under compute-only, non-displacing training and pre-offer buyer invariance. Inference can fail if G/K changes D/W, K records are selected, rights fail, deployment clocks differ, or combination training harms old checkpoints. Keep zeros for W=0 K absence, and never read a technical benchmark percentage as captured money.
