# Replication protocol: adaptive qualification-menu coupling

No external package, confidential data or robot runtime required.

At a normal local checkout of the assistant research branch, run:

    node research/theory_integration_2026_11_17/data_value/adaptive_menu_copula.js > /tmp/adaptive_menu_copula_replay.json

Compare parsed JSON in the replay with the committed [record](adaptive_menu_copula_results.json); ignore whitespace differences. The source is an immediately invoked JavaScript function that uses native BigInt exact rational arithmetic (the script prints its result under Node). The assertion failures throw and terminate execution. The code checks 38 feasible quarter-grid Bernoulli couplings, 127 exact arithmetic/invariant assertions and the explicit even/odd three-policy parity distributions.

The analysis was executed in the available V8 tool from the exact stored source blob and returned JSON was compared against the stored result blob before publication. Separate Python Fraction enumeration independently checked the three two-policy regimes and parity menu values. This verifies **synthetic arithmetic only**; it does not establish a mathematically complete general theorem, full repository CI, customer field transport, physical approval or originality.

Main chapter: [ADAPTIVE_QUALIFICATION_MENU.md](ADAPTIVE_QUALIFICATION_MENU.md). Proof, empirical and student/instructor distinctions: [proof](ADAPTIVE_MENU_PROOF_LEDGER.md), [protocol](ADAPTIVE_MENU_EMPIRICAL.md), [exercises](ADAPTIVE_MENU_EXERCISES.md) and [solutions](ADAPTIVE_MENU_SOLUTIONS.md).

The next falsifiable evidence requirement is a valid matched or sequential joint full-customer qualification and original-order comparison; static policy means alone are insufficient to calibrate staged acquisition.
