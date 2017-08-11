if __name__ == '__main__':
    N = int(input())
    MOD = 1e9 + 7
    memo = [-1 for i in range(N + 1)]
    memo[1] = 1
    sum_odd = 1
    sum_even = 0
    for i in range(2, N + 1):
        if i % 2 == 0:
            memo[i] = i * sum_odd % MOD
            sum_even += memo[i]
            sum_even %= MOD
        else:
            memo[i] = i * sum_even % MOD
            sum_odd += memo[i]
            sum_odd %= MOD

    print(int(memo[N]))
