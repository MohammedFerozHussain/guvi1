n=int(input())
s=0
for i in range(0,n):
    c=n%10
    s=s+c 
    n=n//10
s1=str(s)
c=s1[::-1]
if c==s1:
    print("YES")
else:
    print("NO")
