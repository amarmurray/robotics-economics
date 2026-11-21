#!/usr/bin/env python3
"""Independent exact Fraction audit; no actual robot or customer data."""
from fractions import Fraction as F
from itertools import product
def main():
    n=0
    for ps,pr,qs,qr in product(range(11),repeat=4):
        i=0 if ps>=pr else 1
        j=0 if qs>=qr else 1
        D=max(ps,pr)-max(qs,qr)
        a=abs((ps,pr)[i]-(qs,qr)[i])
        b=abs((ps,pr)[j]-(qs,qr)[j])
        assert D<=a and -D<=b and abs(D)<=max(a,b)
        m=F(99,100)*abs(ps-qs)+F(1,100)*abs(pr-qr)
        C=F(100) if i or j else F(100,99)
        assert F(max(a,b))<=C*m
        n+=1
    k=0
    for p1,p2,q1,q2 in product(range(11),repeat=4):
        assert abs(p1*p2-q1*q2)<=10*abs(p1-q1)+q1*abs(p2-q2)
        k+=1
    assert F(45,100)-F(-15,100)==F(3,5)
    print({"one_stage_cases":n,"two_stage_cases":k,"tail":str(F(3,5)),"passed":True})
if __name__=="__main__":main()
