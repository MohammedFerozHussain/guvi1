n=int(input())
li=list(map(int,input().split()))
print("yes" if all(li[i]<=li[i+1] for i in range(0,len(li)-1)) else "no")


