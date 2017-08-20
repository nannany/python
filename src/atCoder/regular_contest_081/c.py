if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))

    A.sort(reverse=True)

    v = []
    while len(A) > 1:
        if len(v) == 2:
            break

        if A[0] == A[1]:
            v.append(A[0])
            A.pop(0)
            A.pop(0)
        else:
            A.pop(0)

    if len(v) == 1 or len(v) == 0:
        print(0)
    else:
        print(v[0] * v[1])
