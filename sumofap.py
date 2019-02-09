def sumofAP(a,d,n):
    s=0
    i=0
    while i<n:
        s+=a
        a+=d
        i+=1
    return s    
a,d,n=map(int,input().split())
print(sumofAP(a,d,n))
    
