if __name__ == '__main__':
    K = int(input())
    N = 50
    plus_height = K / N
    modulo = K % N

    ans = [(i + plus_height) for i in range(N - 1, -1, -1)]

    for i in range(0, modulo):
        ans[i] += 1

    ans = list(map(lambda x: str(int(x)), ans))
    print(N)
    print(" ".join(ans))
