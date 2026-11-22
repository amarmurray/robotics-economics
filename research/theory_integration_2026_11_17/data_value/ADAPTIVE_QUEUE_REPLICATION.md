# Adaptive action-created recovery queue: exact replication

22 November 2026. Scope: original synthetic qualified customer-production comparison. The model is not trained on, or calibrated to, any robotics fleet, buyers, work customer, or confidential information.

From a clean checkout at the tested assistant-branch commit:

    node research/theory_integration_2026_11_17/data_value/adaptive_queue_exact.js
    python research/theory_integration_2026_11_17/data_value/adaptive_queue_independent.py

The JavaScript source uses native BigInt rational arithmetic and Node built-in assert (no dependencies). It independently enumerates both feasible queue histories and all four new-job/buyer joint cells for 17 rational laws z=k/64, k=16,...,32; compares to the analytic Bellman formula; tests each marginal, fallback and T/R switching condition, P/G/E rankings and 101 randomized fixed-policy mixtures. It executes **260 explicitly counted assertions** in the scoped program and prints a JSON document; compare the printed fields to [recorded expected results](adaptive_queue_exact_results.json), which contains 17 scenarios. The Python Fraction code independently recomputes the joint-law, two initial durations, current paid gain and t3 worker/customer continuation and executes **242 counted assertions**.

Expected summary: P_low=17/4; P_high=69/16; G=107/25; E=43/10; old R=4; T/R cutoff z=3/8; worst-case fixed P dispatch chooses R at date 2 absent lawful information about z. These are exact normalized synthetic values; they must not be treated as measured production, a technical transfer benchmark translated to money, or peer-reviewed originality.

For cross-check, the locally executed Node source was Git-hash-matched to blob 5c10bc94e6e407983255790a589f362365fc0d80 before publication, with 260 successful checks. A local exact Fraction script of the same algorithm produced 242 successful checks; no full-repository CI or independently administered replication is claimed.

Required eventual empirical validation is specified in [the unpopulated evidence protocol](ADAPTIVE_QUEUE_LEARNER_DEMAND_EVIDENCE.md): lawful rights, original-buyer order/no-offer and cleared payment panels, physically feasible shared-worker incident arrivals and queue timing, prospective conditional policy information, cluster treatment exposure and separate embodiment resources. November22 scientific gate OPEN.