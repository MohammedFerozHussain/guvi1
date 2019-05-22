n=int(input())
s=0
for i in range(0,n):
    n1=n%10
    s=s+n1*n1
    n=n//10
print(s)    
