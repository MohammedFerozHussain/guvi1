n,m=map(int,input().split())
sum1=0
for i in range(n,m+1):
    if i %2!=0:
        sum1=sum1+i
print(sum1)    
