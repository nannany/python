if __name__ == '__main__':
    N, M = map(int, input().split())
    # 初項 *　1/(1-r)**2
    shoko = (1900 * M + 100 * (N - M)) / (2 ** M)
    r = (2 ** M - 1) / (2 ** M)

    # print(shoko)
    # print(r)
    print(int(shoko / ((1 - r) ** 2)))
