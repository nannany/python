from collections import deque
import copy


def C(_mid):
    if _mid < len(L) and L[_mid] <= K:
        return True
    else:
        return False


T = int(input())
for i in range(T):
    N, Q = list(map(int, input().split()))
    L = list(map(int, input().split()))
    L.sort()

    for j in range(Q):
        K = int(input())
        ans = 0

        lb = 0
        ub = 1000000000

        while ub - lb > 1:
            mid = int((ub + lb) / 2)
            if C(mid):
                lb = mid
            else:
                ub = mid

        ans += len(L) - (lb + 1)

        que = deque()
        for k in range(0, lb + 1):
            que.append(L[k])

        while len(que) != 0:
            eater = que.pop()
            eat_count = K - eater
            if len(que) < eat_count:
                break

            ans += 1
            for k in range(eat_count):
                que.popleft()

        print(ans)
