n=int(input())
li=list(map(int,input().split()))
li1=list(map(int,input().split()))
if li==li1[::-1]:
  print("yes")
else:
  print("no")  
