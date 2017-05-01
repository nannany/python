import copy

global M, P, X


def solve():
    n = 1 << M
    prev = [0 for k in range(n + 1)]
    nxt = [0 for k in range(n + 1)]
    prev[n] = 1.0
    for r in range(0, M):
        for l in range(0, n + 1):
            jub = min(l, n - l)
            t = 0.0
            for j in range(0, jub + 1):
                t = max(t, P * prev[l + j] + (1 - P) * prev[l - j])
            nxt[l] = t
        prev = copy.deepcopy(nxt)

    return prev[int(X * n / 1000000)]


if __name__ == '__main__':
    N = int(input())
    for i in range(1, N + 1):
        inputs = input().split()
        M = int(inputs[0])
        P = float(inputs[1])
        X = int(inputs[2])
        ans = solve()
        print("Case #" + str(i) + ": " + ('%0.6f' % ans))
