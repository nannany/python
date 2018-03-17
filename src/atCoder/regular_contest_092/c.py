from operator import itemgetter


def ret(red, blue):
    ans = 0
    for b_x, b_y in blue:
        del_flg = False
        for r_x, r_y in red:
            if r_x > b_x:
                continue
            if r_y > b_y:
                continue

            del_flg = True
            del_x = r_x
            del_y = r_y
            ans += 1
            break
        if del_flg:
            red.remove([del_x, del_y])

    return ans


if __name__ == '__main__':
    N = int(input())
    red = [list(map(int, input().split())) for _ in range(N)]
    blue = [list(map(int, input().split())) for _ in range(N)]

    red1 = sorted(red, reverse=True, key=itemgetter(0))
    blue1 = sorted(blue, key=itemgetter(0))

    ans_1 = ret(red1, blue1)

    red2 = sorted(red, reverse=True, key=itemgetter(1))
    blue2 = sorted(blue, key=itemgetter(1))

    ans_2 = ret(red2, blue2)

    print(max(ans_1, ans_2))
