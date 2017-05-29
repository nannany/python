import math


def C(_mid):
    c1 = sum([abs(x - _mid) for x in S])
    c2 = sum([abs(x - (_mid + 1)) for x in S])
    if c1 < c2:
        return False
    else:
        return True


if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        N, L, A, B = list(map(int, input().split()))
        S = list(map(int, input().split()))
        S.sort()

        lb = 0
        ub = 1000000000
        while ub - lb > 1:
            mid = int((ub + lb) / 2)
            if C(mid):
                lb = mid
            else:
                ub = mid

        lower_limit = ub - math.ceil(N * L / 2)
        upper_limit = ub + math.ceil(N * L / 2)

        if lower_limit < A:
            upper_limit += A - lower_limit
            lower_limit = A

        if B < upper_limit:
            lower_limit -= upper_limit - B
            upper_limit = B

        print(str(lower_limit) + " " + str(upper_limit))

        ans = 0
        for j in range(0, N):
            ans += abs((lower_limit + L * j) - S[j])

        print(ans)
