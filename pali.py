n=int(input())
e=n
sum1=0
while(0<n):
  f=n%10
  sum1=sum1*10+f
  n=n//10
if(e==sum1):
  print("yes")
else:
  print("no")
