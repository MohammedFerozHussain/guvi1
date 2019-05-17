m=int(input())
if m>=1:
    for i in range(1,m):
        if m%i==0:
            print("yes")
            break
        else:
            print("no")
            break
else:
    print("no")
    
