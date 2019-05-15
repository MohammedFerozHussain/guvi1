n,k=map(int,input().split())
li=list(map(int,input().split()))
for i in range(0,n-1):
  for j in range(i+1,n):
    if li[i]+li[j]==k:
      c=1
      break
if c==1:
  print("yes")
else:
  print("no")    
