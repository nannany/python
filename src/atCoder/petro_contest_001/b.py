if __name__ == '__main__':
    N = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    b_minus_a = [tmp_b - tmp_a for tmp_a, tmp_b in zip(a, b)]

    if 2 * -sum([_ for _ in b_minus_a if _ < 0]) <= sum([_ - 1 for _ in b_minus_a if _ > 1 and _ % 2 == 1]) + sum(
            [_ for _ in b_minus_a if _ > 1 and _ % 2 == 0]):
        print('Yes')
    else:
        print('No')
