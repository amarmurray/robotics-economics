"""Linear local price feedback near an interior operating point, and bundle check."""
from itertools import combinations
from math import sqrt

def errors(gain, delayed, steps=18):
    past, current = 1., 1.
    history = [current]
    for step in range(steps):
        next_error = current - gain * (past if delayed else current)
        past, current = current, next_error
        history.append(current)
    return history

def main():
    # Characteristic roots for delayed feedback when 4*gain>1 are complex conjugates.
    for gain in (0.6, 1.2):
        assert abs(1-gain)<1
        assert (sqrt(gain)<1) == (gain<1)
        print("gain",gain,"instantaneous root",round(1-gain,4),
              "delayed magnitude",round(sqrt(gain),4))
    pairs = [set(s) for s in ("AB", "AC", "BC")]
    assert all(a & b for a,b in combinations(pairs, 2))
    assert all(sum(.5 for pair in pairs if item in pair) == 1 for item in "ABC")
    print("bundle packing: integer optimum 1, fractional optimum 1.5")
if __name__ == "__main__":
    main()
