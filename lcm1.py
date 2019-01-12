def findlcm(x1,y1):
    if x1>y1:
        mi=x1
    else:
        mi=y1
    while(1):
        if(mi%x1==0 and mi%y1==0):
            l=mi
            break
        mi=mi+1
    return l
n1,n2=map(int,input().split())
l=findlcm(n1,n2)
print(l)
