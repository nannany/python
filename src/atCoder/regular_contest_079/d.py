if __name__ == '__main__':
    K = int(input())
    N = 50
    ans = [i for i in range(0, N)]

    modulo = K % N
    for i in range(0, modulo):
        ans[i] += N
        for j in range(0, N):
            if i != j:
                ans[j] -= 1

    divide = K // N

    ans = [str(divide + i) for i in ans]
    print(N)
    print(" ".join(ans))
