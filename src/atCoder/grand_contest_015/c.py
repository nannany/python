N, M, Q = list(map(int, input().split()))
S = [list(map(int, list(input()))) for i in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def dfs(_x, _y):
    target_map[_x][_y] = 0
    for l in range(0, 4):
        nx = _x + dx[l]
        ny = _y + dy[l]
        if 0 <= nx <= tmp_N and 0 <= ny <= tmp_M and target_map[nx][ny] == 1:
            dfs(nx, ny)


for i in range(Q):
    x1, y1, x2, y2 = list(map(int, input().split()))

    target_map = []
    for j in range(x1 - 1, x2):
        tmp_list = []
        for k in range(y1 - 1, y2):
            tmp_list.append(S[j][k])
        target_map.append(tmp_list)

    res = 0
    tmp_N = x2 - x1
    tmp_M = y2 - y1

    for j in range(0, tmp_N + 1):
        for k in range(0, tmp_M + 1):
            if target_map[j][k] == 1:
                dfs(j, k)
                res += 1

    print(res)
