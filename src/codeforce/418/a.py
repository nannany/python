if __name__ == '__main__':
    n, k = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ans = "No"
    if 2 <= k:
        ans = "Yes"
    else:
        for i in range(0, n):
            if a[i] == 0:
                a[i] = b[0]

        for i in range(0, n - 1):
            if a[i + 1] < a[i]:
                ans = "Yes"
                break

    print(ans)
