from collections import deque

d = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def bfs(n):
    global pos_x, pos_y
    while len(que) != 0:
        x, y = que.popleft()
        for dx, dy in d:
            if 0 <= x + dx < W and 0 <= y + dy < H:
                if meiz[x + dx][y + dy] == str(n):
                    pos_x = x + dx
                    pos_y = y + dy
                    # print(distance)
                    return distance[x][y] + 1
                elif meiz[x + dx][y + dy] != "X" and distance[x + dx][y + dy] == float("inf"):
                    distance[x + dx][y + dy] = distance[x][y] + 1
                    # print(distance)
                    que.append((x + dx, y + dy))


if __name__ == '__main__':
    H, W, N = list(map(int, input().split()))
    meiz = [input() for i in range(H)]

    pos_x = 0
    for tmp in meiz:
        if tmp.find("S") != -1:
            pos_y = tmp.find("S")
            break
        pos_x += 1

    ans = 0
    for i in range(1, N + 1):
        distance = [[float("inf") for i in range(W)] for i in range(H)]
        distance[pos_x][pos_y] = 0
        que = deque()
        que.append((pos_x, pos_y))
        # print(que)
        ans += bfs(i)

    print(ans)
