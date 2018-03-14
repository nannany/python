import queue

dif = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def dfs(_y, _x):
    global c
    q = queue.Queue()
    q.put([_y, _x])
    while not q.empty():
        tmp_y, tmp_x = q.get()
        c[tmp_y][tmp_x] = "#"
        for d in dif:
            if 0 <= tmp_x + d[1] <= W - 1 and 0 <= tmp_y + d[0] <= H - 1:
                if c[tmp_y + d[0]][tmp_x + d[1]] == "g":
                    return True
                elif c[tmp_y + d[0]][tmp_x + d[1]] == ".":
                    q.put([tmp_y + d[0], tmp_x + d[1]])
    return False


if __name__ == '__main__':
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

    if dfs(y, x):
        print("Yes")
    else:
        print("No")
