from collections import deque

dif = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def dfs(_y, _x):
    global c
    q = deque()
    q.append([_y, _x])
    while q:
        tmp_y, tmp_x = q.pop()
        c[tmp_y][tmp_x] = "#"
        for d in dif:
            if 0 <= tmp_x + d[1] <= W - 1 and 0 <= tmp_y + d[0] <= H - 1:
                if c[tmp_y + d[0]][tmp_x + d[1]] == "g":
                    print("Yes")
                    exit()
                elif c[tmp_y + d[0]][tmp_x + d[1]] == ".":
                    q.append([tmp_y + d[0], tmp_x + d[1]])
                    continue
                else:
                    continue
            else:
                continue

H, W = map(int, input().split())
c = [[] for _ in range(H)]
for i in range(H):
    c[i] = list(input())
    try:
        tmp = c[i].index('s')
    except:
        tmp = -1
    if tmp > -1:
        x = tmp
        y = i

dfs(y, x)
print("No")
