if __name__ == '__main__':
    s = input()
    x, y = map(int, input().split())

    s = s.split("T")
    s = [len(_) for _ in s]

    x_move = [ele for (i, ele) in enumerate(s) if i % 2 == 0]
    y_move = [ele for (i, ele) in enumerate(s) if i % 2 == 1]

    dpx = [[False for _ in range(sum(x_move) * 2 + 1)] for _ in range(len(x_move) + 1)]

    dpx[1][x_move[0]] = True
    for i, _x in enumerate(x_move):
        if i == 0:
            continue

        for j in range(-sum(x_move), sum(x_move) + 1):
            dpx[i + 1][j] = dpx[i][j - _x] or dpx[i][j + _x]

    dpy = [[False for _ in range(sum(y_move) * 2 + 1)] for _ in range(len(y_move) + 1)]

    dpy[0][0] = True
    for i, _y in enumerate(y_move):
        for j in range(-sum(y_move), sum(y_move) + 1):
            dpy[i + 1][j] = dpy[i][j - _y] or dpy[i][j + _y]

    try:
        dpx[len(x_move)][x] and dpy[len(y_move)][y]
    except:
        print("No")
        exit()

    if dpx[len(x_move)][x] and dpy[len(y_move)][y]:
        print("Yes")
    else:
        print("No")
