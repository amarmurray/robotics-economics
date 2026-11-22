# Queue-duration transfer: reproducibility notes

**22 November 2026. Synthetic CPU-only model, not a field estimate.** From this directory:

```sh
node queue_duration_grounding_exact.js > /tmp/queue_duration_grounding_replayed.json
python queue_duration_grounding_independent.py
```

The Node program prints a JSON record with 12 feasible integer-quarter transportation assignments, 163 scoped exact assertions, gain bounds 0 and 3/4, optional P total bounds 6 and 13/2, grounding G=63/10, independent embodiment E=127/20 and a separate conserved-order identified value 1/2. Compare the complete Node output with [committed expected JSON](queue_duration_grounding_results.json) using a JSON structural comparison, since whitespace differences alone are not substantive. The Python Fraction audit independently checks 12 assignments and 45 exact assertions with the same sharp figures; it does not parse the Node JSON or run the Node code.

The signed derivation and assumptions are in [theory](QUEUE_DURATION_GROUNDING_AND_TRANSFER.md) and prospective unpopulated [field evidence protocol](QUEUE_DURATION_GROUNDING_EVIDENCE.md). It is conditional on t1 pilot choice before queue duration and buyer path, one target-specific worker with D=1,2,3 and no subsequent persistent worker jobs, all future target service lasting one window, legally admissible source/grounding use, and fully qualified original customer offers with stipulated expected net payment classes. Violating those restrictions requires a new full Bellman/queue kernel, not reuse of these numeric thresholds. No model benchmark score was priced as a customer receipt. No complete repository CI, independent scientific peer review, real P/G/E interventions, original-buyer payment panels or quantitative official BEA/BLS industry input-output coefficient is represented.
