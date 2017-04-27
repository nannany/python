if __name__ == '__main__':
    T = int(input())
    for i in range(0, T):
        n = int(input())
        x = list(map(int, input().split()))
        y = list(map(int, input().split()))
        x = sorted(x)
        y = sorted(y, reverse=True)
        ans = 0
        for j in range(0, n):
            ans += x[j] * y[j]

        print("Case #" + str(i + 1) + ": " + str(ans))
