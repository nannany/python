if __name__ == '__main__':
    N, M, R = list(map(int, input().split()))
    r = list(map(int, input().split()))
    # ワーシャルフロイド
    d = [[float('inf') for i in range(N)] for i in range(N)]
    for i in range(0, N):
        d[i][i] = 0
    for i in range(M):
        A, B, C = list(map(int, input().split()))
        d[A - 1][B - 1] = C
        d[B - 1][A - 1] = C

    for k in range(0, N):
        for i in range(0, N):
            for j in range(0, N):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
    print(d)

    mincost = [float('inf') for i in range(N)]
    used = [False for i in range(N)]

    mincost[r[0] - 1] = 0
    ans = 0

    while True:
        v = -1
        for tmp_r in r:
            # print(tmp_r)
            if not used[tmp_r - 1] and (v == -1 or mincost[tmp_r - 1] < mincost[v]):
                v = tmp_r - 1

        if v == -1:
            break

        used[v] = True
        ans += mincost[v]

        for tmp_r in r:
            mincost[tmp_r - 1] = min(mincost[tmp_r - 1], d[v][tmp_r - 1])

    print(ans)
