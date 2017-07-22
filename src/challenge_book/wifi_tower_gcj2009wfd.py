class Edge:
    def __init__(self, to, cap, rev):
        self.to = to
        self.cap = cap
        self.rev = rev


def add_edge(_from, _to, _cap):
    G[_from].append(Edge(_to, _cap, len(G[_to])))
    G[_to].append(Edge(_from, 0, len(G[_from]) - 1))


def dfs(_v, _t, _f):
    if _v == _t:
        return _f
    global used
    used[_v] = True
    for i in range(0, len(G[_v])):
        e = G[_v][i]
        if not used[e.to] and e.cap > 0:
            d = dfs(e.to, _t, min(_f, e.cap))
            if d > 0:
                e.cap -= d
                G[e.to][e.rev].cap += d
                return d
        G[_v][i] = e
    return 0


def max_flow(_s, _t):
    flow = 0
    while True:
        global used
        used = [0 for i in range(V)]
        f = dfs(_s, _t, float("inf"))
        if f == 0:
            return flow
        flow += f


def sqr(_x):
    return _x * _x


if __name__ == '__main__':
    T = int(input())
    for caseNo in range(1, T + 1):
        n = int(input())
        x = []
        y = []
        r = []
        s = []
        for i in range(n):
            tmp_x, tmp_y, tmp_r, tmp_s = list(map(int, input().split()))
            x.append(tmp_x)
            y.append(tmp_y)
            r.append(tmp_r)
            s.append(tmp_s)
        V = n + 2
        G = [[] for i in range(V)]
        ans = 0
        for i in range(0, n):
            if s[i] < 0:
                add_edge(n, i, -s[i])
            else:
                ans += s[i]
                add_edge(i, n + 1, s[i])

            for j in range(0, n):
                if i == j:
                    continue

                if sqr(x[i] - x[j]) + sqr(y[i] - y[j]) <= sqr(r[i]):
                    add_edge(j, i, float("inf"))

        ans -= max_flow(n, n + 1)
        print("Case #{0:d}: {1:d}".format(caseNo, ans))
