import sys
import heapq


class SegmentTree:
    def __init__(self, _n):
        n = 1
        while n < _n:
            n *= 2
        self.n = n
        self.dat = [(sys.maxsize, i) for i in range(0, 2 * n - 1)]

    def update(self, _k, _a):
        _k += self.n - 1
        self.dat[_k] = _a
        while 0 < _k:
            _k = (_k - 1) // 2
            self.dat[_k] = min(self.dat[_k * 2 + 1], self.dat[_k * 2 + 2], key=(lambda x: x[0]))

    def query(self, _a, _b, _k, _l, _r):
        if _r <= _a or _b <= _l:
            return (sys.maxsize, 0)

        if _a <= _l and _r <= _b:
            return self.dat[_k]
        else:
            vl = self.query(_a, _b, _k * 2 + 1, _l, (_l + _r) // 2)
            vr = self.query(_a, _b, _k * 2 + 2, (_l + _r) // 2, _r)
            return min(vl, vr, key=(lambda x: x[0]))


if __name__ == '__main__':
    N = int(input())
    p = list(map(int, input().split()))

    segtree_odd = SegmentTree(N)
    segtree_even = SegmentTree(N)
    for i in range(0, N):
        if i % 2 == 0:
            segtree_even.update(i, (p[i], i))
        else:
            segtree_odd.update(i, (p[i], i))
    pq = []
    heapq.heappush(pq, (segtree_even.query(0, N, 0, 0, N)[0], 0, N))
    ans = []
    while len(ans) != N:
        target_range = heapq.heappop(pq)
        if target_range[1] % 2 == 0:
            tmp_even_min = segtree_even.query(target_range[1], target_range[2], 0, 0, N)
            ans.append(tmp_even_min[0])
            tmp_odd_min = segtree_odd.query(tmp_even_min[1], target_range[2], 0, 0, N)
            ans.append(tmp_odd_min[0])

            # segtree_even.update(tmp_even_min[1], (sys.maxsize, tmp_even_min[1]))
            # segtree_odd.update(tmp_odd_min[1], (sys.maxsize, tmp_odd_min[1]))
            if target_range[1] + 1 != tmp_even_min[1]:
                heapq.heappush(pq, (
                    segtree_even.query(target_range[1], tmp_even_min[1], 0, 0, N)[0], target_range[1], tmp_even_min[1]))
            if tmp_even_min[1] + 1 != tmp_odd_min[1] - 1:
                heapq.heappush(pq, (
                    segtree_odd.query(tmp_even_min[1] + 1, tmp_odd_min[1], 0, 0, N)[0], tmp_even_min[1] + 1,
                    tmp_odd_min[1]))
            if tmp_odd_min[1] + 1 != target_range[2] - 1:
                heapq.heappush(pq, (
                    segtree_even.query(tmp_odd_min[1] + 1, target_range[2], 0, 0, N)[0], tmp_odd_min[1] + 1,
                    target_range[2]))
        else:
            tmp_odd_min = segtree_odd.query(target_range[1], target_range[2], 0, 0, N)
            ans.append(tmp_odd_min[0])
            tmp_even_min = segtree_even.query(tmp_odd_min[1], target_range[2], 0, 0, N)
            ans.append(tmp_even_min[0])

            # segtree_odd.update(tmp_odd_min[1], (sys.maxsize, tmp_odd_min[1]))
            # segtree_even.update(tmp_even_min[1], (sys.maxsize, tmp_even_min[1]))
            if target_range[1] + 1 != tmp_odd_min[1]:
                heapq.heappush(pq, (
                    segtree_odd.query(target_range[1], tmp_odd_min[1], 0, 0, N)[0], target_range[1], tmp_odd_min[1]))
            if tmp_odd_min[1] + 1 != tmp_even_min[1] - 1:
                heapq.heappush(pq, (
                    segtree_even.query(tmp_odd_min[1] + 1, tmp_even_min[1], 0, 0, N)[0], tmp_odd_min[1] + 1,
                    tmp_even_min[1]))
            if tmp_even_min[1] + 1 != target_range[2] - 1:
                heapq.heappush(pq, (
                    segtree_odd.query(tmp_even_min[1] + 1, target_range[2], 0, 0, N)[0], tmp_even_min[1] + 1,
                    target_range[2]))

    ans = list(map(str, ans))
    print(" ".join(ans))
