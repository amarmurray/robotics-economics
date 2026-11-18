# Proof ledger — comparative learned-policy support

**18 Nov 2026, conditional mathematics.** Main argument: [COMMON_EXIT_VALUE_COMPARISON.md](COMMON_EXIT_VALUE_COMPARISON.md).

1. Same-version policy-closed pre-action demand/order horizon and independently admissible policies; no robot-level independence assumed. K_i includes known whole-network and training costs exactly once.
2. **Known p is policy-specific.** Previous F logs or another checkpoint's p are not valid substitutes. Each p_ij is identified only under approved joint target history-action kernels up to first exit.
3. A **shared u_j(theta)** means invariant conditional *whole-service continuation expectation*, including B order displacement, customer substitution, operator effects and material resource response, after identified arm differences are removed. Same j name/benchmark is insufficient.
4. Paired identity: Delta=D+sum_j(p_aj-p_bj)u_j. Standard linear extrema under independent-box feasible u and sharpness only if all relevant corners share feasible completed worlds with fixed K,p.
5. Joint persistent theta may constrain u_j across j; optimize Delta over a single feasible theta set, not separate component worlds. If theta also changes K,p, revise the entire expression.
6. The inward lower/upper improvement over subtracting independent intervals is sum_j min(p_aj,p_bj)(h_j-l_j). Verified by elementary per-j signed cases.
7. If p_a=p_b for every j, paired contrast D is fully determined under common residual; it does **not** imply physical policy safety or dominance over F/S.
8. If arm residuals differ by e_ij with certified magnitude epsilon_ij, triangle inequality adds sum_j(p_aj epsilon_aj+p_bj epsilon_bj) to either error radius; absent certification, do not use this shortcut.
9. Existing exact source example reused: no-copy K=7/5,p=1/4; source-copy K=27/20,p=1/2; u in [0,4]; paired [-1/20,19/20] versus independent [-21/20,39/20]; [3,4] conditional grounding makes paired [7/10,19/20]. Not field evidence.
10. Counterexample: identical p=1/4 and known K but conditional u_copy=0,u_no=4 produce -1 contrast despite falsely predicted zero under shared u. A complete state/control/demand/qualification invariance restriction, not merely matching telemetry labels, is essential.
11. Scientific boundaries: no independent proof of novelty, field source-copy/grounding comparison, actual B-inert topology, operator hard-capacity approval, calibrated target kernels, verified fixed-world invariance or numeric BEA–BLS crosswalk.
