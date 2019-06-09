n=int(input())
li=list(map(int,input().split()))
l=[]
s=0
for i,j in enumerate(li):
    s+=li[i]
    l.append(s)
print(*l)
    
