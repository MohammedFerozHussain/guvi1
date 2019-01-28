import statistics
a = [int(x) for x in input().split()]
w=a.sort()
median=statistics.median(a)
print(median)
