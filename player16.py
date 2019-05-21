n=int(input()) 
l=list(map(int,input().split()))
l.sort()
r=[]
for i in range(0,n-1):
  if l[i]==l[i+1]:
    r.append(l[i])
    if i not in r:
      r.append(l[i])
r.sort()      
for i in l:
  if i not in r:
    print(i)      
      
