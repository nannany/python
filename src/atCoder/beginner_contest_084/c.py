if __name__ == '__main__':
    N = int(input())
    C = []
    S = []
    F = []
    for _ in range(N - 1):
        c, s, f = map(int, input().split())
        C.append(c)
        S.append(s)
        F.append(f)

    ans_list = []

    for i in range(N - 1):
        tmp_ans = 0
        while i < N - 1:
            if tmp_ans <= S[i]:
                tmp_ans = S[i] + C[i]
            else:
                if tmp_ans % F[i] != 0:
                    tmp_ans += F[i] - (tmp_ans % F[i])
                tmp_ans += C[i]

            i += 1

        ans_list.append(tmp_ans)

    # print(ans_list)
    ans_list.append(0)
    for answer in ans_list:
        print(answer)
