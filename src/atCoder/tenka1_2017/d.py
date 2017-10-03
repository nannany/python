import math

if __name__ == '__main__':
    N, K = list(map(int, input().split()))
    integer_value = []
    for i in range(N):
        integer, value = list(map(int, input().split()))
        integer_value.append((integer, value))
    if K == 0:
        r = 0
    else:
        r = int(math.log(K, 2))
    max_value = 0
    for i in range(r + 1):
        # print((K >> i) & 0b1)
        if not ((K >> i) & 0b1):
            continue

        tmp_sum = 0

        mask = 1
        for j in range(i):
            mask = (mask << 1) + 1
        Ki = (K | mask) - 2 ** i

        for tmp_int, tmp_val in integer_value:
            if Ki | tmp_int == Ki:
                tmp_sum += tmp_val

        # print(str(tmp_sum) + " " + str(i))
        if max_value < tmp_sum:
            max_value = tmp_sum

    # K の場合
    K_val = 0
    for tmp_int, tmp_val in integer_value:
        if K | tmp_int == K:
            K_val += tmp_val
    # print("max_val" + str(max_value))
    # print("K_val" + str(K_val))
    if K_val < max_value:
        print(max_value)
    else:
        print(K_val)
