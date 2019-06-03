n,m=map(int,input().split())
l=list(map(int,input().split()))
li=list(map(int,input().split()))
r = set(x in l for x in li) 
c = 0
for i in r:
    if i == False:
        c=1
if c==0: 
    print("YES") 
else: 
    print("NO") 
  
