import sys

d = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def dfs(x, y, c):
    judged[x][y] = True
    for dx, dy in d:
        if 0 <= x + dx < H and 0 <= y + dy < W and (not judged[x + dx][y + dy]) and orchard[x + dx][y + dy] == c:
            dfs(x + dx, y + dy, c)


if __name__ == '__main__':
    while True:
        H, W = list(map(int, input().split()))
        if H == 0 and W == 0:
            break
        orchard = [input() for i in range(H)]
        judged = [[False for i in range(W)] for j in range(H)]
        # print(orchard)
        ans = 0
        for i in range(0, H):
            for j in range(0, W):
                if not judged[i][j]:
                    ans += 1
                    dfs(i, j, orchard[i][j])

        print(ans)
