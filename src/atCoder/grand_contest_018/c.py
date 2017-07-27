import heapq

if __name__ == '__main__':
    X, Y, Z = list(map(int, input().split()))
    A = []
    B = []
    C = []
    N = X + Y + Z
    for i in range(N):
        tmp_a, tmp_b, tmp_c = list(map(int, input().split()))
        A.append(tmp_a)
        B.append(tmp_b)
        C.append(tmp_c)

    gold_minus_silver = [(a - b, a, b, c) for (a, b, c) in zip(A, B, C)]
    gold_minus_silver.sort()
    print(gold_minus_silver)

    left_side = []
    ans = 0
    for i in range(0, Y):
        heapq.heappush(left_side, (
            gold_minus_silver[i][2] - gold_minus_silver[i][3], gold_minus_silver[i][2], gold_minus_silver[i][3]))

    left_max = [0 for i in range(Z)]

    for K in range(Y, Y + Z + 1):

    right_side = []
    for i in range(Y, N):
        heapq.heappush(right_side, gold_minus_silver[i][1] - gold_minus_silver[i][3], gold_minus_silver[i][1],
                       gold_minus_silver[i][3])
