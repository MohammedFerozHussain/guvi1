x1=int(input())
re=0
while(x1>0):
    dig=x1%10
    re=re*10+dig
    x1=x1//10
print(re)
