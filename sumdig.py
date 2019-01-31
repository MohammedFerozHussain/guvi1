n1=int(input())
dig=0
while n1>0:
  a=n1%10
  dig=dig+a
  n1=n1//10
print(dig)  
