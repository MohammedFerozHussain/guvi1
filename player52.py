N,K=map(int,input().split())
li=list(input().split())
li.sort()
print(*li[K-1:K])
