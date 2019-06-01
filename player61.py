n,x=map(int,input().split())
l=list(map(int,input().split()))
for i in range(0,n-1):
    if l[i]+l[i+1]==x or l[i]==x:
        print("yes")
        break
else:
    print("no")
    
