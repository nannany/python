import sys

if __name__ == '__main__':
    N = int(input())
    T, A = map(int, input().split())
    H = list(map(int, input().split()))

    ans = 0
    best = sys.maxsize
    for i in range(0, N):
        target = T - 0.006 * H[i] - A
        if abs(target) < best:
            best = abs(target)
            ans = i + 1

    print(ans)
