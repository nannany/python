if __name__ == '__main__':
    # 砂の合計量
    X = int(input())

    # ひっくり返す回数
    K = int(input())
    # ひっくり返す秒数
    r = list(map(int, input().split()))
    # クエリの個数
    Q = int(input())

    # r の制御のための変数
    j = 0
    sign = -1
    '''
    ある時刻を切り取り、横軸を最初のAの砂の量、縦軸をその時の砂の量とする。
    s:傾き始め
    e:傾き終わり
    c:切片
    '''
    s = 0
    e = X
    c = 0
    # 出入りする砂の量
    sand_quantity = [r[0]]
    for i in range(1, K):
        sand_quantity.append(r[i] - r[i - 1])

    chasm_time = 0
    for i in range(Q):
        # t:時刻 a:初期に A に入っている砂の量
        t, a = list(map(int, input().split()))
        while j < K and r[j] < t:
            c += sign * sand_quantity[j]
            c = max(min(X, c), -X)
            # sについて更新
            if s < -c:
                s = -c
                if e < s:
                    s = e
            # eについて更新
            if X - c < e:
                e = X - c
                if e < s:
                    e = s
            chasm_time = r[j]
            j += 1
            sign *= -1

        tmp_time = t - chasm_time

        if a < s:
            print(max(min(s + c + tmp_time * sign, X), 0))
        elif a < e:
            print(max(min(a + c + tmp_time * sign, X), 0))
        else:
            print(max(min(e + c + tmp_time * sign, X), 0))

        # print("s:" + str(s) + " e:" + str(e) + " c:" + str(c) + " a:" + str(a))
