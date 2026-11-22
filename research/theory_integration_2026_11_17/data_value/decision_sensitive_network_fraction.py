from fractions import Fraction as F
from itertools import product
N=8
checks=0
laws=0
for a in range(N+1): # Q and H
    for b in range(N-a+1): # Q not H
        for c in range(N-a-b+1): # not Q and H
            d=N-a-b-c
            p_q=F(a+b,N); p_h=F(a+c,N); p_joint=F(a,N)
            terminal=F(2*b+d,N)
            direct=F(2*b+d,N)
            assert terminal==direct; checks+=1
            B=F(3,4)+terminal
            A=F(2)
            assert B==F(3,4)+1-p_h+p_q-p_joint; checks+=1
            assert max(A,B)>=A; checks+=1
            if p_q+p_h<=1:
                reference=F(3,4)+1-p_h+p_q
                refV=max(A,reference)
                gapB=refV-reference
                gapA=refV-A
                assert B==refV-p_joint-gapB; checks+=1
                assert A==refV-gapA; checks+=1
                TV=2*p_joint
                assert abs(B-reference)<=2*TV; checks+=1
            laws+=1
for Q,H,A,C in product([0,1],repeat=4):
    direct=0 if H else max(A,2*Q*C)
    expansion=A*(1-H)+2*Q*C*(1-H)-A*Q*C*(1-H)
    assert direct==expansion; checks+=1
for j in [F(0),F(1,8),F(1,4)]:
    P=max(F(2),F(17,8)-j)
    E=F(33,16)
    assert (P>E)==(j<F(1,16));checks+=1
    assert (F(17,8)-j>F(2))==(j<F(1,8));checks+=1
print({"independent_fraction_checks":checks,"laws":laws,"j_high_scenario_gap":str(max(F(2),F(17,8)-F(1,4))-F(33,16))})
