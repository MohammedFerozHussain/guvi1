n=int(input())
l=[]
for i in range(n):
  li=list(map(int,input().split()))
  for i in li:
    l.append(i)
l.sort()
print(*l)    
