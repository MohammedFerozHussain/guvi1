def GCD(x,y):
    if x>y:
        sm=y
    else:
        sm=x
    for i in range(1,sm+1):
        if((x%i==0) and (y%i==0)):
            gcd=i
    return gcd
y1,y2=map(int,input().split())
print(GCD(y1,y2))
