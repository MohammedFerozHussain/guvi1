s=input()
c=s.upper()
for i in s:
    if s.count(i)>1:
        print("No")
        break
else:
    print("Yes")
