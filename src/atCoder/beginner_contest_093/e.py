if __name__ == '__main__':
    N = int(input())
    A = []
    B = []
    ans = 0
    for _ in range(N):
        a, b = map(int, input().split())
        if a < b:
            ans += b
        A.append(a)
        B.append(b)

    print(ans)
