N, K = map(int, input().split())
for i in range(0, N):
    c = K**i
    if c == N:
        print("yes")
        break
else:
    print("no")
