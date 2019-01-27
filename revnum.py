z=int(input())
re=0
while(z>0):
    dig=z%10
    re=re*10+dig
    z=z//10
print(re)
