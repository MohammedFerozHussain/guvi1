N,M=map(str,input().split())
l=[]
li=[]
for i in N:
  l.append(i)
for j in M:
  li.append(j)
if i in j:
  print("yes")
else:
  print("no")      
