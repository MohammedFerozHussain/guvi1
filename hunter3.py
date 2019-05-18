n=int(input())
li=list(map(int,input().split()))
r=[]
c1=[]
for i,j in enumerate(li):
    if i==j:
        r.append(j)
c1=sorted(r)
if c1:
    print(*c1)
else:
    print(-1)
