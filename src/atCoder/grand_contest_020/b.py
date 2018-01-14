if __name__ == '__main__':
    K = int(input())
    A = list(map(int, input().split()))

    # min
    target_nums = [2]
    for a in reversed(A):
        targets = [_ for _ in target_nums if _ % a == 0]
        if len(targets) == 0:
            print(-1)
            exit()

        target_nums = []
        for target in targets:
            target_nums += [_ + target for _ in range(a)]

    print(str(min(target_nums)) + " " + str(max(target_nums)))
