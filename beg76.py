m=int(input())
if m>1:
    for i in range(1,m):
        if m%i==0:
            print("no")
            break
        else:
            print("yes")
            break
else:
    print("no")
