from operator import itemgetter

if __name__ == '__main__':
    N = int(input())
    red = [list(map(int, input().split())) for _ in range(N)]
    blue = [list(map(int, input().split())) for _ in range(N)]

    for i in range(N):
        ap = 0
        for j in range(N):
            b_x, b_y = blue[i]
            r_x, r_y = red[j]

            if b_x > r_x and b_y > r_y:
                ap += 1

        blue[i].append(ap)

    blue = sorted(blue, key=itemgetter(2))

    red = sorted(red, reverse=True, key=itemgetter(0))

    ans = 0

    for b2_x, b2_y, t in blue:
        del_flg = False
        for r_x, r_y in red:
            if r_x > b2_x:
                continue
            if r_y > b2_y:
                continue

            del_flg = True
            del_x = r_x
            del_y = r_y
            ans += 1
            break
        if del_flg:
            red.remove([del_x, del_y])

    print(ans)
