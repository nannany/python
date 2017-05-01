import sys
import queue

if __name__ == '__main__':
    T = int(input())
    for caseNo in range(1, T + 1):
        P, Q = list(map(int, input().split()))
        A = list(map(int, input().split()))
        A.insert(0, 0)
        A.append(P + 1)

        dp = [[100000000 for i in range(0, Q + 2)] for j in range(Q + 1)]
        for i in range(0, Q + 1):
            dp[i][i + 1] = 0

        for w in range(2, Q + 2):
            for i in range(0, Q - w + 2):
                j = i + w
                t = 100000000
                for k in range(i + 1, j):
                    t = min(t, dp[i][k] + dp[k][j])

                dp[i][j] = t + A[j] - A[i] - 2

        print("Case #" + str(caseNo) + ": " + str(dp[0][Q + 1]))
