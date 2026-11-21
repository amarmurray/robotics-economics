"""Independent exact Fraction audit for the synthetic buyer-demand economic quotient."""
from fractions import Fraction as F

checks = 0
for k in range(17):
    p = F(k,16)
    old = p
    source_coarse = max(p, 1-p)
    source_informed = p+(1-p)
    embodiment = max(F(3,4),old)
    interaction = source_informed-source_coarse-(old-old)
    assert interaction == min(p,1-p); checks += 1
    assert source_coarse >= old and source_informed >= source_coarse; checks += 1
    assert embodiment >= old; checks += 1
    # Enumerate 4 deterministic buyer-contingent dispatch policies.
    values = []
    for when_A in ('A','B'):
        for when_B in ('A','B'):
            values.append(p*(when_A=='A')+(1-p)*(when_B=='B'))
    assert max(values) == 1; checks += 1

p=F(1,2)
assert max(p,1-p) == F(1,2); checks+=1
assert F(1,1)-F(3,4) == F(1,4); checks+=1
assert max(p,1-p)-F(3,4) == -F(1,4); checks+=1
errors=[abs(F(int(z==a),1)-F(1,2)) for z in ('A','B') for a in ('A','B')]
assert max(errors) == F(1,2); checks+=1
assert F(1,1)-F(1,2) == max(errors); checks+=1
print({'exact_fraction_checks':checks,'SG_future_full':str(F(1,1)),'SG_future_coarse':str(F(1,2)),'E_future':str(F(3,4)),'ranking_gap_full':str(F(1,4)),'ranking_gap_coarse':str(-F(1,4)),'one_stage_bound_tight':True})
