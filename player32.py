N,K=map(int,input().split())
li=list(map(int,input().split()))
c=sorted(li)
for i in range(0,N):
  if K in c:
    print("Yes")
    break
else:
  print("No")     
