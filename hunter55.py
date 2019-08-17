c,d=map(int,input().split())
l=list(map(int,input().split()))
c1=l[d:]+l[:d]
print(*c1)
