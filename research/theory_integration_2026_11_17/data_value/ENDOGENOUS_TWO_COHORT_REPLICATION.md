# Replication — endogenous two-cohort source, buyer and worker response

Execute with Node 22+:

    node endogenous_two_cohort_exact.js > endogenous_two_cohort_results.json

The program enumerates 11 exactly represented F/T common laws, 20 source atoms and three binary D0/R0/W0 seeds (160 atom histories per law). Expected receipt numerators are integer-scaled by denominator 1600; E=992/1600, P=960/1600. It asserts every policy's program contribution, P source-selection/offer/worker moments, the G demand-worker coupling counterworld, rank changes, endpoint regrets and ideal signal value. The terminal output is JSON only, synthetic and versioned. Exact source and results should be checked after publication against this specification; full repository CI may be separately unavailable.

Independent mathematical checks: direct Fraction expansion gives P=3/5, G-I=13/20-3x/4 and G-II=3x-1/10, x=k/20; the G/E minimax regret is 69/2500 at precommitted G share 2/25, and the two-endpoint equal-prior perfect-signal ceiling is 3/200. These calculations are symbolic and do not validate field transport assumptions, customer rights, interindustry flows, or scientific originality. The source uses no outside packages or network data.

Read alongside [the chapter](ENDOGENOUS_TWO_COHORT_SOURCE_AND_DEMAND.md), [unpopulated experiment](ENDOGENOUS_TWO_COHORT_EVIDENCE.md), student [exercises](ENDOGENOUS_TWO_COHORT_EXERCISES.md) and instructor [solutions](ENDOGENOUS_TWO_COHORT_SOLUTIONS.md).