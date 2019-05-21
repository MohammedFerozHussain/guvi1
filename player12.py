n,m=map(int,input().split())
li=list(map(int,input().split()))
r=[]
for i in range(n-m,n):
  r.append(li[i])
for i in li:
  if i not in r:
    r.append(i)
print(*r)      
