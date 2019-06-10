n,k=map(int,input().split())
l=list(map(int,input().split()))
li=[]
for i in l:
  if i%2!=0:
    li.append(i)
    li.sort()
c=li[k-1]
print(c)        
    
    
