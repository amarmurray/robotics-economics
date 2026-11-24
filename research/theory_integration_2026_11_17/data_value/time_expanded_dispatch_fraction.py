from fractions import Fraction as F
s,a,b,d=F(1,2),F(5,16),F(7,32),F(1,8)
base=-F(1,4)-s-2*a+6*b
assert base==-F(1,16)
rows=[]
for qa in range(5):
 for qbK in range(5):
  for qbP in range(8):
   for n,q in [(8,qa),(8,qbK),(14,qbP)]:
    cells=[q,n//2-q,n//2-q,q]; assert sum(cells)==n and min(cells)>=0
   delta=F(qbK+qbP-qa,64)
   e=F(83,8)+2*F(qa,64);g=F(165,16)+2*F(qbK+qbP,64)
   assert g-e==base+2*delta
   rows.append((g-e,delta))
assert min(x for x,_ in rows)==-F(3,16)
assert max(x for x,_ in rows)==F(9,32)
assert min(base+F(7,4)*z-F(1,16) for _,z in rows if z>=F(1,8))==F(3,32)
print(len(rows),min(x for x,_ in rows),max(x for x,_ in rows),'audit',F(3,32))
