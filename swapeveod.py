li=[]
n1=input()
n1=list(n1)
n1.insert(0,"q")
for i in range(1,len(n1),2):
  n1[i],n1[i+1]=n1[i+1],n1[i]
del n[0]
print(" ".join(n1))
