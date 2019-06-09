n,m=map(int,input().split())
l=list(map(int,input().split()))
c=[]
for i in range(0,n-1):
    for j in range(i+1,m):
        if l[i]+l[j]==l:
            c=1
            break
if c==1:
    print("YES")
else:
    print("NO")
