import math


# union find。初期化
def init(_n):
    for i in range(0, _n):
        par[i] = i
        rank[i] = 0


# 木の根を求める
def find(_x):
    if par[_x] == _x:
        return _x
    else:
        par[_x] = find(par[_x])
        return par[_x]


# 集合を併合
def unite(_x, _y):
    _x = find(_x)
    _y = find(_y)
    if _x == _y:
        return

    if rank[_x] < rank[_y]:
        par[_x] = _y
    else:
        par[_y] = _x
        if rank[_x] == rank[_y]:
            rank[_x] += 1


# 同じ集合かどうか
def same(_x, _y):
    return find(_x) == find(_y)


def is_prime(_n):
    for j in range(2, int(math.sqrt(_n)) + 1):
        if _n % j == 0:
            return False
    return True


def sieve(_n):
    prime_or_not = [True for i in range(_n + 1)]
    p = 0
    prime_or_not[0] = prime_or_not[1] = False
    for i in range(2, _n + 1):
        if prime_or_not[i]:
            prime.append(i)
            p += 1
            for j in range(2 * i, _n + 1, i):
                prime_or_not[j] = False
    return p


if __name__ == '__main__':
    T = int(input())
    prime = []
    # for i in range(2, 1000000):
    #     if is_prime(i):
    #         prime.append(i)
    p = sieve(1000000)
    for caseNo in range(1, T + 1):
        A, B, P = list(map(int, input().split()))

        len = B - A + 1
        par = [0 for i in range(len)]
        rank = [0 for i in range(len)]
        init(len)
        for i in range(0, p):
            if prime[i] >= P:
                start = int((A + prime[i] - 1) / prime[i]) * prime[i]
                end = int(B / prime[i]) * prime[i]
                for j in range(start, end + 1, prime[i]):
                    unite(start - A, j - A)

        res = 0
        for i in range(A, B + 1):
            if find(i - A) == i - A:
                res += 1

        print("Case #{0:d}: {1:d}".format(caseNo, res))
