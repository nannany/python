if __name__ == '__main__':
    N = int(input())
    a = 0
    for i in range(N):
        tmp_a, tmp_b = list(map(int, input().split()))
        if a < tmp_a:
            a = tmp_a
            b = tmp_b

    print(a + b)
