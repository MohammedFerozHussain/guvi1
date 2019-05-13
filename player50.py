N=int(input())
li=[]
for i in range(2,N):
  li.append(i)
for i in li:
  if N%i==0:
    print("yes")
    break
else:
  print("no")   
