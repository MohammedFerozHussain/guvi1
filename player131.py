n=int(input())
s=0
for i in range(0,n):
    c=n%10
    s=s+c 
    n=n//10
if s%2==0:
    print("E")
else:
    print("O")
    
