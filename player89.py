def nPr(n, r):
    return (fact(n) // fact(n - r)) 
def fact(n):
    f=1
    for i in range(2, n+1): 
        f=f*i 
    return f
n,r=map(int,input().split())
print(nPr(n, r)) 
