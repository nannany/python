if __name__ == '__main__':
    N = int(input())
    D, X = map(int, input().split())
    A = [int(input()) for _ in range(N)]

    eat = 0
    for a in A:
        eat += 1
        eat += (D - 1) // a

    print(X + eat)
