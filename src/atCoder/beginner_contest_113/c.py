if __name__ == '__main__':
    N, M = map(int, input().split())

    ans = [None] * M
    prefMap = {}
    for i in range(M):
        P, Y = map(int, input().split())

        if P in prefMap:
            prefMap[P].append((Y, i))
        else:
            prefMap[P] = [(Y, i)]

    for P, L in prefMap.items():
        L.sort()

        for j, (y, i) in enumerate(L):
            ans[i] = str(P).zfill(6) + str(j + 1).zfill(6)

    print("\n".join(ans))
