if __name__ == '__main__':
    N, M, K = list(map(int, input().split()))

    ans = "No"
    for kn in range(0, N + 1):
        for km in range(0, M + 1):
            # print(M * kn + N * km - (km * kn))
            if M * kn + N * km - 2 * (km * kn) == K:
                ans = "Yes"

    print(ans)
