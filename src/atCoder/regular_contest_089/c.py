def main():
    N = int(input())
    b_t = 0
    b_x = 0
    b_y = 0
    flg = True
    for _ in range(N):
        a_t, a_x, a_y = map(int, input().split())
        spend_time = a_t - b_t
        distance = abs(a_x - b_x) + abs(a_y - b_y)
        if spend_time >= distance and (distance - spend_time) % 2 == 0:
            continue
        else:
            flg = False
            break

    if flg:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()
