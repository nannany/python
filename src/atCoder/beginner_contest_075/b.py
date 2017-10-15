if __name__ == '__main__':
    H, W = map(int, input().split())
    S = [list(input()) for _ in range(H)]

    d = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
    for i in range(H):
        for j in range(W):
            if S[i][j] == "#":
                continue

            num = 0
            for x, y in d:
                if 0 <= i + x <= H - 1 and 0 <= j + y <= W - 1:
                    if S[i + x][j + y] == "#":
                        num += 1

            S[i][j] = num

    for strings in S:
        strings = map(str, strings)
        print("".join(strings))
