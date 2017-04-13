def solve(_dp, _v):
    for k in range(0, _v + 1):
        for i in range(0, _v + 1):
            for j in range(0, _v + 1):
                _dp[i][j] = min(_dp[i][j], _dp[i][k] + _dp[k][j])

    return _dp


if __name__ == '__main__':
    while True:
        n = int(input())
        if n == 0: break
        dp = [[100000] * 10 for i in range(10)]
        v = 0
        for i in range(0, n):
            dp[i][i] = 0
            inputs = list(map(int, input().split()))
            dp[inputs[0]][inputs[1]] = inputs[2]
            dp[inputs[1]][inputs[0]] = inputs[2]
            if v < inputs[0]:
                v = inputs[0]
            if v < inputs[1]:
                v = inputs[1]

        dp = solve(dp, v)
        ans_town = 0
        ans_dis = float("inf")
        for i in range(0, v + 1):
            tmp_sum = 0
            for j in range(0, v + 1):
                tmp_sum += dp[i][j]
            if tmp_sum < ans_dis:
                ans_dis = tmp_sum
                ans_town = i

        print(str(ans_town) + " " + str(ans_dis))
