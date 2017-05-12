def compress(_x1, _x2, _w):
    xs = []

    for i in range(0, N):
        for d in range(-1, 2):
            tx1 = _x1[i] + d
            tx2 = _x2[i] + d
            if 1 <= tx1 <= _w:
                xs.append(tx1)
            if 1 <= tx2 <= _w:
                xs.append(tx2)

    xs = list(set(xs))
    xs.sort()

    # for i in range(0, N):


if __name__ == '__main__':
    W, H = list(map(int, input().split()))
    N = int(input())
    x1 = []
    x2 = []
    y1 = []
    y2 = []
    for i in range(0, N):
        inputs = list(map(int, input().split()))
        x1.append(inputs[0])
        x2.append(inputs[1])
        y1.append(inputs[2])
        y2.append(inputs[3])
