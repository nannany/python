if __name__ == '__main__':
    quarter, half, single, double = list(map(int, input().split()))
    N = int(input())
    new_single = min(4 * quarter, 2 * half, single)
    new_double = min(2 * new_single, double)

    if N % 2 == 1:
        print(new_double * (N // 2) + new_single)
    else:
        print(new_double * (N // 2))
