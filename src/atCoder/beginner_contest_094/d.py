if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))

    l = max(a)
    r = 0
    best = l / 2
    for target in a:
        if abs(best - r) >= abs(best - target):
            r = target

    print(str(l) + " " + str(r))
