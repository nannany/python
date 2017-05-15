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

    return len(xs)


if __name__ == '__main__':
    W, H = list(map(int, input().split()))
    N = int(input())
    X1 = []
    X2 = []
    Y1 = []
    Y2 = []
    for i in range(0, N):
        inputs = list(map(int, input().split()))
        X1.append(inputs[0])
        X2.append(inputs[1])
        Y1.append(inputs[2])
        Y2.append(inputs[3])

    W = compress(X1, X2, W)
    H = compress(Y1, Y2, H)

    fld = [False for i in range(6 * N)]

    for i in range(0, N):
        for y in range(Y1[i], Y2[i]):
            for x in range(X1[i], X2[i]):
                fld[y][x] = True

    ans = 0
