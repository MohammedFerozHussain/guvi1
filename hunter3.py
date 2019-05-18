n=int(input())
li=list(map(int,input().split()))
r=[]
for i,j in enumerate(li):
    if i==j:
        r.append(j)
        c=sorted(r)
print(*c)        
