N=int(input())
li=[]
l=[]
if N%2==0:
  for i in range(1,N):
    if N%i==0:
      li.append(i)
  for i in li:    
    if i%2!=0:
      l.append(i) 
  print(*l)
elif N%2!=0:
  for i in range(1,N):
    if N%i==0:
      li.append(i)
  for i in li:    
    if i%2!=0:
      l.append(i) 
  if N in l:
    print(*l)
  else:
    l.append(N)
    print(*l)
      



