# Student exercises: physical queue and economic data transfer

All numbers are synthetic normalized original-customer paid contribution, not robotics measurements. Work from [chapter](QUEUE_DURATION_GROUNDING_AND_TRANSFER.md), without consulting [separate solutions](QUEUE_DURATION_GROUNDING_SOLUTIONS.md).

1. **Nonanticipative pilot.** R yields 2 at each of three dates. At t1 the optional pilot yields 7/4 and qualifies a future target. Target replaces R and raises expected paid net by 1 when an eligible buyer orders and the recovery worker is free. Explain why the correct P expression is 6+[-1/4+E(C)]_+, and why E([ -1/4+C ]_+) is illegal.
2. **Nested worker.** With pilot duration D in {1,2,3}, write worker-free indicators at t2,t3. What joint state is impossible absent later worker jobs? Give one empirical observation that would refute this model.
3. **Sharp coupling.** Buyer paths 00,10,01,11 are equiprobable; D marginals are 1/4,1/4,1/2. Assign durations to paths to maximize/minimize E(C), and prove the extrema without presuming independence.
4. **Program choice.** Under G cost 7/10 and E cost 13/20 with each receiving expected incremental future original-customer production of one, calculate total J_G,J_E and both possible investment rankings against P.
5. **Identification rescue.** Suppose D is 1 or 3 with equal probability and U=10 or 01 with equal probability. Show E(C) is always 1/2 under *every* joint law. Contrast the answer with the periodwise Fréchet outer bound. Why does this not solve endogenous later worker arrival?
6. **Evidence design.** Specify the minimal physical and buyer data needed to distinguish source+field pilot from target grounding and from an independently resourced embodiment without converting benchmarks into dollars.
