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

    gold_minus_silver = [a - b for a in A for b in B]


    left_side = []
    for i in range(0, Y):
        heappush(left_side, )
    right_side = []
    for K in range(Y, Y + Z + 1):
