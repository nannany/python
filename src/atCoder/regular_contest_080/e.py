import sys
import heapq

class SegmentTree:
    def __init__(self, _n):
        n = 1
        while n < _n:
            n *= 2
        self.n = n
        self.dat = [sys.maxsize for i in range(2 * n - 1)]

    def update(self, _k, _a):
        _k += self.n - 1
        self.dat[_k] = _a
        while 0 < _k:
            _k = (_k - 1) / 2
            self.dat[_k] = min(self.dat[_k * 2 + 1], self.dat[_k * 2 + 2])

    def query(self, _a, _b, _k, _l, _r):
        if _r <= _a or _b <= _l:
            return sys.maxsize

        if _a <= _l and _r <= _b:
            return self.dat[_k]
        else:
            vl = self.query(_a, _b, _k * 2 + 1, _l, (_l + _r) / 2)
            vr = self.query(_a, _b, _k * 2 + 2, (_l + _r) / 2, _r)
            return min(vl, vr)


if __name__ == '__main__':
    N = int(input())
    p = list(map(int, input().split()))

    segtree_odd = SegmentTree(N)
    segtree_even = SegmentTree(N)
    for i in range(0, N):
        if i % 2 == 0:
            segtree_even.update(i, p[i])
        else:
            segtree_odd.update(i, p[i])
    pq = []
    heapq.heappush(pq,(segtree_even()))

