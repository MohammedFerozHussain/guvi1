s1,s2=map(str,input().split())
a=list(set(s1)&set(s2))
for i in a:
    if i in a:
      print("yes")
      break
else:
  print("no")      
