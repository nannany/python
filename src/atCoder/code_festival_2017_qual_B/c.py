import sys

sys.setrecursionlimit(10 ** 6)


def dfs(v, c):
    flgs[v] = c
    for i in range(len(G[v])):
        if flgs[G[v][i]] == c:
            return False
        if flgs[G[v][i]] == 0 and not dfs(G[v][i], -c):
            return False

    return True


if __name__ == '__main__':
    N, M = map(int, input().split())
    G = [[] for _ in range(N + 1)]
    for i in range(M):
        a, b = map(int, input().split())
        G[a].append(b)
        G[b].append(a)

    # 二部グラフ判定をする
    bi_flg = True
    flgs = [0 for _ in range(N + 1)]
    for i in range(1, N + 1):
        if flgs[i] == 0:
            if not dfs(i, 1):
                bi_flg = False

    if bi_flg:
        # 二部グラフならBW-M
        print(flgs.count(1) * flgs.count(-1) - M)
    else:
        # 二部グラフでないなら全辺-M
        print((N * (N - 1) // 2) - M)
