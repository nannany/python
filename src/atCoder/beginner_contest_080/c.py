import itertools

if __name__ == '__main__':
    N = int(input())
    F = [list(map(int, input().split())) for _ in range(N)]
    P = [list(map(int, input().split())) for _ in range(N)]

    # print(list(itertools.product(range(2), repeat=10)))

    max1 = -float('inf')
    max2 = -float('inf')

    for target in list(itertools.product(range(2), repeat=10)):
        sum_every_shop = 0
        for i in range(N):
            sum_same_time = 0
            for j in range(10):
                if target[j] == 1 and F[i][j] == 1:
                    sum_same_time += 1

            sum_every_shop += P[i][sum_same_time]

        if max2 < sum_every_shop:
            max2 = sum_every_shop

        if max1 < max2:
            max1, max2 = max2, max1
            result_target = target

    if result_target == (0, 0, 0, 0, 0, 0, 0, 0, 0, 0):
        print(max2)
    else:
        print(max1)
