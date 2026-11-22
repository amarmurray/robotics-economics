# Exercises: shared robot learning, causal buyer orders and the worker queue

*All examples are synthetic. Instructor answers are in GLOBAL_MULTI_JOB_SOLUTIONS.md.*

**1 — Pairwise evidence can fail.** Three binary variables J,H,Y are fair and all their pairwise two-by-two tables have probability 1/4 in every cell. Characterize all eight-atom joint laws, derive the sharp range for Pr(J=H=0,Y=1) and explain why pairwise incident/order logs cannot identify accepted-customer production under the shared worker queue.

**2 — A new service creates a new job.** Two unit jobs arrive at the end of t2, worker clears one at t3, and a t3 qualified original site-2 service (incremental receipt 1/2) is possible if no initial job is outstanding. Serving generates K=1 after t3 and blocks a potential site-3 order Y at t4. Derive B4, both T-wait and T-serve receipt expectations, and the correct nonanticipative t3 policy conditional on known theta (not future Y).

**3 — An oracle is not a fixed controller.** P costs 1/8 and retains a lawful R after pilot with future qualified-and-ordered production probability 7/16. G adds net 3/8; E adds net 13/32 and genuinely extra resources. Find sharp P−E known-law bounds and the winner at theta=0 and theta=1. Find a legal fixed P policy maximizing worst-case expected production for theta in [0,1], and distinguish this from theta-informed program value.

**4 — Shared-law LP proof.** With finite policy vectors A_i, B_j and a *single* convex polytope of feasible structural scenario laws Gamma, derive epigraph/hypograph linear programs for min and max of max_i A_i(mu)−max_j B_j(mu), and formulate a robust dominance test for an ex-ante randomized first-program policy against an environment-tailored second-program policy. What changes if legality excludes a policy?
