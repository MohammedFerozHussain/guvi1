def c(n): 
    if n <=1 : 
        return 1
    r=0 
    for i in range(n): 
        r+=c(i)*c(n-i-1)
    return r 
n=int(input())
l=[]
for i in range(0,n+1): 
    l.append(c(i))
print(*l)    
