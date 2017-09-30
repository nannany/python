from itertools import chain, product

N = int(input())

P = list(chain((0,), map(lambda x: int(x) - 1, input().split())))
# print("P:" + str(P))
X = list(map(int, input().split()))

L = [list() for _ in range(N)]
# print("L:" + str(L))
debug = [None] * N

# 後ろから
for i in reversed(range(N)):
    p = P[i]
    l = L[i]
    print(l)
    x = X[i]

    offset = sum(min(t) for t in l)
    print("offset:" + str(offset))
    x -= offset
    if x < 0:
        print('IMPOSSIBLE')
        exit()
    dp = [False] * (x + 1)
    dp[0] = True
    s = 0
    for a, b in l:
        d = abs(a - b)
        s += d
        for j in reversed(range(x - d + 1)):
            dp[j + d] = dp[j + d] or dp[j]
    m = x
    while not dp[m]:
        m -= 1
    m = s - m
    m += offset
    x += offset

    debug[i] = (x, m)
    L[p].append((x, m))
    L[i] = None

print('POSSIBLE')
print(sum([]))