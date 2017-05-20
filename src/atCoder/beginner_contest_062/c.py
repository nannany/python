def max_minus_min(_a, _b, _c):
    return max(_a, _b, _c) - min(_a, _b, _c)


H, W = list(map(int, input().split()))
# 横幅が必ず縦幅以上となるようにする
if W <= H:
    tmp = W
    W = H
    H = tmp

if W % 3 == 0 or H % 3 == 0:
    print(0)
else:
    # yoko_to_two1 = max_minus_min(
    #     int(H / 2) * (W - (int(W / 3) + 1)), (H - int(H / 2)) * (W - (int(W / 3) + 1)), ((int(W / 3) + 1) * H))
    # yoko_to_two2 = max_minus_min(
    #     int(H / 2) * (W - (int(W / 3))), (H - int(H / 2)) * (W - (int(W / 3))), ((int(W / 3)) * H))
    # yoko_to_two3 = max_minus_min(
    #     (int(H / 2) + 1) * (W - (int(W / 3) + 1)), (H - (int(H / 2) + 1)) * (W - (int(W / 3) + 1)),
    #     ((int(W / 3) + 1) * H))
    # yoko_to_two4 = max_minus_min(
    #     (int(H / 2) + 1) * (W - (int(W / 3))), (H - (int(H / 2) + 1)) * (W - (int(W / 3))), ((int(W / 3)) * H))
    #
    # tate_to_two1 = max_minus_min(int(W / 2) * (H - (int(H / 3) + 1)), (W - int(W / 2)) * (H - (int(H / 3) + 1)),
    #                              ((int(H / 3) + 1) * W))
    # tate_to_two2 = max_minus_min(int(W / 2) * (H - (int(H / 3))), (W - int(W / 2)) * (H - (int(H / 3))),
    #                              ((int(H / 3)) * W))
    # tate_to_two3 = max_minus_min((int(W / 2) + 1) * (H - (int(H / 3) + 1)),
    #                              (W - (int(W / 2) + 1)) * (H - (int(H / 3) + 1)),
    #                              ((int(H / 3) + 1) * W))
    # tate_to_two4 = max_minus_min((int(W / 2) + 1) * (H - (int(H / 3))), (W - (int(W / 2) + 1)) * (H - (int(H / 3))),
    #                              ((int(H / 3)) * W))
    #
    # print(min(yoko_to_two1, yoko_to_two2, yoko_to_two3, yoko_to_two4, tate_to_two1, tate_to_two2, tate_to_two3,
    #           tate_to_two4))
    if i in range(1,H):
