x,z=input().split()
if len(x) > len(z):
    print(x)
elif len(x) == len(z):
    print(x or z)
