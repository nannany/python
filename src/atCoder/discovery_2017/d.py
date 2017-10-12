if __name__ == '__main__':
    H, W = map(int, input().split())
    A, B = map(int, input().split())
    m = [[0] * W for i in range(H)]
    for i in range(H):
        tmp = input()
        for j in range(W):
            if tmp[j] == "S":
                m[i][j] = 1
    mh = [[0] * W for i in range(H)]
    mw = [[0] * W for i in range(H)]
    m4 = [[0] * W for i in range(H)]

    # mhに南北対称なものマーク
    for i in range(H):
        for j in range(W):
            if m[i][j] & m[H - (i + 1)][j] == 1:
                mh[i][j] = mh[H - (i + 1)][j] = 1
    # mwに東西対称なものマーク
    for i in range(H):
        for j in range(W):
            if m[i][j] & m[i][W - (j + 1)] == 1:
                mw[i][j] = mw[i][W - (j + 1)] = 1
    # m4に東西南北対称なものマーク
    for i in range(H):
        for j in range(W):
            if mh[i][j] & mh[i][W - (j + 1)] == 1:
                m4[i][j] = m4[i][W - (j + 1)] = 1

    m4sum = sum(map(sum, m4))
    mhsum = sum(map(sum, mh)) - m4sum
    mwsum = sum(map(sum, mw)) - m4sum

    ans = 0

    ans += max(mhsum // 2 * A + m4sum // 4 * (max(A, B) + A + B), mwsum // 2 * B + m4sum // 4 * (max(A, B) + A + B))
    ans += A + B

    msum = sum(map(sum, m))
    if msum == sum(map(sum, mh)):
        ans -= A
    if msum == sum(map(sum, mw)):
        ans -= B

    print(ans)
