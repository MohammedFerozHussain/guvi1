def sumofAP(n2,a2,d2):
    su=0
    i=0
    while i<n2:
        su+=a2
        a2+=d2
        i+=1
    return su    
n2,a2,d2=map(int,input().split())
print(sumofAP(n2,a2,d2))
