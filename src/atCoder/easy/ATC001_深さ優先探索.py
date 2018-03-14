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
    c = [list(input()) for _ in range(H)]

    y = 0
    for letters in c:
        if "s" in letters:
            x = letters.index("s")
            break

        y += 1

    if dfs(y, x):
        print("Yes")
    else:
        print("No")
