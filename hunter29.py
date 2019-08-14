n=int(input())
k=[]
li=[]
l=list(map(int,input().split()))
for i in range(0,len(l)+1):
    for j in range(0,len(l)+1):
        k.append(sum(l[i:j]))
print(max(k))        
    
