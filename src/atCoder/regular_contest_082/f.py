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
    a:傾き始め
    b:傾き終わり
    c:切片
    '''
    a = 0
    b = X
    c = 0
    # 出入りする砂の量
    sand_quantity = [r[0]]
    for i in range(1, K):
        sand_quantity.append(r[i] - r[i - 1])

    for i in range(Q):
        # t:時刻 a:初期に A に入っている砂の量
        t, ini_sand = list(map(int, input().split()))
        while j < K and r[j] < t:
            c += sign * sand_quantity[j]
            c = max(min(c, X), -X)
            # aについて更新
            if a < -c:
                a = -c
            # bについて更新
            if X - c < b:
                b = X - c

            j += 1
            sign *= -1

        if j == 0:
            tmp_time = t
        else:
            tmp_time = t - r[j - 1]

        if ini_sand < a:
            print(max(min(a + c + tmp_time * sign, X), 0))
        elif ini_sand < b:
            print(max(min(ini_sand + c + tmp_time * sign, X), 0))
        else:
            print(max(min(b + c + tmp_time * sign, X), 0))

            # print("a:" + str(a) + " b:" + str(b) + " c:" + str(c))
