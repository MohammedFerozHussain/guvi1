n,k=map(int,input().split())
li=list(map(int,input().split()))
c=0
for i,j in enumerate(li):
  if j==k:
    c+=1
print(c)        
