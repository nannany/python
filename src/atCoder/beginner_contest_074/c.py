if __name__ == '__main__':
    A, B, C, D, E, F = list(map(int, input().split()))

    # A+B のアリエル値
    a_plus_b = set()
    for i in range(0, 31, A):
        for j in range(0, 31, B):
            if not (i == 0 and j == 0):
                if i + j <= 30:
                    a_plus_b.add(i + j)

    c_plus_d = set()
    for i in range(0, F, C):
        for j in range(0, F, D):
            if i + j <= F:
                c_plus_d.add(i + j)

    max_concent = -1
    ans_sum = 0
    ans_sugar = 0
    # print(c_plus_d)
    # print(a_plus_b)
    for cd in c_plus_d:
        for ab in a_plus_b:
            if cd <= E * ab and cd <= F - 100 * ab:
                if max_concent <= cd / ab:
                    max_concent = cd / ab
                    ans_sum = 100 * ab + cd
                    ans_sugar = cd

    print(str(ans_sum) + " " + str(ans_sugar))
