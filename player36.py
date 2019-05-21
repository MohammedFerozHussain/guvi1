n,m=map(int,input().split())
c=0
s=len(str(n))
for i in range(0,s):
  v=n%10
  n=n//10
  if v==m:
    c+=1
print(c)    
