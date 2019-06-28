n,m=map(int,input().split())
l=list(map(int,input().split()))
c=l[:len(l)-m]
print(*c)
