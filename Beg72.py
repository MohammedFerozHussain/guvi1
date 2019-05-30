s=input()
l=list(s)
li=["a","e","i","o","u"]
for i,j in enumerate(li):
  if j in l:
    print("yes")
    break
else:
  print("no")        
