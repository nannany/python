from collections import deque

INF = 100000000
H, W, N = list(map(int, input().split()))
maze = [list(input()) for i in range(H)]

x = -1
for letters in maze:
    x += 1
    y = -1
    for letter in letters:
        y += 1
        if letter == "S":
            sx = x
            sy = y
        elif letter == str(N):
            gx = x
            gy = y

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def bfs():
    q = deque([[sx, sy]])
    for i in range(1, N + 1):
        d = [[INF for i in range(W)] for j in range(H)]
        if i == 1 :
            d[sx][sy] = 0
        else :

        while len(q) != 0:
            tmp_q = q.popleft()
            print(tmp_q)
            tmp_x = tmp_q[0]
            print("x" + str(tmp_x))
            tmp_y = tmp_q[1]
            print(tmp_y)
            if maze[tmp_x][tmp_y] == str(i): break
            for j in range(0, 4):
                nx = tmp_x + dx[j]
                ny = tmp_y + dy[j]
                if 0 <= nx < H and 0 <= ny < W and maze[nx][ny] != "X" and d[nx][ny] == INF:
                    q.append([nx, ny])
                    d[nx][ny] = d[tmp_x][tmp_y] + 1
    return d[gx][gy]


if __name__ == '__main__':
    ans = bfs()
    print(ans)
