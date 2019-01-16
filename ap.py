def sumofAP1(n2,a2,d2):
    su1=0
    i=0
    while i<n2:
        su1+=a2
        a2+=d2
        i+=1
    return su1    
n2,a2,d2=map(int,input().split())
print(sumofAP1(n2,a2,d2))
