d,g=map(int,input().split())
li=[]
for num in range(d, g):
  sum1=0
  s=len(str(num))
  y=num
  while(y>0):
    d=y%10
    sum1=sum1+d**s
    y=y//10
  if(num==sum1):
    li.append(num)
print(*li)
