s,s1=map(str,input().split())
s2=list(s)
l=[]
s3=list(s1)
li=[]
c=[]
for i in range(0,len(s)-1):
    l.append(s2[i:i+2])
for j in range(0,len(s1)-1):
    li.append(s3[j:j+2])
for i in l:
    for j in li:
        if i==j:
            c=1
            break
if c==1:
    print("yes")
else:
    print("no")
