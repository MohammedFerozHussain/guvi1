n,m=map(int,input().split())
o=n+m
c=bin(o)
s=c[2:]
s1=list(s)
c=0
for i,j in enumerate(s1):
    if "1" in j:
        c+=1 
print(c)        
