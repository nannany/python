

if __name__ == '__main__':
    N = int(input())
    red = [list(map(int, input().split())) for _ in range(N)]
    blue = [list(map(int, input().split())) for _ in range(N)]

    red.sort(reverse=True)
    blue.sort()

    # print(red)
    # print(blue)
    ans_1 = 0
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
            ans_1 += 1
            break
        if del_flg:
            red.remove([del_x, del_y])

    ans_

    print(ans_1)