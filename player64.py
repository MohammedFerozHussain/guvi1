n,k=map(int,input().split())
li=list(map(int,input().split()))
li.sort()
l=[]
for i in li:
    if i<k:
        l.append(i)
print(*l)        
            
        
