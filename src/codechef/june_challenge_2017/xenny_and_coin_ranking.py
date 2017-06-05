if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        U, V = list(map(int, input().split()))
        n = U + V

        ans = int(int(int(int(n) * int(n + 1)) / 2) + int(U)) + 1
        print(ans)
