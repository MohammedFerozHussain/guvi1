s1=input()
s2=input()
s3=list(s1)
s4=list(s2)
if s2 in s1:
    for i,j in enumerate(s1):
        if j==s2[0]:
            print(i)
            break
else:
    print("-1")
