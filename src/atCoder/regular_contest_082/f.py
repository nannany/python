if __name__ == '__main__':
    # 砂の合計量
    X = int(input())

    # ひっくり返す回数
    K = int(input())
    # ひっくり返す秒数
    r = list(map(int, input()))
    # クエリの個数
    Q = int(input())

    # r の制御のための変数
    j = 0
    sign = -1
    for i in range(Q):
        # t:時刻 a:初期に A に入っている砂の量
        t, a = list(map(int, input().split()))
        while j < K and r[j] < t:
