"""Exact, synthetic, lawful paid-Q coupling checks. Python 3 standard library only."""
import json
from fractions import Fraction as F

Z = F(0)

def pos(x):
    return max(Z, x)

def loss(p, d):
    a, b = d
    return p * pos(a) + (1 - p) * pos(b) - pos(p * a + (1 - p) * b)

def model(p, alpha, beta, theta):
    assert Z < p < 1 and alpha < beta
    return loss(p, (theta - alpha, theta - beta))

def analytic(p, alpha, beta, theta):
    pivot = p * alpha + (1 - p) * beta
    if theta <= alpha or theta >= beta:
        return Z
    if theta <= pivot:
        return p * (theta - alpha)
    return (1 - p) * (beta - theta)

def joint_interval(p, alpha, beta, lo, hi):
    assert lo <= hi
    pivot = p * alpha + (1 - p) * beta
    xstar = min(max(pivot, lo), hi)
    return min(analytic(p, alpha, beta, lo), analytic(p, alpha, beta, hi)), analytic(p, alpha, beta, xstar)

def interpolate(x, y, t):
    return (x[0] + t * (y[0] - x[0]), x[1] + t * (y[1] - x[1]))

def clip_polygon(poly, halfplane):
    """Exact convex-polygon/segment clipping; halfplane(point)>=0."""
    out = []
    for i, x in enumerate(poly):
        y = poly[(i + 1) % len(poly)]
        fx, fy = halfplane(x), halfplane(y)
        if fx >= 0:
            out.append(x)
        if (fx > 0 > fy) or (fx < 0 < fy):
            out.append(interpolate(x, y, fx / (fx - fy)))
        elif fx < 0 and fy == 0:
            out.append(y)
    return list(dict.fromkeys(out))

def sharp_convex_paid_support(p, poly):
    """Sharp information-loss extrema over a convex Q-difference polygon.
    Partition by two action-difference signs and the blind-policy tie line.
    L is affine on each resulting cell, so candidates are cell vertices.
    Vertices must be cyclically ordered; segment and singleton also work.
    """
    assert poly and Z < p < 1
    candidates = []
    for s in (1, -1):
        for t in (1, -1):
            cell = clip_polygon(clip_polygon(poly, lambda d: s * d[0]), lambda d: t * d[1])
            if not cell:
                continue
            for tie_side in (1, -1):
                sub = clip_polygon(cell, lambda d: tie_side * (p * d[0] + (1 - p) * d[1]))
                candidates.extend(loss(p, d) for d in sub)
    assert candidates
    return min(candidates), max(candidates)

def textfrac(x):
    return str(x.numerator) + '/' + str(x.denominator)

checks = 0
for p in [F(i, 10) for i in range(1, 10)]:
    for alpha in (F(-1), Z, F(2)):
        for gap in (F(1, 4), F(1), F(3)):
            beta = alpha + gap
            for i in range(-10, 111):
                theta = alpha + gap * F(i, 100)
                v = model(p, alpha, beta, theta)
                assert v == analytic(p, alpha, beta, theta) and v >= 0
                assert (theta <= alpha or theta >= beta) == (v == 0) or theta in (alpha, beta)
                checks += 2
            for i in range(0, 11):
                for j in range(i, 11):
                    lo = alpha + gap * F(i, 10)
                    hi = alpha + gap * F(j, 10)
                    lower, upper = joint_interval(p, alpha, beta, lo, hi)
                    observations = [model(p, alpha, beta, lo + (hi - lo) * F(k, 20)) for k in range(21)]
                    assert lower <= min(observations) and upper >= max(observations)
                    checks += 2

p = F(1, 2)
unit_rectangle = [(Z, -F(1)), (F(1), -F(1)), (F(1), Z), (Z, Z)]
coupled_segment = [(Z, -F(1)), (F(1), Z)]
triangular_support = [(Z, -F(1)), (F(1), Z), (Z, Z)]
assert sharp_convex_paid_support(p, unit_rectangle) == (Z, F(1, 2)); checks += 1
assert sharp_convex_paid_support(p, coupled_segment) == (Z, F(1, 4)); checks += 1
assert sharp_convex_paid_support(p, triangular_support) == (Z, F(1, 4)); checks += 1
assert joint_interval(p, Z, F(1), Z, F(1)) == (Z, F(1, 4)); checks += 1

# Actual source-generated new physical qualifications and pre-dispatch reports are
# distinct interventions: lowering a qualification threshold has increasing
# differences with θ, but the value of a demand report peaks and then declines.
for i in range(1, 100):
    theta_low = F(i, 100)
    theta_high = F(i + 1, 100)
    gap_low = pos(theta_low + F(1, 4)) - pos(theta_low)
    gap_high = pos(theta_high + F(1, 4)) - pos(theta_high)
    assert gap_high >= gap_low; checks += 1
assert model(p, Z, F(1), F(1, 4)) < model(p, Z, F(1), F(1, 2)); checks += 1
assert model(p, Z, F(1), F(3, 4)) < model(p, Z, F(1), F(1, 2)); checks += 1

record = {
    'scope': 'synthetic conditional Q, no robot data or monetary calibration',
    'checks': checks,
    'shared_theta_half_half': {
        'coupled_information_loss_max': textfrac(sharp_convex_paid_support(p, coupled_segment)[1]),
        'rectangular_information_loss_max': textfrac(sharp_convex_paid_support(p, unit_rectangle)[1]),
        'interior_theta_star': '1/2',
        'endpoint_losses': ['0/1', '0/1'],
        'qualification_versus_report_signs': 'threshold-lowering grounding complements theta; report premium rises then falls'
    },
    'nonrectangular_triangle_max': textfrac(sharp_convex_paid_support(p, triangular_support)[1]),
    'scientific_gate': 'OPEN',
    'real_original_buyer_Q_support': False,
    'signed_robot_programs': False,
    'official_quantitative_BLS_BEA_flow': False
}
if __name__ == '__main__':
    print(json.dumps(record, indent=2, sort_keys=True))
