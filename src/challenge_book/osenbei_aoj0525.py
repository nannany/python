def hantei(mask, pos):
    if mask & (1 << pos):
        return True
    else:
        return False


if __name__ == '__main__':
    while True:
        R, C = list(map(int, input().split()))
        if R == 0 and C == 0: break
        mesh = [list(map(int, input().split())) for i in range(R)]
        ans = 0
        for mask in range(0, (1 << R)):
            tmp_sum = [0 for i in range(C)]
            for pos in range(0, R):
                if hantei(mask, pos):
                    for i in range(0, C):
                        if mesh[pos][i] == 1:
                            tmp_sum[i] += 1
                else:
                    for i in range(0, C):
                        if mesh[pos][i] == 0:
                            tmp_sum[i] += 1
            tmp_ans = 0
            for i in range(0, C):
                if tmp_sum[i] < R / 2:
                    tmp_ans += R - tmp_sum[i]
                else:
                    tmp_ans += tmp_sum[i]
            ans = max([ans, tmp_ans])
        print(ans)
