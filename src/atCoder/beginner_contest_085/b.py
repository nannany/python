if __name__ == '__main__':
    N = int(input())
    d = [int(input()) for _ in range(N)]
    ans = len(set(d))
    print(ans)
