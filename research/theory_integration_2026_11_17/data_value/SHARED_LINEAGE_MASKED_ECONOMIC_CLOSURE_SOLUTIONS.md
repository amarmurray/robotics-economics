# Solutions — shared resource and masked learning

1. Even parity: at H=0, (Y,Z)=(0,0),(1,1); at H=1, (0,1),(1,0). Odd parity reverses them. Hence conditional success for M at H=0 and N at H=1 is (1−p)/2, and the contrasts are 3−6p and 1−4p. Each cell has original mass 1/8; 6+(4−10p)/8=13/2−5p/4.
2. At p=1/2, each cell has M contrast 0, N contrast −1 and L=0, so no feasible rule, randomized or not, exceeds 6. L gives 6 everywhere. Without H, unconditional M=6 and N=23/4 regardless of p, so a law-known but report-blind rule cannot exceed 6 in this menu.
3. Relative to p=0 the maximum per-cell absolute error is 6p≤3/4, and released mass is 1/4: error ≤3/16. Lower bound 13/2−3/16=101/16>25/4. The selected errors are (6p+4p)/8=5p/4≤5/32, giving 203/32>25/4.
4. M and N are distinct single-slot schedules. Their common coefficient-error difference can be as large as e_M+e_N, not max(e_M,e_N); shared activities cancel. If the worker spans customers, local report policies may conflict; define the joint history and feasible schedule or a demonstrably executable shared-capacity policy, then bound its residual under its occupancy. Independent local optima are only a relaxation.
