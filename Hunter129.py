def a(l, n):
    l.sort()
    m=1
    r=l[0] 
    c=1
    for i in range(1, n):  
        if (l[i]==l[i-1]): 
            c+=1
        else : 
            if (c>m):  
                m=c
                r=l[i-1] 
            c=1
    if (c>m):
        m=c 
        r=l[n-1] 
    return r 
n=int(input())
l=list(map(int,input().split()))
print(a(l, n)) 
