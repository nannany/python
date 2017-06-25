class Edge:
    def __init__(self, u, v, cost):
        self.u = u
        self.v = v
        self.cost = cost
        # self.n = n


class Coordinate:
    def __init__(self, x, y, n):
        self.x = x
        self.y = y
        self.n = n

    def __repr__(self):
        return repr((self.x, self.y))


if __name__ == '__main__':
    N = int(input())
    x = []
    y = []
    Coordinates = []
    for i in range(0, N):
        tmp_x, tmp_y = list(map(int, input().split()))
        # x.append(tmp_x)
        # y.append(tmp_y)
        Coordinates.append(Coordinate(tmp_x, tmp_y, i))

    print(sorted(Coordinates, key=lambda coordinate: coordinate.y))

    sorted_by_x = sorted(Coordinates, key=lambda coordinate: coordinate.x)
    sorted_by_y = sorted(Coordinates, key=lambda coordinate: coordinate.y)

    Edges = []
    for i in range(0, N - 1):
        cost_x = min(abs(sorted_by_x[i].x - sorted_by_x[i + 1].x), abs(sorted_by_x[i].y - sorted_by_x[i + 1].y))
        Edges.append(Edge(sorted_by_x[i].n, sorted_by_x[i + 1].n, cost_x))
        cost_y = min(abs(sorted_by_y[i].x - sorted_by_y[i + 1].x), abs(sorted_by_y[i].y - sorted_by_y[i + 1].y))
        Edges.append(Edge(sorted_by_y[i].n, sorted_by_y[i + 1].n, cost_y))

