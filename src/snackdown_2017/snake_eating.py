from collections import deque
import copy

T = int(input())
for i in range(T):
    N, Q = list(map(int, input().split()))
    L = list(map(int, input().split()))
    L.sort()

    for j in range(Q):
        K = int(input())
        target = copy.deepcopy(L)
        ans = 0
        k = 0
        while True:
            if K <= target[k]:
                ans += 1
                target.pop(k)
                if len(target) <= k:
                    break
            else:
                if len(target) - 1 == k:
                    break
                else:
                    k += 1

        que = deque()
        for num in target:
            que.append(num)

        while len(que) != 0:
            eater = que.pop()
            eat_count = K - eater
            if len(que) < eat_count:
                break

            ans += 1
            for k in range(eat_count):
                que.popleft()

        print(ans)
