if __name__ == '__main__':
    N = int(input())
    K = int(input())
    x = list(map(int, input().split()))
    sum_half = 0
    for tmp_x in x:
        sum_half += min(tmp_x, K - tmp_x)

    print(sum_half * 2)
