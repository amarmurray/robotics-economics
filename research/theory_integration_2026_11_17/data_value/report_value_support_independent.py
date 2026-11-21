#!/usr/bin/env python3
"""Independent stdlib enumeration for sharp signed report-value bounds.

Run: python report_value_support_independent.py
Uses fixed-point integer numerators, probabilities (2,1,1)/4 and deltas /4.
"""
from itertools import product
import json

W = (2, 1, 1)
INTERVALS = [(a, b) for a in range(-2, 3) for b in range(a, 3)]

def report_loss(d):
    positive = sum(w * max(x, 0) for w, x in zip(W, d))
    negative = sum(w * max(-x, 0) for w, x in zip(W, d))
    return min(positive, negative)

def lower(a, b):
    return min(
        sum(w * max(x, 0) for w, x in zip(W, a)),
        sum(w * max(-x, 0) for w, x in zip(W, b))
    )

def upper(a, b):
    best = 0
    for signs in product((0, 1), repeat=len(W)):
        if any((s and b[i] < 0) or ((not s) and a[i] > 0)
               for i, s in enumerate(signs)):
            continue
        p = sum(W[i] * b[i] for i, s in enumerate(signs) if s)
        n = sum(W[i] * (-a[i]) for i, s in enumerate(signs) if not s)
        best = max(best, min(p, n))
    return best

def main():
    count = 0
    vectors = 0
    for choices in product(INTERVALS, repeat=3):
        a, b = tuple(z[0] for z in choices), tuple(z[1] for z in choices)
        values = [report_loss(d) for d in product(
            *[range(x, y + 1) for x, y in zip(a, b)]
        )]
        vectors += len(values)
        assert min(values) == lower(a, b), (a, b, "lower")
        assert max(values) == upper(a, b), (a, b, "upper")
        count += 1
    a, b = (1, -2, -2), (2, -1, 2)
    assert (lower(a, b), upper(a, b)) == (1, 4)
    return {"interval_configurations":count, "brute_candidate_delta_vectors":vectors,
            "exact_assertions":2*count+2,
            "main_lower":"1/16","main_upper":"1/4"}

if __name__ == "__main__":
    print(json.dumps(main(), indent=2))
