n1=int(input())
sum=0
while n1>0:
  c=n1%10
  sum=sum+c*c
  n1=n1//10
print(sum)  
