# Student exercises — robust physical fallback and data economics

**20 November 2026.** Attempt these before using the [separate instructor solutions](ROBUST_RECOVERY_GAME_SOLUTIONS.md).

1. Let G=\{done\}. A safe \`retry\` state has one legally available old action whose only successor is \`done\`. A safe \`blocked\` state has no old actions. Compute W0,W1 for these states. Does storing R weights help at \`blocked\`?

2. X at \`initial\` can reach either \`done\` or \`retry\` after a one-step attempt. An alternative X update additionally can reach \`blocked\` after failure. Evaluate admission with two initial service steps. Explain why an average X success probability cannot replace the universal successor condition.

3. A fully safe, physically admitted X probe consumes operator time and changes the buyer's menu; its modeled full-network net contribution is 1, while retained R earns 2. Is X preferable simply because its robust qualification contains R's? Where must the future data benefit enter Model B?

4. In Model B source training improves the probability of visiting an informative failure state but not the signed reachability set; target grounding adds a verified one-step recovery action. Which can expand the *robust* old-recovery winning set, and what empirical distinction would establish that mechanism?
