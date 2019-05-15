N=int(input())
li=list(map(int,input().split()))
c=[]
d=max(li)
li.remove(li[0])
for i in range(0,N-2):
  if li[i]>li[i+1]:
    c.append(li[i])
c.append(li[N-2])
print(*c)
print(d)
    
          
