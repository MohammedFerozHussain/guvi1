n,k=map(int,input().split())
l=list(map(int,input().split()))
c=[]
li=[]
for i,j in enumerate(l):
    if j>k and k in l:
        li.append(j)
        li.sort()
        c=li[0]
print(c)     
