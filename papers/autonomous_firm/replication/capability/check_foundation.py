from fractions import Fraction as Q
from itertools import product


def chance_from_records(probs):
    total = Q(0)
    for hits in product((False, True), repeat=len(probs)):
        mass = Q(1)
        for hit, probability in zip(hits, probs):
            mass *= probability if hit else 1 - probability
        if any(hits):
            total += mass
    return total


def qualify(tests, budget, usable_rule):
    if budget == 0:
        return Q(0)
    hits = 0
    for marker in range(tests):
        for orientation in range(tests):
            correct_test = (marker + orientation) % tests
            selected = [correct_test] if usable_rule else range(budget)
            hits += correct_test in selected
    return Q(hits, tests**2)


def settlement(own, rival, prize):
    total = [Q(0)] * 4
    for i, j in product(range(2), repeat=2):
        weight = (own if i else 1 - own) * (rival if j else 1 - rival)
        # Relative to two high-cost offers. Ordered as i profit, j profit,
        # buyer saving, and real saving in the winning method.
        outcomes = (i * (1 - j), j * (1 - i), i * j, max(i, j))
        for k, item in enumerate(outcomes):
            total[k] += prize * weight * item
    assert sum(total[:3]) == total[3]
    return total


def run():
    checks = 0
    ordinary, instrumented = Q(1,5), Q(4,5)
    for tests in range(2, 7):
        for budget in range(tests+1):
            h = Q(budget, tests)
            b = (1-h) if budget else Q(0)
            assert qualify(tests, budget, False) == h
            assert qualify(tests, budget, True) == h+b
            for slots in range(1, 6):
                for n in range(slots):
                    baseline = chance_from_records([instrumented]*n + [ordinary]*(slots-n))
                    gain = chance_from_records([instrumented]*(n+1) + [ordinary]*(slots-n-1)) - baseline
                    assert baseline == 1-(1-instrumented)**n*(1-ordinary)**(slots-n)
                    assert gain == (instrumented-ordinary)*(1-instrumented)**n*(1-ordinary)**(slots-n-1)
                    for reach, rival in product((Q(0),Q(1,3),Q(1)),(Q(0),Q(2,5),Q(1))):
                        p = h+b*reach*baseline
                        paired = settlement(p+b*reach*gain,rival,100)[0]-settlement(p,rival,100)[0]
                        assert paired == 100*(1-rival)*b*reach*gain
                        checks += 1

    # No assumption of independence is required for a change in the gain
    # on a fixed jointly evaluated portfolio of opportunities.
    for baseline, own, rival in product(range(16), repeat=3):
        a = [(baseline >> j) & 1 for j in range(4)]
        b = [(own >> j) & 1 for j in range(4)]
        r = [(rival >> j) & 1 for j in range(4)]
        total_change = sum(x*(1-z) for x,z in zip(b,r))-sum(x*(1-z) for x,z in zip(a,r))
        assert total_change == sum((y-x)*(1-z) for x,y,z in zip(a,b,r))

    for p,r,dp,dr in product([Q(i,4) for i in range(5)],repeat=4):
        if p+dp>1 or r+dr>1:
            continue
        assert settlement(p+dp,r,1)[0]-settlement(p,r+dr,1)[0] == dp*(1-r)+p*dr
    base, active, cost = Q(3,5), Q(9,10), 6
    rows = []
    for a,b in product((0,1),repeat=2):
        pi,pj=(active if a else base),(active if b else base)
        firm1,firm2,buyer,social=settlement(pi,pj,100)
        rows.append(tuple(map(float,(firm1-cost*a,firm2-cost*b,buyer,social-cost*(a+b)))))
    assert rows == [(24,24,36,84),(6,30,54,90),(30,6,54,90),(3,3,81,87)]
    probability = Q(2,3)
    assert (1-probability)*30+probability*3 == (1-probability)*24+probability*6
    print(f"{checks} source-to-settlement comparisons, all 4,096 joint panels, exclusive bids, payoffs, mixed equilibrium: verified.")
    print(rows)


if __name__=="__main__":
    run()
