def gcd(_a, _b):
    if _b == 0:
        return _a
    return gcd(_b, _a % _b)


if __name__ == '__main__':
    N, K = list(map(int, input().split()))
    A = list(map(int, input().split()))

    if max(A) < K:
        print("IMPOSSIBLE")
    elif K in A:
        print("POSSIBLE")
    else:
        tmp = -1
        min_value = min(A)
        for i in range(0, N):
            tmp = gcd(min_value, A[i])
            if tmp == 1:
                break
        if tmp == 1:
            print("POSSIBLE")
        elif K % tmp == 0:
            print("POSSIBLE")
        else:
            print("IMPOSSIBLE")
