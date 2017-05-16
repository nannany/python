import queue


class XY:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def compress(x1, x2, _w):
    xs = []
    for i in range(0, N):
        for d in range(-1, 2):
            tx1 = x1[i] + d
            tx2 = x2[i] + d
            if 0 <= tx1 <= _w:
                xs.append(tx1)
            if 0 <= tx2 <= _w:
                xs.append(tx2)
    xs = list(set(xs))
    xs.sort()

    for i in range(0, N):
        x1[i] = xs.index(x1[i])
        x2[i] = xs.index(x2[i])

    return len(xs) -1


if __name__ == '__main__':
    while True:
        W, H = list(map(int, input().split()))
        if W == 0 and H == 0: break
        N = int(input())
        X1 = []
        X2 = []
        Y1 = []
        Y2 = []
        for i in range(0, N):
            inputs = list(map(int, input().split()))
            X1.append(inputs[0])
            Y1.append(inputs[1])
            X2.append(inputs[2])
            Y2.append(inputs[3])

        W = compress(X1, X2, W)
        H = compress(Y1, Y2, H)
        # print(str(W) + " " + str(H))
        fld = [[False for i in range(6 * N)] for i in range(6 * N)]
        for i in range(0, N):
            for y in range(Y1[i], Y2[i]):
                for x in range(X1[i], X2[i]):
                    fld[y][x] = True
        ans = 0
        dx = [0, 1, 0, -1]
        dy = [-1, 0, 1, 0]

        # for i in range(0, 6):
        #     for j in range(0, 15):
        #         if fld[i][j]:
        #             if j != 14:
        #                 print("■", end="")
        #             else:
        #                 print("■")
        #         else:
        #             if j != 14:
        #                 print("　", end="")
        #             else:
        #                 print("　")

        for y in range(0, H):
            for x in range(0, W):
                if fld[y][x]:
                    continue
                # print("xy" + str(x) + " " + str(y))
                ans += 1

                que = []
                que.append(XY(x, y))

                while len(que) != 0:
                    xy = que.pop()
                    sx = xy.x
                    sy = xy.y
                    for i in range(0, 4):
                        tx = sx + dx[i]
                        ty = sy + dy[i]
                        if tx < 0 or W <= tx or ty < 0 or H <= ty:
                            continue
                        if fld[ty][tx]: continue
                        que.append(XY(tx, ty))
                        # print("txty" + str(tx) + " " + str(ty))
                        fld[ty][tx] = True

        print(ans)
