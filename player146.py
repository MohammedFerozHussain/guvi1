n1,n2=map(int,input().split())
fac=1
fac1=1
for i in range(1,n1+1):
  fac*=i
for j in range(1,n2+1):
  fac1*=j
c=fac//fac1
print(c)      
