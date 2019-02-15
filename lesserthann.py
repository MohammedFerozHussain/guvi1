n=int(input())
li=list(map(int,input().split()))
l=[]
for i in li:
    if i<n:
        l.append(i)
print(*l)
