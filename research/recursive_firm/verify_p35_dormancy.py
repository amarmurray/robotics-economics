"""Exact P3.5 arithmetic witnesses; no optimizer, simulation, or empirical inputs.

Run: python research/recursive_firm/verify_p35_dormancy.py
All mathematical numeric arithmetic uses fractions.Fraction (integer indices only).
The analytical proofs, including invariant sets and renewal, are in PROOFS A.5.
"""
from fractions import Fraction as F


def receipt(beta, delta, lag, theta, yield_rec, stake, arrival):
    a_surv = beta * (1 - delta)
    ceiling = theta * yield_rec * stake * beta**lag
    return ceiling * arrival / (1 - a_surv + a_surv * arrival)


def boundary(ceiling, a_surv, cost):
    assert ceiling > cost > 0 and 0 < a_surv < 1
    return cost * (1 - a_surv) / (ceiling - a_surv * cost)


beta, delta, lag = F(9, 10), F(1, 10), 2
theta, yield_rec, stake = F(3, 4), F(1, 2), F(40)
cost_cash, hours, outlay = F(2), F(1), F(1)
failure_index, gamma = F(1, 2), 1
arrival = failure_index**gamma
a_surv = beta * (1 - delta)
ceiling = theta * yield_rec * stake * beta**lag
r = receipt(beta, delta, lag, theta, yield_rec, stake, arrival)
assert a_surv == F(81, 100) and ceiling == F(243, 20)
assert r == F(1215, 119)

# An exact geometric prefix plus its untruncated analytic tail.
ratio = (1 - arrival) * a_surv
prefix = sum((arrival * ratio**k for k in range(5)), F(0))
tail = arrival * ratio**5 / (1 - ratio)
assert ceiling * (prefix + tail) == r

# Threshold factorization, equality, and signs on either side.
cost_low = cost_cash + hours * F(5)
lam_star = boundary(ceiling, a_surv, cost_low)
assert lam_star == F(133, 648) and 0 < lam_star < arrival
assert receipt(beta, delta, lag, theta, yield_rec, stake, lam_star) == cost_low
factorized = (ceiling - a_surv * cost_low) * (arrival - lam_star)
factorized /= 1 - a_surv + a_surv * arrival
assert factorized == r - cost_low == F(382, 119)
assert receipt(beta, delta, lag, theta, yield_rec, stake, lam_star / 2) < cost_low
assert receipt(beta, delta, lag, theta, yield_rec, stake, (1 + lam_star) / 2) > cost_low

# Cash-rich dormancy with identical technical cost, yield, and stake.
cost_high = cost_cash + hours * F(10)
assert boundary(ceiling, a_surv, cost_high) == F(76, 81) > arrival
assert r - cost_high == F(-213, 119)
bridge = outlay * lag
start_buffer = cost_cash + bridge
assert bridge == F(2) and start_buffer == F(4)
assert F(1) < bridge <= F(3) < start_buffer <= F(5) < F(10)
assert yield_rec * stake - cost_cash == F(18) > 0

# Fresh cash prefix and mature-pipeline refill; no repeated bridge charge.
initial, surplus = F(4), F(5)
cash_at_lag = initial - cost_cash - outlay * lag
cash_after = cash_at_lag + surplus * F(1)
assert cash_at_lag == 0 and cash_after == F(5)
waiting_initial, waiting_surplus = F(3), F(3)
funding_time = F(lag) + (cost_cash + bridge - waiting_initial) / waiting_surplus
assert waiting_initial - bridge + waiting_surplus * (funding_time - lag) == cost_cash
refill_periods = 1  # ceil(2/5), exactly checked below.
assert (refill_periods - 1) * surplus < cost_cash <= refill_periods * surplus
buffer = cost_cash
assert buffer - cost_cash + surplus * refill_periods >= buffer
q_beta = beta**(lag + refill_periods) * arrival / (1 - beta + beta * arrival)
assert 0 < q_beta < 1
regen_value = (r - cost_low) / (1 - q_beta)
assert regen_value == (r - cost_low) + q_beta * regen_value > 0

# A particular no-renewal cutoff: old known errors cannot replenish evidence.
eta = F(1, 2)
assert arrival * eta > lam_star > arrival * eta**2
assert receipt(beta, delta, lag, theta, yield_rec, stake, arrival * eta) > cost_low
assert receipt(beta, delta, lag, theta, yield_rec, stake, arrival * eta**2) < cost_low

# Sandbox: gamma=0 gives arrival=1; capture=1, no lag/hazard/opportunity cost.
sandbox_arrival = failure_index**0
sandbox = receipt(beta, F(0), 0, F(1), yield_rec, stake, sandbox_arrival)
assert sandbox - cost_cash == yield_rec * stake - cost_cash == F(18)
print("PASS P3.5 exact identities, cash-rich sign flip, funding, renewal, stopping, sandbox")
print("receipt=1215/119; active_margin=382/119; dormant_margin=-213/119; sandbox_margin=18")
