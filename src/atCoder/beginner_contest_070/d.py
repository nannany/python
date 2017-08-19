def dfs(v, p, d):
    distance[v] = d
    for tmp in G[v]:
        if tmp[0] == p:
            continue
        dfs(tmp[0], v, d + tmp[1])


if __name__ == '__main__':
    N = int(input())
    G = [[] for i in range(N)]
    for i in range(N - 1):
        # print(G)
        a, b, c = list(map(int, input().split()))
        a -= 1
        b -= 1
        G[a].append((b, c))
        G[b].append((a, c))

    Q, K = list(map(int, input().split()))
    distance = [-1 for i in range(N)]
    K -= 1
    dfs(K, -1, 0)
    for i in range(Q):
        x, y = list(map(int, input().split()))
        x -= 1
        y -= 1
        print(distance[x] + distance[y])
