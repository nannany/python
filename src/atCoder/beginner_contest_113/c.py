if __name__ == '__main__':
    N, M = map(int, input().split())

    p_and_y = list()
    prefMap = {}
    for i in range(M):
        P, Y = map(int, input().split())

        p_and_y.append((P, Y))

        if P in prefMap:
            prefMap[P].append(Y)
        else:
            prefMap[P] = [Y]

    for shiList in prefMap.values():
        shiList.sort()

    for P, Y in p_and_y:
        left = str(P).zfill(6)

        right = prefMap[P].index(Y) + 1
        right = str(right).zfill(6)

        print(left + right)
