if __name__ == '__main__':
    N, M = map(int, input().split())
    G = [[] for _ in range(N+1)]
    for i in range(M):
        a, b = map(int, input().split())
        G[a].append(b)
        G[b].append(a)

    