import itertools
import bisect

if __name__ == '__main__':
    N, M = map(int, input().split())
    points = [int(input()) for _ in range(N)]

    points.append(0)

    half = set()
    for i, j in itertools.product(points, repeat=2):
        half.add(i + j)

    half_set = sorted(list(half))

    ans = 0
    for target in half_set:
        if M - target < 0:
            break
        tmp = bisect.bisect_right(half_set, M - target)
        if target + half_set[tmp-1] > ans:
            ans = target + half_set[tmp-1]

    print(ans)