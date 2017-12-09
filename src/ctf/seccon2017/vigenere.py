import sys


# idx で指定した値でsの前後入れ替える
def _l(idx, s):
    return s[idx:] + s[:idx]


# pは SECCON{**************************}
# pは 34文字
# k1 は **************
# k2 は k1 を逆にしたもの
# k1,k2 は14文字
# 暗号は POR4dnyTLHBfwbxAAZhe}}ocZR3Cxcftw9
def main(p, k1, k2):
    # s は65文字
    s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz_{}"
    t = [[_l((i + j) % len(s), s) for j in range(len(s))] for i in range(len(s))]
    i1 = 0
    i2 = 0
    c = ""
    for a in p:
        c += t[s.find(a)][s.find(k1[i1])][s.find(k2[i2])]
        i1 = (i1 + 1) % len(k1)
        i2 = (i2 + 1) % len(k2)
    return c


if __name__ == '__main__':
    s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz_{}"
    t = [[_l((i + j) % len(s), s) for j in range(len(s))] for i in range(len(s))]
    # for gyo in t:
    #     print(gyo)
    # argv1 = input()
    # argv2 = input()

    # ans = ""
    # # S が P になる時
    # combi_1_14 = []
    # for i in range(65):
    #     for j in range(65):
    #         if t[18][i][j] == "P":
    #             print("1番目と14番目の組み合わせ " + s[i] + ":" + s[j])
    #             combi_1_14.append((s[i], s[j]))
    #
    # for moji in s:
    #     for pair_1_14 in combi_1_14:
    #         if t[s.find(moji)][s.find(pair_1_14[0])][s.find(pair_1_14[1])] == "x":
    #             print("15番目、29番目のやつ " + moji + ":" + pair_1_14[0] + ":" + pair_1_14[1])
    #             ans += moji
    #
    # # E が O になる時
    # combi_2_13 = []
    # for i in range(65):
    #     for j in range(65):
    #         if t[4][i][j] == "O":
    #             print("2番目と13番目の組み合わせ " + s[i] + ":" + s[j])
    #             combi_2_13.append((s[i], s[j]))
    #
    # for moji in s:
    #     for pair_2_13 in combi_2_13:
    #         if t[s.find(moji)][s.find(pair_2_13[0])][s.find(pair_2_13[1])] == "A":
    #             print("15番目、29番目のやつ " + moji + ":" + pair_2_13[0] + ":" + pair_2_13[1])
    #
    # # C が O になる時
    # combi_2_13 = []
    # for i in range(65):
    #     for j in range(65):
    #         if t[4][i][j] == "O":
    #             print("2番目と13番目の組み合わせ " + s[i] + ":" + s[j])
    #             combi_2_13.append((s[i], s[j]))
    #
    # for moji in s:
    #     for pair_2_13 in combi_2_13:
    #         if t[s.find(moji)][s.find(pair_2_13[0])][s.find(pair_2_13[1])] == "A":
    #             print("15番目、29番目のやつ " + moji + ":" + pair_2_13[0] + ":" + pair_2_13[1])
    #
    # for i in range(65):
    #     for j in range(65):
    #         # 片方だけでも結果同じ
    #         if t[13][i][j] == "n" and t[64][i][j] == "9":
    #             print("組み合わせ " + s[i] + ":" + s[j])

    combi = []
    key = [("S", "P"), ("E", "O"), ("C", "R"), ("C", "4"), ("O", "n"), ("N", "n"), ("{", "y")]
    for hira_and_ango in key:
        tmp_combi = []
        for i in range(65):
            for j in range(65):
                tmp_num = s.find(hira_and_ango[0])
                if t[tmp_num][i][j] == hira_and_ango[1]:
                    tmp_combi.append((s[i], s[j]))

        combi.append(tmp_combi)
    print(combi)
    angos = "TLHBfwbxAAZhe}}ocZR3Cxcftw"
    ans = ""
    # 26は不明な平文文字数
    for i in range(26):
        tmp_combi = combi[i % 7]
        for moji in s:
            for target_pair in tmp_combi:
                if t[s.find(moji)][s.find(target_pair[0])][s.find(target_pair[1])] == angos[i]:
                    ans_moji = moji

        ans += ans_moji

    print("SECCON{" + ans + "}")
