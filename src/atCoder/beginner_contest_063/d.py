import math


def C(_mid):
    tmp = [x - B * _mid for x in h]
    explode_count = 0
    for i in range(0, len(tmp)):
        if tmp[i] <= 0:
            pass
        else:
            explode_count += math.ceil(tmp[i] / (A - B))

    if _mid < explode_count:
        return True
    else:
        return False


if __name__ == '__main__':
    N, A, B = list(map(int, input().split()))

    h = [int(input()) for i in range(N)]

    lb = 0
    ub = 1000000000
    while ub - lb > 1:
        mid = int((lb + ub) / 2)
        if C(mid):
            lb = mid
        else:
            ub = mid

    print(ub)
