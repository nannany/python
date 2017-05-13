N, M = list(map(int, input().split()))

road = [[] for i in range(N)]
for i in range(M):
    a, b = list(map(int, input().split()))
    road[a - 1].append(b)
    road[b - 1].append(a)

for i in range(N):
    print(len(road[i]))
