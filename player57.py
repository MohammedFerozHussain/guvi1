s,k=map(str,input().split())
li=[]
l=[]
for i in s:
    li.append(i)
for i,j in enumerate(li):
    if k==j:
        l.append(i+1)
print(l[0]) 
