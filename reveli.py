n=int(input())
li=list(map(str,input().split()))
c=li[::-1]
for i in c:
    d="->".join(c)
print(d)
