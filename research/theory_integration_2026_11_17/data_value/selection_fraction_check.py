#!/usr/bin/env python3
"""Independent exact-rational audit of the synthetic source-screening example.
No robotics training, customer field measurement or safety test is performed.
"""
from fractions import Fraction as F

types = ("easy", "hard")
weights = (F(1, 2), F(1, 2))
w, cg, cb, cx = F(2), F(2, 5), F(7, 10), F(3, 10)
q0 = (0, 0)
q1 = (1, 0)
ground = (1, 0)
body = (0, 1)

def initial(q):
    return sum((p * w * qualified for p, qualified in zip(weights, q)), F(0))

def increment(q, target, cost):
    return sum((p * (1 - qualified) * (w * acquired - cost)
               for p, qualified, acquired in zip(weights, q, target)), F(0))

assert initial(q0) == 0 and initial(q1) == 1
assert increment(q0, ground, cg) == F(3, 5)
assert increment(q0, body, cb) == F(3, 10)
assert increment(q1, ground, cg) == F(-1, 5)
assert increment(q1, body, cb) == F(13, 20)
assert initial(q1) + increment(q1, body, cb) - cx == F(27, 20)
diagnostic = sum((p * max(F(0), w * g - cg, w * b - cb)
                  for p, g, b in zip(weights, ground, body)), F(0))
assert diagnostic == F(29, 20)
assert F(3, 5) == F(1, 2) * F(8, 5) + F(1, 2) * F(-2, 5)
assert F(3, 10) == F(1, 2) * F(-7, 10) + F(1, 2) * F(13, 10)
assert diagnostic - (initial(q1) + increment(q1, body, cb) - cx) == F(1, 10)
print("10 independent Fraction assertions passed: synthetic source-selection example")
