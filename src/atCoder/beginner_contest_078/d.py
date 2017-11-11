if __name__ == '__main__':
    N, Z, W = map(int, input().split())
    a = list(map(int, input().split()))

    if N == 1:
        print(abs(W - a[-1]))
    else:
        print(max(abs(W - a[-1]), abs(a[-2] - a[-1])))
