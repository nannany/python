if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    A.insert(0, 0)
    A.append(0)
    # print(A)
    sum_A = 0
    for i in range(N + 1):
        sum_A += abs(A[i + 1] - A[i])

    # print(sum_A)

    for i in range(1, N + 1):
        if A[i - 1] <= A[i] <= A[i + 1] or A[i + 1] <= A[i] <= A[i - 1]:
            print(sum_A)
            continue

        print(sum_A - (abs(A[i - 1] - A[i]) + abs(A[i] - A[i + 1]) - abs(A[i + 1] - A[i - 1])))
