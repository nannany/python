dx = [-1, -1, 1, 1]
dy = [-1, 0, -1, 0]

G = []
match = []
global used


def add_edge(u, v):
    G[u].append(v)
    G[v].append(u)


def dfs(v):
    used[v] = True
    for i in range(0, len(G[v])):
        u = G[v][i]
        w = match[u]
        if w < 0 or not used[w] and dfs(w):
            match[v] = u
            match[u] = v
            return True

    return False


def bipartite_matching():
    res = 0
    global match
    match = [-1 for i in range(V)]
    for v in range(0, V):
        if match[v] < 0:
            global used
            used = [False for i in range(V)]
            if dfs(v):
                res += 1

    return res


if __name__ == '__main__':
    caseNo = int(input())
    for case in range(1, caseNo + 1):
        M, N = list(map(int, input().split()))
        seat = []
        for i in range(M):
            seat.append(list(input()))

        num = 0
        V = M * N
        G = [[] for i in range(V)]
        for y in range(0, M):
            for x in range(0, N):
                if seat[y][x] == '.':
                    num += 1
                    for k in range(0, 4):
                        x2 = x + dx[k]
                        y2 = y + dy[k]
                        if 0 <= x2 < N and 0 <= y2 < M and seat[y2][x2] == '.':
                            add_edge(x * M + y, x2 * M + y2)

        print("Case #{0:d}: {1:d}".format(case, num - bipartite_matching()))
