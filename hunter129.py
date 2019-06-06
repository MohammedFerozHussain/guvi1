n=int(input())
li=list(map(int,input().split()))
r=[]
for i in range(0,n-1):
    count=1
    for j in li[i+1:]:
        if li[i]==j:
            count+=1
            break
    if count>1 and j not in r:
        r.append(j)
if r:
    c=sorted(r)
    print(*c)
