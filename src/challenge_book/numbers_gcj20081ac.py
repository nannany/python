import numpy as np


def pow(_matrix, _n):
    res = np.identity(2)
    while _n > 0:
        if _n & 1:
            res = res.dot(_matrix)
            res = np.mod(res, 1000)
        _matrix = _matrix.dot(_matrix)
        _matrix = np.mod(_matrix, 1000)
        _n >>= 1

    return res


if __name__ == '__main__':
    caseNo = int(input())
    for i in range(1, caseNo + 1):
        n = int(input())
        m = np.matrix('3 5;1 3')
        m = pow(m, n)
        print("Case #{0:d}: {1:03d}".format(i, int((m[0, 0] * 2 - 1) % 1000)))
