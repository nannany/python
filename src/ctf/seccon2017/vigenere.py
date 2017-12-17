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

    combi = []
    key = [("S", "P"), ("E", "O"), ("C", "R"), ("C", "4"), ("O", "d"), ("N", "n"), ("{", "y")]
    for hira_and_ango in key:
        tmp_combi = []
        for i in range(65):
            for j in range(65):
                tmp_num = s.find(hira_and_ango[0])
                if t[tmp_num][i][j] == hira_and_ango[1]:
                    tmp_combi.append((s[i], s[j]))

        combi.append(tmp_combi)
    add_combi = []
    for i in range(7):
        add_combi.append(combi[-(i + 1)])
    for tmp_add in add_combi:
        combi.append(tmp_add)
    print(combi)
    angos = "POR4dnyTLHBfwbxAAZhe}}ocZR3Cxcftw9"
    ans = ""
    # 26は不明な平文文字数
    for i in range(7,33):
        tmp_combi = combi[i % 14]
        for moji in s:
            for target_pair in tmp_combi:
                if t[s.find(moji)][s.find(target_pair[0])][s.find(target_pair[1])] == angos[i]:
                    ans_moji = moji

        ans += ans_moji

    print("SECCON{" + ans + "}")

