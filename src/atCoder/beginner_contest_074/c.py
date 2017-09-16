if __name__ == '__main__':
    A, B, C, D, E, F = list(map(int, input().split()))
    M = []
    # A
    for a_ in range(0, 31):
        # B
        for b_ in range(0, 31):
            # C
            for c_ in range(0, 31):
                # D
                for d_ in range(0, 31):
                    if (c_ + d_) <= E * (a_ + b_) and 100 * (a_ + b_) + c_ + d_ <= F:
                        if not (a_ == 0 and b_ == 0):
                            M.append((a_, b_, c_, d_))
                    else:
                        break
    print(M)
    max_concent = 0
    for a, b, c, d in M:
        if max_concent < (c + d) / (a + b):
            ans = (a, b, c, d)
            max_concent = (c + d) / (a + b)

    sum_g = 100 * (ans[0] + ans[1]) + ans[2] + ans[3]
    print(ans)
    sugar_g = ans[2] + ans[3]

    print(str(sum_g) + " " + str(sugar_g))
