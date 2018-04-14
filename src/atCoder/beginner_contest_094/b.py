if __name__ == '__main__':
    N, M, X = map(int, input().split())
    A = list(map(int, input().split()))

    for i in range(M):
        if A[i] > X:
            pos = i
            break
        else:
            pos = M

    print(min(pos, M - pos))
