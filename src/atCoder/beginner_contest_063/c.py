if __name__ == '__main__':
    N = int(input())
    s = []
    for i in range(N):
        s.append(int(input()))

    not_10_multi = list(filter(lambda x: (x % 10) != 0, s))

    if sum(s) % 10 != 0:
        print(sum(s))
    elif len(not_10_multi) == 0:
        print(0)
    else:
        print(sum(s) - min(not_10_multi))
