f,g=map(int,input().split())
li=[]
for i in range(f+1,g):
  if(i%2)==0:
    li.append(i)
print(*li)
