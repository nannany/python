if __name__ == '__main__':
    N = int(input())
    a = list(map(int, input().split()))
    sunuke_sum = 0
    arai_sum = sum(a)
    ret = 2000000000
    for i in range(0, N - 1):
        sunuke_sum += a[i]
        arai_sum -= a[i]
        tmp_diff = abs(sunuke_sum - arai_sum)
        if tmp_diff < ret:
            ret = tmp_diff

    print(ret)
