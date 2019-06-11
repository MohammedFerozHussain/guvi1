n=int(input())
l=list(map(int,input().split()))
li=list(map(int,input().split()))
l1=[]
for i in range(0,len(l)):
  l1.append(l[i]+li[i])
print(*l1)  
       
  
