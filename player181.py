n=int(input())
if n%3==0 or n%7==0:
  print("yes")
elif n%3+7==0:
  print("yes")  
else:
  print("no")  
