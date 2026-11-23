# Replication: heterogeneous histories, joint qualification and data value

Use Node 22.x with no packages from this directory:

```sh
node history_compression_exact.js > history_compression_results.json
```

The script exactly enumerates four equally probable *synthetic* late histories and four t4 net paid-production actions, keeping a retained no-update policy feasible. It computes V(full)=4, V(count)=5/2, V(provenance signature)=4, V(none)=9/4, and verifies all 15 partitions of the four histories. Across each partition it checks (1) information monotonicity, (2) zero regret if and only if each compression cell contains a common optimal terminal action, (3) equality with the conditional-max identity. Also checks the t3 signal-dependent source-service/recovery decision: 11/2 full versus 3 without the signal; independent E benchmark 4.2.

Independently recompute values with Python Fraction or manual exact fractions, not just the same floating-point code. Latest local executed Node 22.16 run reported 64 assertions and independent Python Fraction calculations confirmed all four main values, the 3/2 information difference and both t3 acquisition values. Verify the code and results after fetching the published commit; there has been no live robot run, no entire-repository CI and no external independent scientific review.

Every return is a **normalized synthetic net contribution** under the stipulated single original buyer budget and exclusive final service/validation slot. There is no training of pretrained/real robot models; the deterministic qualification map is an assumption. The actual P/G/E/R market decision needs lawful causal kernels, customer receipts, worker and compute accounting, and source-to-target technical validation before using this as an empirical decision tool.
