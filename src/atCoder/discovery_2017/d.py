if __name__ == '__main__':
    H, W = map(int, input().split())
    A, B = map(int, input().split())
    m = [list(input()) for i in range(H)]

    mh = [[0] * W for i in range(H)]
    mw = [[0] * W for i in range(H)]
    m4 = [[0] * W for i in range(H)]

    # mhに南北対称なものマーク
    for i in range(H):
        for j in range(W):
            if m[i][j] == "S" and m[H - (i + 1)][j] == "S":
                mh[i][j] = mh[H - (i + 1)][j] = 1
    # mwに東西対称なものマーク
    for i in range(H):
        for j in range(W):
            if m[i][j] == "S" and m[i][W - (j + 1)] == "S":
                mw[i][j] = mw[i][W - (j + 1)] = 1
    # m4に東西南北対称なものマーク
    for i in range(H):
        for j in range(W):
            if mh[i][j] == "S" and mh[i][W - (j + 1)] == "S":
                m4[i][j] = m4[i][W - (j + 1)] = m4[H - (i + 1)][j] = m4[H - (i + 1)][W - (j + 1)] = 1

    m4sum = sum(map(sum, m4)) // 4
    mhsum = sum(map(sum, mh)) // 2 - m4sum
    mwsum = sum(map(sum, mw)) // 2 - m4sum

    ans = 0

    ans += max(mhsum * A, mwsum * B)

    ans += m4sum * (max(A, B) + A + B)

    ans += A + B

    msum = sum(map(sum, m))
    if msum == sum(map(sum, mh)) :
        ans -= A
    if msum == sum(map(sum, mh)) :