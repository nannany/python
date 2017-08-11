if __name__ == '__main__':
    N = int(input())

    sum_odd = 1
    sum_even = 0
    for i in range(2, N + 1):
        if i % 2 == 0:
            sum_even += sum_odd * i
        else:
            sum_odd += sum_even * i

    if N % 2 == 0:
        print((sum_odd * N) % 1000000007)
    elif N == 1:
        print(1)
    else:
        print((sum_even * N) % 1000000007)
