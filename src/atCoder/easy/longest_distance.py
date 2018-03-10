import itertools
import math


def calc_len(_x, _y):
    return math.sqrt((_x[0] - _y[0]) ** 2 + (_x[1] - _y[1]) ** 2)


if __name__ == '__main__':
    N = int(input())
    plots = [list(map(int, input().split())) for _ in range(N)]

    ans = 0
    for x, y in itertools.combinations(plots, r=2):
        tmp = calc_len(x, y)
        if tmp > ans:
            ans = tmp

    print(ans)
