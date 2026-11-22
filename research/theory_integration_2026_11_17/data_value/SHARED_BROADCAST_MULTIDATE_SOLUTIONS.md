# Separate instructor solutions — adaptive shared-learner data value

**1.** If neither site is eligible or worker F=0, use R=2. If only site 1 is eligible, add v1−2; only site 2, add v2−2; if both, add v1−2, not their sum. Inclusion-exclusion yields `2+(v1−2)FS1+(v2−2)FS2−(v2−2)FS1S2`. Multiple simultaneous independent operators, unsafe/unsuitable fallback R or sequential service with no deadline invalidate the resource assumption.

**2.** R across both dates pays 4. At L=1,W=w, B loses 2−3/4=5/4 current receipt and adds 2 at date 2 iff F(S1∨S2). Its expected incremental unconditional contribution is `2p_w−5m_w/4`; the date-1 lawful policy takes its positive part independently per w. Sum to obtain `J_P=4+sum_w[2p_w−5m_w/4]_+`. If L=0 B is forbidden. With unchanged production kernel, discarding an optional W cannot improve the optimizer.

**3.** Fréchet overlap c lies in [1/2,3/4]. Diversified table (11,10,01,00)=(1/2,1/4,1/4,0) gives eligible union1, p_given_L=3/4, positive pilot gain `2·3/4−5/4=1/4` and J_P=4+(1/2)(1/4)=33/8. Synchronized table=(3/4,0,0,1/4) gives p_given_L=9/16, negative pilot gain -1/8, so J_P=4 by retained R. E=65/16 lies between. If F depends on joint failures, the complete triple law `Pr(F,S1,S2|L,W,do B)`, not f times a union, is necessary.
