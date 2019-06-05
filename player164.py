n,k=map(int,input().split())
li=list(map(int,input().split()))
if k in li:
  print(k)
else:
  print(min(li))  
