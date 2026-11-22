# Reproduction — exact multi-date buyer/worker audit theorem

**22 November 2026; synthetic only.** From the repository's data_value directory:

```sh
python3 policy_audit_fraction.py
node policy_audit_integer.js
```

Python 3 uses only the standard library Fraction and exhaustive 8-atom common-law reconstruction at 257 rational values b=j/1024 (0<=j<=256); independently written Node code uses integer 1024-unit scenario masses and 4096-unit contribution accounting. These are distinct implementations, not two different field datasets or mathematical proofs. Python executed **5,422 exact assertions on 257 laws**. Node executed **6,049 exact integer assertions on 257 laws**, reconstructing the pairs and physical payoff without relying on the Python result. Their committed outputs are policy_audit_results.json and policy_audit_integer_results.json. The retrieved staged blobs matched the tested local sources (Python Git blob 27104c8f1b5c1be2bac4e5ebc61f150f72020866; JS Git blob 96e5e8aa6bc0230eb64f4f967490c7f9b4d39c5b); result blobs 05687c31352246d6d6de7dd04897448eac7a867d and 56d70ac0e4f8acfb29b4f99f4a83cbb6d9bee93f.

All tests are **numeric checks over a stipulated rational family**; the mathematical proof is in JOINT_BUYER_QUEUE_AUDIT_AND_TIMING.md. They do not estimate population b, validate actual worker duration, show causal G uplift, verify robot transfer or provide independent peer review. No runtime controls outside this explicit test were used, and no whole-repository CI claim is made.

Expected exact outputs: b=0: P=11/16, G=15/32, E=9/16; b=5/32: P=17/32, G=35/64, E=9/16; b=1/4: P=1/2, G=19/32, E=9/16. Uniform three-world prior with report before program: 59/96; after program but before dispatch: 7/12; after both decisions: 9/16. Positive timing components 1/32 and 1/48 sum to 5/96. Under absent G action support at b=1/4, G can equal either 15/32 or 19/32 depending on the unobserved k, despite perfect old-policy audit.

A real implementation needs an authorized event-level Y/no-Y and Z/no-Z original buyer registry, actual resource occupancy/queue timestamp, qualification and settled-payment validation, transfer/rights checks, and independent E resource costs. Without them, every numerical quantity in this package remains **synthetic normalized production**, not empirical money.
