#!/usr/bin/env python3
"""Exact synthetic checks for Learning where generalization works.

No fitted industrial parameters. Python 3 standard library only.
Run: python3 generalization_allocation.py --output generalization_allocation_results.json
"""
from __future__ import annotations

import argparse
import itertools
import json
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path


def product(xs):
    out = 1
    for x in xs:
        out *= x
    return out


def assignments(n):
    return itertools.product((-1, 1), repeat=n)


def even_expansion(n, edges, signs, reliabilities):
    """Likelihood ratio against independent uniform edge observations."""
    out = F(0)
    for mask in range(1 << len(edges)):
        parity = [0] * n
        term = F(1)
        for k, (i, j) in enumerate(edges):
            if mask >> k & 1:
                parity[i] ^= 1
                parity[j] ^= 1
                term *= signs[k] * reliabilities[k]
        if not any(parity):
            out += term
    return out


def label_likelihood_ratio(n, edges, signs, reliabilities):
    return sum((product(1 + y * r * z[i] * z[j]
                        for (i, j), y, r in zip(edges, signs, reliabilities))
                for z in assignments(n)), F(0)) / (1 << n)


def components(n, edges):
    parent = list(range(n))
    def root(i):
        while parent[i] != i:
            i = parent[i]
        return i
    for i, j in edges:
        parent[root(i)] = root(j)
    return len({root(i) for i in range(n)})


def check_graph_likelihoods():
    all_edges = tuple(itertools.combinations(range(4), 2))
    errors = (F(1, 5), F(2, 5), F(3, 5), F(7, 10), F(4, 5), F(9, 10))
    noisy = perfect = 0
    for mask in range(1 << len(all_edges)):
        edges = tuple(e for k, e in enumerate(all_edges) if mask >> k & 1)
        rs = tuple(r for k, r in enumerate(errors) if mask >> k & 1)
        rank = len(edges) - 4 + components(4, edges)
        for signs in assignments(len(edges)):
            assert even_expansion(4, edges, signs, rs) == label_likelihood_ratio(4, edges, signs, rs)
            noisy += 1
            exact = even_expansion(4, edges, signs, (F(1),) * len(edges))
            compatible = any(all(z[i] * z[j] == y for (i, j), y in zip(edges, signs))
                             for z in assignments(4))
            assert exact == ((1 << rank) if compatible else 0)
            perfect += 1
    half = (F(1, 2),) * 6
    overlap_lr = even_expansion(4, all_edges, (1,) * 6, half)
    assert overlap_lr == F(27, 16)
    false_independence = (1 + F(1, 8)) ** 3
    assert overlap_lr != false_independence
    return {"noisy_graph_pattern_equalities": noisy,
            "perfect_graph_pattern_equalities": perfect,
            "overlapping_cycle_likelihood_ratio": float(overlap_lr),
            "incorrect_independent_cycle_product": float(false_independence)}


class ExactGraphDecision:
    """Enumerate the joint latent world, then optimize all permitted experiment histories.

    H=1: four independent vertex signs generate pair relations.
    H=0: the six true pair relations are independent signs.
    Base observations are exact 0--1=+1 and 1--2=+1.
    Terminal economic decision uses target pair 0--3, source accuracy
    reliability 4/5, and an ordinary independent target report of reliability 2/5.
    Its value is relative to using that ordinary route. A separate complete
    qualification stage and fallback are included in the stipulated payoff.
    """
    edges = tuple(itertools.combinations(range(4), 2))
    p = F(2, 5)
    source = F(4, 5)
    direct = F(2, 5)
    weight = F(100)

    def __init__(self, audit_reliability=F(1), external_cost=F(39, 2)):
        self.index = {e: k for k, e in enumerate(self.edges)}
        self.actions = {
            "audit": ((0, 2), audit_reliability, F(1, 2)),
            "bridge": ((2, 3), F(1), F(4, 5)),
            "external_direct": ((0, 3), F(1), external_cost),
        }
        self.worlds = []
        for z in assignments(4):
            rel = tuple(z[i] * z[j] for i, j in self.edges)
            self.worlds.append((1, rel, self.p / 16))
        for rel in assignments(6):
            self.worlds.append((0, rel, (1 - self.p) / 64))

    @lru_cache(None)
    def posterior(self, history):
        values = []
        for h, rel, prior in self.worlds:
            mass = prior
            for edge in ((0, 1), (1, 2)):
                mass *= int(rel[self.index[edge]] == 1)
            for action, result in history:
                edge, reliability, _ = self.actions[action]
                mass *= (1 + result * reliability * rel[self.index[edge]]) / 2
            values.append(mass)
        normalizer = sum(values)
        assert normalizer > 0
        return tuple(x / normalizer for x in values)

    def moment(self, history, item):
        weights = self.posterior(history)
        if item == "H":
            return sum(w * h for w, (h, _, _) in zip(weights, self.worlds))
        return sum(w * rel[self.index[item]] for w, (_, rel, _) in zip(weights, self.worlds))

    def terminal(self, history):
        reliability = self.source * abs(self.moment(history, (0, 3)))
        return self.weight * (max(reliability, self.direct) - self.direct) / 2

    def outcomes(self, history, action):
        edge, reliability, _ = self.actions[action]
        mean = reliability * self.moment(history, edge)
        return tuple((y, (1 + y * mean) / 2) for y in (-1, 1) if (1 + y * mean) > 0)

    @lru_cache(None)
    def value(self, history=(), slots=2, allowed=("audit", "bridge", "external_direct")):
        best_value, best_action = self.terminal(history), "stop"
        used = {a for a, _ in history}
        if slots:
            for action in allowed:
                if action in used:
                    continue
                value = self.action_value(history, slots, action, allowed)
                if value > best_value:
                    best_value, best_action = value, action
        return best_value, best_action

    def action_value(self, history, slots, action, allowed):
        cost = self.actions[action][2]
        return -cost + sum(probability * self.value(history + ((action, result),), slots - 1, allowed)[0]
                           for result, probability in self.outcomes(history, action))


def positive(x):
    return max(F(0), x)


def check_allocation():
    model = ExactGraphDecision()
    p, a, d, w = model.p, model.source, model.direct, model.weight
    z = (1 + p) / 2
    plus = p / z
    bridge_value = lambda belief: w * positive(a * belief - d) / 2
    b, c = F(4, 5), F(1, 2)
    assert bridge_value(p) == 0
    assert model.moment((), "H") == p
    for sign in (-1, 1):
        assert model.moment((("bridge", sign),), "H") == p
        assert model.terminal((("bridge", sign),)) == 0
    assert model.moment((("audit", 1),), "H") == plus
    assert model.moment((("audit", -1),), "H") == 0
    assert model.terminal((("audit", 1),)) == 0
    no_external = ("audit", "bridge")
    optimal = model.value((), 2, no_external)
    closed = -c + z * positive(bridge_value(plus) - b)
    assert optimal == (closed, "audit") == (F(47, 50), "audit")
    simultaneous = z * bridge_value(plus) - b - c
    assert simultaneous == F(7, 10)
    assert closed - simultaneous == (1 - z) * b == F(6, 25)
    full = model.value()
    direct_net = F(1, 2)
    assert full == (F(109, 100), "audit")
    assert full[0] == -c + z * positive(bridge_value(plus) - b) + (1 - z) * direct_net
    assert model.value((("audit", 1),), 1)[1] == "bridge"
    assert model.value((("audit", -1),), 1)[1] == "external_direct"
    assert model.value((), 1) == (F(1, 2), "external_direct")
    first = {act: float(model.action_value((), 2, act, tuple(model.actions))) for act in model.actions}
    assert first == {"audit": 1.09, "bridge": .7, "external_direct": .5}
    noisy = ExactGraphDecision(F(4, 5))
    assert noisy.value() == (F(1, 2), "external_direct")
    assert noisy.action_value((), 2, "audit", tuple(noisy.actions)) == F(171, 500)
    # Nonzero p after an adverse imperfect audit; no false proof of impossibility.
    assert noisy.moment((("audit", -1),), "H") == F(2, 17)
    threshold = F(315, 374)
    threshold_model = ExactGraphDecision(threshold)
    assert threshold_model.action_value((), 2, "audit", tuple(threshold_model.actions)) == F(1, 2)
    return {"parameters": {"p": float(p), "source_reliability": float(a), "ordinary_direct_reliability": float(d),
                            "terminal_weight": float(w), "bridge_cost": float(b), "audit_cost": float(c),
                            "external_direct_cost": 19.5},
            "gross_pair_value": float(z * bridge_value(plus)),
            "simultaneous_pair_net": float(simultaneous),
            "adaptive_pair_net_without_external": float(closed),
            "adaptive_best_first_values_with_external": first,
            "best_one_slot": .5,
            "perfect_audit_positive_probability": float(z),
            "perfect_audit_positive_posterior": float(plus),
            "perfect_audit_positive_action": "bridge",
            "perfect_audit_negative_action": "external_direct",
            "noisy_audit_reliability": .8,
            "noisy_audit_first_value": .342,
            "noisy_best_action": "external_direct",
            "audit_reliability_indifference": float(threshold)}


def local_deviation_likelihood(n, edges, signs, structural, measurement):
    """Independent direct sum over actual relations, measurement errors and labels."""
    total = F(0)
    for z in assignments(n):
        for relations in assignments(len(edges)):
            term = F(1, 1 << n)
            for (i, j), y, relation in zip(edges, signs, relations):
                term *= (1 + structural * relation * z[i] * z[j]) / 2
                term *= (1 + measurement * y * relation) / 2
            total += term
    return total


def check_nonidentification():
    edges = ((0, 1), (1, 2), (0, 2))
    compared = 0
    for signs in assignments(3):
        first = local_deviation_likelihood(3, edges, signs, F(1), F(1, 2))
        second = local_deviation_likelihood(3, edges, signs, F(1, 2), F(1))
        assert first == second
        assert first == label_likelihood_ratio(3, edges, signs, (F(1, 2),) * 3) / 8
        compared += 1
    # A two-edge path has posterior label correlation (tau * lambda)^2 = 1/4.
    label_correlation = F(1, 4)
    predictions = (label_correlation, F(1, 2) * label_correlation)
    repeat_products = (F(1, 2) ** 2, F(1) ** 2)
    assert predictions == (F(1, 4), F(1, 8))
    assert repeat_products == (F(1, 4), F(1))
    # Direct sum independently verifies predictions for the unobserved target edge.
    for structural, measurement, expected in ((F(1), F(1, 2), predictions[0]),
                                               (F(1, 2), F(1), predictions[1])):
        numerator = denominator = F(0)
        for z in assignments(3):
            path_likelihood = product((1 + structural * measurement * z[i] * z[j]) / 2
                                      for i, j in ((0, 1), (1, 2))) / 8
            denominator += path_likelihood
            numerator += path_likelihood * structural * z[0] * z[2]
        assert numerator / denominator == expected
    return {"observationally_equivalent_triangle_patterns": compared,
            "world_1": {"structural_reliability": 1, "measurement_reliability": .5,
                        "unobserved_relation_prediction": .25, "repeat_product_expectation": .25},
            "world_2": {"structural_reliability": .5, "measurement_reliability": 1,
                        "unobserved_relation_prediction": .125, "repeat_product_expectation": 1}}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = {"status": "all checks passed", "evidence_status": "synthetic exact rational enumeration; no field calibration",
              "graph_likelihoods": check_graph_likelihoods(),
              "sequential_allocation": check_allocation(),
              "structural_noise_nonidentification": check_nonidentification()}
    encoded = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(encoded)
    print(encoded, end="")


if __name__ == "__main__":
    main()
