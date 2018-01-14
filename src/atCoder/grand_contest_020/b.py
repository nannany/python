if __name__ == '__main__':
    K = int(input())
    A = list(map(int, input().split()))

    A_rev = reversed(A)

    # min
    min_target_nums = [2]
    for i, a in enumerate(A_rev):
        if i == 0 and a != 2:
            print(-1)
            exit()

        targets = [_ for _ in min_target_nums if _ % a == 0]
        if len(targets) == 0:
            print(-1)
            exit()
        target = min(targets)

        min_target_nums = [_ for _ in range(a)]
        min_target_nums = list(map(lambda x: x + target, min_target_nums))

    # max
    max_target_nums = [2]
    for i, a in enumerate(A_rev):
        if i == 0 and a != 2:
            print(-1)
            exit()

        targets = [_ for _ in max_target_nums if _ % a == 0]
        if len(targets) == 0:
            print(-1)
            exit()
        target = max(targets)

        max_target_nums = [_ for _ in range(a)]
        max_target_nums = list(map(lambda x: x + target, max_target_nums))

    print(str(min(min_target_nums)) + " " + str(max(max_target_nums)))
