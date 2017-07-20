import math


def cover(_x, _y, _r):
    S = 0
    for i in range(0, N):
        if R[i] <= _r:
            dx = _x - X[i]
            dy = _y - Y[i]
            dr = _r - R[i]
            if dx * dx + dy * dy <= dr * dr:
                S |= 1 << i

    return S


def C(_r):
    cand = [0]
    for i in range(0, N):
        for j in range(0, i):
            if R[i] < _r and R[j] < _r:
                x1 = X[i]
                y1 = Y[i]
                r1 = _r - R[i]
                x2 = X[j]
                y2 = Y[j]
                r2 = _r - R[j]
                dx = x2 - x1
                dy = y2 - y1
                a = dx * dx + dy * dy
                b = ((r1 * r1 - r2 * r2) / a + 1) / 2
                d = r1 * r1 / a - b * b
                if d >= 0:
                    d = math.sqrt(d)
                    x3 = x1 + dx * b
                    y3 = y1 + dy * b
                    x4 = -dy * d
                    y4 = dx * d
                    ij = 1 << i | 1 << j
                    cand.append(cover(x3 - x4, y3 - y4, _r) | ij)
                    cand.append(cover(x3 + x4, y3 + y4, _r) | ij)

    for i in range(0, N):
        if R[i] <= _r:
            cand.append(cover(X[i], Y[i], _r) | 1 << i)

    for i in range(0, len(cand)):
        for j in range(0, i):
            if cand[i] | cand[j] == (1 << N) - 1:
                return True

    return False


if __name__ == '__main__':
    T = int(input())
    for caseNo in range(1, T + 1):
        N = int(input())
        X = []
        Y = []
        R = []
        for i in range(N):
            tmp_x, tmp_y, tmp_r = list(map(int, input().split()))
            X.append(tmp_x)
            Y.append(tmp_y)
            R.append(tmp_r)

        lb = 0
        ub = 10000
        for i in range(100):
            mid = (lb + ub) / 2
            if C(mid):
                ub = mid
            else:
                lb = mid

        print("Case #{0:d}: {1:.6f}".format(caseNo, ub))
