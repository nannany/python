if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n = int(input())
        h = list(map(int, input().split()))
        L = [-1 for j in range(n)]
        L[0] = 1
        for j in range(1, n):
            if L[j - 1] + 1 <= h[j]:
                L[j] = L[j - 1] + 1
            else:
                L[j] = h[j]
        # print(L)

        R = [-1 for j in range(n)]
        R[n - 1] = 1

        for j in range(n - 2, -1, -1):
            if R[j + 1] + 1 <= h[j]:
                R[j] = R[j + 1] + 1
            else:
                R[j] = h[j]

        # print(R)
        height = 0
        for j in range(0, n):
            target_height = min(L[j], R[j])
            if height < target_height:
                height = target_height
                pos = j

        # print("h:" + str(height) + "pos:" + str(pos))
        ans = 0
        for j in range(0, n):
            if 0 < height - abs(pos - j):
                ans += h[j] - (height - abs(pos - j))
            else:
                ans += h[j]

        print(ans)
