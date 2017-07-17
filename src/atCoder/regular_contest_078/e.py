def width(_X, _Y, _n, _x):
    lb = float("inf")
    ub = -float("inf")

    for i in range(0, N):
        x1 = _X[i]
        y1 = _Y[i]
        X2


if __name__ == '__main__':
    M, N = list(map(int, input().split()))
    X1 = []
    Y1 = []
    X2 = []
    Z2 = []
    for i in range(M):
        tmp_x1, tmp_y1 = list(map(int, input().split()))
        X1.append(tmp_x1)
        Y1.append(tmp_y1)
    for i in range(N):
        tmp_x2, tmp_z2 = list(map(int, input().split()))
        X2.append(tmp_x2)
        Z2.append(tmp_z2)

    min1 = min(X1)
    max1 = max(X1)
    min2 = min(X2)
    max2 = max(X2)

    xs = X1.append(X2)
    sorted(xs)

    res = 0
    for i in range(i + 1, len(xs)):
        a = xs[i]
        b = xs[i + 1]
        c = (a + b) / 2
        if min1 <= c <= max1 and min2 <= c <= max2:
            fa = width(X1, Y1, M, a) * width(X2, Z2, N, a)
            fb = width(X1, Y1, M, b) * width(X2, Z2, N, b)
            fc = width(X1, Y1, M, c) * width(X2, Z2, N, c)
            res += (b - a) / 6 * (fa + 4 * fc + fb)

