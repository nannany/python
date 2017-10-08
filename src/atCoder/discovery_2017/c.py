from collections import deque

if __name__ == '__main__':
    N, C = list(map(int, input().split()))
    L = [int(input()) for i in range(N)]
    L.sort()

    d = deque(L)
    ans = 0
    while len(d) != 0:
        tmp_max = d.pop()
        if len(d) != 0 and tmp_max + d[0] + 1 <= C:
            d.popleft()

        ans += 1

    print(ans)