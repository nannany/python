if __name__ == '__main__':
    N, M = list(map(int, input().split()))
    A = []
    for i in range(N):
        A.append(list(map(int, input().split())))

    ans = float("inf")
    while len(A[0]) != 0:
        count_list = [0 for i in range(M + 1)]
        for i in range(0, N):
            count_list[A[i][0]] += 1

        max_value = max(count_list)
        for i in range(0, N):
            A[i].remove(count_list.index(max_value))

        if ans > max_value:
            ans = max_value

    print(ans)
