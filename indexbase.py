num=int(input())
li=list(map(int,input().split()))
c=min(li)
d=max(li)
e=li.index(c)+1
f=li.index(d)+1
print(e,f)

