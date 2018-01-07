if __name__ == '__main__':
    N, Y = map(int, input().split())

    target = 10000 * N - Y

    ans_x = -1
    ans_y = -1
    for x in range(0, N + 1):
        y = 0
        while x + y <= N:
            if 9000 * x + 5000 * y == target:
                ans_x = x
                ans_y = y
                break
            y += 1

    if ans_x != -1:
        print(str(N - ans_x - ans_y) + ' ' + str(ans_y) + ' ' + str(ans_x))
    else:
        print("-1 -1 -1")
