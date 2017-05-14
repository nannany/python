class Edge:
    def __init__(self, fromE, to, cost):
        self.fromE = fromE
        self.to = to
        self.cost = cost


def min_path(_s):
    d[_s] = 0
    while True:
        update = False
        for k in range(0, M):
            edge = abc[k]
            if d[edge.fromE - 1] != float("inf") and d[edge.to - 1] > d[edge.fromE - 1] + edge.cost:
                d[edge.to - 1] = d[edge.fromE - 1] + edge.cost
                update = True
        if not update:
            break


def find_negative_loop():
    d = [0 for i in range(N)]
    for i in range(0, N):
        for j in range(0, M):
            edge = abc[j]
            if d[edge.to - 1] > d[edge.fromE - 1] + edge.cost:
                d[edge.to - 1] = d[edge.fromE - 1] + edge.cost

                if i == N - 1:
                    return True

    return False


N, M = list(map(int, input().split()))

abc = []

for i in range(M):
    a, b, c = list(map(int, input().split()))
    abc.append(Edge(a, b, -c))

if find_negative_loop():
    print('inf')
else:
    d = [float("inf") for i in range(N)]
    min_path(0)
    ans = -d[N - 1]
    print(ans)
