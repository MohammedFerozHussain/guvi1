import statistics
n=int(input())
a = list(map(int,input().split()))
w=a.sort()
median=statistics.median(a)
print(median)
