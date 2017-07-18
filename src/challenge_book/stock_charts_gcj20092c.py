G = []
used = []
match = []
V = 0


def add_edge(_u, _v):
    G[_u].append(_v)
    G[_v].append(_u)


def dfs(_v):
    used[_v] = True
    for i in range(0, len(G[_v])):
        u = G[_v][i]
        w = match[u]
        if w < 0 or not used[w] and dfs(w):
            match[_v] = u
            match[u] = _v
            return True
    return False


def bipartile_matching():
    res = 0
    global match
    match = [-1 for i in range(V)]
    for v in range(0, V):
        if match[v] < 0:
            global used
            used = [0 for i in range(V)]
            if dfs(v):
                res += 1

    return res


if __name__ == '__main__':
    T = int(input())
    for caseNo in range(1, T + 1):
        N, K = list(map(int, input().split()))
        P = [list(map(int, input().split())) for i in range(N)]
        V = N * 2
        G = [[] for i in range(V)]
        for i in range(0, V):
            G[i].clear()

        for i in range(0, N):
            for j in range(0, N):
                if i == j:
                    continue
                f = True
                for k in range(0, K):
                    if P[j][k] >= P[i][k]:
                        f = False
                if f:
                    add_edge(i, N + j)

        ans = N - bipartile_matching()
        print("Case #{0:d}: {1:d}".format(caseNo, ans))
