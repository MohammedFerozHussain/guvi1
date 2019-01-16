x,l=map(int,input().split())
lis=[]
for i in range(x,l+1):
    if(i>1):
        for v in range(2,i):
            if(i%v==0):
               break
        else:
            lis.append(i)
print(*lis)       
     
