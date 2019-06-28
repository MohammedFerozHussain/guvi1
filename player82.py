def AND(a, n) :
    ans = a[0] 
    for i in range(n) : 
        ans &= a[i]
    return ans 
n=int(input())
a=list(map(int,input().split()))
print(AND(a, n)) 
