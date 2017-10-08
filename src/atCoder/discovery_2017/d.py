def get_reverse_count(i, j):
    ret = 0
    if m[i][j] == "S":
        ret += 1
    if m[H - (i + 1)][j] == "S":
        ret += 1
    if m[i][W - (j + 1)] == "S":
        ret += 1
    if m[H - (i + 1)][W - (j + 1)] == "S":
        ret += 1

    return ret


def judge_nanboku_tozai(i, j):
    if m[i][j] == "S" and m[H - (i + 1)][j] == "S":
        return "NS"
    elif m[i][W - (j + 1)] == "S" and m[H - (i + 1)][W - (j + 1)] == "S":
        return "NS"
    elif m[i][j] == "S" and m[i][W - (j + 1)] == "S":
        return "EW"
    elif m[H - (i + 1)][j] == "S" and m[H - (i + 1)][W - (j + 1)] == "S":
        return "EW"
    else:
        return "no"


if __name__ == '__main__':
    H, W = list(map(int, input().split()))
    A, B = list(map(int, input().split()))
    m = [list(input()) for i in range(H)]

    m_for_ans = [[0 for i in range(W // 2)] for j in range(H // 2)]

    A_con = 0
    B_con = 0
    for h in range(H // 2):
        for w in range(W // 2):
            m_for_ans[h][w] = get_reverse_count(h, w)
            if m_for_ans[h][w] == 2:
                if judge_nanboku_tozai(h, w) == "NS":
                    A_con += 1
                elif judge_nanboku_tozai(h, w) == "EW":
                    B_con += 1

    if A_con < B_con :
        print((A_con +  * A )
