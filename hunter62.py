n=int(input())
li=list(map(int,input().split()))
li.sort()
c=li[0]
d=max(li)
k=d-c
print(k)
