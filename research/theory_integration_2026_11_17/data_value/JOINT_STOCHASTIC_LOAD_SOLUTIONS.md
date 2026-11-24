# Solutions

1. q=h-P(H=1,overload); overlap bounded by min(p,h) and max(0,h+p-1), yielding [max(0,h-p),min(h,1-p)]. Blocked units do not dual execute.
2. q in [5/16,1/2]; G=23/8 to 13/4; strict G>E iff q>3/8.
3. G=3/2 vs X=1/2,E=3. Refinement adds 5/4 gross before its cost, revised G=11/4 still below E.
4. Signed lambda(A-b) is negative at slack; subtracting it gives artificial credit. Positive part is zero for every safe action, so enough penalty suppresses unsafe candidates in a finite bounded menu. Both require certified support and an actual safe witness for a lower bound.
