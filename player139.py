s=int(input())
c=bin(s)
d=list(c[2:])
c2="".join(d)
c3=list(c2)
c=0
for i,j in enumerate(c3):
  if "1" in j:
    c+=1
print(c)            
    
