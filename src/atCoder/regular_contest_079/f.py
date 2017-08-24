from collections import defaultdict
import heapq as hq


# nから出ている辺の先の頂点の値を除く、最小の数と2番目に小さい値を返す。
def helper(n):
    q = child_L[n]
    del child_L[n]

    hq.heapify(q)
    i = 0
    while q:
        t = hq.heappop(q)
        if i < t:
            break
        else:
            i += (i == t)

    j = i + 1
    while q:
        t = hq.heappop(q)
        if j < t:
            break
        else:
            j += (j == t)

    return (i, j)


if __name__ == '__main__':

    N = int(input())
    P = list(map(lambda x: int(x) - 1, input().split()))
    # D:出している辺の本数
    D = [0] * N
    for p in P:
        D[p] += 1
    # print(D)
    child_L = defaultdict(list)
    # S:辺を出してないものリスト
    S = [p for p in range(N) if D[p] == 0]

    # 各頂点に持たせる値
    L = [None] * N

    # Dに閉路のみ残すようにする。
    while S:
        # print(child_L)
        n = S.pop()

        q = child_L[n]
        # print(q)
        del child_L[n]

        # listのqをヒープキューに変換
        hq.heapify(q)
        i = 0
        while q:
            t = hq.heappop(q)
            if i < t:
                break
            else:
                i += (i == t)

        L[n] = i
        # print(L)
        m = P[n]
        # print("m:" + str(m))
        child_L[m].append(i)
        D[m] -= 1
        if D[m] == 0:
            S.append(m)

    # print(D)
    # cycle check
    try:
        start = D.index(1)
    except ValueError:
        print('POSSIBLE')
        exit()

    s1, s2 = helper(start)
    G = []
    n = P[start]
    # 閉路に関して、それぞれの頂点で（最小の数、2番目に小さい数） を G に入れていく。
    while n != start:
        G.append(helper(n))
        n = P[n]

    # 可能な初期値をそれぞれシミュレート
    # grundy数と仮定した場合。一周まわって、向き先がその値でなければよい。
    n = s1
    for g in G:
        if g[0] == n:
            n = g[1]
        else:
            n = g[0]
    if n != s1:
        print('POSSIBLE')
        exit()

    # 2番目に小さい数と仮定した場合。一周まわって、向き先がgrundy数であればよい。
    n = s2
    for g in G:
        if g[0] == n:
            n = g[1]
        else:
            n = g[0]
    if n == s1:
        print('POSSIBLE')
        exit()

    print('IMPOSSIBLE')
