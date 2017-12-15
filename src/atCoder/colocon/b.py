if __name__ == '__main__':
    N, X = map(int, input().split())
    S = input()
    T = [int(input()) for _ in range(N)]

    ans = 0
    for i in range(N):
        if S[i] == '0':
            ans += T[i]
        else:
            if T[i] < X:
                ans += T[i]
            else:
                ans += X

    print(ans)
