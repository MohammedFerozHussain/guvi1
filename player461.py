import math
A=int(input())
c=math.radians(A)
x=math.sin(c)
c1=(round(x,1))
k=abs(c1)
if k<1 :
  print(c1)
else:
  print(round(c1))
