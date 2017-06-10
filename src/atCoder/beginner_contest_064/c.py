if __name__ == '__main__':
    N = int(input())
    a = list(map(int, input().split()))

    # 0:gray 1:brown 2:green ...... 7:red
    colors_count = [0 for i in range(8)]
    super_count = 0
    for score in a:
        if int(score / 400) == 0:
            colors_count[0] += 1
        elif int(score / 400) == 1:
            colors_count[1] += 1
        elif int(score / 400) == 2:
            colors_count[2] += 1
        elif int(score / 400) == 3:
            colors_count[3] += 1
        elif int(score / 400) == 4:
            colors_count[4] += 1
        elif int(score / 400) == 5:
            colors_count[5] += 1
        elif int(score / 400) == 6:
            colors_count[6] += 1
        elif int(score / 400) == 7:
            colors_count[7] += 1
        else:
            super_count += 1

    # print(colors_count)

    # colors_count で0ではないとこの数
    not_zero_count = 0
    for num in colors_count:
        if num != 0:
            not_zero_count += 1

    if not_zero_count == 0:
        ans_min = 1
        # ans_max = super_count if super_count <= 8 else 8
        ans_max = super_count
    else:
        ans_min = not_zero_count
        # ans_max = not_zero_count + super_count if (not_zero_count + super_count) <= 8 else 8
        ans_max = not_zero_count + super_count

    print(str(ans_min) + ' ' + str(ans_max))
