m=int(input())
li=list(map(str,input().split()))
k=input()
l=len(k)
c=0
for i in range(0,m):
  a=li[i]
  b=a[0:l]
  if k==b:
    c+=1
  a=''
print(c)   
